from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    """This class serialize Comment objects"""

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'content', 'creation_date', 'post')



class PostListSerializer(serializers.ModelSerializer):
    """This class serialize Post objects"""

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ("id", "title", "link", "amount_of_upvotes", "author")


class PostDetailSerializer(serializers.ModelSerializer):
    """Detail info abut Post"""
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'creation_date', 'amount_of_upvotes', 'author', 'comments')


class PostCreateSerializer(serializers.ModelSerializer):
    """Detail info abut Post"""

    class Meta:
        model = Post
        exclude = ('author', 'amount_of_upvotes', 'creation_date')
        depth = 1


class CommentCreateSerializer(serializers.ModelSerializer):
    """This class serialize Comment objects"""

    class Meta:
        model = Comment
        fields = ('content',)

