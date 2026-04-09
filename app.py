import streamlit as st
import time
import random

# 1. Page Configuration
st.set_page_config(page_title="Success Stacker: Master OS", page_icon="🏆", layout="wide")

# 2. State Management (Prevents reset on clicks)
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

# --- SIDEBAR: HIDDEN DOUBT ENGINE ---
with st.sidebar:
    st.title("🛡️ Intelligence Hub")
    menu = st.radio("Main Menu", [
        "🏠 Command Center", 
        "📅 Holiday/Weekend Planner",
        "📂 Faculty Study Material", 
        "📚 Syllabus Master (Drill)", 
        "📝 Papers & Doubts", 
        "🏋️ Fitness & Moto"
    ])
    st.divider()
    with st.expander("🔍 Click to Resolve Doubt"):
        dq = st.text_input("New Doubt (Private Search):")
        if st.button("Archive Doubt"):
            if dq:
                l = f"https://www.google.com/search?q={dq.replace(' ', '+')}+notes+pdf"
                st.session_state.search_history.append({"q": dq, "l": l})
                st.success("Archived in Papers & Doubts!")
    st.info("Current Mode: 12-Hour Strategic")

# --- PAGE 1: COMMAND CENTER (REGULAR DAY) ---
if menu == "🏠 Command Center":
    st.title("🚀 Command Center: Regular Day")
    
    st.subheader("Your 12-Hour Strategic Roadmap")
    c1, c2, c3 = st.columns(3)
    with c1: 
        if st.button("06:00 AM - Fitness"): st.session_state.current_page = "🏋️ Fitness & Moto"; st.rerun()
    with c2: 
        if st.button("06:00 PM - Study"): st.session_state.current_page = "📂 Faculty Study Material"; st.rerun()
    with c3: 
        if st.button("09:00 PM - Cyber"): st.session_state.current_page = "🛡️ Cyber Roadmap"; st.rerun()

    st.divider()
    st.subheader("Task Completion Flow")
    if st.session_state.task_step == 1:
        st.markdown('<div class="info-card">🕒 <b>06:00 AM</b>: Morning Mobility Protocol. Approve to unlock evening tasks.</div>', unsafe_allow_html=True)
        if st.button("APPROVE COMPLETION ✅"): st.session_state.task_step = 2; st.rerun()
    elif st.session_state.task_step == 2:
        st.success("Morning Mission Complete!")
        st.markdown('<div class="info-card">🕒 <b>06:00 PM</b>: Core Academic Session. Update your material vault.</div>', unsafe_allow_html=True)
        if st.button("APPROVE COMPLETION ✅"): st.session_state.task_step = 3; st.rerun()

# --- PAGE 2: HOLIDAY/WEEKEND PLANNER ---
elif menu == "📅 Holiday/Weekend Planner":
    st.title("🏖️ Holiday Grind Plan")
    st.subheader("Max Productivity Mode")
    st.markdown("""
    <div class="holiday-card">
    <b>🌅 08:00 AM - 10:30 AM:</b> Deep Work - Solving Previous Papers<br>
    <b>🏙️ 11:30 AM - 01:30 PM:</b> Cyber Security Labs (TryHackMe/Linux)<br>
    <b>🌇 04:00 PM - 06:00 PM:</b> Extended Fitness (Outdoor Run/Gym)<br>
    <b>🌃 08:00 PM - 10:00 PM:</b> Syllabus Master Random Drill Questions
    </div>
    """, unsafe_allow_html=True)
    st.warning("Holiday Goal: Finish 1 Full Unit of BEE or Maths.")

# --- PAGE 3: FACULTY STUDY MATERIAL (INDIVIDUAL SUBJECTS) ---
elif menu == "📂 Faculty Study Material":
    st.title("📂 Faculty Resource Hub")
    st.info("Direct uploads and notes from your college professors.")
    
    tabs = st.tabs(["BEE", "DS", "Maths (ODVC)", "Chemistry", "Drawing"])
    
    with tabs[0]:
        st.header("⚡ BEE Material")
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.write("**Unit 1: Transformers**")
        st.image("https://www.electrical4u.com/wp-content/uploads/ideal-transformer.png", width=400)
        

[Image of a single phase transformer diagram]

        st.latex(r"E = 4.44 \cdot f \cdot N \cdot \Phi_m")
        st.write("• [Faculty Link: Mid-2 Question Bank](https://example.com)")
        st.markdown('</div>', unsafe_allow_html=True)

    with tabs[1]:
        st.header("💻 Data Structures Material")
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.write("**Unit 2: Stacks & Queues**")
        st.image("https://upload.wikimedia.org/wikipedia/commons/2/29/Data_stack.svg", width=300)
        
        st.write("Faculty Note: Understand the difference between LIFO and FIFO.")
        st.markdown('</div>', unsafe_allow_html=True)

    with tabs[2]:
        st.header("🔢 Maths (ODVC) Material")
        st.latex(r"\iint_R f(x,y) \,dA")
        st.write("Faculty Strategy: Practice changing the order of integration.")

# --- PAGE 4: SYLLABUS MASTER (UNIT DRILLS) ---
elif menu == "📚 Syllabus Master (Drill)":
    st.title("🎯 Complete Syllabus Coverage Drill")
    target_sub = st.selectbox("Select Subject", ["BEE", "DS", "Maths"])
    
    if st.button("Generate Random Syllabus Question"):
        q_bank = {
            "BEE": ["Explain Transformer Losses.", "Derive DC Generator EMF Eq.", "Compare MC and MI Meters."],
            "DS": ["Write Push/Pop Algorithm for Stacks.", "Explain Binary Search Tree insertion.", "Compare BFS vs DFS."],
            "Maths": ["Solve Double Integral for y=x and y=x^2.", "State Gauss Divergence Theorem.", "Apply Green's Theorem."]
        }
        st.markdown(f'<div class="holiday-card" style="font-size: 20px;"><b>Question:</b> {random.choice(q_bank[target_sub])}</div>', unsafe_allow_html=True)

# --- PAGE 5: PAPERS & DOUBTS (HIDDEN DATA) ---
elif menu == "📝 Papers & Doubts":
    st.title("📝 Exams & Saved Doubts")
    tab_p, tab_d = st.tabs(["Previous Papers", "My Doubt Archive"])
    
    with tab_p:
        st.link_button("JNTU FastUpdates: Previous Papers", "https://www.jntufastupdates.com/")
        st.link_button("Search All Past Papers (Google)", "https://www.google.com/search?q=JNTU+Previous+Year+Question+Papers")
    
    with tab_d:
        if not st.session_state.search_history:
            st.write("No doubts saved yet. Use the sidebar to add some!")
        for item in reversed(st.session_state.search_history):
            st.markdown(f"❓ **{item['q']}** → [Solution Link]({item['l']})")

# --- PAGE 6: FITNESS & MOTO ---
elif menu == "🏋️ Fitness & Moto":
    st.title("🏍️ Goal: Yamaha FZ-X")
    try:
        st.image("bike.png", use_container_width=True)
    except:
        st.image("https://www.yamaha-motor-india.com/theme/v3/images/fzx/color/matte-copper.png", use_container_width=True)
    st.markdown('<div class="info-card"><b>Target:</b> 80kg Goal.<br><b>Process:</b> Incline Pushups, Squats, Planks.</div>', unsafe_allow_html=True)
