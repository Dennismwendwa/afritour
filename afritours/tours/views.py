from django.shortcuts import render
from django.urls import path

from . models import Post


# Create your views here.
def city (request):

    post = Post.objects.all()


    return render(request, 'tours/index.html', {'post': post})


def home (request):

    return render(request, 'tours/home.html')