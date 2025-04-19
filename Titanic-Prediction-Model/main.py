import streamlit as st
import pandas as pd
import joblib

model = joblib.load("titanic_model.pkl")

st.title("🚢 Titanic Survival Predictor")

st.markdown("### Enter passenger details:")

pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
sex = st.radio("Sex", ["male", "female"])
age = st.slider("Age", 0, 100, 25)
sibsp = st.number_input("No. of siblings/spouses aboard", 0, 10, 0)
parch = st.number_input("No. of parents/children aboard", 0, 10, 0)
fare = st.number_input("Fare", 0.0, 600.0, 50.0)

input_data = pd.DataFrame({
    'Pclass': [pclass],
    'Sex': [1 if sex == "male" else 0],
    'Age': [age],
    'SibSp': [sibsp],
    'Parch': [parch],
    'Fare': [fare]
})

if st.button("Predict Survival"):
    prediction = model.predict(input_data)
    st.success("✅ Survived!" if prediction[0] == 1 else "❌ Did not survive.")
