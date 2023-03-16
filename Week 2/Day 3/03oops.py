# Note:
# Nouns --> Class (Person, Student, Employee)
# Adjectives--> Object(Age, Salary, Height)
# Verb --> Method (getSalary(), printName())

# Changing class attributes
class Student:
    college="BMC"
    def getInfo(self):
        print(f"Name : {self.name}")
        print(f"Roll : {self.roll}")
s1=Student()
s1.name="Saini"
s1.roll=23
s1.getInfo()
print("College: "+s1.college)
# Changing class attribute on line 18 
# Syntax {ClassName}.attributename="{New name}"
Student.college="Padma Kanya"
print(f"College: {s1.college}")
