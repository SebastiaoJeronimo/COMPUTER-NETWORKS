#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: cpm
"""
import sys  #needed to access the command-line arguments

def main():
    print("Testing ... ")
    n = len(sys.argv)       #get number of arguments
    
    print("Number of arguments: ",n-1)
    print("Argument list: ")
    
    for i in range(1,n):    #list all arguments
        print(str(sys.argv[i]))
    
if __name__ == "__main__":  #check if the module is being run as the main program
    main()