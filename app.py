from flask import Flask, render_template, request, jsonify
from weather_api import WeatherAPI
from weather_parser import WeatherParser
import json

app = Flask(__name__)
weather_api = WeatherAPI()
weather_parser = WeatherParser()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather/<city>')
def get_weather(city):
    """Get current weather for a city"""
    data = weather_api.get_current_weather(city)
    parsed_data = weather_parser.parse_current_weather(data)
    return jsonify(parsed_data)

@app.route('/api/forecast/<city>')
def get_forecast(city):
    """Get 5-day forecast"""
    data = weather_api.get_forecast(city)
    parsed_data = weather_parser.parse_forecast(data)
    return jsonify(parsed_data)

@app.route('/api/coordinates', methods=['POST'])
def get_weather_by_coords():
    """Get weather by coordinates"""
    coords = request.get_json()
    lat = coords.get('lat')
    lon = coords.get('lon')
    
    weather_data = weather_api.get_weather_by_coordinates(lat, lon)
    air_quality_data = weather_api.get_air_quality(lat, lon)
    
    weather = weather_parser.parse_current_weather(weather_data)
    air_quality = weather_parser.parse_air_quality(air_quality_data)
    
    return jsonify({'weather': weather, 'air_quality': air_quality})

@app.route('/api/air-quality/<city>')
def get_air_quality(city):
    """Get air quality for a city"""
    weather_data = weather_api.get_current_weather(city)
    if 'error' in weather_data:
        return jsonify({'error': 'City not found'})
    
    lat = weather_data.get('coord', {}).get('lat')
    lon = weather_data.get('coord', {}).get('lon')
    
    air_quality_data = weather_api.get_air_quality(lat, lon)
    air_quality = weather_parser.parse_air_quality(air_quality_data)
    
    return jsonify(air_quality)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)