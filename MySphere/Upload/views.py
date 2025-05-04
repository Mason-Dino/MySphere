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
        "path": "/home/mason-server/",
        "shortPath": "Home",
        "back": "stay"
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
        "shortPath": shortPath,
        "back": "history"
    }
    
    return HttpResponse(template.render(context=context, request=requests))

def fileUpload(requests):
    logger = logging.getLogger("file-upload")
    logging.basicConfig(filename="viewTXT.log")
    
    if requests.method == "POST":
        logger.error("check1")
        logger.error(f"{requests.FILES}")
        
        uploadFile = requests.FILES['file']
        
        logger.error(f"test: {requests.POST}")
        
        filePath = os.path.join(requests.POST['path'], str(uploadFile.name).replace(" ", "-"))

        logger.error(f"File uploading: {filePath}")
        try:
            file = open(filePath, 'x')
            file.close()
            
        except:
            pass
    
        logger.error("check 2")
        with open(filePath, "wb") as f:
            for chunk in uploadFile.chunks():
                f.write(chunk)
                
        logger.error(f"File uploaded: {filePath}")
        
        
        return JsonResponse({
            "code": 200
        })
        

def fileMultipleUpload(request):
    logger = logging.getLogger("file-upload")
    logging.basicConfig(filename="viewTXT.log")

    if request.method == "POST":
        logger.error("Upload started")
        logger.error(f"POST data: {request.POST}")
        logger.error(f"FILES data: {request.FILES}")

        uploaded_files = request.FILES.getlist('files[]')  # Accept multiple files from key 'files[]'

        upload_path = request.POST.get('path', '')
        if not os.path.isdir(upload_path):
            logger.error(f"Invalid path: {upload_path}")
            return JsonResponse({"code": 400, "message": "Invalid path"}, status=400)

        uploaded_filenames = []

        for uploadFile in uploaded_files:
            sanitized_name = str(uploadFile.name).replace(" ", "-")
            filePath = os.path.join(upload_path, sanitized_name)

            logger.error(f"Uploading file: {filePath}")
            try:
                os.makedirs(os.path.dirname(filePath), exist_ok=True)
                with open(filePath, "wb") as f:
                    for chunk in uploadFile.chunks():
                        f.write(chunk)
                uploaded_filenames.append(sanitized_name)
                logger.error(f"File uploaded: {filePath}")
            except Exception as e:
                logger.error(f"Error uploading {uploadFile.name}: {str(e)}")

        return JsonResponse({
            "code": 200,
            "files_uploaded": uploaded_filenames
        })

    return JsonResponse({"code": 405, "message": "Method not allowed"}, status=405)
