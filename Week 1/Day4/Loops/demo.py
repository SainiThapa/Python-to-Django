# WAP to enter the name of a given number of students and display them using for loop
a=[]
b=int(input("Enter the number of students: "))
for i in range(b):
    b=input("Enter the name of student"+str(i+1)+": ")
    a.append(b)
for name in a:
    print(name,end="\t")