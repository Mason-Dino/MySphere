from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.template import loader
import os
import glob
import subprocess
import logging

# Create your views here.
def getValidUSB():
    logger = logging.getLogger("getValidUSB")
    logging.basicConfig(filename="viewTXT.log")
    
    files = glob.glob("/dev/sd*")
    logger.error(f"usb device: {files}")
    
    usb = []
    validUSB = []

    for file in files:
        usb.append(file.removeprefix('/dev/'))


    for device in usb:
        mount_point = f"/home/mason-server/usb-{device}"
        
        if not os.path.exists(mount_point):
            os.makedirs(mount_point)

    # Mount each USB device
    for i, device in enumerate(usb):
        mount_point = f"/home/mason-server/usb-{device}"
        
        # Mount the device
        result = subprocess.call(["sudo", "mount", f"/dev/{device}", mount_point])
        
        if result == 0:
            logger.error(f"Successfully mounted /dev/{device} at {mount_point}")
            result = subprocess.call(["sudo", "umount", mount_point])
            
            if result == 0:
                try:
                    os.removedirs(mount_point)
                except:
                    pass
            
            validUSB.append(device)
            logger.error(validUSB)
        else:
            print(f"Failed to mount /dev/{device}")
            try:
                os.removedirs(mount_point)
            except:
                pass
            
    return validUSB



def home(requests):
    template = loader.get_template('home-usb.html')
    
    context = {
        "usb": getValidUSB()
    }
    
    return HttpResponse(template.render(context=context, request=requests))