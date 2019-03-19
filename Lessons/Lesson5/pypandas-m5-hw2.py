import pandas
import json

freq_dict = {}
data = pandas.read_json("m5-access-log-100.2.json")
print(data["ip"].value_counts())

with open("m5-access-log-100.2.json") as fp:
    data = json.load(fp)
    print(len(data))

    for record in data:
        print(record["ip"], record["timestamp"],record["user-agent"])
        #print(record["ip"], record["timestamp"],record["user-agent"])
    for record in data:
        if record["ip"] in freq_dict:
            freq_dict[record["ip"]] = freq_dict[record["ip"]] + 1
        else:
            freq_dict[record["ip"]] = 1
    for ip in freq_dict:
        f = freq_dict[ip]
        print(f)
        if f == 54:
            print(ip)

