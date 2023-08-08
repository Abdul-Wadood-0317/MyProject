#Read and write json file
import json
file =open("post.json","r")
x=file.read()
finaldata=json.loads(x)

for a in finaldata:
    print(a['title'],a['userId'])