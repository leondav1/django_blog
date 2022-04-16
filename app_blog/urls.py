from django.urls import path
from .views import PostsListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('posts/', PostsListView.as_view(), name='posts_list_url'),
    path('post/create/', PostCreateView.as_view(), name='post_create_url'),
    path('post/<int:profile_id>/', PostDetailView.as_view(), name='post_detail_url'),
    path('post/<int:profile_id>/update/', PostUpdateView.as_view(), name='post_update_url'),
    path('post/<int:profile_id>/delete/', PostDeleteView.as_view(), name='post_delete_url'),
]
