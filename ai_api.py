from fastapi import FastAPI
import random
import time

app = FastAPI()

# ---------------- SHIPMENT STATES ----------------
STATUSES = ["CREATED", "IN_TRANSIT", "DELAYED", "DELIVERED"]
WEATHER = ["clear", "rain", "storm"]
TRAFFIC = ["low", "medium", "high"]

# ---------------- SIMPLE STATE STORAGE ----------------
shipments_db = []

# ---------------- RISK ENGINE ----------------
def calculate_risk(weather, traffic):
    risk = 10
    if weather == "rain":
        risk += 20
    if weather == "storm":
        risk += 40
    if traffic == "medium":
        risk += 15
    if traffic == "high":
        risk += 35
    return min(risk, 100)

# ---------------- EVENT GENERATOR ----------------
def generate_shipment():
    shipment_id = f"SHP-{random.randint(1000,9999)}"

    weather = random.choice(WEATHER)
    traffic = random.choice(TRAFFIC)

    risk = calculate_risk(weather, traffic)

    status = random.choice(STATUSES)

    return {
        "shipment": {
            "shipment_id": shipment_id,
            "distance": random.randint(100, 2000),
            "weather": weather,
            "traffic": traffic,
            "shipment_type": random.choice(["standard", "express"])
        },
        "analysis": {
            "risk_score": risk,
            "status": status,
            "reason": "AI computed based on weather + traffic"
        },
        "timestamp": time.time()
    }

# ---------------- BASE ENDPOINT ----------------
@app.get("/")
def home():
    return {"status": "AI Logistics Backend Running"}

# ---------------- LIVE STREAM ----------------
@app.get("/stream")
def stream():
    global shipments_db

    # simulate continuous updates
    new_data = generate_shipment()
    shipments_db.append(new_data)

    # keep only latest 10
    shipments_db = shipments_db[-10:]

    return {
        "live_feed": shipments_db
    }

# ---------------- SINGLE SHIPMENT ----------------
@app.get("/live-shipment")
def live_shipment():
    return generate_shipment()
