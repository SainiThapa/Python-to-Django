#WAP to calculate the factorial of a given number using for loop
a=int(input("Enter any number: "))
fact=1
for i in range(1,a+1):
    fact=fact*i
    i=i+1
print("The factorial of",a," = ",fact)