import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

model = load_model("skin_cancer_model.h5")

def procces_image(img):
    img = img.resize((170, 170)) # Resize image
    img = np.array(img) # Convert to array
    img =img/ 255.0 # Normalize image
    img = np.expand_dims(img,axis=0) # Add batch dimension
    return img
st.title("Cancer detection - Classification :cancer:")

st.write("Select a image of skin cancer to classify")

file = st.file_uploader("Upload a image", type=["jpg", "png", "jpeg"])

if file is None:
    st.text("Please upload an image file")
else:
    img = Image.open(file)
    st.image(img, caption="Uploaded Image")
    image = procces_image(img)
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction[0])
    class_names = ["Not-Cancer", "Cancer"]
    st.write(class_names[predicted_class])
