import requests
import logging
from config import NEWS_API_KEY

class NewsService:
    BASE_URL = "https://newsapi.org/v2/"
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    def get_top_headlines(self, country='cl'):
        try:
            url = f"{self.BASE_URL}top-headlines"
            params = {
                'country': country,
                'apiKey': NEWS_API_KEY
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json().get('articles', [])
            
        except Exception as e:
            self.logger.error(f"Error fetching news: {str(e)}")
            return []

    def get_business_news(self):
        try:
            url = f"{self.BASE_URL}top-headlines"
            params = {
                'country': 'us',
                'category': 'business',
                'apiKey': NEWS_API_KEY
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json().get('articles', [])
            
        except Exception as e:
            self.logger.error(f"Error fetching business news: {str(e)}")
            return []