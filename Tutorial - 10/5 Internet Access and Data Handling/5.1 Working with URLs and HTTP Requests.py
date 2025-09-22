# The urllib module provides tools for working with URLs and making HTTP requests, which is fundamental for web applications that need to communicate with other services or APIs.

from urllib.request import urlopen
import json

# Fetch data from a web API
def fetch_api_data(url):
    with urlopen(url) as response:
        data = response.read().decode()
        return json.loads(data)

# Example: Get current weather information
try:
    weather_data = fetch_api_data('http://api.weatherapi.com/v1/current.json?key=XXX&q=London')
    print(f"Temperature: {weather_data['current']['temp_c']}°C")
except Exception as e:
    print(f"Error fetching weather data: {e}")

# Download and save an image (e.g., for user avatars)
def download_file(url, save_path):
    with urlopen(url) as response:
        with open(save_path, 'wb') as f:
            f.write(response.read())

# Example usage
# download_file('https://example.com/avatar.jpg', 'user_avatar.jpg')