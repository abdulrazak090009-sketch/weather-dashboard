async function searchWeather() {
    const city = document.getElementById('cityInput').value.trim();
    if (!city) return;
    
    try {
        const [weatherRes, forecastRes, airQualityRes] = await Promise.all([
            fetch(`/api/weather/${city}`),
            fetch(`/api/forecast/${city}`),
            fetch(`/api/air-quality/${city}`)
        ]);
        
        const weather = await weatherRes.json();
        const forecast = await forecastRes.json();
        const airQuality = await airQualityRes.json();
        
        if (weather.error) {
            showError('City not found');
            return;
        }
        
        displayWeather(weather);
        displayForecast(forecast);
        displayAirQuality(airQuality);
        hideError();
    } catch (error) {
        showError('Error fetching weather data');
        console.error(error);
    }
}

function displayWeather(weather) {
    if (!weather || weather.error) return;
    
    document.getElementById('cityName').textContent = `${weather.city}, ${weather.country}`;
    document.getElementById('weatherDescription').textContent = weather.description || weather.weather;
    document.getElementById('temperature').textContent = `${Math.round(weather.temperature)}°C`;
    document.getElementById('feelsLike').textContent = `${Math.round(weather.feels_like)}°C`;
    document.getElementById('humidity').textContent = `${weather.humidity}%`;
    document.getElementById('pressure').textContent = `${weather.pressure} hPa`;
    document.getElementById('windSpeed').textContent = `${weather.wind_speed} m/s`;
    document.getElementById('visibility').textContent = `${(weather.visibility / 1000).toFixed(1)} km`;
    
    const iconUrl = `https://openweathermap.org/img/wn/${weather.icon}@4x.png`;
    document.getElementById('weatherIcon').src = iconUrl;
    
    document.getElementById('currentWeather').style.display = 'block';
}

function displayForecast(forecast) {
    if (!forecast || forecast.length === 0) return;
    
    const forecastCards = document.getElementById('forecastCards');
    forecastCards.innerHTML = '';
    
    // Show every 8th item (24-hour intervals)
    for (let i = 0; i < forecast.length; i += 8) {
        const item = forecast[i];
        const date = new Date(item.datetime * 1000);
        
        const card = document.createElement('div');
        card.className = 'forecast-card';
        card.innerHTML = `
            <div class="date">${date.toLocaleDateString()}</div>
            <img src="https://openweathermap.org/img/wn/${item.icon}@2x.png" alt="Weather" />
            <div class="temp">${Math.round(item.temperature)}°C</div>
            <div class="desc">${item.description}</div>
        `;
        forecastCards.appendChild(card);
    }
    
    document.getElementById('forecast').style.display = 'block';
}

function displayAirQuality(airQuality) {
    if (!airQuality || airQuality.error) return;
    
    document.getElementById('aqi').textContent = airQuality.aqi || 'N/A';
    document.getElementById('pm25').textContent = `${airQuality.pm25?.toFixed(1) || 'N/A'} µg/m³`;
    document.getElementById('pm10').textContent = `${airQuality.pm10?.toFixed(1) || 'N/A'} µg/m³`;
    document.getElementById('o3').textContent = `${airQuality.o3?.toFixed(1) || 'N/A'} µg/m³`;
    
    document.getElementById('airQuality').style.display = 'block';
}

function getCurrentLocation() {
    if (!navigator.geolocation) {
        showError('Geolocation not supported');
        return;
    }
    
    navigator.geolocation.getCurrentPosition(
        async (position) => {
            const { latitude, longitude } = position.coords;
            
            try {
                const res = await fetch('/api/coordinates', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ lat: latitude, lon: longitude })
                });
                
                const data = await res.json();
                displayWeather(data.weather);
                displayAirQuality(data.air_quality);
                hideError();
            } catch (error) {
                showError('Error fetching location weather');
                console.error(error);
            }
        },
        (error) => {
            showError('Unable to get your location');
            console.error(error);
        }
    );
}

function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
}

function hideError() {
    document.getElementById('error').style.display = 'none';
}

// Allow Enter key to search
document.getElementById('cityInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') searchWeather();
});

// Load default city on page load
window.addEventListener('load', function() {
    document.getElementById('cityInput').value = 'London';
    searchWeather();
});