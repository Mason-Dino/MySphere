from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import FileResponse
from django.template import loader
import os
import glob
import logging

from datetime import datetime
import time
import math
import subprocess
import json
import pytz


# Create your views here.
def home(requests):
    template = loader.get_template("home-process.html")
    logger = logging.getLogger("home-process")
    logging.basicConfig(filename="viewTXT.log")
    
    result = subprocess.run(["pm2", "jlist"], capture_output=True, text=True)
    result = json.loads(result.stdout)
    
    data = []
    
    timezone = pytz.timezone('US/Central')
    
    for i in range(len(result)):
        data.append({})
        
        data[i]['name'] = result[i]['name']
        data[i]['id'] = result[i]['pm_id']
        data[i]['status'] = result[i]['pm2_env']['status']
        
        if data[i]['status'] != 'errored':
            data[i]['created'] = datetime.fromtimestamp(result[i]['pm2_env']['created_at']/1000).astimezone(timezone).strftime('%m/%d %I:%M %p')
        
            uptime = (datetime.fromtimestamp(time.time()).astimezone(timezone) - datetime.fromtimestamp(result[i]['pm2_env']['created_at']/1000).astimezone(timezone))
            data[i]['uptime'] = f"{round(uptime.seconds/3600, 2)} hours"
        
            #data[i]['uptime'] = datetime.fromtimestamp(result[i]['pm2_env']['pm_uptime']/1000).astimezone(timezone).strftime('%m/%d %I:%M %p')
            data[i]['restart'] = result[i]['pm2_env']['restart_time']
            data[i]['location'] = str(result[i]['pm2_env']['PWD']).removeprefix('/home/mason-server/')
            
        else:
            data[i]['created'] = "DOWN"
            data[i]['uptime'] = "DOWN"
            data[i]['restart'] = "ERROR"
            data[i]['location'] = str(result[i]['pm2_env']['PWD']).removeprefix('/home/mason-server/')
    
    
        
    logger.error(f"{data}")
    
    context = {
        "data": data
    }
    
    return HttpResponse(template.render(context=context, request=requests))

def pm2Update(requests):
    if requests.method == "POST":
        data = json.loads((requests.body).decode("utf-8"))
        
        if data['task'] == "stop":
            result = subprocess.run(["pm2", "stop", f"{int(data['id'])}"], capture_output=True, text=True)
        
        elif data['task'] == "restart":
            result = subprocess.run(["pm2", "restart", f"{int(data['id'])}"], capture_output=True, text=True)
            
        elif data['task'] == "start":
            result = subprocess.run(["pm2", "start", f"{int(data['id'])}"], capture_output=True, text=True)
        
        else:
            return JsonResponse({
                "code": 404,
                "message": "unknown task"
            })
        
        return JsonResponse({
            "code": 200
        })
        
    else:
        return HttpResponse("only post")