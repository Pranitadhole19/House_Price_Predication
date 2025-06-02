### House Price Prediction Web App Using Flask
I built and trained a machine learning model to predict house prices based on inputs like location, square footage, number of bathrooms, and BHK. After training the model in a Jupyter notebook, I saved it using pickle and then created a Flask web app where users can input data and see the predicted house price.

### Project Overview
- I used a dataset with house-related features to train a regression model from Kaggle.
- The model was saved as a .pkl file so it can be reused without retraining.
- I created a simple web form where users can enter details like location, total area, bathrooms, and BHK.
- The Flask app takes the input, sends it to the model, and displays the predicted price on the same page.

### Files Included
- Train_Model.ipynb – used to train and save the model
- app.py – Flask code to load the model and handle prediction
- templates/index.html – basic HTML form for user input
- house_price_model.pkl – saved regression model

### Requirements
- scikit-learn  
- pandas  
- numpy  
- flask

### Steps Involved in the Project
#### 1. Model Training
- Load the dataset and select the necessary features.
- Use LabelEncoder to convert location to numerical format.
- Train a regression model using scikit-learn.
- Save the trained model using pickle so it can be used later.

#### 2. Building the Web App
- Use Flask to create a simple backend.
- Load the saved model when the app starts.
- Create an HTML form for user input.
- When the form is submitted, collect the input values and format them for prediction.
- Use the model to predict the price and show the result on the page.



