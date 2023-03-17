#Single inheritance
class Employee:
    def getdata(self,name,salary):
        self.name=name
        self.salary=salary
class Info(Employee):
    def showdata(self):
        print(self.name)
        print(self.salary)
a1=Info()
a1.getdata('Mark',34000)
a1.showdata()