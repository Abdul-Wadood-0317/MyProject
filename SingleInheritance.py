#In this instant work,we will be working on single inheritance
class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print(f"sound made by the animal")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species = "Dog")
        self.breed = breed
    def make_sound(self):
        print("Bark!")

d = Dog("Dog","Dogerman")
d.make_sound()
a = Animal("Dog","Dog")
a.make_sound()
