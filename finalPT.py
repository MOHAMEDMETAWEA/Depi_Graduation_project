import streamlit as st
from sklearn.preprocessing import LabelEncoder
import joblib
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="Heart Risk Prediction", layout="wide")

# تخصيص CSS للتصميم
st.markdown("""
    <style>
    body {
        background-color: #1e1e2f;
        color: #e0e0e0;
    }
    .main {
        background-color: #2a2a3b;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    }
    h1 {
        color: #4fc3f7;
        text-align: center;
        font-size: 36px;
        font-weight: bold;
    }
    h2, h3, h4 {
        color: #81d4fa;
    }
    .stButton>button {
        background-color: #4fc3f7;
        color: black;
        font-weight: bold;
        border: None;
        padding: 0.5em 2em;
        border-radius: 12px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #29b6f6;
        transform: scale(1.05);
    }
    .stRadio>div {
        font-weight: bold;
        color: #aed581;
    }
    .stTextInput>div>input {
        background-color: #3a3a4d;
        color: #e0e0e0;
        border: 1px solid #4fc3f7;
        border-radius: 8px;
        padding: 5px;
    }
    .stSelectbox>div>div {
        background-color: #3a3a4d !important;
        color: #e0e0e0 !important;
    }
    .stSlider>div>label {
        color: #81c784;
    }
    .stSlider>div>div {
        color: #ffffff;
    }
    .css-1d391kg {  /* هذا كود داخلي للحقول الجديدة */
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# حالة تسجيل الدخول
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# اختيار النموذج
if 'model_choice' not in st.session_state:
    st.session_state.model_choice = None

# شاشة تسجيل الدخول
if not st.session_state.logged_in:
    st.markdown("<h1>🔐 Secure Login</h1>", unsafe_allow_html=True)
    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    if st.button("Login"):
        if username == "kimo" and password == "123":
            st.session_state.logged_in = True
            st.success("Welcome back, Kimo! ✅")
        else:
            st.error("❌ Invalid username or password")

# بعد تسجيل الدخول
if st.session_state.logged_in:

    if st.session_state.model_choice is None:
        st.markdown("<h1>📊 Choose Your Prediction Model</h1>", unsafe_allow_html=True)
        model_option = st.radio("🧠 Choose the AI model you want to use:", ["lightgbm", "XGBClassifier"])

        if st.button("Next"):
            st.session_state.model_choice = model_option
            st.rerun()

    else:
        st.markdown(f"<h1>💓 Heart Disease Risk Prediction - ({st.session_state.model_choice})</h1>", unsafe_allow_html=True)

        # تحميل الموديل
        if st.session_state.model_choice == "lightgbm":
            model = joblib.load("Lightgbm.pkl")
        else:
            model = joblib.load("XGBClassifier.pkl")

        with st.form("prediction_form"):
            st.subheader("📥 Enter Your Health Information")

            col1, col2 = st.columns(2)
            with col1:
                bmi = st.slider("⚖️ BMI", 13.04, 42.5, 25.0)
                smoking = st.radio("🚬 Do you smoke?", ["No", "Yes"])
                stroke = st.radio("🧠 Have you had a stroke?", ["No", "Yes"])
                physical_health = st.slider("🧑‍⚕️ Physical Health (0-30)", 0.0, 30.0, 5.0)
                mental_health = st.slider("🧠 Mental Health (0-30)", 0.0, 30.0, 5.0)
                diff_walking = st.radio("🚶‍♂️ Difficulty Walking?", ["No", "Yes"])
                sex = st.radio("👤 Gender", ["Female", "Male"])
                age_category = st.selectbox("🎂 Age Category", [
                    "18-24", "25-29", "30-34", "35-39", "40-44", "45-49",
                    "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80 or older"
                ])
            with col2:
                race = st.selectbox("🌍 Race", ["White", "Black", "Hispanic", "Other"])
                diabetic = st.selectbox("🩸 Diabetic", ["Yes", "No"])
                physical_activity = st.radio("💪 Physical Activity", ["No", "Yes"])
                gen_health = st.selectbox("🩺 General Health", ["Good", "Medium", "Poor"])
                sleep_time = st.slider("🛌 Sleep Time (hours)", 0, 24, 7)
                kidney_disease = st.radio("🩻 Kidney Disease?", ["No", "Yes"])
                health_strain = st.slider("💪 Health Strain", 1.343, 5.5, 3.0)
                health_strain_level = st.selectbox("⚖️ Health Strain Level", ["Low", "Medium", "High"])

            submitted = st.form_submit_button("🚀 Predict Now")

        if submitted:
            input_data = pd.DataFrame([{
                'BMI': bmi,
                'Smoking': smoking,
                'Stroke': stroke,
                'PhysicalHealth': physical_health,
                'MentalHealth': mental_health,
                'DiffWalking': diff_walking,
                'Sex': sex,
                'AgeCategory': age_category,
                'Race': race,
                'Diabetic': diabetic,
                'PhysicalActivity': physical_activity,
                'GenHealth': gen_health,
                'SleepTime': sleep_time,
                'KidneyDisease': kidney_disease,
                'HealthStrain': health_strain,
                'HealthStrainLevel': health_strain_level
            }])

            # تحويل البيانات
            input_data['Smoking'] = input_data['Smoking'].map({'No': 0, 'Yes': 1})
            input_data['Stroke'] = input_data['Stroke'].map({'No': 0, 'Yes': 1})
            input_data['DiffWalking'] = input_data['DiffWalking'].map({'No': 0, 'Yes': 1})
            input_data['Sex'] = input_data['Sex'].map({'Female': 0, 'Male': 1})
            input_data['AgeCategory'] = input_data['AgeCategory'].map({
                "18-24": 0, "25-29": 1, "30-34": 2, "35-39": 3, "40-44": 4,
                "45-49": 5, "50-54": 6, "55-59": 7, "60-64": 8, "65-69": 9,
                "70-74": 10, "75-79": 11, "80 or older": 12
            })
            input_data['Race'] = input_data['Race'].map({"White": 0, "Black": 1, "Hispanic": 2, "Other": 3})
            input_data['Diabetic'] = input_data['Diabetic'].map({"No": 0, "Yes": 1})
            input_data['PhysicalActivity'] = input_data['PhysicalActivity'].map({'No': 0, 'Yes': 1})
            input_data['GenHealth'] = input_data['GenHealth'].map({"Good": 0, "Medium": 1, "Poor": 2})
            input_data['KidneyDisease'] = input_data['KidneyDisease'].map({"No": 0, "Yes": 1})
            input_data['HealthStrainLevel'] = input_data['HealthStrainLevel'].map({"Low": 0, "Medium": 1, "High": 2})

            prediction = model.predict(input_data)

            if prediction[0] == 1:
                st.error("⚠️ You are at **risk** of heart disease. Please consult a doctor.")
            else:
                st.success("✅ No significant risk of heart disease. Keep up the healthy lifestyle!")
