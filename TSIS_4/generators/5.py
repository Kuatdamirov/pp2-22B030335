n=int(input())
def fun_4():
    for i in range(n, 0, -1):
        yield i
for a in fun_4():
    print(a)