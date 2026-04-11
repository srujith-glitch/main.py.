// This is your data store
const appState = {
    subjects: [
        { name: "Maths", mid1: 15, target: 27, color: "#3b82f6" },
        { name: "BEE", mid1: 8, target: 28, color: "#ef4444" },
        { name: "Chemistry", mid1: 14, target: 26, color: "#10b981" },
        { name: "DS", mid1: 15, target: 25, color: "#8b5cf6" },
        { name: "Drawing", mid1: 15, target: 25, color: "#f59e0b" }
    ]
};

// This function clears the screen and shows the 'Marks' tab
function showTab(tabName) {
    const main = document.getElementById('app-content');
    
    if (tabName === 'marks') {
        renderMarks(main);
    } else {
        main.innerHTML = `<div class="card"><h2>${tabName.toUpperCase()}</h2><p>Coming soon...</p></div>`;
    }
    
    // Update active button
    document.querySelectorAll('.nav-item').forEach(btn => {
        btn.classList.remove('active');
        if(btn.innerText.toLowerCase() === tabName) btn.classList.add('active');
    });
}

function renderMarks(container) {
    let html = `
        <div class="alert">
            <strong>Lab Focus:</strong> Chem Lab (Wed) & DS Lab (Fri). 
            Don't worry about theory until Saturday.
        </div>
    `;

    appState.subjects.forEach(s => {
        const pct = Math.round((s.mid1 / 30) * 100);
        html += `
            <div class="card">
                <div style="display:flex; justify-content:space-between; align-items:center">
                    <h3 style="margin:0">${s.name}</h3>
                    <span class="tag" style="background:${s.color}22; color:${s.color}">${s.mid1}/30</span>
                </div>
                <div class="progress-bg">
                    <div class="progress-fill" style="width: ${pct}%; background: ${s.color}"></div>
                </div>
                <p style="font-size:12px; color:#94a3b8; margin-top:8px">
                    Target for 2nd Mid: <b>${s.target}+</b>
                </p>
            </div>
        `;
    });

    container.innerHTML = html;
}

// Start the app on the Marks tab
document.addEventListener('DOMContentLoaded', () => {
    showTab('marks');
    document.getElementById('current-date').innerText = new Date().toDateString();
});
