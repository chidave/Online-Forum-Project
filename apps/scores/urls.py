from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='scores'),
    path('getData', views.getData, name='getData'),
]
