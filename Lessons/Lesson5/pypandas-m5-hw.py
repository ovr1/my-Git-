import pandas

#data = pandas.read_json("m5-access-log-100.json")
#s = data[-100:]["ip"]
#print(s)

data = pandas.read_json("m5-access-log-100.json")
N = data["ip"].value_counts()
print((N[0]+N[1]+N[2]),'%')


