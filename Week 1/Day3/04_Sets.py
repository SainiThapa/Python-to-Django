# Sets consist of non repititive elements
a={12,45,49,47,67,89}
# If a={}, then it creates an empty dictionary and not set
b=set() #creating an empty set
print(type(b))
print(type(a))
print(a)
# Adding element to a set using add()
b.add(3)
b.add(4)
# b.add({"name":"Saini"}) // Dictionary cannot be added to the sets (because its not hashable)
# b.add([3,4,5]) // Lists cannot be added to the sets (because its not hashable)
b.add((4,5,6)) #Tuples can be added to the sets (it is hashable)
print(b)
