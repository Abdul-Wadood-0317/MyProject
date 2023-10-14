class Employee:
    company = "Apple"
    def show(self):
        print(f"THe name is {self.name} and company is {self.company}")
        
    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "AbdulWadood"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)
#code bro code 