# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:54:17 2019

@author: IIIT-rgukt
"""

#Funciton to count number of alphabets in a file

def char_count(filename):
    c=0
    with open(filename,'r') as f:
        for line in f:  
            for ch in line: 
                if ch.isalpha()==True:
                    c=c+1
    print("File has ",c," number of alphabets\n")
filename="C:/Users/IIIT-rgukt/Desktop/python_basics_apssdc/jupyter/data.txt"
char_count(filename)