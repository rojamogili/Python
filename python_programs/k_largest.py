# Exam problems problem number 3(easy)  K-th largest Frequency for string
def freqency_cal(s,k):
    d={}
    for i in range(0,len(s),1):
        if s[i] in d:
            d[s[i]]+=1
        else:
            d[s[i]]=1
    return d
def k_th_largest(values,d,k):
    values=list(set(values))
    values=sorted(values)
    if k<=len(values):
        sm=9999999999999
        for i in range(0,len(s),1):
            if d[s[i]]==values[-k]:
                if sm>=ord(s[i]):
                    sm=ord(s[i])
        print(chr(sm))
                
    else:
        print(-1)
    
t=int(input())
for i in range(0,t,1):
    s=input()
    k=int(input())
    d=freqency_cal(s,k)
    values=[]
    for key,value in d.items():
        values=values+[d[key]]
    #print(d)
    
    k_th_largest(values,d,k)
