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
for row in c:
    r.append(row)
    z=z+1
q=[]
f={}
# for i in range(5):
#     d[i]=[[],[]]
#     for j in range(2):
#         q=d[i][j]
#         for k in range(2):
#             w=r[i][j+1]
#                 s=w[:2]
#                 t=w[3:]
#                 u=(int(s)*60)+int(t) 

#             if(k%2==0):
#                 print(end=",")
for i in range(len(r)):
    m=1
    f[i]=[[],[]]
    for j in range(len(f[i])):
        q=f[i][j]
        for k in range(2):
            q[k]=r[i][m]
            m=m+1
print(f)            