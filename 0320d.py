import csv
with open("bodyinfo.csv",encoding="utf-8") as fp:
    datareader = csv.DictReader(fp)
print