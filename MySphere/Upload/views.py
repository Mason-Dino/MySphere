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
    
    directories = []

    for dir in glob.glob(f"/home/mason-server/*"):
        if os.path.isdir(dir) and dir != "/home/mason-server/usb":
            directories.append([dir, dir.removeprefix("/home/mason-server/"), dir.removeprefix("/home/mason-server/").replace("/", ".")])
    
    logger.error(f"{directories}")
    
    context = {
        "directories": directories,
        "path": "/home/mason-server/"
    }
    
    return HttpResponse(template.render(context=context, request=requests))

def dir(requests, path: str):
    template = loader.get_template('home-upload.html')
    logger = logging.getLogger("home-upload")
    logging.basicConfig(filename="viewTXT.log")
    
    path = path.replace(".", "/")
    
    directories = []
    
    for dir in glob.glob(f"/home/mason-server/{path}/*"):
        if os.path.isdir(dir):
            logger.error(f"{dir.removeprefix('/home/mason-server/').replace('/', '.')}")
            directories.append([dir, dir.removeprefix(f"/home/mason-server/{path}/"), dir.removeprefix("/home/mason-server/").replace("/", ".")])
    
    shortPath = path.split("/")[len(path.split("/")) - 1]
    
    context = {
        "directories": directories,
        "path": f"/home/mason-server/{path}/",
    }
    
    return HttpResponse(template.render(context=context, request=requests))

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