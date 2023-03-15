#rename the old file into Newfile.txt using python
import os
filename1='prac8.txt'
filename2='Newfile.txt'
with open("prac8.txt") as f:
    a=f.read()
    print(a)
with open("Newfile.txt",'w') as f:
    f.write(a)
os.remove("prac8.txt")