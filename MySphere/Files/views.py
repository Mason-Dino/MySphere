from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os
import glob

import logging

# Create your views here.

def home(request):
    template = loader.get_template('home.html')

    directory = "/home/mason-server/"

    files = glob.glob(f"{directory}*")

    serverFiles = []

    for file in files:
        if os.path.isdir(file):
            serverFiles.append([file, "folder", file.removeprefix(directory)])
            
        elif file.endswith(".py") or file.endswith(".c") or file.endswith(".html") or file.endswith(".cc"):
            serverFiles.append([file, "code", file.removeprefix(directory)])
            
        elif file.endswith(".txt") or file.endswith(".pdf"):
            serverFiles.append([file, "txt", file.removeprefix(directory)])
            
        elif file.endswith("mp4") or file.endswith(".mp3") or file.endswith(".mov"):
            serverFiles.append([file, "movie", file.removeprefix(directory)])
            
        elif file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".heif") or file.endswith(".svg"):
            serverFiles.append([file, "img", file.removeprefix(directory)])

        else:
            serverFiles.append([file, "other", file.removeprefix(directory)])


    context = {
        "files": serverFiles
    }

    return HttpResponse(template.render(context=context, request=request))

def directory(request, path: str):
    template = loader.get_template('dir.html')

    root = "/home/mason-server/"
    path = path.replace(".", "/")

    #directory = root + path
    directory = f"{root}{path}/"

    files = glob.glob(f"{directory}*")

    serverFiles = []
            
    for file in files:
        if os.path.isdir(file):
            serverFiles.append([file, "folder", file.removeprefix(directory), file.removeprefix(root).replace("/", ".")])
            
        elif file.endswith(".py") or file.endswith(".c") or file.endswith(".html") or file.endswith(".cc"):
            serverFiles.append([file, "code", file.removeprefix(directory)])
            
        elif file.endswith(".txt") or file.endswith(".pdf"):
            serverFiles.append([file, "txt", file.removeprefix(directory)])
            
        elif file.endswith("mp4") or file.endswith(".mp3") or file.endswith(".mov"):
            serverFiles.append([file, "movie", file.removeprefix(directory)])
            
        elif file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".heif") or file.endswith(".svg"):
            serverFiles.append([file, "img", file.removeprefix(directory)])

        else:
            serverFiles.append([file, "other", file.removeprefix(directory)])


    context = {
        "files": serverFiles,
        "dir": directory
    }

    
    return HttpResponse(template.render(context=context, request=request))

def viewTXT(request, path: str):    
    logger = logging.getLogger("mylogger")
    logging.basicConfig(filename="viewTXT.log")
    logger.info("Whatever to log")
    
    logger.error(f"{path}")
    
    root = "/home/mason-server/"

    template = loader.get_template("view-txt.html")
    
    with open(f"{root}{path}", "r") as f:
        data = f.read()
        
    logger.error(f"{data}")
    
    data = data.replace("\n", " lineBreakHere ")
    
    context = {
        "data": data,
        "path": path
    }
    
    
    return (HttpResponse(template.render(context=context, request=request)))
