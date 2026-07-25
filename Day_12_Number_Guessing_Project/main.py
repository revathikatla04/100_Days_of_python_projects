import random
import art
RES=random.randrange(1,101)
def guess(n):
    for i in range(n, 0, -1):
        print(f"You have {i} attempts remaining to guess the number.")
        ans = int(input("Make a guess: "))
        if RES == ans:
            print("You got it! The answer is ", RES)
            return
        elif i==1:
            break
        elif RES > ans:
            print("Too low. \nGuess again.")
        else:
            print("Too high. \nGuess again.")
    print("You've run out of guesses. Refresh the page to run again.")

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
flag=input("Choose a difficulty. Type 'easy' or 'hard': ")
if flag=="easy":
    guess(10)
elif flag=="hard":
    guess(5)
else:
    print("Invalid Input")

