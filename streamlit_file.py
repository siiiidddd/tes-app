import streamlit as st

st.write('hello world')
umur = st.number_input("Masukan umur= ", 0)
usia = st.button("lanjut")
if usia :
sidan = umur
st.write("Umur=",sidan)