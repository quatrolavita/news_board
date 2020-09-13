from news_board.celery import app
from posts.models import Vote, Post


@app.task()
def reset_upvotes():
    """ Task that wake up every 24h"""

    Vote.objects.all().delete()

    posts = Post.objects.all()

    for post in posts:
        post.amount_of_upvotes = 0
        post.save()
