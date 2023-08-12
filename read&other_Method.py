#We will see read,readlines and other methods:
f=open('myfile.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break