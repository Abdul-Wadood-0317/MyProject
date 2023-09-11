# #Inheritance is two or more object is called inheritance:
# # #Single line Inheritance:
# # class A:
# #     def displayA(self):
# #         print("Welcome to programming A")
    
# # class B(A):
# #     def displayB(self):
# #         print("Welcome to Programming B")
# # obj=B()
# # obj.displayA()
# # obj.displayB()

# #Multi-Level inheritance:
# # class A:
# #     def displayA(self):
# #         print("Welcome to Programming A")

# # class B(A):
# #     def displayB(self):
# #         print("Welcome to programming B")

# # class C(B):
# #     def displayC(self):
# #         print("Welcome to Programming C")

# # obj =C()
# # obj.displayA()
# # obj.displayB()
# # obj.displayC()

# #Now Multi-Level Inheritance!
# class A:
#     def displayA(self):
#         print("Welcome to programming A")
# class B:
#     def displayB(self):
#         print("Welcome to programming B")

# class C(A,B):
#     def displayC(self):
#         print("Welcome to programming C")

# obj=C()
# obj.displayA()
# obj.displayB()
# obj.displayC()

#Inheritance = when a class derives from another class:
class Employee:
    def __init__(self, name, id) :
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")
class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")
        
e1 = Employee("Ali khan",400)
e1.showDetails()
e2 = Programmer("Abdul",4100)
e2.showDetails()
e2.showLanguage()
#be consistent bro