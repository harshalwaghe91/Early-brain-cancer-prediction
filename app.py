import streamlit as st
from PIL import Image
from predict import predict_image

st.set_page_config(page_title="Brain Tumor Detection")

st.title("🧠 Early Brain Tumor Prediction")
st.write("Upload an MRI image to detect the tumor type.")

uploaded_file = st.file_uploader(
    "Choose an MRI Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded MRI", use_container_width=True)

    with st.spinner("Analyzing MRI..."):
        label, confidence = predict_image(image)

    st.success(f"Prediction: {label}")
    st.info(f"Confidence: {confidence*100:.2f}%")