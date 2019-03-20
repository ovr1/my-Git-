import pandas

#data = pandas.read_json("m5-access-log-100.json")
#s = data[-100:]["ip"]
#print(s)

data = pandas.read_csv("m5-access-log-all.csv")
N = data["ip"].value_counts()
print(N)
print((N[0]))


