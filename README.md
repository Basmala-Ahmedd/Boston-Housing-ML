# 🏠 Boston Housing Price Predictor

Predict Boston housing prices using a Decision Tree regression model.  
This project includes data exploration, model training, evaluation, and a Streamlit web app for interactive predictions.


# Project Structure

Boston-Housing-ML/
│
├── data/
│   └── housing.csv          
├── model/
│   └── model.pkl             
│
├── Notebook/
│   ├── boston_housing.ipynb  
│   └── visuals.py            
│
├── app.py                    
├── README.md                 
---

## 📊 Project Overview

This project aims to predict housing prices in Boston based on features such as:

- **RM**: Average number of rooms per dwelling
- **LSTAT**: Percentage of lower status population
- **PTRATIO**: Pupil-teacher ratio in local schools

We use a **Decision Tree Regressor** to predict prices and evaluate model performance using **R² score**.

---

## 📝 Data Exploration

The dataset contains 506 entries with 13 features. The target variable is `MEDV` (Median value of owner-occupied homes in $1000s).  

We analyze the statistics, check for missing values, and observe relationships between features and target.

---

## ⚙️ Model Training

- **Algorithm**: Decision Tree Regressor  
- **Optimization**: GridSearchCV for `max_depth`  
- **Cross-validation**: ShuffleSplit with 10 splits, 20% test size  
- **Performance metric**: R² Score  

The optimal model achieved reliable predictions across training and testing sets.

---

## 🌐 Streamlit Web Application

You can interact with the model using a Streamlit web app. Enter house features to get instant price predictions.

![Boston Housing App](Notebook/images/Streamlit.png)

**Example Input & Predictions:**

| Feature | Client 1 | Client 2 | Client 3 |
| --- | --- | --- | --- |
| Rooms | 5 | 4 | 8 |
| Poverty (%) | 17 | 32 | 3 |
| PTRATIO | 15 | 22 | 12 |

**Predicted Selling Prices:**

- Client 1: $419,700.00  
- Client 2: $287,100.00
- Client 3: $927,500.00

These results align with expectations: bigger houses in better neighborhoods have higher predicted prices.

---
📄 Notes

Make sure model/model.pkl exists before running the app.

The app uses integer inputs for Rooms, Poverty %, and PTRATIO for simplicity.

Prediction is instant and does not require loading the full dataset.