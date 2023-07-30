i = [10,20,30,50,60]
# t = type(i)
t = len(i)

for l in range(t):
    # print(i)
    print(i[l])
print("")


i = [10,20,30,50,60]
for a in i:
    print(a)
print("")

k = [10,20,30,50,60]
t = len(k)

for a in range(t-1,-1,-1):  #(start,stop,decrement)
    print(k[a])
print("")

b = [10,20,30,40,60,80,90]
t = len(b)
print(t)
print("")

# for a in b:
#     print(a)
# for a in range(t):
#     print(b[a])
for a in range(t-1,-1,-1):
    print(a) #print(b[a])
