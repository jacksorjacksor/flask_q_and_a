from flask import render_template
from my_flask_app import app
from my_flask_app.models import User, Post, Comment

@app.route("/")
def home_function():

    list_of_posts = Post.query.all() # Gives us a list of all the Post objects

    one_post = Post.query.first()   # Gives a Post object

    # filter_by: only allows those that satisfy a criteria
    # ID
    list_of_posts_with_id_1 = Post.query.filter_by(id=1).all()

    # order_by: orders the objects based on a criteria
    # Date (asc and desc)

    # for post in list_of_posts:
    #     if post.comments:
    #         # post.comments will be a list of all the comments
    #         for comment in post.comments:
    #             print(comment.comment)


    return render_template("home.html", list_of_posts=list_of_posts)