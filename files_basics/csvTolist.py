# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:44:55 2019

@author: IIIT-rgukt
"""

def csvTolist(filename):
    li=[]
    with open(filename,'r') as f:
        data=f.read()
        for line in data:
            li.append(line.split(' '))
    l=0          
    #for i in range(0,len(li),1):
     #   l=l+len(li[i]
    print(len(li))
    print(li)

filename="C:/Users/IIIT-rgukt/Desktop/python_basics_apssdc/jupyter/data.txt"
csvTolist(filename)
