#Raising Custom Errors
a = (input("Enter Correct Passcode:"))
try:
    if (int(a)<5 or int(a)>9):
        raise ValueError("Value should be between 5 and 9")
    
except:
    if (a!="quit"):
        raise ValueError("Incorrect Password")

