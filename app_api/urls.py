from django.urls import path

from .api import PostCreateAPIView, CommentCreateAPIView, CommentListAPIView, CommentLevelListAPIView

urlpatterns = [
    path('post/create/', PostCreateAPIView.as_view()),
    path('comment/create/', CommentCreateAPIView.as_view()),
    path('comments/list/', CommentListAPIView.as_view()),
    path('comments/list/level/', CommentLevelListAPIView.as_view()),
]
