from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import FileResponse
from django.template import loader
import os
import glob

# Create your views here.
def home(requests):
    print("this is some code")
    return HttpResponse("Process Page")