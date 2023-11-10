#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: cpm
"""
from socket import *

serverName = "localhost"            # server name
serverPort = 12000                  # socket server port number
sockBuffer = 2048                   # socket buffer size

def main():
    clientSocket = socket(AF_INET,SOCK_STREAM)       # create TCP socket
    clientSocket.connect((serverName, serverPort))   # open TCP connection

    
    sentence = input("Input lowercase sequence: ")   # take input

    clientSocket.send(sentence.encode())             # send user's sentence
                                                 # over TCP connection

    modifiedSentence = clientSocket.recv(sockBuffer).decode()  # receive response
    print("Message received: ", modifiedSentence)
    
    clientSocket.close()            # close TCP connection

main()
