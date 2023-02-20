import math
height=int(input())
first_value=int(input())
second_value=int(input())
def trapezoid(h, a, b):
    return ((a+b)/2)*h
print(trapezoid(height, first_value, second_value))