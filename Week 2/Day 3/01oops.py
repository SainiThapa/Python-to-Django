# Intro to class and objects
class student:
    def name(self):             #self denotes the instance of class
        return self.a+self.b
name1=student() #creating an object name1
name1.a="Saini"
name1.b="Thapa"
s=name1.name()
print(s)


'''
EmployeeName --> PascalCase 
Classes are written in PascalCase

isInt, isFloat --> camelCase
'''