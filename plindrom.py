def pa(a):
    f=a
    d=0
    while(a>0):
        r=a%10
        d=d*10+r
        a=a//10
    if(f==d):
        return 0
    else:
        return 2



a=int(input())
p=pa(a)
if(p==0):
    print("palindrom")
else:
    print("not a palindrm")