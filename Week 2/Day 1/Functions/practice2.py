#WAP using function to convert temperature given in celsius to fahrenheit
def CtoF(cel):
    F=((cel*9)/5)+32
    return F
Cel=int(input("Enter the temperature in Celsius: "))
print(str(Cel)+" degree Celsius = "+str(CtoF(Cel))+" degree Fahrenheit")