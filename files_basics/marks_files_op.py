# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:31:17 2019

@author: IIIT-rgukt
"""
''' working with random numbers and files
- % of students passed
- % of students failed
- % of students with distinction'''


from random import randint
def generatemarks(n,lb,ub):
    r=randint(lb,ub)
    f.write(r.__str__())
    for i in range(0,n-1,1):
        r=randint(lb,ub)
        f.write(" "+r.__str__())

def passed_percentage(filename,marks):
    count=0
    Passmarks=int(input("Enter pass marks  "))
    for i in range(0,len(marks),1):
        if marks[i]>=Passmarks:
            count+=1
    print("Pass percentage is ",int((count/n)*100),"%")
    
def failed_percentage(filename,marks):
    count=0
    Passmarks=int(input("Enter pass marks  "))
    for i in range(0,len(marks),1):
        if marks[i]<Passmarks:
            count+=1
    print("fail percentage is ",int((count/n)*100),"%")

        
def distinction(filename,marks):
    count=0
    dist=int(input("Enter distinction marks lower bound  "))
    for i in range(0,len(marks),1):
        if marks[i]>=dist:
            count+=1
    print("distinction percentage is ",int((count/n)*100),"%")

    

filename="C:/Users/IIIT-rgukt/Desktop/python_basics_apssdc/jupyter/marks.txt"
n=int(input("Enter how many student marks u want to geenrate "))
with open(filename,'r+') as f:
    generatemarks(n,0,100)
    
with open(filename,'r') as f:
    data=f.read()
    m=data.split(" ")
    marks=[]
    for i in range(0,len(m),1):
        marks=marks+[int(m[i])]
c=1
while c==1:
    print("\n1.List of marks\n2.Pass percentage\n3.Failed percentage\n4.Distinction percentage\n")
    value=int(input())
    if value==1:
        for i in range(0,len(marks),1):
            print(marks[i],end=" ")
        
    elif value==2:
        passed_percentage(filename,marks)
    elif value==3:
        failed_percentage(filename,marks)
    elif value==4:
        distinction(filename,marks)
    else:
        print("\nWrong input.Please enter correct input\n")

    print("\nEnter 1 to continue\nEnter 0 to exit\n")
    c=int(input())


    