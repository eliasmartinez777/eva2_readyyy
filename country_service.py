import requests
import logging

class CountryService:
    BASE_URL = "https://restcountries.com/v3.1/"
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    def get_country_info(self, country_name):
        try:
            url = f"{self.BASE_URL}name/{country_name.lower()}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()[0]
            currencies = data.get('currencies', {})
            currency_info = next(iter(currencies.values())) if currencies else {}
            
            return {
                'name': data.get('name', {}).get('common', 'Chile'),
                'capital': data.get('capital', ['Santiago'])[0],
                'population': data.get('population', 0),
                'currency': currency_info.get('name', 'Peso Chileno'),
                'currency_symbol': currency_info.get('symbol', 'CLP')
            }
            
        except Exception as e:
            self.logger.error(f"Error obteniendo datos del país: {str(e)}")
            return {
                'name': 'Chile',
                'capital': 'Santiago',
                'currency': 'Peso Chileno',
                'currency_symbol': 'CLP'
            }