#We will see other functions in Python
#MAP
# def cub(x):
#     return x*x*x
# print(cub(3))

l = [1,2,4,6,4,3]
# newl = []
# for item in l:
#     newl.append(cub(item))

newl = list(map(lambda x:x*x*x,l))
print(newl)

#Filter 
def filter_function (a):
    return a>2

newl = list(filter(filter_function,l))
print(newl)

#Reduce 
from functools import reduce
#list of numbers
numbers = [1,2,3,4,5]

#Calculate sum of numbers using reduce
def mysum(x,y):
    return x+y
sum = reduce(mysum,numbers)
#print the sum
print(sum)