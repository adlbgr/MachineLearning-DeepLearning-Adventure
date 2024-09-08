import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import streamlit as st

df= pd.read_excel('cars.xls')
X = df.drop('Price', axis=1)
y = df['Price']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

preprocessor = ColumnTransformer(
    transformers=[
        ('num',StandardScaler(),['Mileage','Doors','Cylinder','Liter']),
        ('cat',OneHotEncoder(),['Make','Model','Type'])
    ]

)
model = LinearRegression()

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', model)
])

pipeline.fit(x_train, y_train)
pred = pipeline.predict(x_test)

rmse=  mean_squared_error(pred, y_test)**.5
r2 =  r2_score( pred,y_test)

def price_pred(Make,Model,Trim,Type,Cylinder,Liter, Doors,Cruise, Sound, Leather, Mileage):
    input_data = pd.DataFrame({
        'Make': [Make],
        'Model': [Model],
        'Trim': [Trim],
        'Type': [Type],
        'Cylinder': [Cylinder],
        'Liter': [Liter],
        'Doors': [Doors],
        'Cruise': [Cruise],
        'Sound': [Sound],
        'Leather': [Leather],
        'Mileage': [Mileage]
    })

    prediction = pipeline.predict(input_data)[0]
    return prediction

st.title('Car Price Prediction with MLOps :red_car:')
st.write('This app predicts the price of a car based on the features of the car.')

def main():
    make = st.selectbox('Make', df['Make'].unique())
    model = st.selectbox('Model', df[df['Make']== make ]['Model'].unique())
    trim = st.selectbox('Trim', df[(df['Model']== model ) & (df['Make']== make)]['Trim'].unique())
    mileage = st.number_input('Mileage', min_value=0,max_value= 1000000)
    car_type = st.selectbox('Type', df['Type'].unique())
    cylinder = st.selectbox('Cylinder', df['Cylinder'].unique())
    liter = st.number_input('Liter', min_value=0.0, max_value=10.0)
    doors = st.number_input('Doors', min_value=2, max_value=5)
    cruise = st.radio('Cruise', [0,1])
    sound = st.radio('Sound', [0,1])
    leather = st.radio('Leather', [0,1])


    if st.button('Predict'): 
        price = price_pred(make, model, trim, car_type, cylinder, liter, doors, cruise, sound, leather, mileage)
        st.info(f'The predicted price of the car is ${price:2f}')
        st.balloons()
if __name__ == '__main__':
    main()
