from django.urls import path, include
from .views import UserBlogListView

app_name = "myblog"


urlpatterns = [
    path("blogs", UserBlogListView.as_view(), name="blogs-list"),
]
