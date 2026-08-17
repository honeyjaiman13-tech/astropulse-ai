# 🌌 AstroPulse AI — Space Weather Operations Intelligence

**Challenge Theme:** Space Exploration  
**Live Deployed Application:** [AstroPulse AI Dashboard](https://astropulse-ai.streamlit.app)  

---

## 📌 Problem Statement
Solar flares and geomagnetic storms pose critical operational risks to modern infrastructure, causing radio blackouts, satellite orbit degradation, and ground power grid disturbances. Raw space weather telemetry from space agencies is often dense, fragmented, and difficult for non-specialist mission operators to rapidly interpret and act upon.

---

## 🚀 Solution Description
**AstroPulse AI** bridges the gap between raw scientific space data and mission operations. It continuously ingests real-time solar flare (FLR) and geomagnetic activity from NASA's Space Weather Database Of Notifications, Knowledge, Information (DONKI) API, analyzes activity levels, and translates raw telemetry into actionable, plain-language operational summaries and risk indices.

---

## 🧠 AI Approach & Architecture
1. **Data Ingestion:** Fetches real-time space weather feeds from the NASA DONKI REST API (`/DONKI/FLR`).
2. **Contextual Risk Assessment:** Evaluates solar flare classifications (C, M, X class) against orbital and ground threshold models.
3. **Natural-Language Insight Engine:** Transforms structured physical metrics into human-readable alerts, highlighting affected systems (LEO satellites, HF radio bands, aviation routes) and recommended mitigations.
4. **Operations Dashboard:** Built with a lightweight, high-performance UI providing real-time KPI metrics and raw telemetry inspection.

---

## 🛠️ How IBM Bob Was Used
IBM Bob served as the core development and architectural acceleration tool:
* **Scaffolding & Architecture:** Bob generated the baseline data contracts, ingestion pipelines, and interactive UI structure.
* **API Integration Logic:** Bob assisted in formulating the NASA DONKI telemetry parser and resilient fallback logic for continuous availability during API rate limits.
* **Operational Prompts & Logic:** Bob helped design the automated AI assessment logic mapping technical solar indices into operational risk tiers.

---

## 💻 Local Setup & Execution
1. Clone the repository:
   ```bash
   git clone [https://github.com/honeyjaiman13-tech/astropulse-ai.git](https://github.com/honeyjaiman13-tech/astropulse-ai.git)
   cd astropulse-ai
