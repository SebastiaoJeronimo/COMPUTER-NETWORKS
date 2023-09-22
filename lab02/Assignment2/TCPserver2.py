#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: cpm
"""
from socket import *

serverPort = 12000
sockBuffer = 2048

def main():

    serverSocket = socket(AF_INET,SOCK_STREAM)   # create TCP welcoming socket
    serverSocket.bind(("", serverPort))

    serverSocket.listen(1)              # begin listening for incoming TCP requests
    print("Server is running")

    while True:
        connSocket, addr = serverSocket.accept()    # waits for incoming requests:
                                                    # new socket created on return
        print("Connected by: ", str(addr))

        sentence = connSocket.recv(sockBuffer).decode()     # read a sentence of bytes
                                                            # received from client
  
        print("Data from connected user: ", sentence)       # display received sentence


        if (number < 1 or number > 100):          #checks if the number is valid
            print("invalid number please put a number between 1 and 100")
            return
        
        sentenceUpper = sentence.upper()                    # convert to upper case
    
        connSocket.send(sentenceUpper.encode())             # send modified sentence over
                                                            # TCP connection

        connSocket.close()      # close TCP connection:
                                # the welcoming socket continues

main()
