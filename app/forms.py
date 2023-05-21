from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import user

# Create form -> checks if email is unique/already in db
def validate_email(self, email):
    exists = user.query.filter_by(email=email.data).first()
    if exists:
        raise ValidationError("This email is already in use, either log in or use a different email.")

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired("email required")])
    password = PasswordField('password', validators=[DataRequired("password required")])
    submit = SubmitField('Sign In')

class CreateForm(FlaskForm):
    name = StringField('name', validators=[DataRequired("name required")])
    email = StringField('email', validators=[DataRequired("email required"), validate_email])
    password = PasswordField('password', validators=[DataRequired("password required")])
    submit = SubmitField('Sign Up')