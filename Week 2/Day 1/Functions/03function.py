# WAP using Userdefine function for finding the maximum number amongst the two entered number
def maximum(a,b):

    if a>b:
        return True
    else:
        return False
a=int(input("Enter a num1: "))
b=int(input("Enter a num2: "))
if(a!=b):
    if(maximum(a,b)):
        print(str(a)+" is greater than "+str(b))
    else:
        print(str(b)+" is greater than "+str(a))
else:
    print("Both numbers are equal")