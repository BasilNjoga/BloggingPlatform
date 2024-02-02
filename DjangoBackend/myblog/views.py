from django.shortcuts import render
from rest_framework.generics import ListAPIView
from myblog.models import UserBlog

from myblog.serializers import UserBlogSerializer

class UserBlogListView(ListAPIView):
    serializer_class = UserBlogSerializer
    queryset = UserBlog.objects.all()