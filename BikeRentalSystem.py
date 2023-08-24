#We are making Bike Ranking System:
class bikeshop:
    def __init__ (self,stock):
        self.stock = stock
    def displayinfoBike(self):
        print("Total Bikes",self.stock)
    def rentForBike(self,q):
        if q<0:
            print("Enter the positive value or greater than zero")
        elif q>self.stock:
            print("Enter the vlaue (less than stack)")
        else:
            self.stock=self.stock-q
            print("Total Prices",q*100)
            print("Total Bikes",self.stock)
while True:
    obj=bikeshop(100)
    uc=int(input('''
1 Display Stocks
2 Rent a Bike
3 Exit
'''))
    if uc == 1:
        obj.displayinfoBike()
    elif uc ==2:
        n=int(input("Enter the Quantity:"))
        obj.rentForBike(n)
    else:
        break
#Just move on man!
