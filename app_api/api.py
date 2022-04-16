from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app_blog.models import Post, PostComment
from app_api.serializers import PostSerializer, CommentSerializer, CommentListSerializer, CommentLevelListSerializer


@permission_classes([IsAuthenticated])
class PostCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # parser_classes = (MultiPartParser, FormParser,)


@permission_classes([IsAuthenticated])
class CommentCreateAPIView(generics.ListCreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = CommentSerializer


# @permission_classes([IsAuthenticated])
# class CommentListAPIView(APIView):
#     def get(self, request):
#         comments = PostComment.objects.all()
#         serializer = CommentListSerializer(comments, many=True)
#         return Response(serializer.data)


@permission_classes([IsAuthenticated])
class CommentListAPIView(generics.ListAPIView):
    model = PostComment
    serializer_class = CommentListSerializer
    queryset = PostComment.objects.filter(level=0)


@permission_classes([IsAuthenticated])
class CommentLevelListAPIView(generics.ListAPIView):
    model = PostComment
    serializer_class = CommentLevelListSerializer
    queryset = PostComment.objects.filter(level=3)
