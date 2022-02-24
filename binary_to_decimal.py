def bi(a):
    d=0
    c=1
    while(a>0):
        r=a%10
        d=d+(c*r)
        c=c*2
        a=a//10
    return d
a=int(input())
p=bi(a)
print(p)