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

# if (response_type(mode, encrypted_service) == 'one'):
    # Networking Layer
response = client_socket.recv(1024).decode()
# File Service Layer, Crypto Layer
service_response(mode, response)

# elif (response_type(mode, encrypted_service) == 'dwd'):
#     client_socket.settimeout(5)
#     f = open('received_file.txt', 'w')
#     while True:
#         try:
#             data = client_socket.recv(1024)
#         except:
#             print("File downloaded on client")
#             break

#         response_data = decrypt(mode, data.decode())

#         f.write(response_data)

#     f.close()

# elif (response_type(mode, encrypted_service).split(' ')[0] == 'UPD'):
#     upload_file = response_type(mode, encrypted_service).split(' ')[1]
#     print(upload_file)

#     # Networking Layer
#     f = open(upload_file, 'r')
#     l = f.read(1024)
#     print(l)
#     while (l):
#         client_socket.send(encrypt(mode, l).encode())
#         l = f.read(1024)
#     f.close()
#     print('File uploaded to client')

client_socket.close()
print('Connection Closed')


# DWD test.txt