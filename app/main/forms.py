from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,
                     SubmitField, SelectField, IntegerField)
from wtforms.validators import Required


class AddAffirmation(FlaskForm):
    title = StringField()
    added_affirmation = TextAreaField("What's on your mind")
    submit = SubmitField("Add Affirmation")


class DelAffirmation(FlaskForm):
    id = IntegerField()
    submit = SubmitField("Delete Affirmation")


class AffirmationComment(FlaskForm):
    comment = TextAreaField("what do you think")
    submit = SubmitField("Add comment")


class DelAffirmationComment(FlaskForm):
    id = IntegerField(
        "Please enter the ID number of the comment you would like to delete")

class getDatabaseAffirmations(FlaskForm):
    title = StringField()
    DatabaseAffirmations = TextAreaField()
