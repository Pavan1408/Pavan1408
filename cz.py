import csv
fi="st.csv"
header=[]
rows=[]
with open(fi,'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(rows)
with open(fi, 'w') as file:
    for header in header:
        file.write(str(header)+', ')
    file.write('n')
    for row in rows:
        for x in row:
            file.write(str(x)+', ')
        file.write('n')