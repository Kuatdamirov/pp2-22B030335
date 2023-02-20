import math
n=int(input())
def even():
    for x in range(n):
        if x%2==0:
            yield x
for i in even():
    print(i, end=", ")
