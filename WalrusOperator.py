numbers = [1,2,3,4,5]
while (n:=len(numbers))>0:
    print(numbers.pop())
#Aam Zindagi:
# foods = list()
# while True:
#     food = input("What food do you like?:")
#     if food == "quit":
#             break
#     foods.append(food)
#Mentos Zindagi:
foods = list()
while (food := input ("What food do you like?:")) !="quit":
    foods.append(food)