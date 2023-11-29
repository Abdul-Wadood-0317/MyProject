# import requests

# def get_news(api_key, topic):
#     base_url = "https://newsapi.org/v2/top-headlines"
#     params = {
#         'apiKey': api_key,
#         'q': topic,
#     }

#     response = requests.get(base_url, params=params)

#     if response.status_code == 200:
#         articles = response.json().get('articles', [])

#         if not articles:
#             print("No news found for the specified topic.")
#         else:
#             for index, article in enumerate(articles, 1):
#                 print(f"--- Article {index} ---")
#                 print(f"Title: {article['title']}")
#                 print(f"Author: {article['author']}")
#                 print(f"Description: {article['description']}")
#                 print(f"URL: {article['url']}")
#                 print("\n")
#     else:
#         print(f"Error {response.status_code}: {response.text}")

# if __name__ == "__main__":
#     api_key = 'a6424b665b0343248fc27892d2b9b955'

#     while True:
#         user_input = input("What type of news are you interested in? (Type 'exit' to quit): ")

#         if user_input.lower() == 'exit':
#             break

#         get_news(api_key, user_input)
import requests
import json 

query = input("What type of news are you intereted in?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-10-29&sortBy=publishedAt&apiKey=a6424b665b0343248fc27892d2b9b955"
r = requests.get(url)
news = json.loads(r.text)

# print(news,type(news))
for article in news ["articles"]:
    print(article["title"])
    print(article["description"])
    print("---------------------")
