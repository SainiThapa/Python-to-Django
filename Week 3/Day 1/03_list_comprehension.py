# List comprehension examples
lst1=[n for n in range(10)]
print(lst1)

lst2=[n+1 for n in range(10) if n%2==0]
print(lst2)

lst3=[n+1 for n in range(10) if n%2==0 if n%3==0]
print(lst3)

lst4=[n+1 if (n+1)%2==0 else 'Odd' for n in range(10)]
print(lst4)