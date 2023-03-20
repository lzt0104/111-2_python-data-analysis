f = open("hello.dat", "w" ,encoding="utf-8")
for i in range(5):
    f.write("Hello World\n")
f.close()