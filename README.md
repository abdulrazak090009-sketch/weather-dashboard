# Weather Dashboard

A real-time weather dashboard application that fetches data from OpenWeatherMap API.

## Features

- **Current Weather**: Real-time temperature, humidity, wind speed, pressure
- **5-Day Forecast**: Weather predictions for the next 5 days
- **Air Quality**: PM2.5, PM10, O3, NO2 levels
- **Geolocation**: Get weather for your current location
- **Search**: Search weather for any city worldwide
- **Responsive Design**: Works on desktop and mobile devices

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Get API Key**:
   - Sign up at [OpenWeatherMap](https://openweathermap.org/api)
   - Get your free API key

3. **Configure**:
   - Copy `.env.example` to `.env`
   - Add your OpenWeatherMap API key

4. **Run**:
   ```bash
   python app.py
   ```

5. **Access**:
   - Open `http://localhost:5000` in your browser

## Files

- `app.py` - Flask application
- `weather_api.py` - API integration
- `weather_parser.py` - Data parsing
- `templates/index.html` - Frontend
- `static/style.css` - Styling
- `static/script.js` - Frontend logic

## API Endpoints

- `GET /` - Main dashboard
- `GET /api/weather/<city>` - Get current weather
- `GET /api/forecast/<city>` - Get 5-day forecast
- `POST /api/coordinates` - Get weather by coordinates
- `GET /api/air-quality/<city>` - Get air quality data
