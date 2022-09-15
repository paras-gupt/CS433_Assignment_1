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

    # Server sends list of available services
    conn.send(supported_commands().encode())

    # Networking Layer
    mode = conn.recv(1024).decode()
    requested_service = conn.recv(1024).decode()

    # Crypto Layer and File Service Layer
    # if response_type(mode, requested_service) == "one":
    response = exec_service_server(mode, requested_service)

    # Networking Layer
    conn.send(response.encode())

    # elif response_type(mode, requested_service) == "dwd":
    #     response_file = exec_service_server(mode, requested_service)

    #     # Networking Layer
    #     f = open(response_file, 'r')
    #     l = f.read(1024)
    #     while (l):
    #         conn.send(encrypt(mode, l).encode())
    #         l = f.read(1024)
    #     f.close()

    # elif response_type(mode, requested_service) == "upd":
    #     server_socket.settimeout(10)
    #     f = open('uploaded_file.txt', 'w')
    #     while True:
    #         try:
    #             data = conn.recv(1024)
    #             print(data)
    #         except:
    #             print("File received from client")
    #             server_socket.settimeout(None)
    #             break

    #         response_data = decrypt(mode, data.decode())
    #         f.write(response_data)
    #     f.close()


