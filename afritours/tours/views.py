from django.shortcuts import render


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
    titles = Post.objects.all()

    

    return render(request, 'tours/home.html', {'main': main, 'main_sub': main_sub, 'titles': titles, 'shimba': shimba, 'park': park}) 






    