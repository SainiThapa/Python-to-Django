# Append mode
f=open("python.txt",'a')
a=input("Enter a string: ")
f.write(a)
b=input("Enter a string: ")
f.write(b)
f.close()
g=open("python.txt",'r')
c=g.read()
print(c)
g.close