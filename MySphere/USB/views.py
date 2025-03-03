from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.template import loader
import os
import glob

# Create your views here.
def home(requests):
    template = loader.get_template('home.html')
    print("he")
    
    return HttpResponse(template.render(request=requests))