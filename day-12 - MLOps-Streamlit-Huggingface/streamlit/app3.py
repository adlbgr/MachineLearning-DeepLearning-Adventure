import streamlit as st
import pandas as pd
import pickle   

st.title('Salary Prediction :heavy_dollar_sign:')

model = pickle.load(open('guess_salary.pkl', 'rb'))

experience = st.number_input('Enter your experience in years', min_value=0, max_value=20, value=0, step=1)
test_score = st.number_input('Enter your test score out of 100', min_value=0, max_value=10, value=0, step=1)
interview_score = st.number_input('Enter your interview score out of 10', min_value=0, max_value=10, value=0, step=1)

if st.button('Predict Salary'):
    input_data = pd.DataFrame(data=[[experience, test_score, interview_score]], columns=['experience', 'test_score', 'interview_score'])
    prediction = model.predict(input_data)
    st.success(f'Your estimated salary is ${prediction[0]:.2f}')
    st.balloons() 

st.write('---')