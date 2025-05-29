import logging
from dashboard import Dashboard
from config import DEFAULT_CITY, DEFAULT_COUNTRY

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler()
        ]
    )

def main():
    setup_logging()
    
    try:
        print("Iniciando aplicación...")
        dashboard = Dashboard()
        report = dashboard.generate_daily_report(DEFAULT_CITY, DEFAULT_COUNTRY)
        
        if report and 'error' not in report:
            print("¡Proceso completado exitosamente!")
        else:
            print("Ocurrió un error en el proceso")
            
    except Exception as e:
        print(f"Error fatal: {str(e)}")

if __name__ == "__main__":
    main()