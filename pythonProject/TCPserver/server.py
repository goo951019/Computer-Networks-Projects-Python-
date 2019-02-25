import socket
import pickle
import random

# Create a Socket
s = socket.socket()
s_name = "Jerry's server"
print("Socket successfully created")

# Port number
port = 1234

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print("Socket binded to port %s" %(port))



# While loop that listens to clients
connected = 1
while connected == 1:
    print("Waiting for client...")
    # Establish connection with client.
    c, address = s.accept()
    print('Got connection from', address)

    # receive client input and send receipt to the client
    try:
        arr = c.recv(4096)
        a = pickle.loads(arr)

        # print client name
        #       server name
        #       client int input
        #       random number generated
        #       sum
        print("Client Name: " + a[1])
        print("Server Name: " + s_name)
        n = int(a[0])
        r = random.randint(1, 100)
        add = n + r
        print("Sum of client's int (" + str(n) + ") and a random number (" + str(r) + ") is " + str(add))

        arr = [str(r), str(add), s_name]
        data = pickle.dumps(arr)
        c.send(data)
    except socket.error:
        print("Error Occured.")

    # Close the connection with the client
    print("Client Connection Closed")
    c.close()

    # Ask server to continue or terminate
    loop = ""
    while loop == "":
        close = str(input("Enter [C] to close server, else continue :"))
        if (close == 'C') or (close == 'c'):
            connected = 0
            loop = "S"
        else:
            loop = "S"

print("SERVER CLOSING...")
s.close()
