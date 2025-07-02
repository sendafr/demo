from django.contrib.auth.forms import forms
from .models import Posts

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"


class CreatePostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"        