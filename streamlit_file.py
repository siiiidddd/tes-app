import streamlit as st

st.title('Posyandu Balita Bunda')
st.header("Aplikasi pendeteksi kurang gizi pada anak dibawah 1 tahun")
st.write("Posyandu merupakan kependekan dari Pos Pelayanan Terpadu, merupakan Lembaga Kemasyarakatan Desa/Kelurahan (LKD/LKK) sebagai wadah partisipasi masyarakat yang bertugas membantu Kepala Desa/Lurah dalam peningkatan pelayanan social dasar termasuk bidang kesehatan.")
st.write("5 langkah pelayanan pada Posyandu, yaitu:")
st.write("Pendaftaran")
st.write("Pengukuran dan Penimbangan")
st.write("Pencatatan")
st.write("Penyuluhan Kesehatan")
st.write("Jika tertulis keterangan 'true' berarti kurang gizi, jika tertulis 'false' maka gizi tidak kurang")

umur = st.number_input("Masukan umur anak(bulan)= ", 0)
tinggi = st.number_input("Masukan tinggi anak=", 0)
berat = st.number_input("Masukan berat anak=", 0)

if umur == 1 :
    berat == 0
    st.write("kurang gizi")
if umur == 1 :
    berat == 1
    st.write("kurang gizi")
if umur == 1 :
    berat == 2
    st.write("kurang gizi")
if umur == 2 :
    berat < 4
    st.write("Kurang gizi")
if umur == 3 :
    berat < 4
    st.write("Kurang gizi")
if umur == 4 :
    berat < 5
    st.write("Kurang gizi")
if umur == 5 :
    berat < 6
    st.write("Kurang gizi")

