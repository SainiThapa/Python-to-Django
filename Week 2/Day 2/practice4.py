with open("practice4.txt",'r') as f:
    a=f.read()
if 'Donkey' in a or 'donkey' in a:
    a=a.replace('Donkey','######')
    a=a.replace('donkey',"######")
print(a)
with open("practice4.txt",'w') as f:
    f.write(a)
