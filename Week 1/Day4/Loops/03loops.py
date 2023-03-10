#RANGE FUNCTION

for i in range(10): #range(starting index,ending index, step size)
    print(i)    
    if(i==7):
        break
else:
    print("The value of i exceeds the range")
for j in range(10,15):
    if(j==12):
        continue
    print(j)