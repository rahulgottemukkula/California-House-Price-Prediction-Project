# 🏡 California House Price Prediction using Machine Learning

## 📌 Project Overview

This project predicts California house prices using multiple supervised machine learning regression algorithms. The complete machine learning pipeline has been implemented, starting from data preprocessing and feature engineering to model training, hyperparameter tuning, evaluation, model deployment, and a Streamlit web application.

The objective of this project is to compare different regression models and identify the best-performing model for predicting house prices.

---

# 📂 Dataset

- **Dataset:** California Housing Dataset
- **Target Variable:** `median_house_value`

### Features Used

- Longitude
- Latitude
- Housing Median Age
- Total Rooms
- Total Bedrooms
- Population
- Households
- Median Income
- Ocean Proximity

---

# 🚀 Project Workflow

## 1. Data Loading

- Loaded the California Housing dataset
- Explored dataset structure
- Checked data types
- Displayed summary statistics

---

## 2. Exploratory Data Analysis (EDA)

Performed:

- Shape of dataset
- Missing value analysis
- Duplicate value check
- Descriptive statistics
- Correlation analysis
- Feature distributions
- Relationship between features and target variable

---

## 3. Data Preprocessing

### Missing Value Handling

- Identified missing values
- Cleaned the dataset

### Categorical Encoding

- Label Encoding for:
  - Ocean Proximity

### Feature Scaling

Scaled numerical features using preprocessing techniques before training the models.

---

## 4. Feature Engineering

Created new informative features such as:

- Rooms per Household
- Bedrooms per Room
- Population per Household

These engineered features improved model performance.

---

## 5. Train-Test Split

Split the dataset into:

- Training Data (80%)
- Testing Data (20%)

Random State = 42

---

# 🤖 Machine Learning Models Implemented

The following regression algorithms were trained and evaluated:

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

Hyperparameter tuning was also performed to improve model performance.

---

# 📊 Model Evaluation

Models were compared using regression evaluation metrics:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

The best-performing model was selected for deployment.

---

# ⚙️ Hyperparameter Tuning

GridSearchCV was used to optimize model parameters and improve prediction accuracy.

---

# 💾 Model Saving

The final trained model and preprocessing objects were saved using Pickle.

Saved files include:

- california_model.pkl
- scaler.pkl
- encoder.pkl

These files are used during deployment.

---

# 🌐 Streamlit Web Application

A Streamlit application was developed to make predictions interactively.

### User Inputs

- Longitude
- Latitude
- Housing Median Age
- Total Rooms
- Total Bedrooms
- Population
- Households
- Median Income
- Ocean Proximity

The application automatically:

- Performs feature engineering
- Scales numerical features
- Encodes categorical features
- Predicts house price using the trained model

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Libraries

- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost
- Pickle
- Streamlit

---

# 📁 Project Structure

```
California-Housing-Prediction/
│
├── California_Housing_All_Models.ipynb
├── app.py
├── california_model.pkl
├── scaler.pkl
├── encoder.pkl
├── README.md
```

---

# ▶️ How to Run

### Clone Repository

```bash
git clone <repository-link>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit

```bash
streamlit run app.py
```

---

# 📈 Project Highlights

✔ End-to-End Machine Learning Project

✔ Data Cleaning

✔ Exploratory Data Analysis (EDA)

✔ Feature Engineering

✔ Feature Scaling

✔ Label Encoding

✔ Multiple Regression Models

✔ Hyperparameter Tuning

✔ Model Comparison

✔ Model Serialization

✔ Streamlit Deployment

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- Data preprocessing techniques
- Exploratory Data Analysis
- Feature Engineering
- Supervised Machine Learning
- Regression Algorithms
- Hyperparameter Optimization
- Model Evaluation
- Model Deployment using Streamlit
- Building a complete end-to-end ML pipeline

---

# 📧 Author

**Rahul Gottemukkula**

Aspiring AI & Machine Learning Engineer

Skills:
- Python
- SQL
- Machine Learning
- Data Analysis
- Scikit-learn
- XGBoost
- Streamlit
- Pandas
- NumPy
