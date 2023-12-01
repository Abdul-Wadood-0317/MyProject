import re
pattern = r"[A-Z]+yclone"
text = '''Cyclone are rapidly-rotating storm systems that rotate cyclone (counter-clockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere) around a low pressure centre. They are 
generally slow moving but severe,cyclone dyclone with winds of between 120-320 kilometres an cyclone hour.'''

# match = re.search(pattern,text)
# print(match)

matches = re.finditer(pattern,text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])
