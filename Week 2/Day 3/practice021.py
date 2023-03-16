class Calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f"\nSquare of {self.num} = {self.num**2}")
    def squareroot(self):
        print(f"Square root of {self.num} = {round(self.num**0.5,3)}")
    def cube(self):
        print(f"Cube of {self.num} = {self.num**3}")
n=int(input("Enter a number: "))
num=Calculator(n)
num.square()
num.squareroot()
num.cube()
