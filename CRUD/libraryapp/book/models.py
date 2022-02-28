from pydoc import describe
from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField()
    author=models.CharField(max_length=30, default="anonymous")
    time=models.DateTimeField()
    email=models.EmailField(blank=True)
    describe=models.TextField(default="Anonymous Hacker")
    
    
    
    
    def __str__(self):
        return self.name