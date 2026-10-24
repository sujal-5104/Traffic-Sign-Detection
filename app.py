import json
import numpy as np
import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model

st.set_page_config(
    page_title="Traffic Sign Recognition",
    page_icon="🚦"
)

@st.cache_resource
def load_trained_model():
    return load_model("traffic_sign_model.keras")

model = load_trained_model()

with open("classes.json", "r", encoding="utf-8") as f:
    classes = {int(k): v for k, v in json.load(f).items()}

st.title("Traffic Sign Recognition")
st.write("Upload a traffic-sign image to predict its class.")

uploaded_file = st.file_uploader(
    "Choose a traffic-sign image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded traffic sign", width=300)

    resized = image.resize((32, 32))
    image_array = np.array(resized, dtype=np.float32) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    probabilities = model.predict(image_array, verbose=0)[0]
    predicted_id = int(np.argmax(probabilities))
    confidence = float(probabilities[predicted_id]) * 100

    st.subheader("Prediction Result")
    st.success(classes.get(predicted_id, "Unknown"))
    st.write(f"Class ID: {predicted_id}")
    st.write(f"Confidence: {confidence:.2f}%")
