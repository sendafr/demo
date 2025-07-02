from django.shortcuts import render, redirect
from account.models import Account
from giox.serializers import CreateBlogPostSSerializer
from .models import BlogPost
from rest_framework import generics
from .forms import CreateBlogPostForm
from django.http import JsonResponse, HttpResponse
# Create your views here.

def giox_home(request):
    context ={}
    blogPosts = BlogPost.objects.all()
    context['blogPosts']= blogPosts
    return render(request, 'giox/giox_home.html', context)

class BlogPostView(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = CreateBlogPostSSerializer


def create_blogPost(request):
    context = {}
    form = CreateBlogPostForm()
    
    user = request.user
    if not user.is_authenticated:
       return redirect('account/must_authenticate')
    form = CreateBlogPostForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.athor = author
        form = CreateBlogPostForm()

    context['form'] =form
    return render(request, 'giox/create_blogPost.html', context)    



def getBlogPost(request):
    blogPosts = BlogPost.objects.all()
    return JsonResponse({"blogPosts": list(blogPosts.values())})