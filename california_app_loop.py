import streamlit as st
import numpy as np
import pandas as pd
import joblib
###############################
obj=joblib.load('californai.joblib')
model=obj['model']
cols=obj['columns']
###########################################
st.title('Predict California Housing')
In=[]
for i in cols:
    v=st.number_input(f'enter the {i} value')
    In.append(v)
if st.button('Click'):
    
    out=model.predict([In])
    st.success(out)