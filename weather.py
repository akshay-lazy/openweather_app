
import requests
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather():

    if not API_KEY:
        print("API key not found. Check your .env file.")
        return

    city = input("Enter city name: ").strip()

    if not city:
        print("Please enter a city name.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        # Extract weather information
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        # Display results
        print("\n===== WEATHER REPORT =====")
        print("City:", city_name)
        print("Country:", country)
        print("Temperature:", temperature, "°C")
        print("Feels Like:", feels_like, "°C")
        print("Humidity:", humidity, "%")
        print("Weather:", weather)
        print("Wind Speed:", wind_speed, "m/s")

    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print("City not found.")
        elif response.status_code == 401:
            print("Invalid or inactive API key.")
        else:
            print("HTTP error:", e)

    except requests.exceptions.RequestException as e:
        print("Connection error:", e)

    except (KeyError, IndexError, ValueError) as e:
        print("Unable to process weather data:", e)


# Main program
while True:

    print("\n===== WEATHER APPLICATION =====")
    print("1. Check Weather")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        get_weather()

    elif choice == "2":
        print("Thank you for using Weather App!")
        break

    else:
        print("Invalid choice. Try again.")
