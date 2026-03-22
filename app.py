
import streamlit as st 
import pandas as pd
import streamlit as st
import pandas as pd 
import altair as alt


import streamlit as st

st.set_page_config(
    page_title="My App",
    page_icon="📊",
    layout="wide"
)

# Header with navigation
st.markdown("""
    <style>
    .compact-header {
        background: white;
        padding: 1rem 2rem;
        border-bottom: 3px solid #667eea;
        margin-bottom: 2rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .logo {
        font-size: 1.5rem;
        font-weight: bold;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .nav-links {
        display: flex;
        gap: 2rem;
    }
    
    .nav-link {
        text-decoration: none;
        color: #4a5568;
        font-weight: 500;
        transition: color 0.3s ease;
        cursor: pointer;
    }
    
    .nav-link:hover {
        color: #667eea;
    }
    
    .user-info {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .avatar {
        width: 40px;
        height: 40px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
    }
    </style>
    
    <div class="compact-header">
        <div class="nav-container">
            <div class="logo">
                📊 FUTURE DATA ANALYST
            </div>
            <div class="nav-links">
                <span class="nav-link">Dashboard</span>
                <span class="nav-link">Analytics</span>
                <span class="nav-link">Reports</span>
                <span class="nav-link">Settings</span>
            </div>
            <div class="user-info">
                <span>ROTIMI</span>
                <div class="avatar">JD</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

import streamlit as st

st.title("⚽ Football Fans")

# Simple dictionary
fans = {
    "Donald": "Arsenal 🔴",
    "Jemilat": "Man City 💙",
    "Tochukwu": "Man United 🔴",
    "Rotimi": "Real Madrid  👑",
    "Muinat": "Man United 💙",
    "Ayobami": "Barcelona 🔴 "


}

# Buttons in a row
col1, col2, col3, col4, col5, col6 = st.columns(6)

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
with col5:
    if st.button("Muinat", use_container_width=True):
        st.session_state.selected = "Muinat"
with col6:
    if st.button("Ayobami", use_container_width=True):
        st.session_state.selected = "Ayobami"

st.divider()

if 'selected' in st.session_state:
    st.success(f"✅ {st.session_state.selected} supports {fans[st.session_state.selected]}!")
else:
    st.info("👆 Click on a name to see their football club")
