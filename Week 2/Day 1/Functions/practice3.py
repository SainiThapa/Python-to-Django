def inchtocm(inch):
    cm=inch*2.54
    return cm
a=int(input("Enter the height of the student in inches: "))
b=inchtocm(a)
print("The student is "+str(b)+"cm tall or "+str(round(b/100,2))+"m tall")