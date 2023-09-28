from socket import *

#creates the UDP socket
serverSocket = socket(AF_INET,SOCK_DGRAM)

serverPort= 12000

#server doesnt want its operating system to apoint a random port number to its socket because the client is going to contact him 
#from there from the server port 12000 in this case
#so with this method it assigns the port 12000 to this socket
#this code doesnt check for errors
serverSocket.bind(("",serverPort))

#loop
while  True:
    message, clientAddress = serverSocket.recvfrom( 2048 ) #receivs from client
    modifiedMessage = message.decode().upper()
    serverSocket.sendto( modifiedMessage.encode(), clientAddress)

serverSocket.close()
