from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("house_price_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    area = float(request.form["area"])
    
    prediction = model.predict(np.array([[area]]))
    price = round(prediction[0], 2)

    return render_template("index.html", prediction_text=f"Estimated House Price: ₹ {price}")

if __name__ == "__main__":
    app.run(debug=True)
