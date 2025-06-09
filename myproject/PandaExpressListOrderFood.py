def printMenu(menu):
    for key in menu:
        print(key)


total=0
pandalist=[]
menudictonary={"bowl":8
               ,"plate":10
               ,"bigger plate":13,
               "family meal":35}
print("Welcome to panda express")
print("---------------------------")


printMenu(menudictonary)

while True:
    food=input("What do you want from the menu q to quit r to reset \n")
    print (food.upper())
    if (food.upper() == "Q"):
        break
    elif (food.lower() == "r"):
        pandalist.clear()
    elif food not in menudictonary.keys():
        printMenu(menudictonary)
        print(" please enter a item from the menu ")
    else:
        pandalist.append(food)


for food in pandalist :
    print(food)
    print(f"${(menudictonary.get(food)):.2f}",end=" " )
    total+=(menudictonary.get(food))

print(f"your total is ${total:.2f}")














