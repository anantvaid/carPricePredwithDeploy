# Car Price Prediction
# Year - 4 digit number
# Ex Showroom Price (In Lakhs)
# Number of Kilometers
# How many owners had the cars before hand
# Fuel Type of the Car
# Are you Dealer or Individual?
# Transmission Type
# Prediction Value

import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
import pandas as pd

import streamlit as st

from PIL import Image

pickle_in = open('random_forest.pkl','rb')
regressor = pickle.load(pickle_in)
pickle_in.close()

def welcome():
    return 'Welcome All'

def predict_val(S_Price, Kms, noOwners, Year, fuelDiesel, fuelPetrol, sellerType, transmissionType):
    arr = []
    for i in range(Year, Year+3):
        p = regressor.predict([[S_Price, Kms, noOwners, i, fuelDiesel, fuelPetrol, sellerType, transmissionType]])[0]
        arr.append(p)
    return arr

def main():
    st.title("Car Price Predictor")
    html_temp = """
    <div style="background-color:#383e56;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Car Price Predictor App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Year = 2020 - int(st.slider("Year of Manufacture", 1998, 2020))
    S_Price = st.text_input('Ex-Showroom Price (In lakhs)')
    Kms = st.text_input('Kilometers')
    noOwners = int(st.radio('Number of Owners', (0, 1, 2, 3)))
    fuelType = st.selectbox('Fuel Type', ('Petrol', 'Diesel', 'CNG'))
    sellerType = st.selectbox('Seller Type', ('Individual', 'Dealer'))
    transmissionType = st.selectbox('Transmission Type', ('Automatic', 'Manual'))
    fuelPetrol = 1 if fuelType == 'Petrol' else 0
    fuelDiesel = 1 if fuelType == 'Diesel' else 0
    sellerType = 1 if sellerType == 'Individual' else 0
    transmissionType = 1 if transmissionType == 'Manual' else 0
    if st.button('Predict'):
        result = predict_val(S_Price, Kms, noOwners, Year, fuelDiesel, fuelPetrol, sellerType, transmissionType)
        st.success('The Prediction for current year is {} Lakhs'.format(np.round(result[0], 2)))
        if ((result[0] - result[1])>=0.2):
            st.warning('The Prediction for next year is {} Lakhs'.format(np.round(result[1], 2)))
        else:
            st.success('The Prediction for next year is {} Lakhs'.format(np.round(result[1], 2)))
        if ((result[1] - result[2])>=0.3):
            st.error('The Prediction two years later is {} Lakhs'.format(np.round(result[2], 2)))
        else:
            st.warning('The Prediction two years later is {} Lakhs'.format(np.round(result[2], 2)))

if __name__ == '__main__':
    main()