#more on Constructor
class Person:
    def __init__(self,name,age,salary):
        print("\nA person is arrived to a survey\n")
        self.name=name
        self.age=age
        self.salary=salary
    def showInfo(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Salary : {self.salary}")
    @staticmethod
    def greet():
        print("\nHave A Nice Day Sir !!")
a=input("Enter your name : ")
b=int(input("Enter your age: "))
c=int(input("Enter your salary: "))
# p1=Person() // throws an error as the constructor needs arguments
p1=Person(a,b,c)
p1.showInfo()

p1.greet()