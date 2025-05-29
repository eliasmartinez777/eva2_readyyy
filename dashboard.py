import json
import logging
from datetime import datetime
from weather_service import WeatherService
from news_service import NewsService
from country_service import CountryService
from email_service import EmailService
from config import SENDER_EMAIL

class Dashboard:
    def __init__(self):
        self.weather_service = WeatherService()
        self.news_service = NewsService()
        self.country_service = CountryService()
        self.email_service = EmailService()
        self.logger = logging.getLogger(__name__)
        
    def generate_daily_report(self, city, country='Chile'):
        try:
            self.logger.info(f"Generando reporte para {city}, {country}")
            
            # Obtener datos de todas las APIs
            weather = self.weather_service.get_current_weather(city) or {}
            general_news = self.news_service.get_top_headlines() or []
            business_news = self.news_service.get_business_news() or []
            country_info = self.country_service.get_country_info(country) or {}
            
            # Crear estructura del reporte
            report = {
                'date': datetime.now().strftime('%d/%m/%Y %H:%M'),
                'location': {'city': city, 'country': country},
                'weather': weather,
                'general_news': general_news[:3],  # 3 noticias generales
                'business_news': business_news[:3], # 3 noticias de negocios
                'country_info': country_info
            }
            
            # Procesar reporte
            self.save_report_to_json(report)
            self.display_report(report)
            self.send_report_by_email(report)
            
            return report
            
        except Exception as e:
            self.logger.error(f"Error generando reporte: {str(e)}")
            return {'error': str(e)}

    def save_report_to_json(self, report, filename='daily_report.json'):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
            self.logger.info(f"Reporte guardado en {filename}")
        except Exception as e:
            self.logger.error(f"Error guardando reporte: {str(e)}")

    def display_report(self, report):
        try:
            print("\n" + "="*50)
            print("          INFORME DIARIO COMPLETO")
            print("="*50 + "\n")
            
            # Mostrar información de Chile
            if report.get('country_info'):
                ci = report['country_info']
                print(f"Datos de {ci.get('name', 'Chile')}:")
                print(f"- Capital: {ci.get('capital', 'Santiago')}")
                print(f"- Moneda: {ci.get('currency', 'Peso Chileno')} ({ci.get('currency_symbol', 'CLP')})\n")
            
            # Mostrar información meteorológica
            if 'temperature' in report.get('weather', {}):
                w = report['weather']
                print(f"Clima en {report['location']['city']}:")
                print(f"- Temperatura: {w['temperature']}°C")
                print(f"- Humedad: {w['humidity']}%")
                print(f"- Descripción: {w.get('description', '').capitalize()}\n")
            
            # Mostrar noticias generales
            if report.get('general_news'):
                print("Noticias Generales de Chile:")
                for i, article in enumerate(report['general_news'], 1):
                    print(f"{i}. {article.get('title', 'Sin título')}")
                    print(f"   Enlace: {article.get('url', 'No disponible')}\n")
            
            # Mostrar noticias de negocios
            if report.get('business_news'):
                print("Noticias de Negocios (EE.UU.):")
                for i, article in enumerate(report['business_news'], 1):
                    print(f"{i}. {article.get('title', 'Sin título')}")
                    print(f"   Enlace: {article.get('url', 'No disponible')}\n")
            
            print("="*50 + "\n")
            
        except Exception as e:
            self.logger.error(f"Error mostrando reporte: {str(e)}")

    def send_report_by_email(self, report):
        try:
            subject = f"Reporte Completo - {report['location']['city']} {report['date']}"
            
            # Construir cuerpo del email
            body = "="*50 + "\n"
            body += "       INFORME DIARIO COMPLETO\n"
            body += "="*50 + "\n\n"
            
            # Sección de información de Chile
            if report.get('country_info'):
                ci = report['country_info']
                body += f"Datos de {ci.get('name', 'Chile')}:\n"
                body += f"- Capital: {ci.get('capital', 'Santiago')}\n"
                body += f"- Moneda: {ci.get('currency', 'Peso Chileno')} ({ci.get('currency_symbol', 'CLP')})\n\n"
            
            # Sección meteorológica
            if 'temperature' in report.get('weather', {}):
                w = report['weather']
                body += f"Clima en {report['location']['city']}:\n"
                body += f"- Temperatura: {w['temperature']}°C\n"
                body += f"- Humedad: {w['humidity']}%\n"
                body += f"- Descripción: {w.get('description', '').capitalize()}\n\n"
            
            # Sección de noticias generales
            if report.get('general_news'):
                body += "Noticias Generales de Chile:\n"
                for i, article in enumerate(report['general_news'], 1):
                    body += f"{i}. {article.get('title', 'Sin título')}\n"
                    body += f"   Enlace: {article.get('url', 'No disponible')}\n\n"
            
            # Sección de noticias de negocios
            if report.get('business_news'):
                body += "Noticias de Negocios (EE.UU.):\n"
                for i, article in enumerate(report['business_news'], 1):
                    body += f"{i}. {article.get('title', 'Sin título')}\n"
                    body += f"   Enlace: {article.get('url', 'No disponible')}\n\n"
            
            body += "="*50 + "\n"
            
            # Enviar email
            if self.email_service.send_email(subject, body, SENDER_EMAIL):
                self.logger.info("Email enviado exitosamente")
            else:
                self.logger.error("Error al enviar email")
                
        except Exception as e:
            self.logger.error(f"Error enviando email: {str(e)}")