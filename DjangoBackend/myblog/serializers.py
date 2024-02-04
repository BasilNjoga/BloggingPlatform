from rest_framework import serializers

from myblog.models import UserBlog

class UserBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBlog
        fields = "__all__"

class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBlog
        fields = [
            'title',
            'category',
            'body',
            'created_by'
        ]
class UpdateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBlog
        fields = [
            'title',
            'category',
            'body',
            'created_by'
        ]