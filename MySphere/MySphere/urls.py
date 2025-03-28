"""
URL configuration for MySphere project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('files/', include("Files.urls")),
    path('usb/', include('USB.urls')),
    path('folder/', include('Folder.urls')),
    path('upload/', include("Upload.urls")),
    path('process/', include("Process.urls")),
    path('edit/', include('Editor.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('success/', views.success, name='success')
]
