# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:41:44 2019

@author: IIIT-rgukt
"""

#Function to count number of characters in file
def char_count(filename):
    c=0
    with open(filename,'r') as f:
        for line in f:  
            for ch in line: 
                if ch!=" ":
                    c=c+1
    print("File has ",c," number of characters\n")
filename="C:/Users/IIIT-rgukt/Desktop/python_basics_apssdc/jupyter/data.txt"
char_count(filename)