def game():
    a=input("Present score: ")
    return a
f=open("game.txt")
a=f.read()
b=game()
if(b>a):
    print("HIGH SCORE : ",str(b))
    print("Previous High score : ",str(a))
    with open("game.txt",'w') as f:
        f.write(b)
else:
    print("Score : ",str(b))
    print("HIGH SCORE : ",str(a))
f.close()