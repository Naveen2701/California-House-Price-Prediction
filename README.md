# California House Price Prediction and Model Deployment

This repository contains files related to California House Price Prediction and the deployment of the trained model using FastAPI.

## Project Overview

In this project, I obtained the California House Price Prediction dataset by CAM NUGENT from Kaggle. The dataset can be found [here](https://www.kaggle.com/datasets/camnugent/california-housing-prices). I used Jupyter Notebook for training the House Price Prediction Model and Deployed it using `FastAPI`.

## Steps Used To Train and Deploy the Model

### Step 1: Data Collection

- Obtained the California House Price Prediction dataset by CAM NUGENT from Kaggle.
- Used Jupyter Notebook to train the House Price Prediction Model.

### Step 2: Training the Model

- Installed all required libraries and modules mentioned in the `requirements.txt` file.
- Imported necessary libraries and modules for data preprocessing and model training.
- Analyzed the data and looked for outliers.
- Checked for null values.
- Performed data preprocessing, including handling skewed distributions and converting categorical data to numerical data.
- Conducted feature engineering.
- Split the preprocessed dataset into train and test sets.
- Scaled/standardized/normalized the features of X_train and X_test.
- Fit the Model using Linear Regression.
- Calculated the evaluation metrics.
- Stored the trained model as a `.pkl` file using Joblib.

### Step 3: Deploy the Saved Model using FastAPI

- Imported all necessary libraries and modules to deploy the model.
- Created a class `model_input(BaseModel)` to post input to the model for prediction.
- Loaded the trained model using Joblib.
- Used `@app.post('/')` to create a website directory.
- Defined a function next to the `@app` to use the variables mentioned in the `model_input` class to predict the house price.
- Returned the house price value in the function.

### Step 4: Starting the FastAPI Server Locally

- Used the following command to start the FastAPI server: `uvicorn ml_api:app`
- `ml_api` is the file name.
- Obtained a URL to interact with the deployed model.

### Step 5: Using the Deployment Service

#### Method 1:

- Accessed http://127.0.0.1:8000/docs to get FastAPI Swagger UI.
- Entered the model parameters manually and posted them using JSON to obtain the output.

#### Method 2:

- Used a Python file to post model input parameters using `JSON` and the `requests` module.

These are all the steps required to train and deploy the California House Price Prediction model. Feel free to explore the repository for more details and files related to this project.
