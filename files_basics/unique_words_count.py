# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:09:05 2019

@author: IIIT-rgukt
"""

# count unique words in a text file
def unique_words_count(filename):
    dict={}
    count=0
    with open(filename,'r') as f:
        data=f.read().split()
        for j in range(0,len(data),1):
            if (data[j] in dict):
                 dict[data[j]]+=1
            else:
                dict[data[j]]=1
    for key,value in dict.items():
        if dict[key]==1:
            count=count+1
    print("we have ",count,"Unique words in file")
filename="C:/Users/IIIT-rgukt/Desktop/python_basics_apssdc/jupyter/data.txt"
unique_words_count(filename)