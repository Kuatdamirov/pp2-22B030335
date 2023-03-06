import os
direc=r'C:\Users\INTEKNO-PC4\Desktop\Dir_and_files'
dir=os.listdir(direc)
# 1
print("Only files: ")
files=[f for f in dir if os.path.isfile(direc+'/'+f)]
print(files, sep=";")
# 2
print("Only directories: ")
directories=[d for d in dir if os.path.isdir(direc+'/'+d)]
print(directories)
#3
print("Directories and files: ")
print(os.listdir())