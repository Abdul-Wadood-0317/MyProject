#In this project we are making an Game i.e 
#--------Rock-Paper-Scissor-Game---------
#lets get started:
import random

l = ["rock", "paper", "scissor"]

while True:
    ccount = 0
    ucount = 0
    uc = int(input('''
    Game Start........
    1 Yes
    2 No | Exit
    '''))

    if uc == 1:
        for a in range(1, 6):
            userInput = int(input('''
            1 Rock
            2 Paper
            3 Scissor
            '''))
            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "paper"
            elif userInput == 3:
                uchoice = "scissor"

            Cchoice = random.choice(l)

            if Cchoice == uchoice:
                print("Computer Value", Cchoice)
                print("User Value", uchoice)
                print("Game Draw")
                ucount = ucount + 1
                ccount = ccount + 1
            elif (uchoice == "rock" and Cchoice == "scissor") or \
                 (uchoice == "paper" and Cchoice == "rock") or \
                 (uchoice == "scissor" and Cchoice == "paper"):
                print("Computer Value", Cchoice)
                print("User Value", uchoice)
                print("You Win")
                ucount = ucount + 1
            else:
                print("Computer Value", Cchoice)
                print("User Value", uchoice)
                print("Computer Win")
                ccount = ccount + 1

        if ucount == ccount:
            print("Final Game Draw")
            print("User Score", ucount)
            print("Computer Score", ccount)
        elif ucount > ccount:
            print("Finally You Win the Game")
            print("User Score", ucount)
            print("Computer Score", ccount)
        else:
            print("Finally Computer Win the Game")
            print("User Score", ucount)
            print("Computer Score", ccount)
    else:
        break
