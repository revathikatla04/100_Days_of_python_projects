print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
x=input('You are at a crossroad. Where do you want to go?\n Type "left" or "right"\n')
if x=="left"or x=="Left":
    y=input('''You've come to a lake. There is an island in the middle of the lake.\n Type "wait" for a boat. Type "swim" to swim across.\n''' )
    if y=="Wait" or y=="wait":
        z=input('''There are 3 doors in front of you. Which one do you want to chose?\n Type "Red" to choose a Red door. Type "Blue" to choose a Blue door. Type "Yellow" to choose a Yellow door.\n''')
        if z=="Red"or z=="red":
            print("Burned by fire.\n Game over.")
        elif  z=="Blue"or z=="blue":
            print("Eaten by beasts.\n Game Over.")
        elif  z=="Yellow"or z=="yellow":
            print("Congratulations! You Win the Game.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("You have fallen into a hole. Game Over.")