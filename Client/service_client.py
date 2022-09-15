from client_crypt import *

def init_service_client():
    # Choose the encryption mode for sending and receiving data
    mode = encryption_mode()
    # Enter command to request service from server
    service = input('Enter service: ')
    # Encrypt the requested service and send it to server
    encrypted_service = encrypt(mode, service)
    return mode, encrypted_service

def service_response(mode, response):
    response = decrypt(mode, response)
    print("Response from server: ", response)

# def response_type(mode, encrypted_service):
#     service = decrypt(mode, encrypted_service)
#     if(service.split(' ')[0] == 'DWD'):
#         return 'dwd'
#     elif(service.split(' ')[0] == 'UPD'):
#         return service
#     else:
#         return 'one'