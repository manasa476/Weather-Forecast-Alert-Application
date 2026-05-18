import requests
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

HIGH_TEMP = 35
HIGH_HUMIDITY = 80


def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


def analyze_weather(data):

    forecast_list = data["list"]

    records = []
    alerts = []

    for item in forecast_list[:8]:

        date = item["dt_txt"]
        temp = item["main"]["temp"]
        humidity = item["main"]["humidity"]
        weather = item["weather"][0]["main"]
        rain = item.get("rain", {}).get("3h", 0)

        records.append({
            "DateTime": date,
            "Temperature": temp,
            "Humidity": humidity,
            "Weather": weather,
            "Rain": rain
        })

        if temp >= HIGH_TEMP:
            alerts.append(f"High Temperature Alert at {date}")

        if humidity >= HIGH_HUMIDITY:
            alerts.append(f"High Humidity Alert at {date}")

        if rain > 0:
            alerts.append(f"Rain Alert at {date}")

    return records, alerts


def save_report(records, city):

    df = pd.DataFrame(records)

    filename = f"reports/{city}_weather_report.csv"

    df.to_csv(filename, index=False)

    return df


def generate_chart(df, city):

    plt.figure(figsize=(10, 5))

    plt.plot(df["DateTime"], df["Temperature"], marker="o")

    plt.xticks(rotation=45)

    plt.title(f"Temperature Forecast for {city}")

    plt.xlabel("Date")

    plt.ylabel("Temperature °C")

    plt.tight_layout()

    image_path = f"images/{city}_chart.png"

    plt.savefig(image_path)

    print("Chart Saved:", image_path)


def main():

    city = input("Enter City Name: ")

    data = fetch_weather(city)

    if not data:
        return

    records, alerts = analyze_weather(data)

    print("\n===== WEATHER FORECAST =====\n")

    for r in records:

        print(f"Time: {r['DateTime']}")
        print(f"Temperature: {r['Temperature']}°C")
        print(f"Humidity: {r['Humidity']}%")
        print(f"Weather: {r['Weather']}")
        print(f"Rain: {r['Rain']} mm")
        print("----------------------------")

    print("\n===== ALERTS =====\n")

    if alerts:
        for alert in alerts:
            print(alert)
    else:
        print("No Alerts")

    df = save_report(records, city)

    generate_chart(df, city)


if __name__ == "__main__":
    main()