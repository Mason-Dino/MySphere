from django.urls import path, re_path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home-1'),
    path('', views.home, name='home-2'),
    path('home/<str:path>', views.directory, name='directory'),
    path('home/txt/<str:path>/<str:file>', views.viewTXT, name="txt-view"),
    path('home/movie/<str:path>/<str:file>', views.viewMovie, name="movie-view"),
    path('movie/play/<str:path>/<str:file>', views.playMovie, name="movie-play")
]