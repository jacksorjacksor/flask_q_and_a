from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField

class CommentForm(FlaskForm):
    comment_field = TextAreaField(label="Add a comment")
    submit = SubmitField("Submit")