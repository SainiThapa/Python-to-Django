#WAP to find whether a given username contains less than 10 characters or not

username=input("Enter your username: ")
b=len(username)
if(b<10):
    print(username,"contains less than 10 characters")
else:
    print(username,"contains more than 10 characters")