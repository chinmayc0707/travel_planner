import os
def get_weather_data(CITY):
    """Fetches current weather data for a specified city using OpenWeatherMap API.
    Returns:
        str: Current temperature in Celsius.
    """
    import requests

    # Replace with your API key and city
    API_KEY = os.environ['OPENWEATHER_API_KEY']
    

    # API request URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    # Send request
    response = requests.get(url)

    # Check response status
    if response.status_code == 200:
        data = response.json()
        temp_celsius = data['main']['temp']
        return str(temp_celsius)
    

