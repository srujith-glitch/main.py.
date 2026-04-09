import streamlit as st
import os
import time

# --- 1. PERSISTENT SERVER STORAGE ENGINE ---
# Creates a physical directory structure on the server to store files permanently
VAULT_ROOT = "srujith_vault"
SECTIONS = ["Material Section", "Formula Section"]
SUBJECTS = ["BEE", "Data Structures", "Maths (ODVC)", "Chemistry", "Drawing"]

# Ensure folder structure exists on the server disk
for sec in SECTIONS:
    for sub in SUBJECTS:
        path = os.path.join(VAULT_ROOT, sec.replace(" ", "_"), sub.replace(" ", "_"))
        if not os.path.exists(path):
            os.makedirs(path)

def save_to_server(uploaded_file, section, subject):
    """Saves the file to a categorized folder on the server."""
    target_dir = os.path.join(VAULT_ROOT, section.replace(" ", "_"), subject.replace(" ", "_"))
    file_path = os.path.join(target_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def list_server_files(section, subject):
    """Retrieves list of files stored in a specific server category."""
    target_dir = os.path.join(VAULT_ROOT, section.replace(" ", "_"), subject.replace(" ", "_"))
    return os.listdir(target_dir) if os.path.exists(target_dir) else []

# --- 2. UI CONFIGURATION & STYLING ---
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

# --- 3. SIDEBAR: NAVIGATION & GUIDED UPLOADS ---
with st.sidebar:
    st.title("🛡️ srujith-glitch Control")
    menu = st.radio("Main Menu", [
        "🏠 Master Day Plan", 
        "🧪 Formula Vault", 
        "📂 Academic Vault", 
        "🎯 Syllabus Drill", 
        "📝 Exams & Archive",
        "🏋️ Fitness & Moto"
    ])
    
    st.divider()
    st.subheader("📥 Guided Server Upload")
    # Selection of specific section and subject for file storage
    dest_sec = st.selectbox("Assign to Section:", SECTIONS)
    dest_sub = st.selectbox("Target Subject:", SUBJECTS)
    up_file = st.file_uploader("Upload Notes/Formula Sheets", type=["docx", "pdf", "png", "jpg", "jpeg"])
    
    if up_file and st.button("🚀 Confirm Server Upload"):
        save_to_server(up_file, dest_sec, dest_sub)
        st.success(f"Stored in {dest_sec} → {dest_sub}")
        time.sleep(1)
        st.rerun()

# --- 4. PAGE: MASTER DAY PLAN (12-HOUR ROADMAP) ---
if menu == "🏠 Master Day Plan":
    st.title("🚀 12-Hour Strategic Roadmap")
    st.markdown("""
        <div class="info-card">
        🌅 <b>06:00 AM:</b> Fitness & Pushup Protocol<br>
        📖 <b>06:00 PM:</b> Core Study (D-E-D-P Deep Dive)<br>
        🛡️ <b>09:00 PM:</b> Cyber Security Roadmap Path
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Daily Task Approval")
    if st.checkbox("06:00 AM Fitness Protocol Completed"):
        st.success("✅ Morning Mobility & Pushups Finished")
    if st.checkbox("06:00 PM Academic Deep Dive Completed"):
        st.success("✅ BEE/DS Study Session Finished")

# --- 5. PAGE: FORMULA VAULT (Integrated Academic Content) ---
elif menu == "🧪 Formula Vault":
    st.title("🧪 Subject Formula Vault")
    f_sub = st.selectbox("Select Subject:", SUBJECTS)
    st.markdown(f"<h3 class='section-header'>{f_sub} Reference Formulas</h3>", unsafe_allow_html=True)
    
    # BEE FORMULAS [cite: 34, 36, 38, 41, 42, 49, 55]
    if f_sub == "BEE":
        st.markdown('<div class="formula-box">', unsafe_allow_html=True)
        st.write("**Ohm’s Law:** $V = I R$ [cite: 36]")
        st.write("**Power:** $P = V I = I^2 R = V^2 / R$ [cite: 38]")
        st.write("**Network Laws:** KCL & KVL (Sum of I/V = 0) [cite: 41, 42]")
        st.write("**Impedance:** $Z = \sqrt{R^2 + (X_L - X_C)^2}$ [cite: 49]")
        st.write("**Resonant Frequency:** $f_r = 1 / (2\pi\sqrt{LC})$ [cite: 55]")
        st.markdown('</div>', unsafe_allow_html=True)

    # DATA STRUCTURES FORMULAS [cite: 23, 25, 27, 32, 33]
    elif f_sub == "Data Structures":
        st.markdown('<div class="formula-box">', unsafe_allow_html=True)
        st.write("**Complexity:** $O(1), O(n), O(\log n)$ [cite: 25]")
        st.write("**Binary Search:** $\log_2 n$ [cite: 27]")
        st.write("**Trees:** Max nodes $n = 2^h - 1$ [cite: 32]")
        st.write("**AVL Balance Factor:** $BF = h_L - h_R$ [cite: 33]")
        st.markdown('</div>', unsafe_allow_html=True)

    # MATHS (ODVC) FORMULAS [cite: 11, 13, 17, 18, 20]
    elif f_sub == "Maths (ODVC)":
        st.markdown('<div class="formula-box">', unsafe_allow_html=True)
        st.write("**Linear DE:** $dy/dx + P y = Q$ [cite: 13]")
        st.write("**Dot Product:** $A \cdot B = AB \cos\\theta$ [cite: 17]")
        st.write("**Cross Product:** $|A \\times B| = AB \sin\\theta$ [cite: 18]")
        st.write("**Vector Calculus:** $\\nabla\\phi$ (Grad), $\\nabla \cdot A$ (Div), $\\nabla \\times A$ (Curl) [cite: 20]")
        st.markdown('</div>', unsafe_allow_html=True)

    # CHEMISTRY FORMULAS [cite: 1, 3, 5, 6, 8, 10]
    elif f_sub == "Chemistry":
        st.markdown('<div class="formula-box">', unsafe_allow_html=True)
        st.write("**Nernst Equation:** $E = E^\circ - (0.0591/n) \log Q$ [cite: 3]")
        st.write("**Cell Potential:** $E_{cell} = E_{cathode} - E_{anode}$ [cite: 5]")
        st.write("**Gibbs Energy:** $\Delta G = -nFE$ [cite: 6]")
        st.write("**Polymers:** $DP = Molecular Weight / Monomer Weight$ [cite: 8]")
        st.write("**Fuels:** $CV = Heat / Mass$ [cite: 10]")
        st.markdown('</div>', unsafe_allow_html=True)

    # Display server files assigned specifically to this subject's formula section
    st.write("---")
    st.subheader("📁 My Server-Stored Sheets")
    files = list_server_files("Formula_Section", f_sub)
    if files:
        for f in files: st.info(f"📄 {f}")
    else: st.write("No extra files stored yet.")

# --- 6. PAGE: ACADEMIC VAULT (MATERIAL SECTION) ---
elif menu == "📂 Academic Vault":
    st.title("📂 Academic Resource Hub")
    m_sub = st.selectbox("Select Subject:", SUBJECTS)
    st.markdown(f"<h3 class='section-header'>{m_sub} Study Material</h3>", unsafe_allow_html=True)
    
    # Specific topic reminders
    if m_sub == "BEE":
        st.info("Key Topic: Single Phase Transformer (Core/Windings Diagram required).")
    elif m_sub == "Maths (ODVC)":
        st.latex(r"\iint_R f(x,y) \,dA")
        st.write("Always draw the integration region R first!")

    # Display files assigned to Material Section for this subject
    files = list_server_files("Material_Section", m_sub)
    if files:
        for f in files: st.success(f"📘 {f}")
    else: st.write("Upload notes in the sidebar to view them here.")

# --- 7. PAGE: SYLLABUS DRILL (INTERACTIVE) ---
elif menu == "🎯 Syllabus Drill":
    st.title("🎯 Interactive Syllabus Drill")
    drill_sub = st.selectbox("Select Drill Subject:", ["BEE", "Data Structures"])
    
    if st.button("Generate Question"):
        st.session_state.q = "Derive Transformer EMF Equation." if drill_sub == "BEE" else "Explain Stack PUSH/POP logic."
        st.session_state.show_key = False

    if "q" in st.session_state:
        st.markdown(f'<div class="info-card" style="color:#f1e05a"><b>DRILL:</b> {st.session_state.q}</div>', unsafe_allow_html=True)
        st.text_area("Your Response:")
        if st.button("Verify Answer"): st.session_state.show_key = True
        
        if st.session_state.show_key:
            key = "E = 4.44 * f * N * Φm" if drill_sub == "BEE" else "PUSH: Top++ then insert. POP: Remove then Top--."
            st.warning(f"✅ ANSWER KEY: {key}")

# --- 8. PAGE: EXAMS & ARCHIVE ---
elif menu == "📝 Exams & Archive":
    st.title("📝 Exam Repository")
    st.link_button("JNTU Previous Year Papers", "https://www.jntufastupdates.com/")
    st.write("Access your uploaded mid-term papers and previous university keys here.")

# --- 9. PAGE: FITNESS & MOTO ---
elif menu == "🏋️ Fitness & Moto":
    st.title("🏍️ Target: Yamaha FZ-X")
    st.markdown('<div class="info-card" style="background-color:#1d3321; border-color:#238636"><b>GOAL: 80kg Baseline</b></div>', unsafe_allow_html=True)
    st.write("Daily Protocol: 3x15 Pushups, 3x20 Squats, 60s Planks.")
