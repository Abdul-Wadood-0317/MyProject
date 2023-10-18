#Mainly Super Keyword is used child class method in to parent class method and to call them 
class Employee:
    def __init__ (self,name,id):
        self.name = name
        self.id = id
class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang
rohan =Employee("AbdulWadood","760")
waleed = Programmer("Asad","2345","Python")
print(waleed.name)
print(waleed.id)
print(waleed.lang)
