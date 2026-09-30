import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.title('Predict California Housing')

a=st.number_input('Choose MedInc Value:')
b=st.number_input('Choose House Age Value:')
c=st.number_input('Choose AveRooms Value:')
d=st.number_input('Choose AVEBedRooms Value:')
e=st.number_input('Choose Population Value:')
f=st.number_input('Choose Ave0ccup Value:')
g=st.number_input('Choose Latitude Value:')
h=st.number_input('Choose Longitude Value:')

if st.button('Predict'):
    m_loaded=joblib.load('californai.joblib')
    model = m_loaded['model']
    columns = m_loaded['columns']
    input=np.array([[a,b,c,d,e,f,g,h]])
    prediction=m_loaded['model'].predict(input)

    st.write('PredictedHouse Value:',prediction[0])


