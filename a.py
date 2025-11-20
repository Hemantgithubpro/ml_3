import streamlit as st
import joblib
import numpy as np

# --- Configuration and Loading ---
st.set_page_config(page_title="Housing Predictor", layout="centered")

# Load the pipeline object (contains scaler and model)
try:
    pipeline = joblib.load("pipeline.pkl")
except FileNotFoundError:
    st.error("Pipeline file not found. Please ensure 'pipeline.pkl' is in the same directory.")
    st.stop() 

# --- Streamlit UI ---
st.title("California Housing Price Predictor 🏠")
st.markdown("Enter the following **8 features** to predict the Median House Value (in $100,000s):")

# Input Fields for 8 Features
# These must be in the exact order the model expects: 
# MedInc, HouseAge, AveDesks, AveOccup, AveRooms, AveBedrms, Latitude, Longitude

col1, col2, col3, col4 = st.columns(4)

with col1:
    MedInc = st.number_input("**Median Income (MedInc)**", min_value=0.0, value=3.87, format="%.4f", help="Median income in block group, in $10,000s")
    AveRooms = st.number_input("**Average Rooms (AveRooms)**", min_value=0.0, value=5.43, format="%.4f")

with col2:
    HouseAge = st.number_input("**House Age (HouseAge)**", min_value=1, value=28, step=1, help="Median house age in block group")
    AveBedrms = st.number_input("**Average Bedrooms (AveBedrms)**", min_value=0.0, value=1.10, format="%.4f")

with col3:
    AveDesks = st.number_input("**Average Dwellings (AveDesks)**", min_value=0.0, value=2.50, format="%.4f")
    Latitude = st.number_input("**Latitude**", min_value=30.0, max_value=45.0, value=34.0, format="%.4f")

with col4:
    AveOccup = st.number_input("**Average Occupancy (AveOccup)**", min_value=0.0, value=3.00, format="%.4f")
    Longitude = st.number_input("**Longitude**", min_value=-130.0, max_value=-110.0, value=-118.0, format="%.4f")

st.markdown("---")

# --- Prediction Logic ---
if st.button("**Predict Median House Value**", use_container_width=True):
    # 1. Gather all inputs into a single 2D NumPy array in the correct feature order
    user_data = np.array([
        [MedInc, HouseAge, AveDesks, AveOccup, AveRooms, AveBedrms, Latitude, Longitude]
    ])
    
    # 2. Make the prediction using the pipeline (it scales internally)
    prediction = pipeline.predict(user_data)
    
    # 3. Display the result
    st.success("### Prediction Result")
    # The output is in $100,000s, so we multiply by 100,000 for display
    st.markdown(f"The **Predicted Median House Value** is:")
    st.markdown(f"## **${prediction[0] * 100000:.2f}**")