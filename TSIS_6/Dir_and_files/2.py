import os
p=r'C:\Users\INTEKNO-PC4\Desktop\Dir_and_files\hello.txt'
print('Exist: ', os.access(p, os.F_OK))
print('Readable: ', os.access(p, os.R_OK))
print('Writable: ', os.access(p, os.W_OK))
print('Executable: ', os.access(p, os.X_OK))
