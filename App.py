import streamlit as st
import joblib
import numpy as np

st.set_page_config(
    page_title="Wine Quality Predictor",
    layout="centered",
    initial_sidebar_state="auto",
)

try:
    model = joblib.load('random_forest_model.pkl')
except FileNotFoundError:
    st.error("Model file 'random_forest_model.pkl' not found. Please train and save the model first.")
    st.stop()


st.markdown("<h1 style='text-align: center; color: #8B0000;'>Wine Quality Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Check if a wine sample meets premium standards based on its chemical profile.</p>", unsafe_allow_html=True)
st.markdown("---")

features = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
            'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
            'pH', 'sulphates', 'alcohol']

st.markdown("### Enter Wine Chemical Properties")
cols = st.columns(2)
user_input = []

for i, feature in enumerate(features):
    with cols[i % 2]:
        val = st.number_input(f"{feature.title()}", min_value=0.0, format="%.3f", key=feature)
        user_input.append(val)

if st.button("Predict Quality"):
    input_array = np.array([user_input])
    prediction = model.predict(input_array)[0]
    probabilities = model.predict_proba(input_array)[0]
    confidence = probabilities[prediction] * 100

    if prediction == 1:
        st.success(f"The wine is **Good Quality**")
        st.progress(min(int(confidence), 100))
        st.markdown(f"<h4 style='color:green;'>Confidence: {confidence:.2f}%</h4>", unsafe_allow_html=True)
    else:
        st.error(f"The wine is **Not Good Quality**")
        st.markdown(f"<h4 style='color:red;'>Confidence: {confidence:.2f}%</h4>", unsafe_allow_html=True)
