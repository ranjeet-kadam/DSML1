import streamlit as st

st.title("Welcome to Streamlit application")

name = st.text_input("Enter your Name: ")

if name:
    st.write(f"Hello,{name}")

## Creating a slider
age = st.slider("Select your age : ", 0, 100, 25)
st.write(f"Your age is : {age}")

## Create a select box 
options = ['Python','Java','C++','JS']
choice = st.selectbox("Choose your favourite subject: ",options)
st.write(f"You selected: {choice}") 