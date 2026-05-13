import requests
import random

API_KEY = "8e84f17e239f60fe0c63e307c039c1e9"
CITY = "Chennai"

# -----------------------------
# 1. GET WEATHER DATA
# -----------------------------
url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

weather_data = requests.get(url).json()

print("\n--- RAW WEATHER DATA ---")
print(weather_data)

if weather_data.get("cod") != 200:
    print("Weather API Error:", weather_data.get("message"))
    exit()

weather = weather_data["weather"][0]["main"]
temp = weather_data["main"]["temp"]
humidity = weather_data["main"]["humidity"]

# -----------------------------
# 2. SIMPLE LOGISTICS SIMULATION
# -----------------------------
flight_id = "UPS101"
parcel_load = random.choice(["LOW", "MEDIUM", "HIGH"])

# -----------------------------
# 3. DELAY RISK ENGINE
# -----------------------------
delay_risk = "LOW"

if weather in ["Rain", "Thunderstorm", "Drizzle"]:
    delay_risk = "HIGH"
elif humidity > 80:
    delay_risk = "MEDIUM"
elif parcel_load == "HIGH":
    delay_risk = "MEDIUM"

# -----------------------------
# 4. OUTPUT
# -----------------------------
print("\n--- LOGISTICS OUTPUT ---")
print("Flight ID:", flight_id)
print("Weather:", weather)
print("Temperature:", temp)
print("Humidity:", humidity)
print("Parcel Load:", parcel_load)
print("Delay Risk:", delay_risk)
