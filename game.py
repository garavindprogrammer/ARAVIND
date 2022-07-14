import random
import time
player1=0
player2=0
for i in range(13) :
   print('🕺💃',end='')
print('\n\n_______welcome to the game_____')
print()
print('******************')
while ((player1<100)and(player2<1000)):
                time.sleep(2)
                j=random.randint(1,6) 
                print('The dice is rolled as : ',j)
                if (j%2==0):
                    print('its player one time')
                    print('\tsince it is even number')
                    if (player1==20)or(player1==25)or(player1==32)or(player1==39):
                        print('Oh my god player1 has bitten by a snake ')
                        player1=player1-20
                        j=0
                    player1=player1+j
                    print('\t\tthe score of player1 is : ',player1)
                    print('\n\n\n')
                else:
                    print('Its player2 time ')
                    print('\tsince it is oddnumber ')
                    if (player2==30)or(player2==35)or(player2==72)or(player2==69):
                        print('Oh my god player2 has bitten by a snake ')
                        player2=player2-25
                        j=0
                    player2=player2+j
                    print('\t\tThe score of player 2 is : ',player2)
                    print('\n\n\n')
                if player1>=100:
                    print('____player1 won the game _______')
                elif player2>=100:
                    print('____player2 won the match__')
