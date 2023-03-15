with open("file.txt") as f:
    content=f.read()
with open("copyfile.txt",'w') as g:
    g.write(content)
with open("copyfile.txt",'r') as g:
    print(g.read())