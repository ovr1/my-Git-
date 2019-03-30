import csv
rows = []
S =[]
with open("m5-access-log-all.csv") as fp:
    reader = csv.reader(fp)
    for row in reader:
        rows.append(row)
    for row in rows[1:]:
        if "23.101.169.3" in row:
            print(row[1]+ " ' " + row[0] + " ' " + row[2])
            S.append(row)

print("S = ",len(S))
print("N = ", len(rows))

