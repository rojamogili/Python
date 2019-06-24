# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 18:41:46 2019

@author: IIIT-rgukt
"""

def remove_contact(filename,name):
    with open(filename,'r+') as f:
        data=f.readlines()
        f.seek(0)
        for line in data:
            if name not in line:
                f.write(line,end="")
        f.truncate()
filename="C:/Users/IIIT-rgukt/Desktop/python_basics_apssdc/jupyter/contacts.txt"
remove_contact(filename,"lally1")