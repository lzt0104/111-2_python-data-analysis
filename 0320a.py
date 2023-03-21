f = open("data.txt","a",encoding="UTF-8")
score = int(input("請輸入成績：(-1結束)"))

while score != -1:
    f.write("{}\n".format(score))
    score = int(input("請輸入成績：(-1結束)"))
