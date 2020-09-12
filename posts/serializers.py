from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    """This class serialize Post objects"""

    class Meta:
        model = Post
        fields = ('title', 'link', 'creation_date', 'amount_of_upvotes', 'author')


class CommentSerializer(serializers.ModelSerializer):
    """This class serialize Comment objects"""

    class Meta:
        model = Comment
        fields = ('author', 'content', 'creation_date', 'post')
