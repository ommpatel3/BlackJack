import random
import time

leave='n'
money=200
cost=5

print(" BlackJack")
print("+++++++++++")
print("        ()")
print("        /\\")
print("   ()--'  '--()")
print("     `.    .'")
print("      / .. \\")
print("     ()'  '()")

print("Welcome to blackJack, it costs $10 to play, out of the $200 you have")
while(leave=='n' or leave=='N') and money>0:
    #resetting all variables
    cost=cost*2
    money=money-cost
    playercontinue = True
    dealercontinue = True
    yes='h'
    end='n'
    player=0
    dealer=0
    i=1
    #is the person has less than the bet, they dont hane enough to play
    if money-cost<=0:
        print("you don't have enough money to play!")
        exit(0)
    print("\nyou have $"+str(money))
    #player turn

    card=random.randint(1,11)
    card2=random.randint(1,10)
    player=card+card2
    print("Your 2 cards are "+str(card)+" and "+ str(card2) )
    print("Your Score: "+ str(player))
    #gives optio to double down if they can afford it
    if money-cost*2<=0:
        yes = input ("Hit or stand ? (h/s)")
    else:
        yes = input ("Hit, stand or Double Down? (h/s/d)")

    #if they choose to double down
    if yes=='d' or yes=='D':
        money=money-cost
        cost=cost*2
        print("The cost is now "+ str(cost))
        card=random.randint(1,11)
        player=player+card;
        print("\nYou got a: "+ str(card))
        print("Your Score: "+ str(player))
        cost=cost*2
        if player==21:
            print("You Win!")
            playercontinue=False
            money+=cost*2
            print("You now have $"+str(money))
            yes='s'
        elif player>21:
            print("You Lose!")
            playercontinue=False
            print("You now have $"+str(money))
            yes='s'
    #if they choose to hit
    while (yes=='h' or yes=='H') and i<=10:
        card=random.randint(1,11)
        player=player+card;
        print("\nYou got a: "+ str(card))
        print("Your Score: "+ str(player))
        i=i+1
        if player==21:
            print("You Win!")
            playercontinue=False
            money+=cost*2
            print("You now have $"+str(money))
            yes='s'
        elif player>21:
            print("You Lose!")
            playercontinue=False
            print("You now have $"+str(money))
            yes='s'
        else:
            yes = input ("Hit or stand? (h/s)")



    if playercontinue==True:#does dealers turn only if player didnt win/lose
        print("\n Dealer's Turn")
        print("+++++++++++++++")
        end='n';
        i=1;
        while i<=5 and end=='n':
            card=random.randint(1,11)
            dealer=dealer+card
            print("Dealer got a: "+ str(card))
            print("Dealer's score: "+str(dealer))
            i=i+1
            if dealer==21:
                print("Dealer Wins!")
                dealercontinue=False
                print("You now have $"+str(money))
                end='y'
            elif dealer>17 and dealer<21:
                print("Dealer Stands")
                end='y';
            elif dealer>21:
                print("Dealer went over 21! You win!")
                dealercontinue=False
                money+=cost*2
                end='y'
                print("You now have $"+str(money))
            else:
                print("Dealer hits \n")
            time.sleep(1)

    if  (dealercontinue==True and playercontinue==True): #ending comaprisons only if noone won/lost
        print("\n Let's Compare\n+++++++++++++++");
        print("You had: "+ str(player))
        print("Dealer had: "+ str(dealer))
        if (player>dealer):
            print("You Win!")
        elif (player<dealer):
            print("You Lose!")
        else:
            print("Tie!")
            money=money+cost
            print("You now have $"+str(money))
    #asks if they want to play again
    leave=input("\nleave? y/n\n")
    if leave=='n' or leave=='N':
        print("The cost has now been doubled to $"+str(cost*2)+"!")
    else:
        exit(0)
