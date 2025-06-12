import streamlit as st      
user_input = st.text_input("Enter something:")

if user_input:
    st.write("You entered:", user_input)