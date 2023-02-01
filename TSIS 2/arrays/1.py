cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)
cars[0] = "Toyota"
print(cars[0])
y = len(cars)
for a in cars:
  print(a)
cars.append("Honda")
print(cars)
cars.pop(1)
print(cars)
cars.remove("Volvo")
print(cars)