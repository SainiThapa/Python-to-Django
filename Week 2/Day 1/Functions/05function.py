# Recursion example for factorial and sum of n number
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
def sumofn(n):
    if(n==1):
        return 1
    else:
        return n+sumofn(n-1)
n=int(input("Enter a number: "))
print(fact(n))
print(sumofn(n))