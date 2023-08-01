t =(10,20,30,40,50)
u=(10)
print(type(t))
print(type(u))
print()

for i in t:
    print(i)
print()
#Get the index value of tuple:
n=t[3]
print(n)

#Find the index value in tuple:
t= (10,20,30,40,50)
l=len(t)
print(t[0])
print()
#To get the index value
for i in range (l):
    print(i)
print()
#To get the values from item of tuple
for a in range (l):
    print(t[a])

#Tuple Funct:
#1)min 2)max 3) count 4) index 5) sum()
t=(5,6,7,8,9,10)
i= min(t)
print(i)

t=(5,6,7,8,9,10)
i= max(t)
print(i)

t=(5,6,7,8,9,10,6,6)
i=t.count(5)
print(i)

t=(5,6,7,8,9,10)
i=t.index(7)
print(i)
print()

t=(5,6,7,8,9,10)
i= sum(t,5)
print(i)

