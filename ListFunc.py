#List Function 

#1)count() 
#2)max() 
#3)min() 
#4)sort() 
#5)reverse() 
#6)index() 

#To count a number in a list:
l = [10,20,30,40,10]
a = (l.count(10))

print(type(l))
print(a)

#To find the max of the list
m = max(l)
print(m)

#To find the max in str of list
n =['Hello',"World"]
m = max(n)
print(m)

#To find the min in str of list
n =['Hello',"World"]
print(min(n))

#To find the min number of list
l = [10,20,30,50,10] 
m = min(l)
print(m)
print(min(l))

#To arrange number in Ascending order
l = [10,20,30,50,10]
l.sort()
print(l)

# To arrange number in Decending order
l = [10,20,30,50,10]
l.sort(reverse=True)
print(l)

# To arrange number in Reverse order
l = [10,20,30,50,10]
l.reverse()
print(l)

# To find index number in list
l = [10,20,30,50,10]
a=l.index(50)
print(a)

