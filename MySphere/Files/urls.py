from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home-1'),
    path('', views.home, name='home-2')
]