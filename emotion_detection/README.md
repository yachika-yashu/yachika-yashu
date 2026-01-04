# Twitter Sentiment Analysis (Happiness vs Sadness)

This project implements an end-to-end **binary sentiment classification pipeline** on Twitter data, focusing on distinguishing between **happiness** and **sadness**.
The notebook emphasizes **clean preprocessing, careful evaluation, and reproducible experimentation**, rather than black-box accuracy chasing.

---

## 🧠 Problem Definition

Given the text of a tweet, predict whether the expressed emotion is:

* **Happiness (1)**
* **Sadness (0)**

The task is framed as a binary classification problem to establish a strong and interpretable baseline before extending to multi-class emotion detection.

---

## 📂 Dataset

* Source: Public Twitter emotion dataset
* Original columns:

  * `tweet_id`
  * `sentiment`
  * `content`
* Processing steps:

  * Removed `tweet_id`
  * Filtered to **happiness** and **sadness**
  * Encoded labels (`happiness → 1`, `sadness → 0`)
  * Removed very short or noisy tweets

Final dataset is balanced enough to allow meaningful precision and recall analysis.

---

## 🛠️ Tech Stack

* **Python**
* **Pandas / NumPy** – data manipulation
* **NLTK** – stopword removal and lemmatization
* **scikit-learn**

  * Train–test split
  * Bag of Words (CountVectorizer)
  * Evaluation metrics
* **XGBoost** – gradient boosted decision trees

---

## 🧹 Text Preprocessing

Each tweet undergoes the following normalization steps:

* Lowercasing
* URL removal
* Punctuation and digit removal
* Stopword removal
* Lemmatization
* Removal of very short texts (noise reduction)



## 🔬 Modeling Approach

### Feature Engineering

* **Bag of Words (CountVectorizer)**

  * Unigrams and bigrams
  * Vocabulary size capped to reduce sparsity and overfitting

### Model

* **XGBoost Classifier**

  * Handles high-dimensional sparse features well
  * Subsampling enabled to improve generalization
  * Tuned for balanced performance rather than maximum accuracy

### Train/Test Split

* 80/20 split
* **Stratified** to preserve class distribution

---

## 📊 Results

**Overall Performance**

* **Accuracy:** 0.77
* **Precision:** 0.80
* **Recall:** 0.71
* **ROC AUC:** 0.86

**Classification Report**

```
              precision    recall  f1-score   support

           0       0.75      0.83      0.79      1060
           1       0.80      0.71      0.75      1015

    accuracy                           0.77      2075
   macro avg       0.77      0.77      0.77      2075
weighted avg       0.77      0.77      0.77      2075
```

### Interpretation

* The model achieves a **strong ROC-AUC (0.86)**, indicating good class separability.
* Precision is higher than recall for the *happiness* class, meaning predictions are reliable but somewhat conservative.
* Performance is well-balanced across classes, suggesting no severe bias toward one sentiment.

---

## 📓 Notebook Structure

The notebook follows a clear experimental flow:

1. Data loading and filtering
2. Text cleaning and normalization
3. Train–test split
4. Feature extraction (Bag of Words)
5. Model training (XGBoost)
6. Model evaluation

Each step is designed to be readable, debuggable, and extensible.

---

## 🚀 How to Run

1. Clone the repository
2. Open the notebook
3. Run cells sequentially from top to bottom

All dependencies are standard Python ML libraries.

---

## 🔮 Future Improvements

* Compare Bag of Words with **TF-IDF**
* Add a **Logistic Regression** baseline
* Perform cross-validated hyperparameter tuning
* Extend to **multi-class emotion classification**
* Track experiments using DVC or MLflow

---

## ✨ Key Takeaways

This project demonstrates:

* Practical NLP preprocessing decisions
* Awareness of data leakage and evaluation pitfalls
* Balanced metric-driven model assessment
* Clean notebook organization suitable for experimentation

---

### Final recruiter subtext (important)

This README quietly signals that you:

* understand **why** each step exists,
* evaluate models responsibly,
* and treat ML as an iterative scientific process.

That subtext is exactly what turns a notebook into a **portfolio artifact**, not just a school exercise.

