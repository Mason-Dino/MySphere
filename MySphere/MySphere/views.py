from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
import os
import glob

import logging
import json

# Create your views here.
def home(requests):
    return HttpResponseRedirect("/files/")