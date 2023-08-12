x=10    #global Variable
def my_function():
    global x
    x=4
    y=5 #local Variable
    print(y)
my_function()
print(x)