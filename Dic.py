#Dictionary Basic Crud Opr performing
d= {
    'Course':'Python',
    'fees':8000,
    'duration':'2 months'
}
f = d['fees']
print(f)
print(type(d))

for n in d:
    print(n)
print()
for n in d:
    print(d[n])

b= {"Name":'Ali',
    "age":15,
    'gender':"male"
}
print(b)
print(b.get("gender"))

ep1={122:45,123:89,567:69,670:69}
ep2={222:67,566:90}
ep1.update(ep2)
print(ep1)