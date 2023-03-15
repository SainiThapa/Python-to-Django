def game():
    a=int(input("Present score: "))
    return a
with open("game.txt") as f:
    c=f.read()
b=game()
if c=='':
    print("HIGH SCORE : ",str(b))
    with open("game.txt",'w') as g:
        c=g.write(str(b))
elif int(c)<b:
    print("HIGH SCORE : ",str(b))
    print("Previous High score : ",c)
    with open("game.txt",'w') as g:
        g.write(str(b))
else:
    print("Score : ",str(b))
    print("HIGH SCORE : ",c)