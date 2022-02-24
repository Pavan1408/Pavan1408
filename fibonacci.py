def fi(leng):
    c=0
    d=1
    f=[]
    f.append(c)
    f.append(d)
    for i in range(2,leng):
        m=f[i-1]+f[i-2]
        f.append(m)
    return f
leng=int(input())
p=fi(leng)
print(p)