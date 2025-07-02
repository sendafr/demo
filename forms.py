from django import forms
from django.forms import ModelForm
from.models import BlogPost

class CreateBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields= ("title", "image", "author")