import streamlit as st
import pickle
import pandas as pd
with open("trained_model.sav", "rb") as f:
    model = pickle.load(f)

# App title and header
st.title("Diabetes Prediction App")
st.write("This app predicts the risk of diabetes based on the Pima Indians Diabetes dataset.")

# Input fields for user data
pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20)
glucose = st.number_input("Glucose Level (mg/dL)", min_value=0)
blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0)
skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0)
insulin = st.number_input("Insulin Level (μU/mL)", min_value=0)
bmi = st.number_input("Body Mass Index (kg/m^2)", min_value=0.0)
diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age (years)", min_value=0)

# User input data
user_data = pd.DataFrame({
    "Pregnancies": [pregnancies],
    "Glucose": [glucose],
    "BloodPressure": [blood_pressure],
    "SkinThickness": [skin_thickness],
    "Insulin": [insulin],

    
"BMI": [bmi],
    "DiabetesPedigreeFunction": [diabetes_pedigree_function],
    "Age": [age]
})

# Predict button and result display
if st.button("Predict"):
    prediction = model.predict(user_data)[0]
    if prediction == 0:
        st.success("The person is not likely to have diabetes.")
    else:
        st.warning("The person is at risk of diabetes.")
        st.write("It is recommended to consult a doctor for further evaluation.")