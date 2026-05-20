# 📩 SMS Spam Detection — Naive Bayes with NLP (TF-IDF)
An end-to-end Natural Language Processing (NLP) classification project that automatically identifies whether an SMS message is Spam or Ham (legitimate) using text processing and a Multinomial Naive Bayes model.  

This project demonstrates a complete NLP workflow:  

Text Cleaning → Feature Extraction (TF-IDF) → Model Training → Probability-based Prediction → Threshold Tuning → Evaluation  

## 📌 Problem Statement
Mobile users receive a large number of unwanted promotional and fraudulent SMS messages.
Manually filtering them is inefficient and error-prone.

The goal of this project is to:

- Automatically classify SMS messages as Spam or Ham
- Detect spam messages with high recall
- Reduce unwanted messages in the inbox
- Understand practical NLP classification workflow

---

## 📊 Dataset Description

The dataset contains real SMS messages labeled as spam or ham.

Target Variable:  
**Class**

- 0 → Ham (Legitimate message)
- 1 → Spam (Unwanted/Promotional/Fraudulent message)

Each record contains:
|Column	|Description|
|-|-|
|Message	|SMS text content|
|Class	|Spam or Ham label|

---

## 📂 Project Structure
08_NLP_&_Naive_Bayes_SMS_spam_detection/<br>
│<br>
├── data/<br>
│   └── Spam_SMS.csv<br>
│<br>
├── notebook/<br>
│   └── NLP_naive_bayes_sms_spam_detection.ipynb<br>
│<br>
└── README.md<br>


---

## 🧹 Text Preprocessing (NLP)

The following preprocessing steps were applied:

- Convert text to lowercase
- Remove punctuation
- Tokenization
- Stopword removal
- Lemmatization
- Removal of empty messages

Purpose:
Clean text helps the model learn meaningful word patterns instead of noise.

---

## 🔤 Feature Extraction — TF-IDF

Text data cannot be directly used by machine learning models.  
TF-IDF (Term Frequency – Inverse Document Frequency) converts words into numerical features based on importance.  

Key settings used:

- Unigrams + Bigrams (1,2)
- Rare word inclusion (min_df = 1)
- Sublinear term frequency scaling

Why TF-IDF?  
It gives higher importance to unique spam-indicator words like:  
free, win, urgent, prize, call now, claim

---

## 🤖 Model Training – K-nearest neaighbors
The Multinomial Naive Bayes classifier was used because it is well-suited for text classification problems.

The model learns:

**Probability (message is spam | words present in message)**

Additional improvements:

- Laplace smoothing (alpha = 0.3)
- Class balancing using class priors
- Probability-based decision making

---

## 🎯 Threshold Tuning

Instead of directly using model predictions, spam classification was controlled using probability:

`y_prob = model.predict_proba(X_test_tfidf)[:,1] `  
`y_pred = (y_prob > 0.45).astype(int)`

Why?
Spam detection prioritizes catching spam (recall) over accuracy.

Lower threshold → Detect more spam
Higher threshold → Fewer false alarms

---

## 📈 Model Evaluation

### Performance Results

- Accuracy ≈ 95%
- Spam Recall ≈ 93%
- Spam Precision ≈ 79%
- Spam F1-Score ≈ 0.85

### Key Observations

- Most spam messages are successfully detected
- Very few spam messages enter inbox
- Some legitimate messages are flagged (acceptable trade-off)

---

## 🧠 Key Learnings

- NLP problems require text preprocessing before modeling
- TF-IDF is effective for classical text classification
- Naive Bayes performs very well on sparse text data
- Accuracy alone is misleading for imbalanced datasets
- Decision threshold strongly affects model behavior
- Spam detection is a recall-focused problem

---

## 🛠️ Tools & Technologies
- **Python**
- **pandas, numpy**
- **nltk**
- **scikit-learn**
- **TF-IDF Vectorizer** 
- **Jupyter Notebook**

---

## 👤 Author
**Sitaram Dalvi**  
AI / ML Enthusiast | Project Management Professional


