#Create a class  programmer for storing information of few programmers working at microsoft.
class Programmer:
    company="Microsoft"
    def __init__(self,name,app):
        self.name=name
        self.app=app
    def getInfo(self):
        print(f"\nThe name of the {self.company} programmer is {self.name}")
        print(f"Working on the {self.app} app ")
P1=Programmer("Mark","Office")
P2=Programmer("Suzanne","Store")
P1.getInfo()
P2.getInfo()