from my_flask_app import db
from my_flask_app.models import Post, User, Comment

# Clear the database
db.drop_all()

# Create the database
db.create_all()

# Create some entries
post1 = Post(title="My first title", content="1contentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontent")
post2 = Post(title="My second title", content="2acontentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontent")
post3 = Post(title="My third title", content="3contentcontentcontentcontentcontentcontentcontentcontentcontentcontentcontent")

user1 = User(username="user1")

comment1 = Comment(comment="Hi this is my comment", user=user1, post=post3)


# Add these to the database session
db.session.add(post1)
db.session.add(post2)
db.session.add(post3)
db.session.add(user1)
db.session.add(comment1)

# Commit (/save) these to the database session
db.session.commit()