import streamlit as st
import json
import requests

st.title("Basic Calculator App")

# taking user inputs
option = st.selectbox("What operation you want to perform?",
                      ('Addition', 'Subtraction', 'Multiplication', 'Division'))

st.write("")
st.write("Select the numbers from slider below")
x = st.slider("X", 0, 100, 20)
y = st.slider("Y", 0, 130, 10)

# converting the inputs to json
inputs = {"operation": option, "x": x, "y": y}

# when the user clicks on button it will fetch the API
if st.button("Calculate"):
    res = requests.post(url = "http://127.0.0.1:8000/calculator", data = json.dumps(inputs))

    st.subheader(f"Response from API = {res.text}")