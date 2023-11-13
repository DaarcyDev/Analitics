
import streamlit as st
import pandas as pd
 
st.write("""
# My first app
# Liam Alvarez Peralta N.C: 19091253
Hello *world!*
""")
 
df = pd.read_csv("housing.csv")

st.line_chart(df["population"])
