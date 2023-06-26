import streamlit as st
import pickle
import pandas as pd
import sklearn
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Visualization",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title('Diabetics_Visualization')

st.header('1.How data looks like after converting it into dataframe:') 
img = Image.open('1.png')
st.image(img)

st.header('2.Checking for null values in our DataFrame:')
img = Image.open('2.png')
st.image(img)
img = Image.open('4.png')
st.header('3.HeatMap For Correlation Between the varibles')
st.image(img)
img = Image.open('3.png')
st.header('4.Correlation with target variable')
st.image(img)
img = Image.open('5.png')
st.header('5.Smoking History based on Gender:')
st.image(img)
img = Image.open('6.png')
st.header('7.Accuracy:')
st.image(img)
