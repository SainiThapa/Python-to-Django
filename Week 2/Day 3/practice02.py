import math
class Calculator:
    def square(self):
        # print( pow(self.num,2))
        print(self.num**2) #This can also be written if you dont want to import the math library
    def squareroot(self):
        a=pow(self.num1,0.5)
        print(round(a,3))
    def cube(self):
        print(pow(self.num2,3))
s1=Calculator()
s1.num=int(input("Enter a number to find the square: "))
s1.square()
s1.num1=int(input("Enter a number to find the square root: "))
s1.squareroot()
s1.num2=int(input("Enter a number to find the cube : "))
s1.cube()

    