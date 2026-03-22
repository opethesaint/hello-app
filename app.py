
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
                <span class="nav-link">Analytics</span>
                <span class="nav-link">Reports</span>
            </div>
            <div class="user-info">
                <span>ROTIMI</span>
                <div class="avatar">ORR</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

import streamlit as st
import streamlit as st

# Configure page
st.set_page_config(
    page_title="My App",
    page_icon="✨",
    layout="wide"
)

# Beautiful header with gradient text
st.markdown("""
    <style>
    .gradient-header {
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .gradient-header h1 {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .gradient-header p {
        font-size: 1.2rem;
        color: #2c3e50;
        margin-top: 0.5rem;
    }
    </style>
    <div class="gradient-header">
        <h1>✨ My Awesome App</h1>
        <p>Transforming ideas into insights</p>
    </div>
""", unsafe_allow_html=True)


import streamlit as st
from PIL import Image
import base64

st.set_page_config(
    page_title="My App",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS for modern header
st.markdown("""
    <style>
    /* Modern header styling */
    .modern-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem 2rem;
        border-radius: 0 0 20px 20px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        position: relative;
        overflow: hidden;
    }
    
    .modern-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 1%, transparent 1%);
        background-size: 50px 50px;
        animation: shimmer 20s linear infinite;
    }
    
    @keyframes shimmer {
        0% {
            transform: translate(0,0);
        }
        100% {
            transform: translate(50px,50px);
        }
    }
    
    .header-content {
        position: relative;
        z-index: 1;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    
    .title-section h1 {
        color: white;
        font-size: 2.5rem;
        margin: 0;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    
    .title-section p {
        color: rgba(255,255,255,0.9);
        margin: 0.5rem 0 0 0;
        font-size: 1rem;
    }
    
    .stats {
        display: flex;
        gap: 2rem;
    }
    
    .stat-item {
        text-align: center;
        background: rgba(255,255,255,0.2);
        padding: 0.5rem 1rem;
        border-radius: 10px;
        backdrop-filter: blur(10px);
    }
    
    .stat-number {
        color: white;
        font-size: 1.5rem;
        font-weight: bold;
        display: block;
    }
    
    .stat-label {
        color: rgba(255,255,255,0.8);
        font-size: 0.8rem;
    }
    </style>
""", unsafe_allow_html=True)

# Create header
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
        <div class="title-section">
            <h1>🚀 EID MUBARAK</h1>
            <p>Happy Celebration</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="stats">
            <div class="stat-item">
                <span class="stat-number">1.2K+</span>
                <span class="stat-label">Users</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">99.9%</span>
                <span class="stat-label">Uptime</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="modern-header"><div class="header-content">', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

import streamlit as st

st.set_page_config(
    page_title="My App",
    page_icon="🎨",
    layout="wide"
)

# Animated header with CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .animated-header {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%);
        border-radius: 30px;
        margin-bottom: 2rem;
        animation: fadeInUp 0.8s ease-out;
        position: relative;
        overflow: hidden;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .animated-header h1 {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        animation: slideIn 0.5s ease-out;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .animated-header p {
        font-size: 1.2rem;
        color: #5a6e8a;
        max-width: 600px;
        margin: 0 auto;
        animation: fadeIn 1s ease-out 0.3s both;
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    
    .wave {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 100px;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="rgba(255,255,255,0.3)" fill-opacity="1" d="M0,96L48,112C96,128,192,160,288,160C384,160,480,128,576,122.7C672,117,768,139,864,154.7C960,171,1056,181,1152,165.3C1248,149,1344,107,1392,85.3L1440,64L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path></svg>') repeat-x;
        background-size: cover;
        animation: wave 20s linear infinite;
    }
    
    @keyframes wave {
        0% {
            background-position-x: 0;
        }
        100% {
            background-position-x: 1440px;
        }
    }
    </style>
    
    <div class="animated-header">
        <div class="wave"></div>
        <h1>🌟 Welcome to Rotimi Streamlit Hub</h1>
        <p>Your gateway to powerful data analytics and visualization</p>
    </div>
""", unsafe_allow_html=True)

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
