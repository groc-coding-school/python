import math as m;


#user data
def start(ch):
    bot = "groc_bot"
    print("....................................................................")
    print("Hi, i'm " +bot.upper())
    name = raw_input("what's your name: ").title()
    print("Okay, " + name)
    print("would you love to play some math game...")



#calculator
def calculator(ch):
    print("==================================================================")
    x = input("Enter the value of x: ")
    y = input("Enter the value of y: ")
    sum = int(x) + int(y)
    print("X: ",str(x))
    print("Y: ",str(y))
    print("Z = X + Y: ",sum)
#program ending
def endprog():
    print("==================================================================")
    print("Thanks, program ended successfully...")

#menu
def menu():
    commands = ["YES","Yes","yes","NO","No","no"]
    print("==================================================================")
    print("Enter yes or no to perform your desired operation.")
    ch = raw_input("")
    for ch in commands:
        if(ch == "YES" or ch == "Yes" or ch =="yes"):
            start(ch)
            calculator(ch)
        
        elif(ch == "NO"  or ch == "No" or ch == "no" ):
            start()
    else:
        endprog()
    


menu()
