# from urllib import requests
import requests
# from bs4 import BeautifulSoup

# url = "https://www.geeksforgeeks.org/"
# r = requests.get(url)
# print(r.text)
# soup =BeautifulSoup(r.text,"html.parser")
# print(soup.prettify())
# for heading in soup.find_all("h2"):
#     print(heading.text)
# response = requests.get("https://www.wikipedia.com")
# print(response.text)
url="https://jsonplaceholder.typicode.com/posts"
data = {
    "title":'Ahmed',
    "body":'bhai',
    "userId":10,
    }
headers ={
    'content-type':
    'application/json; charset = UTF-8',
    }
response = requests.post(url,headers=headers,json = data)
print(response.text)