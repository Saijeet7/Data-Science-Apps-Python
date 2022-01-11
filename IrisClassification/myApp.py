import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
#Simple Iris Flower Prediction App

This app predict the Iris flower type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('sepal_length',4.3,7.9,5.4)
    sepal_width = st.sidebar.slider('sepal_width',2.0,4.4,3.4)
    petal_length = st.sidebar.slider('petal_length',1.0,6.9,1.3)
    petal_width = st.sidebar.slider('petal_width',0.1,2.5,0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features =pd.DataFrame(data, index=[0])
    return features