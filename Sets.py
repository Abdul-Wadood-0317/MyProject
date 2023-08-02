#Sets in Pyhton
#Display an empty set:
wadood= set()
print(type(wadood))

info = {"Carla",19,5.9,15,False} 
print(info)

for value in info:
    print(value)
    
s={10,20,30,40,50}
print(s)

for a in s:
    print(a)

#Set Functions
#1)Sets 2) remove 3)discard 4)pop 5) clear 6) add 7) update
l=[10,20,30,40]
m=set(l)
print(type(m))

s={10,20,30,40,50}
s.discard(10)
print(s)

s={10,20,30,40,50}
s.remove(10)
print(s)

s={10,20,30,40,50}
s.pop()   #Delete random item
print(s)


s={10,20,30,40,50}
s.clear()   #Delete all items
print(s)


s={10,20,30,40,50}
s.add(60)
print(s)

l=[10,80,90]
s={20,10,30}
s.update(l)
print(s)