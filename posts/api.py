from django.shortcuts import get_object_or_404
from rest_framework import viewsets, renderers, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostModleViewSet(viewsets.ViewSet):
