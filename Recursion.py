#To calculate the factorial of a number using Recursion function:
# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n *factorial(n-1)
# print(factorial(5))


#Practice :
# a=int(input("Enter the value:-"))
# def factorial(a):
#     if (a==0 or a==1):
#         return 1
#     else:
#         return a *factorial(a-1)
# print(factorial(a))

#Quizk Quiz:
a=int(input("Enter the value:-"))
def fibonacci(n):
    if (n==0 or n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
for i in range (a):
    print(fibonacci(i))
