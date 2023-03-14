import random
def game(a,b):
    if(a=='R'):
        if(b=='P'):
            return 0
        if (b=='S'):
            return 1
        elif(b=='R'):
            return 2
    
    if(a=='P'):
        if(b=='S'):
            return 0
        if (b=='R'):
            return 1
        elif(b=='P'):
            return 2
    if(a=='S'):
        if(b=='R'):
            return 0
        if (b=='P'):
            return 1
        elif(b=='S'):
            return 2

a=input("Player 1 turn: Rock(R) or Paper(P) or Scissor(S)? \n")
# b=input("Player 2 turn: Rock(R) or Paper(P) or Scissor(S)?")
randNo=random.randint(1,3)
if(randNo==1):
    comp='R'
elif(randNo==2):
    comp='P'
else:
    comp='S'
print("Computer chose "+comp)
C=game(a,comp)
if(C==0):
    print("Computer won, Player 1 lost")
elif(C==1):
    print("Player 1 won, Computer lost")
elif(C==2):
    print("Match was Draw")
else:
    print("ENTER VALID INPUT !!")