import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("traffic_model.pkl")

st.title("🚦 Smart Traffic Prediction & Optimization")

st.write("Enter current traffic conditions:")

# Inputs
avg_density = st.slider("Current Avg Density", 0.0, 1.0, 0.3)
prev_density = st.slider("Previous Density", 0.0, 1.0, 0.3)
prev2_density = st.slider("Previous 2-Step Density", 0.0, 1.0, 0.3)
rolling_mean = st.slider("Rolling Mean (3)", 0.0, 1.0, 0.3)
rolling_mean_5 = st.slider("Rolling Mean (5)", 0.0, 1.0, 0.3)

hour = st.slider("Hour of Day", 0, 23, 10)
day = st.slider("Day of Week (0=Mon)", 0, 6, 2)

# Predict
if st.button("Predict Traffic"):

    input_data = np.array([[avg_density, prev_density, prev2_density,
                            rolling_mean, rolling_mean_5, hour, day]])

    prediction = model.predict(input_data)

    st.subheader(f"Predicted Traffic Density: {round(prediction[0], 4)}")

# Optimization
st.subheader("🚦 Signal Optimization")

d1 = st.slider("Road 1 Density", 0, 200, 50)
d2 = st.slider("Road 2 Density", 0, 200, 100)
d3 = st.slider("Road 3 Density", 0, 200, 30)
d4 = st.slider("Road 4 Density", 0, 200, 20)

def allocate_signal(densities, total_time=120):
    total_density = sum(densities)
    return [(d / total_density) * total_time for d in densities]

if st.button("Optimize Signal"):

    densities = [d1, d2, d3, d4]
    result = allocate_signal(densities)

    for i, t in enumerate(result):
        st.write(f"Road {i+1}: {round(t,2)} sec")