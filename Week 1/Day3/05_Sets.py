# OPERATION OF SETS
S={2,1,47,3,4}
# Length of the set
print(len(S))
# S.remove(5) throws an error cause there is no 5 in the list
S.remove(4) #Removes 4 from the list
print(S)
print(S.pop()) #Returns an arbitrary element and returns the element removed
S.clear() #Clears/Empties the set
A={1,3,5,7,9,11}
B=A.union({0,3,6,9,12})
print(B)
C=A.intersection({0,3,6,9,12})
print(C)