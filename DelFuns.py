l = [20,30,50,60]
del l[3]
print(l)

l = [20,30,50,60]

print(l.pop(2))
print(l)

l =[20,30,50,60]
l.remove(20)
print(l)

l =[20,30,50,60]
l.clear()
print(l)    #gives empty list

l =[20,30,50,60]
l[0] = (10,40)
l[1] = 20
print(l)

l =[20,30,50,60]
l.insert(2,40)
# l.insert(3,50)
print(l)

l = [20,30,50,60]
l.append(70)
l.append((80,90))
print(l)

l = [20,30,50,60]
l.insert(2,40)
n = [70,80]
l.extend(n)
print(l)
print(l[0])
print(l[1])
print(l[2])
print(l[3])
