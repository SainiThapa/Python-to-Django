#Super() method 
class Emp:
    def __init__(self):
        print("Initializing Employee \n")

    def process(self):
        print("I am a student")
    
    def info(self):
        print("SUPER METHOD")

class Emp1(Emp):

    def __init__(self):
        super().__init__()
        print("Initializing Object \n")

    def process(self):
        super().process()       # directs to its Super class method named process() and works on it
        print("I am a graduate.")

class Emp2(Emp1):
    def process(self):
        super().process()       #directs to its Super class method named process() and works on it
        super().info()          #looks further to find the method info() if not found on its nearest parent class
        print("I am a full time employee")

stu=Emp2()
stu.process()