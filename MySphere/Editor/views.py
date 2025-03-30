from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.http import JsonResponse
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

def editFile(requests, file):
    template = loader.get_template('file-edit.html')
    
    try:
        os.makedirs("/home/mason-server/Editor")
    except:
        pass
    
    with open(f"/home/mason-server/Editor/{file}") as f:
        content = f.read()
    
    context = {
        "filename": file,
        "content": content
    }
    
    return HttpResponse(template.render(context=context, request=requests))

def saveFile(requests):
    logger = logging.getLogger("save-file")
    logging.basicConfig(filename="viewTXT.log")
    
    logger.error(f"{requests.method}")
    if requests.method == "POST":
        #data = dict(requests.body)
        data = json.loads((requests.body).decode("utf-8"))
        logger.error(f"{data}")
        
        if os.path.exists(f"/home/mason-server/Editor/{data['filename']}") == True:
            return JsonResponse({
                "code": 400,
                "message": "File already exists"
            })
        
        with open(f"/home/mason-server/Editor/{data['filename']}", "w") as f:
            for line in str(data["content"]).splitlines():
                f.write(f"{line}\n")
        
        return JsonResponse({
            "code": 200,
            "message": "File Saves"
        })
    
    else:
        return HttpResponse("Data failed!")
    
def editSaveFile(requests):
    logger = logging.getLogger("save-file")
    logging.basicConfig(filename="viewTXT.log")
    
    logger.error(f"{requests.method}")
    if requests.method == "POST":
        #data = dict(requests.body)
        data = json.loads((requests.body).decode("utf-8"))
        logger.error(f"{data}")
        
        with open(f"/home/mason-server/Editor/{data['filename']}", "w") as f:
            for line in str(data["content"]).splitlines():
                f.write(f"{line}\n")
        
        return JsonResponse({
            "code": 200,
            "message": "File Saves"
        })
    
    else:
        return HttpResponse("Data failed!")

def runFile(requests):
    logger = logging.getLogger("save-file")
    logging.basicConfig(filename="viewTXT.log")
    
    logger.error(f"{requests.method}")
    if requests.method == "POST":
        #data = dict(requests.body)
        data = json.loads((requests.body).decode("utf-8"))
        logger.error(f"{data}")
        
        value = os.system(f"sh /home/mason-server/Editor/{data['filename']}")
        logger.error(f"{value}")
        
        return JsonResponse({
            "code": 200,
            "result": value
        })
    
    else:
        return HttpResponse("Data failed!")