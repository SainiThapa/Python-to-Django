#CONSTRUCTOR in py
#Syntax: def__init__(self):

class Election:
    def __init__(self):
        print("Voter is here...!! ")
    def info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}\n")
s1=Election() #calls the constructor as soon as a class is created
s1.name="Saini"
s1.age=22
s1.info()
s2=Election()
s2.name="Sujan"
s2.age=23
s2.info()