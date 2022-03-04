import csv
import pandas as p
df=p.read_csv(r'data.csv')
print(df)
f=open('data.csv')
c=csv.reader(f)
header=[]
header=next(c)
z=0
o=0
f={}
r=[]
for row in c:
    r.append(row)
    z=z+1
q=[]
f={}
d=[]
sl=[]
for i in range(len(r)):
    m=1
    f[i]=[[0]*2,[0]*2]
    for j in range(2):
        q=f[i][j]
        for k in range(2):
            w=r[i][m]
            v=(int(w[:2]))*60+(int(w[3:]))
            q[k]=v
            m=m+1
print(f)
print('who you want to schd a meet or ne:')
a=input()
while a=='y':
    if(a=='y'):
        flags=0
        print('plea enter how man memb')
        b=int(input())
        for i in range(b):
            d.append(int(input()))
        print("minutes in")
        n=int(input())
        for i in range(b):
            q=f[d[i]-1]
            for j in range(len(q)):
                sl.append(q[j][0])
        sl.sort()
        for k in range(len(sl)):
            x=0
            for i in range(b):
                for j in range (len(f[d[i]-1])):
                    q=f[d[i]-1]
                    if(q[j][0]<=sl[k] and q[j][1]>=(sl[k]+n)):
                        x=x+1
                        if(b==x):
                            print(sl[k],(sl[k]+n))
                            h=sl[k]
                            s=sl[k]+n
                            flags=1
            if(flags==1):
                break
        for i in range(b):
            g=[0]*2
            for j in range(len(f[d[i]-1])):
                q=f[d[i]-1]
                if(q[j][1]>=s and h>=q[j][0]):
                    g[1]=q[j][1]
                    q[j][1]=h
                    g[0]=s
                    print(g)
                    f[d[i]-1].insert(j+1,g)
                    if(f[d[i]-1][j][0]==f[d[i]-1][j][1]):
                        del f[d[i]-1][j]
                        for
    a=input()