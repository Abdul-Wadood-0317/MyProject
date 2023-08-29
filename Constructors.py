class Person:
    def __init__(self,name,occ) :
        print("Hey, I am a Person")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Abdul","Full stack")
b = Person("Eman","HR")

a.info()
b.info()

# print(a.name)
# a.name = "Eman"
# a.occ = "HR"
# a.info()


