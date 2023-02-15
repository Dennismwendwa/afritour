from django.db import models
from django .contrib.auth.models import User
from datetime import date
from django.urls import reverse

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
    


class Post (models.Model):

    title = models.CharField(max_length=250)
    title_tag = models.CharField(max_length=250, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='tours/image')
    country = models.CharField(max_length=250, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE, blank=True, null=True)

    

    def __str__(self):

        return self.title + ' | ' + str(self.author)




