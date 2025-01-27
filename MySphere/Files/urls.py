from django.urls import path, re_path
from . import views

urlpatterns = [
    path('home/', views.home, name='home-1'),
    path('', views.home, name='home-2'),
    path('home/<str:path>', views.directory, name='directory')
]