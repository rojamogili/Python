# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 11:05:40 2019

@author: IIIT-rgukt
"""

import re
def mail_validator(mail):
    pattern='^[a-zA-Z0-9][0-9a-zA-Z_.]{5,14}[0-9a-zA-Z](@)[0-9a-zA-Z]{2,15}(.)[a-z]{2,4}'
    if re.match(pattern,mail):
        return True
    else:
        return False
    
def PhoneNumber_validator(number):
    pattern='^[6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$|^[0][6-9][0-9]{9}$'
    if re.match(pattern,number):
        return True
    else:
        return False


def add_contact(name,phone,email):
    #store datas name, phone,email in the contact text file
    filename="C:/Users/IIIT-rgukt/Desktop/python_basics_apssdc/jupyter/contacts.txt"
    if not checkContactExists(name):
        p=phone.__str__()
        if PhoneNumber_validator(p)==True and mail_validator(email)==True:
            with open(filename,'a') as f:
                line=name+','+str(phone)+','+email+"\n"
                f.write(line)
        print(name,'added to contact list')
    else:
        print(name,'already exists')
    return

#Function to check if contact already exists
def checkContactExists(name):
    filename="C:/Users/IIIT-rgukt/Desktop/python_basics_apssdc/jupyter/contacts.txt"
    with open(filename,'r') as f:
        data=f.read()
        pattern=name+','
    print(re.search(pattern,data))
    return re.search(name,data)



def search(filename,name):
    with open(filename,'r')as f:
        lines=f.readlines()
        pattern=name+","
        for name in lines:
            if re.search(pattern,name):
                print(name)
def delete_contact(filename,name):
    with open(filename,'r+') as f:
        data=f.readlines()
        f.seek(0)
        for line in data:
            if name not in line:
                f.write(line)
        f.truncate()
        
def list_of_contacts(filename):
    with open(filename,'r') as f:
        data=f.readlines()
        for line in data:
            print(line,end="")

def update_contact(filename,name):
    j=0
    with open(filename,'r') as f:
        data=f.readlines()
        f.seek(0)
        for line in data:
            if name in line:
                delete_contact(filename,name)
                
                new_name=input("Enter new name  ")
                phone=int(input("Enter Phone number  "))
                email=input("Enter email address  ")
                
                add_contact(new_name,phone,email)
                j=1
                print("Cotnact updated")
    if j!=1:
        print("\nTheir is no such contact exist.Please check the name\n")
    
    
c=1
filename="C:/Users/IIIT-rgukt/Desktop/python_basics_apssdc/jupyter/contacts.txt"
while c==1:
    print("\n1.Add contact\n2.list of contacts\n3.Delete contact\n4.search for a contact\n5.Update a contact")
    value=int(input())
    if value==1:
        name=input("Etner name to add  ")
        phone=int(input("Etner phone number  "))
        email=input("Etner email address  ")
        add_contact(name,phone,email)
    elif value==2:
        list_of_contacts(filename)
    elif value==3:
        name=input("Etner name to delete ")
        delete_contact(filename,name)
    elif value==4:
        name=input("Enter name to search for a contact")
        search(filename,name)
    elif value==5:
        name=input("Etner name to update contact info ")
        update_contact(filename,name)
        
    print("\nEnter 1 to continue\nEtner 0 to exit\n") 
    c=int(input())