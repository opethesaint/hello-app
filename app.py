
import streamlit as st 
import pandas as pd
import streamlit as st
import pandas as pd 
import altair as alt

#

st.write("HELLO")
st.write("TOCHUKWU")
st.write("DONALD")
st.write("JEMILAT")
st.write("ROTIMI")
import streamlit as st

# Set page title
st.set_page_config(page_title="Nigerian States", page_icon="")

# Title
st.title("🇳🇬 Nigerian States & Capitals")

# Dictionary of states and their capitals
states_info = {
    "Abia": "Umuahia", "Adamawa": "Yola", "Akwa Ibom": "Uyo", "Anambra": "Awka",
    "Bauchi": "Bauchi", "Bayelsa": "Yenagoa", "Benue": "Makurdi", "Borno": "Maiduguri",
    "Cross River": "Calabar", "Delta": "Asaba", "Ebonyi": "Abakaliki", "Edo": "Benin City",
    "Ekiti": "Ado-Ekiti", "Enugu": "Enugu", "Gombe": "Gombe", "Imo": "Owerri",
    "Jigawa": "Dutse", "Kaduna": "Kaduna", "Kano": "Kano", "Katsina": "Katsina",
    "Kebbi": "Birnin Kebbi", "Kogi": "Lokoja", "Kwara": "Ilorin", "Lagos": "Ikeja",
    "Nasarawa": "Lafia", "Niger": "Minna", "Ogun": "Abeokuta", "Ondo": "Akure",
    "Osun": "Oshogbo", "Oyo": "Ibadan", "Plateau": "Jos", "Rivers": "Port Harcourt",
    "Sokoto": "Sokoto", "Taraba": "Jalingo", "Yobe": "Damaturu", "Zamfara": "Gusau",
    "FCT (Abuja)": "Abuja"
}

# Create 3 columns for buttons
cols = st.columns(3)

# Display buttons
for idx, (state, capital) in enumerate(states_info.items()):
    col_idx = idx % 3
    with cols[col_idx]:
        if st.button(state, key=f"btn_{state}", use_container_width=True):
            st.session_state.selected_state = state
            st.session_state.selected_capital = capital

# Initialize session state
if 'selected_state' not in st.session_state:
    st.session_state.selected_state = None
    st.session_state.selected_capital = None

# Display results
st.divider()

if st.session_state.selected_state:
    col1, col2 = st.columns(2)
    
    with col1:
        st.success(f"🏙️ **State:** {st.session_state.selected_state}")
    
    with col2:
        st.info(f"🏛️ **Capital:** {st.session_state.selected_capital}")
    
    if st.button("🔄 Clear Selection"):
        st.session_state.selected_state = None
        st.session_state.selected_capital = None
        st.rerun()
else:
    st.info("👆 Click on any state to see its capital")
