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

    # Adding mode header to the command
    encrypted_service = mode + " " + encrypted_service

    return encrypted_service

def service_response(encrypted_service, response):
    mode = encrypted_service.split(' ', 1)[0]
    encrypted_service = encrypted_service.split(' ', 1)[1]
    response = decrypt(mode, response)
    service = decrypt(mode, encrypted_service)
    if(service.split(' ')[0] == "DWD"):
        try:
            f = open('downloaded_file.txt', 'w')
            data = response.split(' ', 1)[1]
            response = response.split(' ', 1)[0]
            f.write(data)
            f.close()
            print("Response from server: ", response , "\nFile downloaded succesfully into downloaded_file.txt")
        except:
            print("Response from server: Status:NOK")
    elif(service.split(' ')[0] == "UPD"):
        print("Response from server: ", response , "\nFile uploaded succesfully to server")
    else:
        print("Response from server: ", response)

def supported_commands():
    return ''' 
The following services can be requested from the server:
    1. CWD - Retrieve the path of the current working directory for the user
    2. LS - List the files/folders present in the current working directory
    3. CD <dir> - Change the directory to <dir> as specified by the client
    4. DWD <file> - Download the <file> specified by the user on server to client
    5. UPD <file> - Upload the <file> on client to the remote server in CWD
    '''