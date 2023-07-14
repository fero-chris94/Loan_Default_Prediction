# Loan Default Prediction

## Introduction
This project focuses on predicting loan defaults using a logistic regression model. The aim is to help identify customers who are more likely to default on their loans based on various factors such as age, income, homeownership, employment length, loan intent, and loan grade. The model is trained on a dataset and deployed as a web application for easy prediction.

### Dataset
The project utilizes a dataset named "cr_loan2.csv". It contains information about customers and their loan details. The dataset is loaded using Pandas and explored to gain insights into the data.

## Exploratory Data Analysis
Several exploratory data analysis (EDA) techniques are employed to understand the dataset and visualize relationships between variables. The EDA techniques used include:

- Histogram: The distribution of loan amounts is visualized using a histogram.
- Scatter Plot: The relationship between personal income and age is plotted as a scatter plot.
- Cross Tabulation: Cross tabulation is performed on loan intent, loan status, home ownership, and loan grade to analyze their relationships.
- Box Plot: A box plot is created to examine the percentage of income by loan status.
- Null Value Handling: Null values in the dataset are identified and handled appropriately.

## Feature Engineering
Feature engineering is performed to prepare the dataset for model training. The following steps are taken:

- Selecting Numerical Features: Numerical features are separated from the dataset.
- Selecting Categorical Features: Categorical features are separated from the dataset.
- One-Hot Encoding: Categorical features are one-hot encoded to convert them into numerical representation.
- Concatenation: Numerical and encoded categorical features are concatenated to form the final dataset.

## Model Training
The logistic regression model is chosen for predicting loan default. The dataset is split into training and testing sets using the train_test_split function. The logistic regression model is then trained on the training set.

## Model Evaluation
The trained model is evaluated using various metrics to assess its performance. The following evaluation techniques are employed:

- Accuracy Score: The accuracy score is calculated to measure the model's performance on the testing set.
- Classification Report: The classification report is generated to obtain metrics such as precision, recall, and F1-score for each class.
- Receiver Operating Characteristic (ROC) Curve: The ROC curve is plotted to visualize the model's performance in terms of sensitivity and specificity.
- Area Under the Curve (AUC): The AUC score is calculated to quantify the overall performance of the model.
- Confusion Matrix: The confusion matrix is created to analyze the model's predictions in terms of true positives, true negatives, false positives, and false negatives.

## Web Application
The trained logistic regression model is deployed as a web application using the Streamlit library. The web application allows users to input customer information such as age, income, homeownership, employment length, loan intent, and loan grade. Based on the inputs, the model predicts the likelihood of loan default for the customer.

Files
The project repository includes the following files:

- credit_loan_default.ipynb: Jupyter Notebook containing the project code and EDA analysis.
- app.py: Python script for the loan default prediction web application.
- model.joblib: Saved trained logistic regression model
- cr_loan2.csv: Dataset used for training and analysis

## Usage
To run the loan default prediction web application locally, follow these steps:

- Install the required libraries: pip install -r requirements.txt.
- Run the Python script: python app.py.
- Access the web application through the provided local URL.

## Conclusion
The Loan Default Prediction project demonstrates the use of a logistic regression model to predict the likelihood of loan default. By analyzing various customer attributes, the model provides insights into the risk associated with lending to specific customers. The web application further enhances the usability of the model by allowing real-time predictions based on user inputs.

For more details and code implementation, please refer to the Jupyter Notebook file (jupyter_file.ipynb) and Python script file (python_file.py) in this repository.
