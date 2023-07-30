#Convert string to list
n = input("Enter the Value\n")
print(n)
l = n.split()
print(l)

#Take the input from user and make a list of it:
l = []

for a in range(1,4):
    n = input("Enter the value"+str(a)+":-")
    l.append(n)
    print(l)
