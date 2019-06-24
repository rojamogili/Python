# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:20:48 2019

@author: IIIT-rgukt
"""

def read_file(filename):
    with open(filename,'r') as file:
        data=file.read()
        print(data)
def write_file(filename,filedata):
    with open(filename,'w') as file:
        file.write(filedata)
def append_Data(filename,filedata):
    with open(filename,'a') as file:
        file.write(filedata)

c=1
filename="C:/Users/IIIT-rgukt/Desktop/python_basics_apssdc/jupyter/contacts.txt"
while c==1:
    print("\n1.Read file\n2.Write Data into file\n3.Append data into file\n")
    value=int(input())
    if value==1:
        read_file(filename)
    elif value==2:
        filedata=input("Enter data to write into file  ")
        write_file(filename,filedata)
    elif value==3:
        filedata=input("Enter data to write into file  ")
        append_Data(filename,filedata)
    else:
        print("\n***********Wrong choice**********\n")
    print("\nEnter 1 to continue\nEnter 0 to exit\n")
    c=int(input())