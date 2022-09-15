import re
from client_crypt import *

def init_service_client():
    # Choose the encryption mode for sending and receiving data
    mode = encryption_mode()
    # Enter command to request service from server
    service = input('Enter service: ')

    if(service.split(' ')[0] == "UPD"):
        f = open(service.split(' ')[1], 'r')
        service = "UPD " + f.read(2048)
        # print(service)
        f.close()

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
