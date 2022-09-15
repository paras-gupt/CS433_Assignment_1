from asyncio.windows_events import NULL
import socket
from service_client import *
from client_crypt import *

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           
host = socket.gethostname()    
port = 5000            
client_socket.connect((host, port))

# Supported Commands received from server
print("Server says: \n", client_socket.recv(1024).decode())

# File Service Layer, Crypto Layer
mode, encrypted_service = init_service_client()

# Networking Layer
client_socket.send(mode.encode())
client_socket.send(encrypted_service.encode())

# Networking Layer
response = client_socket.recv(1024).decode()
# File Service Layer, Crypto Layer
service_response(mode, encrypted_service, response)


client_socket.close()
print('Connection Closed')


# DWD test.txt