import streamlit as st

st.title("Basit Kare Hesaplayıcı")

number = st.number_input("Bir sayı girin:", min_value=0)

square = number ** 2

st.write(f"Girdiğiniz sayının karesi: {square}")