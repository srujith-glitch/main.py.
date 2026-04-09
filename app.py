import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Success Stacker Ultimate", page_icon="🌐", layout="wide")

# Styling for a clean, non-boring look
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #e0e0e0; }
    .stButton>button { background: linear-gradient(45deg, #00c6ff, #0072ff); color: white; border: none; }
    .resource-card { background-color: #1a1f29; padding: 15px; border-radius: 10px; border-left: 5px solid #00c6ff; margin-bottom: 10px; }
    .alert-card { background-color: #2d1b1b; padding: 15px; border-radius: 10px; border-left: 5px solid #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. INTERNET SYNC FUNCTIONS ---
def get_live_market():
    # Example: Tracking Bitcoin as a proxy for your 1.5L tech goal
    try:
        res = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=inr")
        return res.json()['bitcoin']['inr']
    except: return "Check Connection"

# --- 2. SIDEBAR NAVIGATION ---
st.sidebar.title("🎯 Stacker Menu")
app_mode = st.sidebar.selectbox("Go to:", ["Dashboard", "80kg Fitness Program", "Exam & Answer Vault", "Cyber Security & AI"])

# --- 3. DASHBOARD SECTION ---
if app_mode == "Dashboard":
    st.title("🚀 Your Daily Mission")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Live Goal Tracking")
        st.write(f"**Current Bitcoin Price:** ₹{get_live_market()}")
        st.info("💡 Keep an eye on the market—this is your 1.5L bike motivation!")
        
        st.subheader("Daily Non-Negotiables")
        st.checkbox("🌅 Hostel Workout (No Equipment)")
        st.checkbox("📖 1-3-7 Revision (Day 1, 3, or 7 logic)")
        st.checkbox("📘 Reading 'How to Win Friends'")

    with col2:
        st.markdown('<div class="alert-card">', unsafe_allow_html=True)
        st.subheader("⚠️ Exam Focus")
        st.write("Mid-1 Recap:")
        st.write("- BEE: 8/25 (Needs Diagrams)")
        st.write("- Chemistry: 14/25 (Needs Eqns)")
        st.markdown('</div>', unsafe_allow_html=True)

# --- 4. 80KG FITNESS PROGRAM ---
elif app_mode == "80kg Fitness Program":
    st.title("⚖️ Path to 80kg")
    
    # Weight Progress
    weight = st.slider("Current Weight (kg)", 80, 120, 105)
    st.progress((120 - weight) / (120 - 80))
    st.write(f"You are **{weight - 80}kg** away from your goal!")

    # Dynamic Exercise Library
    day = datetime.now().strftime("%A")
    st.subheader(f"Today's Routine: {day}")
    
    with st.expander("Show Exercise Instructions"):
        if day in ["Monday", "Wednesday", "Friday"]:
            st.write("1. **Incline Push-ups:** 3 sets of 15 (Hands on bed)")
            st.write("2. **Backpack Squats:** 3 sets of 20 (Fill bag with books)")
            st.write("3. **Wall Sits:** 3 sets of 45 seconds")
        else:
            st.write("1. **Burpees:** 3 sets of 10")
            st.write("2. **Plank:** 3 sets of 1 minute")
            st.write("3. **Walking:** 30 minutes around hostel campus")

# --- 5. EXAM & ANSWER VAULT ---
elif app_mode == "Exam & Answer Vault":
    st.title("📚 JNTU Resources & D-E-D-P Answers")
    
    st.subheader("Quick Links (Updates via Internet)")
    st.markdown('''
    <div class="resource-card">
        <a href="https://www.jntufastupdates.com/" target="_blank">🔗 JNTU Official Question Banks</a><br>
        <a href="https://www.youtube.com/results?search_query=bee+thevenin+theorem+simplified" target="_blank">🎥 BEE Video Tutorials</a>
    </div>
    ''', unsafe_allow_html=True)

    # D-E-D-P Material Template
    st.subheader("Create a D-E-D-P Note")
    topic = st.text_input("Topic Name")
    col1, col2 = st.columns(2)
    with col1:
        st.text_area("Definition")
        st.text_area("Equations")
    with col2:
        st.file_uploader("Upload Diagram Photo")
        st.text_area("Key Points (Bullets)")

# --- 6. CYBER SECURITY & AI ---
elif app_mode == "Cyber Security & AI":
    st.title("🛡️ The 'Stacker' Career Path")
    st.info("Focusing on these skills is how you earn the 1.5L.")
    st.write("1. **Linux Basics:** Essential for Cyber Sec.")
    st.write("2. **Python Automation:** Use your Python skills to automate security tasks.")
    st.write("3. **AI Prompting:** Use AI to explain complex DS code.")
