list1=[n+2 for n in range(7)]
print(list1)

# Normal syntax
'''
def filter_func(x):
    return x>4
lis2=[]
for items in list1:
    if(filter_func(items)):
        lis2.append(items)
print(lis2)
'''

# Using FILTER function

def filter_function(x):
    return x>4
list2=list(filter(filter_function,list1))
print(list2)

# Another example can be 

fill=lambda x:True if x%2==0 else False
list3=list(filter(fill,list1))
print(list3)