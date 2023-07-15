import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder

# Load the logistic regression model
model = joblib.load('model.joblib')

# Define the prediction function
def predict(person_age, person_income, person_home_ownership, person_emp_length, loan_intent, loan_grade, 
loan_amnt, loan_int_rate, loan_percent_income, cb_person_default_on_file, cb_person_cred_hist_length): 
    #Predicting loan eligibility
    if person_home_ownership == 'RENT':
        person_home_ownership = 0
    elif person_home_ownership == 'MORTGAGE':
        person_home_ownership = 1
    elif person_home_ownership == 'OWN':
        person_home_ownership = 2
    elif person_home_ownership == 'OTHER':
        person_home_ownership = 3

    if loan_intent == 'EDUCATION':
        loan_intent = 0
    elif loan_intent == 'MEDICAL':
        loan_intent = 1
    elif loan_intent == 'VENTURE':
        loan_intent = 2
    elif loan_intent == 'PERSONAL':
        loan_intent = 3
    elif loan_intent == 'DEBTCONSOLIDATION':
        loan_intent = 4
    elif loan_intent == 'HOMEIMPROVEMENT':
        loan_intent = 5

    if loan_grade == 'A':
        loan_grade = 0
    elif loan_grade == 'B':
        loan_grade = 1
    elif loan_grade == 'C':
        loan_grade = 2
    elif loan_grade == 'D':
        loan_grade = 3
    elif loan_grade == 'E':
        loan_grade = 4
    elif loan_grade == 'F':
        loan_grade = 5
    elif loan_grade == 'G':
        loan_grade = 6
    
    if cb_person_default_on_file == 'N':
        cb_person_default_on_file = 0
    elif cb_person_default_on_file == 'Y':
        cb_person_default_on_file = 1
    

    prediction = model.predict(pd.DataFrame([[person_age, person_income, person_home_ownership, person_emp_length, loan_intent, loan_grade, 
loan_amnt, loan_int_rate, loan_percent_income, cb_person_default_on_file, cb_person_cred_hist_length]], 
columns=['person_age', 'person_income', 'person_home_ownership', 'person_emp_length', 'loan_intent', 'loan_grade', 
'loan_amnt', 'loan_int_rate', 'loan_percent_income', 'cb_person_default_on_file', 'cb_person_cred_hist_length']))
    return prediction


st.title('LOAN DEFAULT PREDICTOR')
# st.image("""https://www.thestreet.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cq_auto:good%2Cw_1200/MTY4NjUwNDYyNTYzNDExNTkx/why-dominion-diamonds-second-trip-to-the-block-may-be-different.png""")
st.header('Enter the characteristics of the applicant:')

# Split the input boxes into two columns
col1, col2 = st.columns(2)

# Input boxes for the first column
with col1:
    person_age = st.number_input('Age of Applicant:', min_value=0.0, max_value=120.0, value=1.0)
    person_income = st.number_input('Income of Applicant:', min_value=0.0, max_value=1000000.0, value=1.0)
    person_home_ownership = st.selectbox('Type of Residence:', ['RENT', 'MORTGAGE', 'OWN', 'OTHER'])
    person_emp_length = st.number_input('Years of Employment:', min_value=0.0, max_value=30.0, value=1.0)
    loan_intent = st.selectbox('Loan Intent:', ['EDUCATION', 'MEDICAL', 'VENTURE', 'PERSONAL', 'DEBTCONSOLIDATION', 'HOMEIMPROVEMENT'])

# Input boxes for the second column
with col2:
    loan_grade = st.selectbox('Loan Grade:', ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    loan_amnt = st.number_input('Loan Amount:', min_value=0.0, max_value=1000000.0, value=1.0)
    loan_int_rate = st.number_input('Interest Rate:', min_value=0.0, max_value=100.0, value=0.01)
    loan_percent_income = st.number_input('Percentage of Loan to Income', min_value=0.0, max_value=100.0, value=0.01)
    cb_person_default_on_file = st.selectbox('Previous History of Default:', ['N','Y'])
    cb_person_cred_hist_length = st.number_input('Length of Credit History (In Years)', min_value=0.0, max_value=50.0, value=1.0)

if st.button('Predict Default'):
    loan_status = predict(person_age, person_income, person_home_ownership, person_emp_length, loan_intent, loan_grade, 
                          loan_amnt, loan_int_rate, loan_percent_income, cb_person_default_on_file, cb_person_cred_hist_length)
    result = 'YES' if loan_status[0] == 1 else 'NO'
    st.success(f'Application Result: {result}')

