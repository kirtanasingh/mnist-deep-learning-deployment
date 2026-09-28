
import streamlit as st
import requests

st.title("Digit Recognition - Deep Learning Lab")

st.write("Upload a handwritten digit image to get a prediction.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    st.image(
        uploaded_file,
        caption="Uploaded Image",
        width=150
    )

    if st.button("Predict"):

        files = {
            "file": uploaded_file.getvalue()
        }

        response = requests.post(
            "http://127.0.0.1:5000/predict",
            files=files
        )

        if response.status_code == 200:

            result = response.json()

            st.success(
                f"Predicted Digit: {result['predicted_digit']}"
            )

            st.write(
                f"Confidence: {result['confidence'] * 100:.2f}%"
            )

        else:

            st.error("Prediction failed. Please try again.")
