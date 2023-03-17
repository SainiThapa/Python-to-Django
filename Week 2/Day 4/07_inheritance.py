# Property decorator
class Expense:
    company="Nepal Oil Corporation"
    Quantity=11
    Rate=179
    
    @property       #getter
    def totalprice(self):
        return self.Quantity*self.Rate
    
    @totalprice.setter  #setteer
    def totalprice(self,val):
        self.Rate=val/self.Quantity

a=Expense()
print(f"{a.Quantity} litres of petrol at Rs.{a.Rate}/l")
print(f"Total petrol price : {a.totalprice}\n")
b=int(input("Enter the total cost of petrol to pay : "))
a.totalprice=b
print(f"{a.Quantity} litres of petrol") 
print(f"The price of petrol now is : {round(a.Rate,2)}")