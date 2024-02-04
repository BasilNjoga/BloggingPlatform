from django.urls import path, include
from .views import UserBlogListView, UserBlogCreateView, UserBlogUpdateView

app_name = "myblog"


urlpatterns = [
    path("blogs", UserBlogListView.as_view(), name="blogs-list"),
    path("create", UserBlogCreateView.as_view(), name="create"),
    path('update', UserBlogUpdateView.as_view(), name="update"),
    
]
