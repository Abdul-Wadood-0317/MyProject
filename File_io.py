#we will be discussing file handling(IO)
#Reading A File
f =open('myfile.txt','r')
#print(f)
text=f.read()
print(text) 
f.close()

#Wrting A File
f=open('myfile.txt','a')
f.write('Hello,World!')
f.close()
