import streamlit as st
import pickle
import numpy as np
import os

# Load model safely
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')

try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except:
    st.error("❌ Model file not found! Make sure 'model.pkl' is in the repo.")
    st.stop()

# Page config
st.set_page_config(page_title="Energy Forecast", layout="centered")

# Title
st.title("⚡ Energy Consumption Forecasting")
st.write("Predict electricity usage based on time and past consumption")

# Inputs
hour = st.slider("Hour of Day", 0, 23)
day = st.slider("Day of Week (0=Mon)", 0, 6)
month = st.slider("Month", 1, 12)
is_weekend = st.selectbox("Is Weekend?", [0, 1])

lag_1 = st.number_input("Previous Hour Consumption", min_value=0.0)
lag_24 = st.number_input("Same Hour Yesterday Consumption", min_value=0.0)
rolling_mean = st.number_input("24hr Average Consumption", min_value=0.0)

# Prediction
if st.button("Predict"):
    features = np.array([[hour, day, month, is_weekend, lag_1, lag_24, rolling_mean]])

    try:
        prediction = model.predict(features)
        value = prediction[0]

        st.success(f"⚡ Predicted Consumption: {value:.2f} MW")

        # Insight
        if value > 50000:
            st.warning("High energy usage expected ⚠️ Try reducing load during peak hours.")
        else:
            st.info("Normal usage level ✅")

    except Exception as e:
        st.error(f"Prediction error: {e}")
