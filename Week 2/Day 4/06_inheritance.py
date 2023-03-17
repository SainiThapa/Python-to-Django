#Class method() : bound to class and not on the object of the class

class Registration:
    Collegename="Bhaktapur Multiple Campus"
    Address="Bhaktapur"
    Contact='071-728374'

    # def changeCollege(self,name,address,contact):
    #     self.Collegename=name
    #     self.Address=address
    #     self.Contact=contact
    @classmethod
    def changeCollege(cls,name,address,contact):
        cls.Collegename=name
        cls.Address=address
        cls.Contact=contact

s1=Registration()
print(f"College : {s1.Collegename}\nAddress : {s1.Address}\nContact : {s1.Contact}\n")

s1.changeCollege('Padma Kanya','Kathmandu','071-567489')
print(f"College : {s1.Collegename}\nAddress : {s1.Address}\nContact : {s1.Contact}\n")