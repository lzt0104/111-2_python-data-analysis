f = open("bodyinfo.csv", "r", encoding="utf-8")
rawdata = f.readlines()
f.close()

data = [item.split(",") for item in rawdata]
height = [int(d[1])for d in data]
weight = [int(d[2])for d in data]
print(data)

