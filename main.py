import os

from art import logo
import random

def checkforace(s):
    i=0
    while sum(s)>21 and i<len(s):
        if s[i]==11:
            s[i]=1
        i+=1

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")=='y':
    print("\n"*20)
    print(logo)
    s1 = random.choices(cards,k=2)
    c1 = random.choices(cards,k=2)
    checkforace(s1)
    win=''
    if sum(c1) == 21 :
        win='c'
    elif sum(s1) ==21:
        win='y'
    while sum(s1)<=21:
        print(f"Your cards: {s1},  current score: {sum(s1)}")
        print("Computer's first card: ",c1[0])
        if win=='c' or win=='y':
            break
        if input("Type 'y' to get another card, type 'n' to pass: ")=='y':
            s1.append(random.choice(cards))
            checkforace(s1)
        else:
            while sum(c1) <= 16:
                c1.append(random.choice(cards))
                checkforace(c1)
            break

    print(f"Your final hand: {s1}, final score: {sum(s1)}")
    print(f"Computer's final hand: {c1}, final score: {sum(c1)}" )
    if win=='c':
        print("Lose, opponent has Blackjack")
    elif win=='y':
        print("Win with a Blackjack")

    elif (21>sum(s1)>sum(c1)) or (sum(s1)==21 and sum(c1)!=21):
        print("You win")

    elif sum(c1)>21:
        print("Opponent went over. You Win")
    elif sum(s1)==sum(c1):
            print("It's a Draw")
    else:
        if sum(s1)>21:
            print("You went over. You lose")
        else:
            print("You lose")



