l = [1,2,3,4,5]
print(type(l))

l = [1,2,3,4,5]
print(l[2])

m = [1,2,3,[4,5,6]]
print(m[3][1])

l = [2,3,"Hello",[3,4,5]]
print(l[2])

print(l[0:2])
print(l[1:])

o = [1,2,3,4,5]
print(o[0::2])

print(o[-1::-1])

l= [10,30,40,50,'Hello']
print(l[3],l[4])

print(l[0:3])

l= [10,30,40,50,'Hello']
print(l[1:])

l= [10,30,40,50,'Hello']
print(l[-1::-2])

l = [1,2,3,45,5]
l.reverse()
l.sort()
print(l.count(5))
print(l)
