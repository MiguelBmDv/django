from django.db import models


    
class Article(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField()
    image=models.ImageField(default='nullj')
    public=models.BooleanField()
    create_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

class Category(models.Model):
    name=models.CharField(max_length=110)
    description=models.CharField(max_length=250)
    create_date=models.DateField()