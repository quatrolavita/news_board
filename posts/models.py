import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    """Contain information about user posts"""

    title = models.CharField(max_length=64)
    link = models.URLField()
    creation_date = models.DateField(auto_now=True)
    amount_of_upvotes = models.SmallIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # class Meta:
    #     ordering = ['creation_date']
    def __str__(self):
        return self.title


class Comment(models.Model):
    """Contain information about posts comments"""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return str(self.id)