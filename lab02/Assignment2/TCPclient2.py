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

    client_number = input("Input interger: ")             # take input Integer between 1 and 100
    client_name = input("please input a random name: ")   # asks for a name in input
    message = client_name+":"+client_number               # transform number in string
    
    clientSocket.send(message.encode())             # send user's sentence
                                                    # over TCP connection

    server_sentence = clientSocket.recv(sockBuffer).decode()  # receive response
    print("Message received: ", server_sentence)              # server sentence

    array = server_sentence.split(":") #split the server sentence 
    server_name = array[0]
    server_number = array[1]
    sum_numbers = array[2]

    print("Server Name: ",server_name) # print the name of the server
    print("Client Name: ",client_name) # print the client name

    print("client number :" ,client_number) # print the client number
    print("server number :", server_number) # print the server number
    print("sum of both numbers :", sum_numbers) # print sum of both numbers
    
    clientSocket.close()            # close TCP connection

main()
