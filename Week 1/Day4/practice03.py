#A spam comment is defined as a text containing following keywords:
# "make a lot of money", "buy now","subscribe this", "check this"
# WAP to detect these spams
a=input("Enter a comment: ")
if("make a lot of money" in a or "buy now" in a or "subscribe this" in a or "check this" in a):
    print("Spam detected !!")
else:
    print('The comment \"'+a+'\" is not a spam')