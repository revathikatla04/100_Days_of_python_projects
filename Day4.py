import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
x=[rock,paper,scissors]
y=int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if 0<=y<=2:
    print(x[y])
    print("Computer chose:")
    z=random.choice(x)
    print(z)
    if y==0 and z==paper:
        print("You lose!")
    elif y==1 and z==scissors:
        print("You loose!")
    elif y==2 and z==rock:
        print("You loose!")
    elif z==x[y]:
        print("It's a draw!")
    else:
        print("You win!")
else:
    print("Invalid choice. You loose!")





