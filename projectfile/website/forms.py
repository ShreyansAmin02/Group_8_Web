from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField, FileAllowed
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo

ALLOWED_FILE={'PNG','JPG','png','jpg'}

#Create new destination
class DestinationForm(FlaskForm):
  name = StringField('Country', validators=[InputRequired(), Length(min=3, max=30)], render_kw={"placeholder": "Enter Planet and the City name: "})
  description = TextAreaField('Description', 
            validators=[InputRequired(), Length(min=3, max=100)], render_kw={"placeholder": "Enter Description:  "})
  image = FileField('Destination Image',
        validators=
        [FileRequired(message='Image cannot be empty'),
        FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')
        ])
  
  currency = StringField('Currency', validators=[InputRequired(), Length(min=3, max=10)], render_kw={"placeholder": "Enter Description:  "})
  submit = SubmitField("Create")
    
#User login
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name'), Length(min=3, max=30)], render_kw={"placeholder": "Enter your Username:  "})
    password=PasswordField("Password", validators=[InputRequired('Enter user password')], render_kw={"placeholder": "Enter Your Password:  "})
    submit = SubmitField("Login")

#User register
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired(), Length(min=3, max=30)], render_kw={"placeholder": "Enter your Username: "})
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email"), Length(min=3, max=200)], render_kw={"placeholder": "Enter your Email address:  "})
    
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")], render_kw={"placeholder": "Enter Your Password:  "})
    confirm = PasswordField("Confirm Password", [InputRequired()], render_kw={"placeholder": "Confirm Your Password:  "})
    #submit button
    submit = SubmitField("Register")

#User comment
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()], render_kw={"placeholder": "Leave a comment:  "})
  submit = SubmitField('Create')
