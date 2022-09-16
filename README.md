# CS 433 Computer Networks
### Assignment 1
### Network Application using Socket Programming

Start the server and the client socket files in separate terminal windows.

```python
  # Start the server in one terminal window
  cd Server
  python server.py
  
  # Start the client in another terminal window
  cd Client
  python client.py
```

Once the server and the client are up running, the client displays a list of available services that can be requested from the server. 
  1. CWD - Retrieve the path of the current working directory for the user
  2. LS - List the files/folders present in the current working directory
  3. CD &lt; dir &gt; - Change the directory to <dir> as specified by the client
  4. DWD &lt; file &gt; - Download the <file> specified by the user on server to client
  5. UPD &lt;file &gt; - Upload the <file> on client to the remote server in CWD

The client then asks to choose one of the following encryption methods for encrypting any service request and data shared between the client and the server.
  1. Plain text: Mode 1
  2. Substitute: Mode 2
  3. Transpose: Mode 3

Enter the encryption mode to continue. The client next asks for the service that is to be requested from the server.

```
  Enter encryption mode: 2
  Enter service: LS
```

The client now establishes a connection with the server and requests the service. The following is the response of the requested service as received from server. 
  
```
  Response from server:  C:\Users\Paras_Gupta\CS433_Assignment_1\Server
```
  
The ouput above is the path of the current working directory of the server, as was expected.
  
Once, the response is displayed, the service execution completes and the connection between client and server closes. However, the server continues to run and waits for other service requests from clients. The connection between the client and the server is thus **non-persistent** in nature.

The user can restart the client to establish the client-server connection once again, and see the outputs for more of the supported commands.

