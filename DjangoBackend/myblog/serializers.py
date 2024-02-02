from rest_framework import serializers

from myblog.models import UserBlog

class UserBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBlog
        fields = "__all__"