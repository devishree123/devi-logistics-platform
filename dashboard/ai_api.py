from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import time

app = FastAPI()

# ---------------- CORS CONFIGURATION ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- ROOT ----------------
@app.get("/")
def home():
    return {
        "status": "AI Logistics Backend Running"
    }

# ---------------- SHIPMENT GENERATOR ----------------
def create_shipment():
    return {
        "shipment_id": f"SHP-{random.randint(1000, 9999)}",
        "distance": random.randint(50, 2000),
        "weather": random.choice(["clear", "rain", "storm"]),
        "traffic": random.choice(["low", "medium", "high"]),
        "shipment_type": random.choice(["express", "standard"])
    }

# ---------------- AI RISK ENGINE ----------------
def risk_engine(shipment):

    score = 0

    # Weather impact
    if shipment["weather"] == "rain":
        score += 20

    elif shipment["weather"] == "storm":
        score += 40

    # Traffic impact
    if shipment["traffic"] == "medium":
        score += 15

    elif shipment["traffic"] == "high":
        score += 30

    # Distance impact
    score += shipment["distance"] // 50

    status = "ON TIME"
    reason = "Normal conditions"

    if score > 60:
        status = "DELAYED"
        reason = "Traffic + weather impact"

    if score > 85:
        status = "HIGH RISK"
        reason = "Severe disruption detected"

    return {
        "risk_score": score,
        "status": status,
        "reason": reason
    }

# ---------------- LIVE STREAM DATABASE ----------------
live_db = []

# ---------------- LIVE STREAM ENDPOINT ----------------
@app.get("/stream")
def stream():

    global live_db

    shipment = create_shipment()

    analysis = risk_engine(shipment)

    event = {
        "shipment": shipment,
        "analysis": analysis,
        "timestamp": time.time()
    }

    live_db.append(event)

    # Keep only latest 10 events
    live_db = live_db[-10:]

    return {
        "live_feed": live_db
    }