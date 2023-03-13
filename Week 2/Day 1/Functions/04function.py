#WAP using userdefined functions to find the power(e.g. a^n) and squareroot of a number.
def power(x,n):
    for i in range(1,n+1):
        sum=x*x
    return sum
def findsqrt(x):
    if x<2:
        return x
    y=x
    z=(y+(x/y))/2
    while(abs(y-z)>=0.000001):
        y=z
        z=(y+(x/y))/2
    return z
a=int(input("Enter a number: "))
b=int(input("Enter the power: "))
print("Pow("+str(a)+","+str(b)+") = "+str(power(a,b)))
print("Square root of "+str(a)+" = "+str(findsqrt(a)))