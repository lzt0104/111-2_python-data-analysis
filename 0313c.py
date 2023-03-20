f = open("bodyinfo.csv","r",encoding="utf-8")
data = f.readlines()
f.close()
for item in data:
    name , h ,w =item.split(",")
    print(name, round(int(w)/(int(h)/100)**2 , 2))