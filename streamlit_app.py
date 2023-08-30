import streamlit as st

st.title("Find the Largest Number")

num1 = st.number_input("Enter the first number:", value=0)
num2 = st.number_input("Enter the second number:", value=0)
num3 = st.number_input("Enter the third number:", value=0)

if st.button("Find Largest"):
    largest = max(num1, num2, num3)
    st.write(f"The largest number is: {largest}")
