from rest_framework import serializers

from app_blog.models import Post, PostComment


# class FilterReviewListSerializer(serializers.ListSerializer):
#     def to_representation(self, data):
#         data = data.filter(parent=None)
#         return super().to_representation(data)
#
#
# class RecursiveSerializer(serializers.Serializer):
#     def to_representation(self, value):
#         serializer = self.parent.parent.__class__(value, context=self.context)
#         # if serializer.data['children'].level > 3:
#         print(dir(serializer.data))
#         print(serializer.data.keys())
#             # return
#         # print(type(serializer.data))
#         return serializer.data


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'active']

    def create(self, validated_data):
        post = Post.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            active=validated_data['active'],
        )
        post.save()
        return post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ['name', 'user', 'comment', 'post', 'parent', 'is_active']

    def create(self, validated_data):
        comm = PostComment.objects.create(
            name=validated_data['name'],
            user=validated_data['user'],
            comment=validated_data['comment'],
            post=validated_data['post'],
            parent=validated_data['parent'],
            is_active=validated_data['is_active'],
        )
        comm.save()
        return comm


# class CommentListSerializer(serializers.ModelSerializer):
#     children = RecursiveSerializer(many=True)
#
#     class Meta:
#         list_serializer_class = FilterReviewListSerializer
#         model = PostComment
#         fields = ('name', 'user', 'comment', 'created_at', 'post', 'is_active', 'children')


class CommentListSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        depth = 1
        model = PostComment
        fields = ('name', 'user', 'comment', 'created_at', 'post', 'is_active', 'children')

    @staticmethod
    def get_children(obj):
        if obj.level > 2:
            return
        return CommentListSerializer(obj.get_children(), many=True).data


class CommentLevelListSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        depth = 1
        model = PostComment
        fields = ('name', 'user', 'comment', 'created_at', 'post', 'is_active', 'children')

    @staticmethod
    def get_children(obj):
        return CommentLevelListSerializer(obj.get_children(), many=True).data
