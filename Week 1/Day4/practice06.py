#WAP to calculate the grade of a student from his marks from the following scheme:
# 90-100 -> Ex
# 80-90 -> A
# 70-80 -> B
# 60-70 -> C
# 50-60 -> D
a=int(input("Enter the marks of the student: "))
if(a>100 or a<0):
    print("Invalid input !! ")
else:
    if(a>=90):
        c="Excellent"
    elif(a>=80 and a<90):
        c="A"
    elif(a>=70 and a<80):
        c="B"
    elif(a>=60 and a<70):
        c="C"
    elif(a>=50 and a<60):
        c="D"
    else:
        c="F"
print("The student has scored",c,"in the subject.")