import art

def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

def calculator():
    print(art.logo)
    x= float(input("What's the first number?: "))
    flag=True
    while flag:
        print("+\n-\n*\n/")
        y=input("Pick an operation: ")
        z=float(input("What's the next number?: "))
        dic={"+":add(x,z),"-":sub(x,z),"*":mul(x,z),"/":div(x,z)}
        ans=dic[y]
        print(f"{x} {y} {z} = {ans}" )
        p=input(f"Type 'y' to continue calculating with {ans} or type 'n' to start a new calculation:  ").lower()
        if p=="y":
            x=ans
        else:
            flag=False
            print("\n"*20)
            calculator()
calculator()