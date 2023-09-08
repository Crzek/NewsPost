from django.forms import ModelForm
from .models import Post


class AddPostForm(ModelForm):
    class Meta(object):
        model = Post
        fields = ["title", "body"]
