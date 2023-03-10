a=["Boss","Employee","Intern"]
s=int(input("Enter your salary: "))
if(s>=5000 and s<=10000):
    print("Your position is",a[2])
elif(s>10000 and s<=30000):
    print("Your position is", a[1])
elif(s>30000):
    print("Your position is",a[0])
if(a is not None):
    print(True) 