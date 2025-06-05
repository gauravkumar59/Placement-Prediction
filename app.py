import streamlit as st
import joblib
import numpy as np


model=joblib.load("placement_model.pkl")

st.title("Placement Package Predictor")
st.write("Fill in the details to see your estimated placement package (in LPA)")


cgpa= st.slider("Your CGPA", 5.0, 10.0, step=0.1)
internship= st.slider("Internship Rating (1-10)", 1, 10)
experience= st.slider("Years of Experience", 0, 5)
coding= st.slider("Coding Skill (1-10)", 1, 10)
communication= st.slider("Communication Skill (1-10)", 1, 10)


if st.button("Predict"):
    input_data = np.array([[cgpa, internship, experience, coding, communication]])
    result = model.predict(input_data)[0]
    st.write("Your predicted package is:")
    st.success(str(round(result, 2)) + " LPA")
