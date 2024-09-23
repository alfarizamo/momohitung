import streamlit as st

x = st.number_input("Masukkan nilai suhu")
sx = st.text_input("Satuan awal (C/F/K)", "C")
sy = st.text_input("Satuan tujuan (C/F/K)", "C")

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "C":
        if to_unit == "F":
            return value * 9/5 + 32
        elif to_unit == "K":
            return value + 273.15
    elif from_unit == "F":
        if to_unit == "C":
            return (value - 32) * 5/9
        elif to_unit == "K":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "K":
        if to_unit == "C":
            return value - 273.15
        elif to_unit == "F":
            return (value - 273.15) * 9/5 + 32
    return None

result = convert_temperature(x, sx.upper(), sy.upper())

if result is not None:
    st.write(f"{x} {sx.upper()} = {result:.2f} {sy.upper()}")
else:
    st.write("Satuan yang dimasukkan tidak valid. Gunakan C, F, atau K.")
