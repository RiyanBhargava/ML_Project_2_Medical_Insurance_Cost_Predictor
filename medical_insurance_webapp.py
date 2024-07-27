import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('medical_insurance.pickle', 'rb') as f:
    model = pickle.load(f)

st.title("Riyan's Medical Insurance Cost Predictor 👨‍⚕️🏥💰")

# User input for the features
age = st.number_input('Age', min_value=0, max_value=120, value=25)
sex = st.selectbox('Sex', options=[0, 1], format_func=lambda x: 'Male' if x == 0 else 'Female')
bmi = st.number_input('BMI', min_value=0.0, max_value=50.0, value=25.0)
children = st.number_input('Number of Children', min_value=0, max_value=10, value=0)
smoker = st.selectbox('Smoker', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
region = st.selectbox('Region', options=[0, 1, 2, 3], format_func=lambda x: ['Northeast', 'Northwest', 'Southeast', 'Southwest'][x])

# Predict button
if st.button('Predict'):
    # Prepare the features for prediction
    features = np.array([[age, sex, bmi, children, smoker, region]])
    prediction = model.predict(features)
    st.success(f'The predicted medical insurance cost is: ${prediction[0]:.2f} per year')


#To run the above code, run the command "python -m streamlit run" in the terminal