import requests
from config import OPENWEATHER_API_KEY

class WeatherAPI:
    def __init__(self):
        self.base_url = 'https://api.openweathermap.org/data/2.5'
        self.api_key = OPENWEATHER_API_KEY
    
    def get_current_weather(self, city):
        """Get current weather for a city"""
        try:
            url = f"{self.base_url}/weather?q={city}&appid={self.api_key}&units=metric"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}
    
    def get_forecast(self, city):
        """Get 5-day forecast for a city"""
        try:
            url = f"{self.base_url}/forecast?q={city}&appid={self.api_key}&units=metric"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}
    
    def get_weather_by_coordinates(self, lat, lon):
        """Get weather by latitude and longitude"""
        try:
            url = f"{self.base_url}/weather?lat={lat}&lon={lon}&appid={self.api_key}&units=metric"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}
    
    def get_air_quality(self, lat, lon):
        """Get air quality data"""
        try:
            url = f"{self.base_url}/air_pollution?lat={lat}&lon={lon}&appid={self.api_key}"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}