from django.urls import path
from .views import (
    posts_home,
    get_Posts,
    create_posts,
)

urlpatterns=[
    path("", posts_home, name="posts_home"),
    path("get_Posts", get_Posts, name="get_Posts"),
    path("create_posts", create_posts, name="create_posts"),
]