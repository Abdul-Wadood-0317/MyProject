#Using List Data Type to implement Queue Operations:
l=[]
while True:
    c= int(input('''
      1  Push Element
      2  Pop Element
      3  Front Element
      4  Last Element
      5  Display Queue
      6  Exit
    '''))

    if c==1:
        n=input("Enter the value:-\n");
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Queue")
        else:
            del l[0]
            print(l)
    elif c==3:
        if len (l)==0:
            print("Empty Queue")
        else:
            print("First Queue Value:-",l[0])
    elif c==4:
        if len(l)==0:
            print("Empty Queue")
        else:
            print("last Queue Value:-",l[-1])
    elif c==5:
        print("Display Queue",l)
    elif c==6:
        break;
    else:
        print("Invalid Opr........")

