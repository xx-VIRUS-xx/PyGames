import random

# to create users
class user():
    name="Honey"
    def __init__(self, name):
        self.name = name

    #code for gameplay    
    def play(self,dice,pl):
        #coordinates for snake
        snake={40:3,27:5,56:31,43:18,66:45,78:58,89:53,99:41}

        #coordinates for ladder
        ladder={4:25,13:46,42:63,50:69,33:49,62:81,74:92}
        
        # while 0<=pl<100:
            #dice= random.randrange(1,7)
        print("{} got {}".format(self.name,dice))
        pl+=dice
        print("{} is at {}".format(self.name,pl))

        #when player hits snake
        if pl in snake.keys():
            pl=snake[pl]
            print("{} hit a snake! Move back to {}".format(self.name,pl))
        #when player found ladder
        elif pl in ladder.keys():
            pl=ladder[pl]
            print("{} found a ladder! Move up to {}".format(self.name,pl))
        #when player goes out of bound
        if pl>100:
            print("{} is Out Of Bound!".format(self.name))
            pl-=dice
        #player wins
        if pl == 100:
                return(pl)
        return(pl)
    
'''player=user(name=input())
player2=user(name=input())
us=player2.play(random.randint(1,6),0)
me=player.play(random.randint(1,6),0)
while me<100 and us <100:
    us=player2.play(random.randint(1,6),us)
    me=player.play(random.randint(1,6),me)
    if me ==100:
        print(player.name + ' Win')
        break
    elif us == 100:
        print(player2.name + ' Win')
        break'''
n=int(input("No Of Player playing:"))
players={}
game={}
flag=1
for i in range(n):
    players[i]=user(name=input("Player#{}: ".format(i+1)))
for i in range(n):
    game[i]=players[i].play(random.randint(1,6),0)
while flag :
    for j , k in game.items():
        if k==100:
            print(players[j].name + ' Win')
            flag=0
            break
        else:
            game[j]=players[j].play(random.randint(1,6),k)


     

     
