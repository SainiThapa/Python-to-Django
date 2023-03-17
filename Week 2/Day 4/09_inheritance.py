#other dunder method
class Number:
    def __init__(self,num):
        self.num=num

    def __str__(self):
        return f"Decimal number : {self.num}"
    def __len__(self):
        return 12
a=Number(9)
print(a)
print(len(a))