from django.db import models
from datetime import date

# Create your models here.

class Contact(models.Model):

	name     = models.CharField(max_length=250)
	email    = models.EmailField()
	date     = models.DateField(auto_now_add=True)
	subject  = models.CharField(max_length=250, default="request details")
	message  = models.TextField()

	def __str__(self):
		return "%s - %s - %s" % (self.name, self.email, self.date)

