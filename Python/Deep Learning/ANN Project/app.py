import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler,LabelEncoder,OneHotEncoder
import time
import tensorflow as tf
import pickle

### Load the trained model
model = tf.keras.models.load_model('model.h5')

## load the scaler and label encoder
with open('label_encoder_gender.pkl', 'rb') as file:
    label_encoder = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('one_hot_encoder_geography.pkl', 'rb') as file:
    one_hot_encoder = pickle.load(file)

### Streamlit
st.title('Customer Churn Prediction')

## User input
geography = st.selectbox('Geography', one_hot_encoder.categories_[0])
gender = st.selectbox('Gender', label_encoder.classes_)
age = st.slider('Age', 18, 92)
balance = st.number_input('Balance')
credit_score = st.slider('Credit Score', 300, 850)
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1, 4)
has_credit_card = st.selectbox('Has Credit Card', [0,1])
is_active_member = st.selectbox('Is Active Member', [0,1])

## Prepare the input for prediction
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Geography': [geography],
    'Gender': [gender],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_credit_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

### Encode the gender using the label encoder
input_data['Gender'] = label_encoder.transform(input_data['Gender'])

### One-hot encode the geography
geography_encoded = one_hot_encoder.transform(input_data[['Geography']]).toarray()
geography_encoded_df = pd.DataFrame(geography_encoded, columns=one_hot_encoder.get_feature_names_out(['Geography']))

# Drop Geography from input_data and combine with one-hot encoded geography
input_data = input_data.drop('Geography', axis=1)
input_data = pd.concat([input_data, geography_encoded_df], axis=1)

## Scale the input data
scaled_input = scaler.transform(input_data)

## Predict the probability of churn
prediction = model.predict(scaled_input)
prediction_probability = prediction[0][0]

st.write(f"Predicted probability of churn: {prediction_probability:.2f}")

if prediction_probability > 0.5:
    st.write("The customer is likely to churn.")
else:
    st.write("The customer is not likely to churn.")