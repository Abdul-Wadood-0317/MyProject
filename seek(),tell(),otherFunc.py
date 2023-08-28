#We will see other functions like seek ()and tell()
with open('sample.txt','r')as f:
    print(type(f))
    f.seek(10) #using seek functions
    print(f.tell()) #using tell functions 
    data = f.read(5)
    print(data)

with open('sample.txt','w')as f:
    f.write('Hello World3!')
    f.truncate(5)
with open('sample.txt','r') as f:
    print(f.read())