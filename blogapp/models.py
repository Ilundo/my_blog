from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField()

class Post(models.Model):
    title=models.CharField(max_length=100)
    content = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
