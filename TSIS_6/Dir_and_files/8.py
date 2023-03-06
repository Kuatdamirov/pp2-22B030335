import os
try:
    os.access(r'C:\Users\INTEKNO-PC4\Desktop\Dir_and_files\a.txt', os.F_OK)
    os.remove(r'C:\Users\INTEKNO-PC4\Desktop\Dir_and_files\a.txt')
except FileNotFoundError:
    print('Как ты собираешься удалить то, чего нет?')