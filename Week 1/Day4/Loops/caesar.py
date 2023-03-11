def encrypt(plaintext,key):
    ciphertext=''
    m=''
    for i in range(len(plaintext)):
        c=plaintext[i]
        if (type(c)==str):
            c.upper()
            m=(ord(c)-65+key)%26 + 65
        ciphertext=ciphertext+chr(m)
    return ciphertext
plaintext=input("Enter the plaintext: ")
key=int(input("Enter the key: "))
ciphertext=encrypt(plaintext,key)
print("Ciphertext: "+ ciphertext)


