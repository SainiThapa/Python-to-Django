#Perfect Guess

import random
def random_num():
    return random.randint(1,100)
def guess(m,n):
    if(m==n):
        return True
    else:
        return False

m=random_num()
n=int(input("\nGuess the number (1-100): "))
c=1
while guess(m,n)==False:
    if m>n:
        print("Enter a Higher number please\n")
    elif m<n:
        print("Enter a Lower number please\n")
    c+=1
    n=int(input("Guess the number: "))
print(f"\nCONGRATULATION THE NUMBER IS {m}")
print(f"Number of tries : {c}")

with open("Highscore.txt") as f:
    a=f.read()
if (int(a)>c):
    with open("Highscore.txt",'w') as f:
        f.write(str(c))
    print("\nYou set your personal best score")
    print(f"Your score : {c}")
    print(f"Prev best score : {a}")
else:
    print(f"Your score : {c}")
    print(f"Best score : {a}")