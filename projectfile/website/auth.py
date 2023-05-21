from flask import Blueprint, render_template, request,redirect,url_for,flash
from .forms import LoginForm, RegisterForm
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User

#create a blueprint
authbp = Blueprint('auth', __name__ )

@authbp.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        uname = form.user_name.data
        new_user = User(
            name = uname,
            password_hash = generate_password_hash(form.password.data),
            emailid = form.email_id.data
        )
        #check if a user exists
        u1 = User.query.filter_by(name=uname).first()
        if u1:
            flash('User name already exists, please login')
            return redirect(url_for('auth.login'))
        # commit to database
        db.session.add(new_user)
        db.session.commit()
        flash('successfully registered user. Please login.')
        return redirect(url_for('auth.login'))
    return render_template('login.html', form=form)


@authbp.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    error=None
    if(login_form.validate_on_submit()==True):
        #get the username and password from the database
        user_name = login_form.user_name.data
        password = login_form.password.data
        u1 = User.query.filter_by(name=user_name).first()
        #if there is no user with that name
        if u1 is None:
            error='Incorrect user name'
        #check the password - notice password hash function
        elif not check_password_hash(u1.password_hash, password): # takes the hash and password
            error='Incorrect password'
        if error is None:
            #all good, set the login_user of flask_login to manage the user
            login_user(u1)
            return redirect(url_for('main.index'))
        else:
            flash(error)
    return render_template('login.html', form=login_form,  heading='Login')

@authbp.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('User successfully logged out.')
    return redirect(url_for("auth.login"))


