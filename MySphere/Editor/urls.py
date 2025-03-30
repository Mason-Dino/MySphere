from django.urls import path, re_path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home-1'),
    path('', views.home, name='home-2'),
    path('file/<str:file>', views.test, name='code-edit-test'),
    path('saveFile/', views.saveFile, name='save-file'),
    path('edit-saveFile/', views.editSaveFile, name='save-file')
]