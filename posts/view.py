from django.shortcuts import get_object_or_404
from rest_framework import viewsets, renderers, permissions, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment
from .serializers import (PostDetailSerializer, PostListSerializer,
                          PostCreateSerializer, CommentSerializer,
                          CommentCreateSerializer)


class PostViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrive(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)

    def create(self, request):
        serializer = PostCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostCreateSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(viewsets.ViewSet):

    def list(self, request, post_pk):
        queryset = Comment.objects.filter(post=post_pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrive(self, request, pk=None, **kwargs):
        queryset = Comment.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(post)
        return Response(serializer.data)

    def create(self, request, post_pk=None):
        serializer = CommentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Comment.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = CommentCreateSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Comment.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
