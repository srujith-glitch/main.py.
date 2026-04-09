import streamlit as st
import time
import random

# 1. Page Configuration
st.set_page_config(page_title="Success Stacker: Master OS", page_icon="🏆", layout="wide")

# 2. State Management
if 'task_step' not in st.session_state: st.session_state.task_step = 1
if 'search_history' not in st.session_state: st.session_state.search_history = []
if 'current_page' not in st.session_state: st.session_state.current_page = "🏠 Command Center"

# 3. High-Contrast Designer UI
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #ffffff; }
    img { filter: brightness(1.2) contrast(1.1); background-color: #ffffff; border-radius: 12px; padding: 10px; margin: 15px 0; border: 2px solid #30363d; }
    .stButton>button { background: linear-gradient(90deg, #00d4ff, #0072ff); color: white; border-radius: 12px; font-weight: 800; border: none; transition: 0.3s; height: 3.5em; width: 100%; }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0px 8px 20px #00d4ff; }
    .info-card { background: #161b22; border-left: 5px solid #238636; padding: 20px; border-radius: 12px; margin-bottom: 20px; border: 1px solid #30363d; }
    .holiday-card { background: #1c2128; border-left: 5px solid #f1e05a; padding: 20px; border-radius: 12px; margin-bottom: 20px; }
    .time-badge { background-color: #1f6feb; color: white; padding: 5px 15px; border-radius: 20px; font-weight: bold; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: NAVIGATION ---
with st.sidebar:
    st.title("🛡️ srujith-glitch OS")
    menu = st.radio("Main Menu", [
        "🏠 Command Center", 
        "📅 Holiday/Weekend Planner",
        "📂 Faculty Study Material", 
        "📚 Syllabus Master (Drill)", 
        "📝 Papers & Doubts", 
        "🏋️ Fitness & Moto"
    ])
    st.divider()
    with st.expander("🔍 Quick Doubt Search"):
        dq = st.text_input("New Doubt:")
        if st.button("Save & Archive"):
            if dq:
                l = f"https://www.google.com/search?q={dq.replace(' ', '+')}+JNTU+notes"
                st.session_state.search_history.append({"q": dq, "l": l})
    st.info("Mode: 12-Hour Strategic")

# --- PAGE 1: COMMAND CENTER ---
if menu == "🏠 Command Center":
    st.title("🚀 Command Center")
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="info-card"><b>🌅 06:00 AM</b><br>Fitness Protocol</div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="info-card"><b>📖 06:00 PM</b><br>Core Subject Study</div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="info-card"><b>🛡️ 09:00 PM</b><br>Cyber Sec Lab</div>', unsafe_allow_html=True)
    
    st.divider()
    st.subheader("Task Approval")
    if st.session_state.task_step == 1:
        st.info("🕒 Pending: 06:00 AM Fitness & Mobility")
        if st.button("APPROVE COMPLETION ✅"): st.session_state.task_step = 2; st.rerun()
    elif st.session_state.task_step == 2:
        st.success("✅ Morning Session Done")
        st.info("🕒 Pending: 06:00 PM D-E-D-P Study Session")
        if st.button("APPROVE COMPLETION ✅"): st.session_state.task_step = 3; st.rerun()

# --- PAGE 2: HOLIDAY PLANNER ---
elif menu == "📅 Holiday/Weekend Planner":
    st.title("🏖️ Holiday Strategy")
    st.markdown("""
    <div class="holiday-card">
    <b>08:00 AM - 10:30 AM:</b> Deep Problem Solving (Maths/BEE)<br>
    <b>11:30 AM - 01:30 PM:</b> Cyber Security Path Labs<br>
    <b>04:00 PM - 06:00 PM:</b> Extended Fitness Reset<br>
    <b>08:00 PM - 10:00 PM:</b> Full Syllabus Drill
    </div>
    """, unsafe_allow_html=True)

# --- PAGE 3: FACULTY STUDY MATERIAL ---
elif menu == "📂 Faculty Study Material":
    st.title("📂 Faculty Resource Hub")
    tabs = st.tabs(["BEE", "DS", "Maths", "Chemistry", "Drawing"])
    
    with tabs[0]:
        st.header("⚡ BEE")
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.write("**Topic: Single Phase Transformer**")
        st.image("https://www.electrical4u.com/wp-content/uploads/ideal-transformer.png", width=400)
        st.latex(r"E = 4.44 \cdot f \cdot N \cdot \Phi_m")
        st.write("• [Faculty Notes Link](https://example.com)")
        st.markdown('</div>', unsafe_allow_html=True)

    with tabs[1]:
        st.header("💻 Data Structures")
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.write("**Topic: Stacks**")
        st.image("https://upload.wikimedia.org/wikipedia/commons/2/29/Data_stack.svg", width=300)
        st.write("Faculty Tip: Focus on LIFO (Last In First Out).")
        st.markdown('</div>', unsafe_allow_html=True)

    with tabs[2]:
        st.header("🔢 Maths (ODVC)")
        st.latex(r"\iint_R f(x,y) \,dA")
        st.write("Focus on changing the order of integration.")

# --- PAGE 4: SYLLABUS MASTER ---
elif menu == "📚 Syllabus Master (Drill)":
    st.title("🎯 Syllabus Drill")
    sub = st.selectbox("Select Subject", ["BEE", "DS", "Maths"])
    if st.button("Generate Random Question"):
        q = {"BEE": "Derive the EMF Eq.", "DS": "Write Stack Push/Pop Logic.", "Maths": "State Green's Theorem."}
        st.warning(f"**Random Drill:** {q[sub]}")

# --- PAGE 5: PAPERS & DOUBTS ---
elif menu == "📝 Papers & Doubts":
    st.title("📝 Exams & Archive")
    st.link_button("JNTU Previous Papers", "https://www.jntufastupdates.com/")
    st.divider()
    for item in reversed(st.session_state.search_history):
        st.markdown(f"❓ **{item['q']}** → [Solution Link]({item['l']})")

# --- PAGE 6: FITNESS & MOTO ---
elif menu == "🏋️ Fitness & Moto":
    st.title("🏍️ Goal: Yamaha FZ-X")
    try:
        st.image("bike.png", use_container_width=True)
    except:
        st.image("https://www.yamaha-motor-india.com/theme/v3/images/fzx/color/matte-copper.png", use_container_width=True)
    st.success("Target: 80kg Goal Motivation")
