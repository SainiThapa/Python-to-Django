#WAP to find whether a number is prime or not 
a=int(input("Enter a number: "))
c=0
for i in range(1,a):
    if(a%i==0):
        c=c+1
    else:
        pass
if(c==1):
    print(a,"is a prime number")
else:
    print(a,"is not a prime number")