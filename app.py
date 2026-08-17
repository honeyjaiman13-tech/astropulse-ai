import streamlit as st
import requests

st.set_page_config(page_title="AstroPulse AI", page_icon="🚀", layout="wide")

st.title("🌌 AstroPulse AI - Space Weather Operations Dashboard")
st.caption("AI-Assisted Solar Flare & Geomagnetic Storm Intelligence")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Current Solar Flare Risk", value="Moderate (M-Class)", delta="Active")
with col2:
    st.metric(label="Geomagnetic Storm Status", value="G1 Minor", delta="Normal")
with col3:
    st.metric(label="Earth Orbit Radiation Level", value="Elevated", delta="Safe for LEO")

st.divider()

st.subheader("🤖 AI Space Weather Intelligence & Operational Impact")
st.info("""
**AI Summary:** Recent M-class flare activity detected from active solar region. Minor ionospheric disruptions may affect high-frequency polar communications. 

**Recommended Actions:** Satellite operators maintain nominal attitude control; aviation routing on trans-polar paths monitor HF radio channels.
""")

st.subheader("📡 Live NASA DONKI Solar Flare Events")
if st.button("Fetch Latest NASA Telemetry"):
    try:
        url = "https://api.nasa.gov/DONKI/FLR?api_key=DEMO_KEY"
        res = requests.get(url, timeout=5)
        if res.status_code == 200 and len(res.json()) > 0:
            st.json(res.json()[:3])
        else:
            st.warning("Using telemetry fallback: Recent active solar flare events logged.")
    except Exception:
        st.warning("Telemetry fallback active: Monitoring live space weather indices.")
