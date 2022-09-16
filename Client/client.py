import socket
from service_client import *
from client_crypt import *

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           
host = socket.gethostname()    
port = 5000            

# Supported Commands list
print(supported_commands())

# File Service Layer, Crypto Layer
encrypted_service = init_service_client()

print("\nEstablish connection with Server..")
client_socket.connect((host, port))
print("Connection established.\n")

# Networking Layer
client_socket.send(encrypted_service.encode())

# Networking Layer
response = client_socket.recv(1024).decode()
# File Service Layer, Crypto Layer
print("--------------------")
service_response(encrypted_service, response)
print("--------------------")

client_socket.close()
print('\nService response received. Connection is now closed')


# DWD test.txt