import streamlit as st
import time
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Success Stacker: Engineering Edition", page_icon="⚡", layout="wide")

# Initialize Session State
if 'task_step' not in st.session_state:
    st.session_state.task_step = 1
if 'search_history' not in st.session_state:
    st.session_state.search_history = []

# Styling
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #e0e0e0; }
    .calc-box { background-color: #1e293b; padding: 20px; border-radius: 15px; border: 1px solid #38bdf8; }
    .step-math { color: #fbbf24; font-family: monospace; font-size: 18px; }
    .time-badge { background-color: #00c6ff; color: black; padding: 4px 10px; border-radius: 8px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: SEARCH & HISTORY ---
st.sidebar.title("🔍 Study Portal")
doubt = st.sidebar.text_input("Doubt (e.g., KVL Calculation):")
if st.sidebar.button("Search & Save"):
    if doubt:
        url = f"https://www.google.com/search?q={doubt.replace(' ', '+')}+step+by+step+solution"
        st.session_state.search_history.append({"query": doubt, "url": url})
        st.sidebar.markdown(f"[View Solution]({url})")

# --- NAVIGATION ---
menu = st.sidebar.radio("Go to:", ["🏠 Command Center", "🔢 Problem Solver (Math)", "📚 Subject Vault", "🏋️ Fitness & Moto"])

# --- 1. COMMAND CENTER ---
if menu == "🏠 Command Center":
    st.title("⚡ Mission Sequence")
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown('<span class="time-badge">18:00 - 20:00</span> **Practice 5 BEE Numerical Problems**', unsafe_allow_html=True)
    with col2:
        if st.session_state.task_step == 1:
            if st.button("APPROVE ✅"):
                st.balloons()
                st.success("Congratulations! Calculation skills leveled up.")
                st.session_state.task_step += 1
                time.sleep(1)
                st.rerun()
        else: st.write("✅ Task Finished")

# --- 2. PROBLEM SOLVER (THE CALCULATOR) ---
elif menu == "🔢 Problem Solver (Math)":
    st.title("⚡ BEE Numerical Solver")
    st.write("Use this to verify your homework or practice problems.")
    
    calc_type = st.selectbox("Select Calculation", ["Ohm's Law (V=IR)", "Electrical Power (P=VI)", "Series Resistance"])
    
    st.markdown('<div class="calc-box">', unsafe_allow_html=True)
    if calc_type == "Ohm's Law (V=IR)":
        st.subheader("Ohm's Law Calculator")
        i = st.number_input("Enter Current (I) in Amps", value=0.0)
        r = st.number_input("Enter Resistance (R) in Ohms", value=0.0)
        if st.button("Calculate Voltage"):
            v = i * r
            st.markdown(f"### Result: {v} Volts")
            st.markdown(f"**Steps:**")
            st.markdown(f'<p class="step-math">V = I × R</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="step-math">V = {i} × {r} = {v}V</p>', unsafe_allow_html=True)

    elif calc_type == "Electrical Power (P=VI)":
        st.subheader("Power Calculator")
        v = st.number_input("Enter Voltage (V)", value=0.0)
        i = st.number_input("Enter Current (I)", value=0.0)
        if st.button("Calculate Power"):
            p = v * i
            st.markdown(f"### Result: {p} Watts")
            st.markdown(f'<p class="step-math">P = V × I = {v} × {i} = {p}W</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 3. SUBJECT VAULT (DIAGRAMS) ---
elif menu == "📚 Subject Vault":
    st.title("📖 D-E-D-P Master Section")
    sub = st.selectbox("Select Subject", ["BEE", "Chemistry"])
    
    if sub == "BEE":
        st.header("Topic: Single Phase Transformer")
        st.write("**Definition:** A static device that transfers electrical energy from one circuit to another through electromagnetic induction.")
        
        st.subheader("Diagram Requirement")
        st.info("⚠️ MUST DRAW: Core, Primary Winding, Secondary Winding, and Magnetic Flux Lines.")
        # Visual Aid for student
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Transformer_ideal.svg/1200px-Transformer_ideal.svg.png", width=400, caption="Core Diagram Reference")
        
        st.subheader("Equation")
        st.latex(r"E = 4.44 \cdot f \cdot N \cdot \Phi_m")
        st.write("Where f=frequency, N=number of turns, Φm=maximum flux.")

# --- 4. FITNESS & MOTO ---
elif menu == "🏋️ Fitness & Moto":
    st.title("🏍️ Goal: Yamaha FZ-X")
    st.image("https://www.yamaha-motor-india.com/theme/v3/images/fzx/color/matte-copper.png", use_container_width=True)
    st.markdown("### Process: 100kg → 80kg")
    st.write("1. **Incline Pushups:** 3 Sets x 15 Reps")
    st.write("2. **Squats:** 3 Sets x 20 Reps")
