a1=int(input("Enter the value of a1: "))
a2=int(input("Enter the value of a2: "))
a3=int(input("Enter the value of a3: "))
a4=int(input("Enter the value of a4: "))
if(a1>a2 and a1>a3 and a1>a4):
    c=a1
    d=1
elif(a2>a1 and a2>a3 and a2>a4):
    c=a2
    d=2
elif(a3>a1 and a3>a2 and a3>a4):
    c=a3
    d=3
elif(a4>a1 and a4>a2 and a4>a3):
    c=a4
    d=4
print("a"+str(d),"=",c,"is the greatest number")