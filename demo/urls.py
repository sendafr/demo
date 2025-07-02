"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from demo.settings import MEDIA_ROOT
from giox.urls import giox_home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', giox_home, name="giox_home"),
    path("giox", include(("giox.urls", "giox"), namespace="giox")),
    path("account", include(("account.urls", "account"), namespace="account")),
    path("my_pasionate", include(("my_pasionate.urls", "my_pasionate"), namespace="my_pasionate")),
    path("posts", include(("posts.urls", "posts"), namespace="posts")),
    path("videos", include(("videos.urls", "videos"), namespace="videos")),
    path("embed_video", include(("embed_video.urls", "embed_video"), namespace="embed_video")),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
