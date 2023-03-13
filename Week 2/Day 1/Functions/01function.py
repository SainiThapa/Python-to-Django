def per(marks):
    sum=marks[0]+marks[1]+marks[2]+marks[3]
    return (sum/4)
print("Enter the marks of 4 subjects:")
a=[]
for i in range(0,4):
    b=int(input("Enter the marks of subject"+ str(i+1)+": "))
    a.append(b)
print("Percentage:",per(a),"%")