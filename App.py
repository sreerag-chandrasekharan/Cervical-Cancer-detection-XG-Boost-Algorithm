import streamlit as st
import numpy as np
import pickle
import xgboost as xgb

# Load trained XGBoost model
model = pickle.load(open("xgb_model.pkl", "rb"))  # Ensure this file exists

st.title("Cervical Cancer Risk Prediction (Biopsy)")

st.write("Enter the following medical information to predict biopsy result:")

# Input fields for user
age = st.number_input("Age", min_value=0, max_value=100, value=25)
partners = st.number_input("Number of sexual partners", min_value=0, value=1)
first_sex = st.number_input("Age at first sexual intercourse", min_value=0, max_value=100, value=17)
pregnancies = st.number_input("Number of pregnancies", min_value=0, value=1)

if st.button("Predict"):
    # Format input as 2D array for prediction
    input_data = np.array([[age, partners, first_sex, pregnancies]])

    # Make prediction
    prediction = model.predict(input_data)

    # Display result
    if prediction == 1:
        st.error("⚠️ High Risk: Positive Biopsy likely.")
    else:
        st.success("✅ Low Risk: Negative Biopsy likely.")
