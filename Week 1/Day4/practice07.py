#WAP to find out whether a given post is talking about books or not
a=input("Enter the caption of the post :")
if("Books" in a or "books" in a or "Book" in a or "Book" in a):
    state=True
else:
    state=False
if(state):
    print("\nThe post is talking about 'Books'")
else:
    print("\nThe post is not talking about 'Books'")