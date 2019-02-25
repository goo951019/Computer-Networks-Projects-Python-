#import socket module
from socket import *
import sys # in order to terminate the program

# Create Socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# port number
port = 8002

# bind to the port
serverSocket.bind(('', port))
print("Socket binded to port %s" %(port))

# Socket listening
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print("Connection from: ", addr)
    try:
        message = connectionSocket.recv(1024)
        print('message: ', message)
        if not message:
            print('Message was empty')
        else:
            filename = message.split()[1]
            print('filename: ', filename)
            f = open(filename[1:])
            outputdata = f.read()
            f.close()
            # Send one HTTP header line into socket
            connectionSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n', 'UTF-8'))
            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        print('404 Not Found')
        connectionSocket.send(bytes('HTTP/1.1 404 Not Found\r\n\r\n', 'UTF-8'))
        connectionSocket.send(bytes('<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n', 'UTF-8'))
        connectionSocket.close()
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data


