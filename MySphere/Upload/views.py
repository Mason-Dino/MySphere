from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.http import FileResponse
from django.template import loader
from django import forms
import os
import glob

import logging
import json

UPLOAD_DIR = "/home/mason-server/"

# Create your views here.
def home(requests):
    template = loader.get_template('home-upload.html')
    logger = logging.getLogger("home-upload")
    logging.basicConfig(filename="viewTXT.log")
    
    context = {
        "path": None
    }
    
    return HttpResponse(template.render(request=requests))
    
def handleUpload(f):
    with open("/home/mason-sever/name.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def fileUpload(requests):
    logger = logging.getLogger("file-upload")
    logging.basicConfig(filename="viewTXT.log")
    
    if requests.method == "POST":
        logger.error("check1")
        logger.error(f"{requests.FILES}")
        
        uploadFile = requests.FILES['file']
        
        filePath = os.path.join(UPLOAD_DIR, uploadFile.name)

        logger.error(f"File uploading: {filePath}")
        
        file = open(filePath, 'x')
        file.close()
        logger.error("check 2")
        with open(filePath, "wb") as f:
            for chunk in uploadFile.chunks():
                f.write(chunk)
                
        logger.error(f"File uploaded: {filePath}")
        
        
        return JsonResponse({
            "code": 202
        })