import streamlit as st
import pandas as pd
import plotly.express as px
import os
from datetime import date

st.title('Get data from form and save it to a csv file')

name = st.text_input('Enter your name:', max_chars=20)
password = st.text_input('Enter your password:', type='password')
dob = st.date_input('Enter your date of birth:', min_value=date(1950, 1, 1))
age = st.slider('Enter your age:', min_value=0, max_value=100)
message = st.text_area('Enter your feedback:', height=100)

if st.button('Submit'):
    data = {'Name': name, 'Password': password, 'DOB': dob, 'Age': age, 'Feedback': message}
    df = pd.DataFrame(data, index=[0])
    st.write(df)
    
    # Check if the file exists
    file_path = 'data/user_data.csv'
    if os.path.exists(file_path):
        # If the file exists, append the new data without writing the header
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        # If the file does not exist, write the data with the header
        df.to_csv(file_path, index=False)
    
    st.success('Data saved successfully!')

st.button('Click me!')