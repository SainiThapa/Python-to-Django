#mine a sample log file and find out whether it contains python or not
# also specify in which line is the word 'python' present
with open("log.txt") as f:
    con=f.read()
if 'python' in con.lower():
    print("Yes python is present on the file")
else:
    print("Not present")
line=True
i=1
with open("log.txt") as g:
    while(line):
        line=g.readline()
        if 'python' in line.lower():
            print(line)
            print("python is present on the line",str(i),"\n");
        i+=1