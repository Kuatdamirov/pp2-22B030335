from math import pi
n=int(input())
def to_radian(int):
    return (int*pi)/180
print(round(to_radian(n), 6))