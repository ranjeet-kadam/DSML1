import streamlit as st
import numpy as np
import pandas as pd
import pickle
from tensorflow.keras.models import load_model

# Load saved files
model = load_model('regression_model.h5')

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('labelencoder.pkl', 'rb') as f:
    labelencoder = pickle.load(f)

with open('onehotencoder.pkl', 'rb') as f:
    onehotencoder = pickle.load(f)

# Title
st.title("💰 Salary Prediction App (ANN Model)")

st.write("Enter customer details to estimate salary")

# User Inputs
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=600)
age = st.number_input("Age", min_value=18, max_value=100, value=30)
tenure = st.number_input("Tenure", min_value=0, max_value=10, value=3)
balance = st.number_input("Balance", value=50000.0)
num_of_products = st.number_input("Number of Products", min_value=1, max_value=4, value=1)
has_cr_card = st.selectbox("Has Credit Card", [0, 1])
is_active_member = st.selectbox("Is Active Member", [0, 1])
gender = st.selectbox("Gender", ["Male", "Female"])
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])

# Encode Gender
gender_encoded = labelencoder.transform([gender])[0]

# One-hot encode Geography
geo_encoded = onehotencoder.transform([[geography]]).toarray()

exited = 0  # dummy value


# Prepare input array
input_data = np.array([[credit_score, gender_encoded, age, tenure,
                        balance, num_of_products,
                        has_cr_card, is_active_member,exited]])

# Combine with geography
input_data = np.concatenate([input_data, geo_encoded], axis=1)

# Scale input
input_data_scaled = scaler.transform(input_data)

# Prediction
if st.button("Predict Salary"):
    prediction = model.predict(input_data_scaled)
    st.success(f"Estimated Salary: ₹ {prediction[0][0]:,.2f}")