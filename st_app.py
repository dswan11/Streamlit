import streamlit as st
st.write("Hello there")
x = st.slider("Pick a number", 1, 10, 1)
#st.number_input("enter a number")
x_sq = x * x
'***Title***'
st.write("The number squared is:")
st.write(x_sq)