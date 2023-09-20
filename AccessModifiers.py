class Student:
    def __init__(self) :
        self._name="Abdul"
    def _funName(self):     #protected method
        return "CodeWithWadood"

class Subject(Student):     #inherited class
    pass
obj=Student()
obj1=Subject()

#Calling by object of Student Class
print(obj._name)
print(obj._funName())

#Calling by object of Subject Class
print(obj1._name)
print(obj1._funName())