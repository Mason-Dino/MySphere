from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.template import loader
import os
import glob
import subprocess
import logging
import json

# Create your views here.
def home(requests):
    template = loader.get_template('home-edit.html')
    
    try:
        os.makedirs("/home/mason-server/Editor")
    except:
        pass
    
    return HttpResponse(template.render(request=requests))

def saveFile(requests):
    pass

def test(requests):
    template = loader.get_template('test.html')
    
    return HttpResponse(template.render(request=requests))