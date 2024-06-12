import streamlit as st
import joblib
import pandas as pd
import numpy as np

# with st.sidebar:
#     add_radio = st.text("Created by SAHAL PATHAN")


@st.cache_data  # 👈 Add the caching decorator
def GetData():
    model=joblib.load(open('./models/CarPricePredictor','rb'))
    car=pd.read_csv('./datasets/newCar.csv')
    companies=sorted(car['company'].unique())
    fuels=car['fuel_type'].unique()
    years=sorted(car['year'].unique(),reverse=True)
    return model,car,companies,fuels,years

model,car,companies,fuels,years = GetData()

# Emoji for car :{}: car or oncoming_automobile
st.title('Car :red[Price] Predictor :oncoming_automobile:')
st.divider()

st.subheader('Select the details')

colA1, colA2, colA3 = st.columns(3)

with colA1:
   company = st.selectbox("Company :man-shrugging:", companies)

with colA2:
    year = st.selectbox("Year :date:", years)

with colA3:
    fuels=sorted(car[car.name.str.startswith(company)]['fuel_type'].unique())
    fuel_type = st.selectbox("Fuel Type :oil_drum:", fuels)

colB1, colB2 = st.columns(2)

with colB1:
    car_models = sorted(car[car.name.str.startswith(company)]['name'].unique())
    car_model = st.selectbox("Model :diamond_shape_with_a_dot_inside:", car_models)

with colB2:
    driven = st.number_input(label='Kilometres travelled :motorway:', min_value=1, max_value=1000000)


if st.button('Predict :money_with_wings:'):
    if not car_model or not company or not year or not driven or not fuel_type:
        st.warning('Select Properly')
    else:
        st.balloons()
        ipData = pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                          data=np.array([car_model,company,year,driven,fuel_type]).reshape(1, 5))
        prediction = model.predict(ipData)
        prediction = prediction[0].astype(str)
        # print(type(prediction[0]))

        st.divider()
        st.markdown("**Value** of Your :red[Car] is :blue-background[ ₹ " + prediction + " :moneybag:]")

