import streamlit as st
import joblib
import pandas as pd
from advisor import generate_advice

# Load model
model = joblib.load("models/sleep_quality_model.joblib")

# Streamlit page setup
st.set_page_config(page_title="Sleep Quality Predictor & Advisor", layout="centered")
st.title("😴 Sleep Quality Predictor & Advisor")

st.header("Enter your lifestyle data")

# Input form
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=10, max_value=100, value=22)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    sleep_hours = st.slider("Average sleep hours/night", 0.0, 12.0, 7.0, 0.25)
    screen_time = st.slider("Evening screen time (hours before bed)", 0.0, 12.0, 1.5, 0.25)
    exercise_mins = st.number_input("Exercise minutes/day", min_value=0, max_value=300, value=20)

with col2:
    caffeine_cups = st.number_input("Cups of caffeine/day (tea/coffee)", min_value=0, max_value=10, value=1)
    stress_level = st.selectbox("Stress level", ["Low", "Medium", "High"])
    bedtime_variability_mins = st.number_input("Bedtime variability (mins)", min_value=0, max_value=300, value=30)
    has_sleep_disorder = st.selectbox("Known sleep disorder?", ["No", "Yes"])

# Create input dict
input_dict = {
    "age": age,
    "gender": gender,
    "sleep_hours": sleep_hours,
    "screen_time": screen_time,
    "exercise_mins": exercise_mins,
    "caffeine_cups": caffeine_cups,
    "stress_level": stress_level,
    "bedtime_variability_mins": bedtime_variability_mins,
    "has_sleep_disorder": 1 if has_sleep_disorder == "Yes" else 0,
    "steps": 6500  # default assumption
}

# Predict button
if st.button("Predict Sleep Quality"):
    df = pd.DataFrame([input_dict])
    pred = model.predict(df)[0]
    
    st.subheader(f"Predicted Sleep Quality: **{pred.upper()}**")
    advice = generate_advice(df.iloc[0])
    
    st.markdown("### 💡 Personalized Suggestions:")
    for a in advice:
        st.write("- " + a)

st.markdown("---")
st.caption("⚠️ Demo app using synthetic data. Retrain with real-world sleep/lifestyle data for production use.")
