import subprocess

test = subprocess.run(["tailscale", "status"], capture_output=True, text=True)

output = test.stdout.splitlines()

for i in range(len(output)):
    output[i] = output[i].split(" ")
    
for i in range(len(output)):
    output[i] = [item for item in output[i] if item != '']
    output[i] = output[i][:2]
    
    ping = subprocess.run(["tailscale", "ping", "--c", "1", "--timeout", "1s", f"{output[i][0]}"], capture_output=True, text=True)
    print(ping.stdout)
    
    if ("local" in ping.stdout) or ("pong" in ping.stdout):
        output[i].append(True)
        
    else:
        output[i].append(False)
    
print(output)