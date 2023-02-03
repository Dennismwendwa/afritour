from django.db import models
from django .contrib.auth.models import User

# Create your models here.
class Post (models.Model):

    title = models.CharField(max_length=250)
    title_tag = models.CharField(max_length=250, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=250)

    

    def __str__(self):

        return self.title + ' | ' + self.author