const appState = {
    subjects: [
        { name: "Maths", mid1: 15, target: 27, color: "#3b82f6" },
        { name: "BEE", mid1: 8, target: 28, color: "#ef4444" },
        { name: "Chemistry", mid1: 14, target: 26, color: "#10b981" }
    ],
    // Syllabus data from your provided plan
    units: [
        { sub: "BEE", unit: 3, topic: "Transformers & Losses", status: 0 },
        { sub: "DS", unit: 4, topic: "Graphs & Sorting", status: 0 }
    ]
};

// Function to calculate "Survival Marks"
function calculateTargets() {
    return appState.subjects.map(s => {
        const remaining = 30 - s.mid1;
        const urgency = s.mid1 < 10 ? "CRITICAL" : "RECOVERY";
        return { ...s, urgency };
    });
}

// Render the Dashboard
function renderDashboard() {
    const container = document.getElementById('main-content');
    const targets = calculateTargets();
    
    container.innerHTML = targets.map(s => `
        <div class="card">
            <div style="display:flex; justify-content:space-between">
                <h3>${s.name}</h3>
                <span class="tag">${s.urgency}</span>
            </div>
            <p>1st Mid: ${s.mid1}/30</p>
            <div class="progress-bar-bg">
                <div class="progress-fill" style="width: ${(s.mid1/30)*100}%; background: ${s.color}"></div>
            </div>
            <small>Need ${s.target}+ in 2nd Mid to secure 8.5 CGPA</small>
        </div>
    `).join('');
}
