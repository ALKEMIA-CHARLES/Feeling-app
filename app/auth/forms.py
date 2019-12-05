from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,validators,BooleanField
from wtforms.validators import EqualTo,DataRequired
from wtforms import ValidationError

class SignupForm(FlaskForm):
  username = StringField('User Name',[validators.DataRequired()])
  email = StringField('Email',[validators.DataRequired()])
  password = PasswordField('Password',[validators.DataRequired(), validators.EqualTo("confirm", message='passwords must match')])
  confirm = PasswordField('Confir Password',[validators.DataRequired()])
  submit = SubmitField('Sign Up')

  def check_email(self,dataf_ield):
    if User.query.filter_by(email = data_field.data).first():
      raise ValidationError('an account with this email exist')

  def check_username(self,data_field):
    if User.query.filter_by(username = data_field).first():
      raise ValidationError('username taken, choose another username..')


class LoginForm(FlaskForm):
  username = StringField('username',[validators.DataRequired()])
  password = PasswordField('Password',[validators.DataRequired()])
  remember = BooleanField('remember me')
  submit = SubmitField('Sign In')
  