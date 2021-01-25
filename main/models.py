from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class ShopBooks(models.Model):
     title = models.CharField(max_length=100)
     subtitle = models.CharField(max_length=100)
     description = models.CharField(max_length=200)
     price = models.CharField(max_length=10)
     genre = models.CharField(max_length=50)
     author = models.CharField(max_length=50)
     year = models.CharField(max_length=10)
     date = models.DateTimeField(auto_now_add=True)

     

   
