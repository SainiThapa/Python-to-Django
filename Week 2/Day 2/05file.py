# with statement
with open("saini.txt",'r') as f:
    a=f.read()
print(a)
with open("python.txt",'a') as f:
    f.write(" APPENDED TEXT")
with open("python.txt",'r') as f:
    b=f.read()
print(b)