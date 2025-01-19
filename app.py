import joblib
import pandas as pd
import streamlit as st 
from utils import InternetService_list, Contract_list, PaymentMethod_list

model = joblib.load('churn.joblib')
st.title('Churn Prediction')
gender = st.selectbox("Gender", options=[0, 1], format_func=lambda x: "Male" if x else "Female")
SeniorCitizen = st.selectbox("SeniorCitizen", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
Partner = st.selectbox("Partner", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
Dependents = st.selectbox("Dependents", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
tenure = st.number_input('tenure', 1,100)
PhoneService = st.selectbox("PhoneService", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
MultipleLines = st.selectbox("MultipleLines", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
InternetService = st.selectbox("InternetService", InternetService_list)
OnlineSecurity = st.selectbox("OnlineSecurity", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
OnlineBackup = st.selectbox("OnlineBackup", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
DeviceProtection = st.selectbox("DeviceProtection", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
TechSupport = st.selectbox("TechSupport", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
StreamingTV = st.selectbox("StreamingTV", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
StreamingMovies = st.selectbox("StreamingMovies", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
Contract = st.selectbox("Contract", Contract_list)
PaperlessBilling = st.selectbox("GePaperlessBillingnder", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
PaymentMethod = st.selectbox("PaymentMethod", PaymentMethod_list)
MonthlyCharges = st.number_input('MonthlyCharges', 1,200)
TotalCharges = st.number_input('TotalCharges', 1,2000)

if st.button("Predict Price"):
    user_data = pd.DataFrame({
        'gender': [gender],
        'SeniorCitizen': [SeniorCitizen],
        'Partner': [Partner],
        'Dependents': [Dependents],
        'tenure': [tenure],
        'PhoneService': [PhoneService],
        'MultipleLines': [MultipleLines],
        'OnlineSecurity': [OnlineSecurity],
        'OnlineBackup': [OnlineBackup],
        'DeviceProtection': [DeviceProtection],
        'TechSupport': [TechSupport],
        'StreamingTV': [StreamingTV],
        'StreamingMovies': [StreamingMovies],
        'PaperlessBilling': [PaperlessBilling],
        'MonthlyCharges': [MonthlyCharges],
        'TotalCharges': [TotalCharges]
    })
    
    for Contract_list_col in Contract_list:
        user_data[Contract_list_col] = 0
    user_data[Contract] = 1
        
    for col in PaymentMethod_list:
        user_data[col] = 0
    user_data[PaymentMethod] = 1
    
    for InternetService_col in InternetService_list:
        user_data[InternetService_col] = 0
    user_data[InternetService] = 1
    
    prediction = model.predict(user_data)[0]
    
    if (prediction== 1):
        st.write("### Churn is True")
    else:
        st.write("### Churn is False")


