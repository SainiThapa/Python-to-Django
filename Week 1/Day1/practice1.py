a=input("Enter your name: ")
b=input("Enter today's date: ")
# c= "Dear " + a + ",\n\tYOU ARE SELECTED\n\t"+b
letter='''Dear '''+a+''',
            You are selected
            '''+b
print(letter)

letter1='''Dear <|Name|>,
            You are selected
            Thank you for staying tuned with us 
            Visit again
                <|Date|>'''
letter1=letter1.replace("<|Name|>",a)
letter1=letter1.replace("<|Date|>",b)

print(letter1)