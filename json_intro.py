#Convert json into string 
# import json
# d={
#     'course_name':'Python',
#     'fees':15000
# }

# f=json.dumps(d)
# print(type(f))
# print(f)

#Convert json datato object data
import json
d='{    "cname":"Python","fees":12000,"duration":"2Months"    }'
x=json.loads(d)
print(type(x))
# print(x)

#Iterate the function
for a in x:
    print(a,x[a])
