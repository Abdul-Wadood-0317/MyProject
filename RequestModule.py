# from urllib import requests
import requests
from pip._vendor import requests
from bs4 import BeautifulSoup
import pip._vendor.requests

url = "www.geeksforgeeks.org"
r = requests.get(url)
print(r.text)
soup =BeautifulSoup(r.text,"html.parser")
print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)
# response = requests.get("https://www.wikipedia.com")
# print(response.text)
