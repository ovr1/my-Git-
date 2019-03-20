import pandas


df = pandas.read_csv("m5-access-log-all.csv")

print(df["ip"].value_counts())

print(df["ip"].value_counts().max())

#df.groupby(['A','B']).agg(['count', 'mean'])

print(len(df))

print(1733/41972*100)



