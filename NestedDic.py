#Nested Dictionary in Python:
course ={'C++':{'duration':'2 Months','fees':10000},
         'Java':{'duration':'3 Months','fees':7000},
         'Python':{'duration':'1 Months','fees':8000},
}
print(course)
course['Java']['fees']=5000
#get particular key:
print(course['C++']['fees'])
#for loop:
for (k,v) in course.items():
    print(k,v['duration'],v['fees'])