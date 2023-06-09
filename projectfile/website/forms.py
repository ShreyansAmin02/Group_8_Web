from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField, FileAllowed
from wtforms.fields import TextAreaField, SubmitField, StringField, TimeField, PasswordField, DateField, IntegerField
from wtforms.validators import InputRequired, Length, Email, EqualTo

ALLOWED_FILE = {'PNG', 'JPG', 'png', 'jpg'}

# Create new destination


class EventForm(FlaskForm):
    title = StringField('Event Title', validators=[InputRequired(), Length(
        min=3, max=30)], render_kw={"placeholder": "Enter Event Title"})
    artistName = StringField('Artist Name(s)', validators=[InputRequired(), Length(
        min=3, max=30)], render_kw={"placeholder": "Enter Artist Name(s)"})
    style = StringField('Style', validators=[InputRequired(), Length(
        min=3, max=30)], render_kw={"placeholder": "Enter Style"})
    address = StringField('Address', validators=[InputRequired(), Length(
        min=3)], render_kw={"placeholder": "Enter Address"})
    date = DateField('Date', validators=[InputRequired()])
    startTime = TimeField('Starts at', validators=[InputRequired()])
    endTime = TimeField('Ends at', validators=[InputRequired()])
    image = FileField('Event Image',
                      validators=[FileRequired(message='Image cannot be empty'),
                                  FileAllowed(
                                      ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')
                                  ])
    description = TextAreaField('Description',
                                validators=[InputRequired(), Length(min=3)], render_kw={"placeholder": "Enter Description:  "})
    tickets = IntegerField('Tickets', validators=[InputRequired()], render_kw={
        "placeholder": "Quantity of Tickets Available"})
    price = IntegerField('Price', validators=[InputRequired()], render_kw={
                         "placeholder": "Enter Price"})
    contactDetails = TextAreaField('Contact Details',
                                   validators=[InputRequired(), Length(min=3, max=100)], render_kw={"placeholder": "Enter Contact Details:  "})
    submit = SubmitField("Create")

# User login


class LoginForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired('Enter user name'), Length(
        min=3, max=30)], render_kw={"placeholder": "Enter your Username:  "})
    password = PasswordField("Password", validators=[InputRequired(
        'Enter user password')], render_kw={"placeholder": "Enter Your Password:  "})
    submit = SubmitField("Login")

# User register


class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired(), Length(
        min=3, max=30)], render_kw={"placeholder": "Enter your Username: "})
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email"), Length(
        min=3, max=200)], render_kw={"placeholder": "Enter your Email address:  "})

    # linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password", validators=[InputRequired(),
                                                     EqualTo('confirm', message="Passwords should match")], render_kw={"placeholder": "Enter Your Password:  "})
    confirm = PasswordField("Confirm Password", [InputRequired()], render_kw={
                            "placeholder": "Confirm Your Password:  "})
    # submit button
    submit = SubmitField("Register")

# User comment


class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()], render_kw={
                         "placeholder": "Leave a comment:  "})
    submit = SubmitField('Create')


class BookingForm(FlaskForm):
    type = TextAreaField(validators=[InputRequired()])
    amount = IntegerField(validators=[InputRequired()])
    submit = SubmitField('Book')

# edit


class EditFormButton(FlaskForm):
    submit = SubmitField('Edit Form Button')


class EditEventForm(FlaskForm):  # form for editing the event already created
    title = StringField('Event Title', validators=[InputRequired(), Length(
        min=3, max=30)], render_kw={"placeholder": "Enter Event Title"})
    artistName = StringField('Artist Name(s)', validators=[InputRequired(), Length(
        min=3, max=30)], render_kw={"placeholder": "Enter Artist Name(s)"})
    style = StringField('Style', validators=[InputRequired(), Length(
        min=3, max=30)], render_kw={"placeholder": "Enter Style"})
    address = StringField('Address', validators=[InputRequired(), Length(
        min=3)], render_kw={"placeholder": "Enter Address"})
    date = DateField('Date', validators=[InputRequired()])
    startTime = TimeField('Starts at', validators=[InputRequired()])
    endTime = TimeField('Ends at', validators=[InputRequired()])
    description = TextAreaField('Description',
                                validators=[InputRequired(), Length(min=3)], render_kw={"placeholder": "Enter Description:  "})
    tickets = IntegerField('Tickets', validators=[InputRequired()], render_kw={
        "placeholder": "Quantity of Tickets Available"})
    price = IntegerField('Price', validators=[InputRequired()], render_kw={
                         "placeholder": "Enter Price"})
    contactDetails = TextAreaField('Contact Details',
                                   validators=[InputRequired(), Length(min=3, max=100)], render_kw={"placeholder": "Enter Contact Details:  "})
    submit = SubmitField("Save")
