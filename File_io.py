#we will be discussing file handling(IO)
#Reading A File
f =open('myfile.txt','r')
#print(f)
text=f.read()
print(text) 
f.close()
