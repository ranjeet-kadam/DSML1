import streamlit as st
import pandas as pd 
import numpy as np

## Title for the application
st.title("Hello Streamlit")

## Display the information using simple text
st.write("This is simple text")

## Create a Dataframe

df = pd.DataFrame({
    'name':['Adi','Mohit','Alfredo'],
    'id':[1,2,3],
    'Organiztion':['Deolite','HCL Tech','KPMG']
})

## Display the dataframe

st.write("Here is th data")
st.write(df)

### Create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

## Display the chart
st.write("This is line chart")
st.line_chart(chart_data)