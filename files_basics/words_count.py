# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:51:14 2019

@author: IIIT-rgukt
"""

#Funciton to count number of characters in a file including spaces and newlines
def word_count(filename):
    li=[]
    with open(filename,'r') as f:
        for line in f:
            li.append(line.split(' '))
    l=0          
    for i in range(0,len(li),1):
        l=l+len(li[i])

    print(l)

filename="C:/Users/IIIT-rgukt/Desktop/python_basics_apssdc/jupyter/data.txt"
word_count(filename)
