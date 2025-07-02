from django.shortcuts import render

# Create your views here.

def embed_home(request):
    return render(request, 'embed_video/embed_home.html')