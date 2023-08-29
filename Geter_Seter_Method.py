# class Student:
#     def __init__(self) :
#         self.__name__=""
#     def getname(self):
#         return self.__name__
#     def setname(self,name):
#         self.__name__=name
# obj=Student()
# obj.setname("Testing")
# name=obj.getname()
# print(name)
# #Keep doing and Hardwork,Never give up!

class MyClass:
    def __init__(self,value) :
        self._value = value
    
    def show(self):
        print(f"value is {self._value}")
    @property
    def ten_value(self):
        return 10*self._value
    
    @ten_value.setter
    def ten_value(self,new_value):
        self._value = new_value/10
obj = MyClass(10)
obj.ten_value =67
print(obj.ten_value)
obj.show()

