import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"HostName : { hostname }")
print(f"IP Address : {ip_address}")