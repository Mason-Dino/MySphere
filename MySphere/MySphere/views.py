from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
import os
import glob

import logging
import json

# Create your views here.
def home(requests):
    return HttpResponseRedirect("/files/")

def success(requests):
    template = loader.get_template('success.html')
    
    return HttpResponse(template.render(request=requests))