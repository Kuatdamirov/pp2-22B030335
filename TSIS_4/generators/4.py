a=int(input())
b=int(input())
s=[]
def fun_2():
    for i in range(a, b+1):
        yield i**2
for el in fun_2():
    s.append(el)
print(s)
        