l=""
for i in range(81):

    l[i]=input()
k=0
h=[[0]*9]*9
for i in range(9):
    for j in range(9):
        h[i][j]=l[k]
        k=k+1
        print(h[i][j],end=",")
    print()
