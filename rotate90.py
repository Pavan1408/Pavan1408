r=int(input())
col=int(input())
d=[[int(input()) for i in range(col)] for j in range(r)]
'''for i in range(r):
    f=[]
    for j in range(col):
        f.append(int(input()))
    d.append(f)'''
for k in range(col):
    n=r-1
    while(n>=0): 
        print(d[n][k],end=" ")
        n=n-1
    print()