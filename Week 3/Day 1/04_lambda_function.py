def cube(x):
    return x*x*x
a=3
print(cube(3))

#  Lambda function
CUBE = lambda x : x*x*x
print(CUBE(14))

# def Great(x,y)
# if (x>y):
    # return x
# else:
    # return y

Great = lambda x,y: x if x>y else y #lambda function

print("Enter two number to find the greatest: ")
a=int(input("First number: "))
b=int(input("Second number: "))
print(Great(a,b),"is the greatest number ")