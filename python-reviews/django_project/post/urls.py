from django.urls import path
from .views import HomePageView, CreatePostView # Import the views from the views.py file

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("post/", CreatePostView.as_view(), name="add_post"),
]