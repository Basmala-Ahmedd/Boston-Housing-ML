🏠 Boston Housing Price Predictor

Predict Boston housing prices using a machine learning model trained on the Boston Housing Dataset. This app allows users to enter key features of a house and get an instant prediction of its selling price.

# Project Structure

Boston-Housing-ML/
│
├── data/
│   └── housing.csv           # Boston Housing Dataset
│
├── model/
│   └── model.pkl             # Trained Decision Tree model
│
├── notebook/
│   ├── boston_housing.ipynb  # Jupyter notebook with data exploration, model training and evaluation
│   └── visuals.py            # Supplementary plotting functions for notebook
│
├── app.py                    # Streamlit web application
├── README.md                 # Project documentation


# Features Used

The model predicts house prices based on three key features:

Feature	Description
RM	Average number of rooms per dwelling
LSTAT	Percentage of lower status population (poverty level)
PTRATIO	Student-Teacher ratio in local schools

# Usage

Run Jupyter Notebook

Explore the dataset, train models, and evaluate performance:

jupyter notebook notebook/boston_housing.ipynb
Run Streamlit App

Launch the web application:

streamlit run app.py

Enter the house features: Rooms (RM), Poverty % (LSTAT), Pupil-Teacher Ratio (PTRATIO).

Click Predict Price to see the predicted selling price.

The app will display a metric box with the predicted price and provide insights about the range.

# Model Details

Algorithm: Decision Tree Regressor

Hyperparameter Optimization: GridSearchCV to find the optimal max_depth

Performance Metric: R² Score (Coefficient of Determination)

# Example Predictions

Client	Rooms	Poverty %	PTRATIO	Predicted Price
1	5	17	15	$424,935
2	4	32	22	$284,200
3	8	3	12	$933,975

The model logically predicts higher prices for bigger houses in better neighborhoods and lower prices for smaller houses in poorer neighborhoods.

# Future Improvements

Add more features from the dataset, e.g., crime rate, proximity to employment centers, or property age.

Implement other regression models (Random Forest, Gradient Boosting) for potentially higher accuracy.

Deploy the Streamlit app online using Streamlit Cloud or Heroku for public access.

# Author

Basmala Ahmed – Machine Learning Engineer Nanodegree Project

# License

This project is licensed under the MIT License – see the LICENSE
 file for details