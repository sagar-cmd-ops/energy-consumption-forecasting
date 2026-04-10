# ⚡ Energy Consumption Forecasting using Machine Learning

## 📌 Project Overview

This project focuses on predicting electricity consumption using historical energy usage data and time-based features.
The goal is to build an intelligent forecasting system that helps in optimizing energy distribution and reducing energy waste.

---

## 🎯 Problem Statement

Accurate prediction of energy consumption is essential for:

* Power companies → efficient energy distribution
* Smart cities → reducing energy waste
* Consumers → better energy management

This project implements a **time-series forecasting model** to predict hourly electricity usage.

---

## 📂 Dataset

Dataset used:
👉 Hourly Energy Consumption Dataset (Kaggle)

* Multiple regional datasets provided
* Used dataset: **PJME_hourly.csv**
* Features include:

  * Datetime
  * Energy consumption (MW)

---

## ⚙️ Feature Engineering

Extracted important time-based features:

* Hour of day
* Day of week
* Month
* Weekend indicator

Created advanced features:

* Lag features (previous hour, previous day)
* Rolling mean (24-hour average)

---

## 🤖 Model Used

* Random Forest Regressor
* Optimized for performance and size

---

## 📊 Model Performance

| Metric   | Value  |
| -------- | ------ |
| RMSE     | 788.41 |
| R² Score | 0.985  |

✔ Achieved high accuracy
✔ Meets project requirement (R² > 0.80)

---

## 📈 Visualization

* Actual vs Predicted consumption graph
* Time-series trend analysis
* Peak usage pattern identification

---

## 🌐 Streamlit Application

An interactive web app was developed using Streamlit.

### User Inputs:

* Hour
* Day
* Month
* Weekend indicator
* Previous consumption values

### Output:

* Predicted energy consumption
* Usage insights (High / Normal)

---

## 💡 Key Insights

* Peak consumption occurs during evening hours
* Weekends show different usage patterns
* Energy demand follows daily cycles

---

## 🚀 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Streamlit

---

## 📁 Project Structure

```
energy-consumption-forecasting/
│
├── app.py
├── model.pkl
├── requirements.txt
├── notebook.ipynb
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Clone Repository

```
git clone https://github.com/your-username/energy-consumption-forecasting.git
cd energy-consumption-forecasting
```

### 2. Install Requirements

```
pip install -r requirements.txt
```

### 3. Run Streamlit App

```
streamlit run app.py
```

---

## 🔥 Future Improvements

* Implement LSTM (deep learning model)
* Multi-step forecasting (24h / 7 days)
* Anomaly detection (energy spikes)
* Real-time data integration

---

## 📌 Conclusion

This project successfully demonstrates how machine learning can be used for accurate energy forecasting.
The model provides high accuracy while remaining efficient for deployment.

---

## 🙌 Acknowledgement

Dataset sourced from Kaggle.
Project developed as part of a Machine Learning Hackathon.

---
