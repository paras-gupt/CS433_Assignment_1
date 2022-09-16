import socket
from service_server import *      
from server_crypt import *             

port = 5000

# Set the connection using IPv4 over TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
server_socket.bind((host, port))

# Server can also listen to multiple clients simultanelously, if set
server_socket.listen()

print('Server listening....')


while True:
    conn, addr = server_socket.accept()
    print('Connection established with client having address: ', addr)

    # Networking Layer
    requested_service = conn.recv(1024).decode()

    # Crypto Layer and File Service Layer
    response = exec_service_server(requested_service)

    # Networking Layer
    conn.send(response.encode())

