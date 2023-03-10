# * * *
# *   *
# * * * n=3
n=3
for i in range(n):
    for j in range(n):
        if(i==1 and j==1):
            print(" ",end=" ")
            continue
        print("*",end=" ")
    print("\n")