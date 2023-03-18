class Animal:
    Type="Mammal"

class Pets(Animal):
    color="Grey"

class Dog(Pets):
    @staticmethod
    def bark():
        print("Dog is barking")
Dav=Dog()
print(Dav.Type)
print(Dav.color)
Dav.bark()