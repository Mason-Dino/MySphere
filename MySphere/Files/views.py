from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.http import JsonResponse
from django.template import loader
import os
import glob

from django.views.decorators.csrf import ensure_csrf_cookie

import logging
import filetype
import json
import psutil

# Create your views here.

@ensure_csrf_cookie
def home(request):
    logger = logging.getLogger("home")
    logging.basicConfig(filename="viewTXT.log")
    
    template = loader.get_template('home-files.html')

    directory = "/home/mason-server/"

    files = glob.glob(f"{directory}*")
    files = sorted(files)

    serverFiles = []
    
    diskUsage = psutil.disk_usage('/')
    percent = diskUsage.percent
    strPercent = str(int(percent))
    

    for file in files:
        if os.path.isdir(file) and file == "/home/mason-server/usb":
            pass
        
        elif os.path.isdir(file):
            serverFiles.append([file, "folder", file.removeprefix(directory), file.removeprefix(directory).replace("/", ".")])
            
        elif file.endswith(".py") or file.endswith(".c") or file.endswith(".html") or file.endswith(".c") or file.endswith(".json") or file.endswith(".sh"):
            serverFiles.append([file, "code", file.removeprefix(directory), file.removesuffix(file.removeprefix(directory)).replace("/", ".")])
            
        elif file.endswith(".txt") or filetype.guess_mime(f"{file}") == "text/plain":
            serverFiles.append([file, "txt", file.removeprefix(directory), file.removesuffix(file.removeprefix(directory)).replace("/", ".")])
            
        elif file.endswith(".pdf"):
            serverFiles.append([file, "txt-pdf", file.removeprefix(directory), file.removesuffix(file.removeprefix(directory)).replace("/", ".")])
            
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
        "percent": percent,
        "strPercent": strPercent,
        "path": "/home/mason-server/"
    }

    return HttpResponse(template.render(context=context, request=request))

@ensure_csrf_cookie
def directory(request, path: str):
    template = loader.get_template('dir.html')
    logger = logging.getLogger("directory")
    logging.basicConfig(filename="viewTXT.log")

    root = "/home/mason-server/"
    path = path.replace(".", "/")

    #directory = root + path
    directory = f"{root}{path}/"

    files = glob.glob(f"{directory}*")
    files = sorted(files)
    
    diskUsage = psutil.disk_usage('/')
    percent = diskUsage.percent
    strPercent = str(int(percent))

    serverFiles = []
            
    for file in files:
        if os.path.isdir(file):
            serverFiles.append([file, "folder", file.removeprefix(directory), file.removeprefix(root).replace("/", ".")])
            
        elif file.endswith(".py") or file.endswith(".c") or file.endswith(".html") or file.endswith(".c") or file.endswith(".json") or file.endswith(".sh"):
            serverFiles.append([file, "code", file.removeprefix(directory), file.removesuffix(file.removeprefix(directory)).replace("/", ".")])
            
        elif file.endswith(".txt") or filetype.guess_mime(f"{file}") == "text/plain":
            serverFiles.append([file, "txt", file.removeprefix(directory), file.removesuffix(file.removeprefix(directory)).replace("/", ".")])
            
        elif file.endswith(".pdf"):
            serverFiles.append([file, "txt-pdf", file.removeprefix(directory), file.removesuffix(file.removeprefix(directory)).replace("/", ".")])
            
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
        "dir_short": directory.removeprefix(root),
        "strPercent": strPercent
    }

    
    return HttpResponse(template.render(context=context, request=request))

@ensure_csrf_cookie
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
        
    editFile = False
    if path == "/home/mason-server/Editor/":
        editFile = True
    
    context = {
        "data": data,
        "path": path,
        "path_dot": path.replace("/", "."),
        "filename": file,
        "editFile": editFile
    }
    
    
    return (HttpResponse(template.render(context=context, request=request)))

@ensure_csrf_cookie
def viewPDF(request, path: str, file: str):
    template = loader.get_template("view-pdf.html")
    
    path = path.replace(".", "/")
        
    context = {
        "filename": file,
        "path": path.replace("/", ".")
    }
    
    return HttpResponse(template.render(context=context, request=request))

@ensure_csrf_cookie
def viewMovie(request, path: str, file: str):
    template = loader.get_template("view-movie.html")
    
    path = path.replace(".", "/")
        
    context = {
        "filename": file,
        "path": path.replace("/", ".")
    }
    
    return HttpResponse(template.render(context=context, request=request))

@ensure_csrf_cookie
def viewAudio(request, path: str, file: str):
    template = loader.get_template("view-audio.html")
    
    path = path.replace(".", "/")
        
    context = {
        "filename": file,
        "path": path.replace("/", ".")
    }
    
    return HttpResponse(template.render(context=context, request=request))

@ensure_csrf_cookie
def viewImg(request, path:str, file: str):
    template = loader.get_template("view-img.html")
    
    path = path.replace(".", "/")
        
    context = {
        "filename": file,
        "path": path.replace("/", ".")
    }
    
    return HttpResponse(template.render(context=context, request=request))

@ensure_csrf_cookie
def viewOther(request, path:str, file: str):
    template = loader.get_template("view-other.html")
    
    path = path.replace(".", "/")
        
    context = {
        "filename": file,
        "path": path.replace("/", ".")
    }
    
    return HttpResponse(template.render(context=context, request=request))

@ensure_csrf_cookie
def playMovie(request, path: str, file: str):
    path = path.replace(".", "/")
    video = open(f"{path}{file}", 'rb')
        
    return FileResponse(video, content_type='video/mp4')

@ensure_csrf_cookie
def playAudio(request, path: str, file: str):
    path = path.replace(".", "/")
    audio = open(f"{path}{file}", "rb")
    
    return FileResponse(audio, content_type='audio/mpeg')

@ensure_csrf_cookie
def showImg(request, path: str, file: str):
    path = path.replace(".", "/")
    img = open(f"{path}{file}", "rb")
    
    kind = filetype.guess_mime(f"{path}{file}")
    
    return FileResponse(img, content_type=kind)

@ensure_csrf_cookie
def showOther(request, path: str, file: str):
    path = path.replace(".", "/")
    img = open(f"{path}{file}", "rb")
    
    kind = filetype.guess_mime(f"{path}{file}")
    
    return FileResponse(img, content_type=kind)

@ensure_csrf_cookie
def showPDF(request, path: str, file: str):
    path = path.replace(".", "/")
    pdf = open(f"{path}{file}", "rb")
    
    kind = filetype.guess_mime(f"{path}{file}")
    
    return FileResponse(pdf, content_type=kind)

@ensure_csrf_cookie
def downloadTxt(request, path: str, file: str):
    path = path.replace(".", "/")
    
    video = open(f"{path}{file}", 'rb')
        
    return FileResponse(video, content_type='text')

def viewMD(request, path: str, file: str):
    pass

@ensure_csrf_cookie
def deleteFile(requests):
    logger = logging.getLogger("delete-file")
    logging.basicConfig(filename="viewTXT.log")
    
    if requests.method == "POST":
        data = json.loads((requests.body).decode("utf-8"))
        logger.error(f"Output: {data}")
        
        path = str(data["path"]).replace(".", "/")
        file = str(data["file"])
        
        os.remove(os.path.join(path, file))
        
        return JsonResponse({
            "code": 200
        })
    
    else:
        return HttpResponse("Only Post Request")

@ensure_csrf_cookie
def renameFile(requests):
    logger = logging.getLogger("rename-file")
    logging.basicConfig(filename="viewTXT.log")
    
    if requests.method == "POST":
        data = json.loads((requests.body).decode("utf-8"))
        logger.error(f"Output: {data}")
        
        path = str(data["path"]).replace(".", "/")
        file = str(data["file"])
        newName = str(data["newName"])
        fileExtension = f".{file.split('.')[1]}"
        
        exists = os.path.exists(os.path.join(path, file))
        
        if exists == True:
            logger.error("File Exists")
            
            original = os.path.join(os.path.join(path, file))
            logger.error(f"{os.path.join(path, (newName + fileExtension))}")
            os.rename(original, os.path.join(path, (newName + fileExtension)))
            
            logger.error("File Renamed")
            
            return JsonResponse({
                "result": 200,
                "message": "File renamed"
            })
        
        else:
            return JsonResponse({
                "result": 403,
                "message": "File does not exists"
            })