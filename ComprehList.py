l =[]
for a in range(1,101):
    l.append(a)  #OR print(a)
print(l)
print("")

n = [h for h in range(1,101) ]
print(n)
print("")
#Only Pass even numbers from 1 to 100
n = [h for h in range(1,101) if h%2==0]
print(n)
print("")
#Only pass odd numbers from 1 to 100
n = [h for h in range(1,101) if h%2!=0]
print(n)
print("")

s = 'Hello'
d = [g for g in s]
print(d)