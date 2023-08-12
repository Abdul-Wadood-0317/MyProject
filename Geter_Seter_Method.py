class Student:
    def __init__(self) :
        self.__name__=""
    def getname(self):
        return self.__name__
    def setname(self,name):
        self.__name__=name
obj=Student()
obj.setname("Testing")
name=obj.getname()
print(name)
#Keep doing and Hardwork