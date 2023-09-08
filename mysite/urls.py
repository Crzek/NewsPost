from django.conf.urls import include
from django.contrib import admin
from django.urls import re_path, path

app_name = "my_site"

urlpatterns = [
    re_path("admin/", admin.site.urls),
    re_path("blog/", include("blog.urls", namespace="blog")),
]
