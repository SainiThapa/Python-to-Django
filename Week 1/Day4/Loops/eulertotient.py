def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
def euler(n):
    step=0
    for i in range(1,n):
        if(gcd(i,n)==1):
            step=step+1
    return step
a=int(input("Enter a number to find its Euler totient: "))
print("The Euler Totient of",a," is",euler(a))