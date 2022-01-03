from flask import render_template
from my_flask_app import app
from my_flask_app.models import User, Post, Comment

@app.route("/")
def home_function():
    # Get full list:
    list_of_posts = Post.query.all() # Gives us a list of all the Post objects

    # Get first item
    one_post = Post.query.first()   # Gives a Post object

    # filter_by: only allows those that satisfy a criteria
    list_of_posts_with_id_1 = Post.query.filter_by(id=1).all()

    # order_by: orders the objects based on a criteria
    list_of_posts_ordered_by_id_asc = Post.query.order_by(Post.id.asc()).all()
    list_of_posts_ordered_by_id_desc = Post.query.order_by(Post.id.desc()).all()

    return render_template(
        "home.html", 
        list_of_posts=list_of_posts, 
        one_post=one_post, 
        list_of_posts_with_id_1=list_of_posts_with_id_1,
        list_of_posts_ordered_by_id_asc=list_of_posts_ordered_by_id_asc,
        list_of_posts_ordered_by_id_desc=list_of_posts_ordered_by_id_desc,
        )