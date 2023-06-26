import streamlit as st
import pickle
import pandas as pd
import sklearn
import numpy as np

pipe = pickle.load(open('model4.pkl','rb'))
st.set_page_config(
    page_title="Diabetics prediction",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title('diabetics_Predictor')


col1, col2 = st.columns(2)

with col1:
	gender = st.number_input('Gender(Male:1,Female:0)')
with col2:
  	age = st.number_input('age:')
col3, col4,col8 = st.columns(3)
with col3:
	hypertension = st.number_input('hypertension:(yes:1,No:0)')
with col4:
	heart_disease = st.number_input('heart_disease:(yes:1,No:0)')
	
col5, col6, col7 = st.columns(3)
with col5:
	smoking_history = st.number_input('smoking_history:(never:4,No Info:0,current:1,not current:5,ever:2,former:3)')
with col6:
	bmi = st.number_input('BMI: ')
with col7: 
	HbA1c_level = st.number_input('HbA1c_level:(range:0-1)')

with col8: 
	blood_glucose_level = st.number_input('blood_glucose_level:(range:0-1)')



if st.button('Predict'):
    input_df = pd.DataFrame({'gender':[gender],'age':[age],'hypertension':[hypertension],'heart_disease':[heart_disease],'smoking_history':[smoking_history],'bmi':[bmi],'HbA1c_level':[HbA1c_level],'blood_glucose_level':[blood_glucose_level]})
    result = pipe.predict(input_df)
    if int(result[0]) == 0:result = "No Diabetics"
    elif int(result[0]) == 1:result = "You have Diabetics"
    st.header("Predicted  - " + result)

st.header("Note: It is only for educational purpose")