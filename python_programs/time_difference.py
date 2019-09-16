
t=int(input())
for i in range(t):
    s=list(map(str,input().split()))
    t1=list(map(int,s[0].split(":")))
    t2=list(map(int,s[1].split(":")))
    h=t2[0]-t1[0]
    m=t2[1]-t1[1]
    s=t2[2]-t1[2]
    #print(h,m,s)
    if h==0:
        if m==0:
            if s==0:
                print("0 HOURS 0 MINUTES 0 SECONDS")
            elif s>0:
                print("0 HOURS 0 MINUTES",s,"SECONDS")
        elif m>0:
            if s<0:
                s=60+s
                m=m-1
                print("0 HOURS",m,"MINUTES",s,"SECONDS")
            else:
                print("0 HOURS",m,"MINUTES",s,"SECONDS")
    elif h>0:
        if m==0:
            if s<0:
                s=60+s
                m=m-1
                if m<0:
                    h=h-1
                    m=60+m
                print(h,"HOURS",m,"MINUTES",s,"SECONDS")
            else:
                print(h,"HOURS",m,"MINUTES",s,"SECONDS")

            
        elif m>0:
            if s<0:
                s=60+s
                m=m-1
                print(h,"HOURS",m,"MINUTES",s,"SECONDS")
            else:
                print(h,"HOURS",m,"MINUTES",s,"SECONDS")

        elif m<0:
            m=60+m
            h=h-1
            if s<0:
                s=60+s
                m=m-1
            print(h,"HOURS",m,"MINUTES",s,"SECONDS")
