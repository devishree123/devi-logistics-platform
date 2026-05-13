import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/stream"

st.set_page_config(page_title="AI Logistics Control Tower", layout="wide")

st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #0b0b12, #000000);
    color: white;
}

.title {
    font-size: 40px;
    font-weight: 800;
    color: #ff2e93;
    text-align: center;
    text-shadow: 0 0 20px #ff2e93;
}

.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 16px;
    border: 1px solid rgba(255,46,147,0.3);
    box-shadow: 0 0 25px rgba(255,46,147,0.2);
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.03);
    box-shadow: 0 0 40px rgba(255,46,147,0.6);
}

.label {
    color: #ffd700;
    font-weight: bold;
}

.status-on-time {
    color: #00ff9d;
    font-weight: bold;
}

.status-delayed {
    color: #ff3b3b;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🚚 AI Logistics Control Tower</div>", unsafe_allow_html=True)

try:
    res = requests.get(API_URL, timeout=5)
    data = res.json()["live_feed"][-1]
    
    shipment = data["shipment"]
    analysis = data["analysis"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="card">
        <h3>📦 Shipment ID</h3>
        <h2>{shipment['shipment_id']}</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
        <h3>📍 Distance</h3>
        <h2>{shipment['distance']} km</h2>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        status_class = "status-on-time" if analysis["status"] == "ON TIME" else "status-delayed"
        st.markdown(f"""
        <div class="card">
        <h3>⚡ Status</h3>
        <h2 class="{status_class}">{analysis['status']}</h2>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🔥 Risk Analysis")
    st.progress(analysis["risk_score"] / 100)
    st.write(f"Risk Score: {analysis['risk_score']}")

except Exception as e:
    st.error("❌ Backend not reachable or stream error")
    st.write(str(e))
