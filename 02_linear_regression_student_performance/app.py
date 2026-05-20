import streamlit as st
import pandas as pd
import joblib

# 🔹 Full path to your saved model
model_path = r"C:\Users\Admin\OneDrive\Desktop\Sitaram_Github\ref\04_linear_regression_student_performance\models\ridge_student_performance_model.pkl"

model = joblib.load(model_path)

st.title("🎓 Student Performance Predictor")
st.write("Enter student details to predict the final grade (G3)")

# ---------- Basic Info ----------
school = st.selectbox("School", ["GP", "MS"])
sex = st.selectbox("Sex", ["F", "M"])
age = st.slider("Age", 15, 22, 17)
address = st.selectbox("Address Type", ["U", "R"])
famsize = st.selectbox("Family Size", ["LE3", "GT3"])
Pstatus = st.selectbox("Parent Cohabitation Status", ["T", "A"])

# ---------- Parents ----------
Medu = st.slider("Mother's Education (0–4)", 0, 4, 2)
Fedu = st.slider("Father's Education (0–4)", 0, 4, 2)
Mjob = st.selectbox("Mother's Job", ["teacher", "health", "services", "at_home", "other"])
Fjob = st.selectbox("Father's Job", ["teacher", "health", "services", "at_home", "other"])
reason = st.selectbox("Reason for School Choice", ["home", "reputation", "course", "other"])
guardian = st.selectbox("Guardian", ["mother", "father", "other"])

# ---------- Travel & Study ----------
traveltime = st.slider("Travel Time (1–4)", 1, 4, 2)
studytime = st.slider("Weekly Study Time (1–4)", 1, 4, 2)
failures = st.slider("Past Class Failures (0–3)", 0, 3, 0)

# ---------- Support ----------
schoolsup = st.selectbox("School Support", ["yes", "no"])
famsup = st.selectbox("Family Support", ["yes", "no"])
paid = st.selectbox("Extra Paid Classes", ["yes", "no"])
activities = st.selectbox("Extra Activities", ["yes", "no"])
nursery = st.selectbox("Attended Nursery", ["yes", "no"])
higher = st.selectbox("Wants Higher Education", ["yes", "no"])
internet = st.selectbox("Internet Access at Home", ["yes", "no"])
romantic = st.selectbox("In a Relationship", ["yes", "no"])

# ---------- Lifestyle ----------
famrel = st.slider("Family Relationship Quality (1–5)", 1, 5, 4)
freetime = st.slider("Free Time After School (1–5)", 1, 5, 3)
goout = st.slider("Going Out With Friends (1–5)", 1, 5, 3)
Dalc = st.slider("Workday Alcohol Consumption (1–5)", 1, 5, 1)
Walc = st.slider("Weekend Alcohol Consumption (1–5)", 1, 5, 2)
health = st.slider("Health Status (1–5)", 1, 5, 4)
absences = st.slider("Number of Absences", 0, 50, 5)

# ---------- Previous Grades ----------
G1 = st.slider("First Period Grade (G1)", 0, 20, 10)
G2 = st.slider("Second Period Grade (G2)", 0, 20, 10)

if st.button("Predict Final Grade"):
    input_data = pd.DataFrame([{
        "school": school,
        "sex": sex,
        "age": age,
        "address": address,
        "famsize": famsize,
        "Pstatus": Pstatus,
        "Medu": Medu,
        "Fedu": Fedu,
        "Mjob": Mjob,
        "Fjob": Fjob,
        "reason": reason,
        "guardian": guardian,
        "traveltime": traveltime,
        "studytime": studytime,
        "failures": failures,
        "schoolsup": schoolsup,
        "famsup": famsup,
        "paid": paid,
        "activities": activities,
        "nursery": nursery,
        "higher": higher,
        "internet": internet,
        "romantic": romantic,
        "famrel": famrel,
        "freetime": freetime,
        "goout": goout,
        "Dalc": Dalc,
        "Walc": Walc,
        "health": health,
        "absences": absences,
        "G1": G1,
        "G2": G2
    }])

    prediction = model.predict(input_data)[0]
    st.success(f"🎯 Predicted Final Grade (G3): **{round(prediction, 2)} / 20**")

