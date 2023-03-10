# WAP to find out whether a student is pass or fail if it requires total 40% and atleast 33% in each 
# subject to pass. Assume 3 subjects and take marks as an input from the user

S1=int(input("Enter the marks of subject1: "))
S2=int(input("Enter the marks of subject2: "))
S3=int(input("Enter the marks of subject3: "))
Avg=(S1+S2+S3)/3
if(S1>=33 and S2>=33 and S3>=33):
    if(Avg>=40):
        print("\nStudent is fairly passed in all subjects with a percentage of",round(Avg,2))
        print("Hence, Student is passed.")
    else:
        print("\nStudent is fairly passed in all subjects but didn't score a passing percentage of 40")
        print("Hence, Student is failed.")
        print("Percentage =",round(Avg,2))
else:
    print("Student is failed.")