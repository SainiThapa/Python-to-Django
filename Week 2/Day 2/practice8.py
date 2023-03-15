#Wipe out content of a file
with open("prac8.txt") as f:
    a=f.read()
print(a)
with open("prac8.txt",'w') as f:
    f.write('')
with open("prac8.txt") as f:
    a=f.read()
print("Content now : ", a)