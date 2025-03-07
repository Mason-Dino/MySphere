from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.template import loader
import os
import glob

import logging

# Create your views here.
def home(requests):
    template = loader.get_template('home-folder.html')
    logger = logging.getLogger("home")
    logging.basicConfig(filename="viewTXT.log")

    os.scandir(os.getcwd())
    directories = []

    for dir in glob.glob(f"/home/mason-server/*"):
        if os.path.isdir(dir) and dir != "/home/mason-server/usb":
            directories.append([dir, dir.removeprefix("/home/mason-server/")])

    logger.error(f"{directories}")

    context = {
        "directories": directories
    }
    
    return HttpResponse(template.render(context=context, request=requests))