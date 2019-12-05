from . import auth
from flask import render_template,redirect,url_for,flash,request
from .forms import SignupForm,LoginForm
from ..models import User
from .. import db
from flask_login import login_user, current_user,logout_user 


@auth.route('/login',methods = ["GET","POST"])
def login():
  title='Log In'
  form = LoginForm()
  if form.validate_on_submit():
    print(form.username.data)
    user = User.query.filter_by(username = form.username.data).first()
    print(user)
    if user != None and user.verify_password(form.password.data):
      login_user(user,form.remember.data)
      return redirect(url_for('main.home'))
    
    flash('invalid username or password')

  return render_template('login.html',title=title,form=form)

@auth.route('/signup',methods = ["GET","POST"])
def signup():
  title='Sign up'
  form = SignupForm()
  if form.validate_on_submit():
    user = User(username=form.username.data,email=form.email.data)
    user.password(form.password.data)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('auth.login'))
  return render_template('signup.html',form=form,title=title)

@auth.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('main.index'))
