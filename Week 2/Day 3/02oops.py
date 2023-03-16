class Registration:
    def form(self):
        print("Name : "+self.name)
        print("Roll NO. : "+self.roll)
# Creating an object Student1
Student1=Registration()
Student1.name=input("Enter the Student's name: ")
Student1.roll=input("Enter the Student's roll no.: ")
Student1.form()
# Creating a second object Student2
Student2=Registration()
Student2.name=input("Enter the Student's name: ")
Student2.roll=input("Enter the Student's roll no.: ")
Student2.form()