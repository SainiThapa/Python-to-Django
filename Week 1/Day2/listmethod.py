L1=[3,1,6,9,4,24,12,34,29]
L2=L1
L3=L1
print("Original list : " + str(L1))

# Sorts the list
L1.sort()
print("Sorted  list: "+ str(L1))

# Reverses the list
L2.reverse()
print("Reversed list: "+ str(L2))

# Appends  the list
L3.append(23)
print("Appended list: " + str(L3))

# Inserting in the list
L1.insert(0,24)
print("Inserted list: "+ str(L1))

# Pop - deleted an element from the list
L1.pop(0)
print("Popped list: "+ str(L1))

# Remove - removes an element from the list

L1.remove(1)
print("New list: " + str(L1))