import glob
import subprocess
import os

files = glob.glob("/dev/sd*")
usb = []

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
        print(f"Successfully mounted /dev/{device} at {mount_point}")
    else:
        print(f"Failed to mount /dev/{device}")
        os.removedirs(mount_point)

# Print the list of USB devices found
print("Found USB devices:", files)
