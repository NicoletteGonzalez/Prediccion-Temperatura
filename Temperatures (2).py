import numpy as np
import streamlit as st
import pandas as pd

st.write(''' # Prediccion de Temperatura ''')

st.image("Imagenmexico.jpg", caption="Predicción de temperatura en alguna ciudad de Mexico.")

st.header('Datos')

def user_input_features():
  # Entrada
    ciudad = st.selectbox('City:', ciudades)
    mes = st.number_input('Month (1-12):', min_value=1, max_value=12, value=1)
    año = st.number_input('Year:', min_value=1900, max_value=2100, value=2000)

    user_input_data = {
        'City': ciudad,
        'Month': mes,
        'Year': año

          }


  features = pd.DataFrame(user_input_data, index=[0])

  return features

df = user_input_features()
datos =  pd.read_csv(CityTemperatures_df.csv', encoding='latin-1')
X = datos.drop(columns=['a'])
y = datos['AverageTemperature']

from sklearn.linear_model import LinearRegression
LR = LinearRegression()
LR.fit(X, y)

b = LR.coef_
b0 = LR.intercept_
prediccion = (
    b0
    + b[0] * df['hours_studied']
    + b[1] * df['sleep_hours']
    + b[2] * df['attendance_percent']
    + b[3] * df['previous_scores']

)


st.subheader('Prediccion de temperatura')
st.write('La temperatura esperada es ', prediccion)
