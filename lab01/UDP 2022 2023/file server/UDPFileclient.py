from socket import *

#create the socket
#AF_INET means that its an internet socket IPV4 sock stream
#SOCK_DGRAM indicates that is an UDP socket
clientSocket = socket(AF_INET,SOCK_DGRAM)

#specify the server name and the server port here we just have to know it
serverName="localhost"
serverPort= 12000

#message to the server or datagram
#A datagram is an independent, self-contained message sent over the network whose arrival, arrival time, and content are not guaranteed.
message=input("Input filename: ")


#encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used
#create a datagram with server IP address and port number (we just have to know both)
#envolves a call to DNS
#sends an aplication message to the socket
clientSocket.sendto( message.encode(),(serverName, serverPort))

#reads the message from the server using recvFrom()
#recieves the message and the IP adress of the server
modifiedMessage, serverAddres = clientSocket.recvfrom(2048)

#prints the message
print(modifiedMessage.decode())

clientSocket.close()