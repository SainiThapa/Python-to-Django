#instance class attributes

class Registration:
    college="BMC"
    def showData(self):
        print(f"Name : {self.name}")
        print(f"college : {self.college}\n")
s1=Registration()
s2=Registration()
s3=Registration()
# Creating instance attributes
s1.name="Saini"
s2.name="Sujan"
s2.college="Golden gate"
s3.name="Adarsh"
s3.college="Uniglobe"
# Calling class function aka Methods
s1.showData() #displays the class attribute value for s1.college (i.e BMC)
s2.showData() #displays the instance attribute values for s2.college and s3.college
s3.showData()

# therefore instance attributes have higher precedence than the class attributes