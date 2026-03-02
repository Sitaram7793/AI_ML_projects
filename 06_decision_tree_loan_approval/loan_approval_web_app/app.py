from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# =========================
# Load trained artifacts
# =========================
model = joblib.load("loan_approval_model.pkl")
encoders = joblib.load("encoders.pkl")

# OPTIONAL but STRONGLY recommended
try:
    feature_order = joblib.load("features.pkl")
except:
    feature_order = [
        "Age",
        "Gender",
        "MaritalStatus",
        "EducationLevel",
        "EmploymentStatus",
        "AnnualIncome",
        "LoanAmountRequested",
        "CreditScore",
        "ExistingLoansCount",
        "LatePaymentsLastYear"
    ]


# =========================
# Utility: Safe Encoding
# =========================
def safe_encode(encoder, value):
    if value in encoder.classes_:
        return encoder.transform([value])[0]
    else:
        return -1   # unseen category safeguard


# =========================
# Routes
# =========================
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # -------- Numerical Inputs --------
        age = int(request.form['Age'])
        income = float(request.form['AnnualIncome'])
        loan_amount = float(request.form['LoanAmountRequested'])
        credit_score = int(request.form['CreditScore'])
        existing_loans = int(request.form['ExistingLoansCount'])
        late_payments = int(request.form['LatePaymentsLastYear'])

        # -------- Categorical Inputs --------
        gender = safe_encode(encoders['Gender'], request.form['Gender'])
        marital = safe_encode(encoders['MaritalStatus'], request.form['MaritalStatus'])
        education = safe_encode(encoders['EducationLevel'], request.form['EducationLevel'])
        employment = safe_encode(encoders['EmploymentStatus'], request.form['EmploymentStatus'])

        # -------- Build Input DataFrame --------
        input_df = pd.DataFrame([{
            "Age": age,
            "Gender": gender,
            "MaritalStatus": marital,
            "EducationLevel": education,
            "EmploymentStatus": employment,
            "AnnualIncome": income,
            "LoanAmountRequested": loan_amount,
            "CreditScore": credit_score,
            "ExistingLoansCount": existing_loans,
            "LatePaymentsLastYear": late_payments
        }])

        # -------- Ensure Correct Feature Order --------
        input_df = input_df[feature_order]

        # -------- Prediction --------
        prediction = model.predict(input_df)[0]
        result = "Loan Approved ✅" if prediction == 1 else "Loan Rejected ❌"

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")


# =========================
# Run App
# =========================
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
