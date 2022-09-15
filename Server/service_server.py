import os
from server_crypt import *

def exec_service_server(mode, requested_service):
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
        dir = cmd.split(' ')[1]
        try:
            os.chdir(dir)
            response = "OK"
        except:
            response = "NOK"

    elif(cmd.split(' ')[0] == "DWD"): 
        try:
            f = open(cmd.split(' ')[1], 'r')
            response = "OK "+ f.read(2048)
            print(response)
            f.close()
        except:
            response = "NOK"

    elif(cmd.split(' ')[0] == "UPD"): 
        try:
            f = open('uploaded_file.txt', 'w')
            f.write(cmd.split(' ', 1)[1])
            f.close()
            response = "OK"
        except:
            response = "NOK"

    else: 
        response = "Service not available"

    return encrypt(mode, response)

def supported_commands():
    return ''' The following commands are supported:
    1. CWD - Retrieve the path of the current working directory for the user
    2. LS - List the files/folders present in the current working directory
    3. CD <dir> - Change the directory to <dir> as specified by the client
    4. DWD <file> - Download the <file> specified by the user on server to client
    5. UPD <file> - Upload the <file> on client to the remote server in CWD
    '''


