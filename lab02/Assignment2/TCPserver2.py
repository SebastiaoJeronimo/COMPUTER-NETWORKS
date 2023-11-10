#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: cpm
"""
from socket import *
from random import *

serverPort = 12000
sockBuffer = 2048

def main():

    serverSocket = socket(AF_INET,SOCK_STREAM)   # create TCP welcoming socket
    serverSocket.bind(("", serverPort))

    serverSocket.listen(1)              # begin listening for incoming TCP requests
    print("Server is running")

    server_number = randint(1, 120) # get random number i chosed 120 to get some random numbers that exceed 100
    print(server_number)                  # print for DEBUG
    server_name = "Jhon the server"       # random name 
    print(server_name)                    # print for DEBUG

    while True:
        connSocket, addr = serverSocket.accept()    # waits for incoming requests:
                                                    # new socket created on return
        print("Connected by: ", str(addr))

        client_sentence = connSocket.recv(sockBuffer).decode()     # read a sentence of bytes
                                                                   # received from client
        
        # print("Data from connected user: ", sentence)       # display received sentence

        array = client_sentence.split(":")                # split the sentence by the separator :
        client_number_in_str = array[1]            # get the number of the client
        client_number = int(client_number_in_str)  # transform the number into an int
        client_name = array[0]                     # get the client name
        sum_of_numbers = client_number + server_number

        print("number of client :", client_number)                    # display number of client
        print("number of server :", server_number)                    # display number of client
        print("sum of both numbers :",sum_of_numbers)                 # display the sum of both numbers
        
        print("name of client :", client_name)        # display name of client
        print("name of server :", server_name)        # display name of server


        if (client_number < 1 or client_number > 100):          #checks if the number is valid
            print("invalid number please put a number between 1 and 100")
            #maybe send something to the client to tell them the number is invalid
            connSocket.close()  # close the socket
            break               # exits the loop
        
        #create server sentence
        server_sentence = server_name+":"+str(server_number)+":"+str(sum_of_numbers)     
        connSocket.send(server_sentence.encode())           # send modified sentence over
                                                            # TCP connection

        connSocket.close()      # close TCP connection:
                                # the welcoming socket continues

main()
