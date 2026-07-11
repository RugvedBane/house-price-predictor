import streamlit as st
import requests

st.set_page_config(page_title="CA House Price Predictor", page_icon="🏠", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --bg: #0d0f14; --surface: #13161e; --border: #1e2330;
    --accent: #e8935a; --text: #e8e6e0; --muted: #6b7280;
}
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--bg) !important;
    color: var(--text) !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { max-width: 720px !important; padding: 2.5rem 2rem 4rem !important; }

.hero { text-align: center; padding: 2.5rem 0 2rem; border-bottom: 1px solid var(--border); margin-bottom: 2rem; }
.hero-tag { display: inline-block; font-size: 0.7rem; font-weight: 500; letter-spacing: 0.2em;
    text-transform: uppercase; color: var(--accent); background: rgba(232,147,90,0.1);
    border: 1px solid rgba(232,147,90,0.25); border-radius: 99px; padding: 0.3rem 0.9rem; margin-bottom: 1rem; }
.hero h1 { font-family: 'DM Serif Display', serif; font-size: clamp(2rem,5vw,2.8rem) !important;
    font-weight: 400; line-height: 1.15; letter-spacing: -0.02em; color: var(--text) !important; margin: 0 0 0.6rem !important; }
.hero h1 em { font-style: italic; color: var(--accent); }
.hero p { color: var(--muted); font-size: 0.9rem; margin: 0; }

.section-label { font-size: 0.68rem; font-weight: 500; letter-spacing: 0.18em; text-transform: uppercase;
    color: var(--muted); margin: 2rem 0 0.8rem; display: flex; align-items: center; gap: 0.6rem; }
.section-label::after { content: ''; flex: 1; height: 1px; background: var(--border); }

div[data-testid="stNumberInput"] input,
div[data-testid="stSelectbox"] > div > div {
    background: var(--surface) !important; border: 1px solid var(--border) !important;
    border-radius: 8px !important; color: var(--text) !important; }

label, .stSlider label { color: var(--text) !important; font-size: 0.82rem !important; }

div[data-testid="stButton"] > button {
    width: 100%; background: var(--accent) !important; color: #0d0f14 !important;
    border: none !important; border-radius: 10px !important; padding: 0.85rem 2rem !important;
    font-size: 0.95rem !important; font-weight: 500 !important; margin-top: 1.5rem !important;
    transition: opacity 0.2s, transform 0.1s !important; }
div[data-testid="stButton"] > button:hover { opacity: 0.88 !important; transform: translateY(-1px) !important; }

.result-card { margin-top: 1.8rem;
    background: linear-gradient(135deg, rgba(232,147,90,0.08), rgba(90,142,232,0.06));
    border: 1px solid rgba(232,147,90,0.25); border-radius: 14px; padding: 2rem;
    text-align: center; animation: fadeUp 0.4s ease; }
@keyframes fadeUp { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
.result-label { font-size: 0.72rem; font-weight: 500; letter-spacing: 0.18em;
    text-transform: uppercase; color: var(--muted); margin-bottom: 0.5rem; }
.result-price { font-family: 'DM Serif Display', serif; font-size: clamp(2.4rem,6vw,3.4rem);
    color: var(--accent); line-height: 1.1; letter-spacing: -0.02em; }
.result-sub { font-size: 0.8rem; color: var(--muted); margin-top: 0.5rem; }
</style>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero">
    <div class="hero-tag">California · ML Model</div>
    <h1>Predict <em>House Prices</em><br>in California</h1>
    <p>LightGBM model · R² score 0.86</p>
</div>
""", unsafe_allow_html=True)

# Location
st.markdown('<div class="section-label">📍 Location</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    latitude  = st.number_input("Latitude",  value=37.88)
with col2:
    longitude = st.number_input("Longitude", value=-122.23)
ocean = st.selectbox("Ocean Proximity", ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'])

# Housing Details
st.markdown('<div class="section-label">🏘️ Housing Details</div>', unsafe_allow_html=True)
col3, col4 = st.columns(2)
with col3:
    housing_median_age = st.slider("Median House Age (yrs)", 1, 52, 20)
    total_rooms        = st.number_input("Total Rooms",    value=2000)
with col4:
    total_bedrooms     = st.number_input("Total Bedrooms", value=400)
    households         = st.number_input("Households",     value=400)

# Demographics
st.markdown('<div class="section-label">👥 Demographics</div>', unsafe_allow_html=True)
col5, col6 = st.columns(2)
with col5:
    population    = st.number_input("Population", value=1000)
with col6:
    median_income = st.slider("Median Income (×$10k)", 0.5, 15.0, 3.0, step=0.1)

# Predict
if st.button("✦ Predict House Price"):
    payload = {
        'longitude':          longitude,
        'latitude':           latitude,
        'housing_median_age': housing_median_age,
        'total_rooms':        float(total_rooms),
        'total_bedrooms':     float(total_bedrooms),
        'population':         float(population),
        'households':         float(households),
        'median_income':      median_income,
        'ocean_proximity':    ocean
    }

    response = requests.post('http://127.0.0.1:8000/predict', json=payload)
    prediction = response.json()['prediction House Value']

    st.markdown(f"""
    <div class="result-card">
        <div class="result-label">Estimated Market Value</div>
        <div class="result-price">${prediction:,.0f}</div>
        <div class="result-sub">Based on {ocean} · {housing_median_age} yr old housing block</div>
    </div>
    """, unsafe_allow_html=True)