from functools import reduce

lis1=[2,3,5,7,9,10]
sum=reduce(lambda x,y: x+y,lis1)
# OR 
# sum = reduce(mySum,list1), where mySum=lambda x,y:x+y
print(sum)

def product(a,b):
    return a*b

product=reduce(product,lis1)
print(product)

''' WORKING MECHANISM
product=product([2,3,5,7,9,10])
        =product([6,5,7,9,10])
        =product([30,7,9,10])
        =product([210,9,10])
        =product([1890,10])
        =product([18900])
        '''