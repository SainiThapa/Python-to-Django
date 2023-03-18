# Write a class Complex to represent complex numbers along with overloaded operators + and x which adds 
# and multiplies them
# Addition of two complex numbers: (a+bi)+(c+di)=(a+c)+(b+d)i
# Multiplication of two complex numbers: (a+bi)(c+di)=(ac-bd)+(ad+bc)i

class Complex:
    def __init__(self,r,i):
        self.real=r
        self.img=i
    def __add__(self,c):
        return Complex(self.real + c.real,self.img + c.img)
    
    def __mul__(self,c):
        return Complex(self.real*c.real-self.img*c.img,self.real*c.img+self.img*c.real)


    def __str__(self):
        return f"{self.real} + {self.img}i"


C1=Complex(3,2)
C2=Complex(1,7)
print(C1+C2)
print(C1*C2)