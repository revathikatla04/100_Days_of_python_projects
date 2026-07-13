import art
print(art.logo)
print("Welcome to the secret auction program.")
flag="yes"
auction={}
while flag=="yes":
    name=input("What is your name? ")
    bid=int(input("What's your bid? $"))
    auction[name]=bid
    flag=input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    print("\n"*100)
maximum=0
winner="none"
for key in auction:
    if auction[key]>maximum:
        maximum=auction[key]
        winner=key
print(f"The winner is {winner} with a bid of ${maximum}")
