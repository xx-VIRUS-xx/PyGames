import random
snake={40:3,27:5,56:31,43:18,66:45,78:58,89:53,99:41}
ladder={4:25,13:46,42:63,50:69,33:49,62:81,74:92}
pl=0
while 0<=pl<100:
    dice= random.randrange(1,7)
    print("You got {}".format(dice))
    pl+=dice
    print("You're at {}".format(pl))
    if pl in snake.keys():
        pl=snake[pl]
        print("You hit a snake! Move back to {}".format(pl))
    elif pl in ladder.keys():
        pl=ladder[pl]
        print("You found a ladder! Move up to {}".format(pl))
    if pl>100:
         print("Out Of Bound!")
         pl-=dice
if pl == 100:
        print("You win!")
    