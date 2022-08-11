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

    
@login_required(login_url='login')
def newPost(request):
    return HttpResponse("Welcome to the new posts page!")


def viewPost(request, postId):

    post = Post.objects.get(pk=postId)
    context = {'post': post, 'range': range(10)}

    return render(request, "posts/post.html", context)
    # return HttpResponse(f'This is Post #{postId}')
