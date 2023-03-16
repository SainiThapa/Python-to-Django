# Check if you can change the class attribute from the main driver
class ClassA:
    a=100
    def __init__(self):
        print("Object is created")
obj1=ClassA()
print(obj1.a)
ClassA.a=0
print(obj1.a)
obj2=ClassA()
print(obj2.a)  
# Yes we can