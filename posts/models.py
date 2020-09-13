from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Contain information about user posts"""

    title = models.CharField(max_length=64)
    link = models.URLField()
    creation_date = models.DateField(auto_now=True)
    amount_of_upvotes = models.SmallIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Contain information about posts comments"""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")

    def __str__(self):
        return str(self.id)


class Vote(models.Model):
    """Contain unformation about posts upvotes"""

    ip = models.GenericIPAddressField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="vote")

    def __str__(self):
        return str(self.ip)

    @staticmethod
    def get_user_ip(request):
        """Get user ip"""

        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip
