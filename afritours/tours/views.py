from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Category
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def city(request):

    # object = Post.objects.all()
    return render(request, 'tours/index_test.html', {})


def home(request):

    main = Post.objects.get(pk=2)
    main_sub = Post.objects.get(pk=4)
    shimba = Post.objects.get(pk=6)
    park = Post.objects.get(pk=5)
    titles = Post.objects.all()[0:5]
    slides = Post.objects.all()[2:5]
    recent = Post.objects.all()[:5]
	
    cats = category_fun()
  
    return render(request, 'tours/home.html', {
		    'main': main,
		    'main_sub': main_sub,
		    'titles': titles,
                    'shimba': shimba,
                    'park': park,
                    'slides': slides,
		    'recent': recent,
		    'cats': cats,
  })


class Allposts(ListView):
    model = Post
    template_name = 'tours/allposts.html'
    ordering = ['-post_date']
    # ordering = ['-id']


class DetailView(DetailView):
    model = Post
    template_name = 'tours/detail.html'


def category(request, pk):

	category = get_object_or_404(Category, pk=pk)
	posts = Post.objects.filter(category=category)
    	
	
	return render(request, "tours/category.html", {
			"category": category,
			"posts": posts,
			})


def category_fun():

	cats = Category.objects.all()

	return cats




















