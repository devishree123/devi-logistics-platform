import requests

API_KEY = "8e84f17e239f60fe0c63e307c039c1e9"
CITY = "Chennai"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

data = requests.get(url).json()

print("RAW RESPONSE:", data)

if data.get("cod") != 200:
    print("ERROR:", data.get("message"))
else:
    print("Weather:", data["weather"][0]["main"])
    print("Temperature:", data["main"]["temp"])
