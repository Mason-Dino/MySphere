from django.urls import path, re_path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home-1'),
    path('', views.home, name='home-2'),
    path('make-folder/', views.makeFolder, name="make-folder"),
    path('home/<str:path>', views.dir, name='dir-folder')
]