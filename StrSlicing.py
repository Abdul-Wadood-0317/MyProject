# name = "Waleed,Wadood"
# print(name[0:10])
# print(len(name))

Fruit = 'Bannana'
Fruitlen = len(Fruit)
print (Fruitlen)
print(Fruit[0:2])
print(Fruit[5])
print(Fruit[0:-5])
nm = 'Abdul'
print(nm[-4:-2])

#Uppercase and Lower Case in Strings and remember strings are immutable(cannot change).
a = 'Waleed'
len1= len(a)
print(len1)
print(a.upper())
print(a.lower())
print(a.replace('Abdul-Wadood','Ali'))

BlogHeading = "introduction to PYTHON"  #It'll capital only first Characters
print(BlogHeading.capitalize())

print(a.count("e")) 

str = 'Waleed is a Good boy'
print(str.find("is"))
# print(str.index("boy"))

str1= "Welcometoconsole"
print(str1.isalnum())

str1= "Welcome"
print(str1.isalpha())

str = 'Welcome'
print(str.islower())

str = 'You are great\n'
print(str)
print(str.isprintable())

str = 'Python is Interpreted language'
print(str.startswith("is"))

str = 'yOU aRE pYTHON'  #Convert lower to upper and Vice-Versa
print(str.swapcase())

str = 'You are a good boy' #In str it capitalize the each alphabet of a word
print(str.title())
