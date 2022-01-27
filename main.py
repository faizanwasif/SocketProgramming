# first of all import the socket library
import socket

# set up the host and port
# localhost same as 127.0.0.1
host = "localhost"
# select a port which is free
port = 5050

# Identify the sockets address family like ipv4 in this case
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

""" The code still works without (socket.AF_INET, socket.SOCK_STREAM) but if you are creating a multi client system 
    then you need it.
"""

# bind the server to the address
server.bind((host, port))
# put server in listening mode
server.listen()

print("socket is listening")

while True:
    """Use try and except method to tackle errors and exceptions"""
    try:
        client, addr = server.accept()

        name = client.recv(1024).decode("utf-8")

        print('Got connection from', addr, name)

        # send a message to client.
        # use encode and decode to convert bytes to strings
        client.send('Connected Successfully'.encode("utf-8"))
        # Close the connection with the client
        client.close()
    except Exception as e:
        print("[Exception]", e)






#






