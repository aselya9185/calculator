import streamlit as st
import json
import requests

# Create a title for the calculator
st.title("Engineering Calculator")

# Create a text input for the mathematical expression
expression_input = st.text_input("Enter a mathematical expression", value="", key="expression")

# Create a variable to store the expression
expression = expression_input

# Add CSS to increase the width of the buttons
st.markdown("""
    <style>
    .stButton > button {
        width: 100px;
    }
    </style>
""", unsafe_allow_html=True)

# Create a column layout for the operands
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

# Create buttons for the operands
with col1:
    st.button("sqrt")
    st.button("sin")
    st.button("7")
    st.button("4")
    st.button("1")

with col2:
    st.button("x^2")
    st.button("cos")
    st.button("8")
    st.button("5")
    st.button("2")

with col3:
    st.button("x^3")
    st.button("tan")
    st.button("9")
    st.button("6")
    st.button("3")

with col4:
    st.button("log")
    st.button("(")
    st.button("*")
    st.button("+")
    st.button("0")

with col5:
    st.button("ln")
    st.button(")")
    st.button("/")
    st.button("-")
    ans_button = st.button("ans")

# Create a button to clear the expression
if st.button("Clear"):
    expression = ""
    st.session_state.expression_input = ""

# Display the whole expression
st.write("Expression:", expression)

# Create a button to calculate the expression
if ans_button:
    try:
        inputs = {"expression": expression}
        res = requests.post(url="http://127.0.0.1:8000/calculate", data=json.dumps(inputs))
        result = res.json()["result"]
        st.write("Result:", result)
    except Exception as e:
        st.write("Error:", str(e))




# # converting the inputs to json
# inputs = {"operation": option, "x": x, "y": y}
#
# # when the user clicks on button it will fetch the API
# if st.button("Calculate"):
#     res = requests.post(url = "http://127.0.0.1:8000/calculate", data = json.dumps(inputs))
#
#     if res.status_code == 200:
#         st.subheader(f"Response from API = {res.text}")
#     else:
#         st.subheader(f"Response from API = {res.status_code}")