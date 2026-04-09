import streamlit as st
import os
import time

# --- 1. SERVER STORAGE & DIRECTORY ENGINE ---
VAULT_ROOT = "srujith_vault"
SECTIONS = ["Material Section", "Formula Section"]
SUBJECTS = ["BEE", "Data Structures", "Maths (ODVC)", "Chemistry", "Drawing"]

# Ensure persistent folder structure exists on the server disk
for sec in SECTIONS:
    for sub in SUBJECTS:
        path = os.path.join(VAULT_ROOT, sec.replace(" ", "_"), sub.replace(" ", "_"))
        if not os.path.exists(path):
            os.makedirs(path)

def save_to_server(uploaded_file, section, subject):
    target_dir = os.path.join(VAULT_ROOT, section.replace(" ", "_"), subject.replace(" ", "_"))
    file_path = os.path.join(target_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def list_server_files(section, subject):
    target_dir = os.path.join(VAULT_ROOT, section.replace(" ", "_"), subject.replace(" ", "_"))
    return os.listdir(target_dir) if os.path.exists(target_dir) else []

# --- 2. GLOBAL UI & STYLING ---
st.set_page_config(page_title="Control: srujith-glitch", layout="wide", page_icon="🛡️")

st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #ffffff; }
    .stButton>button { background: linear-gradient(90deg, #00d4ff, #0072ff); color: white; border-radius: 12px; font-weight: 800; border: none; height: 3.5em; width: 100%; }
    .info-card { background: #161b22; border-left: 5px solid #238636; padding: 20px; border-radius: 12px; margin-bottom: 20px; border: 1px solid #30363d; }
    .formula-box { background: #0d1117; border: 1px solid #58a6ff; padding: 15px; border-radius: 10px; margin-bottom: 15px; }
    .section-header { color: #58a6ff; border-bottom: 1px solid #30363d; padding-bottom: 10px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: NAVIGATION & GUIDED UPLOAD ---
with st.sidebar:
    st.title("🛡️ Control Center")
    menu = st.radio("Main Menu", ["🏠 Master Day Plan", "🧪 Formula Vault", "📂 Academic Vault", "🎯 Syllabus Drill", "🏋️ Fitness & Moto"])
    
    st.divider()
    st.subheader("📤 Guided Server Upload")
    dest_sec = st.selectbox("1. Choose Section:", SECTIONS)
    dest_sub = st.selectbox("2. Choose Subject:", SUBJECTS)
    up_file = st.file_uploader("3. Select File:", type=["docx", "pdf", "png", "jpg", "jpeg"])
    
    if up_file and st.button("🚀 Push to Server"):
        save_to_server(up_file, dest_sec, dest_sub)
        st.success(f"Archived in {dest_sec} → {dest_sub}")
        time.sleep(1)
        st.rerun()

# --- 4. PAGE: MASTER DAY PLAN (12-HOUR ROADMAP) ---
if menu == "🏠 Master Day Plan":
    st.title("🚀 Your 12-Hour Strategic Roadmap")
    st.markdown('<div class="info-card"><b>06:00 AM:</b> Fitness & Pushup Protocol<br><b>06:00 PM:</b> BEE & DS Deep Dive (D-E-D-P)<br><b>09:00 PM:</b> Cyber Sec Path</div>', unsafe_allow_html=True)
    
    st.subheader("Daily Task Approval")
    if st.checkbox("06:00 AM Protocol Completed"):
        st.success("✅ Morning Mobility Finished")
    if st.checkbox("06:00 PM Subject Study Completed"):
        st.success("✅ Academic Deep Dive Finished")

# --- 5. PAGE: FORMULA VAULT (Integrated from Word Files) ---
elif menu == "🧪 Formula Vault":
    st.title("🧪 Subject Formula Vault")
    f_sub = st.selectbox("Select Subject Formulas:", SUBJECTS)
    
    st.markdown(f"<h3 class='section-header'>{f_sub} Reference Sheets</h3>", unsafe_allow_html=True)
    
    # Static Data from uploaded Word documents [cite: 1, 11, 23, 34]
    if f_sub == "BEE":
        st.markdown('<div class="formula-box">', unsafe_allow_html=True)
        st.write("**Ohm’s Law:** $V = I R$ [cite: 36]")
        st.write("**Power:** $P = V I = I^2 R = V^2 / R$ [cite: 38]")
        st.write("**AC Impedance:** $Z = \sqrt{R^2 + (X_L - X_C)^2}$ [cite: 49]")
        st.write("**Transformer EMF:** $E = 4.44 \cdot f \cdot N \cdot \Phi_m$ [cite: 55]")
        st.markdown('</div>', unsafe_allow_html=True)
        
    elif f_sub == "Data Structures":
        st.markdown('<div class="formula-box">', unsafe_allow_html=True)
        st.write("**Binary Search Complexity:** $\log_2 n$ [cite: 27]")
        st.write("**Stack PUSH:** $Top = Top + 1$ [cite: 29]")
        st.write("**AVL Balance Factor:** $BF = h_L - h_R$ [cite: 33]")
        st.markdown('</div>', unsafe_allow_html=True)

    elif f_sub == "Maths (ODVC)":
        st.markdown('<div class="formula-box">', unsafe_allow_html=True)
        st.write("**Linear DE:** $dy/dx + P y = Q$ [cite: 13]")
        st.write("**Vector Dot Product:** $A \cdot B = AB \cos\\theta$ [cite: 17]")
        st.write("**Double Integration:** $\iint_R f(x,y) \,dy \,dx$ [cite: 22]")
        st.markdown('</div>', unsafe_allow_html=True)

    elif f_sub == "Chemistry":
        st.markdown('<div class="formula-box">', unsafe_allow_html=True)
        st.write("**Nernst Equation:** $E = E^\circ - (0.0591/n) \log Q$ [cite: 3]")
        st.write("**Gibbs Free Energy:** $\Delta G = -nFE$ [cite: 6]")
        st.markdown('</div>', unsafe_allow_html=True)

    # Server Files for Formulas
    uploaded_formulas = list_server_files("Formula_Section", f_sub)
    if uploaded_formulas:
        st.write("---")
        st.subheader("📁 My Uploaded Formula Files")
        for f in uploaded_formulas:
            st.info(f"📄 {f}")

# --- 6. PAGE: ACADEMIC VAULT (MATERIAL SECTION) ---
elif menu == "📂 Academic Vault":
    st.title("📂 Academic Resource Hub")
    m_sub = st.selectbox("Select Subject Material:", SUBJECTS)
    
    st.markdown(f"<h3 class='section-header'>{m_sub} Faculty Material</h3>", unsafe_allow_html=True)
    
    if m_sub == "BEE":
        st.write("**Topic:** Single Phase Transformer")
        st.write("*Note:* Must draw Core and Windings for full marks.")
    
    uploaded_materials = list_server_files("Material_Section", m_sub)
    if uploaded_materials:
        for m in uploaded_materials:
            st.success(f"📘 {m}")
    else:
        st.write("No files uploaded to this section yet.")

# --- 7. PAGE: SYLLABUS DRILL ---
elif menu == "🎯 Syllabus Drill":
    st.title("🎯 Drill & Solution Verification")
    drill_sub = st.selectbox("Subject for Drill:", ["BEE", "Data Structures"])
    
    if st.button("Generate Random Question"):
        st.session_state.current_q = "Derive the EMF Equation of a Transformer." if drill_sub == "BEE" else "Write the algorithm for Stack PUSH."
        st.session_state.show_drill_key = False

    if "current_q" in st.session_state:
        st.markdown(f'<div class="info-card"><b>QUESTION:</b> {st.session_state.current_q}</div>', unsafe_allow_html=True)
        st.text_area("Type your solution here:")
        
        if st.button("Verify Answer"):
            st.session_state.show_drill_key = True
        
        if st.session_state.show_drill_key:
            key_text = "E = 4.44 * f * N * Φm" if drill_sub == "BEE" else "Check Overflow -> Top++ -> Insert"
            st.warning(f"✅ ANSWER KEY: {key_text}")
            st.info("💡 NEXT TOPIC: Efficiency & Losses" if drill_sub == "BEE" else "💡 NEXT TOPIC: Queue Operations")

# --- 8. PAGE: FITNESS & MOTO ---
elif menu == "🏋️ Fitness & Moto":
    st.title("🏍️ Goal: Yamaha FZ-X")
    st.markdown('<div class="info-card">Target: 80kg Goal Motivation</div>', unsafe_allow_html=True)
    st.write("**80kg Protocol:** 3x15 Pushups | 3x20 Squats | 60s Planks")
    
    fit_files = list_server_files("Material_Section", "Drawing") # Using Drawing folder as a placeholder or Fitness if created
    for f in fit_files:
        st.write(f"🏋️ {f}")
