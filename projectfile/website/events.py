from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from .models import Comment, Event
from .forms import EventForm, CommentForm
import os
from werkzeug.utils import secure_filename
from . import db
from flask_login import login_required, current_user

# handles different destiantion pages

# a url prefix will refer to prefix for the url
eventsbp = Blueprint('events', __name__, url_prefix='/events')


# this will eventually be used to determine what destination is used
@eventsbp.route("/<id>", methods=['GET', 'POST'])
def show(id):  # not done yet
    try:
        event = Event.query.filter_by(id=id).first()
        cmtForm = CommentForm()
        if id == None:
            id = "events/create"
        return render_template("events/details.html", event=event, form=cmtForm)
    except:
        message = "Event was not found"
        return render_template("error.html", errorMessage=message)


@eventsbp.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    print('Method  type: ', request.method)
    eventForm = EventForm()
    if eventForm.validate_on_submit():
        db_file_path = check_upload_file(eventForm)
        event = Event(eventTitle=eventForm.title.data, style=eventForm.style.data, artistName=eventForm.artistName.data, address=eventForm.address.data, date=eventForm.date.data, image=db_file_path, startTime=eventForm.startTime.data, endTime=eventForm.endTime.data,
                      description=eventForm.description.data, tickets=eventForm.tickets.data,
                      price=eventForm.price.data, contactDetails=eventForm.contactDetails.data, user=current_user)
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('events.create'))

    flash('Successfully Created Event!')
    return render_template('events/create.html', form=eventForm)


def check_upload_file(form):
    fp = form.image.data
    filename = fp.filename
    BASE_PATH = os.path.dirname(__file__)
    upload_path = os.path.join(
        BASE_PATH, 'static/image', secure_filename(filename))
    db_upload_path = '/static/image/' + secure_filename(filename)
    fp.save(upload_path)
    return db_upload_path


@eventsbp.route('<id>/comment', methods=['GET', 'POST'])
@login_required
def comment(id):
    event_obj = Event.query.filter_by(id=id).first()
    # here the form is created form = CommentForm()
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(
            text=form.text.data,
            event=event_obj, user=current_user)
        db.session.add(comment)
        db.session.commit()
    return redirect(url_for('event.show', id=id))
