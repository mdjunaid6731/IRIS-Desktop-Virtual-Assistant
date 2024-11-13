from speak import speak
from takecommand import takeCommand
import requests

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()  

        if 'news' in query:
            newsapi = "e557adbb3a0e4ad7b4e4a5d7049aa9da"
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            if r.status_code == 200:
                # Parse the JSON response
                data = r.json()

                # Extract the articles
                articles = data.get('articles', [])

                #print the headlines
                for article in articles:
                    print(article['title'])
                    speak(article['title'])