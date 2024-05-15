from django.shortcuts import render

def home(request):
    return render(request, "index.html")

from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})