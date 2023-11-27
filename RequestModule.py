# from urllib import requests
from pip._vendor import requests
import pip._vendor.requests
response = requests.get("https://www.wikipedia.com")
print(response.text)
