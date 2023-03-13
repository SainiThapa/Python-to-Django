#WAP using function to find the greatest of three numbers
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>a and c>b):
        return c
    else:
        return 0
a=int(input("Enter a number1: "))
b=int(input("Enter a number2: "))
c=int(input("Enter a number3: "))
d=greatest(a,b,c)
if(d!=0):
    print(str(d),"is the largest number")
else:
    print("Re-enter different values of a, b and c")