#In this code we are doing polymorphism(Same function name but different signature and being uses for different types:)
l=[10,20,30,40]
print(len(l))
s = "Welcome"
print(len(s))

#Overloading example:(function name same but different parameters)
# class Ws:
#     def displayinfo(self,name=''):
#         print("Welcome to coding:"+name)
# obj=Ws()
# obj.displayinfo()
# obj.displayinfo(" Python")

#Overriding example:(same function name but different class is called overriding)
class Ws:
    def displayinfo(self):
        print("Welcome to Python ")

class IIP(Ws):
    def displayinfo(self):
        super().displayinfo()
        print("Welcome to IIp")

obj=IIP()
obj.displayinfo()
