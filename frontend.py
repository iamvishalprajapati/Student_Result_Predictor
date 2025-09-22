import streamlit as st
import requests 

st.title('Student Result Predictor')

studyhours = st.number_input('Enter Your Study Hours', min_value=1)
attendance = st.number_input('Enter Your Attendance', min_value=1)
pastscore = st.number_input('Enter Your Past Score', min_value=1)
sleephours = st.number_input('Enter Your Sleep Hours', min_value=1)

if st.button('Predict Result'):
    load = {
        'studyhours': studyhours,
        'attendance': attendance,
        'pastscore': pastscore,
        'sleephours': sleephours
    }

    response = requests.post('http://127.0.0.1:8000/Result', json=load)

    if response.status_code == 200:
        st.success(f'{response.json()}')
    else:
        st.success('Something Went Wrong')