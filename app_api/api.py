from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from app_blog.models import Post, PostComment
from app_api.serializers import PostSerializer, CommentSerializer


@permission_classes([IsAuthenticated])
class PostCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # parser_classes = (MultiPartParser, FormParser,)


@permission_classes([IsAuthenticated])
class CommentCreateAPIView(generics.ListCreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = CommentSerializer
