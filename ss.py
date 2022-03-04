import csv
import pandas as p
df=p.read_csv(r'data.csv')
print(df)
print('who you want to schd a meet or ne:')
f=open('data.csv')
c=csv.reader(f)
header=[]
header=next(c)
z=0
o=0
f={}
r=[]
d=[]
for row in c:
    r.append(row)
    z=z+1
a=input()
while a=='y':
    #o=o+1
    if(a=='y'):
        
        b=int(input())
        for i in range(b):
            d.append(int(input()))
        y=float(input())
        m=int(y*60)
        # for i in range(b):
        #     for j in range(z):
        #         if(j==d[i]):
                    # w=r[j]
                    # v=w[1:3]
                    # u=v[0][3:]
                    # t=u+m
        for i in range(z):
            g=[]
            f[i]=[]
            for j in range(4):
                w=r[i][j+1]
                s=w[:2]
                t=w[3:]
                u=(int(s)*60)+int(t) 
                #e=g.append(u)
                f[i].append(u)
        print(f)
        hero=[]
        start=0
        end=2000
        for i in range(b):
            hero=f[d[i]-1]
            #for j in range(0,2*o-1,2):
            if(hero[0]>start):
                start=hero[0]
                if(hero[1]<end):
                    end=hero[1]
        if((end-start)>=m):
            print('the meeting is place at',end=" ")
            print(start,end=" ")
            print("to",end=" ")
            print(start+m)
            # for i in range(b):
            #     f[d[i]-1][1]=f[d[i]-1][1]-m    
        else:
            start=0
            end=2000
            for i in range(b):
                hero=f[d[i]-1]
                if(hero[2]>start):
                    start=hero[2]
                    if(hero[3]<end):
                        end=hero[3]
            if((end-start)>=m):
                print('the meeting is place at',end=" ")
                print(start,end=" ")
                print("to",end=" ")
                print(start+m)
                # for i in range(b):
                #     f[d[i]-1][3]=f[d[i]-1][3]-m  
        