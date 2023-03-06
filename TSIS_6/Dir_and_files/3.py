import os 
p=r'C:\Users\INTEKNO-PC4\Desktop\Dir_and_files'
try:
    os.access(p, os.F_OK)
    print("Files: ", [f for f in os.listdir(p) if os.path.isfile(p+'/'+f)])
    print("Directories: ", [f for f in os.listdir(p) if os.path.isdir(p+'/'+f)])
except FileNotFoundError:
    print('Path is not defined. Please, try again!')
finally:
    print("Everything is ok, don't worry)")