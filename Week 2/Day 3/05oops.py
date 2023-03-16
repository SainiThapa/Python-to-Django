#self 
class Train:
    trainname="Hawrah Express"
    # def getSalary():
    #     print(f"Train is {b} m long")   // doesn't execute

    def getLength(self):
        print(f"The train is {self.b} long")

    @staticmethod #decorator to mark helloSir as a static method 
    def helloSir():
        print("Good Morning passengers ! ")
a=Train()
a.b=130
a.getLength() #is also Train.getSalary(a) --> so we need to pass an argument in the class method for which we use self
a.helloSir() #will return error unless we use @staticmethod on the top of the calling method

