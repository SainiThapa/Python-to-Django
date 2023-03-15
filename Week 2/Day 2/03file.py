# write mode in the file
f=open("text.txt",'w+')
a=input("Enter any string to enter in the file: ")
f.write(a)
f.close()
f=open("text.txt",'r')
b=f.read()
print(b)
f.close()