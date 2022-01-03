# File where we establish our database schema

from my_flask_app import db
from datetime import datetime
# For hashing of passwords
from werkzeug.security import generate_password_hash, check_password_hash

# ONE
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    comments = db.relationship('Comment', backref="user")

# MANY
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

# ONE
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(40), nullable=False)
    content = db.Column(db.Text, nullable=False)
    comments = db.relationship('Comment', backref="post")