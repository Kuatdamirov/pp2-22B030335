n=int(input())
def fun_1():
    for i in range(n):
        if i%3==0 and i%4==0:
            yield i
for a in fun_1():
    print(a, end=", ")