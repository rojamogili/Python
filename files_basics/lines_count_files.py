# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:54:47 2019

@author: IIIT-rgukt
"""

# Function to find number of lines in a particular file

def Line_count(filename):
    c=0
    with open(filename,'r') as f:
        data=f.readlines()
        for line in data:
            c=c+1
    print("File has ",c," number of lines\n")
filename="C:/Users/IIIT-rgukt/Desktop/python_basics_apssdc/jupyter/contacts.txt"
Line_count(filename)