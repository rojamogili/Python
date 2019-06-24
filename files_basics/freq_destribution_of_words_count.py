# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:09:51 2019

@author: IIIT-rgukt
"""

# Frequency distribution of words in a file(count each word how many times it was occured)
def freq_destribution_of_words(filename):
    dict={}
    with open(filename,'r') as f:
        data=f.read().split()
        
        for j in range(0,len(data),1):
            if (data[j] in dict):
                 dict[data[j]]+=1
            else:
                dict[data[j]]=1
    print(dict)
    for key,value in dict.items():
        print(key,":",value)

filename="C:/Users/IIIT-rgukt/Desktop/python_basics_apssdc/jupyter/data.txt"
freq_destribution_of_words(filename)