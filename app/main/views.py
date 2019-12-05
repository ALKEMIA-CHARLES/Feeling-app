from flask import (render_template, request, redirect, url_for, abort)
from . import main
from ..models import User, UserAffirmations, Comments, DatabaseAffirmations
from .forms import AddAffirmation, DelAffirmation, AffirmationComment, DelAffirmationComment
from flask_login import login_required, current_user
from .. import db


@main.route("/home")
def home():
    return render_template("home.html")


@main.route("/addaffirmation", methods=["GET", "POST"])
def add():
    title = affirmation = None
    form = AddAffirmation()
    if form.validate_on_submit():

        affirmation = form.added_affirmation.data
        title = form.title.data
        new_affirmation = UserAffirmations(
            user_affirmations_title=title, user_affirmations_post_section=affirmation)
        db.session.add(new_affirmation)
        db.session.commit()

        return redirect(url_for('main.affirmations_list'))
    return render_template('add.html', form=form)


@main.route("/affirmationslist")
def affirmations_list():
    added_affirmations = UserAffirmations.query.all()
    return render_template('affirmationslist.html', added_affirmations=added_affirmations)


@main.route("/delaffirmation/<int:user_affirmation_id>", methods=["GET", "POST"])
def delete(user_affirmation_id):

    deleted_affirmation = UserAffirmations.query.filter_by(
        id=user_affirmation_id).first()
    db.session.delete(deleted_affirmation)
    db.session.commit()

    return redirect(url_for('main.affirmations_list'))


@main.route("/comments/<int:database_affirmations_id>", methods=["GET", "POST"])
def addcoments(database_affirmations_id):

    form = AffirmationComment()

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comments(
            comments_section=comment, database_affirmations_id=database_affirmations_id)
        db.session.add(new_comment)
        db.session.commit()

    all_comments = Comments.query.filter_by(
        database_affirmations_id=database_affirmations_id).all()
    return render_template("comments.html", all_comments=all_comments, form=form, database_affirmations_id=database_affirmations_id)


@main.route("/deletecomment/<int:added_affirmation_id>/<int:comments_id>", methods=["GET", "POST"])
def deletecomment(added_affirmation_id, comments_id):

    comments = Comments.query.filterby(id=comments_id).first()
    db.session.delete
    db.session.commit()
    return redirect(url_for('main.addcomments', UserAffirmations_id=added_affirmation_id))


@main.route("/database_affirmations")
def admin_affirmations():
    admin_affirmations = DatabaseAffirmations.query.all()
    print(admin_affirmations)
    form = AffirmationComment()

    return render_template("databaseaffirmations.html", admin_affirmations=admin_affirmations, form=form)


@main.route('/submitcomment/<int:affirmation_id>', methods=['POST'])
def submit_comments(affirmation_id):
    form = AffirmationComment()

    if form.validate_on_submit():
        comment_data = form.comment.data
        new_comment = Comments(comments_section=comment_data,
                               database_affirmations_id=affirmation_id)
        db.session.add(new_comment)
        db.session.commit()

    return redirect(url_for('main.admin_affirmations'))
