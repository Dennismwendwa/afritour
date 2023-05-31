from django.db import models
from django .contrib.auth.models import User
from datetime import date
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    
class Post (models.Model):
    title = models.CharField(max_length=250)
    title_tag = models.CharField(max_length=250, blank=True, null=True)
    keywords  = models.CharField(max_length=250, blank=True, null=True)
    meta_description = models.CharField(max_length=250, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='tours/image')
    country = models.CharField(max_length=250, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)


    def __str__(self):

        return self.title + ' | ' + str(self.author)
    

class Image (models.Model):
	name_of_park = models.CharField(max_length=250, blank=True, null=True)
	area_name = models.CharField(max_length=250)
	date      = models.DateField(auto_now_add=True)
	keywords  = models.CharField(max_length=300)
	descption = models.TextField()
	image     = models.ImageField(upload_to="area/image")

	def __str__(self):
		return "%s - %s - %s" % (self.name_of_park, self.area_name, self.date)



