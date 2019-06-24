# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:10:13 2019

@author: IIIT-rgukt
"""

def unique_word_count(filename,word):
    c=0
    with open(filename,'r') as f:
        for line in f:
            words=line.split(" ")
            for i in range(0,len(words),1):
                if words[i]==word or words[i]==word+"\n":
                    c=c+1
    print(c)
filename="C:/Users/IIIT-rgukt/Desktop/python_basics_apssdc/jupyter/data.txt"
unique_word_count(filename,'roja')