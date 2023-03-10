#WAP which finds out whether a given name is present in a list or not
Name=['Suman','Prabesh','Niroj','Sushil','Vishan','Suraj']
name1=input("Enter a name: ")
if(name1 in Name):
    print(name1,"is present in the list:",Name)
else:
    print(name1,"is not present in the list:",Name)