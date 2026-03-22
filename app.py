
import streamlit as st 
import pandas as pd
import streamlit as st
import pandas as pd 
import altair as alt


import streamlit as st


import streamlit as st
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Lagos LG Explorer",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for beautiful styling
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Header styling */
    .gradient-header {
        background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.98) 100%);
        padding: 2rem 3rem;
        border-radius: 30px;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.3);
    }
    
    .header-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    
    .header-subtitle {
        font-size: 1.1rem;
        color: #4a5568;
        margin-top: 0.5rem;
    }
    
    /* Card styling */
    .info-card {
        background: white;
        padding: 1.5rem;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 1rem;
        border: 1px solid #e2e8f0;
    }
    
    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }
    
    /* 3-dots button styling */
    .three-dots-container {
        position: relative;
        display: inline-block;
    }
    
    .three-dots-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
        padding: 12px 20px;
        border-radius: 50px;
        cursor: pointer;
        font-size: 1.2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        color: white;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .three-dots-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Dropdown menu styling */
    .dropdown-menu {
        position: absolute;
        top: 100%;
        right: 0;
        background: white;
        min-width: 280px;
        max-height: 400px;
        overflow-y: auto;
        border-radius: 15px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        margin-top: 10px;
        z-index: 1000;
        animation: slideDown 0.3s ease-out;
        border: 1px solid #e2e8f0;
    }
    
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .dropdown-item {
        padding: 12px 20px;
        cursor: pointer;
        transition: all 0.2s ease;
        border-bottom: 1px solid #f0f0f0;
        color: #2d3748;
        font-size: 0.95rem;
    }
    
    .dropdown-item:hover {
        background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%);
        padding-left: 25px;
        color: #667eea;
    }
    
    .dropdown-header {
        padding: 12px 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        border-radius: 15px 15px 0 0;
        position: sticky;
        top: 0;
        z-index: 1;
    }
    
    /* Statistics cards */
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    
    /* Search box styling */
    .search-box {
        margin-bottom: 1.5rem;
    }
    
    .search-box input {
        width: 100%;
        padding: 12px 20px;
        border: 2px solid #e2e8f0;
        border-radius: 50px;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .search-box input:focus {
        outline: none;
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    /* Animation for LG items */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .lg-item {
        animation: fadeInUp 0.5s ease-out;
    }
    </style>
""", unsafe_allow_html=True)

# Complete list of Local Governments in Lagos
lagos_lgs = [
    "Agege", "Ajeromi-Ifelodun", "Alimosho", "Amuwo-Odofin", "Apapa",
    "Badagry", "Epe", "Eti-Osa", "Ibeju-Lekki", "Ifako-Ijaiye",
    "Ikeja", "Ikorodu", "Kosofe", "Lagos Island", "Lagos Mainland",
    "Mushin", "Ojo", "Oshodi-Isolo", "Shomolu", "Surulere"
]

# LG data with additional info
lg_data = {
    "Agege": {"population": "459,939", "area": "11.2 km²", "chairman": "Hon. Ganiyu Egunjobi"},
    "Ajeromi-Ifelodun": {"population": "1,000,000+", "area": "12.2 km²", "chairman": "Hon. Fatai Ayoola"},
    "Alimosho": {"population": "1,288,714", "area": "137.8 km²", "chairman": "Hon. Jelili Sulaimon"},
    "Amuwo-Odofin": {"population": "318,166", "area": "134.6 km²", "chairman": "Hon. Valentine Buraimoh"},
    "Apapa": {"population": "217,362", "area": "26.7 km²", "chairman": "Hon. Idowu Senbanjo"},
    "Badagry": {"population": "241,093", "area": "441 km²", "chairman": "Hon. Olusegun Onilude"},
    "Epe": {"population": "181,409", "area": "965 km²", "chairman": "Hon. Adedoyin Adesanya"},
    "Eti-Osa": {"population": "287,785", "area": "192.3 km²", "chairman": "Hon. Saheed Bankole"},
    "Ibeju-Lekki": {"population": "117,481", "area": "455 km²", "chairman": "Hon. Sesan Olowa"},
    "Ifako-Ijaiye": {"population": "427,878", "area": "26.3 km²", "chairman": "Hon. Oloruntoba Oke"},
    "Ikeja": {"population": "313,196", "area": "46.2 km²", "chairman": "Hon. Mojeed Balogun"},
    "Ikorodu": {"population": "535,619", "area": "394.5 km²", "chairman": "Hon. Wasiu Adesina"},
    "Kosofe": {"population": "665,393", "area": "84.3 km²", "chairman": "Hon. Moyosore Ogunlewe"},
    "Lagos Island": {"population": "209,437", "area": "8.7 km²", "chairman": "Hon. Adeola Aro"},
    "Lagos Mainland": {"population": "317,720", "area": "19.6 km²", "chairman": "Hon. Omolola Essien"},
    "Mushin": {"population": "633,009", "area": "17.5 km²", "chairman": "Hon. Emmanuel Bamigboye"},
    "Ojo": {"population": "598,071", "area": "158 km²", "chairman": "Hon. Rasheed Idowu"},
    "Oshodi-Isolo": {"population": "621,509", "area": "44.8 km²", "chairman": "Hon. Kehinde Oloyede"},
    "Shomolu": {"population": "402,449", "area": "11.6 km²", "chairman": "Hon. Ganiyu Kolawole"},
    "Surulere": {"population": "503,975", "area": "23 km²", "chairman": "Hon. Bamidele Yusuf"}
}

# Initialize session state for dropdown visibility
if 'show_dropdown' not in st.session_state:
    st.session_state.show_dropdown = False
if 'search_term' not in st.session_state:
    st.session_state.search_term = ""

# Header section
st.markdown("""
    <div class="gradient-header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <div class="header-title">
                    🏙️ Lagos LG Explorer
                </div>
                <div class="header-subtitle">
                    Discover the 20 Local Government Areas of Lagos State
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Create three columns for statistics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div class="stat-card">
            <div class="stat-number">20</div>
            <div class="stat-label">Local Governments</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="stat-card">
            <div class="stat-number">3,577+</div>
            <div class="stat-label">km² Total Area</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="stat-card">
            <div class="stat-number">20M+</div>
            <div class="stat-label">Population</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="stat-card">
            <div class="stat-number">57</div>
            <div class="stat-label">LCDAs</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Create two columns for main content
col_left, col_right = st.columns([2, 1])

with col_left:
    # 3-dots button with dropdown
    st.markdown("""
        <div style="position: relative;">
            <button class="three-dots-btn" id="dropdownBtn">
                ⋯ View All Local Governments
            </button>
        </div>
    """, unsafe_allow_html=True)
    
    # JavaScript for dropdown toggle
    st.markdown("""
        <script>
        const btn = document.getElementById('dropdownBtn');
        let dropdownOpen = false;
        
        btn.addEventListener('click', function() {
            dropdownOpen = !dropdownOpen;
            if (dropdownOpen) {
                createDropdown();
            } else {
                removeDropdown();
            }
        });
        
        function createDropdown() {
            const dropdown = document.createElement('div');
            dropdown.className = 'dropdown-menu';
            dropdown.id = 'lgDropdown';
            
            const header = document.createElement('div');
            header.className = 'dropdown-header';
            header.innerHTML = '📌 All 20 Local Governments in Lagos';
            dropdown.appendChild(header);
            
            const lgs = """ + str(lagos_lgs) + """;
            lgs.forEach(lg => {
                const item = document.createElement('div');
                item.className = 'dropdown-item';
                item.innerHTML = '📍 ' + lg;
                item.onclick = () => {
                    console.log('Selected:', lg);
                    removeDropdown();
                };
                dropdown.appendChild(item);
            });
            
            btn.parentNode.appendChild(dropdown);
        }
        
        function removeDropdown() {
            const existing = document.getElementById('lgDropdown');
            if (existing) {
                existing.remove();
            }
        }
        
        // Close dropdown when clicking outside
        document.addEventListener('click', function(event) {
            if (!btn.contains(event.target)) {
                removeDropdown();
                dropdownOpen = false;
            }
        });
        </script>
    """, unsafe_allow_html=True)
    
    # Alternative: Streamlit native dropdown with button
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Create a beautiful expander as alternative
    with st.expander("📋 Click here to see all 20 Local Governments", expanded=False):
        # Search functionality
        search_term = st.text_input("🔍 Search LG", placeholder="Type to filter...", key="lg_search")
        
        # Filter LGs based on search
        filtered_lgs = [lg for lg in lagos_lgs if search_term.lower() in lg.lower()] if search_term else lagos_lgs
        
        # Display LGs in a grid
        cols = st.columns(4)
        for idx, lg in enumerate(filtered_lgs):
            with cols[idx % 4]:
                st.markdown(f"""
                    <div class="lg-item" style="padding: 10px; margin: 5px; background: #f8fafc; border-radius: 10px; border-left: 4px solid #667eea;">
                        <strong>📍 {lg}</strong>
                    </div>
                """, unsafe_allow_html=True)
        
        st.markdown(f"<p style='text-align: center; margin-top: 20px; color: #667eea;'>📊 Showing {len(filtered_lgs)} of {len(lagos_lgs)} Local Governments</p>", unsafe_allow_html=True)
    
    # Featured LG information
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🌟 Featured Local Governments")
    
    # Create tabs for featured LGs
    tab1, tab2, tab3 = st.tabs(["🏙️ Alimosho", "🌊 Eti-Osa", "🏛️ Ikeja"])
    
    with tab1:
        st.markdown("""
            <div class="info-card">
                <h3 style="color: #667eea;">Alimosho</h3>
                <p><strong>📊 Population:</strong> 1,288,714 (Largest by population)</p>
                <p><strong>🗺️ Area:</strong> 137.8 km²</p>
                <p><strong>👤 Chairman:</strong> Hon. Jelili Sulaimon</p>
                <p><strong>✨ Known for:</strong> Largest LG in Lagos, vibrant markets, and residential areas</p>
            </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
            <div class="info-card">
                <h3 style="color: #667eea;">Eti-Osa</h3>
                <p><strong>📊 Population:</strong> 287,785</p>
                <p><strong>🗺️ Area:</strong> 192.3 km²</p>
                <p><strong>👤 Chairman:</strong> Hon. Saheed Bankole</p>
                <p><strong>✨ Known for:</strong> Lekki, Victoria Island, upscale neighborhoods, and business district</p>
            </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
            <div class="info-card">
                <h3 style="color: #667eea;">Ikeja</h3>
                <p><strong>📊 Population:</strong> 313,196</p>
                <p><strong>🗺️ Area:</strong> 46.2 km²</p>
                <p><strong>👤 Chairman:</strong> Hon. Mojeed Balogun</p>
                <p><strong>✨ Known for:</strong> State capital, Murtala Muhammed Airport, Government House</p>
            </div>
        """, unsafe_allow_html=True)

with col_right:
    st.markdown("### 📊 Quick Stats")
    
    # Create a simple bar chart using pandas
    lg_population_data = {lg: int(data['population'].replace('+', '').replace(',', '').split()[0]) 
                          for lg, data in lg_data.items() 
                          if data['population'].replace('+', '').replace(',', '').split()[0].isdigit()}
    
    df_pop = pd.DataFrame(list(lg_population_data.items()), columns=['LG', 'Population'])
    df_pop = df_pop.sort_values('Population', ascending=False).head(10)
    
    st.bar_chart(df_pop.set_index('LG'))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 🗺️ LG Areas")
    st.info("""
    **Top 5 Largest LGs by Area:**
    1. Epe - 965 km²
    2. Ibeju-Lekki - 455 km²
    3. Badagry - 441 km²
    4. Ikorodu - 394.5 km²
    5. Alimosho - 137.8 km²
    """)
    
    st.markdown("### 💡 Did You Know?")
    st.success("""
    Lagos State is divided into 20 Local Government Areas (LGAs) and 
    57 Local Council Development Areas (LCDAs) for effective administration 
    and development.
    """)

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 20px; color: #6c757d;">
        <p>🏙️ Lagos LG Explorer | Data as of 2024 | Source: Lagos State Government</p>
        <p style="font-size: 0.85rem;">Click the "⋯ View All Local Governments" button or expander to see the complete list</p>
    </div>
""", unsafe_allow_html=True)

# JavaScript to handle the 3-dots button properly
st.markdown("""
    <script>
    // Function to handle dropdown toggle with Streamlit
    function setupDropdown() {
        const btn = document.querySelector('.three-dots-btn');
        if (btn && !btn.hasListener) {
            btn.hasListener = true;
            btn.addEventListener('click', function(e) {
                e.stopPropagation();
                const existing = document.getElementById('lgDropdown');
                if (existing) {
                    existing.remove();
                } else {
                    const dropdown = document.createElement('div');
                    dropdown.className = 'dropdown-menu';
                    dropdown.id = 'lgDropdown';
                    
                    const header = document.createElement('div');
                    header.className = 'dropdown-header';
                    header.innerHTML = '📌 All 20 Local Governments in Lagos';
                    dropdown.appendChild(header);
                    
                    const lgs = """ + str(lagos_lgs) + """;
                    lgs.forEach(lg => {
                        const item = document.createElement('div');
                        item.className = 'dropdown-item';
                        item.innerHTML = '📍 ' + lg;
                        item.onclick = () => {
                            console.log('Selected:', lg);
                            dropdown.remove();
                        };
                        dropdown.appendChild(item);
                    });
                    
                    btn.parentNode.appendChild(dropdown);
                }
            });
            
            document.addEventListener('click', function(e) {
                if (!btn.contains(e.target)) {
                    const existing = document.getElementById('lgDropdown');
                    if (existing) {
                        existing.remove();
                    }
                }
            });
        }
    }
    
    // Run setup when page loads
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', setupDropdown);
    } else {
        setupDropdown();
    }
    </script>
""", unsafe_allow_html=True)


import streamlit as st
#Here’s a simple starter code for a Streamlit app that displays a title, a sidebar for user input, and shows results dynamically:
import streamlit as st


#In Streamlit, you can mimic a 3-dot menu button (like an options menu) using st.button or st.selectbox. Here’s a neat way to implement it:
import streamlit as st

st.title("Three Dot Menu Example")

# Create a 3-dot style button using selectbox
option = st.selectbox(
    "⋮",  # Unicode for vertical ellipsis (three dots)
    ["Select an option", "Settings", "Help", "Logout"]
)

# Handle actions
if option == "Settings":
    st.info("You opened Settings.")
elif option == "Help":
    st.info("Here’s some help information.")
elif option == "Logout":
    st.warning("You clicked Logout.")





import streamlit as st
import streamlit as st
from PIL import Image
import base64
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
