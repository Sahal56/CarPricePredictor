# CarPricePredictor
Title: Car Price Prediction
Aim: To Predict price of Car using machine learning
Tools: Jupyter notebook-python

The price of a car depends on a lot of factors like the goodwill of the brand of the car, features of the car, 
horsepower and the mileage it gives and many more.

Some of the factors that contribute a lot to the price of a car are:
    Brand
    Model
    Mileage
    BHP
    Safety Features
    year of manufacturing kms driven
    many more.

We will clean some data in car.csv and will save new cleaned data into newCar.csv

We will check relationship between features:
    Company with Price
    Year with Price
    kms_driven with Price
    Fuel Type with Price
    Price with FuelType, Year and Company mixed
    
We have chose features of car like name ,company,year of manufacture/purhase, kms driven,fuel type

We will choose DecisionTreeRegressor Algorithm for training
Before that we will use OneHotEncoder for encoding/transforming features into numerical for mathematical computing

Finally we will make pipeline, drop pipe to save model using joblib
Aslo some accuracy, evaluation checking

app.py contain gui interaction model with user 
It uses flask
It loads the model via joblib and make prediction after filling values

