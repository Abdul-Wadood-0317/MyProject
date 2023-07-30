# import time
# name = input('Enter your Name: ')


# timestap = int(time.strftime("%H:%M:%S"))
# print(timestap)
# timestap = int(time.strftime("%H"))
# print(timestap)
# timestap = int(time.strftime("%M"))
# print(timestap)
# timestap = int(time.strftime("%S"))
# print(timestap)

#OR 
# Morning Time : 04:00:00 to 11:59:59
# Afternoon Time : 12:00:00 to 16:59:59
# Evening Time : 17:00:00 to 20:59:59
# Night Time : 21:00:00 to 03:59:59


import time
name = input("Enter Your Name: ")
day = int(time.strftime("%H"))
if 4<= day <12:
    print('Good morning',name)
elif 12<=day< 17:
    print('Good Aternoon ',name)
elif 17<= day <21:
    print('Good Evening ',name)
else:
    print('Good Night',name)


a = int(input("Enter a Valid Month Number: "))
match a:
    case 1:
      print("January")
    case 2:
      print("February")
    case 3:
      print("March")
    case 4:
      print("April")
    case 5:
      print("May")
    case 6:
      print("June")
    case 7:
      print("July")
    case 8:
      print("August")
    case 9:
      print("September")
    case 10:
      print("Octuber")
    case 11:
      print("November")
    case 12:
      print("December")
    case _:
      print("Please Enter a Valid Month Number")















