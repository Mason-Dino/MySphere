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

def saveFile(requests):
    logger = logging.getLogger("save-file")
    logging.basicConfig(filename="viewTXT.log")
    
    logger.error(f"{requests.method}")
    if requests.method == "POST":
        #data = dict(requests.body)
        data = json.loads((requests.body).decode("utf-8"))
        logger.error(f"{data}")
        
        if os.path.exists(f"/home/mason-server/Editor{data['filename']}") == True:
            return JsonResponse({
                "code": 400,
                "message": "File already exists"
            })
        
        with open(f"/home/mason-server/Editor/{data['filename']}", "w") as f:
            for line in str(data["content"]).splitlines():
                f.write(line)
        
        return JsonResponse({
            "code": 200,
            "message": "File Saves"
        })
    
    else:
        return HttpResponse("Data failed!")

def test(requests):
    template = loader.get_template('test.html')
    
    return HttpResponse(template.render(request=requests))