from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from myblog.models import UserBlog

from myblog.serializers import UserBlogSerializer, CreateBlogSerializer, UpdateBlogSerializer

class UserBlogListView(ListAPIView):
    serializer_class = UserBlogSerializer
    queryset = UserBlog.objects.all()

class UserBlogCreateView(CreateAPIView):
    serializer_class = CreateBlogSerializer
    queryset = UserBlog.objects.all()

class UserBlogUpdateView(UpdateAPIView):
    serializer_class = UpdateBlogSerializer
    queryset = UserBlog.objects.all()
    lookup_field = id