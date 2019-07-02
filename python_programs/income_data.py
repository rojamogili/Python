# Average income of all states from 2005 to 2013
#Average Income of all states from 2005 to 2013
#State with highest average income in the last three years
#State with lowest average income from 2007 to 2010(inclusive)
#Print the list of all states in the same line with average income less than California
#Print the names of states based on descending order of income in the year 2009
#State with the lowest recorded income from 2005 to 2013




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
    for key,values in d.items():
        d[key]=d[key]//dif
    return d


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
def list_of_income_lessthan_california(income,d):
    print("\nList of all states in the same line with average income lessthan california")
    cali=d['California']
    for key,value in d.items():
        if d[key]<cali:
            print(key,end="     ")
def income_descending_year(income,year):
    print("\n\nList of the names of states based on descending order of income in the year 2009")
    k=[]
    for i in income:
        k=k+[i]

    for i in range(0,len(k),1):
        if year==k[i]:
            s=i
    l=[]
    for i in income.values:
        l=l+[i]
    d={}
    value=[]
    for i in range(0,len(l),1):
        if l[i][1] not in d:
            d[l[i][1]]=l[i][s]
            value=value+[l[i][s]]
    #print(d)
    value=sorted(value)
    #print(value)
    for i in range(1,len(value)+1,1):
        for key,v in d.items():
            if v==value[-i]:
                print(key," - ",v)
                
def lowest_income_record(income,start,end):
    k=[]
    print()
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
    low=99999999999999
    for i in range(0,len(l),1):
        for j in range(s,e+1,1):
            if low>l[i][j]:
                low=l[i][j]
                name=l[i][1]
    print(name,"has lowest income ",low)
        
        
        
income=readCSVdata(filepath)
d=average_income(income)
s=0
c=0
for key,value in d.items():
    print(key," - ",value)
    s=s+value
    c=c+1
print("\nCombined income of all states average income is ",s)
average_of_3years(income)
lowest_income(income,'2007','2010')
list_of_income_lessthan_california(income,d)
income_descending_year(income,'2009')
lowest_income_record(income,'2005','2013')
