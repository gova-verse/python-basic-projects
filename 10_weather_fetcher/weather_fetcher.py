# weather_fetcher.py
# Concepts: API calls, requests library, JSON parsing, error handling, functions

import requests
import json
from datetime import datetime

API_KEY  = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather(city):
    # build request parameters
    params = {
        "q"     : city,
        "appid" : API_KEY,
        "units" : "metric"    # celsius
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data     = response.json()

        # check if city was found
        if response.status_code == 404:
            print(f"City '{city}' not found! Check spelling.")
            return None
        elif response.status_code == 401:
            print("Invalid API key! Check your API key.")
            return None
        elif response.status_code != 200:
            print(f"Error fetching weather. Status: {response.status_code}")
            return None

        return data

    except requests.exceptions.ConnectionError:
        print("No internet connection! Please check your network.")
        return None
    except requests.exceptions.Timeout:
        print("Request timed out! Try again.")
        return None

def get_forecast(city):
    params = {
        "q"     : city,
        "appid" : API_KEY,
        "units" : "metric",
        "cnt"   : 5           # next 5 time slots (every 3 hours)
    }
    try:
        response = requests.get(FORECAST_URL, params=params)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def display_weather(data):
    city        = data["name"]
    country     = data["sys"]["country"]
    temp        = data["main"]["temp"]
    feels_like  = data["main"]["feels_like"]
    humidity    = data["main"]["humidity"]
    pressure    = data["main"]["pressure"]
    description = data["weather"][0]["description"].title()
    wind_speed  = data["wind"]["speed"]
    visibility  = data.get("visibility", 0) // 1000

    # convert sunrise and sunset timestamps to readable time
    sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M")
    sunset  = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M")

    print("\n" + "=" * 45)
    print(f"   Weather in {city}, {country}")
    print("=" * 45)
    print(f"  Condition     : {description}")
    print(f"  Temperature   : {temp:.1f}°C")
    print(f"  Feels like    : {feels_like:.1f}°C")
    print(f"  Humidity      : {humidity}%")
    print(f"  Pressure      : {pressure} hPa")
    print(f"  Wind speed    : {wind_speed} m/s")
    print(f"  Visibility    : {visibility} km")
    print(f"  Sunrise       : {sunrise}")
    print(f"  Sunset        : {sunset}")
    print("=" * 45)

def display_forecast(data):
    if not data:
        return
    print("\n--- Next Few Hours Forecast ---")
    print(f"  {'TIME':<10} {'TEMP':<10} {'CONDITION'}")
    print("  " + "-" * 40)
    for item in data["list"]:
        time        = datetime.fromtimestamp(item["dt"]).strftime("%H:%M")
        temp        = item["main"]["temp"]
        description = item["weather"][0]["description"].title()
        print(f"  {time:<10} {temp:<10.1f} {description}")

def get_weather_tip(data):
    description = data["weather"][0]["main"].lower()
    temp        = data["main"]["temp"]
    humidity    = data["main"]["humidity"]

    print("\n--- Weather Tip ---")
    if "rain" in description:
        print("  Carry an umbrella today!")
    elif "snow" in description:
        print("  Wear warm clothes and drive carefully!")
    elif "clear" in description and temp > 30:
        print("  Stay hydrated — it is hot outside!")
    elif "clear" in description:
        print("  Great day to go outside!")
    elif "cloud" in description:
        print("  Mild weather — good for a walk!")
    elif "storm" in description:
        print("  Stay indoors — storm expected!")

    if humidity > 80:
        print("  High humidity — feels more uncomfortable!")

def show_menu():
    print("\n" + "=" * 45)
    print("          Weather Fetcher App")
    print("=" * 45)
    print("  1. Get current weather")
    print("  2. Get weather + forecast")
    print("  3. Get weather tip")
    print("  4. Exit")
    print("=" * 45)

def main():
    print("=" * 45)
    print("     Welcome to Weather Fetcher!")
    print("=" * 45)

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            city = input("\nEnter city name: ").strip()
            if not city:
                print("City name cannot be empty!")
                continue
            data = get_weather(city)
            if data:
                display_weather(data)

        elif choice == "2":
            city = input("\nEnter city name: ").strip()
            if not city:
                print("City name cannot be empty!")
                continue
            data     = get_weather(city)
            forecast = get_forecast(city)
            if data:
                display_weather(data)
                display_forecast(forecast)

        elif choice == "3":
            city = input("\nEnter city name: ").strip()
            if not city:
                print("City name cannot be empty!")
                continue
            data = get_weather(city)
            if data:
                display_weather(data)
                get_weather_tip(data)

        elif choice == "4":
            print("\nGoodbye! Stay weather aware!")
            break

        else:
            print("Invalid choice! Enter 1 to 4.")

if __name__ == "__main__":
    main()