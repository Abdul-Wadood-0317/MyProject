d= {'Course':'Python',
    'fees': 8000,
    'duration':'2 months'
}
#Method 1 to call the key
c= d.get('Course')
print(c)
#Method 2 to call the key
c1 = d['Course']
print(c1)
print()

#key() func to call keys of dic:
d= {"course": "python",
    "fees":8000,
    "duration":"2 months" 
}
for a in d.keys():
    print(a)
print()

#key() func to call value of dic:
d= {"course": "python",
    "fees":8000,
    "duration":"2 months" 
}
for a in d.values():
    print(a)

b = d.get('fees')
print(b)

#items in dic
d = {'course:':'Python',
     'fees:':5000,
     'duration:':'2 weeks'
}
for a,b in d.items():
    print(a,b)

#delete dic element:
d= {'course':'python',
    'fees':7000,
    'duration':'3 months'
}
del d['fees']
print(d)
print()

#pop in dic element:
d ={'course':'python',
'fees':10000,
'duration':'1 month'
}
print(d.pop('duration'))
print(d)
print()
#Methods in Dictionaries:
d = dict (name='python',fees=8000)
print(d)

#update in dictionaries:
d= {'course':'python',
    'fees':4000,
    'duration':'1 month-medium level'
}
d.update({'fees':5000})
d.update({'duration':'2 month become expert'})
print(d)

#clear in all element in dictionaries:
d ={
    'course':'python',
    'fees':4000,
    'duration':'1 month-medium level'
}
d.clear()
print(d)

