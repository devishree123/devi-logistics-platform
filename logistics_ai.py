import os
import requests
import json

API_KEY = os.getenv("GEMINI_API_KEY")

def ask_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

    payload = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }]
    }

    response = requests.post(url, json=payload)
    data = response.json()

    return data["candidates"][0]["content"]["parts"][0]["text"]

# Test use-case for logistics
result = ask_gemini(
    "You are a logistics AI. Explain why parcels get delayed during heavy rain and traffic, and suggest solutions."
)

print("\n--- AI RESPONSE ---\n")
print(result)
