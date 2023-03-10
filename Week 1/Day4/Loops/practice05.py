#WAP to find the sum of first n natural numbers using WHILE loop
a=int(input("Enter any number: "))
i=1
sum=0
while i<=a:
    sum=sum+i
    i=i+1
print("Sum of first",a,"natural numbers = ",sum)