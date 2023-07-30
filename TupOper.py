countries = ("Spain","Italy","Canada","England","Germany")
temp = list(countries)
print(type(countries))
temp.append("Portugal")
temp.pop(3)
temp[1] = "Poland"
countries = tuple(temp)
print(countries)
print(temp)
print("")

countries2 = ("Pakistan", "Turkey","Bangla")
countries3 = ("India","China")
SouthEastAsia = (countries2+countries3)
print(SouthEastAsia)
print("")

#For Check count method in tuple
tuple1 = (0,1,2,34,4,56,7,1,1,2,2)
res = tuple1.count(2)
print("Count of 3 is:",res)

#For check index
tuple1 = (0,1,2,34,5,56,7,1,1,2,2)
res = tuple1.index(5)
print("Count of 3 is:",res)