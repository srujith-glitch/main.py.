import streamlit as st
import time
import random

# 1. Page Configuration & Layout
st.set_page_config(page_title="srujith-glitch OS", page_icon="🚀", layout="wide")

# 2. Advanced State Management for Persistence
if 'task_step' not in st.session_state: st.session_state.task_step = 1
if 'file_vault' not in st.session_state: st.session_state.file_vault = []
if 'search_history' not in st.session_state: st.session_state.search_history = []
if 'drill_state' not in st.session_state: st.session_state.drill_state = {"q": None, "k": None, "next": None, "show": False}

# 3. High-Contrast Dark Theme UI
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #ffffff; }
    img { filter: brightness(1.2) contrast(1.1); border-radius: 12px; border: 2px solid #30363d; margin-bottom: 20px; }
    .stButton>button { background: linear-gradient(90deg, #00d4ff, #0072ff); color: white; border-radius: 12px; font-weight: 800; border: none; height: 3.5em; width: 100%; transition: 0.3s; }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0px 5px 15px #00d4ff; }
    .info-card { background: #161b22; border-left: 5px solid #238636; padding: 20px; border-radius: 12px; margin-bottom: 20px; border: 1px solid #30363d; }
    .formula-card { background: #0d1117; border: 1px solid #58a6ff; padding: 15px; border-radius: 10px; margin-bottom: 15px; text-align: center; }
    .target-box { background-color: #1d3321; color: #4ade80; padding: 15px; border-radius: 10px; font-weight: bold; text-align: center; border: 1px solid #238636; margin-bottom: 20px;}
    .drill-box { background: #1c2128; border: 2px solid #f1e05a; padding: 20px; border-radius: 15px; color: #f1e05a; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: NAVIGATION & PERMANENT VAULT ---
with st.sidebar:
    st.title("🛡️ Control Center")
    menu = st.radio("Main Menu", [
        "🏠 Master Day Plan", 
        "🧪 Formula & Equations", 
        "📂 Subject Vault", 
        "🎯 Syllabus Drill", 
        "📝 Exams & Archive",
        "🏋️ Fitness & Moto"
    ])
    st.divider()
    st.subheader("📥 Store to Vault")
    new_file = st.file_uploader("Upload Notes/Answer Keys", type=["pdf", "png", "jpg", "jpeg"])
    if new_file:
        file_meta = {"name": new_file.name, "time": time.strftime("%H:%M:%S"), "size": new_file.size}
        if file_meta not in st.session_state.file_vault:
            st.session_state.file_vault.append(file_meta)
            st.success(f"Archived: {new_file.name}")

# --- PAGE 1: MASTER DAY PLAN (12-HOUR ROADMAP) ---
if menu == "🏠 Master Day Plan":
    st.title("🚀 Your 12-Hour Strategic Roadmap")
    c1, c2, c3 = st.columns(3)
    with c1: st.success("🌅 06:00 AM - Fitness Protocol")
    with c2: st.info("📖 06:00 PM - Core Study (D-E-D-P)")
    with c3: st.warning("🛡️ 09:00 PM - Cyber Sec Path")
    
    st.divider()
    st.subheader("Daily Task Approval")
    if st.session_state.task_step == 1:
        st.markdown('<div class="info-card">🕒 Pending: <b>06:00 AM Fitness & Pushup Protocol</b></div>', unsafe_allow_html=True)
        if st.button("APPROVE COMPLETION ✅"): st.session_state.task_step = 2; st.rerun()
    elif st.session_state.task_step == 2:
        st.markdown('<div class="info-card" style="border-left-color: #58a6ff;">✅ COMPLETED: Morning Mobility<br>🕒 Pending: <b>06:00 PM BEE & DS Deep Dive</b></div>', unsafe_allow_html=True)
        if st.button("APPROVE COMPLETION ✅"): st.session_state.task_step = 3; st.rerun()
    else:
        st.balloons()
        st.success("All Daily Missions Completed!")

# --- PAGE 2: FORMULA & EQUATIONS ---
elif menu == "🧪 Formula & Equations":
    st.title("🧪 Formula & Equations Vault")
    f_tabs = st.tabs(["BEE", "Maths (ODVC)", "Chemistry"])
    with f_tabs[0]:
        st.markdown('<div class="formula-card"><h4>Transformer EMF</h4>', unsafe_allow_html=True)
        st.latex(r"E = 4.44 \cdot f \cdot N \cdot \Phi_m")
        st.write("f=freq, N=turns, Φm=max flux")
        st.markdown('</div>', unsafe_allow_html=True)
    with f_tabs[1]:
        st.markdown('<div class="formula-card"><h4>Gauss Divergence Theorem</h4>', unsafe_allow_html=True)
        st.latex(r"\iiint_V (\nabla \cdot \mathbf{F}) \,dV = \iint_S (\mathbf{F} \cdot \mathbf{n}) \,dS")
        st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 3: SUBJECT VAULT (RESOURCES) ---
elif menu == "📂 Subject Vault":
    st.title("📂 Faculty Resource Hub")
    s_tabs = st.tabs(["BEE", "DS", "Maths", "Chemistry", "Drawing"])
    with s_tabs[0]: # BEE Details
        st.header("⚡ BEE: Single Phase Transformer")
        st.markdown('<div class="info-card"><b>Definition:</b> A static device that transfers electrical energy via electromagnetic induction.</div>', unsafe_allow_html=True)
        st.error("⚠️ MUST DRAW: Core, Primary Winding, Secondary Winding, and Magnetic Flux Lines.")
        st.image("https://www.electrical4u.com/wp-content/uploads/ideal-transformer.png", width=400)
    
    st.divider()
    st.subheader("🗄️ Your Uploaded Reference Vault")
    if not st.session_state.file_vault: st.info("Vault is empty. Upload in sidebar to refer later.")
    else:
        for f in st.session_state.file_vault:
            st.markdown(f"📄 **{f['name']}** | Stored: {f['time']}")

# --- PAGE 4: SYLLABUS DRILL (INTERACTIVE) ---
elif menu == "🎯 Syllabus Drill":
    st.title("🎯 Drill & Feedback Mode")
    drill_data = {
        "BEE": {"q": "Derive Transformer EMF Eq.", "k": "E = 4.44 f N Φm", "n": "Next: Efficiency & Losses"},
        "DS": {"q": "Explain Stack Push/Pop Logic.", "k": "Push: Overflow check -> Top++ -> Insert", "n": "Next: Queue Operations"}
    }
    sub = st.selectbox("Select Subject", ["BEE", "DS"])
    if st.button("Generate Random Question"):
        st.session_state.drill_state = {"q": drill_data[sub]['q'], "k": drill_data[sub]['k'], "next": drill_data[sub]['n'], "show": False}

    if st.session_state.drill_state["q"]:
        st.markdown(f'<div class="drill-box">QUESTION: {st.session_state.drill_state["q"]}</div>', unsafe_allow_html=True)
        u_ans = st.text_area("Type your solution to verify:")
        if st.button("Verify & Show Key"): st.session_state.drill_state["show"] = True
        
        if st.session_state.drill_state["show"]:
            st.success(f"✅ CORRECT KEY: {st.session_state.drill_state['k']}")
            st.info(f"💡 RECOMMENDATION: {st.session_state.drill_state['next']}")

# --- PAGE 5: EXAMS & ARCHIVE ---
elif menu == "📝 Exams & Archive":
    st.title("📝 Exam Repository")
    st.link_button("JNTU Previous Year Papers", "https://www.jntufastupdates.com/")
    st.divider()
    st.subheader("Mid-1 Papers & Keys")
    # Pulls files from vault that mention 'mid'
    mids = [f for f in st.session_state.file_vault if "mid" in f['name'].lower()]
    if not mids: st.write("No Mid papers found in vault yet.")
    for m in mids: st.write(f"✅ Stored: {m['name']}")

# --- PAGE 6: FITNESS & MOTO ---
elif menu == "🏋️ Fitness & Moto":
    st.title("🏍️ Goal: Yamaha FZ-X")
    st.markdown('<div class="target-box">Target: 80kg Goal Motivation</div>', unsafe_allow_html=True)
    try: st.image("bike.png", use_container_width=True)
    except: st.image("https://www.yamaha-motor-india.com/theme/v3/images/fzx/color/matte-copper.png", use_container_width=True)
    
    st.subheader("📋 Routine Guide")
    st.markdown("""
    <div class="info-card">
    1. Incline Pushups: 3 Sets x 15 Reps<br>
    2. Bodyweight Squats: 3 Sets x 20 Reps<br>
    3. Plank Stability: 3 Reps x 60 Seconds
    </div>
    """, unsafe_allow_html=True)
