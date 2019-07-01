# Average income of all states from 2005 to 2013

filepath = 'Income.csv'
import pandas as pd
def readCSVdata(filepath):
    return pd.read_csv(filepath)

def average_income(income):
    print("Average income of every state from 2005 to 2013\n")
    l=[]
    for i in income.values:
        l=l+[i]
    #print(l)
    d={}
    dif=len(l[0])-2
    for i in range(0,len(l),1):
        if l[i][1] not in d:
            d[l[i][1]]=0
        for j in range(2,len(l[i]),1):
            d[l[i][1]]+=l[i][j]
    #print(d)
    for key,values in d.items():
        print(key,end="-")
        print(d[key]//dif)
def average_of_3years(income):
    l=[]
    for i in income.values:
        l=l+[i]
    d={}
    dif=3
    for i in range(0,len(l),1):
        if l[i][1] not in d:
            d[l[i][1]]=0
        for j in range(1,4,1):
            d[l[i][1]]+=l[i][-j]
    high=-1234
    for key,values in d.items():
        d[key]=d[key]//3
        if high<=d[key]:
            high=d[key]
            name=key
    print("\n",name," has highest income in last 3 years ",high)

def lowest_income(income,start,end):
    k=[]
    for i in income:
        k=k+[i]

    for i in range(0,len(k),1):
        if start==k[i]:
            s=i
        if end==k[i]:
            e=i
    l=[]
    for i in income.values:
        l=l+[i]
    d={}
    for i in range(0,len(l),1):
        if l[i][1] not in d:
            d[l[i][1]]=0
        for j in range(s,e+1,1):
            d[l[i][1]]+=l[i][j]
    diff=e-s+1
    low=9999999999999999999
    for key,values in d.items():
        d[key]=d[key]//diff
        if low>=d[key]:
            low=d[key]
            name=key
    print("\n",name,"has lowest average income ",low)

income=readCSVdata(filepath)
average_income(income)
average_of_3years(income)
lowest_income(income,'2007','2010')
