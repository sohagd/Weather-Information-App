import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print("\n===== WEATHER INFORMATION =====")
    print(f"City: {data['name']}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition.title()}")

else:
    print("\nUnable to find weather information.")
