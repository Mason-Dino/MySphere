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
    
    for item in result:
        logger.error(f"{item}")
        logger.error(f"{item['name']}")
        logger.error(f"{item['pm_id']}")
        logger.error(f"{item['pm2_env']['status']}")
        logger.error(f"created: {item['pm2_env']['created_at']} uptime: {item['pm2_env']['pm_uptime']}")
        logger.error(f"{item['pm2_env']['restart_time']}")
        logger.error(f"{item['pm2_env']['PWD']}")
    
    return HttpResponse(template.render(request=requests))