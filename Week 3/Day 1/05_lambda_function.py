# Normal code for function and list creation
def odd(x):
    if(x%2==0):
        return 'Even'
    else:
        return 'ODD'
a=[]
for i in range(5):
    b=int(input("Enter a number: "))
    a.append(b)
print(a)
for i in range(5):
    print(f"{a[i]} is an {odd(a[i])} number\n")

# Lambda Function with list comprehension

ODD = lambda x:'Even' if x%2==0 else 'Odd'
c=[input("Enter a number: ") for n in range(5)]
print(c)
for i in range(5):
    print(f"{a[i]} is an {ODD(a[i])} number") 