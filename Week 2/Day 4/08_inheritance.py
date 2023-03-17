#OPERATOR OVERLOADING
class number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num1):
        print("ADDITION")
        return self.num+num1.num

    def __mul__(self,num2):
        print("PRODUCT")
        return self.num*num2.num

    def __sub__(self,num2):
        print("SUBTRACTION")
        return self.num-num2.num

    def __truediv__(self,x):
        print("DIVISION")
        return self.num/x.num

a1=number(3)
a2=number(4)

sum=a1 + a2
print(sum)

mul=a1 * a2
print(mul)

sub=a1 - a2
print(sub)

div=a1/a2
print(div)