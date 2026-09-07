class WeatherParser:
    @staticmethod
    def parse_current_weather(data):
        """Parse current weather data"""
        if 'error' in data:
            return None
        
        return {
            'city': data.get('name'),
            'country': data.get('sys', {}).get('country'),
            'temperature': data.get('main', {}).get('temp'),
            'feels_like': data.get('main', {}).get('feels_like'),
            'humidity': data.get('main', {}).get('humidity'),
            'pressure': data.get('main', {}).get('pressure'),
            'weather': data.get('weather', [{}])[0].get('main'),
            'description': data.get('weather', [{}])[0].get('description'),
            'icon': data.get('weather', [{}])[0].get('icon'),
            'wind_speed': data.get('wind', {}).get('speed'),
            'wind_deg': data.get('wind', {}).get('deg'),
            'clouds': data.get('clouds', {}).get('all'),
            'visibility': data.get('visibility'),
            'sunrise': data.get('sys', {}).get('sunrise'),
            'sunset': data.get('sys', {}).get('sunset')
        }
    
    @staticmethod
    def parse_forecast(data):
        """Parse forecast data"""
        if 'error' in data:
            return []
        
        forecasts = []
        for item in data.get('list', []):
            forecasts.append({
                'datetime': item.get('dt'),
                'temperature': item.get('main', {}).get('temp'),
                'feels_like': item.get('main', {}).get('feels_like'),
                'humidity': item.get('main', {}).get('humidity'),
                'weather': item.get('weather', [{}])[0].get('main'),
                'description': item.get('weather', [{}])[0].get('description'),
                'icon': item.get('weather', [{}])[0].get('icon'),
                'wind_speed': item.get('wind', {}).get('speed'),
                'rain': item.get('rain', {}).get('3h', 0),
                'clouds': item.get('clouds', {}).get('all')
            })
        return forecasts
    
    @staticmethod
    def parse_air_quality(data):
        """Parse air quality data"""
        if 'error' in data:
            return None
        
        aqi = data.get('list', [{}])[0].get('main', {}).get('aqi', 0)
        components = data.get('list', [{}])[0].get('components', {})
        
        aqi_levels = {1: 'Good', 2: 'Fair', 3: 'Moderate', 4: 'Poor', 5: 'Very Poor'}
        
        return {
            'aqi': aqi_levels.get(aqi, 'Unknown'),
            'pm25': components.get('pm2_5'),
            'pm10': components.get('pm10'),
            'o3': components.get('o3'),
            'no2': components.get('no2'),
            'so2': components.get('so2'),
            'co': components.get('co')
        }