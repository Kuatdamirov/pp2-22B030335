from time import sleep
from math import sqrt
def fun_1(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
print("Square root after specific miliseconds:") 
print(fun_1(lambda x: sqrt(x), 1000, 16))