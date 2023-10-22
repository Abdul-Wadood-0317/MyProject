#Magic methods in Python are the special methods and  that
# start and end with the double underscores.

#code starts from here
#1)__init__ method:
class Employee:
    name = "Harry"
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
e=Employee()
print(e.name)
print(len(e.name))

#__str__ and __rep__ method:
class Employee:
    def __init__ (self, name):
        self.name = name
    def __len__(self):
        i= 0 
        for c in self.name:
            i = i+1
        return i
    def __str__(self):
        return f"The name of employee is {self.name} str"
    
    def __repr__(self):
        return f"Employee('{self.name}')"

    def __call__(self):
        print("Hey I am good boy")
