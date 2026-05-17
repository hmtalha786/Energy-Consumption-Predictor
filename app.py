# ==============================
# IMPORT LIBRARIES
# ==============================

import streamlit as st
import requests

# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="Energy Consumption Predictor",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================
# CUSTOM CSS
# ==============================

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #111827 50%,
        #1e293b 100%
    );
    color: white;
}

/* Remove Streamlit Header */
header {
    visibility: hidden;
}

/* Main Container */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Glass Card Effect */
.glass-card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(12px);
    border-radius: 24px;
    padding: 30px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

/* Title */
.main-title {
    font-size: 48px;
    font-weight: 700;
    color: white;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    color: #cbd5e1;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Section Header */
.section-title {
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 20px;
    color: white;
}

/* Metric Card */
.metric-card {
    background: rgba(255,255,255,0.06);
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
}

/* Prediction Text */
.prediction-text {
    font-size: 36px;
    font-weight: bold;
    color: #22c55e;
    text-align: center;
}

/* Footer */
.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# HERO SECTION
# ==============================

st.markdown("""
<div class="glass-card">

<div class="main-title">
⚡ Energy Consumption Predictor
</div>

<div class="subtitle">
AI-powered energy consumption forecasting system using Machine Learning,
FastAPI, and Streamlit.
</div>

</div>
""", unsafe_allow_html=True)

st.write("")

# ==============================
# INPUT SECTION
# ==============================

st.markdown("""
<div class="section-title">
📥 Building Information
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    building_type = st.selectbox(
        "🏢 Building Type",
        ["Residential", "Commercial", "Industrial"]
    )

    square_footage = st.number_input(
        "📐 Square Footage",
        min_value=100,
        max_value=100000,
        value=1500
    )

    number_of_occupants = st.number_input(
        "👥 Number of Occupants",
        min_value=1,
        max_value=500,
        value=4
    )

with col2:

    appliances_used = st.number_input(
        "🔌 Appliances Used",
        min_value=1,
        max_value=100,
        value=8
    )

    average_temperature = st.number_input(
        "🌡️ Average Temperature (°C)",
        min_value=-10.0,
        max_value=50.0,
        value=28.0
    )

    day_of_week = st.selectbox(
        "📅 Day Type",
        ["Weekday", "Weekend"]
    )

st.write("")

# ==============================
# PREDICTION BUTTON
# ==============================

predict_button = st.button(
    "⚡ Predict Energy Consumption",
    use_container_width=True
)

# ==============================
# API REQUEST
# ==============================

if predict_button:

    data = {
        "Square_Footage": square_footage,
        "Number_of_Occupants": number_of_occupants,
        "Appliances_Used": appliances_used,
        "Average_Temperature": average_temperature,
        "Building_Type": building_type,
        "Day_of_Week": day_of_week
    }

    try:

        with st.spinner("Analyzing energy consumption patterns..."):

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json=data
            )

            result = response.json()

            prediction = result[
                "Predicted Energy Consumption"
            ]

        st.write("")

        # ==============================
        # RESULT CARD
        # ==============================

        st.markdown(f"""
        <div class="glass-card">

        <div style="text-align:center;">

        <h2 style="color:white;">
        ⚡ Predicted Energy Consumption
        </h2>

        <div class="prediction-text">
        {prediction} kWh
        </div>

        <br>

        <div style="color:#cbd5e1; font-size:16px;">
        Estimated energy usage based on the provided building information.
        </div>

        </div>

        </div>
        """, unsafe_allow_html=True)

    except Exception as e:

        st.error(f"API Connection Error: {e}")

# ==============================
# INFO SECTION
# ==============================

st.write("")
st.write("")

st.markdown("""
<div class="section-title">
📘 Feature Information
</div>
""", unsafe_allow_html=True)

info_col1, info_col2, info_col3 = st.columns(3)

with info_col1:

    st.markdown("""
    <div class="metric-card">
    <h3>🏢 Building Type</h3>
    <p>Residential, Commercial, or Industrial buildings.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="metric-card">
    <h3>👥 Occupants</h3>
    <p>Total number of people using the building.</p>
    </div>
    """, unsafe_allow_html=True)

with info_col2:

    st.markdown("""
    <div class="metric-card">
    <h3>📐 Square Footage</h3>
    <p>Total building area measured in square feet.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="metric-card">
    <h3>🌡️ Temperature</h3>
    <p>Average environmental temperature in Celsius.</p>
    </div>
    """, unsafe_allow_html=True)

with info_col3:

    st.markdown("""
    <div class="metric-card">
    <h3>🔌 Appliances</h3>
    <p>Electrical devices actively used in the building.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="metric-card">
    <h3>📅 Day Type</h3>
    <p>Weekday or Weekend energy usage pattern.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# FOOTER
# ==============================

st.markdown("""
<div class="footer">
<hr>
Built with FastAPI • Streamlit • Scikit-learn
</div>
""", unsafe_allow_html=True)
