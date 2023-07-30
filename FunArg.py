def average(a=9,b =1):
    print("The average is", (a+b)/2)
average()

def name(fanme, mname="John",lname="Whatson"):
    print("Hello",fanme,mname,lname)
name("Amy")

def average(*number):
    print(type(number))
    sum = 0
    for i in number:
        sum = sum+i
    print("Average is:",sum/len(number))

average(5,6)

def name(**name):
    print(type(name))
    print("Hello",name["fname"],
name["mname"],name["lname"])

name(mname="Buchaan",lname = "Sarmad",fname='Jamal')
