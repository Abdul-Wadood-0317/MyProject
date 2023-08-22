#In this code we are doing polymorphism
l=[10,20,30,40]
print(len(l))
s = "Welcome"
print(len(s))

#Overloading example:
class Ws:
    def displayinfo(self,name=''):
        print("Welcome to coding:"+name)
obj=Ws()
obj.displayinfo()
obj.displayinfo(" Python")