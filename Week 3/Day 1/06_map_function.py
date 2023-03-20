cube=lambda x:x*x*x

print(cube(3))
list1=[n+2 for n in range(7)]
print(list1)

# LIST COMPREHENSION TECHNIQUE

'''
list2=[cube(n) for n in list1]
print(list2)
'''

# NORMAL METHOD
'''
list2=[]
for num in list1:
    list2.append(cube(num))
print(list2)'''

# MAP method

list2=list(map(cube,list1))
print(list2)