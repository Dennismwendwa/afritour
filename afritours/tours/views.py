from django.shortcuts import render
from django.urls import path


# Create your views here.
def city (request):

    return render(request, 'tours/index.html')


def home (request):

    return render(request, 'tours/home.html')