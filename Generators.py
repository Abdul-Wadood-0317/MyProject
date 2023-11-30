#It is used for special  of function that allow you to create an iterable sequence of values.
def my_generator():
    for i in range(500):
        #complex computation
        yield i
gen = my_generator()

for j in gen:
    print(j)
#sha