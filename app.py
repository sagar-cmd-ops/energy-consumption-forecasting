import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.set_page_config(page_title="Energy Forecast", layout="centered")

st.title("⚡ Energy Consumption Forecasting")
st.write("Predict electricity usage based on time and past consumption")

# Inputs
hour = st.slider("Hour of Day", 0, 23)
day = st.slider("Day of Week (0=Mon)", 0, 6)
month = st.slider("Month", 1, 12)
is_weekend = st.selectbox("Is Weekend?", [0, 1])

lag_1 = st.number_input("Previous Hour Consumption")
lag_24 = st.number_input("Same Hour Yesterday Consumption")
rolling_mean = st.number_input("24hr Average Consumption")

# Prediction
if st.button("Predict"):
    features = np.array([[hour, day, month, is_weekend, lag_1, lag_24, rolling_mean]])
    prediction = model.predict(features)

    st.success(f"⚡ Predicted Consumption: {prediction[0]:.2f} MW")

    # Insight
    if prediction[0] > 50000:
        st.warning("High energy usage expected ⚠️")
    else:
        st.info("Normal usage level ✅")
