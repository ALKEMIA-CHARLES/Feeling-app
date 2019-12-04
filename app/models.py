from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model,UserMixin):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  full_name = db.Column(db.String(255))
  username = db.Column(db.String(255))
  email = db.Column(db.String(255))
  pass_secure = db.Column(db.String(255))
  bio= db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  config_affirmations = db.relationship(
        "DatabaseAffirmations", backref="database_affirmations", lazy="dynamic")
  user_affirmations = db.relationship(
      "UserAffirmations", backref="user_input", lazy="dynamic")
  comments = db.relationship(
        "Comments", backref="user_comments", lazy="dynamic")

  def password(self,password):
    self.pass_secure = generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)


class DatabaseAffirmations(db.Model):
    __tablename__ = 'affirmations'
    id = db.Column(db.Integer, primary_key=True)
    database_affirmations_title = db.Column(db.String)
    database_affirmations_post_section = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_comments = db.relationship(
        "Comments", backref="database_affirmations_user_comments", lazy="dynamic")


class UserAffirmations(db.Model):
    __tablename__ = 'useraffirmations'
    id = db.Column(db.Integer, primary_key=True)
    user_affirmations_title = db.Column(db.String)
    user_affirmations_post_section = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comments_section = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    database_affirmations_id = db.Column(
        db.Integer, db.ForeignKey('affirmations.id'))