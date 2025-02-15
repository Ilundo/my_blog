from django.shortcuts import render
from django.http import HttpRequest
from .models import Post, Author

# Create your views here.
def posts_list(request:HttpRequest):
    posts = Post.objects.all()
    return render(request,"posts_list.html", {"posts":posts})

def posts_by_author(request, author_id):
    author = Author.objects.get(Author,primary_key=author_id)
    post = Post.onjects.filter(author=author)
    return render(request,"post_author.html",{'post':post , 'author':author})