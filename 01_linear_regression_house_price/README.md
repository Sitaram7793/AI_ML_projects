## 🏠 House Price Prediction using Multiple Linear Regression

Real estate pricing is influenced by multiple factors such as property size, construction quality, location, and property age.
This project builds a Multiple Linear Regression model to estimate housing prices using structural, location, and lifestyle features.

The goal of the project is to:

- Understand which features truly affect house prices
- Build an interpretable regression model
- Perform feature engineering & preprocessing
- Evaluate model performance using regression metrics

This project focuses not only on prediction, but also on data analysis and real-world business interpretation.

---

### 📊 Dataset

The dataset contains residential housing information.  
Each row represents a house and columns describe its physical, location, and environmental characteristics.
 
| Feature                  | Description                        |
| ------------------------ | ---------------------------------- |
| living area              | Total usable interior living space |
| lot area                 | Total land area                    |
| number of bedrooms       | Bedrooms in the house              |
| number of bathrooms      | Bathrooms in the house             |
| floors                   | Number of floors                   |
| grade of the house       | Construction/design quality rating |
| condition of the house   | Overall property condition         |
| waterfront present       | Whether house faces water          |
| number of views          | Scenic view rating                 |
| basement area            | Basement usable area               |
| Latitude / Longitude     | Property location                  |
| Built Year               | Construction year                  |
| Renovation Year          | Last renovation year               |
| Distance from airport    | Distance to nearest airport        |
| Number of schools nearby | Nearby schools                     |
| Price                    | Target variable (house price)      |

---

### 📂 Project Structure

01_linear_regression_house_price/  
│  
|── data/  
│   ├── House Price India.csv    
|  
├── images/  
│   ├── actual_vs_predicted_prices.png    
│   ├── area_vs_price.png    
│   ├── correlation_heatmap.png    
│   ├── price_distribution.png    
│   ├── residual_distribution.png    
│  
├── notebook/  
│   ├── linear_regression_house_price.ipynb 
|  
└── README.md  

---

### 📊 Exploratory Data Analysis (EDA)

#### 🔹 Price Distribution
<p align="center">
  <img src="images/price_distribution.png" width="600">
</p>

#### 🔹 Area vs Price
<p align="center">
  <img src="images/area_vs_price.png" width="600">
</p>

#### 🔹 Correlation Heatmap
<p align="center">
  <img src="images/correlation_heatmap.png" width="600">
</p>

---

### Data preprocessing and feature engineering

#### 1. Removed Irrelevant Columns
'id',' Date', 'Postal Code', 'living_area_renov', 'lot_area_renov'  

#### 2. Feature Engineering

Instead of using year values directly, meaningful features were created:
- house_age = current_year - built_year
- renovation_age = current_year - renovation_year

Why?
Because models understand age better than raw years.

#### 3. Log Transformation (Most Important Step)

House prices were right-skewed. Linear regression assumes normally distributed residuals. So the target variable was transformed:

`y = log(Price)`

After prediction:

Price = exp(predicted_log_price)

This significantly improved model performance.

#### 4. Feature Scaling

Standardization was applied:

`StandardScaler()`

Why needed?
Linear Regression minimizes squared distances. Different feature magnitudes (area vs bathrooms) distort coefficient estimation.

#### 6. Train Test Split
- 80% Training
- 20% Testing
- random_state = 42

---

### 🤖 Model Training
Linear Regression
  - Baseline predictive model
  - Simple & interpretable

--- 

### 📏 Model Performance
MAE: 0.196  
RMSE: 0.065  
R² Score: 0.77  

The model explains 77% of the variation in housing prices.   

### 📈 Key Analytical Insights

#### Property characteristics (Primary drivers)

- Living area is the strongest predictor of price
- House grade significantly increases valuation
- Bathrooms positively influence price
- Above-ground usable area matters more than land area
- Basement adds value but less than main living space

#### Location influence

- Latitude strongly affects house price
- Same-size houses vary in price due to neighborhood prestige
- Location acts as a hidden premium factor

#### Property age impact

- Older houses sell cheaper
- Recently renovated houses command higher prices
- Renovation offsets depreciation

#### Premium features

- Waterfront properties increase value
- Scenic views increase price
- Construction grade matters more than maintenance condition

#### Weak factors

- Distance from airport has little impact
- Nearby schools show weak influence in this dataset

#### Market behavior

- Price distribution is right-skewed
- Majority homes are mid-range
- Few luxury houses create outliers
- Similar houses can have different prices due to quality and location

---

### Conclusion

Multiple Linear Regression successfully estimates housing prices when meaningful features such as size, quality, age, and location are engineered correctly.  

Applying log transformation improved model reliability and stabilized predictions.  
However, luxury homes remain difficult to predict due to intangible factors like neighborhood prestige and interior quality.  

---

### 🛠️ Tools & Technologies

- Python
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- Jupyter Notebook

---

### 👤 Author

Sitaram Dalvi  
AI / ML Enthusiast | Project Management Professional  
