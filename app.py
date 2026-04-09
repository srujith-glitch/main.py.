import streamlit as st
import os
import time
import json
from datetime import datetime, timedelta
from pathlib import Path
import hashlib
import random

# =============================================================================
# 🚀 SRUJITH-GLITCH OS v3.0 - PROFESSIONAL ACADEMIC COMMAND CENTER
# =============================================================================

class SrujithVaultOS:
    def __init__(self):
        self.VAULT_ROOT = "srujith_vault"
        self.SECTIONS = ["📚 Material Section", "🧪 Formula Section", "🏋️ Fitness Logs"]
        self.SUBJECTS = ["BEE", "Data Structures", "Maths (ODVC)", "Chemistry", "Drawing"]
        self.init_vault_structure()
        self.load_user_progress()
    
    def init_vault_structure(self):
        """Initialize professional vault directory structure"""
        for section in self.SECTIONS:
            for subject in self.SUBJECTS:
                section_path = section.replace(" ", "_").replace("📚", "").replace("🧪", "").replace("🏋️", "").strip()
                path = Path(self.VAULT_ROOT) / section_path / subject.replace(" ", "_")
                path.mkdir(parents=True, exist_ok=True)
        
        # Create metadata files
        metadata_path = Path(self.VAULT_ROOT) / "metadata"
        metadata_path.mkdir(exist_ok=True)
        (metadata_path / "progress.json").touch()
        (metadata_path / "analytics.json").touch()
    
    def save_to_vault(self, uploaded_file, section, subject):
        """Secure file storage with metadata tracking"""
        section_clean = section.replace(" ", "_").replace("📚", "").replace("🧪", "").replace("🏋️", "").strip()
        target_dir = Path(self.VAULT_ROOT) / section_clean / subject.replace(" ", "_")
        
        # Generate unique filename with hash to prevent overwrites
        file_hash = hashlib.md5(uploaded_file.getvalue()).hexdigest()[:8]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ext = Path(uploaded_file.name).suffix
        safe_name = f"{timestamp}_{file_hash}{ext}"
        file_path = target_dir / safe_name
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        
        # Update metadata
        self.update_file_metadata(section, subject, safe_name)
        return str(file_path)
    
    def list_vault_files(self, section, subject):
        """List files with metadata"""
        section_clean = section.replace(" ", "_").replace("📚", "").replace("🧪", "").replace("🏋️", "").strip()
        target_dir = Path(self.VAULT_ROOT) / section_clean / subject.replace(" ", "_")
        return [f for f in target_dir.iterdir() if f.is_file()]
    
    def update_file_metadata(self, section, subject, filename):
        """Track file uploads for analytics"""
        metadata_path = Path(self.VAULT_ROOT) / "metadata" / "analytics.json"
        analytics = self.load_json(metadata_path)
        
        section_key = section.replace(" ", "_").replace("📚", "").replace("🧪", "").replace("🏋️", "").strip()
        if section_key not in analytics:
            analytics[section_key] = {}
        if subject not in analytics[section_key]:
            analytics[section_key][subject] = []
        
        analytics[section_key][subject].append({
            "file": filename,
            "timestamp": datetime.now().isoformat(),
            "size": len(filename)  # Simplified size tracking
        })
        
        self.save_json(metadata_path, analytics)
    
    def load_json(self, path):
        """Safe JSON loading"""
        try:
            return json.loads(path.read_text()) if path.exists() else {}
        except:
            return {}
    
    def save_json(self, path, data):
        """Safe JSON saving"""
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2))
    
    def load_user_progress(self):
        """Load persistent user progress"""
        progress_path = Path(self.VAULT_ROOT) / "metadata" / "progress.json"
        return self.load_json(progress_path)
    
    def save_user_progress(self, progress):
        """Save user progress"""
        progress_path = Path(self.VAULT_ROOT) / "metadata" / "progress.json"
        self.save_json(progress_path, progress)

# Initialize OS
os_system = SrujithVaultOS()

# =============================================================================
# 📊 ACADEMIC DATA SYSTEM
# =============================================================================
ACADEMIC_BENCHMARKS = {
    "BEE": {
        "formulas": [
            {"title": "Transformer EMF", "formula": "E = 4.44 f N Φ_m", "ref": "Page 36"},
            {"title": "Power", "formula": "P = VI = I²R = V²/R", "ref": "Page 38"},
            {"title": "Impedance", "formula": "Z = √(R² + (X_L - X_C)²)", "ref": "Page 49"}
        ],
        "drill_questions": [
            {"q": "Derive Transformer EMF Equation", "answer": "E = 4.44 f N Φ_m"},
            {"q": "Power dissipation in resistor", "answer": "P = I²R"}
        ]
    },
    "Data Structures": {
        "formulas": [
            {"title": "Binary Search", "formula": "O(log n)", "ref": "Page 27"},
            {"title": "AVL Balance", "formula": "BF = h_L - h_R", "ref": "Page 33"}
        ],
        "drill_questions": [
            {"q": "Stack PUSH algorithm", "answer": "Check overflow → Top++ → Insert"},
            {"q": "Binary Search complexity", "answer": "O(log n)"}
        ]
    },
    "Maths (ODVC)": {
        "formulas": [
            {"title": "Linear DE", "formula": "dy/dx + Py = Q", "ref": "Page 13"},
            {"title": "Dot Product", "formula": "A·B = AB cosθ", "ref": "Page 17"}
        ]
    },
    "Chemistry": {
        "formulas": [
            {"title": "Nernst Equation", "formula": "E = E° - (0.0591/n)logQ", "ref": "Page 3"},
            {"title": "Gibbs Energy", "formula": "ΔG = -nFE", "ref": "Page 6"}
        ]
    }
}

# =============================================================================
# 🎨 PROFESSIONAL UI SYSTEM
# =============================================================================
def init_professional_ui():
    st.set_page_config(
        page_title="🛡️ Srujith-Glitch OS v3.0", 
        layout="wide", 
        page_icon="🛡️",
        initial_sidebar_state="expanded"
    )
    
    # Professional CSS Framework
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@400;500;600;700&display=swap');
    
    .main { 
        background: linear-gradient(135deg, #0a0e17 0%, #1a1f2e 50%, #16213e 100%); 
        color: #e6edf3; 
        font-family: 'Inter', sans-serif;
        padding-top: 2rem;
    }
    
    h1 { 
        font-family: 'JetBrains Mono', monospace; 
        font-weight: 700; 
        color: #00d4ff; 
        text-shadow: 0 0 20px rgba(0,212,255,0.3);
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: rgba(22,27,34,0.8); 
        border: 1px solid #30363d; 
        border-radius: 16px; 
        padding: 1.5rem; 
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        border-color: #00d4ff;
        box-shadow: 0 10px 30px rgba(0,212,255,0.2);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #00d4ff 0%, #0099ff 100%);
        color: white !important;
        border: none;
        border-radius: 12px;
        font-weight: 600;
        font-family: 'JetBrains Mono', monospace;
        height: 3.2rem;
        padding: 0 2rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,212,255,0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,212,255,0.4);
    }
    
    .section-header {
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
        color: #58a6ff;
        border-bottom: 2px solid #30363d;
        padding-bottom: 1rem;
        margin-bottom: 2rem;
        position: relative;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: -2px;
        left: 0;
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, #00d4ff, #58a6ff);
        border-radius: 2px;
    }
    
    .formula-card {
        background: rgba(13,17,23,0.9);
        border: 1px solid #58a6ff;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        backdrop-filter: blur(10px);
    }
    
    .status-badge {
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: 600;
        font-size: 0.85rem;
    }
    
    .status-completed { background: rgba(34,134,54,0.2); color: #58a6ff; border: 1px solid #238636; }
    .status-pending { background: rgba(48,54,61,0.5); color: #8b949e; border: 1px solid #30363d; }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #0a0e17 0%, #1a1f2e 100%);
    }
    </style>
    """, unsafe_allow_html=True)

# =============================================================================
# 📈 ANALYTICS DASHBOARD
# =============================================================================
def analytics_dashboard():
    st.markdown('<h2 class="section-header">📊 Vault Analytics</h2>', unsafe_allow_html=True)
    
    analytics = os_system.load_json(Path(os_system.VAULT_ROOT) / "metadata" / "analytics.json")
    
    col1, col2 = st.columns(2)
    
    with col1:
        total_files = sum(len(files) for section in analytics.values() for files in section.values())
        st.metric("💾 Total Files", total_files)
    
    with col2:
        unique_subjects = len(set(subject for section in analytics.values() for subject in section.keys()))
        st.metric("📚 Active Subjects", unique_subjects)

# =============================================================================
# 🎯 MAIN PAGES
# =============================================================================
def master_day_plan():
    st.markdown('<h2 class="section-header">🚀 12-Hour Strategic Roadmap</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3 style='color: #f85149; margin: 0;'>06:00 AM</h3>
            <p style='color: #8b949e; margin: 0.5rem 0;'>Fitness Protocol</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.checkbox("✅ Morning Mobility Complete"):
            st.markdown('<span class="status-badge status-completed">ACHIEVED</span>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3 style='color: #00d4ff; margin: 0;'>06:00 PM</h3>
            <p style='color: #8b949e; margin: 0.5rem 0;'>Academic Deep Dive</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.checkbox("✅ Study Session Complete"):
            st.markdown('<span class="status-badge status-completed">ACHIEVED</span>', unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3 style='color: #58a6ff; margin: 0;'>09:00 PM</h3>
            <p style='color: #8b949e; margin: 0.5rem 0;'>Cyber Security</p>
        </div>
        """, unsafe_allow_html=True)

def formula_vault():
    st.markdown('<h2 class="section-header">🧪 Formula Reference System</h2>', unsafe_allow_html=True)
    
    f_sub = st.selectbox("Subject:", os_system.SUBJECTS)
    
    # Academic Benchmarks
    st.markdown(f'<h3 style="color: #58a6ff;">📖 {f_sub} Core Formulas</h3>', unsafe_allow_html=True)
    
    if f_sub in ACADEMIC_BENCHMARKS and ACADEMIC_BENCHMARKS[f_sub].get("formulas"):
        for formula in ACADEMIC_BENCHMARKS[f_sub]["formulas"]:
            st.markdown(f"""
            <div class="formula-card">
                <h4 style='margin: 0 0 0.5rem 0; color: #00d4ff;'>{formula['title']}</h4>
                <div style='font-size: 1.3rem; font-family: monospace; color: #ffffff; margin-bottom: 0.5rem;'>
                    ${formula['formula']}$
                </div>
                <span style='color: #8b949e; font-size: 0.9rem;'>Ref: {formula['ref']}</span>
            </div>
            """, unsafe_allow_html=True)
    
    # Vault Files
    vault_files = os_system.list_vault_files("🧪 Formula Section", f_sub)
    if vault_files:
        st.markdown("---")
        st.markdown(f'<h3 class="section-header">💾 My Formula Files ({len(vault_files)})</h3>', unsafe_allow_html=True)
        for file_path in vault_files:
            st.info(f"📄 {file_path.name}")

def academic_vault():
    st.markdown('<h2 class="section-header">📚 Academic Resource Hub</h2>', unsafe_allow_html=True)
    
    m_sub = st.selectbox("Subject:", os_system.SUBJECTS)
    
    vault_files = os_system.list_vault_files("📚 Material Section", m_sub)
    if vault_files:
        st.markdown(f'<h3 class="section-header">{m_sub} Faculty Materials ({len(vault_files)})</h3>', unsafe_allow_html=True)
        for file_path in vault_files:
            st.success(f"📘 {file_path.name}")
    else:
        st.info("👆 Upload materials using the sidebar to populate this vault.")

def syllabus_drill():
    st.markdown('<h2 class="section-header">🎯 Syllabus Drill Master</h2>', unsafe_allow_html=True)
    
    drill_sub = st.selectbox("Subject:", ["BEE", "Data Structures"])
    
    if st.button("🎲 Generate Drill Question", use_container_width=True):
        if drill_sub in ACADEMIC_BENCHMARKS and ACADEMIC_BENCHMARKS[drill_sub].get("drill_questions"):
            q_data = random.choice(ACADEMIC_BENCHMARKS[drill_sub]["drill_questions"])
            st.session_state.current_drill = q_data
            st.session_state.show_answer = False
            st.rerun()
    
    if "current_drill" in st.session_state:
        st.markdown(f"""
        <div class="metric-card" style='text-align: center; padding: 2rem;'>
            <h3 style='color: #f85149; margin-bottom: 1rem;'>QUESTION</h3>
            <div style='font-size: 1.3rem; font-weight: 500; color: #ffffff;'>
                {st.session_state.current_drill['q']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        user_answer = st.text_area("💭 Your Solution:", height=120)
        
        col1, col2 = st.columns([3,1])
        with col2:
            if st.button("✅ Verify Answer", use_container_width=True):
                st.session_state.show_answer = True
                st.rerun()
        
        if st.session_state.get("show_answer", False):
            st.markdown(f"""
            <div class="metric-card" style='background: linear-gradient(135deg, rgba(34,134,54,0.2), rgba(88,166,255,0.1)); 
                     border-left: 5px solid #238636;'>
                <h3 style='color: #238636; margin-bottom: 1rem;'>✅ ANSWER KEY</h3>
                <div style='font-size: 1.2rem; font-family: monospace; color: #ffffff; font-weight: 500;'>
                    {st.session_state.current_drill['answer']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.success("💡 Next Topic: Review related concepts and practice variations!")

def fitness_moto():
    st.markdown('<h2 class="section-header">🏋️ Fitness & Motivation</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3 style='color: #f85149; margin: 0;'>🎯 TARGET</h3>
            <h2 style='color: #00d4ff; margin: 0.5rem 0;'>80kg</h2>
            <p style='color: #8b949e;'>Yamaha FZ-X Reward</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        ### 💪 Daily Protocol
        - **3x15
