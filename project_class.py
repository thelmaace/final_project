import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn import preprocessing


loaded_model = pickle.load(open('model.sav', 'rb')) 

def prediction(data):

    df = pd.DataFrame(data) 
    num_data = df.values.reshape(1, -1)

    pred = loaded_model.predict(num_data)

    if pred[0] == 0:  
        return "water is safe for drinking"
    else:
        return "Water is not safe for drinking"
    
def main():

    st.title("Water Potability Predictive Model")
    ph = st.number_input("Ph level is")
    Hardness = st.number_input("Hardness state is")
    Solids = st.number_input("The water state is")
    Chloramines = st.number_input("The Chloramines state is in")
    Sulfate = st.number_input("The sulfate state is")
    Conductivity = st.number_input("What is the Conductivity Level")
    Organic_carbon = st.number_input("What is the Organic carbon range")
    Trihalomethanes = st.number_input("The Trihalomethanes level is")
    Turbidity = st.number_input("What is the Turbidity level")

    Potability = " "

    if st.button("Result"):
        Potability = prediction([ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,
                                 Trihalomethanes,Turbidity
                                 ])
        
        st.success(Potability)

    
if __name__ == "__main__":
    main()



