import streamlit as st

st.title('Posyandu Balita Bunda')
st.write("Keterangan")

umur = st.number_input("Masukan umur anak= ", 0)
tinggi = st.number_input("Masukan tinggi anak=", 0)
berat = st.number_input("Masukan berat anak=", 0)
selanjutnya = st.button("lanjut")
if selanjutnya :
    umur == 1
    berat < 3
    st.write("kurang gizi")
