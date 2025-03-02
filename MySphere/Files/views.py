from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.template import loader
import os
import glob

import logging

# Create your views here.

def home(request):
    logger = logging.getLogger("home")
    logging.basicConfig(filename="viewTXT.log")
    
    template = loader.get_template('home.html')

    directory = "/home/mason-server/"

    files = glob.glob(f"{directory}*")

    serverFiles = []
    
    

    for file in files:
        logger.error(f"{file}")
        if os.path.isdir(file) and file == "/home/mason-server/usb":
            pass
        
        elif os.path.isdir(file):
            serverFiles.append([file, "folder", file.removeprefix(directory), file.removeprefix(directory).replace("/", ".")])
            
        elif file.endswith(".py") or file.endswith(".c") or file.endswith(".html") or file.endswith(".c") or file.endswith(".json") or file.endswith(".sh"):
            serverFiles.append([file, "code", file.removeprefix(directory), file.removesuffix(file.removeprefix(directory)).replace("/", ".")])
            
        elif file.endswith(".txt") or file.endswith(".pdf"):
            serverFiles.append([file, "txt", file.removeprefix(directory), file.removesuffix(file.removeprefix(directory)).replace("/", ".")])
            
        elif file.endswith("mp4") or file.endswith(".mov"):
            serverFiles.append([file, "movie", file.removeprefix(directory), file.removesuffix(file.removeprefix(directory)).replace("/", ".")])
            
        elif file.endswith(".mp3"):
            serverFiles.append([file, "audio", file.removeprefix(directory), file.removesuffix(file.removeprefix(directory)).replace("/", ".")])
            
        elif file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".heif") or file.endswith(".svg"):
            serverFiles.append([file, "img", file.removeprefix(directory), file.removesuffix(file.removeprefix(directory)).replace("/", ".")])

        else:
            serverFiles.append([file, "other", file.removeprefix(directory), file.removesuffix(file.removeprefix(directory)).replace("/", ".")])


    context = {
        "files": serverFiles
    }

    return HttpResponse(template.render(context=context, request=request))

def directory(request, path: str):
    template = loader.get_template('dir.html')
    logger = logging.getLogger("directory")
    logging.basicConfig(filename="viewTXT.log")

    root = "/home/mason-server/"
    path = path.replace(".", "/")

    #directory = root + path
    directory = f"{root}{path}/"

    files = glob.glob(f"{directory}*")

    serverFiles = []
            
    for file in files:
        if os.path.isdir(file):
            serverFiles.append([file, "folder", file.removeprefix(directory), file.removeprefix(root).replace("/", ".")])
            
        elif file.endswith(".py") or file.endswith(".c") or file.endswith(".html") or file.endswith(".c") or file.endswith(".json") or file.endswith(".sh"):
            serverFiles.append([file, "code", file.removeprefix(directory), file.removesuffix(file.removeprefix(directory)).replace("/", ".")])
            
        elif file.endswith(".txt") or file.endswith(".pdf"):
            serverFiles.append([file, "txt", file.removeprefix(directory), file.removesuffix(file.removeprefix(directory)).replace("/", ".")])
            
        elif file.endswith("mp4") or file.endswith(".mov"):
            serverFiles.append([file, "movie", file.removeprefix(directory), file.removesuffix(file.removeprefix(directory)).replace("/", ".")])
            
        elif file.endswith(".mp3"):
            serverFiles.append([file, "audio", file.removeprefix(directory), file.removesuffix(file.removeprefix(directory)).replace("/", ".")])
            
        elif file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".heif") or file.endswith(".svg"):
            serverFiles.append([file, "img", file.removeprefix(directory), file.removesuffix(file.removeprefix(directory)).replace("/", ".")])

        else:
            serverFiles.append([file, "other", file.removeprefix(directory), file.removesuffix(file.removeprefix(directory)).replace("/", ".")])


    context = {
        "files": serverFiles,
        "dir": directory,
        "dir_short": directory.removeprefix(root)
    }

    
    return HttpResponse(template.render(context=context, request=request))

def viewTXT(request, path: str, file: str):    
    logger = logging.getLogger("viewTXT")
    logging.basicConfig(filename="viewTXT.log")
    logger.info("Whatever to log")
    
    logger.error(f"{path}")
    
    path = path.replace(".", "/")

    template = loader.get_template("view-txt.html")
    
    logger.info(f"{file}")
    
    with open(f"{path}{file}", "r") as f:
        data = f.read()
    
    context = {
        "data": data,
        "path": path,
        "path_dot": path.replace("/", "."),
        "filename": file
    }
    
    
    return (HttpResponse(template.render(context=context, request=request)))

def viewMovie(request, path: str, file: str):
    template = loader.get_template("view-movie.html")
    
    path = path.replace(".", "/")
        
    context = {
        "filename": file,
        "path": path.replace("/", ".")
    }
    
    return HttpResponse(template.render(context=context, request=request))

def viewAudio(request, path: str, file: str):
    template = loader.get_template("view-audio.html")
    
    path = path.replace(".", "/")
        
    context = {
        "filename": file,
        "path": path.replace("/", ".")
    }
    
    return HttpResponse(template.render(context=context, request=request))

def playMovie(request, path: str, file: str):
    path = path.replace(".", "/")
    video = open(f"{path}{file}", 'rb')
        
    return FileResponse(video, content_type='video/webm')

def playAudio(request, path: str, file: str):
    path = path.replace(".", "/")
    audio = open(f"{path}{file}", "rb")
    
    return FileResponse(audio, content_type='audio/mpeg')


def downloadTxt(request, path: str, file: str):
    path = path.replace(".", "/")
    
    video = open(f"{path}{file}", 'rb')
        
    return FileResponse(video, content_type='text')