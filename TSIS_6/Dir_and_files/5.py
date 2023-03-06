l = [3, True, 'a', "Hello world!"]
f = open("file.txt", "w")
for i in l:
    f.write(str(i) + "\n")
f.close()