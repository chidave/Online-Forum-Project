from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.signin, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('<username>', views.userProfile, name='profile'),
]
