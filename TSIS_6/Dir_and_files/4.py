try:
    file = open('hello.txt')
    lines = 0
    for line in file:
        lines += 1
    print("Lines:", lines)
except FileNotFoundError:
    print("Не нашел я такой файл!")
finally:
    print("Программа завершена успешно")