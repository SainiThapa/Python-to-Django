#Use open function to read the content of a file
f=open("saini.txt",'r')
# By default the more is r
# f=open("saini.txt")
data=f.read() #f.read() returns the entire file, #f.read(n) returns the first n characters from the file
print(data)
# data=f.readline() retursn the line 
# print(data)
f.close()
