"""
1 for snake
2 for water
3 for gun
"""
import random

computer = random.randint(1,3)
your_choice = input("Enter your choice: ")
yourDict = {"Snake": 1, "Water": 2, "Gun": 3}
yournum = yourDict[your_choice]
computer_value_Dict = {1:"Snake", 2 : "Water", 3: "Gun"}
print("Computer chose:",computer_value_Dict[computer])
if computer == yournum:
    print("Draw")
else:

    if computer == 1 and yournum == 2:
        print("You Win")
    elif computer == 1 and yournum == 3:
        print("You Lose")
    elif computer == 2 and yournum == 1:
        print("You Lose")
    elif computer == 2 and yournum == 3:
        print("You Lose")
    elif computer == 3 and yournum == 1:
        print("You Win")
    elif computer == 3 and yournum == 2:
        print("You Lose")
    else:
        print("Something Went Wrong")