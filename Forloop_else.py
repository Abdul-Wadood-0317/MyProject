#How to use forloop with else:
for i in range(5):
    print(i)
else:
    print("Sorry no i")

i=0
while i<7:
    print(i)
    i=i+1
    if i==5:
        break
else:
    print("Sorry no i")
