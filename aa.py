l=[]
def sq():
    n=int(input())
    if(n==1):
        a=int(input())
        l.append(a)

        print(l)
        sq()
    elif(n==2):
        if(l!=[]):
            l.reverse()
            l.pop()
            l.reverse()
            print(l)
            sq()
        else:
            print("queue emp")
            exit
    elif(n==3):
        print(l)
        sq()
    else:
        exit
sq()