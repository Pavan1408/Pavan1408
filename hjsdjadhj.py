n=int(input())
b=[]
a=[]
for i in range(n):
    a.append(int(input()))
for i in range(n):
    for j in range(n):
        if(a[i]==a[j]):
            if i==j:
                if(a[i]>=0):
                    b.append(a[i])
            else:
                a[j]=-1
print(len(b))
for j in b:
    print(j)