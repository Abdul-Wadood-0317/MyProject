#Random Methods
import random as r

n=r.randint(2, 8)
print(n)

n1=r.randrange(2,4)
print(n1)
# if n==n1:
#     print("You are Great, and also good programmer")
# else:
#     print("keep trying")
l=[10,20,30,40]
lc=r.choice(l)
print(lc)

#Random Modules:
#1)random 2)shuffle 3)uniform
a=r.random()
print(a)

l=[10,20,30,40]
r.shuffle(l)
print(l)

u=r.uniform(3, 9)
print(u)

import datetime
x=datetime.datetime.now()
print(x)