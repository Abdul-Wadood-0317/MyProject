#We will see read,readlines and other methods:
f=open('myfile.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    print(f"Marks of Student {i}in Math is:{m1*2}")
    print(f"Marks of Student {i}in English is:{m2*2}")
    print(f"Marks of Student {i}in SST is:{m3*2}")