import requests
import random

# -----------------------------
# WEATHER API
# -----------------------------
API_KEY = "8e84f17e239f60fe0c63e307c039c1e9"
CITY = "Chennai"

weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
weather_data = requests.get(weather_url).json()

# -----------------------------
# MOCK FLIGHT API
# -----------------------------
def get_flight_data():
    return {
        "flight_id": "UPS101",
        "status": random.choice(["ON_TIME", "DELAYED", "BOARDING"]),
        "route": "Chennai → Bangalore"
    }

# -----------------------------
# MOCK TRAFFIC API
# -----------------------------
def get_traffic_data():
    return {
        "traffic_level": random.choice(["LOW", "MEDIUM", "HIGH"]),
        "road_condition": random.choice(["CLEAR", "HEAVY", "BLOCKED"])
    }

# -----------------------------
# EXTRACT WEATHER
# -----------------------------
if weather_data.get("cod") != 200:
    print("Weather API error:", weather_data.get("message"))
    exit()

weather = weather_data["weather"][0]["main"]
temp = weather_data["main"]["temp"]

flight = get_flight_data()
traffic = get_traffic_data()

# -----------------------------
# FINAL LOGISTICS INTELLIGENCE
# -----------------------------
print("\n--- MULTI SOURCE INTELLIGENCE ---")

print("Flight:", flight)
print("Traffic:", traffic)
print("Weather:", weather)
print("Temperature:", temp)
