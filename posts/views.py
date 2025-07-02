
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from.models import Posts
from.forms import CreatePostsForm
from django.http import JsonResponse, HttpResponse

from .forms import PostsForm
# Create your views here.

def posts_home(request):
    return render(request, 'posts/posts_home.html')


def get_Posts(request):
    posts = Posts.objects.all()
    return JsonResponse({'posts': list(posts.values())})

 

def create_posts(request):
    form =CreatePostsForm()

    if request.method == 'POST':
        form = CreatePostsForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("<em>New post was created succesfully<em>")
        
    return render(request, "posts/create_posts.html", {"form": form})


    
   
   

       
    


def hello_world_view(request):
    return JsonResponse({'text': 'hello worldx2'})

"""def my_post(request):
    form = PostsForm()

    if request.method == 'POST':
       form = PostsForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponse("<em>New post was created successfully</em>")

    return render(request, 'my_post.html', {'form':form}) """  


           
        