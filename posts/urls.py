from django.urls import path
from .view import PostViewSet, CommentViewSet, VoteViewSet
from rest_framework.urlpatterns import format_suffix_patterns

post_detail = PostViewSet.as_view({
    'get': 'retrive',
    'put': 'update',
    'delete': 'destroy',
    'post': 'create'
})

post_create_list = PostViewSet.as_view({

    'get': 'list',
    'post': 'create'
})

comments_detail = CommentViewSet.as_view({
    'get': 'retrive',
    'put': 'update',
    'delete': 'destroy',
})

comment_create_list = CommentViewSet.as_view({

    'get': 'list',
    'post': 'create'
})


urlpatterns = format_suffix_patterns([

    path('post/', post_create_list),
    path('post/<int:pk>', post_detail),
    path('post/<int:post_pk>/comment/', comment_create_list),
    path('post/<int:post_pk>/comment/<int:pk>', comments_detail),
    path('post/<int:pk>/vote', VoteViewSet.as_view({'post': 'create'})),
])
