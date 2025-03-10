from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import FileResponse
from django.template import loader
import os
import glob

import logging
import json

# Create your views here.
def home(requests):
    template = loader.get_template('home-upload.html')
    logger = logging.getLogger("home-upload")
    logging.basicConfig(filename="viewTXT.log")

    
    return HttpResponse(template.render(request=requests))

def fileUpload(requests):
    logger = logging.getLogger("file-upload")
    logging.basicConfig(filename="viewTXT.log")
    
    if requests.method == "POST":
        logger.error("TEst")
        logger.error(f"file: {requests.FILES}")
        logger.error(f"file: {requests.body}")
        
        return JsonResponse({
            "code": 200
        })