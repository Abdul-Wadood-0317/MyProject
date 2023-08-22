#overloading example:
class Area:
    def find_area(self,x=None,y=None):
        if x!=None and y!=None:
            print("Area of rectangle:",(x*y))
        elif x!=None:
            print("Area of square:",(x*x))
        else:
            print("Nothing")

obj1=Area()
obj1.find_area()
obj1.find_area(10)
obj1.find_area(10,20)

#Method overriding example:
