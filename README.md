🌦️ Weather & News Dashboard
Proyecto de evaluación práctica: integración de APIs públicas usando Python para generar un dashboard diario con información del clima, noticias relevantes y envío automático por correo electrónico.

📦 Funcionalidades
✅ Obtener clima actual (OpenWeatherMap)
✅ Obtener noticias relevantes (NewsAPI)
✅ Obtener datos del país (REST Countries)
✅ Generar un reporte diario (JSON y TXT)
✅ Enviar el reporte por correo automáticamente con la API de Gmail
🧱 Estructura del Proyecto
weather_news_dashboard/
├── config.py
├── weather_service.py
├── news_service.py
├── country_service.py
├── dashboard.py
├── gmail_service.py
├── main.py
├── requirements.txt
├── .env              # Claves API 
├── credentials.json  # OAuth Gmail 
└── token.json        # Generado automáticamente 
⚙️ Instalación y Configuración
1. Clona el repositorio y entra a la carpeta:
git clone https://github.com/tuusuario/weather_news_dashboard.git
cd weather_news_dashboard
2. Crea un entorno virtual:
python -m venv venv
source venv/bin/activate        # En Linux/macOS
venv\Scripts\activate           # En Windows
3. Instala las dependencias:
pip install -r requirements.txt
4. Crea el archivo .env con tus claves:
OPENWEATHER_API_KEY=tu_api_key_openweather
NEWS_API_KEY=tu_api_key_newsapi
5. Habilita Gmail API:
Ve a Google Cloud Console
Crea un proyecto nuevo
Activa la Gmail API
Crea credenciales OAuth2 (tipo escritorio)
Descarga el archivo credentials.json y colócalo en la raíz del proyecto
🚀 Ejecución
python main.py
Esto generará:

reporte_diario.json
reporte_diario.txt
Un correo será enviado automáticamente con el contenido del reporte
📬 Automatización
Puedes automatizar la ejecución con tareas programadas o cron.

Ejemplo cron (envío diario a las 8:00 AM):
0 8 * * * /ruta/a/tu/proyecto/venv/bin/python /ruta/a/tu/proyecto/main.py
🌐 APIs Utilizadas
API	Función	Registro
OpenWeatherMap	Clima actual y pronóstico	✅
NewsAPI	Noticias principales o por término	✅
REST Countries	Información de país (capital, moneda)	❌
Gmail API	Envío automático del reporte diario	✅
🧪 Ejemplo de Salida
Ciudad: La Serena (Chile)
Capital: Santiago
Población: 19.1 millones
Moneda: Peso Chileno

Clima:
- Descripción: nubes dispersas
- Temperatura: 17°C
- Humedad: 68%
- Viento: 5 km/h

Noticias Principales:
- Gobierno anuncia inversión en infraestructura solar
- Aumentan los índices de turismo en el norte

Noticias sobre Clima:
- Frente frío afectará la zona centro-sur este fin de semana
📌 Autores
Elias Martinez - Ivan Orostegui - Fernando
