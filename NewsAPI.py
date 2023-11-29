#Write a Python program that uses the NewsAPI and the request module to fetch the daily news related to different topics
import requests
from datetime import datetime

def fetch_news(api_key, topic):
    # NewsAPI endpoint URL
    url = "https://newsapi.org/v2/top-headlines"

    # Specify the parameters for the API request
    params = {
        'apiKey': api_key,
        'country': 'us',  # You can change the country code if needed
        'category': topic,
    }

    # Make the API request
    response = requests.get(url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        news_data = response.json()

        # Print the headlines and articles
        print(f"\nTop headlines in '{topic.capitalize()}' on {datetime.now().strftime('%Y-%m-%d')}:")
        for i, article in enumerate(news_data['articles'], start=1):
            print(f"{i}. {article['title']}")
            print(f"   {article['url']}")
            print()

    else:
        # Print an error message if the request was not successful
        print(f"Error: Unable to fetch news. Status code: {response.status_code}")

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual NewsAPI key
    api_key = 'a6424b665b0343248fc27892d2b9b955'

    # Specify the topics you are interested in
    topics = ['business', 'technology', 'science', 'sports', 'health', 'entertainment']

    # Fetch news for each topic
    for topic in topics:
        fetch_news(api_key, topic)
#code bro 