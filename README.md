📌 Descripción del Proyecto
Aplicación Python que integra datos meteorológicos y noticias actuales, generando reportes diarios y enviándolos por correo electrónico automáticamente.

🌟 Características Principales
Datos climáticos en tiempo real de OpenWeatherMap API

Últimas noticias de NewsAPI

Envío automático de reportes por correo electrónico

Almacenamiento local de reportes en formato JSON

Interfaz de consola clara y detallada

📦 Requisitos
Python 3.8+

Cuentas en:

OpenWeatherMap

NewsAPI

Google Cloud Platform (para OAuth de Gmail)

🚀 Instalación
1.Clonar el repositorio: 
git clone https://github.com/eliasmartinez777/eva2_readyyy
cd weather-news-dashboard 
2.Instalar dependencias:
pip install -r requirements.txt 

3.Configurar credenciales:

Renombrar credentials.example.json a credentials.json 
⚙️ Configuración
Editar config.py para personalizar:
DEFAULT_CITY = "La Serena"  # Ciudad a monitorear
DEFAULT_COUNTRY = "cl"      # Código de país (CL para Chile)
SENDER_EMAIL = "tu_email@gmail.com"  # Email re
🏃‍♂️ Ejecución
python main.py 
La primera ejecución abrirá tu navegador para autenticación con Google.
weather-news-dashboard/
├── main.py                # Punto de entrada
├── dashboard.py           # Lógica principal
├── weather_service.py     # Clima
├── news_service.py        # Noticias
├── country_service.py     # Datos de países
├── email_service.py       # Envío de emails
├── config.py              # Configuración
├── credentials.json       # Credenciales Gmail (OAuth)
├── requirements.txt       # Dependencias
└── README.md              # Este archivo
📧 Configuración de Gmail
Habilitar API Gmail en Google Cloud Console
Crear credenciales OAuth 2.0
Descargar archivo JSON y guardar como credentials.json
Agregar tus claves de API en config.py
