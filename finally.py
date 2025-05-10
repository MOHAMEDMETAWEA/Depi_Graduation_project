import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model_pipeline_compressed.pkl")
st.title("Heart Disease Prediction")

with st.form("input_form"):
    st.subheader("Enter Patient Information:")

    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0, step=0.1)
    physical_health = st.slider("Physical Health (days)", min_value=0, max_value=30, value=5)
    mental_health = st.slider("Mental Health (days)", min_value=0, max_value=30, value=5)
    sleep_time = st.slider("Sleep Time (hours)", min_value=0, max_value=24, value=7)

    smoking = st.selectbox("Smoking", ["Yes", "No"])
    diff_walking = st.selectbox("Difficulty Walking", ["Yes", "No"])
    sex = st.selectbox("Sex", ["Male", "Female"])
    age_category = st.selectbox("Age Category", [
        "18-24", "25-29", "30-34", "35-39", "40-44", "45-49",
        "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80 or older"
    ])
    race = st.selectbox("Race", [
        "White", "Black", "Asian", "American Indian/Alaskan Native",
        "Hispanic", "Other"
    ])
    diabetic = st.selectbox("Diabetic", ["Yes", "No", "No, borderline diabetes", "Yes (during pregnancy)"])
    physical_activity = st.selectbox("Physical Activity", ["Yes", "No"])
    gen_health = st.selectbox("General Health", ["Excellent", "Very good", "Good", "Fair", "Poor"])
    has_health_issues = st.selectbox("Has Health Issues", ["Yes", "No"])

    submit = st.form_submit_button("Predict")

if submit:
    input_data = pd.DataFrame({
        "BMI": [bmi],
        "PhysicalHealth": [physical_health],
        "MentalHealth": [mental_health],
        "SleepTime": [sleep_time],
        "Smoking": [smoking],
        "DiffWalking": [diff_walking],
        "Sex": [sex],
        "AgeCategory": [age_category],
        "Race": [race],
        "Diabetic": [diabetic],
        "PhysicalActivity": [physical_activity],
        "GenHealth": [gen_health],
        "HasHealthIssues": [has_health_issues]
    })

    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result:")
    if prediction == 1:
        st.error(f"⚠️ The model predicts that the patient is likely to have heart disease.")
    else:
        st.success(f"✅ The model predicts that the patient is unlikely to have heart disease.")
