from rest_framework import serializers
from .models import BlogPost


class CreateBlogPostSSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields= ("title", "image", "author")