t=int(input())
d={}
for i in range(0,t,1):
    u=input()
    if u in d:
        d[u]+=1
    else:
        d[u]=1
print(d)
values=[]
for key,value in d.items():
    values=values+[d[key]]
print(len(values))
for i in range(0,len(values),1):
    m=max(values)
    v=[]
    for key,value in d.items():
        if d[key]==m:
            v=v+[key]
    v=sorted(v)
    for j in range(0,len(v),1):
        print(v[j])
    for j in range(0,len(values),1):
        if values[j]==m:
            values[j]=0
