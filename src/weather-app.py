import requests

location = "Sheffield"
url = "https://api.weatherapi.com/v1/forecast.json?key=e6948904e5034f53a67170821230110&q=" + location + "&days=7"

weather_request = requests.get(url)
weather_data = weather_request.json()

print(weather_data)
