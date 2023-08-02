#Number Guessing Game:
import random
Cnumber=random.randrange(1,101)
userInput=int(input("Enter the value:"))
if Cnumber>userInput:
    print("Computer Number:",Cnumber)
    print("Your number is too low")
elif userInput>Cnumber:
    print("Computer Number:",Cnumber)
    print("Your number is too high")
else:
    print("Compute Number:",Cnumber)
    print("Your number is equal")