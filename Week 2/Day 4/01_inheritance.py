# Introduction to inheritance

class Student:              #Parent/base class
    def __init__(self) -> None:
        print("I am a student")
    def name(self,name1):          
        print(f"Name: {name1}")

class Info(Student):        #Child/Derived class 
    pass

s1=Info() #creating a object on child class
s1.name("Saini") #inherits the methods and attributes of the parent class
