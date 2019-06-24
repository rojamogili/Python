# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:48:46 2019

@author: IIIT-rgukt
"""

#Funciton to count number of characters in a file including spaces and newlines
def char_count_includespaces(filename):
    li=[]
    with open(filename,'r') as f:
        data=f.read()
        for line in data:
            li.append(line.split(' '))
    l=0          
    #for i in range(0,len(li),1):
     #   l=l+len(li[i]
    print(len(li))

filename="C:/Users/IIIT-rgukt/Desktop/python_basics_apssdc/jupyter/data.txt"
char_count_includespaces(filename)
