import subprocess

test = subprocess.run(["tailscale", "status"], capture_output=True, text=True)

output = test.stdout.splitlines()

for i in range(len(output)):
    output[i] = output[i].split(" ")
    
for i in range(len(output)):
    output[i] = [item for item in output[i] if item != '']
    
print(output)