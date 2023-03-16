#WAP to open "article.txt" and check if 'Euler' is present in the file or not
f=open("article.txt",'r')
a=f.read()
b=input("Enter a keyword to search in the file: ")
if b in a:
    print("Euler is present in the article")
else:
    print("Euler is not present in the article")
f.close()