import streamlit as st
import time
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="Success Stacker: Ultimate Master", page_icon="🏍️", layout="wide")

# 2. State Management (Crucial for Approval Logic & Navigation)
if 'task_step' not in st.session_state:
    st.session_state.task_step = 1
if 'search_history' not in st.session_state:
    st.session_state.search_history = []
if 'current_page' not in st.session_state:
    st.session_state.current_page = "🏠 Master Day Plan"

# 3. Enhanced Styling
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button { background: linear-gradient(45deg, #238636, #2ea043); color: white; border-radius: 10px; width: 100%; border: none; font-weight: bold;}
    .time-badge { background-color: #1f6feb; color: white; padding: 4px 12px; border-radius: 15px; font-weight: bold; font-family: monospace; }
    .calc-box { background-color: #161b22; padding: 20px; border-radius: 12px; border: 1px solid #30363d; margin-top: 10px; }
    .subject-card { background-color: #161b22; padding: 20px; border-radius: 15px; border-left: 5px solid #1f6feb; margin-bottom: 20px; }
    .success-text { color: #238636; font-weight: bold; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

def navigate_to(page):
    st.session_state.current_page = page

# --- SIDEBAR: DOUBT HISTORY ---
st.sidebar.title("🔍 Doubt History")
doubt_input = st.sidebar.text_input("New Doubt (e.g. 'Linked List push')")
if st.sidebar.button("Search & Save"):
    if doubt_input:
        link = f"https://www.google.com/search?q={doubt_input.replace(' ', '+')}+JNTU+notes"
        st.session_state.search_history.append({"query": doubt_input, "url": link})
        st.sidebar.markdown(f"[View Solution]({link})")

st.sidebar.subheader("📜 Recent Doubts")
for item in reversed(st.session_state.search_history[-5:]):
    st.sidebar.markdown(f"• [{item['query']}]({item['url']})")

menu = st.sidebar.radio("Main Menu", 
    ["🏠 Master Day Plan", "📚 Subject Vault", "🛡️ Cyber Roadmap", "🔢 Problem Solver", "🏋️ Fitness & Moto"],
    index=["🏠 Master Day Plan", "📚 Subject Vault", "🛡️ Cyber Roadmap", "🔢 Problem Solver", "🏋️ Fitness & Moto"].index(st.session_state.current_page))
st.session_state.current_page = menu

# --- PAGE 1: MASTER DAY PLAN (12-HOUR + ROADMAP BUTTONS) ---
if st.session_state.current_page == "🏠 Master Day Plan":
    st.title("⚡ Mission Control: srujith-glitch")
    st.markdown("### Your 12-Hour Strategic Roadmap")
    
    # Clickable Roadmap
    c1, c2, c3 = st.columns(3)
    with c1: 
        if st.button("06:00 AM - Fitness"): navigate_to("🏋️ Fitness & Moto"); st.rerun()
    with c2: 
        if st.button("06:00 PM - Core Study"): navigate_to("📚 Subject Vault"); st.rerun()
    with c3: 
        if st.button("09:00 PM - Cyber Sec"): navigate_to("🛡️ Cyber Roadmap"); st.rerun()

    st.divider()
    
    # Sequential Locking Approval Section
    st.subheader("Daily Task Approval")
    
    # Task 1
    t1, b1 = st.columns([3,1])
    t1.markdown('<span class="time-badge">06:00 AM</span> **Fitness & Pushup Protocol**', unsafe_allow_html=True)
    if st.session_state.task_step == 1:
        if b1.button("APPROVE ✅", key="a1"):
            st.balloons(); st.success("Congratulations! Body primed for the day."); st.session_state.task_step = 2; time.sleep(1); st.rerun()
    elif st.session_state.task_step > 1: b1.write("✔️ COMPLETED")

    # Task 2
    t2, b2 = st.columns([3,1])
    t2.markdown('<span class="time-badge">06:00 PM</span> **BEE & DS Deep Dive (D-E-D-P)**', unsafe_allow_html=True)
    if st.session_state.task_step < 2: b2.write("🔒 Locked")
    elif st.session_state.task_step == 2:
        if b2.button("APPROVE ✅", key="a2"):
            st.balloons(); st.success("Congratulations! 9.0 CGPA getting closer."); st.session_state.task_step = 3; time.sleep(1); st.rerun()
    else: b2.write("✔️ COMPLETED")

# --- PAGE 2: SUBJECT VAULT (ALL SUBJECTS + MATERIAL) ---
elif st.session_state.current_page == "📚 Subject Vault":
    st.title("📖 Academic Vault")
    sub = st.selectbox("Choose Subject", ["BEE", "DS", "Maths (ODVC)", "Chemistry", "Drawing"])
    
    st.markdown('<div class="subject-card">', unsafe_allow_html=True)
    if sub == "BEE":
        st.header("⚡ Basic Electrical Engineering")
        st.write("**Topic:** Single Phase Transformer")
        st.image("https://www.electrical4u.com/wp-content/uploads/ideal-transformer.png", caption="Exam-Critical Diagram", width=400)
        st.latex(r"E = 4.44 \cdot f \cdot N \cdot \Phi_m")
        st.write("Mid-2 Strategy: Mastering the D-E-D-P (Definition, Equation, Diagram, Points).")

    elif sub == "DS":
        st.header("💻 Data Structures: Linked Lists")
        st.image("https://upload.wikimedia.org/wikipedia/commons/6/6d/Singly-linked-list.svg", caption="Singly Linked List Diagram", width=500)
        st.write("Key Point: Practice 'Push' and 'Pop' logic for Stacks/Queues.")

    elif sub == "Maths (ODVC)":
        st.header("🔢 Maths (ODVC): Double Integration")
        st.latex(r"\int_{x=a}^{b} \int_{y=g_1(x)}^{g_2(x)} f(x,y) \,dy \,dx")
        st.write("Always draw the integration region R on the graph first!")

    elif sub == "Chemistry":
        st.header("🧪 Engineering Chemistry")
        st.write("**Topic:** Water Technology & Batteries")
        st.write("- Hardness calculations: EDTA method.")
        st.write("- Li-ion Battery working & recharging.")

    elif sub == "Drawing":
        st.header("📐 Engineering Drawing")
        st.image("https://upload.wikimedia.org/wikipedia/commons/4/4e/Orthographic_projection_example.png", caption="Orthographic Projection", width=450)
        st.warning("Mid-2 Tip: Accuracy in First Angle Projection is vital.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 3: CYBER ROADMAP ---
elif st.session_state.current_page == "🛡️ Cyber Roadmap":
    st.title("🛡️ Path to 1.5L: Cyber Security")
    st.markdown('<span class="time-badge">09:00 PM - 10:30 PM</span>', unsafe_allow_html=True)
    st.markdown("""
    - **Step 1:** OSI Model Review (20 mins)
    - **Step 2:** TryHackMe Intro Room (40 mins)
    - **Step 3:** Linux Command Practice (30 mins)
    """)
    st.link_button("🚀 Launch TryHackMe", "https://tryhackme.com/dashboard")

# --- PAGE 4: PROBLEM SOLVER ---
elif st.session_state.current_page == "🔢 Problem Solver":
    st.title("🧮 Engineering Calculator")
    calc = st.radio("Choose Problem", ["Ohm's Law", "Electrical Power"])
    
    st.markdown('<div class="calc-box">', unsafe_allow_html=True)
    if calc == "Ohm's Law":
        i = st.number_input("Enter Current (I)", value=1.0)
        r = st.number_input("Enter Resistance (R)", value=1.0)
        if st.button("Solve Step-by-Step"):
            v = i * r
            st.markdown(f"### Result: {v} Volts")
            st.latex(r"V = I \times R")
            st.latex(f"V = {i} \times {r} = {v}V")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 5: FITNESS & MOTIVATION ---
elif st.session_state.current_page == "🏋️ Fitness & Moto":
    st.title("🏍️ Fitness Goal: The Yamaha FZ-X")
    
    # Motivation Image Added Here
    st.image("https://raw.githubusercontent.com/srujith-glitch/main.py/main/fzx_motivation.png", caption="The Prize: Yamaha FZ-X Matte Black", use_container_width=True)
    
    st.markdown('<p class="success-text">Target: 80kg (Current: 100kg)</p>', unsafe_allow_html=True)
    st.markdown('<span class="time-badge">06:00 AM - 07:00 AM</span>', unsafe_allow_html=True)
    
    with st.expander("Today's Exercise Process"):
        st.write("1. **Incline Pushups:** 3 Sets x 15 Reps. Hands on bed, body straight.")
        st.write("2. **Squats:** 3 Sets x 20 Reps. Heels flat, chest up.")
