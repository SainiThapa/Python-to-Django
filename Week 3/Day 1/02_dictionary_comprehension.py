first=[(44,'Saini'),(56,'Sushil')]
print(first)
first=[]
print("Enter your roll number and name: ")
for i in range(4):
    a=tuple()
    c=int(input("\nRoll: "))
    b=input("Name: ")
    a=a+(c,b)
    first.append(a)
dict1={m:n for m,n in first}

print(dict1)