import streamlit as st
import numpy as np
import os
import pickle

# ===============================
# Load model safely
# ===============================
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')

try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# ===============================
# Page Config
# ===============================
st.set_page_config(page_title="Energy Forecast", layout="centered")

# ===============================
# Title & Description
# ===============================
st.title("⚡ Energy Consumption Forecasting")
st.write("Predict electricity usage based on time and past consumption")

# ===============================
# User Inputs
# ===============================
st.subheader("Enter Input Values")

hour = st.slider("Hour of Day", 0, 23)
day = st.slider("Day of Week (0 = Monday)", 0, 6)
month = st.slider("Month", 1, 12)
is_weekend = st.selectbox("Is Weekend?", [0, 1])

lag_1 = st.number_input("Previous Hour Consumption (MW)", min_value=0.0)
lag_24 = st.number_input("Same Hour Yesterday Consumption (MW)", min_value=0.0)
rolling_mean = st.number_input("24hr Average Consumption (MW)", min_value=0.0)

# ===============================
# Prediction
# ===============================
if st.button("Predict"):
    try:
        features = np.array([[hour, day, month, is_weekend, lag_1, lag_24, rolling_mean]])
        prediction = model.predict(features)
        value = prediction[0]

        st.success(f"⚡ Predicted Consumption: {value:.2f} MW")

        # Insights
        st.subheader("💡 Insight")
        if value > 50000:
            st.warning("High energy usage expected ⚠️ Try reducing usage during peak hours.")
        elif value > 30000:
            st.info("Moderate energy usage 📊")
        else:
            st.success("Low energy usage ✅ Efficient consumption")

    except Exception as e:
        st.error(f"Prediction Error: {e}")

# ===============================
# Footer
# ===============================
st.markdown("---")
st.markdown("Built with ❤️ using Machine Learning & Streamlit")
