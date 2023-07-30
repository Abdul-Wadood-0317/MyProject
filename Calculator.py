#Simple Calculator
# a = 2
# b = 3

# print("The value of", a,"+",b,"is:",a+b)
# print("The value of", a,"-",b,"is:",a-b)
# print("The value of", a,"*",b,"is:",a*b)
# print("The value of", a,"/",b,"is:",a/b)
# print("The value of", a,"%",b,"is:",a%b)
# print("The value of", a,"//",b,"is:",a//b)
# print("The value of", a,"**",b,"is:",a**b)

a = int(input("Enter the Value1: "))
b = int(input("Enter the Value2: "))
c = input("Enter the Opr..(+,-,*,/)")
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    print(a/b)
else:
    print('Invalid Opr')