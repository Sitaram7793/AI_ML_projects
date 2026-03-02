import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model and features
model = joblib.load("models/bike_demand_rf_model.pkl")
feature_cols = joblib.load("models/model_features.pkl")

st.title("🚲 Bike Demand Prediction App")

st.write("Enter environmental and time conditions to predict bike rental demand.")

# User Inputs
temp = st.slider("Temperature (°C)", 0.0, 45.0, 25.0)
humidity = st.slider("Humidity (%)", 0.0, 100.0, 50.0)
windspeed = st.slider("Windspeed", 0.0, 50.0, 10.0)
season = st.selectbox("Season", [1,2,3,4])
workingday = st.selectbox("Working Day", [0,1])
weather = st.selectbox("Weather Condition", [1,2,3,4])
hour = st.slider("Hour of Day", 0, 23, 12)

# Create input dataframe
input_dict = {
    'temp':[temp],
    'humidity':[humidity],
    'windspeed':[windspeed],
    'season':[season],
    'workingday':[workingday],
    'weather':[weather],
    'hour':[hour]
}

input_df = pd.DataFrame(input_dict)

# One-hot encode to match training
input_df = pd.get_dummies(input_df)

# Add missing columns
for col in feature_cols:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[feature_cols]

# Prediction
if st.button("Predict Bike Demand"):
    prediction = model.predict(input_df)[0]
    st.success(f"🚲 Predicted Bike Rentals: {int(prediction)}")
