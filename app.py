
import streamlit as st 
import pandas as pd
import streamlit as st
import pandas as pd 
import altair as alt

#st.write("HELLO")
#st.write("TOCHUKWU")
#st.write("DONALD")
#st.write("JEMILAT")
#st.write("ROTIMI")

import streamlit as st

st.title("⚽ Football Fans")

# Simple dictionary
fans = {
    "Donald": "Arsenal 🔴",
    "Emmanuel": "Man City 💙",
    "Tochukwu": "Man United 🔴",
    "Rotimi": "Real Madrid 💙"
}

# Buttons in a row
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Donald", use_container_width=True):
        st.session_state.selected = "Donald"
with col2:
    if st.button("Jemilat", use_container_width=True):
        st.session_state.selected = "Jemilat"
with col3:
    if st.button("Tochukwu", use_container_width=True):
        st.session_state.selected = "Tochukwu"
with col4:
    if st.button("Rotimi", use_container_width=True):
        st.session_state.selected = "Rotimi"

st.divider()

if 'selected' in st.session_state:
    st.success(f"✅ {st.session_state.selected} supports {fans[st.session_state.selected]}!")
else:
    st.info("👆 Click on a name to see their football club")
