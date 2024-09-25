import streamlit as st

x = st.number_input("Masukkan nilai suhu")
sx = st.text_input("Satuan awal", "C")
st.write("Nilai suhu", x, ' ', sx)
sy = st.text_input("Satuan tujuan", "C")
y = 0

if (sx == 'C'):
    if sy == 'C':
        y = x  
    elif (sy == 'F'):
        y = x * 9/5 + 32 
    elif (sy == 'K'):
        y = x + 273.15 
    elif (sy == 'R'):
        y = x * 4/5
elif (sx == 'F'):
    if (sy == 'C'):
        y = (x - 32) * 5/9 
    elif (sy == 'F'):
        y = x  
    elif (sy == 'K'):
        y = (x - 32) * 5/9 + 273.15 
    elif (sy == 'R'):
        y = (x - 32) * 4/9
elif (sx == 'K'):
    if (sy == 'C'):
        y = x - 273.15  
    elif (sy == 'F'):
        y = (x - 273.15) * 9/5 + 32  
    elif (sy == 'K'):
        y = x 
    elif (sy == 'R'):
        y = (x - 273.15) * 4/5
elif (sx == 'R'):
    if (sy == 'C'):
        y = x * 5/4  
    elif (sy == 'F'):
        y = x * 9/4 + 32  
    elif (sy == 'K'):
        y = x * 5/4 + 273.15  
    elif (sy == 'R'):
        y = x
else:
    st.write("Satuan yang dimasukkan tidak valid. Gunakan 'C', 'F', 'K', atau 'R'.")

st.write(x, ' ', sx, ' = ', y, sy)
