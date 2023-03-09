Me={
    "Kapdaa":"Cloth",
    "Khaat": " Bed",
    "Bidhyarthi":"Student"
}
print("Options are: ",list(Me.keys()))
a=input("Enter the Nepali word: \n")
print("The meaning of your word is: " + str(Me.get(a)))