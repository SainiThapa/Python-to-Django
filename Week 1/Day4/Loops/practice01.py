# WAP to find multiplication table of a given number

a=int(input("Enter any number: "))
print("Multiplicative table of",a,)
for i in range(1,11):
    # print(a,"*",i,"=",a*i)
    print(f"{a} X {i} = {a*i}")