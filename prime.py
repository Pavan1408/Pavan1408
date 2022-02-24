def pr(l):
    c=0
    for i in range(2,l):
        if((l%i)==0):
            c=c+1
    if(c==0):
        return 0
    else:
        return 1
l=int(input())
p=pr(l)
if(p==0):
    print("prim")
else:
    print("not")