import pandas

freq_dict = {}
data = pandas.read_json("m5-access-log-100.2.json")
print("ip: ",data["ip"].max())
print("user-agent: ",data["user-agent"].max())
print("timestamp: ",data["timestamp"].max())
print(data["ip"].value_counts().max())
print(len(data))





