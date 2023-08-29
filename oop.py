#Now we movig towards Object Oriented
# class DemoClass:
#     a =10
#     def sumvalue(self):
#         print(20+30)

# demoobject=DemoClass()
# demoobject1=DemoClass()
# print(demoobject.a)
# print(demoobject1.a)
# demoobject.sumvalue()

#Encapsulation
#Polymorphism
#Inheritance

class Person:
    name = "Ahmed"
    occupation = 'Software Developer'
    networth = 10
    def info (self):
        print(f"{self.name} is a {self.occupation}")
a = Person()
b = Person()
c = Person()

a.name = "Ali"
a.occupation = 'Manager'

b.name = 'Wali'
b.occupation = 'HR'
# print(a.name,a.occupation)
a.info()
b.info()
c.info()

