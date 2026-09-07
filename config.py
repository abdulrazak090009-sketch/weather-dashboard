import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
FLASK_ENV = os.getenv('FLASK_ENV', 'production')
FLASK_DEBUG = os.getenv('FLASK_DEBUG', False)