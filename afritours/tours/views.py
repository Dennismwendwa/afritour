from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
def city (request):

    #object = Post.objects.all()
    return render(request, 'tours/index.html', {})



def home (request):

    main = Post.objects.get(pk=2)
    main_sub = Post.objects.get(pk=4)
    shimba = Post.objects.get(pk=10)
    park = Post.objects.get(pk=11)
    titles = Post.objects.all()[0:8]
    slides = Post.objects.all()[7:13]

    return render(request, 'tours/home.html', {'main': main, 'main_sub': main_sub, 'titles': titles, 
                   'shimba': shimba, 
                   'park': park,
                   'slides':slides,
                }) 
class Allposts(ListView):
    model = Post
    template_name = 'tours/allposts.html'
    ordering = ['-post_date']
    #ordering = ['-id']

class DetailView(DetailView):
    model = Post
    template_name = 'tours/detail.html'


class CatListview(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category=self.kwargs)
            }