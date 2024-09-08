import streamlit as st
import pandas as pd
import plotly.express as px

st.title('MLOps Streamlit App! :flag-tr:')
name = st.text_input('Enter your name:',max_chars=20)
st.slider('Select a number:',min_value=0,max_value=100)
st.button('Click me!')
st.audio('data/song.mp3')
st.success(f'Welcome {name}! :tada:')
st.error('This is an error message!')
st.warning('This is a warning message!')
st.sidebar.title('Sidebar Title')
st.sidebar.text('This is a sidebar text!')
st.sidebar.markdown('This is a sidebar markdown!')
st.sidebar.error('This is a sidebar error!')
st.sidebar.selectbox("Menu", ["Home", "About", "Contact"])

st.info('This is an info message!')

df = pd.read_csv('data/prog_languages_data.csv')
fig = px.pie(df,values='Sum')
st.plotly_chart(fig)
fig2 = px.bar(df,x='lang',y='Sum')
st.plotly_chart(fig2)


file  = st.file_uploader('Upload a file:',type=['csv','txt'])

st.code('''
    import pandas as pd
    df = pd.read_csv('data\iris.csv')
''')

st.video('data\secret_of_success.mp4')
st.camera_input('Capture your photo')
st.date_input('Enter your date of birth:')
st.time_input('Enter your time of birth:')
st.text_input('Enter your password:',type='password')
st.text_area('Enter your feedback:',height=100)
st.number_input('Enter your age:',min_value=0,max_value=100)
st.radio('Select a color:',options=['Red','Green','Blue'])
st.selectbox('Select a color:',options=['Red','Green','Blue'])
st.multiselect('Select a color:',options=['Red','Green','Blue'])
st.video('http://10.0.0.99:8080/video.mp4')
st.image('data\image_01.jpg',width=300)
st.divider()
df = pd.read_csv('data\iris.csv')
st.table(df)
st.dataframe(df)
st.json({'name':'John','age':25})
