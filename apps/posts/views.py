from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Post

# Create your views here.

# @login_required(login_url='login')
def index(request):

    posts = Post.objects.all()
    # for post in posts:
    #     print(f'Title: {post.title}, Author: {post.author}, Date: {post.created_on}')

    context = {'posts': posts}

    return render(request, "posts/index.html", context)

def newPost(request):
    return HttpResponse("Welcome to the new posts page!")
