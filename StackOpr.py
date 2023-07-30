#Use list Data type to Implement a Stack & Queue:
l=[]
while True:
    c = int(input('''
   1 Push element
   2 Pop element
   3 Peek element
   4 Display Stack 
   5 Exit
    '''))
    if c==1:
        n= input("Enter the value:-\n");
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Stack")
        else:
            p =l.pop()
            print(p)
            print(l)
    elif c==3:
        if len(l)==0:
            print("Empty Stack")
        else:
            print("Last Stack Value:-",l[-1])
    elif c==4:
        print("Display Stack:-",l)
    elif c==5:
        break;
    else:
        print("Invalid Opr.....")
    