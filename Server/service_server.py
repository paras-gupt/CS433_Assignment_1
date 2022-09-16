import os
from server_crypt import *

def exec_service_server(requested_service):
    mode = requested_service.split(' ', 1)[0]
    requested_service = requested_service.split(' ', 1)[1]
    cmd = decrypt(mode, requested_service)
    response = ""

    if(cmd == "CWD"): 
        response = os.getcwd()

    elif(cmd == "LS"): 
        lst = os.listdir()
        str = "List of directories \n"
        for i in lst:
            str += i + "\n"
        response = str

    elif(cmd.split(' ')[0] == "CD"): 
        dir = cmd.split(' ', 1)[1]
        try:
            os.chdir(dir)
            response = "Status:OK"
        except:
            response = "Status:NOK"

    elif(cmd.split(' ')[0] == "DWD"): 
        try:
            f = open(cmd.split(' ', 1)[1], 'r')
            response = "Status:OK "+ f.read(2048)
            # print(response)
            f.close()
        except:
            response = "Status:NOK"

    elif(cmd.split(' ')[0] == "UPD"): 
        try:
            f = open('uploaded_file.txt', 'w')
            if(len(cmd.split(' ')) == 1):
                response = "Status:NOK"
            else:
                f.write(cmd.split(' ', 1)[1])
                f.close()
                response = "Status:OK"
        except:
            response = "Status:NOK"

    else: 
        response = "Service not available"

    return encrypt(mode, response)


