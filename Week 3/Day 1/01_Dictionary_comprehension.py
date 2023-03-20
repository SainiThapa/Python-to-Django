dict1={}
for n in range(10):
    if n%2==0:
        dict1[n] =  n*2
    else:
        dict1[n]="Odd index"
print(dict1)

dict2={n:n*3 if n%3==0 else 'Invalid ' for n in range(10) }
print(dict2)
