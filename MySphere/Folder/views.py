from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import FileResponse
from django.template import loader
import os
import glob

import logging
import json
import shutil

# Create your views here.
def home(requests):
    template = loader.get_template('home-folder.html')
    logger = logging.getLogger("home-folder")
    logging.basicConfig(filename="viewTXT.log")

    os.scandir(os.getcwd())
    directories = []

    for dir in glob.glob(f"/home/mason-server/*"):
        if os.path.isdir(dir) and dir != "/home/mason-server/usb":
            directories.append([dir, dir.removeprefix("/home/mason-server/"), dir.removeprefix("/home/mason-server/").replace("/", ".")])

    logger.error(f"{directories}")

    context = {
        "directories": directories,
        "path": "/home/mason-server/",
        "shortPath": "Home",
        "back": "stay",
        "root": True
    }
    
    return HttpResponse(template.render(context=context, request=requests))

def dir(requests, path: str):
    template = loader.get_template('home-folder.html')
    logger = logging.getLogger("dir-folder")
    logging.basicConfig(filename="viewTXT.log")
    directories = []
    
    path = path.replace(".", "/")
    
    for dir in glob.glob(f"/home/mason-server/{path}/*"):
        if os.path.isdir(dir):
            logger.error(f"{dir.removeprefix('/home/mason-server/').replace('/', '.')}")
            directories.append([dir, dir.removeprefix(f"/home/mason-server/{path}/"), dir.removeprefix("/home/mason-server/").replace("/", ".")])
    
    shortPath = path.split("/")[len(path.split("/")) - 1]
    
    context = {
        "directories": directories,
        "path": f"/home/mason-server/{path}/",
        "shortPath": shortPath,
        "back": "history",
        "root": False
    }
    
    return HttpResponse(template.render(context=context, request=requests))

def makeFolder(requests):
    logger = logging.getLogger("make-folder")
    logging.basicConfig(filename="viewTXT.log")
    
    logger.error(f"{requests.method}")
    if requests.method == "POST":
        #data = dict(requests.body)
        data = json.loads((requests.body).decode("utf-8"))
        logger.error(f"{data}")
        
        os.makedirs(f"{data['path']}{data['name']}")
        
        return JsonResponse({
            "code": 200,
            "message": "folder made"
        })
    
    else:
        return HttpResponse("Data failed!")
    
def deleteFolder(requests):
    logger = logging.getLogger("delete-folder")
    logging.basicConfig(filename="viewTXT.log")
    
    if requests.method == "POST":
        data = json.loads((requests.body).decode("utf-8"))
        
        path = str(data["path"]).replace(".", "/")
        logger.error(f"{path}")
        
        shutil.rmtree(path=path)
        
        return JsonResponse({
            "code": 200
        })
    
    else:
        return HttpResponse("Only post request")