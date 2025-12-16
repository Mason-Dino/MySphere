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
        
            logger.error(f"{datetime.fromtimestamp(result[i]['pm2_env']['created_at']/1000).astimezone(timezone)}")
            uptime = (datetime.fromtimestamp(time.time()).astimezone(timezone) - datetime.fromtimestamp(result[i]['pm2_env']['created_at']/1000).astimezone(timezone))
            logger.error(f"{uptime}")
            data[i]['uptime'] = f"{round(uptime.seconds/3600 + (uptime.days * 24), 2)} hours"
        
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

def machine(requests):
    template = loader.get_template("machine.html")
    
    logger = logging.getLogger("machines")
    logging.basicConfig(filename="viewTXT.log")
    
    out = subprocess.run(["tailscale", "status"], capture_output=True, text=True)

    output = out.stdout.splitlines()

    for i in range(len(output)):
        output[i] = output[i].split(" ")
        
    logger.error(f"Before: {output}")

    badIndex = 0
        
    for i in range(len(output)):
        try:
            output[i] = [item for item in output[i] if item != '']
            output[i] = output[i][:4]
            logger.error(f"Device {i}: {output[i]}")
            
            ping = subprocess.run(["tailscale", "ping", "--c", "1", "--timeout", "2s", f"{output[i][0]}"], capture_output=True, text=True)
            logger.error(ping.stdout)
            logger.error(badIndex)
            
            if ("local" in ping.stdout) or ("pong" in ping.stdout):
                output[i].append(True)
                
            else:
                output[i].append(False)

            badIndex += 1
            logger.error(f"Device {i}: {output[i]}")
        except:
            print("Failed")
            output[i].append(False)
            
    for i in range(len(output)):
        try:
            if output[i][1] == "mason" and output[i][3] == "linux":
                output[i][3] = "computer"
                
            elif output[i][3] == "windows" or output[i][3] == "macOS":
                output[i][3] = "computer"
                
            elif output[i][3] == "linux":
                output[i][3] = "server"
                
            elif output[i][3] == "iOS":
                output[i][3] = "phone"
        except: 
            pass

    badIndex -= 1

    print("hello world")
    logger.error(f"Total Output: {output}")
    context = {
        "machines": output
    }
    
    
    return HttpResponse(template.render(context=context, request=requests))

def pm2Update(requests):
    if requests.method == "POST":
        data = json.loads((requests.body).decode("utf-8"))
        
        if data['task'] == "stop":
            result = subprocess.run(["pm2", "stop", f"{int(data['id'])}"], capture_output=True, text=True)
        
        elif data['task'] == "restart":
            result = subprocess.run(["pm2", "restart", f"{int(data['id'])}"], capture_output=True, text=True)
            
        elif data['task'] == "delete":
            result = subprocess.run(["pm2", "delete", f"{int(data['id'])}"], capture_output=True, text=True)
            
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