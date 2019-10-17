import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print(IPAddr)
print("Your computer name is:" + hostname)
print("Your computer IP Address is:" + IPAddr)
