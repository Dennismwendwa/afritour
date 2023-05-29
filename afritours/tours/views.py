from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Category, Image
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.


def city(request):
    # object = Post.objects.all()
    return render(request, "tours/index_test.html", {})#this function not in use


def home(request):
    main = Post.objects.get(pk=2)
    main_sub = Post.objects.get(pk=4)
    shimba = Post.objects.get(pk=6)
    park = Post.objects.get(pk=5)
    titles = Post.objects.all()[0:5]
    slides = Post.objects.all()[2:5]
    recent = Post.objects.all()[:5]

    cats = category_fun()

    return render(
        request,
        "tours/index_test.html",
        {
            "main": main,
            "main_sub": main_sub,
            "titles": titles,
            "shimba": shimba,
            "park": park,
            "slides": slides,
            "recent": recent,
            "cats": cats,
        },
    )


def allposts(request):
    posts = Post.objects.all()
    cats = category_fun()
    recent = Post.objects.all()[:5]

    return render(
        request,
        "tours/allposts.html",
        {
            "posts": posts,
            "cats": cats,
            "recent": recent,
        },
    )


"""
class DetailView(DetailView):
    model = Post
    template_name = 'tours/detail.html'
"""


def detailview(request, pk):
    post = get_object_or_404(Post, pk=pk)
    cats = category_fun()
    recent = Post.objects.all()[:5]

    return render(
        request,
        "tours/detail.html",
        {
            "post": post,
            "cats": cats,
            "recent": recent,
        },
    )


def category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category)

    cats = category_fun()
    recent = Post.objects.all()[:5]

    return render(
        request,
        "tours/category.html",
        {
            "category": category,
            "posts": posts,
            "cats": cats,
            "recent": recent,
        },
    )


def allcategory(request):
    category = category_fun()
    posts = Post.objects.all()
    cats = category_fun()
    recent = Post.objects.all()[:5]

    return render(
        request,
        "tours/category_all.html",
        {
            "category": category,
            "posts": posts,
            "cats": cats,
            "recent": recent,
        },
    )


def category_fun():
    cats = Category.objects.all()

    return cats


def each_category(pk):
    categoryeach = Post.objects.filter(category.pk == pk)

    return categoryeach


def search(request):
    cats = category_fun()
    recent = Post.objects.all()[:5]

    query = request.GET.get("search")
    results = []

    if query and query.strip():
        results = Post.objects.filter(
            Q(body__icontains=query) | Q(title__icontains=query)
        )

    return render(
        request,
        "tours/search.html",
        {
            "results": results,
            "query": query,
        },
    )


def images(request):

	cats = category_fun()
	recent = Post.objects.all()[:5]

	image = Image.objects.all()

	return render(request, "tours/images.html", {
			"cats": cats,
			"recent": recent,
			"image": image,
			})
































