import streamlit as st

# Input suhu dan satuan
x = st.number_input("Masukkan nilai suhu")
sx = st.text_input("Satuan awal", "C")
st.write("Nilai suhu", x, ' ', sx)
sy = st.text_input("Satuan tujuan", "C")

# Inisialisasi hasil konversi
y = 0

# Konversi suhu berdasarkan satuan awal dan tujuan
if sx == 'C':
    if sy == 'C':
        y = x  # Tidak ada perubahan
    elif sy == 'F':
        y = x * 9/5 + 32  # Konversi dari Celsius ke Fahrenheit
    elif sy == 'K':
        y = x + 273.15  # Konversi dari Celsius ke Kelvin
elif sx == 'F':
    if sy == 'C':
        y = (x - 32) * 5/9  # Konversi dari Fahrenheit ke Celsius
    elif sy == 'F':
        y = x  # Tidak ada perubahan
    elif sy == 'K':
        y = (x - 32) * 5/9 + 273.15  # Konversi dari Fahrenheit ke Kelvin
elif sx == 'K':
    if sy == 'C':
        y = x - 273.15  # Konversi dari Kelvin ke Celsius
    elif sy == 'F':
        y = (x - 273.15) * 9/5 + 32  # Konversi dari Kelvin ke Fahrenheit
    elif sy == 'K':
        y = x  # Tidak ada perubahan
else:
    st.write("Satuan yang dimasukkan tidak valid. Gunakan 'C', 'F', atau 'K'.")

# Menampilkan hasil konversi
st.write(x, ' ', sx, ' = ', y, sy)
