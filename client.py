import socket

# Create a socket object
client = socket.socket()

# Define the port and host on which you want to connect
port = 5050
host = '127.0.0.1'

# connect to the server on local computer
client.connect((host, port))
name = input("Enter your name : ")

client.send(name.encode("utf-8"))
# receive data from the server
print(client.recv(1024).decode("utf-8"))
# close the connection
client.close()











