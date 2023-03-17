#Multi level inheritance

class College:
    college="BMC"
    def Faculty(self,fac):
        self.fac=fac
    @staticmethod
    def address():
        print("Bhaktapur, Dudhpati")

class class1(College):             #class1 derived from College
    def class_1(self,classname):
        self.classname=classname
    @staticmethod
    def address():
        print("Kathmandu, Sinamangal")

class Student(class1):              #Student derived from class1
    def Stu(self):
        print(f"College : {self.college}")
        print(f"Faculty : {self.fac}")
        print(f"Class : {self.classname}")

S1=Student()            #object of class Student
S1.Faculty('Science')
S1.class_1('5th Sem CSIT')
S1.Stu()
S1.address()        #This returns the closest parent class method