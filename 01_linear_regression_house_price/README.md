# 🏠 House Price Prediction – Multiple Feature Linear Regression
An end-to-end Machine Learning project that predicts residential property prices based on house features such as area, number of bathrooms, grade, and location characteristics.  
This project demonstrates the complete ML workflow:  
Data Analysis → Feature Selection → Model Training → Model Evaluation → Residual Diagnostics → Model Saving  

## 📌 Problem Statement
Real estate price estimation is difficult because house prices depend on many factors — not just size. Buyers, sellers, and agents need a system that can estimate a property’s value using measurable features.

The goal of this project is to:
- Predict house price using multiple features
- Identify the most important factors affecting price
- Evaluate if Linear Regression assumptions hold
- Build a baseline model for future advanced models

---

## 📊 Dataset Description

The dataset contains residential property details such as:
|Feature|Description|
|-|-|
|living area|usable interior house area|
|lot area|total land area|
|bedrooms	|number of bedrooms|
|bathrooms	|number of bathrooms|
|floors	|number of floors|
|grade	|construction & material quality|
|waterfront present	|whether house faces water|
|basement area	|basement size|
|number of views	|scenic view rating|
|condition	|overall house condition|

Target Variable: Price  

---

## 📂 Project Structure
01_linear_regression_house_price/<br>
│<br>
├── data/<br>
│   └── House Price India.csv<br>
│<br>
├── images/<br>
│   ├── price_distribution.png<br>
│   ├── area_vs_price.png<br>
│   ├── correlation_heatmap.png<br>
│   ├── actual_vs_predicted_prices.png<br>
│   └── residual_distribution.png<br>
│<br>
├── notebook/<br>
│   └── linear_regression_house_price.ipynb<br>
│<br>
└── README.md<br>


---

## 📊 Exploratory Data Analysis (EDA)

### 🔹 Price Distribution
<p align="center">
  <img src="images/price_distribution.png" width="600">
</p>

**Insight:**  
House prices show a right-skewed distribution, meaning a small number of premium properties significantly increase the average price.

---

### 🔹 Area vs Price Relationship
<p align="center">
  <img src="images/area_vs_price.png" width="600">
</p>

**Insight:**  
Living area shows a strong positive relationship with house price — larger houses tend to cost more.

---

### 🔹 Correlation Heatmap
<p align="center">
  <img src="images/correlation_heatmap.png" width="600">
</p>

**Insight:**  
Important observations:

- Living area → strongest influence on price
- Grade → very important feature
- Bathrooms → more impact than bedrooms
- Basement & usable space → increases valuation

---

## 🧹 Data Preprocessing
Key preprocessing steps performed:

- Removed unnecessary columns (ID, Date, coordinates, renovation info)
- Selected relevant numerical features
- Feature–target split
- Train-test split (80% train, 20% test)

This ensures the model learns general patterns rather than memorizing the dataset.

---

## 🤖 Model Training – Linear Regression
A Linear Regression model was trained using multiple independent variables (house features) to predict the target variable Price.

### 🔹 Actual vs Predicted Prices
<p align="center">
  <img src="images/actual_vs_predicted_prices.png" width="600">
</p>

**Insight:**  
The scatter plot shows predicted values closely follow actual values, especially for mid-range properties.

---

## 📈 Model Evaluation & Diagnostics

Metrics used:

- MAE (Mean Absolute Error) → average prediction error
- RMSE (Root Mean Squared Error) → penalizes large errors
- R² Score → how well features explain house price

Model Performance

- MAE ≈ 103,255
- R² Score ≈ 0.74

Interpretation:
The model explains about 74% of price variation, which is a good baseline regression performance for a real estate dataset.

### 🔹 Residual Distribution
<p align="center">
  <img src="images/residual_distribution.png" width="600">
</p>

**Insight:**  
The linear regression assumptions are reasonably satisfied and the model is not strongly biased.

---

## 🧠 Key Learnings

- Living area is the strongest predictor of house price
- Property quality (grade) significantly affects valuation
- More bathrooms and usable space increase price
- Linear Regression provides interpretable results
- Residual analysis is essential before deploying a model

---

## 🛠️ Tools & Technologies
- **Python**
- **pandas, numpy**
- **matplotlib, seaborn**
- **scikit-learn**
- **Jupyter Notebook**

---

## 👤 Author
**Sitaram Dalvi**  
AI / ML Enthusiast | Project Management Professional


