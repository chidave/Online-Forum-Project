from django.urls import path
from . import views

urlpatterns = [
    path('', views.yesterdayResults, name='scores'),
    path('todays-fixtures/', views.todayFixtures, name='fixtures')
]
