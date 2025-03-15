from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import FileResponse
from django.template import loader
import os
import glob
import logging

import subprocess
import json

# Create your views here.
def home(requests):
    template = loader.get_template("home-process.html")
    logger = logging.getLogger("home-process")
    logging.basicConfig(filename="viewTXT.log")
    
    result = subprocess.run(["pm2", "jlist"], capture_output=True, text=True)
    result = json.loads(result.stdout)
    
    data = []
    
    for i in range(len(result)):
        data.append({})
        
        data[i]['name'] = result[i]['name']
        data[i]['id'] = result[i]['pm_id']
        data[i]['status'] = result[i]['pm2_env']['status']
        data[i]['created'] = result[i]['pm2_env']['created_at']
        data[i]['uptime'] = result[i]['pm2_env']['pm_uptime']
        data[i]['restart'] = result[i]['pm2_env']['restart_time']
        data[i]['location'] = result[i]['pm2_env']['PWD']
        
    logger.error(f"{data}")
    
    context = {
        "data": data
    }
    
    return HttpResponse(template.render(context=context, request=requests))