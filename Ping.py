import os

def ping(host):
    param = "-n 2"
    response = os.system(f"ping {param} {host} >nul 2>&1")

    return response == 0

# List of IP addresses to ping
ip_addresses = [
    "192.168.178.10",
    "192.168.178.11",
    "192.168.178.12",
    "192.168.178.13",
    "192.168.178.14"
]

# Ping each IP and print result
for ip in ip_addresses:
    if ping(ip):
        print(f"{ip} is reachable.")  #if value will be true
    else:   #if value will be false
        print(f"{ip} is not reachable.")
print ("*********end of code************")

