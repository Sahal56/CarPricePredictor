import streamlit as st
import joblib
import pandas as pd
import numpy as np

model=joblib.load(open('CarPricePredictor','rb'))
car=pd.read_csv('newCar.csv')

st.title('Car Price Predictor')
st.subheader('Select the details')

col1, col2, col3, col4 = st.columns(4)

with col1:
   companies=sorted(car['company'].unique())
   company = st.selectbox("Company:", companies)

with col2:
   car_models=sorted(car[car.name.str.startswith(company)]['name'].unique())
   car_model = st.selectbox("Model:", car_models)

with col3:
    years=sorted(car['year'].unique(),reverse=True)
    year = st.selectbox("Year:", years)

with col4:
    fuels=car['fuel_type'].unique()
    fuel_type = st.selectbox("Fuel Type:", fuels)
    
driven = st.number_input('Kilometres travelled:')

if st.button('Predict'):
    if not car_model or not company or not year or not driven or not fuel_type:
        st.warning('Select Properly')
    else:
        st.balloons()
        prediction=model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                          data=np.array([car_model,company,year,driven,fuel_type]).reshape(1, 5)))
        prediction=prediction[0].astype(str)
        st.text('₹ ' + prediction)

