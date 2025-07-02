from django.urls import path
from .views import embed_home

urlpatterns=[
    path("", embed_home, name="embed_home"),
]