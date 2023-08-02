def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if (a>b):
     print("First Number is greater")
    else:
     print("Second Number is greater or equal")
    

a = 9
b = 8
isGreater (a,b)
calculateGmean(a,b)

c = 8
d = 9
isGreater(c,d)
calculateGmean(c,d)
# if (c>d):
#     print("First Number is greater")
# else:
#     print("Second Number is greater or equal")

def showdata():
    print("Welcome to Python Program")
showdata()

def sum_arg(a,b):
    print(a+b)
sum_arg(4, 5)

def sum_value(a,b=7):
    print(a+b)
sum_value(2,4)

def Sum_Value(a=5,b=3):
    print(a*b)
Sum_Value()

def square(x):
    return(x*x) #return is used for we don't want to print the input
s=square(4)
print(s)
