#WAP using function to remove a word from the string and strip the resultant string.
def removeandsplit(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()
string=input("Enter a string: ")
word=input("Enter a word to remove from the string: ")
print("Resultant string: ",removeandsplit(string,word))
