import requests
import pandas as pd

api_key = "9b9e5b9bb03bd7c581598dd19a5b727d"

cities = ["Abuja", "Lagos", "Port Harcourt"]

weather_records = []

for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        weather_data = {
            "City": data["name"],
            "Temperature_C": data["main"]["temp"],
            "Humidity_%": data["main"]["humidity"],
            "Weather_Condition": data["weather"][0]["main"],
            "Wind_Speed_mps": data["wind"]["speed"],
            "Date_Time": pd.to_datetime(data["dt"], unit="s")
        }

        weather_records.append(weather_data)

    else:
        print(f"Could not retrieve data for {city}")

print(weather_records)

df = pd.DataFrame(weather_records)

print(df)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

df.to_csv("weather_data.csv", index=False)

print("Weather data successfully saved to weather_data.csv")

loaded_df = pd.read_csv("weather_data.csv")

print("\nLoaded Dataset:")
print(loaded_df)

print("\n--- BASIC WEATHER ANALYSIS ---")

# 1. Compare temperatures across cities
print("\nTemperature Comparison:")
print(df[["City", "Temperature_C"]].sort_values("Temperature_C", ascending=False))

# 2. Identify the city with the highest humidity
highest_humidity = df.loc[df["Humidity_%"].idxmax()]

print("\nHighest Humidity:")
print(f"{highest_humidity['City']} has the highest humidity at {highest_humidity['Humidity_%']}%.")

# 3. Compare weather conditions
print("\nWeather Conditions:")
print(df[["City", "Weather_Condition"]])