import json

from numpy.distutils.fcompiler import none

freq_dict = {}
N =[]

with open("m5-access-log-100.json") as fp:
    data = json.load(fp)
#print(data)

    #for record in data:
        #print(record["ip"], record["timestamp"])


    for record in data:
        if record["ip"] in freq_dict:
            freq_dict[record["ip"]] = freq_dict[record["ip"]] + 1
        else:
            freq_dict[record["ip"]] = 1

    for ip in freq_dict:
        f = freq_dict[ip]
        if f ==1:
            print(f)