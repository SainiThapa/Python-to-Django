import math
class Calculator:
    def square(self):
        print( pow(self.num,2))
    def squareroot(self):
        print(pow(self.num1,0.5))
    def cube(self):
        print(pow(self.num2,3))
s1=Calculator()
s1.num=int(input("Enter a number to find the square: "))
s1.square()
s1.num1=int(input("Enter a number to find the square root: "))
s1.squareroot()
s1.num2=int(input("Enter a number to find the cube root : "))
s1.cube()

    