import streamlit as st
import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression


model = joblib.load('model.joblib')

home_owership = ['RENT', 'MORTGAGE', 'OWN', 'OTHER']
loan_intent = ['EDUCATION',
               'MEDICAL',
               'VENTURE',
               'PERSONAL',
               'DEBTCONSOlIDATION',
               'HOMEIMPROVEMENNT']
loan_grade = ('A', 'B', 'C', 'D', 'E','F', 'G')
default_on_file = ['N', 'Y']


st.markdown('# Loan Default Prediction App')
st.markdown('---')
col1 ,col2 = st.columns(2)

with col1:
    age = st.slider('Person Age (in Years)', 18, 60)
    income = st.number_input('Perso Income($)')
    owership = st.selectbox('Home Owership', home_owership)
    emp_length = st.number_input('Length of Employment')
    intent = st.selectbox('Loan Intent', loan_intent)
    grade = st.selectbox('Loan Grade', loan_grade)

with col2:
    web_time = st.number_input('Time on website (in Minutes)')
    mem_length = st.number_input('Length of membership (in Months)')

if st.button("Predict"):
    sample = np.array([sess, app_time, web_time, mem_length]).reshape(1, -1)
    prediction = model.predict(sample)[0]
    prediction = f'${prediction:.2f}'
    st.info(f'This customer is likely to spend up to {prediction}')