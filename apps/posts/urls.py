from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.newPost, name='newPost'),
    path('<postId>', views.viewPost, name='viewPost'),
]
