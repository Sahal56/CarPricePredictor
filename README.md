# Title: Car Price Prediction

# Description

Aim: To Predict price of Car using machine learning

Tools & libraries: 
- Model Training: Python, Jupyter Notebook, Joblib
- GUI Dashboard : streamlit


## Author

- [SAHAL PATHAN](https://github.com/sahal56)

## Demo
![result-carpredictor](https://github.com/Sahal56/CarPricePredictor/assets/63746256/ab5d56c5-8ef8-4e37-bac6-a39e8c9c408e)

## Deployment
[STREAMLIT-LINK](https://car-pricepredictor-sahal.streamlit.app/)

## Explanation
1. The price of a car depends on a lot of factors like the goodwill of the brand of the car, features of the car, 
horsepower and the mileage it gives and many more.

2. Some of the factors that contribute a lot to the price of a car are:
    - Brand
    - Model
    - Mileage
    - BHP
    - Safety Features
    - year of manufacturing kms driven
    - many more.

3. We will clean some data in car.csv and will save new cleaned data into newCar.csv

4. We will check relationship between features:
    - Company with Price
    - Year with Price
    - kms_driven with Price
    - Fuel Type with Price
    - Price with FuelType, Year and Company mixed
    
5. We have chose features of car like name ,company,year of manufacture/purhase, kms driven,fuel type

6. We will choose DecisionTreeRegressor Algorithm for training
Before that we will use OneHotEncoder for encoding/transforming features into numerical for mathematical computing

7. Finally we will make pipeline, drop pipe to save model using joblib

8. some accuracy, evaluation checking

8. app.py contain gui interaction model with user 
    - It uses flask
    - It loads the model via joblib and make prediction after filling values

## EXTRAS

Install a Virtual Environment `pip install virtualenv`

Use `python<version> -m venv <virtual-environment-name>`

Activate `source env/bin/activate`

Check `pip list`

requirements.txt file :
- `pip freeze > requirements.txt`

- `pip install -r requirements.txt`

Deactivate `deactivate`
