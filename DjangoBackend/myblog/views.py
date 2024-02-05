from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from myblog.models import UserBlog

from myblog.serializers import UserBlogSerializer, CreateBlogSerializer, UpdateBlogSerializer


class PostPagination(PageNumberPagination):
    page_size = 6
class UserBlogListView(ListAPIView):
    pagination_class = PostPagination
    serializer_class = UserBlogSerializer
    queryset = UserBlog.objects.all()
    

class UserBlogCreateView(CreateAPIView):
    serializer_class = CreateBlogSerializer
    queryset = UserBlog.objects.all()

class UserBlogUpdateView(UpdateAPIView):
    serializer_class = UpdateBlogSerializer
    queryset = UserBlog.objects.all()
    lookup_field = id