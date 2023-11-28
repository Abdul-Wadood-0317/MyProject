# from urllib import requests
from pip._vendor import requests
from bs4 import BeautifulSoup
import pip._vendor.requests

url = "www.geekforgeeks.com"
r = requests.get(url)
print(r.text)
soup =BeautifulSoup(r.text,"html.parser")
print(soup.prettify())
# response = requests.get("https://www.wikipedia.com")
# print(response.text)
#