from django.db import models

# Create your models here.

class Post(models.Model):
    # post itself
    title = models.CharField(max_length=200, default="")
    author = models.CharField(max_length=200, default="")
    body = models.TextField(default="")
    
    # personal info
    email = models.EmailField(max_length=254, default="")
    address = models.CharField(max_length=200, default="", blank=True, null=True)