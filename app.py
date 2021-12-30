import streamlit as st
import pickle
import numpy as np
import pandas as pd


bike_df = pickle.load(open('bike_new1_df.pkl','rb'))
bike_pipe= pickle.load(open('bike_pipe.pkl','rb'))
car_df= pickle.load(open('car_df.pkl','rb'))
car_pipe= pickle.load(open('car_pipe.pkl','rb'))

st.title("Used Vehicle price predictor")
decision = st.selectbox("Choose Your Category",['bike','car'])

#if user select bike then show bike feature

if decision =='bike':

    #bike name
    Bike_name =st.selectbox("Bike Model", bike_df['bike_name'].unique())

    # city
    City= st.selectbox("City", bike_df['city'].unique())

    # kms
    Kms_driven = st.number_input(label="kms driven")

    # bike age
    Age = st.number_input("Age")

    # bike power
    Power = st.number_input("Engine CC")

    # brand
    Brand = st.selectbox("Brand", bike_df['brand'].unique())

    #pass value to model
    if st.button('pridict price'):
        st.title('Selling price would be '+str(int(bike_pipe.predict(pd.DataFrame([[Bike_name,City,Kms_driven,Age,Power,Brand]],columns=['bike_name', 'city', 'kms_driven', 'age', 'power', 'brand']))[0])))









else:
    # car name
    Car_Name = st.selectbox("Car Name", car_df['car_name'].unique())

    # min cost price
    Car_minprice = st.number_input(label="Minimum New Car Price ")

    # max cost price
    Car_maxprice = st.number_input(label="Maximum New Car Price ")

    # car age
    Car_age = st.number_input(label="Car Age ")

    # car age
    Car_km = st.number_input(label="Kms Driven ")

    # car seller
    Car_seller = st.selectbox("seller", car_df['seller_type'].unique())

    # car fuel
    Car_fuel = st.selectbox("Fuel", car_df['fuel_type'].unique())

    # car tranmission
    Car_tranmission = st.selectbox("Tranmission Type", car_df['transmission_type'].unique())

    # car 	mileage
    Car_mileage = st.number_input(label="Mileage")

    # car 	engine
    Car_engine = st.number_input(label="Engine in cc")

    # car 	power
    Car_power = st.number_input(label="power in bhp")

    # car 	seat
    Car_seat = st.number_input(label="Seats")
    if st.button('pridict price'):
        st.title('Selling price would be ' + str(int(car_pipe.predict( pd.DataFrame([[Car_Name,Car_minprice,Car_maxprice,Car_age,Car_km,Car_seller,Car_fuel,Car_tranmission,Car_mileage,Car_engine,Car_power,Car_seat]], columns=['car_name','min_cost_price','max_cost_price','vehicle_age','km_driven','seller_type','fuel_type','transmission_type','mileage','engine','max_power','seats']))[0])))



