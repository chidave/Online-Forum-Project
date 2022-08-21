from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm

# Create your views here.

# @login_required(login_url='login')
def index(request):

    posts = Post.objects.all()
    # for post in posts:
    #     print(f'Title: {post.title}, Author: {post.author}, Date: {post.created_on}')

    context = {'posts': posts}

    return render(request, "posts/index.html", context)

    
@login_required(login_url='login')
def newPost(request: HttpRequest):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            form = form.save(commit=False)
            form.author = request.user
            form.save()

            return redirect('index')

    context = {'form': form}
    return render(request, "posts/newPost.html", context)


def viewPost(request, postId):

    post = Post.objects.get(pk=postId)
    context = {'post': post, 'range': range(10)}

    return render(request, "posts/post.html", context)
    # return HttpResponse(f'This is Post #{postId}')
