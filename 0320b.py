f = open("data.txt","r",encoding="UTF-8")
data = f.readlines()
f.close()

scores = [int(d) for d in data]
print("Max:",max(scores))
print("Min:",min(scores))
print("Average:",round(sum(scores)/len(scores),2))


print(data)
print(scores)
