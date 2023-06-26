import streamlit as st
import pickle
import pandas as pd
import sklearn
import numpy as np

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)
st.title("Main Page")
st.sidebar.success("Select a page above.")

st.write('Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Glucose is your body’s main source of energy. Your body can make glucose, but glucose also comes from the food you eat.')

st.write('Insulin is a hormone made by the pancreas that helps glucose get into your cells to be used for energy. If you have diabetes, your body doesn’t make enough—or any—insulin, or doesn’t use insulin properly. Glucose then stays in your blood and doesn’t reach your cells.')

st.write('Diabetes raises the risk for damage to the eyes, kidneys, nerves, and heart. Diabetes is also linked to some types of cancer. Taking steps to prevent or manage diabetes may lower your risk of developing diabetes health problems.')

st.write('Over time, high blood glucose can damage your heart, kidneys, feet, and eyes. If you have diabetes, you can take steps to lower your chances of developing diabetes health problems by taking steps to improve your health and learning how to manage the disease. Managing your blood glucose, blood pressure, and cholesterol levels can help prevent future health problems.')