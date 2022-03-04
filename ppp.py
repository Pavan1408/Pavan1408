import pandas as p
df = p.read_csv(r'ti.csv')
f=p.DataFrame(df,columns=['no.. ','no.. '])
print(f)
import csv
fil=open('ti.csv')
#type(fil)
cs=csv.reader(fil)
header=[]
header=next(cs)
c=0
rows=[]
for row in cs:
    
    rows.append(row)
    c=c+1
for row in range(c-1):
    for col in range(len(header)+1):
        print(rows[col][row])
print(header)
print(rows)
fil.close()