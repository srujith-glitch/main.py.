import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import hashlib
import random

# =============================================================================
# ⚙️ CONFIG
# =============================================================================
VAULT_ROOT = Path("srujith_vault")
SECTIONS = ["📚 Material", "🧪 Formula", "🏋️ Fitness"]
SUBJECTS = ["BEE", "Data Structures", "Maths", "Chemistry", "Drawing"]

# =============================================================================
# 🧠 CORE SYSTEM
# =============================================================================
class VaultSystem:

    def __init__(self):
        self.init_structure()

    def init_structure(self):
        for sec in SECTIONS:
            for sub in SUBJECTS:
                path = VAULT_ROOT / sec.replace(" ", "_") / sub.replace(" ", "_")
                path.mkdir(parents=True, exist_ok=True)

        (VAULT_ROOT / "metadata").mkdir(exist_ok=True)

    def save_file(self, file, section, subject):
        folder = VAULT_ROOT / section.replace(" ", "_") / subject.replace(" ", "_")

        file_hash = hashlib.md5(file.getvalue()).hexdigest()[:6]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ext = Path(file.name).suffix

        filename = f"{timestamp}_{file_hash}{ext}"
        filepath = folder / filename

        with open(filepath, "wb") as f:
            f.write(file.getvalue())

        return filepath

    def list_files(self, section, subject):
        folder = VAULT_ROOT / section.replace(" ", "_") / subject.replace(" ", "_")
        return list(folder.glob("*"))

# =============================================================================
# 📊 ANALYTICS
# =============================================================================
def get_stats():
    total = 0
    for sec in SECTIONS:
        for sub in SUBJECTS:
            folder = VAULT_ROOT / sec.replace(" ", "_") / sub.replace(" ", "_")
            total += len(list(folder.glob("*")))
    return total

# =============================================================================
# 🎨 UI
# =============================================================================
def load_ui():
    st.set_page_config(page_title="Vault OS", layout="wide")

    st.markdown("""
    <style>
    .main {background: #0e1117; color: white;}
    h1 {color:#00d4ff;}
    .card {
        background:#161b22;
        padding:20px;
        border-radius:12px;
        margin-bottom:10px;
    }
    </style>
    """, unsafe_allow_html=True)

# =============================================================================
# 📌 DASHBOARD
# =============================================================================
def dashboard():
    st.title("🛡️ Srujith Vault OS")
    st.subheader("Professional Academic Command Center")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📂 Total Files", get_stats())

    with col2:
        st.metric("📚 Subjects", len(SUBJECTS))

# =============================================================================
# 📚 ACADEMIC VAULT
# =============================================================================
def academic(vault):
    st.header("📚 Academic Vault")

    subject = st.selectbox("Subject", SUBJECTS)
    file = st.file_uploader("Upload Notes / PDFs")

    if file:
        path = vault.save_file(file, "📚 Material", subject)
        st.success(f"Saved: {path.name}")

    files = vault.list_files("📚 Material", subject)

    st.subheader("Files")
    for f in files:
        st.markdown(f"<div class='card'>📄 {f.name}</div>", unsafe_allow_html=True)

# =============================================================================
# 🧪 FORMULA SYSTEM
# =============================================================================
FORMULAS = {
    "BEE": ["P = VI", "E = 4.44 f N Φ"],
    "Data Structures": ["O(log n)", "BF = hL - hR"]
}

def formula():
    st.header("🧪 Formula Vault")

    subject = st.selectbox("Subject", list(FORMULAS.keys()))

    for f in FORMULAS[subject]:
        st.markdown(f"<div class='card'>📘 {f}</div>", unsafe_allow_html=True)

# =============================================================================
# 🎯 DRILL SYSTEM
# =============================================================================
QUESTIONS = [
    {"q": "What is Stack?", "a": "LIFO"},
    {"q": "Binary Search complexity?", "a": "O(log n)"}
]

def drill():
    st.header("🎯 Smart Drill")

    if st.button("Generate Question"):
        st.session_state.q = random.choice(QUESTIONS)

    if "q" in st.session_state:
        st.info(st.session_state.q["q"])

        if st.button("Show Answer"):
            st.success(st.session_state.q["a"])

# =============================================================================
# 🏋️ FITNESS
# =============================================================================
def fitness():
    st.header("🏋️ Fitness System")

    st.markdown("""
    ### 💪 Daily Routine
    - Pushups (3x15)
    - Squats (3x15)
    - Situps (3x15)
    - Cardio
    """)

    if st.checkbox("Completed Today"):
        st.success("Great job! 🔥")

# =============================================================================
# 🚀 MAIN
# =============================================================================
def main():
    load_ui()
    vault = VaultSystem()

    menu = ["Dashboard", "Academic", "Formula", "Drill", "Fitness"]
    choice = st.sidebar.radio("Navigation", menu)

    if choice == "Dashboard":
        dashboard()
    elif choice == "Academic":
        academic(vault)
    elif choice == "Formula":
        formula()
    elif choice == "Drill":
        drill()
    elif choice == "Fitness":
        fitness()

if __name__ == "__main__":
    main()
