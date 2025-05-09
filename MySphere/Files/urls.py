from django.urls import path, re_path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home-1'),
    path('', views.home, name='home-2'),
    path('home/<str:path>', views.directory, name='directory'),
    path('home/txt/<str:path>/<str:file>', views.viewTXT, name="txt-view"),
    path('text/download/<str:path>/<str:file>', views.downloadTxt, name="download-text"),
    path('home/pdf/<str:path>/<str:file>', views.viewPDF, name='pdf-view'),
    path('pdf/show/<str:path>/<str:file>', views.showPDF, name='pdf-show'),
    path('home/movie/<str:path>/<str:file>', views.viewMovie, name="movie-view"),
    path('movie/play/<str:path>/<str:file>', views.playMovie, name="movie-play"),
    path('audio/play/<str:path>/<str:file>', views.playAudio, name="audio-play"),
    path('home/audio/<str:path>/<str:file>', views.viewAudio, name="audio-view"),
    path('home/image/<str:path>/<str:file>', views.viewImg, name="img-view"),
    path('image/show/<str:path>/<str:file>', views.showImg, name="img-show"),
    path('other/view/<str:path>/<str:file>', views.viewOther, name="other-view"),
    path('other/show/<str:path>/<str:file>', views.showOther, name="other-view"),
    path('delete/', views.deleteFile, name="delete-file"),
    path('rename/', views.renameFile, name="rename-file"),
    path('home/md/<str:path>/<str:file>', views.viewMD, name="md-view")
]