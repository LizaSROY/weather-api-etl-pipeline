import requests
import pandas as pd
from datetime import datetime

API_KEY = "37a3ab2c4adf1cd3043a007db378a93b"
CITY = "Phnom Penh"

def extract_data():

    URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

    response = requests.get(URL)
    data = response.json()

    weather_data = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    df = pd.DataFrame([weather_data])

    df.to_csv(
        "/opt/airflow/data/raw/weather_raw.csv",
        index=False
    )

    print("Weather data extracted successfully.")