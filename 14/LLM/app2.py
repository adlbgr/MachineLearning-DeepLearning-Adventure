import streamlit as st
import google.generativeai as genai

# Configure the generative AI model
genai.configure(api_key='Your API Key')

st.title('Analysis Image with AI')
model = genai.GenerativeModel('gemini-1.5-pro-latest')

from PIL import Image
resim = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if resim is not None:
    img = Image.open(resim)
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    # response = model.generate_content(img)
    # st.write(response.text)
que = st.text_input("Enter your question")

if st.button('Submit'):
    response = model.generate_content([que, img],stream=True)
    response.resolve()
    st.write(response.text)