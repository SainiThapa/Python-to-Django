#Multiple inheritance
#Child class inherits from more than one class
class Registration:         #Parent class 1
    college="BMC"

class Student:              #Parent class 2
    Faculty="Science"
    @staticmethod
    def showInfo():
        print("BSc. CSIT     BSc. Microbiology     BSc.Physics")

class Info(Registration,Student):      #Derived class from parent 1 and 2
    name="Saini"

s1=Info()       #object of the child class
print(s1.college)
print(s1.Faculty)
s1.showInfo()
print(s1.name)