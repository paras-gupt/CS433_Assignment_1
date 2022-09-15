import re
from client_crypt import *

def init_service_client():
    # Choose the encryption mode for sending and receiving data
    mode = encryption_mode()
    # Enter command to request service from server
    service = input('Enter service: ')

    if(service.split(' ')[0] == "UPD"):
        try:
            f = open(service.split(' ', 1)[1], 'r')
            service = "UPD " + f.read(2048)
            # print(service)
            f.close()
        except:
            service = "UPD"

    # Encrypt the requested service and send it to server
    encrypted_service = encrypt(mode, service)
    return mode, encrypted_service

def service_response(mode, encrypted_service, response):
    response = decrypt(mode, response)
    service = decrypt(mode, encrypted_service)
    if(service.split(' ')[0] == "DWD"):
        try:
            f = open('downloaded_file.txt', 'w')
            data = response.split(' ', 1)[1]
            response = response.split(' ', 1)[0]
            f.write(data)
            f.close()
            print("Response from server: ", response)
        except:
            print("Response from server: NOK")
    else:
        print("Response from server: ", response)

def supported_commands():
    return ''' The following commands are supported:
    1. CWD - Retrieve the path of the current working directory for the user
    2. LS - List the files/folders present in the current working directory
    3. CD <dir> - Change the directory to <dir> as specified by the client
    4. DWD <file> - Download the <file> specified by the user on server to client
    5. UPD <file> - Upload the <file> on client to the remote server in CWD
    '''