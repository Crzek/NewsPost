from django.urls import re_path
from .views import index, add_post, post

app_name = "blog"

urlpatterns = [
    # Your code here
    re_path("", index, name="index"),
    re_path("add_post/", add_post, name="addpost"),
    re_path("post/<int:article_id>/", post, name="post"),

]
