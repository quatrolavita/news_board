from django.shortcuts import get_object_or_404
from rest_framework import viewsets, renderers, generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from core.permissions import IsAuthorOrAdmin
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

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def create(self, request):
        new_post = Post(author=request.user)
        serializer = PostCreateSerializer(new_post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, permission_classes=[IsAuthorOrAdmin])
    def update(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostCreateSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, permission_classes=[IsAuthorOrAdmin])
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

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def create(self, request, post_pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=post_pk)
        new_comment = Comment(author=request.user, post=post)
        serializer = CommentCreateSerializer(new_comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, permission_classes=[IsAuthorOrAdmin])
    def update(self, request, pk=None, **kwargs):
        queryset = Comment.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = CommentCreateSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, permission_classes=[IsAuthorOrAdmin])
    def destroy(self, request, pk=None, **kwargs):
        queryset = Comment.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
