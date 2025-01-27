from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os
import glob

# Create your views here.

def home(request):
    template = loader.get_template('home.html')

    directory = "/home/mason-server/"

    files = glob.glob(f"{directory}*")

    serverFiles = []

    for file in files:
        if os.path.isdir(file):
            serverFiles.append([file, True, file.removeprefix(directory)])

        else:
            serverFiles.append([file, False, file.removeprefix(directory)])


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
            serverFiles.append([file, True, file.removeprefix(directory)])

        else:
            serverFiles.append([file, False, file.removeprefix(directory)])


    context = {
        "files": serverFiles,
        "dir": directory
    }

    
    return HttpResponse(template.render(context=context, request=request))
