import requests
import logging
from config import OPENWEATHER_API_KEY

class WeatherService:
    BASE_URL = "https://api.openweathermap.org/data/2.5/"
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    def get_current_weather(self, city, country_code='cl'):
        try:
            url = f"{self.BASE_URL}weather"
            params = {
                'q': f"{city},{country_code}",
                'appid': OPENWEATHER_API_KEY,
                'units': 'metric',
                'lang': 'es'
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            return {
                'city': data.get('name', city),
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'],
                'wind_speed': data['wind']['speed']
            }
            
        except Exception as e:
            self.logger.error(f"Error obteniendo clima: {str(e)}")
            return None