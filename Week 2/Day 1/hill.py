a=input("Enter a message: ")
b=int(input("Enter a key: "))
c=len(a)
s=[]
j=0
flag=0
for i in range(c):
    s[i][j]=a[i]
    if j==b-1:
        flag=1
    elif j==0:
        flag=0
    if flag==0:
        j=j+1
    else:
        j=j-1
for i in range(0,b):
    for j in range(0,c):
        if s[i][j]!=' ':
            print(s[i][j])