with open("copyfile.txt") as f:
    a=f.read()
with open("file.txt") as g:
    b=g.read()
if(a==b):
    print("File A and B are identical")
else:
    print("File A and B are not identical")