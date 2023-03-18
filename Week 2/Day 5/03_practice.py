# Create a class Employee and add Salary and increment properties to it.
# Write a method SalaryafterIncrement method with a @property decorator with a setter which changes the value
# of increment based on the salary.

class Employee:
    def salary(self,sal):
        self.sal=sal
    def increment(self,inc):
        self.inc=inc
    def showsalary(self):
        print(f"Salary : {self.sal}")

class AfterIncrement(Employee):
    @property
    def Salaryafterincrement(self):
        return self.sal+self.inc
        # return self.sal
    @Salaryafterincrement.setter
    def Salaryafterincrement(self,sal):
        self.inc=sal-self.sal
 
e=AfterIncrement()
e.salary(15000)
e.increment(1500)
print(f"Salary: {e.sal}")
print(f"Increment: {e.inc}")
print(f"Salary after increment: {e.Salaryafterincrement}")
e.Salaryafterincrement=20000
print(f"Total salary = {e.Salaryafterincrement} Increment: {e.inc}")