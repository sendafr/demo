from django.urls import path
from giox.views import( 
    giox_home,
    create_blogPost,
    getBlogPost,
    BlogPostView,
    )


urlpatterns=[
    path(" ", giox_home, name="giox_home"),
    path("BlogPostView", BlogPostView.as_view()),
    path("create_blogPost", create_blogPost, name="create_blogPost"),
    path("getBlogPost", getBlogPost, name="getBlogPost"),
]