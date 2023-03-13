
def Prime(n):
    step=0
    for i in range(2,n):
        if(n%i==0):
            step=step+1
    print(step)
    if(step==0):
            return 0
    else:
            return 1
def result(m):
    st=0
    if Prime(m)==0 :
        return m-1
    else:
        for j in range(1,m):
            if(m%j==0):
                st=st+1
        return m-st-1
a=int(input("Enter a number to find its Euler totient: "))
print("The Euler's totient of",a,"is",result(a))