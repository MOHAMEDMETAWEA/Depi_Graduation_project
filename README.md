
# 🫀 Heart Disease Prediction Web App

This is a Streamlit-based machine learning web application that predicts the risk of heart disease based on user-provided health and lifestyle data.

---

## 📌 Overview

Heart disease is a leading global health issue. This project leverages machine learning to offer a lightweight, real-time prediction tool that can assist in early risk detection. Built entirely in Python and deployed using Streamlit, the app provides a user-friendly interface for risk evaluation.

---

## 🚀 Features

- ✅ Streamlit-based interactive web interface  
- 🧠 Uses a trained Random Forest Classifier model  
- ⏱️ Real-time prediction without backend infrastructure  
- 📈 Model trained on structured health and lifestyle data  
- 📊 Personalized prediction messages ("At Risk" / "No Risk")  
- 🔍 Feature importance analyzed during model development

---

## 🧪 Input Fields

**Numerical Inputs:**
- Body Mass Index (BMI)
- Physical Health (days with poor physical health)
- Mental Health (days with poor mental health)
- Sleep Time (average hours slept per day)

**Categorical Inputs:**
- Smoking (Yes/No)
- Difficulty Walking (Yes/No)
- Sex (Male/Female)
- Age Category (e.g., 18–24, 25–29, ..., 80 or older)
- Race
- Diabetic Status (e.g., No, Yes, Borderline)
- Physical Activity (Yes/No)
- General Health (Excellent to Poor)
- Alcohol Consumption (Yes/No)
- Chronic Conditions: Asthma, Kidney Disease, Skin Cancer (Yes/No)

---

## 🧠 Machine Learning Model

- **Model Used:** `RandomForestClassifier`
- **Library:** scikit-learn
- **Pipeline File:** `model_pipeline.pkl`
- **Encoding:** Manual mapping (e.g., Yes/No → 1/0), ordinal encoding for age and general health
- **Evaluation Metrics (development phase):** Accuracy, F1-score

---

## 🧱 System Architecture

### Backend:
- Encodes user input
- Loads model and performs predictions
- Built with: `pandas`, `scikit-learn`, `joblib`, `streamlit`

### Frontend:
- Clean and intuitive form-based UI
- Streamlit interface with radio buttons, sliders, and dropdowns

---

## 📂 Files Included

- `finally.py` — Main Streamlit app script
- `model_pipeline.pkl` — Pre-trained ML model pipeline (must be in the same directory)
- `HealthCare.docx` — Full project documentation and methodology (optional for users)

---

## ▶️ How to Run

1. **Install required packages**:
   ```bash
   pip install streamlit pandas joblib scikit-learn
   ```

2. **Make sure the following files are in the same directory**:
   - `finally.py`
   - `model_pipeline.pkl`

3. **Run the app**:
   ```bash
   streamlit run finally.py
   ```

4. **Open your browser** and use the app to input data and receive predictions.

---

## 👨‍💻 Team & Credits

Developed as part of the IBM Data Science project by:

- Eman Abdelfatah  
- Hazem Ibrahim  
- Hussein Mohamed  
- Kareem Fekry  
- Mohamed Mostafa  

Supervised by: **Eng. Eslam Adel**

Group Code: `CLS GIZ2_AIS4_S1`

---

## 📚 License

For educational use only. If you'd like to reuse or adapt the project for commercial or research purposes, please contact the authors.
