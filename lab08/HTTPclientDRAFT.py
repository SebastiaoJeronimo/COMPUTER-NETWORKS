#!/usr/bin/env python3

# Importing libraries
from socket import *

#serverName = "localhost"
#serverPort = 8000
#print("Server info: ", serverName, str(serverPort))


# Ask file fig.jpg
msg1 = "GET fig.jpg HTTP/1.0\r\n"
msg2 = "host:localhost:8000\r\n"
msg3 = "\r\n"

s = socket(AF_INET,SOCK_STREAM)
s.connect((serverName, serverPort))
s.send((msg1+msg2+msg3).encode())

while True:
    # recebe dados do servidor
    # processa response message (header e body)
    

s.close()
print("Connection close")




