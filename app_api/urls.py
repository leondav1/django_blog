from django.urls import path

from .api import PostCreateAPIView, CommentCreateAPIView


urlpatterns = [
    path('post/create/', PostCreateAPIView.as_view()),
    path('comment/create/', CommentCreateAPIView.as_view()),
]
