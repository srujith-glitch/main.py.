<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Srujith-Glitch Control</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#0d1117;--bg2:#161b22;--bg3:#21262d;--border:#30363d;
  --accent:#58a6ff;--green:#3fb950;--red:#f85149;--gold:#e3b341;
  --purple:#d2a8ff;--orange:#ffa657;--text:#e6edf3;--text2:#8b949e;
}
body{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;font-size:14px;display:flex;min-height:100vh}

/* SIDEBAR */
.sb{width:200px;background:var(--bg2);border-right:1px solid var(--border);flex-shrink:0;display:flex;flex-direction:column;position:sticky;top:0;height:100vh;overflow-y:auto}
.sb-brand{padding:14px 14px 12px;border-bottom:1px solid var(--border)}
.sb-brand h2{font-size:12px;font-weight:800;color:var(--accent);letter-spacing:.08em}
.sb-brand p{font-size:10px;color:var(--text2);margin-top:2px}
.nav{padding:6px 0}
.ni{display:flex;align-items:center;gap:9px;padding:8px 14px;cursor:pointer;border-left:3px solid transparent;color:var(--text2);font-size:12px;transition:all .15s}
.ni:hover{background:var(--bg3);color:var(--text)}
.ni.active{border-left-color:var(--accent);background:rgba(88,166,255,.08);color:var(--accent)}
.ni-icon{font-size:14px;width:16px;text-align:center}

/* MAIN */
.main{flex:1;padding:18px;overflow-y:auto;max-width:900px}
.page{display:none}.page.active{display:block}
.pt{font-size:19px;font-weight:700;margin-bottom:3px}
.ps{font-size:12px;color:var(--text2);margin-bottom:16px}

/* CARDS */
.card{background:var(--bg2);border:1px solid var(--border);border-radius:8px;padding:14px;margin-bottom:12px}
.ct{font-size:13px;font-weight:600;margin-bottom:10px;color:var(--text)}

/* GRIDS */
.g2{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px}

/* STAT */
.stat{background:var(--bg3);border-radius:6px;padding:10px;text-align:center}
.snum{font-size:20px;font-weight:700}
.slbl{font-size:10px;color:var(--text2);margin-top:2px}

/* BADGES */
.badge{display:inline-block;padding:2px 7px;border-radius:10px;font-size:10px;font-weight:700}
.br{background:rgba(248,81,73,.15);color:var(--red)}
.bg{background:rgba(63,185,80,.15);color:var(--green)}
.bb{background:rgba(88,166,255,.15);color:var(--accent)}
.bp{background:rgba(210,168,255,.15);color:var(--purple)}
.bo{background:rgba(255,166,87,.15);color:var(--orange)}

/* TABS */
.tabs{display:flex;gap:5px;flex-wrap:wrap;margin-bottom:14px}
.tab{padding:5px 12px;border-radius:16px;border:1px solid var(--border);background:transparent;color:var(--text2);cursor:pointer;font-size:11px;transition:all .15s}
.tab:hover{border-color:var(--accent);color:var(--accent)}
.tab.active{background:var(--accent);color:#000;border-color:var(--accent);font-weight:700}

/* BOXES */
.warn{border-left:3px solid var(--red);background:rgba(248,81,73,.06);border-radius:0 6px 6px 0;padding:9px 12px;margin-bottom:10px;font-size:12px}
.tip{border-left:3px solid var(--orange);background:rgba(255,166,87,.06);border-radius:0 6px 6px 0;padding:9px 12px;margin-bottom:10px;font-size:12px}
.ok{border-left:3px solid var(--green);background:rgba(63,185,80,.06);border-radius:0 6px 6px 0;padding:9px 12px;margin-bottom:10px;font-size:12px}
.info{border-left:3px solid var(--accent);background:rgba(88,166,255,.06);border-radius:0 6px 6px 0;padding:9px 12px;margin-bottom:10px;font-size:12px}

/* FORMULA */
.fbox{background:var(--bg);border:1px solid var(--accent);border-radius:6px;padding:11px;margin-bottom:9px;font-family:'Courier New',monospace;font-size:12px;line-height:1.7}
.flbl{font-size:10px;color:var(--purple);font-weight:700;margin-bottom:5px;font-family:'Segoe UI',sans-serif;text-transform:uppercase;letter-spacing:.06em}

/* DEDP */
.dedp{display:grid;grid-template-columns:1fr 1fr;gap:7px;margin-bottom:12px}
.dc{background:var(--bg3);border-radius:6px;padding:10px}
.dc h5{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px}
.dc p,.dc ul{font-size:11px;color:var(--text2);line-height:1.6}
.dc ul{padding-left:14px}
.dd{border-top:2px solid var(--accent)}.de{border-top:2px solid var(--green)}
.dd2{border-top:2px solid var(--purple)}.dp{border-top:2px solid var(--orange)}

/* ACCORDION */
.acc{border:1px solid var(--border);border-radius:7px;margin-bottom:8px;overflow:hidden}
.acc-hd{padding:10px 13px;cursor:pointer;display:flex;justify-content:space-between;align-items:center;font-size:12px;font-weight:600;background:var(--bg2)}
.acc-hd:hover{background:var(--bg3)}
.acc-bd{padding:12px 13px;border-top:1px solid var(--border);display:none}
.acc-bd.open{display:block}

/* EXAM Q */
.eq{background:var(--bg3);border-radius:6px;padding:11px;margin-bottom:8px}
.eq-q{font-size:12px;font-weight:600;margin-bottom:6px}
.eq-a{font-size:11px;color:var(--text2);line-height:1.6}
.eq-marks{float:right}

/* RULES */
.rl{padding:7px 0;border-bottom:1px solid var(--border);font-size:12px}
.rl:last-child{border:none}
.rn{font-weight:700;color:var(--accent);margin-right:6px}

/* PROGRESS */
.pb{background:var(--bg3);border-radius:4px;height:7px;overflow:hidden;margin-top:5px}
.pf{height:100%;border-radius:4px;transition:width .5s}

/* TASKS */
.task{display:flex;align-items:center;gap:8px;padding:8px 10px;background:var(--bg3);border-radius:5px;margin-bottom:6px;cursor:pointer}
.task input{width:14px;height:14px;accent-color:var(--green);cursor:pointer}
.task.done{opacity:.5}.task.done span{text-decoration:line-through}

/* SVG DIAGRAMS */
.diag-wrap{background:var(--bg);border:1px solid var(--border);border-radius:8px;padding:14px;margin-bottom:12px;text-align:center}
.diag-title{font-size:12px;font-weight:600;color:var(--purple);margin-bottom:10px;text-align:left}
svg text{font-family:'Courier New',monospace}

/* CYBER STEPS */
.cstep{background:var(--bg3);border-radius:6px;padding:11px;margin-bottom:7px;display:flex;gap:10px}
.csn{width:26px;height:26px;border-radius:50%;background:var(--accent);color:#000;font-weight:800;font-size:12px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.cst h4{font-size:12px;font-weight:600;margin-bottom:3px}
.cst p{font-size:11px;color:var(--text2)}

/* TIMELINE */
.tl{display:flex;gap:10px;margin-bottom:10px;padding-bottom:10px;border-bottom:1px solid var(--border)}
.tl-time{font-size:11px;font-weight:700;color:var(--accent);min-width:75px;padding-top:1px}
.tl-body h4{font-size:12px;font-weight:600;margin-bottom:2px}
.tl-body p{font-size:11px;color:var(--text2)}

/* INPUTS */
select,input[type=text]{background:var(--bg3);border:1px solid var(--border);border-radius:5px;padding:6px 9px;color:var(--text);font-size:12px;width:100%;margin-bottom:8px}
.btn{padding:7px 14px;border-radius:5px;border:1px solid var(--accent);background:rgba(88,166,255,.1);color:var(--accent);cursor:pointer;font-size:12px;font-weight:600;transition:all .15s}
.btn:hover{background:var(--accent);color:#000}
.btn-g{border-color:var(--green);color:var(--green);background:rgba(63,185,80,.1)}
.btn-g:hover{background:var(--green);color:#000}

.confetti{background:linear-gradient(135deg,rgba(63,185,80,.12),rgba(88,166,255,.08));border:1px solid var(--green);border-radius:7px;padding:14px;text-align:center;display:none;margin-top:10px}
.confetti.show{display:block}

@media(max-width:640px){
  .sb{width:52px}
  .ni span{display:none}
  .sb-brand{display:none}
  .g2,.g3{grid-template-columns:1fr}
  .dedp{grid-template-columns:1fr}
}
</style>
</head>
<body>

<!-- SIDEBAR -->
<div class="sb">
  <div class="sb-brand">
    <h2>SRUJITH-GLITCH</h2>
    <p>B.Tech CSE · R25 · SNIST</p>
  </div>
  <div class="nav">
    <div class="ni active" onclick="pg('roadmap',this)"><span class="ni-icon">🗺️</span><span>Roadmap</span></div>
    <div class="ni" onclick="pg('schedule',this)"><span class="ni-icon">📅</span><span>Daily Plan</span></div>
    <div class="ni" onclick="pg('exams',this)"><span class="ni-icon">📝</span><span>Exam + Answers</span></div>
    <div class="ni" onclick="pg('formulas',this)"><span class="ni-icon">🧪</span><span>Formulas</span></div>
    <div class="ni" onclick="pg('diagrams',this)"><span class="ni-icon">🔷</span><span>Diagrams (SVG)</span></div>
    <div class="ni" onclick="pg('dedp',this)"><span class="ni-icon">✍️</span><span>D-E-D-P All Units</span></div>
    <div class="ni" onclick="pg('cyber',this)"><span class="ni-icon">🛡️</span><span>Cybersecurity</span></div>
    <div class="ni" onclick="pg('fitness',this)"><span class="ni-icon">🏋️</span><span>Fitness + Bike</span></div>
    <div class="ni" onclick="pg('books',this)"><span class="ni-icon">📚</span><span>Books + AI</span></div>
  </div>
</div>

<!-- MAIN -->
<div class="main">

<!-- ======= ROADMAP ======= -->
<div id="page-roadmap" class="page active">
<div class="pt">🗺️ Comeback Roadmap</div>
<div class="ps">Mid-1 done · Mid-2: June 4 · End Sem: June 22 · Target: 8.5–9.0 CGPA</div>

<div class="g3" style="margin-bottom:14px">
  <div class="stat"><div class="snum" style="color:var(--red)">8</div><div class="slbl">BEE /25 🔴 Red Zone</div></div>
  <div class="stat"><div class="snum" style="color:var(--gold)">14</div><div class="slbl">Chemistry /25</div></div>
  <div class="stat"><div class="snum" style="color:var(--gold)">15</div><div class="slbl">Drawing /25</div></div>
  <div class="stat"><div class="snum" style="color:var(--gold)">15</div><div class="slbl">DS /25</div></div>
  <div class="stat"><div class="snum" style="color:var(--green)">25</div><div class="slbl">ODVC /25 ✓</div></div>
  <div class="stat"><div class="snum" style="color:var(--accent)">77</div><div class="slbl">Total /125</div></div>
</div>

<div class="warn"><strong>Root cause of all lost marks:</strong> Paragraphs instead of Diagrams + Equations + Bullet points. Fix = D-E-D-P format on every 5-mark answer.</div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>📌 Phase 1 · Now → May 17 (College Days)</span><span>▼</span></div>
<div class="acc-bd open">
  <div class="rl"><span class="rn">Daily Rule</span>3 tasks only: Gym + 1 D-E-D-P topic + 10 min Cyber video</div>
  <div class="rl"><span class="rn">Priority</span>BEE first (circuit diagrams + theorems) → Chemistry equations → 3 ODVC problems/day</div>
  <div class="rl"><span class="rn">1-3-7</span>Every new concept: review on Day 1, Day 3, Day 7. Tick box on note page.</div>
  <div class="rl"><span class="rn">Drawing</span>Read question TWICE. Visualize 3D object before pencil touches paper.</div>
  <div class="rl"><span class="rn">DS Lab</span>Next Friday: Cycles 1,2,3,4,5,8,10. AVL = draw all 4 rotations from memory.</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>🌴 Phase 2 · May 18–30 (Summer Vacation)</span><span>▼</span></div>
<div class="acc-bd">
  <div class="rl"><span class="rn">09:00 AM</span>Deep Work 4 hrs — BEE theorems + Chemistry reactions (brain is freshest)</div>
  <div class="rl"><span class="rn">02:00 PM</span>Cyber Security Sprint — 2 hrs (double normal)</div>
  <div class="rl"><span class="rn">Evening</span>Totally free. No guilt. This is mandatory recovery.</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>🔥 Phase 3 · June 1–3 (Pre-Mid-2 Blitz)</span><span>▼</span></div>
<div class="acc-bd">
  <div class="rl"><span class="rn">June 1</span>All BEE D-E-D-P notes. Draw every circuit from memory.</div>
  <div class="rl"><span class="rn">June 2</span>All Chemistry equations + diagrams. Galvanic cell, Li-ion, corrosion.</div>
  <div class="rl"><span class="rn">June 3</span>DS trees + Drawing keyword guide + ODVC formula page. Sleep 10 PM.</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>🎯 Phase 4 · June 22+ End Semester</span><span>▼</span></div>
<div class="acc-bd">
  <div class="rl"><span class="rn">BEE</span>Electrical machines: DC motor, Induction motor, Transformer — all diagrams</div>
  <div class="rl"><span class="rn">DS</span>Graphs, Hashing, File Organization — write algorithms on paper</div>
  <div class="rl"><span class="rn">ODVC</span>Green's, Stokes', Gauss' — statement + formula on one page each</div>
  <div class="rl"><span class="rn">Chemistry</span>Polymers, Fuels, Lubricants — Unit IV & V needs diagrams too</div>
  <div class="rl"><span class="rn">Drawing</span>Isometric views + Sections of Solids — practice 2 per day</div>
</div></div>
</div>

<!-- ======= SCHEDULE ======= -->
<div id="page-schedule" class="page">
<div class="pt">📅 Daily Plan</div>
<div class="ps">3-mode schedule — Weekday / Holiday / Sunday Cheat Day</div>

<div class="tabs">
  <button class="tab active" onclick="sw('sched','weekday',this)">📚 Weekday</button>
  <button class="tab" onclick="sw('sched','holiday',this)">🌴 Holiday</button>
  <button class="tab" onclick="sw('sched','sunday',this)">😴 Sunday Cheat</button>
</div>

<div id="sched-weekday">
  <div class="tip">The 3-task rule: Complete just these 3. Anytime after 5 PM. No fixed clock — just finish them.</div>
  <div id="daily-tasks">
    <div class="task" onclick="chk(this,true)"><input type="checkbox"><span>🏋️ <strong>Gym</strong> — 20 min incline walk + 40 min weights (6 AM)</span></div>
    <div class="task" onclick="chk(this,true)"><input type="checkbox"><span>📖 <strong>1 D-E-D-P topic</strong> — Worst subject first. Write diagram + equation + points.</span></div>
    <div class="task" onclick="chk(this,true)"><input type="checkbox"><span>🛡️ <strong>10 min Cyber Security video</strong> — For the FZ-X. This is non-negotiable.</span></div>
  </div>
  <div class="confetti" id="congrats">🎉 All 3 tasks DONE! That's a win. Rest now. The bike gets closer.</div>
  <div class="card" style="margin-top:14px">
    <div class="ct">Full Weekday Timeline</div>
    <div class="tl"><div class="tl-time">06:00 AM</div><div class="tl-body"><h4>Gym & Fitness</h4><p>20 min incline walk + 40 min compound weights. >100 kg = consistency over intensity.</p></div></div>
    <div class="tl"><div class="tl-time">07:30 AM</div><div class="tl-body"><h4>Morning Routine</h4><p>High-protein breakfast, shower, commute to SNIST.</p></div></div>
    <div class="tl"><div class="tl-time">09:00 AM</div><div class="tl-body"><h4>College</h4><p>Stay engaged. Finish assignments in free periods — don't bring them home.</p></div></div>
    <div class="tl"><div class="tl-time">05:00 PM</div><div class="tl-body"><h4>Reset</h4><p>Home, snack, 30 min decompress. No guilt.</p></div></div>
    <div class="tl"><div class="tl-time">06:00 PM</div><div class="tl-body"><h4>Core Study (D-E-D-P)</h4><p>BEE circuits + Chemistry equations. Write diagrams — NOT paragraphs.</p></div></div>
    <div class="tl"><div class="tl-time">08:00 PM</div><div class="tl-body"><h4>1-3-7 Revision Block</h4><p>Review: what you learned 1 day ago, 3 days ago, 7 days ago. 45 min max.</p></div></div>
    <div class="tl"><div class="tl-time">08:45 PM</div><div class="tl-body"><h4>Dinner + Short Walk</h4><p>15 min walk clears brain fog and helps digest.</p></div></div>
    <div class="tl"><div class="tl-time">09:30 PM</div><div class="tl-body"><h4>Cyber Security</h4><p>One video / one concept. Linux, Networking, Ethical Hacking.</p></div></div>
    <div class="tl" style="border:none;margin:0"><div class="tl-time">10:15 PM</div><div class="tl-body"><h4>Read 2 Pages + Sleep</h4><p>"How to Win Friends" — 2 pages only. No screen. Sleep.</p></div></div>
  </div>
</div>

<div id="sched-holiday" style="display:none">
  <div class="ok"><strong>Summer Vacation (May 18–May 30)</strong> — Flip to morning deep work when brain is freshest.</div>
  <div class="card">
    <div class="tl"><div class="tl-time">06:00 AM</div><div class="tl-body"><h4>Gym</h4><p>Same routine. Don't skip just because there's no college.</p></div></div>
    <div class="tl"><div class="tl-time">09:00 AM</div><div class="tl-body"><h4>Deep Work (4 hrs)</h4><p>BEE theorems + Chemistry reactions. Peak focus window. No phone.</p></div></div>
    <div class="tl"><div class="tl-time">01:00 PM</div><div class="tl-body"><h4>Lunch + Rest</h4><p>Eat well. 30 min nap is fine — consolidates morning learning.</p></div></div>
    <div class="tl"><div class="tl-time">02:00 PM</div><div class="tl-body"><h4>Cyber Security Sprint (2 hrs)</h4><p>Double quota. This is your FZ-X fund time.</p></div></div>
    <div class="tl" style="border:none;margin:0"><div class="tl-time">04:00 PM+</div><div class="tl-body"><h4>Free Evening</h4><p>Totally free. Brain consolidates knowledge even while resting.</p></div></div>
  </div>
</div>

<div id="sched-sunday" style="display:none">
  <div class="ok" style="font-size:14px;text-align:center;padding:20px">
    😴 <strong>SUNDAY = MANDATORY CHEAT DAY</strong><br><br>
    No textbooks. No 1-3-7. No Cyber Security. No diet tracking.<br>Sleep in. Games. Movies. Friends. Eat whatever you want.<br><br>
    <span style="color:var(--green)">This is not optional — your brain NEEDS this to transfer short-term → long-term memory. If you skip Sunday rest, Monday is wasted.</span>
  </div>
</div>
</div>

<!-- ======= EXAMS + ANSWERS ======= -->
<div id="page-exams" class="page">
<div class="pt">📝 Mid-1 Papers + Full Answers</div>
<div class="ps">Your actual exam questions with D-E-D-P formatted answers · 30 marks structure</div>

<div class="tabs">
  <button class="tab active" onclick="sw('exam','ec',this)">Chemistry</button>
  <button class="tab" onclick="sw('exam','bee',this)">BEE</button>
  <button class="tab" onclick="sw('exam','ds',this)">Data Structures</button>
  <button class="tab" onclick="sw('exam','odvc',this)">ODVC</button>
  <button class="tab" onclick="sw('exam','draw',this)">Drawing</button>
</div>

<!-- CHEMISTRY EXAM -->
<div id="exam-ec">
<div class="warn"><strong>Score: 14/30 · Missing: Chemical equations, unit diagrams, point-format answers</strong></div>
<div class="card">
  <div class="ct">Part A — 10×1 = 10 Marks (Short Answers)</div>
  <div class="eq"><div class="eq-q">Q1. Compare soft water with hard water. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Soft water: does not contain dissolved salts of Ca²⁺/Mg²⁺; lathers easily with soap. Hard water: contains dissolved Ca²⁺, Mg²⁺ salts (carbonates, sulphates, chlorides); does not lather; forms scum with soap.</div></div>

  <div class="eq"><div class="eq-q">Q2. Define break point chlorination. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">The point at which sufficient chlorine is added to satisfy all demand (oxidation of organic matter, ammonia) so that residual free chlorine appears in water. Beyond this point, free available chlorine increases linearly.</div></div>

  <div class="eq"><div class="eq-q">Q3. What is sludge in boilers? <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Sludge is a soft, loose, slimy precipitate formed at the bottom of a boiler due to concentration of MgCO₃, MgCl₂, CaCl₂ in boiler water. It does not form a hard scale but reduces heat transfer efficiency.</div></div>

  <div class="eq"><div class="eq-q">Q4. Which direction does water move in reverse osmosis? <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">In reverse osmosis, water moves from the concentrated solution (impure side) to the dilute side (pure water side) — opposite to natural osmosis — by applying high external pressure greater than osmotic pressure.</div></div>

  <div class="eq"><div class="eq-q">Q5. Interpret Pilling-Bedworth rule. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">P-B ratio = Volume of metal oxide / Volume of metal. If P-B ratio &lt; 1: oxide layer is porous → not protective (e.g., Mg). If P-B ratio = 1 to 2: oxide is non-porous → protective (e.g., Al, Cr). If &gt; 2: oxide cracks → non-protective.</div></div>

  <div class="eq"><div class="eq-q">Q6. Why does impure metal corrode faster than pure metal? <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Impure metal contains different metals forming galvanic cells. More electropositive metal acts as anode (corrodes). Larger potential difference between impurities = faster corrosion. Pure metal has no potential difference → no galvanic action → corrodes slower.</div></div>

  <div class="eq"><div class="eq-q">Q7. Distinguish electrolytic cell from electrochemical cell. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Electrochemical cell: converts chemical energy to electrical energy spontaneously (ΔG &lt; 0). Electrolytic cell: converts electrical energy to chemical energy; non-spontaneous (ΔG &gt; 0); external power required.</div></div>

  <div class="eq"><div class="eq-q">Q8. State what EMF is. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">EMF (Electromotive Force) = maximum potential difference between electrodes when no current flows. EMF = E_cathode − E_anode. Unit: Volt. It is the driving force for electron flow in the circuit.</div></div>

  <div class="eq"><div class="eq-q">Q9. Can a primary battery be recharged? <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">No. Primary batteries (e.g., dry cell, zinc-carbon) cannot be recharged. The electrode reactions are irreversible. Once reactants are consumed, the battery is discarded.</div></div>

  <div class="eq"><div class="eq-q">Q10. Justify why fuel cells operate longer than batteries. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Fuel cells operate as long as fuel (H₂, methanol) and oxidant (O₂) are supplied continuously from outside. Batteries have fixed internal reactants that deplete. Fuel cells = continuous external supply → longer operation.</div></div>
</div>

<div class="card">
  <div class="ct">Part B — 4×5 = 20 Marks (D-E-D-P Answers)</div>

  <div class="eq"><div class="eq-q">Q11. Elaborate ion exchange process with neat diagram. <span class="eq-marks badge bg">5M</span></div>
  <div class="dedp">
    <div class="dc dd"><h5 style="color:var(--accent)">D — Definition</h5><p>Ion exchange is a water softening method where Ca²⁺ and Mg²⁺ ions in hard water are exchanged with Na⁺ or H⁺ ions of a resin (zeolite/synthetic resin), producing soft water.</p></div>
    <div class="dc de"><h5 style="color:var(--green)">E — Equation</h5><p>2Na⁺-Resin + Ca²⁺ → Ca²⁺-Resin + 2Na⁺<br>2Na⁺-Resin + Mg²⁺ → Mg²⁺-Resin + 2Na⁺<br>Regeneration: Ca-Resin + 2NaCl → 2Na-Resin + CaCl₂</p></div>
    <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Hard water IN ↓ → Cation Exchanger (Na⁺ resin removes Ca²⁺/Mg²⁺) → Anion Exchanger (OH⁻ resin removes Cl⁻/SO₄²⁻) → Pure/Soft water OUT ↓</p></div>
    <div class="dc dp"><h5 style="color:var(--orange)">P — Points</h5><ul><li>Removes ALL types of hardness</li><li>Produces demineralised water</li><li>Resin regenerated by NaCl (cation) or NaOH (anion)</li><li>Used in pharmaceuticals, power plants</li><li>Better than lime-soda for high purity needs</li></ul></div>
  </div></div>

  <div class="eq"><div class="eq-q">Q14. Analyze mechanism of wet corrosion. <span class="eq-marks badge bg">5M</span></div>
  <div class="dedp">
    <div class="dc dd"><h5 style="color:var(--accent)">D — Definition</h5><p>Wet corrosion is electrochemical degradation of metals in presence of an electrolyte (water/moisture) where anodic and cathodic areas form on the metal surface causing oxidation.</p></div>
    <div class="dc de"><h5 style="color:var(--green)">E — Equation</h5><p>Anode: Fe → Fe²⁺ + 2e⁻<br>Cathode: O₂ + 2H₂O + 4e⁻ → 4OH⁻<br>Fe²⁺ + 2OH⁻ → Fe(OH)₂<br>4Fe(OH)₂ + O₂ + 2H₂O → 4Fe(OH)₃ (Rust)</p></div>
    <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Iron piece in water → Label anodic area (−) where Fe dissolves → cathodic area (+) → e⁻ flow from anode to cathode through metal → OH⁻ migrates toward anode → Rust forms at anodic site</p></div>
    <div class="dc dp"><h5 style="color:var(--orange)">P — Points</h5><ul><li>Requires electrolyte (water/moisture)</li><li>More area difference → faster corrosion</li><li>Acidic environment accelerates corrosion</li><li>Control: cathodic protection, coatings, inhibitors</li><li>Sacrificial anode: Zn or Mg used</li></ul></div>
  </div></div>

  <div class="eq"><div class="eq-q">Q15. Discuss construction and working of methanol-oxygen fuel cell with reactions. <span class="eq-marks badge bg">5M</span></div>
  <div class="dedp">
    <div class="dc dd"><h5 style="color:var(--accent)">D — Definition</h5><p>A DMFC (Direct Methanol Fuel Cell) is an electrochemical device that directly converts chemical energy of methanol oxidation into electrical energy without combustion.</p></div>
    <div class="dc de"><h5 style="color:var(--green)">E — Equation</h5><p>Anode: CH₃OH + H₂O → CO₂ + 6H⁺ + 6e⁻<br>Cathode: 3/2 O₂ + 6H⁺ + 6e⁻ → 3H₂O<br>Overall: CH₃OH + 3/2 O₂ → CO₂ + 2H₂O</p></div>
    <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Anode | Proton Exchange Membrane | Cathode<br>CH₃OH+H₂O → | H⁺ ions pass → | + O₂ from air<br>CO₂+H⁺+e⁻ | (PEM membrane) | → H₂O produced<br>Load connected between anode and cathode externally</p></div>
    <div class="dc dp"><h5 style="color:var(--orange)">P — Points</h5><ul><li>No combustion → high efficiency ~40-60%</li><li>Anode: platinum-ruthenium catalyst</li><li>Cathode: platinum catalyst</li><li>Electrolyte: proton exchange membrane (Nafion)</li><li>Applications: portable electronics, vehicles</li></ul></div>
  </div></div>

  <div class="eq"><div class="eq-q">Q13. Summarize metal-metal insoluble salt electrode (Calomel electrode). <span class="eq-marks badge bg">5M</span></div>
  <div class="dedp">
    <div class="dc dd"><h5 style="color:var(--accent)">D — Definition</h5><p>Calomel electrode is a secondary reference electrode consisting of mercury in contact with mercurous chloride (calomel) paste and KCl solution. Used as reference for pH measurement.</p></div>
    <div class="dc de"><h5 style="color:var(--green)">E — Equation</h5><p>Electrode reaction: Hg₂Cl₂ + 2e⁻ ⇌ 2Hg + 2Cl⁻<br>E = +0.242 V (saturated KCl)<br>E = +0.280 V (1N KCl)<br>E = +0.334 V (0.1N KCl)</p></div>
    <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Pt wire → Mercury (Hg) → Hg₂Cl₂ paste → Saturated KCl solution → Porous plug (salt bridge connection). Glass tube with side arm for KCl refill.</p></div>
    <div class="dc dp"><h5 style="color:var(--orange)">P — Points</h5><ul><li>Stable, reproducible, easy to use</li><li>Cannot be used at high temperatures</li><li>Used in potentiometric titrations</li><li>E depends on KCl concentration</li><li>Connected to unknown cell via salt bridge</li></ul></div>
  </div></div>
</div>
</div>

<!-- BEE EXAM -->
<div id="exam-bee" style="display:none">
<div class="warn"><strong>Score: 8/30 — RED ZONE · Missing: Circuit diagrams in every answer, boxed equations, stepwise working</strong></div>
<div class="card">
  <div class="ct">Part A — 10×1 = 10 Marks</div>
  <div class="eq"><div class="eq-q">Q1. State KCL & KVL. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">KCL: Sum of currents entering a node = Sum of currents leaving. ΣI_in = ΣI_out.<br>KVL: Algebraic sum of all voltages around a closed loop = 0. ΣV = 0 (rise +ve, drop −ve).</div></div>

  <div class="eq"><div class="eq-q">Q2. Write V-I relations of R, L, C. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Resistor: V = IR. Inductor: V = L(di/dt). Capacitor: I = C(dv/dt). These define how each element responds to current/voltage.</div></div>

  <div class="eq"><div class="eq-q">Q3. State Thevenin's Theorem. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Any linear two-terminal network can be replaced by a single voltage source V_th (open circuit voltage) in series with a resistance R_th (with all sources deactivated).</div></div>

  <div class="eq"><div class="eq-q">Q4. Write expression for energy stored in inductor. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">E = ½LI² where L = inductance (Henry), I = current (Ampere). Energy stored in magnetic field of inductor.</div></div>

  <div class="eq"><div class="eq-q">Q5. Define Alternating quantity. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">A quantity that varies sinusoidally with time, alternating in direction/polarity. v(t) = V_m sin(ωt + φ) where V_m = peak value, ω = angular frequency, φ = phase angle.</div></div>

  <div class="eq"><div class="eq-q">Q6. If v(t) = 20sin(50t+25°) find amplitude & frequency. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Amplitude V_m = 20 V. Angular frequency ω = 50 rad/s. Frequency f = ω/2π = 50/2π ≈ 7.96 Hz. Phase angle = 25°.</div></div>

  <div class="eq"><div class="eq-q">Q7. Difference between "balanced" and "unbalanced" system. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Balanced 3-phase: all three voltages equal in magnitude, displaced 120° apart. Unbalanced: magnitudes or phase angles are unequal. Balanced system simplifies to per-phase analysis.</div></div>

  <div class="eq"><div class="eq-q">Q8. Define active power. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Active (Real) Power P = VIcosφ (Watts). It is the actual power consumed/dissipated in resistance. It does useful work. Also called true power.</div></div>

  <div class="eq"><div class="eq-q">Q9. Types of transformers. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Based on voltage: Step-up (N₂>N₁) and Step-down (N₂&lt;N₁). Based on core: Core type and Shell type. Based on phases: Single-phase and Three-phase.</div></div>

  <div class="eq"><div class="eq-q">Q10. Basic function of a transformer. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Transfers electrical energy between two circuits through electromagnetic induction without electrical connection. Changes voltage level while keeping frequency constant. Works on Faraday's law.</div></div>
</div>

<div class="card">
  <div class="ct">Part B — 4×5 = 20 Marks (D-E-D-P Full Answers)</div>

  <div class="eq"><div class="eq-q">Q11. Explain ideal & practical voltage/current sources. Find current in 3Ω using superposition. <span class="eq-marks badge bg">5M</span></div>
  <div class="dedp">
    <div class="dc dd"><h5 style="color:var(--accent)">D — Definition</h5><p>Ideal voltage source: maintains constant voltage regardless of current drawn. Ideal current source: maintains constant current regardless of load. Practical sources have internal resistance r.</p></div>
    <div class="dc de"><h5 style="color:var(--green)">E — Equation</h5><p>Practical V-source: V_terminal = EMF − I×r<br>Superposition: activate one source at a time<br>→ V-source OFF = replace with short circuit<br>→ I-source OFF = replace with open circuit<br>I_total = I₁ + I₂ (algebraic sum)</p></div>
    <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Circuit: 120V source, 6Ω, 3Ω, 4Ω, 12A source in parallel.<br>Step 1: Keep 120V, open 12A → find I₁ in 3Ω<br>Step 2: Keep 12A, short 120V → find I₂ in 3Ω<br>I_3Ω = I₁ ± I₂ (check directions)</p></div>
    <div class="dc dp"><h5 style="color:var(--orange)">P — Points</h5><ul><li>Superposition only for linear circuits</li><li>Power cannot be superimposed (non-linear)</li><li>Each source analyzed independently</li><li>Results algebraically added with direction</li><li>Check polarity marks carefully</li></ul></div>
  </div></div>

  <div class="eq"><div class="eq-q">Q14. Derive delta connected system — line & phase quantities. <span class="eq-marks badge bg">5M</span></div>
  <div class="dedp">
    <div class="dc dd"><h5 style="color:var(--accent)">D — Definition</h5><p>In delta (Δ) connection, each winding is connected end-to-end forming a triangle. Three line terminals A, B, C taken at junctions. No neutral wire in delta.</p></div>
    <div class="dc de"><h5 style="color:var(--green)">E — Equation</h5><p>V_line = V_phase (voltage same across each winding)<br>I_line = √3 × I_phase<br>Phase angle between I_line and I_phase = 30°<br>Power: P = √3 × V_L × I_L × cosφ</p></div>
    <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Draw triangle: A-B-C at corners. Windings: Z_AB, Z_BC, Z_CA. Line currents I_A, I_B, I_C at each terminal. Phase currents I_AB, I_BC, I_CA through windings. Phasor: I_A = I_AB − I_CA.</p></div>
    <div class="dc dp"><h5 style="color:var(--orange)">P — Points</h5><ul><li>No neutral point available</li><li>Line voltage = Phase voltage</li><li>Line current = √3 × Phase current</li><li>Used in motors, power transmission</li><li>Can handle unbalanced loads</li></ul></div>
  </div></div>

  <div class="eq"><div class="eq-q">Q16. Explain principle of operation of single-phase transformer with diagrams. <span class="eq-marks badge bg">5M</span></div>
  <div class="dedp">
    <div class="dc dd"><h5 style="color:var(--accent)">D — Definition</h5><p>A transformer is a static electromagnetic device that transfers electrical energy between two circuits through mutual induction, changing voltage/current levels while keeping frequency constant.</p></div>
    <div class="dc de"><h5 style="color:var(--green)">E — Equation</h5><p>EMF Equation: E = 4.44 × f × N × Φ_m ← BOX THIS<br>Turns ratio: a = N₁/N₂ = V₁/V₂ = I₂/I₁<br>Efficiency: η = P_out/P_in × 100%<br>Losses: Copper loss = I²R, Iron loss = Eddy+Hysteresis</p></div>
    <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>AC supply → Primary coil (N₁ turns) → Iron Core (flux φ) → Secondary coil (N₂ turns) → Load. Show: laminated iron core, primary winding left, secondary right, flux φ arrows in core.</p></div>
    <div class="dc dp"><h5 style="color:var(--orange)">P — Points</h5><ul><li>Works on Faraday's law of electromagnetic induction</li><li>Step-up: N₂&gt;N₁ → V₂&gt;V₁</li><li>Step-down: N₂&lt;N₁ → V₂&lt;V₁</li><li>No moving parts → high reliability</li><li>Core laminated to reduce eddy current losses</li></ul></div>
  </div></div>
</div>
</div>

<!-- DS EXAM -->
<div id="exam-ds" style="display:none">
<div class="ok"><strong>Score: 15/30 · Good on code & definitions. Strengthen: tree diagrams step-by-step, rotation drawings</strong></div>
<div class="card">
  <div class="ct">Part A — 10×1 = 10 Marks</div>
  <div class="eq"><div class="eq-q">Q1. What is a Stack ADT? <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Stack is a linear data structure following LIFO (Last In First Out) principle. Operations: PUSH (insert at top), POP (delete from top), PEEK (view top without removing). Implemented using array or linked list.</div></div>

  <div class="eq"><div class="eq-q">Q2. Applications of queue data structure. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">CPU scheduling (Round Robin), printer spooling, breadth-first search in graphs, handling of requests in web servers, keyboard buffer, simulation of real-world queues.</div></div>

  <div class="eq"><div class="eq-q">Q3. What is a circular linked list? <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">A linked list where last node's next pointer points back to the first node instead of NULL. Can be traversed circularly. Types: Circular Singly LL and Circular Doubly LL. Used in round-robin scheduling.</div></div>

  <div class="eq"><div class="eq-q">Q4. Structure of a doubly linked list. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Each node has 3 parts: [PREV | DATA | NEXT]. PREV = pointer to previous node, NEXT = pointer to next node. First node's PREV = NULL, Last node's NEXT = NULL. Can be traversed in both directions.</div></div>

  <div class="eq"><div class="eq-q">Q5. Two differences between binary tree and binary search tree. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Binary Tree: at most 2 children per node; no ordering constraint on keys. BST: left child &lt; parent &lt; right child; ordered; supports efficient O(log n) search.</div></div>

  <div class="eq"><div class="eq-q">Q6. Short note on post-order traversal. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Post-order: Left → Right → Root (LRN). Process: traverse left subtree, traverse right subtree, then visit root. Used for: deleting a tree, evaluating postfix expressions, finding height of tree.</div></div>

  <div class="eq"><div class="eq-q">Q7. Maximum nodes in binary tree of height 6. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Max nodes = 2^(h+1) − 1 = 2^7 − 1 = 127. (Using h=6 where root is at height 0). Each level doubles the nodes: 1+2+4+8+16+32+64 = 127.</div></div>

  <div class="eq"><div class="eq-q">Q8. Four rotations in AVL tree. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">LL Rotation: Right rotate (BF=+2, left heavy). RR Rotation: Left rotate (BF=−2, right heavy). LR Rotation: Left rotate child, then right rotate (BF=+2, left-right). RL Rotation: Right rotate child, then left rotate (BF=−2, right-left).</div></div>

  <div class="eq"><div class="eq-q">Q9. B-tree of order m=6: min keys in non-root node. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Min keys in non-root = ⌈m/2⌉ − 1 = ⌈6/2⌉ − 1 = 3 − 1 = 2. Min children = ⌈m/2⌉ = 3.</div></div>

  <div class="eq"><div class="eq-q">Q10. What happens when key inserted into full B-tree leaf? <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">The full leaf node splits: median key is promoted to parent node. Left keys go to left child, right keys go to right child. If parent also becomes full, splitting propagates upward. Root splits → tree height increases by 1.</div></div>
</div>

<div class="card">
  <div class="ct">Part B — 4×5 = 20 Marks</div>

  <div class="eq"><div class="eq-q">Q13. Construct BST for: 45,20,10,30,60,50,75,5,25 <span class="eq-marks badge bg">5M</span></div>
  <div class="dedp">
    <div class="dc dd"><h5 style="color:var(--accent)">D — Definition</h5><p>BST: Binary tree where for every node, all keys in left subtree &lt; node's key &lt; all keys in right subtree. Supports O(log n) average search, insert, delete.</p></div>
    <div class="dc de"><h5 style="color:var(--green)">E — Equation</h5><p>Insert rule: if new_key &lt; node → go left, if new_key &gt; node → go right. Search: O(log n) avg, O(n) worst (skewed). Height h = ⌊log₂n⌋ for balanced BST.</p></div>
    <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram (draw step-by-step)</h5><p>Insert 45 (root) → 20 (left of 45) → 10 (left of 20) → 30 (right of 20) → 60 (right of 45) → 50 (left of 60) → 75 (right of 60) → 5 (left of 10) → 25 (left of 30)<br>Final tree: show all 9 nodes with edges.</p></div>
    <div class="dc dp"><h5 style="color:var(--orange)">P — Points</h5><ul><li>In-order traversal gives sorted order</li><li>Insertion: compare at each node, go left/right</li><li>Deletion: 3 cases (leaf, one child, two children)</li><li>Successor = in-order successor for 2-child delete</li></ul></div>
  </div></div>

  <div class="eq"><div class="eq-q">Q14. Construct AVL tree: 10,20,30,40,50,25 <span class="eq-marks badge bg">5M</span></div>
  <div class="dedp">
    <div class="dc dd"><h5 style="color:var(--accent)">D — Definition</h5><p>AVL tree is a self-balancing BST where Balance Factor (BF) = Height(Left) − Height(Right) must be −1, 0, or +1 for every node. Rotations restore balance after insertion/deletion.</p></div>
    <div class="dc de"><h5 style="color:var(--green)">E — Equation</h5><p>BF = h_L − h_R. Valid: {−1, 0, +1}.<br>Insert 10,20→RR rotation at 10(BF=−2)<br>Insert 30→RR at 20. Insert 40→RR at 30.<br>Insert 50→RR. Insert 25→LR rotation.</p></div>
    <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Show each insertion + BF of each node + rotation applied. After inserting 10,20,30: BF of 10=−2 → RR rotation → 20 becomes root, 10 left, 30 right. Continue for 40,50,25 with their rotations.</p></div>
    <div class="dc dp"><h5 style="color:var(--orange)">P — Points</h5><ul><li>LL: single right rotation</li><li>RR: single left rotation</li><li>LR: left rotate child, then right rotate parent</li><li>RL: right rotate child, then left rotate parent</li><li>Always draw BEFORE and AFTER rotation</li></ul></div>
  </div></div>
</div>
</div>

<!-- ODVC EXAM -->
<div id="exam-odvc" style="display:none">
<div class="ok"><strong>Score: 25/30 · Good! Don't get complacent. Mid-2 = Vector Calculus (Green's/Stokes'/Gauss')</strong></div>
<div class="card">
  <div class="ct">Part A — 10×1 = 10 Marks</div>
  <div class="eq"><div class="eq-q">Q1. Solve (ye^x)dx+(2y+e^x)dy=0 <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Check exactness: M=ye^x, N=2y+e^x. ∂M/∂y=e^x, ∂N/∂x=e^x → Exact equation. Solution: ∫M dx + ∫(N terms without x)dy = C → ye^x + y² = C</div></div>

  <div class="eq"><div class="eq-q">Q3. Find integrating factor of dy/dx + y sinx = e^(cosx) <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">It is linear DE: dy/dx + P(x)y = Q(x). P(x) = sinx. IF = e^(∫sinx dx) = e^(−cosx)</div></div>

  <div class="eq"><div class="eq-q">Q5. Solve (D³−3D²−D+3)y=0 <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Auxiliary equation: m³−3m²−m+3=0. Roots: m=1,−1,3. CF = C₁e^x + C₂e^(−x) + C₃e^(3x)</div></div>

  <div class="eq"><div class="eq-q">Q9. Sufficient conditions for Laplace Transform existence. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">f(t) must be: (1) Piecewise continuous on every finite interval, (2) Of exponential order — |f(t)| ≤ Me^(αt) for some M>0, α>0 as t→∞. Then L{f(t)} exists for s>α.</div></div>

  <div class="eq"><div class="eq-q">Q10. Change of Scale Property in Laplace. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">If L{f(t)} = F(s), then L{f(at)} = (1/a)F(s/a) for a>0. Scaling the time axis by 'a' scales the frequency axis by '1/a'.</div></div>
</div>

<div class="card">
  <div class="ct">Part B — Key 5-Mark Answers</div>
  <div class="eq"><div class="eq-q">Q11. Solve dy/dx + (y/x) = x³y³ (Bernoulli's) <span class="eq-marks badge bg">5M</span></div>
  <div class="dedp">
    <div class="dc dd"><h5 style="color:var(--accent)">D — Definition</h5><p>Bernoulli's equation: dy/dx + P(x)y = Q(x)y^n. Nonlinear, solved by substitution v = y^(1−n) which converts it to a linear first-order ODE.</p></div>
    <div class="dc de"><h5 style="color:var(--green)">E — Equation (Step-by-step)</h5><p>n=3. Divide by y³: y⁻³dy/dx + (1/x)y⁻² = x³<br>Let v = y⁻², dv/dx = −2y⁻³dy/dx<br>→ −(1/2)dv/dx + v/x = x³<br>→ dv/dx − 2v/x = −2x³ (linear!)<br>IF = e^(∫−2/x dx) = x⁻². Solve to get v, then y.</p></div>
    <div class="dc dd2"><h5 style="color:var(--purple)">D — Steps Diagram</h5><p>Bernoulli → Divide by y^n → Substitute v=y^(1-n) → Linear ODE → Find IF → Multiply both sides by IF → Integrate → Get v → Substitute back y.</p></div>
    <div class="dc dp"><h5 style="color:var(--orange)">P — Points</h5><ul><li>Always identify n first</li><li>Divide entire equation by y^n</li><li>Substitution v = y^(1-n) is key step</li><li>After substitution, standard linear method applies</li><li>Don't forget to back-substitute for y at end</li></ul></div>
  </div></div>

  <div class="eq"><div class="eq-q">Q15. Find L{3e^(-4t) + cos2t + 7 − sinht + t^(3/2)} <span class="eq-marks badge bg">5M</span></div>
  <div class="dedp">
    <div class="dc dd"><h5 style="color:var(--accent)">D — Definition</h5><p>Laplace Transform: L{f(t)} = ∫₀^∞ e^(−st) f(t) dt. Apply linearity — transform each term separately using standard Laplace table.</p></div>
    <div class="dc de"><h5 style="color:var(--green)">E — Equations (Term by Term)</h5><p>L{e^(−4t)} = 1/(s+4) → L{3e^(−4t)} = 3/(s+4)<br>L{cos2t} = s/(s²+4)<br>L{7} = 7/s<br>L{sinht} = L{(e^t−e^(−t))/2} = 1/(s²−1)<br>L{t^(3/2)} = Γ(5/2)/s^(5/2) = (3√π/4)/s^(5/2)</p></div>
    <div class="dc dd2"><h5 style="color:var(--purple)">D — Laplace Table</h5><p>L{1}=1/s · L{t^n}=n!/s^(n+1) · L{e^(at)}=1/(s−a) · L{sinkt}=k/(s²+k²) · L{coskt}=s/(s²+k²) · L{sinhat}=a/(s²−a²)</p></div>
    <div class="dc dp"><h5 style="color:var(--orange)">P — Points</h5><ul><li>Apply linearity: L{af+bg} = aL{f} + bL{g}</li><li>For t^(3/2): use Gamma function Γ(n+1) = nΓ(n)</li><li>Γ(1/2) = √π is standard result</li><li>sinht = (e^t − e^(−t))/2 — expand first</li><li>Final answer: sum of all transformed terms</li></ul></div>
  </div></div>
</div>
</div>

<!-- DRAWING EXAM -->
<div id="exam-draw" style="display:none">
<div class="warn"><strong>Score: 15/30 · Missing: Misread questions, confused views, missing 1-mark questions</strong></div>
<div class="card">
  <div class="ct">Part A — 10×1 = 10 Marks</div>
  <div class="eq"><div class="eq-q">Q1. Compare aligned & unidirectional methods. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Aligned method: dimensions placed inside dimension lines, read from bottom or right side. Unidirectional method: all dimensions placed horizontally, read from bottom only. Unidirectional is preferred in modern practice.</div></div>

  <div class="eq"><div class="eq-q">Q2. Define eccentricity. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Eccentricity (e) = Distance from focus / Distance from directrix = PF/PD. Circle: e=0. Ellipse: e&lt;1. Parabola: e=1. Hyperbola: e&gt;1. Determines shape of conic section.</div></div>

  <div class="eq"><div class="eq-q">Q3. Applications of cycloids. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Gear tooth profile design, shape of curved ramps (brachistochrone), clock pendulums, curved slides in playgrounds, cam design in machinery.</div></div>

  <div class="eq"><div class="eq-q">Q4. Define involute. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Involute is the curve traced by the free end of a thread when unwound from a circle (base circle). Used in gear tooth profile design. Every point on the involute is tangent to the base circle.</div></div>

  <div class="eq"><div class="eq-q">Q5. Define orthographic projection. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Method of representing 3D objects on 2D plane using parallel projectors perpendicular to the projection plane. Object features projected onto Horizontal Plane (HP), Vertical Plane (VP), and Profile Plane (PP).</div></div>

  <div class="eq"><div class="eq-q">Q6. Difference between 1st and 3rd angle projection. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">1st angle (European): object between observer and plane; Front view top-left, Top view below, Side view on left. 3rd angle (American): plane between observer and object; Front view top-left, Top view above, Side view on right.</div></div>

  <div class="eq"><div class="eq-q">Q7. Why 2nd and 4th angle projections not used? <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">In 2nd and 4th angle projections, the views overlap each other causing confusion and ambiguity. The top and front views coincide on the same side, making interpretation impossible. Hence not used in practice.</div></div>

  <div class="eq"><div class="eq-q">Q8. Point A: 20mm below HP, 35mm in front of VP — draw projections. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">Point below HP → top view (plan) below xy line. 20mm below HP → a (front view) 20mm below xy. Point in front of VP → a' (top view) 35mm below xy line. Draw both views.</div></div>

  <div class="eq"><div class="eq-q">Q9. Triangular plane perpendicular to HP and VP — shape of FV, TV, SV. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">FV: straight line (edge view in front). TV: straight line (edge view on top). SV: true shape = triangle. When a plane is perpendicular to both HP and VP, its true shape appears in the side view (Profile Plane).</div></div>

  <div class="eq"><div class="eq-q">Q10. List orientations of planes with respect to HP and VP. <span class="eq-marks badge bb">1M</span></div>
  <div class="eq-a">(1) Parallel to HP: TV=true shape, FV=line. (2) Parallel to VP: FV=true shape, TV=line. (3) Perpendicular to HP, inclined to VP: TV=line, FV=distorted. (4) Perpendicular to VP, inclined to HP: FV=line, TV=distorted. (5) Oblique: both views distorted.</div></div>
</div>

<div class="card">
  <div class="ct">Part B — 4×5 = 20 Marks</div>
  <div class="eq"><div class="eq-q">Q11. Conic curve: focus-directrix = 50mm, eccentricity = 1. Draw tangent & normal at 65mm. <span class="eq-marks badge bg">5M</span></div>
  <div class="dedp">
    <div class="dc dd"><h5 style="color:var(--accent)">D — Definition</h5><p>Parabola (e=1): locus of a point equidistant from a fixed point (focus F) and a fixed line (directrix). Since e=1, PF = PD for every point P on the curve.</p></div>
    <div class="dc de"><h5 style="color:var(--green)">E — Steps</h5><p>1. Draw directrix DD' vertical. 2. Axis = horizontal perpendicular to directrix. 3. Mark F at 50mm from directrix on axis. 4. Vertex V = midpoint of focus-directrix = 25mm from each. 5. Mark points using PF=PD construction. 6. Draw smooth parabola. 7. Tangent at 65mm: draw line from F to point, bisect the angle with directrix perpendicular → tangent direction.</p></div>
    <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram Steps</h5><p>Directrix | | | F(focus) → Vertex(V) midpoint. Draw multiple points P equidistant from F and directrix. Connect smoothly. At point 65mm from directrix: T = tangent (bisector of angle FP with perp from P to directrix). N = normal (perpendicular to T).</p></div>
    <div class="dc dp"><h5 style="color:var(--orange)">P — Points (Exam Tips)</h5><ul><li>e=1 → Parabola (not ellipse, not hyperbola)</li><li>Vertex is ALWAYS midpoint of F and directrix</li><li>Tangent: bisect ∠(FP, perpendicular from P to directrix)</li><li>Normal: perpendicular to tangent at point P</li><li>Use pencil + drafter, draw neat construction lines</li></ul></div>
  </div></div>

  <div class="eq"><div class="eq-q">Q13. Project 65mm line: (A) inclined 45° to VP in HP, one end in VP. (B) inclined 30° to HP, one end 20mm above HP, 30mm in front VP. <span class="eq-marks badge bg">5M</span></div>
  <div class="dedp">
    <div class="dc dd"><h5 style="color:var(--accent)">D — Definition</h5><p>Projection of a line inclined to one plane: draw true length in the plane it lies on first. Then project to the other plane. For inclined to both: use auxiliary view or two-step method.</p></div>
    <div class="dc de"><h5 style="color:var(--green)">E — Steps (Case A)</h5><p>Line in HP, inclined 45° to VP. One end on VP (a on xy line). In TV: draw a'b' = 65mm at 45° to xy line from a'. In FV: both end points on xy line (line lies in HP). ab is horizontal line.</p></div>
    <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram Steps</h5><p>Draw xy reference line. Case A: a on xy. Measure 65mm at 45° in TV (above xy). Project to FV → both points on xy. Case B: one end 20mm above HP → a is 20mm above xy in FV. 30mm in front of VP → a' is 30mm below xy in TV. Draw 30° inclination for FV.</p></div>
    <div class="dc dp"><h5 style="color:var(--orange)">P — Points (Exam Tips)</h5><ul><li>Read question: "inclined to VP" = angle in TV (top view)</li><li>"Inclined to HP" = angle visible in FV (front view)</li><li>One end on VP = that point's TV is on xy line</li><li>Above HP = FV point above xy line</li><li>Always draw xy line first, then position end points</li></ul></div>
  </div></div>
</div>
</div>
</div>

<!-- ======= FORMULAS ======= -->
<div id="page-formulas" class="page">
<div class="pt">🧪 Formula Vault</div>
<div class="ps">All formulas from your uploaded docs + complete subject coverage</div>

<div class="tabs">
  <button class="tab active" onclick="sw('form','bee',this)">BEE</button>
  <button class="tab" onclick="sw('form','chem',this)">Chemistry</button>
  <button class="tab" onclick="sw('form','ds2',this)">Data Structures</button>
  <button class="tab" onclick="sw('form','odvc2',this)">ODVC</button>
  <button class="tab" onclick="sw('form','draw2',this)">Drawing</button>
</div>

<div id="form-bee">
  <div class="ok">From your BEE_Formulas.docx + complete coverage</div>
  <div class="fbox"><div class="flbl">Unit 1 · Basic Laws</div>V = I × R &nbsp;|&nbsp; P = VI = I²R = V²/R &nbsp;|&nbsp; E = Pt (energy)<br>KCL: ΣI_in = ΣI_out &nbsp;|&nbsp; KVL: ΣV = 0 (around any closed loop)</div>
  <div class="fbox"><div class="flbl">Unit 1 · Source Conversion</div>V_terminal = EMF − I × r (practical voltage source)<br>Thevenin: V_th = V_oc &nbsp;|&nbsp; R_th = V_th / I_sc<br>Norton: I_N = I_sc &nbsp;|&nbsp; R_N = R_th (same resistance)<br>Superposition: ΣI from each source independently (replace V→short, I→open)</div>
  <div class="fbox"><div class="flbl">Unit 2 · AC Circuits</div>v(t) = V_m sin(ωt + φ) &nbsp;|&nbsp; V_rms = V_m / √2 &nbsp;|&nbsp; V_avg = 0.637 V_m<br>X_L = 2πfL &nbsp;|&nbsp; X_C = 1/(2πfC)<br>Z = √(R² + (X_L − X_C)²) &nbsp;|&nbsp; I = V/Z<br>Phase angle: tanφ = (X_L − X_C)/R</div>
  <div class="fbox"><div class="flbl">Unit 3 · Power</div>P = VIcosφ (Active, Watts) &nbsp;|&nbsp; Q = VIsinφ (Reactive, VAR)<br>S = VI (Apparent, VA) &nbsp;|&nbsp; Power Factor = cosφ = P/S = R/Z<br>S² = P² + Q²</div>
  <div class="fbox"><div class="flbl">Unit 4 · Resonance & 3-Phase</div>Resonant frequency: f_r = 1/(2π√LC) &nbsp;|&nbsp; At resonance: X_L = X_C, Z = R<br>Q-factor = ω_r L/R = 1/(ω_r CR)<br>Star: V_L = √3 V_P &nbsp;|&nbsp; I_L = I_P<br>Delta: V_L = V_P &nbsp;|&nbsp; I_L = √3 I_P<br>3-phase power: P = √3 V_L I_L cosφ</div>
  <div class="fbox"><div class="flbl">Unit 5 · Transformer</div>EMF: E = 4.44 × f × N × Φ_m ← BOX IN EXAM<br>Turns ratio: a = N₁/N₂ = V₁/V₂ = I₂/I₁<br>Efficiency: η = P_out/(P_out + Copper loss + Iron loss) × 100%<br>Regulation: VR% = (V_NL − V_FL)/V_FL × 100%</div>
</div>

<div id="form-chem" style="display:none">
  <div class="ok">From your Chemistry_Formulas.docx + complete coverage</div>
  <div class="fbox"><div class="flbl">Unit 1 · Water Treatment</div>Hardness (ppm) = Vol(EDTA) × M × 100000 / Vol(sample)<br>Hardness units: mg/L = ppm<br>1° hardness = 1 part CaCO₃ per 100,000 parts water<br>Softening by ion exchange: 2NaR + Ca²⁺ → CaR₂ + 2Na⁺</div>
  <div class="fbox"><div class="flbl">Unit 2 · Electrochemistry (from your doc)</div>Nernst Equation: E = E° − (0.0591/n) × log Q &nbsp;[at 25°C]<br>Cell EMF: E_cell = E_cathode − E_anode<br>Gibbs Energy: ΔG = −nFE &nbsp;(F = 96500 C/mol)<br>E°_cell = E°_cathode − E°_anode</div>
  <div class="fbox"><div class="flbl">Unit 2 · Corrosion (from your doc)</div>Pilling-Bedworth ratio = Vol(oxide) / Vol(metal)<br>P-B &lt; 1 → porous oxide (unprotective) eg. Mg<br>P-B 1−2 → non-porous (protective) eg. Al, Cr<br>P-B &gt; 2 → cracks (unprotective) eg. Fe₂O₃</div>
  <div class="fbox"><div class="flbl">Unit 3 · Batteries & Fuel Cells</div>Li-ion: Anode LiC₆ → Li⁺ + e⁻ + C₆ (discharge)<br>Cathode: Li⁺ + e⁻ + CoO₂ → LiCoO₂ (discharge)<br>DMFC Anode: CH₃OH + H₂O → CO₂ + 6H⁺ + 6e⁻<br>DMFC Cathode: 3/2 O₂ + 6H⁺ + 6e⁻ → 3H₂O<br>Zn-air: Zn + 1/2 O₂ → ZnO</div>
  <div class="fbox"><div class="flbl">Unit 4 · Polymers (from your doc)</div>DP = Molecular Weight / Monomer Weight<br>Addition polymerization: initiation → propagation → termination<br>Condensation: produces small molecule (H₂O) as byproduct<br>e.g., Nylon-6,6: adipic acid + hexamethylenediamine</div>
  <div class="fbox"><div class="flbl">Unit 5 · Fuels (from your doc)</div>CV = Heat released / Mass of fuel (kcal/kg or kJ/kg)<br>Dulong's formula: CV = 1/100 × [8084C + 34500(H−O/8) + 2240S] kcal/kg<br>HCV: latent heat of steam INCLUDED. LCV: latent heat NOT included.<br>LCV = HCV − 0.09H × 587 kcal/kg (H = % hydrogen)</div>
</div>

<div id="form-ds2" style="display:none">
  <div class="ok">From your Data_Structures_Formulas.docx + complete coverage</div>
  <div class="fbox"><div class="flbl">Unit 1 · Complexity (from your doc)</div>O(1) Constant &nbsp;|&nbsp; O(log n) Logarithmic &nbsp;|&nbsp; O(n) Linear<br>O(n log n) Linearithmic &nbsp;|&nbsp; O(n²) Quadratic &nbsp;|&nbsp; O(2^n) Exponential<br>Space complexity: extra memory used by algorithm</div>
  <div class="fbox"><div class="flbl">Unit 1 · Linked Lists & Stack/Queue (from your doc)</div>Stack PUSH: Top = Top + 1, then a[Top] = item<br>Stack POP: item = a[Top], then Top = Top − 1<br>Queue Enqueue: Rear = (Rear + 1) % n, then Q[Rear] = item<br>Queue Dequeue: item = Q[Front], Front = (Front + 1) % n<br>Queue Full: (Rear + 1) % n == Front</div>
  <div class="fbox"><div class="flbl">Unit 2 · Searching (from your doc)</div>Binary Search complexity: O(log₂n)<br>Linear Search: O(n)<br>Binary Search mid: mid = low + (high − low) / 2<br>Interpolation Search: pos = low + [(key−a[low])/(a[high]−a[low])] × (high−low)</div>
  <div class="fbox"><div class="flbl">Unit 2 · Trees (from your doc)</div>Max nodes in tree of height h = 2^(h+1) − 1<br>Min height for n nodes = ⌈log₂(n+1)⌉ − 1<br>AVL Balance Factor BF = h_L − h_R ∈ {−1, 0, +1}<br>B-Tree order m: max keys = m−1, min keys = ⌈m/2⌉−1<br>BST Search O(log n) avg, O(n) worst (skewed)</div>
  <div class="fbox"><div class="flbl">Unit 3 · Heaps & Sorting</div>Heap property: parent ≤ children (min-heap) or ≥ (max-heap)<br>Heapsort: O(n log n) guaranteed, in-place<br>Radix sort: O(d(n+k)) where d=digits, k=range<br>Shell sort: O(n log² n) — gap sequence matters</div>
  <div class="fbox"><div class="flbl">Unit 4 · Hashing</div>Division method: h(k) = k mod m<br>Multiplication: h(k) = ⌊m(kA mod 1)⌋, A ≈ 0.618<br>Load factor λ = n/m (n=items, m=table size)<br>Open addressing: h(k,i) = (h(k)+i) mod m (linear probing)</div>
</div>

<div id="form-odvc2" style="display:none">
  <div class="ok">From your ODVC_Formulas.docx + complete coverage</div>
  <div class="fbox"><div class="flbl">Unit 1 · First Order ODE (from your doc)</div>Linear DE: dy/dx + P(x)y = Q(x)<br>Integrating Factor: IF = e^(∫P dx)<br>Solution: y × IF = ∫(Q × IF)dx + C<br>Bernoulli: dy/dx + Py = Qy^n → substitute v = y^(1-n)<br>Exact: M dx + N dy = 0, check ∂M/∂y = ∂N/∂x</div>
  <div class="fbox"><div class="flbl">Unit 2 · Higher Order DE (from your doc)</div>Char. Equation: m² + am + b = 0 (for D²+aD+b)y=0<br>Real distinct roots m₁,m₂: CF = C₁e^(m₁x) + C₂e^(m₂x)<br>Equal roots m,m: CF = e^(mx)(C₁ + C₂x)<br>Complex roots α±βi: CF = e^(αx)[C₁cos(βx)+C₂sin(βx)]<br>PI for e^(ax): 1/(f(D)) e^(ax) = e^(ax)/f(a) if f(a)≠0</div>
  <div class="fbox"><div class="flbl">Unit 3 · Laplace Transform (from your doc)</div>L{1}=1/s &nbsp;|&nbsp; L{t^n}=n!/s^(n+1) &nbsp;|&nbsp; L{e^(at)}=1/(s−a)<br>L{sin kt}=k/(s²+k²) &nbsp;|&nbsp; L{cos kt}=s/(s²+k²)<br>L{sinh at}=a/(s²−a²) &nbsp;|&nbsp; L{cosh at}=s/(s²−a²)<br>L{t^(1/2)}=√π/(2s^(3/2)) &nbsp;|&nbsp; L{t^(3/2)}=3√π/(4s^(5/2))<br>Shift: L{e^(at)f(t)}=F(s−a) &nbsp;|&nbsp; L{f'(t)}=sF(s)−f(0)</div>
  <div class="fbox"><div class="flbl">Unit 4 · Vector Algebra (from your doc)</div>Dot product: A·B = |A||B|cosθ = AxBx+AyBy+AzBz<br>Cross product: |A×B| = |A||B|sinθ (direction by right-hand rule)<br>Gradient: ∇φ = (∂φ/∂x)i + (∂φ/∂y)j + (∂φ/∂z)k<br>Divergence: ∇·A = ∂Ax/∂x + ∂Ay/∂y + ∂Az/∂z<br>Curl: ∇×A = (3×3 determinant with i,j,k and ∂/∂x,∂/∂y,∂/∂z)</div>
  <div class="fbox"><div class="flbl">Unit 5 · Vector Integration (from your doc)</div>Line integral: ∫_C A·dr = ∫(Ax dx + Ay dy + Az dz)<br>Green's: ∮(M dx+N dy) = ∬(∂N/∂x − ∂M/∂y) dA<br>Stokes': ∮_C F·dr = ∬_S (∇×F)·dS<br>Gauss': ∯_S F·dS = ∭_V (∇·F) dV<br>Surface integral: ∬A·dS = ∬A·n̂ dS</div>
</div>

<div id="form-draw2" style="display:none">
  <div class="info">Drawing is a practical subject — formulas here are construction rules and key definitions to memorize.</div>
  <div class="fbox"><div class="flbl">Unit 1 · Conic Sections</div>Eccentricity: e = PF/PD (focus to point / directrix to point)<br>Circle: e=0 &nbsp;|&nbsp; Ellipse: 0&lt;e&lt;1 &nbsp;|&nbsp; Parabola: e=1 &nbsp;|&nbsp; Hyperbola: e&gt;1<br>Ellipse: sum PF₁+PF₂ = constant = 2a (major axis)<br>Hyperbola: |PF₁−PF₂| = constant = 2a</div>
  <div class="fbox"><div class="flbl">Unit 1 · Scales</div>Representative Fraction (RF) = Drawing length / Actual length<br>Plain scale: measures up to 2 units. Diagonal scale: 3 units.<br>Reducing scale: RF &lt; 1. Enlarging scale: RF &gt; 1. Full scale: RF = 1.</div>
  <div class="fbox"><div class="flbl">Unit 2 · Projection of Points</div>Point above HP → front view ABOVE xy line (FV is above xy)<br>Point below HP → FV below xy line<br>Point in front of VP → top view BELOW xy line (TV below xy)<br>Point behind VP → TV above xy line</div>
  <div class="fbox"><div class="flbl">Unit 2 · Projection of Lines</div>Line inclined to VP → angle visible in TOP VIEW<br>Line inclined to HP → angle visible in FRONT VIEW<br>True length appears in the view where line is parallel to that plane<br>Line parallel to both HP & VP → appears as point in side view</div>
  <div class="fbox"><div class="flbl">Unit 3 · Projections of Planes</div>Plane parallel to HP → TV=true shape, FV=straight line<br>Plane parallel to VP → FV=true shape, TV=straight line<br>Plane inclined to HP, ⊥VP → FV=line at angle to xy, TV=distorted<br>Oblique plane → both views distorted, use auxiliary view</div>
  <div class="fbox"><div class="flbl">Unit 4 · Solids & Sections</div>Prism: 2 parallel polygon bases + rectangular lateral faces<br>Pyramid: polygonal base + triangular lateral faces meeting at apex<br>Section plane ∥ to base → circular/rectangular cut<br>Section plane inclined to axis → elliptical cut (for cylinder/cone)<br>Frustum = solid after cutting apex portion</div>
  <div class="fbox"><div class="flbl">Unit 5 · Isometric</div>Isometric axes: 3 axes at 120° to each other (30° to horizontal)<br>Isometric scale = actual × cos30°/cos45° = actual × 0.816<br>Isometric drawing: use true measurements (not isometric scale)<br>Non-isometric lines: cannot measure directly; plot endpoints</div>
</div>
</div>

<!-- ======= DIAGRAMS (SVG) ======= -->
<div id="page-diagrams" class="page">
<div class="pt">🔷 Diagrams (Visual Format)</div>
<div class="ps">SVG picture diagrams for exam · BEE · Chemistry · DS · Drawing</div>

<div class="tabs">
  <button class="tab active" onclick="sw('diag','bee',this)">BEE</button>
  <button class="tab" onclick="sw('diag','chem',this)">Chemistry</button>
  <button class="tab" onclick="sw('diag','ds',this)">DS Trees</button>
  <button class="tab" onclick="sw('diag','draw',this)">Drawing</button>
</div>

<!-- BEE DIAGRAMS -->
<div id="diag-bee">
<div class="diag-wrap">
  <div class="diag-title">Thevenin Equivalent Circuit</div>
  <svg viewBox="0 0 480 180" width="100%" style="max-width:480px">
    <rect width="480" height="180" fill="#0d1117" rx="6"/>
    <!-- wires -->
    <line x1="40" y1="60" x2="120" y2="60" stroke="#58a6ff" stroke-width="2"/>
    <line x1="200" y1="60" x2="280" y2="60" stroke="#58a6ff" stroke-width="2"/>
    <line x1="280" y1="60" x2="320" y2="60" stroke="#58a6ff" stroke-width="2"/>
    <line x1="380" y1="60" x2="420" y2="60" stroke="#58a6ff" stroke-width="2"/>
    <line x1="40" y1="140" x2="420" y2="140" stroke="#58a6ff" stroke-width="2"/>
    <line x1="40" y1="60" x2="40" y2="140" stroke="#58a6ff" stroke-width="2"/>
    <line x1="420" y1="60" x2="420" y2="100" stroke="#58a6ff" stroke-width="2"/>
    <line x1="420" y1="120" x2="420" y2="140" stroke="#58a6ff" stroke-width="2"/>
    <!-- V_th source -->
    <circle cx="80" cy="100" r="24" fill="none" stroke="#ffa657" stroke-width="2"/>
    <text x="80" y="94" text-anchor="middle" fill="#ffa657" font-size="10" font-family="monospace">+</text>
    <text x="80" y="108" text-anchor="middle" fill="#ffa657" font-size="9" font-family="monospace">Vth</text>
    <line x1="40" y1="100" x2="56" y2="100" stroke="#ffa657" stroke-width="1.5"/>
    <line x1="104" y1="100" x2="120" y2="60" stroke="#ffa657" stroke-width="1.5"/>
    <line x1="80" y1="124" x2="80" y2="140" stroke="#ffa657" stroke-width="1.5"/>
    <line x1="80" y1="76" x2="80" y2="60" stroke="#ffa657" stroke-width="1.5"/>
    <!-- R_th resistor -->
    <rect x="120" y="50" width="80" height="20" fill="none" stroke="#3fb950" stroke-width="2" rx="2"/>
    <text x="160" y="63" text-anchor="middle" fill="#3fb950" font-size="10" font-family="monospace">R_th</text>
    <!-- R_L load -->
    <rect x="380" y="100" width="40" height="40" fill="none" stroke="#d2a8ff" stroke-width="2" rx="2"/>
    <text x="400" y="123" text-anchor="middle" fill="#d2a8ff" font-size="10" font-family="monospace">R_L</text>
    <!-- terminals -->
    <circle cx="420" cy="60" r="5" fill="#58a6ff"/>
    <circle cx="420" cy="140" r="5" fill="#58a6ff"/>
    <text x="435" y="63" fill="#e6edf3" font-size="11" font-family="monospace">A</text>
    <text x="435" y="143" fill="#e6edf3" font-size="11" font-family="monospace">B</text>
    <!-- labels -->
    <text x="10" y="45" fill="#8b949e" font-size="9" font-family="monospace">I_L→</text>
    <text x="160" y="170" text-anchor="middle" fill="#e3b341" font-size="9" font-family="monospace">I_L = Vth / (Rth + RL)</text>
  </svg>
</div>

<div class="diag-wrap">
  <div class="diag-title">Single-Phase Transformer</div>
  <svg viewBox="0 0 480 200" width="100%" style="max-width:480px">
    <rect width="480" height="200" fill="#0d1117" rx="6"/>
    <!-- core -->
    <rect x="170" y="40" width="140" height="120" fill="none" stroke="#e3b341" stroke-width="2.5" rx="4"/>
    <rect x="195" y="65" width="90" height="70" fill="#161b22" stroke="#e3b341" stroke-width="1.5" rx="2"/>
    <text x="240" y="105" text-anchor="middle" fill="#e3b341" font-size="11" font-family="monospace">φ (flux)</text>
    <text x="240" y="120" text-anchor="middle" fill="#e3b341" font-size="9" font-family="monospace">Iron Core</text>
    <!-- primary coil -->
    <text x="100" y="40" text-anchor="middle" fill="#58a6ff" font-size="10" font-family="monospace">PRIMARY</text>
    <text x="100" y="54" text-anchor="middle" fill="#58a6ff" font-size="9" font-family="monospace">N₁ turns</text>
    <line x1="30" y1="80" x2="90" y2="80" stroke="#58a6ff" stroke-width="2"/>
    <line x1="30" y1="140" x2="90" y2="140" stroke="#58a6ff" stroke-width="2"/>
    <line x1="30" y1="80" x2="30" y2="140" stroke="#58a6ff" stroke-width="2"/>
    <text x="30" y="115" text-anchor="middle" fill="#58a6ff" font-size="10" font-family="monospace" transform="rotate(-90,30,110)">~AC V₁</text>
    <!-- coil symbol primary -->
    <path d="M90,80 Q95,60 100,80 Q105,100 110,80 Q115,60 120,80 Q125,100 130,80 Q135,60 140,80 Q145,100 150,80 Q155,60 160,80 Q165,100 170,80" fill="none" stroke="#58a6ff" stroke-width="2"/>
    <path d="M90,140 Q95,120 100,140 Q105,160 110,140 Q115,120 120,140 Q125,160 130,140 Q135,120 140,140 Q145,160 150,140 Q155,120 160,140 Q165,160 170,140" fill="none" stroke="#58a6ff" stroke-width="2"/>
    <!-- secondary coil -->
    <text x="380" y="40" text-anchor="middle" fill="#3fb950" font-size="10" font-family="monospace">SECONDARY</text>
    <text x="380" y="54" text-anchor="middle" fill="#3fb950" font-size="9" font-family="monospace">N₂ turns</text>
    <path d="M310,80 Q315,60 320,80 Q325,100 330,80 Q335,60 340,80 Q345,100 350,80 Q355,60 360,80 Q365,100 370,80 Q375,60 380,80 Q385,100 390,80" fill="none" stroke="#3fb950" stroke-width="2"/>
    <path d="M310,140 Q315,120 320,140 Q325,160 330,140 Q335,120 340,140 Q345,160 350,140 Q355,120 360,140 Q365,160 370,140 Q375,120 380,140 Q385,160 390,140" fill="none" stroke="#3fb950" stroke-width="2"/>
    <line x1="390" y1="80" x2="450" y2="80" stroke="#3fb950" stroke-width="2"/>
    <line x1="390" y1="140" x2="450" y2="140" stroke="#3fb950" stroke-width="2"/>
    <line x1="450" y1="80" x2="450" y2="140" stroke="#3fb950" stroke-width="2"/>
    <text x="455" y="115" fill="#3fb950" font-size="9" font-family="monospace">LOAD V₂</text>
    <!-- EMF equation -->
    <text x="240" y="185" text-anchor="middle" fill="#ffa657" font-size="10" font-family="monospace">E = 4.44 × f × N × Φm</text>
  </svg>
</div>

<div class="diag-wrap">
  <div class="diag-title">Series RLC Circuit with Resonance</div>
  <svg viewBox="0 0 480 160" width="100%" style="max-width:480px">
    <rect width="480" height="160" fill="#0d1117" rx="6"/>
    <!-- AC source -->
    <circle cx="50" cy="80" r="25" fill="none" stroke="#ffa657" stroke-width="2"/>
    <text x="50" y="76" text-anchor="middle" fill="#ffa657" font-size="12" font-family="monospace">~</text>
    <text x="50" y="91" text-anchor="middle" fill="#ffa657" font-size="8" font-family="monospace">V</text>
    <!-- wires -->
    <line x1="50" y1="55" x2="50" y2="25" stroke="#58a6ff" stroke-width="2"/>
    <line x1="50" y1="25" x2="440" y2="25" stroke="#58a6ff" stroke-width="2"/>
    <line x1="50" y1="105" x2="50" y2="135" stroke="#58a6ff" stroke-width="2"/>
    <line x1="50" y1="135" x2="440" y2="135" stroke="#58a6ff" stroke-width="2"/>
    <line x1="440" y1="25" x2="440" y2="135" stroke="#58a6ff" stroke-width="2"/>
    <!-- R -->
    <rect x="100" y="15" width="70" height="20" fill="none" stroke="#f85149" stroke-width="2" rx="2"/>
    <text x="135" y="28" text-anchor="middle" fill="#f85149" font-size="11" font-family="monospace">R</text>
    <!-- L -->
    <path d="M195,25 Q200,5 210,25 Q220,45 230,25 Q240,5 250,25 Q260,45 265,25" fill="none" stroke="#3fb950" stroke-width="2"/>
    <text x="230" y="48" text-anchor="middle" fill="#3fb950" font-size="10" font-family="monospace">L</text>
    <!-- C -->
    <line x1="300" y1="25" x2="330" y2="25" stroke="#58a6ff" stroke-width="2"/>
    <line x1="330" y1="12" x2="330" y2="38" stroke="#d2a8ff" stroke-width="3"/>
    <line x1="340" y1="12" x2="340" y2="38" stroke="#d2a8ff" stroke-width="3"/>
    <line x1="340" y1="25" x2="370" y2="25" stroke="#58a6ff" stroke-width="2"/>
    <text x="335" y="52" text-anchor="middle" fill="#d2a8ff" font-size="10" font-family="monospace">C</text>
    <!-- equations -->
    <text x="50" y="152" fill="#e3b341" font-size="9" font-family="monospace">Z=√(R²+(XL−XC)²) | Resonance: fr=1/(2π√LC), Z=R (min)</text>
  </svg>
</div>
</div>

<!-- CHEMISTRY DIAGRAMS -->
<div id="diag-chem" style="display:none">
<div class="diag-wrap">
  <div class="diag-title">Galvanic (Electrochemical) Cell — Zn-Cu</div>
  <svg viewBox="0 0 480 220" width="100%" style="max-width:480px">
    <rect width="480" height="220" fill="#0d1117" rx="6"/>
    <!-- left beaker (anode) -->
    <rect x="30" y="60" width="140" height="130" fill="none" stroke="#f85149" stroke-width="2" rx="4"/>
    <rect x="30" y="130" width="140" height="60" fill="rgba(248,81,73,0.08)" rx="0"/>
    <text x="100" y="160" text-anchor="middle" fill="#f85149" font-size="10" font-family="monospace">ZnSO₄(aq)</text>
    <!-- Zn rod -->
    <rect x="88" y="55" width="24" height="80" fill="#e3b341" rx="2"/>
    <text x="100" y="50" text-anchor="middle" fill="#e3b341" font-size="11" font-family="monospace">Zn</text>
    <text x="100" y="205" text-anchor="middle" fill="#f85149" font-size="10" font-family="monospace">ANODE (−)</text>
    <!-- right beaker (cathode) -->
    <rect x="310" y="60" width="140" height="130" fill="none" stroke="#3fb950" stroke-width="2" rx="4"/>
    <rect x="310" y="130" width="140" height="60" fill="rgba(63,185,80,0.08)" rx="0"/>
    <text x="380" y="160" text-anchor="middle" fill="#3fb950" font-size="10" font-family="monospace">CuSO₄(aq)</text>
    <!-- Cu rod -->
    <rect x="368" y="55" width="24" height="80" fill="#ffa657" rx="2"/>
    <text x="380" y="50" text-anchor="middle" fill="#ffa657" font-size="11" font-family="monospace">Cu</text>
    <text x="380" y="205" text-anchor="middle" fill="#3fb950" font-size="10" font-family="monospace">CATHODE (+)</text>
    <!-- salt bridge -->
    <rect x="185" y="70" width="110" height="30" fill="none" stroke="#8b949e" stroke-width="2" rx="12"/>
    <text x="240" y="88" text-anchor="middle" fill="#8b949e" font-size="9" font-family="monospace">Salt Bridge</text>
    <!-- external wire + electrons -->
    <line x1="100" y1="55" x2="100" y2="25" stroke="#58a6ff" stroke-width="2"/>
    <line x1="100" y1="25" x2="380" y2="25" stroke="#58a6ff" stroke-width="2"/>
    <line x1="380" y1="25" x2="380" y2="55" stroke="#58a6ff" stroke-width="2"/>
    <!-- arrows for e- flow -->
    <polygon points="220,20 210,25 220,30" fill="#58a6ff"/>
    <polygon points="260,20 270,25 260,30" fill="#58a6ff"/>
    <text x="240" y="18" text-anchor="middle" fill="#58a6ff" font-size="9" font-family="monospace">e⁻ flow</text>
    <!-- reactions -->
    <text x="100" y="100" text-anchor="middle" fill="#ffa657" font-size="8.5" font-family="monospace">Zn→Zn²⁺+2e⁻</text>
    <text x="380" y="100" text-anchor="middle" fill="#ffa657" font-size="8.5" font-family="monospace">Cu²⁺+2e⁻→Cu</text>
    <text x="240" y="215" text-anchor="middle" fill="#e3b341" font-size="9" font-family="monospace">Ecell = Ecathode − Eanode</text>
  </svg>
</div>

<div class="diag-wrap">
  <div class="diag-title">Li-ion Battery (Discharge Mode)</div>
  <svg viewBox="0 0 480 200" width="100%" style="max-width:480px">
    <rect width="480" height="200" fill="#0d1117" rx="6"/>
    <!-- anode -->
    <rect x="20" y="30" width="110" height="140" fill="rgba(248,81,73,0.1)" stroke="#f85149" stroke-width="2" rx="4"/>
    <text x="75" y="55" text-anchor="middle" fill="#f85149" font-size="10" font-family="monospace">ANODE (−)</text>
    <text x="75" y="72" text-anchor="middle" fill="#f85149" font-size="9" font-family="monospace">Graphite</text>
    <text x="75" y="88" text-anchor="middle" fill="#f85149" font-size="8" font-family="monospace">LiC₆</text>
    <text x="75" y="105" text-anchor="middle" fill="#e6edf3" font-size="8" font-family="monospace">LiC₆→Li⁺+e⁻+C₆</text>
    <!-- membrane -->
    <rect x="150" y="30" width="40" height="140" fill="rgba(88,166,255,0.1)" stroke="#58a6ff" stroke-width="1.5" rx="2"/>
    <text x="170" y="95" text-anchor="middle" fill="#58a6ff" font-size="8" font-family="monospace" transform="rotate(-90,170,100)">PEM Electrolyte</text>
    <!-- Li+ arrows through membrane -->
    <polygon points="168,85 178,90 168,95" fill="#e3b341"/>
    <polygon points="168,105 178,110 168,115" fill="#e3b341"/>
    <text x="170" y="78" text-anchor="middle" fill="#e3b341" font-size="8" font-family="monospace">Li⁺</text>
    <!-- cathode -->
    <rect x="210" y="30" width="120" height="140" fill="rgba(63,185,80,0.1)" stroke="#3fb950" stroke-width="2" rx="4"/>
    <text x="270" y="55" text-anchor="middle" fill="#3fb950" font-size="10" font-family="monospace">CATHODE (+)</text>
    <text x="270" y="72" text-anchor="middle" fill="#3fb950" font-size="9" font-family="monospace">LiCoO₂</text>
    <text x="270" y="95" text-anchor="middle" fill="#e6edf3" font-size="8" font-family="monospace">Li⁺+e⁻+CoO₂</text>
    <text x="270" y="110" text-anchor="middle" fill="#e6edf3" font-size="8" font-family="monospace">→LiCoO₂</text>
    <!-- external circuit -->
    <line x1="75" y1="30" x2="75" y2="10" stroke="#58a6ff" stroke-width="2"/>
    <line x1="75" y1="10" x2="350" y2="10" stroke="#58a6ff" stroke-width="2"/>
    <line x1="350" y1="10" x2="350" y2="30" stroke="#58a6ff" stroke-width="2"/>
    <rect x="370" y="30" width="80" height="140" fill="rgba(210,168,255,0.08)" stroke="#d2a8ff" stroke-width="1.5" rx="4"/>
    <text x="410" y="100" text-anchor="middle" fill="#d2a8ff" font-size="9" font-family="monospace">LOAD</text>
    <line x1="350" y1="10" x2="410" y2="10" stroke="#58a6ff" stroke-width="1.5" stroke-dasharray="4"/>
    <line x1="410" y1="10" x2="410" y2="30" stroke="#58a6ff" stroke-width="1.5" stroke-dasharray="4"/>
    <polygon points="200,5 210,10 200,15" fill="#58a6ff"/>
    <text x="155" y="8" fill="#58a6ff" font-size="8" font-family="monospace">e⁻→</text>
    <text x="240" y="185" text-anchor="middle" fill="#e3b341" font-size="9" font-family="monospace">DISCHARGE: Li⁺ moves anode→cathode through electrolyte</text>
  </svg>
</div>

<div class="diag-wrap">
  <div class="diag-title">Ion Exchange Water Softening</div>
  <svg viewBox="0 0 480 180" width="100%" style="max-width:480px">
    <rect width="480" height="180" fill="#0d1117" rx="6"/>
    <!-- arrow in -->
    <line x1="10" y1="90" x2="60" y2="90" stroke="#f85149" stroke-width="2"/>
    <polygon points="55,85 65,90 55,95" fill="#f85149"/>
    <text x="35" y="80" text-anchor="middle" fill="#f85149" font-size="9" font-family="monospace">Hard</text>
    <text x="35" y="93" text-anchor="middle" fill="#f85149" font-size="9" font-family="monospace">Water</text>
    <text x="35" y="106" text-anchor="middle" fill="#f85149" font-size="8" font-family="monospace">Ca²⁺,Mg²⁺</text>
    <!-- cation exchanger -->
    <rect x="65" y="40" width="130" height="100" fill="rgba(88,166,255,0.1)" stroke="#58a6ff" stroke-width="2" rx="6"/>
    <text x="130" y="65" text-anchor="middle" fill="#58a6ff" font-size="10" font-family="monospace">CATION</text>
    <text x="130" y="80" text-anchor="middle" fill="#58a6ff" font-size="10" font-family="monospace">EXCHANGER</text>
    <text x="130" y="98" text-anchor="middle" fill="#e6edf3" font-size="8" font-family="monospace">Na⁺ resin removes</text>
    <text x="130" y="112" text-anchor="middle" fill="#e6edf3" font-size="8" font-family="monospace">Ca²⁺ and Mg²⁺</text>
    <text x="130" y="128" text-anchor="middle" fill="#e3b341" font-size="8" font-family="monospace">2NaR+Ca²⁺→CaR₂+2Na⁺</text>
    <!-- arrow between -->
    <line x1="195" y1="90" x2="240" y2="90" stroke="#8b949e" stroke-width="2"/>
    <polygon points="235,85 245,90 235,95" fill="#8b949e"/>
    <!-- anion exchanger -->
    <rect x="245" y="40" width="130" height="100" fill="rgba(63,185,80,0.1)" stroke="#3fb950" stroke-width="2" rx="6"/>
    <text x="310" y="65" text-anchor="middle" fill="#3fb950" font-size="10" font-family="monospace">ANION</text>
    <text x="310" y="80" text-anchor="middle" fill="#3fb950" font-size="10" font-family="monospace">EXCHANGER</text>
    <text x="310" y="98" text-anchor="middle" fill="#e6edf3" font-size="8" font-family="monospace">OH⁻ resin removes</text>
    <text x="310" y="112" text-anchor="middle" fill="#e6edf3" font-size="8" font-family="monospace">Cl⁻, SO₄²⁻, HCO₃⁻</text>
    <!-- arrow out -->
    <line x1="375" y1="90" x2="420" y2="90" stroke="#3fb950" stroke-width="2"/>
    <polygon points="415,85 425,90 415,95" fill="#3fb950"/>
    <text x="445" y="80" text-anchor="middle" fill="#3fb950" font-size="9" font-family="monospace">Soft</text>
    <text x="445" y="93" text-anchor="middle" fill="#3fb950" font-size="9" font-family="monospace">Water</text>
    <text x="445" y="106" text-anchor="middle" fill="#3fb950" font-size="8" font-family="monospace">Pure</text>
    <text x="240" y="170" text-anchor="middle" fill="#e3b341" font-size="9" font-family="monospace">Regeneration: cation resin with NaCl, anion resin with NaOH</text>
  </svg>
</div>
</div>

<!-- DS DIAGRAMS -->
<div id="diag-ds" style="display:none">
<div class="diag-wrap">
  <div class="diag-title">BST: Inserting 45,20,10,30,60,50,75</div>
  <svg viewBox="0 0 480 230" width="100%" style="max-width:480px">
    <rect width="480" height="230" fill="#0d1117" rx="6"/>
    <!-- nodes -->
    <circle cx="240" cy="35" r="20" fill="rgba(88,166,255,0.15)" stroke="#58a6ff" stroke-width="2"/>
    <text x="240" y="40" text-anchor="middle" fill="#58a6ff" font-size="12" font-family="monospace" font-weight="bold">45</text>
    <!-- left subtree -->
    <circle cx="140" cy="95" r="20" fill="rgba(63,185,80,0.15)" stroke="#3fb950" stroke-width="2"/>
    <text x="140" y="100" text-anchor="middle" fill="#3fb950" font-size="12" font-family="monospace" font-weight="bold">20</text>
    <circle cx="80" cy="155" r="20" fill="rgba(63,185,80,0.12)" stroke="#3fb950" stroke-width="1.5"/>
    <text x="80" y="160" text-anchor="middle" fill="#3fb950" font-size="12" font-family="monospace">10</text>
    <circle cx="200" cy="155" r="20" fill="rgba(63,185,80,0.12)" stroke="#3fb950" stroke-width="1.5"/>
    <text x="200" y="160" text-anchor="middle" fill="#3fb950" font-size="12" font-family="monospace">30</text>
    <!-- right subtree -->
    <circle cx="340" cy="95" r="20" fill="rgba(255,166,87,0.15)" stroke="#ffa657" stroke-width="2"/>
    <text x="340" y="100" text-anchor="middle" fill="#ffa657" font-size="12" font-family="monospace" font-weight="bold">60</text>
    <circle cx="295" cy="155" r="20" fill="rgba(255,166,87,0.12)" stroke="#ffa657" stroke-width="1.5"/>
    <text x="295" y="160" text-anchor="middle" fill="#ffa657" font-size="12" font-family="monospace">50</text>
    <circle cx="390" cy="155" r="20" fill="rgba(255,166,87,0.12)" stroke="#ffa657" stroke-width="1.5"/>
    <text x="390" y="160" text-anchor="middle" fill="#ffa657" font-size="12" font-family="monospace">75</text>
    <!-- edges -->
    <line x1="224" y1="50" x2="157" y2="80" stroke="#8b949e" stroke-width="1.5"/>
    <line x1="256" y1="50" x2="323" y2="80" stroke="#8b949e" stroke-width="1.5"/>
    <line x1="123" y1="108" x2="97" y2="140" stroke="#8b949e" stroke-width="1.5"/>
    <line x1="157" y1="108" x2="183" y2="140" stroke="#8b949e" stroke-width="1.5"/>
    <line x1="323" y1="108" x2="312" y2="140" stroke="#8b949e" stroke-width="1.5"/>
    <line x1="357" y1="108" x2="373" y2="140" stroke="#8b949e" stroke-width="1.5"/>
    <!-- legend -->
    <text x="30" y="200" fill="#58a6ff" font-size="9" font-family="monospace">Root=45</text>
    <text x="90" y="200" fill="#3fb950" font-size="9" font-family="monospace">Left (smaller)</text>
    <text x="200" y="200" fill="#ffa657" font-size="9" font-family="monospace">Right (larger)</text>
    <text x="240" y="220" text-anchor="middle" fill="#e3b341" font-size="9" font-family="monospace">Rule: smaller→left, larger→right at each node</text>
  </svg>
</div>

<div class="diag-wrap">
  <div class="diag-title">AVL Tree — 4 Types of Rotations</div>
  <svg viewBox="0 0 480 280" width="100%" style="max-width:480px">
    <rect width="480" height="280" fill="#0d1117" rx="6"/>
    <!-- LL Rotation -->
    <text x="60" y="18" text-anchor="middle" fill="#f85149" font-size="10" font-weight="bold" font-family="monospace">LL Rotation</text>
    <text x="60" y="30" text-anchor="middle" fill="#8b949e" font-size="8" font-family="monospace">(Right Rotate)</text>
    <circle cx="60" cy="55" r="16" fill="rgba(248,81,73,0.15)" stroke="#f85149" stroke-width="2"/>
    <text x="60" y="59" text-anchor="middle" fill="#f85149" font-size="10" font-family="monospace">C(+2)</text>
    <circle cx="35" cy="90" r="14" fill="rgba(248,81,73,0.1)" stroke="#f85149" stroke-width="1.5"/>
    <text x="35" y="94" text-anchor="middle" fill="#f85149" font-size="10" font-family="monospace">B(+1)</text>
    <circle cx="18" cy="122" r="12" fill="rgba(248,81,73,0.08)" stroke="#f85149" stroke-width="1.5"/>
    <text x="18" y="126" text-anchor="middle" fill="#f85149" font-size="9" font-family="monospace">A</text>
    <line x1="46" y1="68" x2="42" y2="78" stroke="#8b949e" stroke-width="1"/>
    <line x1="28" y1="102" x2="24" y2="112" stroke="#8b949e" stroke-width="1"/>
    <text x="78" y="90" fill="#8b949e" font-size="9" font-family="monospace">→</text>
    <circle cx="100" cy="90" r="14" fill="rgba(63,185,80,0.15)" stroke="#3fb950" stroke-width="2"/>
    <text x="100" y="94" text-anchor="middle" fill="#3fb950" font-size="9" font-family="monospace">B root</text>
    <circle cx="80" cy="122" r="12" fill="rgba(63,185,80,0.1)" stroke="#3fb950" stroke-width="1.5"/>
    <text x="80" y="126" text-anchor="middle" fill="#3fb950" font-size="9" font-family="monospace">A</text>
    <circle cx="122" cy="122" r="12" fill="rgba(63,185,80,0.1)" stroke="#3fb950" stroke-width="1.5"/>
    <text x="122" y="126" text-anchor="middle" fill="#3fb950" font-size="9" font-family="monospace">C</text>
    <line x1="87" y1="102" x2="84" y2="112" stroke="#8b949e" stroke-width="1"/>
    <line x1="113" y1="102" x2="118" y2="112" stroke="#8b949e" stroke-width="1"/>

    <!-- RR Rotation -->
    <text x="250" y="18" text-anchor="middle" fill="#d2a8ff" font-size="10" font-weight="bold" font-family="monospace">RR Rotation</text>
    <text x="250" y="30" text-anchor="middle" fill="#8b949e" font-size="8" font-family="monospace">(Left Rotate)</text>
    <circle cx="230" cy="55" r="16" fill="rgba(210,168,255,0.15)" stroke="#d2a8ff" stroke-width="2"/>
    <text x="230" y="59" text-anchor="middle" fill="#d2a8ff" font-size="10" font-family="monospace">A(−2)</text>
    <circle cx="255" cy="90" r="14" fill="rgba(210,168,255,0.1)" stroke="#d2a8ff" stroke-width="1.5"/>
    <text x="255" y="94" text-anchor="middle" fill="#d2a8ff" font-size="10" font-family="monospace">B(−1)</text>
    <circle cx="272" cy="122" r="12" fill="rgba(210,168,255,0.08)" stroke="#d2a8ff" stroke-width="1.5"/>
    <text x="272" y="126" text-anchor="middle" fill="#d2a8ff" font-size="9" font-family="monospace">C</text>
    <line x1="244" y1="68" x2="248" y2="78" stroke="#8b949e" stroke-width="1"/>
    <line x1="262" y1="102" x2="268" y2="112" stroke="#8b949e" stroke-width="1"/>
    <text x="295" y="90" fill="#8b949e" font-size="9" font-family="monospace">→</text>
    <circle cx="325" cy="90" r="14" fill="rgba(63,185,80,0.15)" stroke="#3fb950" stroke-width="2"/>
    <text x="325" y="94" text-anchor="middle" fill="#3fb950" font-size="9" font-family="monospace">B root</text>
    <circle cx="305" cy="122" r="12" fill="rgba(63,185,80,0.1)" stroke="#3fb950" stroke-width="1.5"/>
    <text x="305" y="126" text-anchor="middle" fill="#3fb950" font-size="9" font-family="monospace">A</text>
    <circle cx="347" cy="122" r="12" fill="rgba(63,185,80,0.1)" stroke="#3fb950" stroke-width="1.5"/>
    <text x="347" y="126" text-anchor="middle" fill="#3fb950" font-size="9" font-family="monospace">C</text>

    <!-- LR and RL descriptions -->
    <line x1="10" y1="150" x2="470" y2="150" stroke="#30363d" stroke-width="1"/>
    <text x="120" y="175" text-anchor="middle" fill="#ffa657" font-size="10" font-weight="bold" font-family="monospace">LR Rotation (Double)</text>
    <text x="120" y="192" text-anchor="middle" fill="#e6edf3" font-size="9" font-family="monospace">Step 1: Left rotate the LEFT child</text>
    <text x="120" y="207" text-anchor="middle" fill="#e6edf3" font-size="9" font-family="monospace">Step 2: Right rotate the parent node</text>
    <text x="120" y="222" text-anchor="middle" fill="#8b949e" font-size="8" font-family="monospace">BF = +2, left-right case</text>

    <text x="360" y="175" text-anchor="middle" fill="#ffa657" font-size="10" font-weight="bold" font-family="monospace">RL Rotation (Double)</text>
    <text x="360" y="192" text-anchor="middle" fill="#e6edf3" font-size="9" font-family="monospace">Step 1: Right rotate the RIGHT child</text>
    <text x="360" y="207" text-anchor="middle" fill="#e6edf3" font-size="9" font-family="monospace">Step 2: Left rotate the parent node</text>
    <text x="360" y="222" text-anchor="middle" fill="#8b949e" font-size="8" font-family="monospace">BF = −2, right-left case</text>

    <text x="240" y="258" text-anchor="middle" fill="#e3b341" font-size="9" font-family="monospace">BF = Height(Left) − Height(Right) | Valid: {−1, 0, +1}</text>
    <text x="240" y="272" text-anchor="middle" fill="#e3b341" font-size="9" font-family="monospace">Always draw BEFORE and AFTER rotation in exam!</text>
  </svg>
</div>
</div>

<!-- DRAWING DIAGRAMS -->
<div id="diag-draw" style="display:none">
<div class="diag-wrap">
  <div class="diag-title">1st Angle vs 3rd Angle Projection</div>
  <svg viewBox="0 0 480 220" width="100%" style="max-width:480px">
    <rect width="480" height="220" fill="#0d1117" rx="6"/>
    <!-- 1st angle -->
    <text x="110" y="18" text-anchor="middle" fill="#58a6ff" font-size="12" font-weight="bold" font-family="monospace">1st Angle (European)</text>
    <line x1="20" y1="110" x2="220" y2="110" stroke="#8b949e" stroke-width="1.5"/>
    <line x1="110" y1="25" x2="110" y2="200" stroke="#8b949e" stroke-width="1.5"/>
    <rect x="60" y="55" width="50" height="50" fill="rgba(88,166,255,0.1)" stroke="#58a6ff" stroke-width="2" rx="2"/>
    <text x="85" y="85" text-anchor="middle" fill="#58a6ff" font-size="9" font-family="monospace">FRONT</text>
    <rect x="15" y="120" width="50" height="35" fill="rgba(63,185,80,0.1)" stroke="#3fb950" stroke-width="1.5" rx="2"/>
    <text x="40" y="142" text-anchor="middle" fill="#3fb950" font-size="9" font-family="monospace">TOP</text>
    <text x="40" y="153" text-anchor="middle" fill="#8b949e" font-size="7" font-family="monospace">(below FV)</text>
    <rect x="118" y="55" width="40" height="50" fill="rgba(255,166,87,0.1)" stroke="#ffa657" stroke-width="1.5" rx="2"/>
    <text x="138" y="84" text-anchor="middle" fill="#ffa657" font-size="8" font-family="monospace">SIDE</text>
    <text x="138" y="94" text-anchor="middle" fill="#8b949e" font-size="7" font-family="monospace">(right of FV)</text>
    <text x="110" y="210" text-anchor="middle" fill="#8b949e" font-size="8" font-family="monospace">Object between observer & plane</text>

    <!-- 3rd angle -->
    <text x="370" y="18" text-anchor="middle" fill="#d2a8ff" font-size="12" font-weight="bold" font-family="monospace">3rd Angle (American)</text>
    <line x1="260" y1="110" x2="470" y2="110" stroke="#8b949e" stroke-width="1.5"/>
    <line x1="360" y1="25" x2="360" y2="200" stroke="#8b949e" stroke-width="1.5"/>
    <rect x="310" y="55" width="50" height="50" fill="rgba(210,168,255,0.1)" stroke="#d2a8ff" stroke-width="2" rx="2"/>
    <text x="335" y="85" text-anchor="middle" fill="#d2a8ff" font-size="9" font-family="monospace">FRONT</text>
    <rect x="265" y="55" width="40" height="50" fill="rgba(63,185,80,0.1)" stroke="#3fb950" stroke-width="1.5" rx="2"/>
    <text x="285" y="84" text-anchor="middle" fill="#3fb950" font-size="8" font-family="monospace">SIDE</text>
    <text x="285" y="94" text-anchor="middle" fill="#8b949e" font-size="7" font-family="monospace">(left of FV)</text>
    <rect x="265" y="25" width="85" height="30" fill="rgba(255,166,87,0.1)" stroke="#ffa657" stroke-width="1.5" rx="2"/>
    <text x="307" y="44" text-anchor="middle" fill="#ffa657" font-size="8" font-family="monospace">TOP VIEW (above FV)</text>
    <text x="370" y="210" text-anchor="middle" fill="#8b949e" font-size="8" font-family="monospace">Plane between observer & object</text>
  </svg>
</div>

<div class="diag-wrap">
  <div class="diag-title">Projections of a Point — All 4 Quadrants</div>
  <svg viewBox="0 0 480 230" width="100%" style="max-width:480px">
    <rect width="480" height="230" fill="#0d1117" rx="6"/>
    <line x1="20" y1="115" x2="460" y2="115" stroke="#e3b341" stroke-width="2"/>
    <text x="460" y="112" fill="#e3b341" font-size="10" font-family="monospace">X</text>
    <text x="230" y="113" fill="#e3b341" font-size="10" font-family="monospace">Y</text>
    <!-- quadrant labels -->
    <text x="115" y="58" text-anchor="middle" fill="#8b949e" font-size="9" font-family="monospace">I (above HP, front VP)</text>
    <text x="345" y="58" text-anchor="middle" fill="#8b949e" font-size="9" font-family="monospace">II (above HP, behind VP)</text>
    <text x="115" y="170" text-anchor="middle" fill="#8b949e" font-size="9" font-family="monospace">IV (below HP, front VP)</text>
    <text x="345" y="170" text-anchor="middle" fill="#8b949e" font-size="9" font-family="monospace">III (below HP, behind VP)</text>
    <!-- point example in Q1 -->
    <circle cx="100" cy="70" r="5" fill="#58a6ff"/>
    <text x="108" y="68" fill="#58a6ff" font-size="9" font-family="monospace">P (above HP)</text>
    <line x1="100" y1="75" x2="100" y2="115" stroke="#58a6ff" stroke-width="1" stroke-dasharray="4"/>
    <circle cx="100" cy="145" r="5" fill="#3fb950"/>
    <text x="108" y="148" fill="#3fb950" font-size="9" font-family="monospace">p (top view below xy)</text>
    <line x1="100" y1="70" x2="100" y2="115" stroke="#58a6ff" stroke-width="1" stroke-dasharray="4"/>
    <circle cx="100" cy="90" r="5" fill="#ffa657"/>
    <text x="108" y="88" fill="#ffa657" font-size="9" font-family="monospace">p' (front view above xy)</text>
    <!-- rules -->
    <text x="240" y="200" text-anchor="middle" fill="#e6edf3" font-size="9" font-family="monospace">FV above xy = point is above HP | FV below xy = point is below HP</text>
    <text x="240" y="215" text-anchor="middle" fill="#e6edf3" font-size="9" font-family="monospace">TV below xy = point is in front of VP | TV above xy = point is behind VP</text>
  </svg>
</div>

<div class="diag-wrap">
  <div class="diag-title">Isometric Axes — 120° Arrangement</div>
  <svg viewBox="0 0 480 200" width="100%" style="max-width:480px">
    <rect width="480" height="200" fill="#0d1117" rx="6"/>
    <!-- isometric box -->
    <polygon points="240,20 370,95 240,170 110,95" fill="none" stroke="#30363d" stroke-width="1"/>
    <!-- top face -->
    <polygon points="240,20 370,95 240,95 110,95" fill="rgba(88,166,255,0.08)" stroke="#58a6ff" stroke-width="1.5"/>
    <!-- left face -->
    <polygon points="110,95 240,95 240,170 110,170" fill="rgba(63,185,80,0.08)" stroke="#3fb950" stroke-width="1.5"/>
    <!-- right face -->
    <polygon points="370,95 240,95 240,170 370,170" fill="rgba(255,166,87,0.08)" stroke="#ffa657" stroke-width="1.5"/>
    <!-- axes -->
    <line x1="240" y1="95" x2="370" y2="20" stroke="#58a6ff" stroke-width="2.5"/>
    <text x="378" y="18" fill="#58a6ff" font-size="10" font-family="monospace">Z (vertical)</text>
    <line x1="240" y1="95" x2="110" y2="170" stroke="#3fb950" stroke-width="2.5"/>
    <text x="40" y="172" fill="#3fb950" font-size="10" font-family="monospace">Y (30° left)</text>
    <line x1="240" y1="95" x2="370" y2="170" stroke="#ffa657" stroke-width="2.5"/>
    <text x="372" y="172" fill="#ffa657" font-size="10" font-family="monospace">X (30° right)</text>
    <!-- angle labels -->
    <text x="240" y="90" text-anchor="middle" fill="#e3b341" font-size="9" font-family="monospace">Origin</text>
    <text x="240" y="190" text-anchor="middle" fill="#e3b341" font-size="9" font-family="monospace">All 3 axes at 120° to each other · X and Y at 30° to horizontal</text>
  </svg>
</div>
</div>
</div>

<!-- ======= D-E-D-P ALL UNITS ======= -->
<div id="page-dedp" class="page">
<div class="pt">✍️ D-E-D-P — Every Unit, Every Subject</div>
<div class="ps">Shortcut answer format for exam · Definition → Equation → Diagram → Points</div>

<div class="ok" style="margin-bottom:12px">Stop writing paragraphs. For every 5-mark answer: D (2 lines) → E (box the formula) → D (draw diagram) → P (4-5 bullet points). This format gets FULL marks.</div>

<div class="tabs">
  <button class="tab active" onclick="sw('unit','bee',this)">BEE Units</button>
  <button class="tab" onclick="sw('unit','chem',this)">Chemistry Units</button>
  <button class="tab" onclick="sw('unit','ds',this)">DS Units</button>
  <button class="tab" onclick="sw('unit','odvc',this)">ODVC Units</button>
  <button class="tab" onclick="sw('unit','draw',this)">Drawing Units</button>
</div>

<!-- BEE D-E-D-P -->
<div id="unit-bee">
<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>BEE Unit 1 · DC Circuits — Thevenin's Theorem</span><span>▼</span></div>
<div class="acc-bd open">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Any linear two-terminal circuit can be replaced by a single voltage source (V_th) in series with resistance (R_th) looking into the terminals.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>V_th = V_oc (open circuit voltage at terminals)<br>R_th = resistance with all sources deactivated<br>I_L = V_th / (R_th + R_L)</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Draw: original circuit → Step 1 remove load R_L → find V_oc = V_th → Step 2 kill sources (V→short, I→open), find R_th → Draw final equivalent: V_th in series with R_th and R_L</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>Works for any linear circuit</li><li>V: short circuit, I: open circuit when deactivating</li><li>Find V_oc with load open</li><li>Find I_sc (short circuit current)</li><li>R_th = V_th / I_sc alternatively</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>BEE Unit 2 · AC Circuits — Series RLC & Resonance</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>In series RLC circuit, at resonance the inductive reactance equals capacitive reactance (X_L=X_C), impedance is purely resistive and minimum, current is maximum.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>f_r = 1/(2π√LC) ← resonant frequency<br>Z = R (minimum at resonance)<br>I_max = V/R<br>Q-factor = ω_r L/R = V_L/V or V_C/V</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Draw series circuit: AC source → R → L → C → back to source. Draw impedance vs frequency curve showing Z minimum at f_r. Draw phasor diagram for resonance: V_R = V (only resistive drop)</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>At resonance: X_L = X_C, Z = R (minimum)</li><li>Current is maximum at resonance</li><li>Power factor = 1 (unity) at resonance</li><li>Bandwidth = f_r/Q</li><li>Higher Q = sharper resonance = more selective</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>BEE Unit 3 · Transformer — EMF & Efficiency</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Transformer transfers electrical energy between two circuits by electromagnetic induction without electrical connection, changing voltage/current levels at same frequency.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>E = 4.44 × f × N × Φ_m ← MUST BOX THIS<br>Turns ratio: a = N₁/N₂ = V₁/V₂ = I₂/I₁<br>η = P_out/(P_out+Cu loss+Fe loss) × 100%<br>At max η: Cu loss = Iron loss</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Draw: Primary (N₁) | Iron Core with flux φ | Secondary (N₂). Label: AC input V₁, laminated core, mutual flux Φ, output V₂, load. Show shell type OR core type cross-section.</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>Based on Faraday's law of EM induction</li><li>Step-up: N₂&gt;N₁, V₂&gt;V₁, I₂&lt;I₁</li><li>Losses: Copper (I²R) + Iron (eddy+hysteresis)</li><li>Core laminated to reduce eddy currents</li><li>Efficiency typically 95-99% for power transformers</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>BEE Unit 4 · DC & AC Machines</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>DC motor converts electrical energy to mechanical energy. Working on Fleming's left-hand rule — current-carrying conductor in magnetic field experiences force (torque).</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>Back EMF: E_b = V − I_a × R_a<br>Torque: T = (P×φ×Z×I_a)/(2πA) Nm<br>Speed: N ∝ E_b/φ<br>Induction Motor slip: s = (N_s−N_r)/N_s</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>DC Motor cross-section: Field poles (stator), Armature (rotor with coils), Commutator, Brushes. Label: field winding, armature winding, commutator segments, brush contact. Show current direction and force direction.</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>DC Motor types: series, shunt, compound</li><li>Series motor: high starting torque (used in cranes)</li><li>Shunt motor: constant speed (used in lathe)</li><li>3-phase induction: self-starting, rugged, no brushes</li><li>Single-phase induction: not self-starting, needs auxiliary</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>BEE Unit 5 · Electrical Installations & Power Factor</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Power factor = cosφ = ratio of active power (W) to apparent power (VA). Low PF means more current drawn for same power → higher losses in cables.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>PF = P/S = cosφ = R/Z<br>P = VIcosφ (W) | Q = VIsinφ (VAR) | S = VI (VA)<br>S² = P² + Q²<br>PF improvement: add capacitor bank (C) in parallel</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Draw power triangle: horizontal P (kW), vertical Q (kVAR), hypotenuse S (kVA), angle φ. Show how adding capacitor C reduces Q_net → smaller angle φ → improved PF closer to 1.</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>MCB: protects against overload + short circuit</li><li>ELCB: protects against earth leakage</li><li>SFU: Switch-Fuse Unit for isolation + protection</li><li>Earthing: safety against electric shock</li><li>PF improvement saves energy, reduces line losses</li></ul></div>
</div>
</div></div>
</div>

<!-- CHEMISTRY D-E-D-P -->
<div id="unit-chem" style="display:none">
<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>Chemistry Unit 1 · Water Treatment — Hardness & Softening</span><span>▼</span></div>
<div class="acc-bd open">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Hardness of water is inability to produce lather with soap due to dissolved Ca²⁺ and Mg²⁺ salts. Types: Temporary (carbonates, removed by boiling) and Permanent (sulphates/chlorides, need chemical treatment).</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>Temporary: Ca(HCO₃)₂ → CaCO₃↓ + CO₂ + H₂O (on boiling)<br>Permanent: CaSO₄ + Na₂CO₃ → CaCO₃↓ + Na₂SO₄<br>Hardness (ppm) = Vol(EDTA)×M×100000/Vol(sample)</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Draw ion exchange setup: Hard water → Cation resin column (Na form) → removes Ca²⁺/Mg²⁺ → Anion resin column (OH form) → removes anions → Soft/demineralized water out</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>Temporary hardness: boiling or lime addition</li><li>Permanent hardness: ion exchange or RO</li><li>EDTA method: complexometric estimation (wine red→steel blue)</li><li>Boiler scaling from hardness → reduces heat transfer</li><li>Sludge ≠ scale (sludge = loose, scale = hard deposits)</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>Chemistry Unit 2 · Corrosion — Galvanic & Wet Corrosion</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Corrosion is electrochemical degradation of metals due to environment interaction. Wet corrosion needs moisture/electrolyte. Forms anodic (oxidation) and cathodic (reduction) areas.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>Anode: Fe → Fe²⁺ + 2e⁻ (oxidation)<br>Cathode: O₂ + 2H₂O + 4e⁻ → 4OH⁻<br>Fe²⁺ + 2OH⁻ → Fe(OH)₂ → Fe₂O₃ (rust)<br>P-B ratio = Vol(oxide)/Vol(metal)</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Draw iron piece in water. Mark anodic area (−) where pits form. Cathodic area (+) where rust appears nearby. Show e⁻ flow through metal from anode to cathode. Show OH⁻ migrating in solution.</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>Larger area of anodic region → more severe corrosion</li><li>Acidic pH accelerates corrosion</li><li>Galvanic corrosion: dissimilar metals in contact</li><li>Control: cathodic protection, sacrificial anode (Mg/Zn)</li><li>Impressed current method: external DC source</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>Chemistry Unit 3 · Batteries — Li-ion & Fuel Cells</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Battery is an electrochemical device that converts chemical energy to electrical energy. Primary: non-rechargeable. Secondary: rechargeable (e.g., Li-ion). Fuel cell: converts fuel energy directly to electricity.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>Li-ion discharge: LiC₆ → Li⁺ + e⁻ + C₆ (anode)<br>Li⁺ + e⁻ + CoO₂ → LiCoO₂ (cathode)<br>DMFC: CH₃OH+H₂O → CO₂+6H⁺+6e⁻ (anode)<br>Fuel cell OCV: E_cell = E°_cathode − E°_anode</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Li-ion: Graphite anode | PEM electrolyte | LiCoO₂ cathode. Li⁺ moves anode→cathode through membrane during discharge. e⁻ flow in external circuit = current. Draw both charge and discharge direction.</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>Li-ion: high energy density, lightweight, no memory effect</li><li>Zn-air: uses atmospheric O₂ as cathode reactant</li><li>Fuel cell vs battery: fuel cell has external fuel supply</li><li>DMFC efficiency: 40-60%, no combustion</li><li>Applications: EVs, portable electronics, aerospace</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>Chemistry Unit 4 · Polymers — Addition & Condensation</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Polymer is a large macromolecule made of repeating structural units (monomers) joined by covalent bonds. DP = degree of polymerization = number of repeating units.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>DP = Molecular Weight / Monomer Weight<br>Addition: nCH₂=CH₂ → (-CH₂-CH₂-)n (no byproduct)<br>Condensation: adipic acid + hexamethylene diamine → Nylon-6,6 + H₂O<br>Free radical: Initiation → Propagation → Termination</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Show monomer → polymer chain. For addition: ethylene double bond opens → chain grows. For condensation: two functional groups react → bond forms + H₂O released. Draw PVC structure: -[CH₂-CHCl]n-</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>Thermoplastic (PVC): soften on heating, remoldable</li><li>Thermosetting (Bakelite): set permanently on heating</li><li>Conducting polymers: polyacetylene, polythiophene</li><li>Biodegradable: Polylactic acid (PLA) from lactic acid</li><li>FRP: carbon/glass fiber in polymer matrix → lightweight+strong</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>Chemistry Unit 5 · Fuels & Lubricants</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Fuel is a substance that releases heat on combustion. Good fuel: high calorific value, low ignition temperature, easy storage, low cost, low ash content. Lubricant reduces friction between surfaces.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>CV = Heat released / Mass (kJ/kg or kcal/kg)<br>Dulong's formula: CV = 1/100[8084C + 34500(H−O/8) + 2240S]<br>LCV = HCV − 0.09H × 587 kcal/kg<br>Viscosity index (VI) = higher → better lubricant</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Thin film lubrication diagram: two surfaces (metal), lubricant film between them forming wedge shape. As speed increases, film pressure builds, surfaces separate completely (hydrodynamic lubrication).</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>HCV: water product in vapour form (latent heat included)</li><li>LCV: water product in liquid form (latent heat excluded)</li><li>Flash point: min temp at which oil vapour ignites momentarily</li><li>Pour point: min temp at which oil just flows</li><li>Green hydrogen: produced by electrolysis using renewable energy</li></ul></div>
</div>
</div></div>
</div>

<!-- DS D-E-D-P -->
<div id="unit-ds" style="display:none">
<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>DS Unit 1 · Linked Lists, Stacks & Queues</span><span>▼</span></div>
<div class="acc-bd open">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Linked list: dynamic data structure of nodes, each containing data and pointer(s) to next/previous node. Stack: LIFO. Queue: FIFO. No random access — sequential traversal only.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>Stack PUSH: Top++, a[Top]=item (O(1))<br>Stack POP: item=a[Top], Top-- (O(1))<br>Queue enqueue: Rear=(Rear+1)%n, Q[Rear]=item<br>Queue dequeue: item=Q[Front], Front=(Front+1)%n</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>SLL node: [DATA | NEXT→]. DLL node: [←PREV | DATA | NEXT→]. Stack: tower with TOP pointer, push adds at top, pop removes from top. Queue: horizontal with FRONT on left (dequeue), REAR on right (enqueue).</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>SLL: O(n) search, O(1) insert/delete at head</li><li>DLL: bidirectional traversal, uses more memory</li><li>CLL: last node → first node (circular)</li><li>Stack apps: function calls, undo, expression evaluation</li><li>Queue apps: CPU scheduling, BFS, printer spooling</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>DS Unit 2 · Binary Trees, BST & AVL Trees</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>BST: binary tree where left child &lt; parent &lt; right child. AVL tree: self-balancing BST where Balance Factor (BF) = h_L − h_R ∈ {−1,0,+1} maintained at every node via rotations.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>BST search: O(log n) avg, O(n) worst (skewed)<br>AVL BF = Height(Left) − Height(Right)<br>Max nodes at height h: 2^(h+1) − 1<br>Rotations: LL(right), RR(left), LR(left+right), RL(right+left)</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Draw BST with 5 nodes showing order property. For AVL: show before rotation (unbalanced BF=±2), show rotation arrows, show after rotation (all BF ∈ {−1,0,+1}). Label BF at each node.</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>Inorder traversal of BST gives sorted sequence</li><li>BST deletion: 3 cases (leaf, 1 child, 2 children)</li><li>2 children: replace with inorder successor/predecessor</li><li>AVL ensures O(log n) for all operations always</li><li>Threaded BST: null pointers replaced with inorder successor links</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>DS Unit 3 · B-Trees & Heaps</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>B-Tree of order m: balanced multi-way search tree. All leaves at same level. Each node has at most m children and m−1 keys. Used in databases for disk access optimization.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>Max keys per node = m−1<br>Min keys (non-root) = ⌈m/2⌉−1<br>Min children (non-root) = ⌈m/2⌉<br>B+ Tree: all data in leaf nodes, internal = index only</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Draw B-Tree of order 3 with values 10,20,5,15,30. Show splits when node overflows. Show how median key is promoted to parent. All leaf nodes at same level (key property).</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>Min-Heap: parent ≤ children. Max-Heap: parent ≥ children</li><li>Heap insert: O(log n) — add at end, bubble up</li><li>Heap delete-max: O(log n) — swap root+last, bubble down</li><li>Heapsort: build heap O(n), sort O(n log n)</li><li>B+ tree: faster sequential access (leaf linked list)</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>DS Unit 4 · Graphs & Graph Traversal</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Graph G = (V, E): set of vertices V and edges E. Directed graph (digraph): edges have direction. Undirected: edges bidirectional. BFS uses queue, DFS uses stack (or recursion).</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>BFS: O(V+E) using queue | DFS: O(V+E) using stack<br>Adjacency matrix: n×n matrix (O(n²) space)<br>Adjacency list: O(V+E) space<br>Degree of vertex v: number of edges incident on v</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Draw graph with 5 vertices. Show adjacency matrix below. Show BFS traversal order: start at vertex, visit all neighbors level by level (queue). Show DFS: go deep first before backtracking (stack).</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>BFS finds shortest path in unweighted graph</li><li>DFS used for topological sort, detecting cycles</li><li>Connected graph: path exists between every pair of vertices</li><li>Biconnected: removing any one vertex keeps graph connected</li><li>Applications: social networks, GPS navigation, internet routing</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>DS Unit 5 · Hashing & Collision Resolution</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Hashing maps keys to positions in a hash table using a hash function. Collision: two keys map to same position. Goal: O(1) average search, insert, delete.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>Division: h(k) = k mod m<br>Multiplication: h(k) = ⌊m(kA mod 1)⌋, A≈0.618<br>Load factor λ = n/m (n=items, m=table size)<br>Linear probing: h(k,i) = (h(k)+i) mod m</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Draw hash table with m=7 slots. Insert keys 15,7,22,34. Show h(k)=k mod 7 for each. When collision occurs (same slot), show linear probing (next slot) or chaining (linked list at slot).</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>Collision by chaining: linked list at each slot</li><li>Collision by open addressing: probe next slots</li><li>Linear probing: clustering problem</li><li>Quadratic probing: h(k,i) = (h(k)+i²) mod m</li><li>Double hashing: two hash functions, better distribution</li></ul></div>
</div>
</div></div>
</div>

<!-- ODVC D-E-D-P -->
<div id="unit-odvc" style="display:none">
<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>ODVC Unit 1 · First Order ODEs — Linear & Bernoulli's</span><span>▼</span></div>
<div class="acc-bd open">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Linear first-order ODE: dy/dx + P(x)y = Q(x). Non-linear Bernoulli: dy/dx + Py = Qy^n, solved by reducing to linear using substitution v = y^(1-n).</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>IF = e^(∫P dx)<br>Solution: y×IF = ∫(Q×IF)dx + C<br>Bernoulli: divide by y^n → let v=y^(1-n)<br>dv/dx + (1-n)Pv = (1-n)Q ← now linear, solve normally</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Steps Diagram</h5><p>Identify type → If linear: find IF → multiply → integrate both sides → get y.<br>If Bernoulli: divide by y^n → substitute v=y^(1-n) → linear ODE → find IF → integrate → back-substitute for y.</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>Newton's cooling: dT/dt = −k(T−T₀) → linear ODE</li><li>Growth/decay: dN/dt = kN → separable</li><li>Exact DE: M dx + N dy = 0, test ∂M/∂y = ∂N/∂x</li><li>Orthogonal trajectories: replace dy/dx with −dx/dy</li><li>Always check for exactness first before other methods</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>ODVC Unit 2 · Higher Order ODEs — CF and PI</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Higher order linear ODE: f(D)y = R(x) where D = d/dx. General solution = CF (complementary function from homogeneous) + PI (particular integral matching RHS).</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>Char. eq: replace D with m, solve polynomial.<br>PI for e^(ax): 1/f(D)e^(ax) = e^(ax)/f(a) if f(a)≠0<br>PI for sin(ax): 1/f(D²)sin(ax) = sin(ax)/f(−a²)<br>PI for xⁿ: expand 1/f(D) as series in D, operate on xⁿ<br>Variation of parameters: y_p = y₁∫(y₂R/W)dx − y₂∫(y₁R/W)dx</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Steps Diagram</h5><p>Step 1: Write char. equation (replace D→m). Step 2: Solve for roots m₁,m₂. Step 3: Write CF based on root type (real/equal/complex). Step 4: Find PI for each term of RHS. Step 5: GS = CF + PI.</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>Real distinct roots: CF has e^(m₁x) and e^(m₂x) terms</li><li>Equal roots: CF has e^(mx)(C₁+C₂x)</li><li>Complex α±βi: CF has e^(αx)[C₁cosβx+C₂sinβx]</li><li>If f(a)=0 for e^(ax): multiply by x and try again</li><li>Use variation of parameters when PI methods fail</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>ODVC Unit 3 · Laplace Transforms</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Laplace Transform converts a function of time f(t) into a function of complex frequency F(s): L{f(t)} = ∫₀^∞ e^(−st)f(t)dt. Used to solve IVPs by converting ODEs to algebraic equations.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>Key pairs: L{1}=1/s, L{e^(at)}=1/(s−a), L{sinkt}=k/(s²+k²)<br>L{coskt}=s/(s²+k²), L{t^n}=n!/s^(n+1)<br>L{f'(t)}=sF(s)−f(0) ← differentiation property<br>Convolution: L{f*g}=F(s)·G(s)</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Steps for IVP</h5><p>Take L of both sides → Algebraic equation in s → Apply initial conditions → Solve for Y(s) → Take inverse Laplace → Apply partial fractions or convolution → Get y(t)</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>Linearity: L{af+bg} = aF(s)+bG(s)</li><li>Shifting: L{e^(at)f(t)} = F(s−a)</li><li>Scaling: L{f(at)} = (1/a)F(s/a)</li><li>Inverse: use partial fractions then table lookup</li><li>Convolution theorem: avoids complex integration</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>ODVC Unit 4 · Vector Differentiation — Grad, Div, Curl</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Gradient of scalar φ: vector pointing in direction of max increase of φ. Divergence of A: scalar measuring outflow from a point. Curl of A: vector measuring rotation/circulation tendency.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>∇φ = (∂φ/∂x)i + (∂φ/∂y)j + (∂φ/∂z)k (Gradient)<br>∇·A = ∂Ax/∂x + ∂Ay/∂y + ∂Az/∂z (Divergence)<br>∇×A = det[i j k; ∂/∂x ∂/∂y ∂/∂z; Ax Ay Az] (Curl)<br>Solenoidal: ∇·A=0. Irrotational: ∇×A=0</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Gradient: arrows pointing uphill on contour map (perpendicular to contours). Divergence: positive = source (arrows out), negative = sink (arrows in). Curl: arrows forming circular pattern around axis (vortex).</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>Directional derivative of φ in direction â = ∇φ · â</li><li>Angle between surfaces: cosθ = (∇φ₁·∇φ₂)/(|∇φ₁||∇φ₂|)</li><li>∇²φ (Laplacian) = ∂²φ/∂x²+∂²φ/∂y²+∂²φ/∂z²</li><li>Conservative field: F = ∇φ (potential function exists)</li><li>Irrotational + simply connected → conservative</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>ODVC Unit 5 · Green's, Stokes', Gauss' Theorems</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Green's: relates line integral around closed curve to double integral over enclosed region. Stokes': relates line integral to surface integral. Gauss' (Divergence): relates surface integral to volume integral.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>Green's: ∮_C(M dx+N dy) = ∬_R(∂N/∂x−∂M/∂y)dA<br>Stokes': ∮_C F·dr = ∬_S(∇×F)·dS<br>Gauss': ∯_S F·dS = ∭_V(∇·F)dV<br>Line integral: ∫_C F·dr = ∫F_x dx+F_y dy+F_z dz</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Diagram</h5><p>Green's: 2D region R with boundary curve C (counterclockwise). Stokes': open surface S with boundary curve C. Gauss': closed surface S enclosing volume V with outward normal n̂. Draw and label all components.</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>Green's: converts hard line integrals to easier double integrals</li><li>Stokes': 3D generalization of Green's theorem</li><li>Gauss': converts surface to volume (easier to compute)</li><li>Use when given: "using Gauss' divergence theorem..."</li><li>Positive normal: outward from closed surface (Gauss)</li></ul></div>
</div>
</div></div>
</div>

<!-- DRAWING D-E-D-P -->
<div id="unit-draw" style="display:none">
<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>Drawing Unit 1 · Conic Sections — Ellipse, Parabola, Hyperbola</span><span>▼</span></div>
<div class="acc-bd open">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Conic sections: curves formed by intersection of a plane with a right circular cone. Defined by eccentricity e = PF/PD (ratio of distance from focus to distance from directrix).</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>Ellipse: e&lt;1, PF₁+PF₂=2a (constant)<br>Parabola: e=1, PF=PD<br>Hyperbola: e&gt;1, |PF₁−PF₂|=2a (constant)<br>Vertex of parabola V: midpoint of focus F and directrix</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Construction Steps</h5><p>1. Draw directrix DD'. 2. Mark focus F at given distance. 3. For parabola: vertex V = midpoint(F, directrix). 4. Mark points P using PF=PD. 5. Connect smoothly. 6. Tangent at P: bisect angle(FP, perpendicular from P to directrix).</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>Cycloid: circle rolling on straight line — point on rim traces cycloid</li><li>Involute: thread unwinding from circle traces involute</li><li>Involute used in gear tooth profile design</li><li>Cycloid used in gear teeth, ramps (brachistochrone)</li><li>Always label focus, directrix, vertex, tangent, normal</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>Drawing Unit 2 · Projections of Points & Lines</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Orthographic projection represents 3D objects on 2D planes. HP (horizontal plane), VP (vertical plane), xy = reference line = intersection of HP and VP. Front view (FV) on VP, Top view (TV) on HP.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>Point above HP → FV above xy | Point below HP → FV below xy<br>Point in front of VP → TV below xy | Point behind VP → TV above xy<br>Line inclined to VP: angle shown in TOP VIEW<br>Line inclined to HP: angle shown in FRONT VIEW</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Steps for Line</h5><p>1. Draw xy line. 2. Locate end points based on HP/VP distances. 3. FV: plot heights above/below xy (HP distances). 4. TV: plot depths above/below xy (VP distances). 5. Connect respective views with straight lines. 6. Draw projectors perpendicular to xy.</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>True length: appears in view where line is parallel to that plane</li><li>True inclination to HP: shown in FV (when parallel to VP)</li><li>True inclination to VP: shown in TV (when parallel to HP)</li><li>Auxiliary view needed for oblique lines</li><li>Projectors are always perpendicular to xy reference line</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>Drawing Unit 3 · Projections of Planes</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>A plane surface (rectangle, triangle, circle, hexagon etc.) when projected onto HP and VP gives views that show true shape only when plane is parallel to that projection plane.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>Parallel to HP → TV = true shape, FV = straight line<br>Parallel to VP → FV = true shape, TV = straight line<br>⊥HP, inclined to VP → TV = line at angle, FV = distorted<br>⊥VP, inclined to HP → FV = line at angle, TV = distorted</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Two-Step Method</h5><p>Step 1: Draw plane in simple position (parallel to HP or VP) → get true shape view. Step 2: Tilt to given inclination → other view changes shape/position accordingly. Draw projectors between the two steps to get final positions.</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>Edge view: plane appears as straight line in that view</li><li>True shape only when plane parallel to projection plane</li><li>Oblique plane: both views distorted → use auxiliary view</li><li>Perpendicular plane: appears as edge (line) in one view</li><li>Most exam questions: plane inclined to one plane only</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>Drawing Unit 4 · Projections of Solids & Sections</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Solid: 3D object with length, breadth, height. Types: Polyhedra (prism, pyramid) and Solids of revolution (cylinder, cone, sphere). Section: cutting plane reveals internal shape.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>Prism resting on HP → base in TV = true shape<br>Cylinder axis ⊥HP → circle in TV, rectangle in FV<br>Section parallel to base → circle/rectangle section<br>Section inclined to axis → ellipse (cylinder/cone)</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Steps for Solid Projection</h5><p>1. Draw FV (front elevation) first. 2. Project down to get TV (plan). 3. Project sideways for SV (side view). 4. For sections: draw cutting plane line in FV. 5. Find intersection points. 6. Project to TV. 7. Draw sectional view using section lining (hatching).</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>Section plane ∥ base → true shape of section = base shape</li><li>Section plane inclined → ellipse for cylinder/cone</li><li>Frustum: solid between two parallel sections of pyramid/cone</li><li>Hatching: 45° parallel lines on cut surfaces</li><li>Auxiliary view needed when solid is inclined to both planes</li></ul></div>
</div>
</div></div>

<div class="acc"><div class="acc-hd" onclick="tog(this)"><span>Drawing Unit 5 · Isometric Projections & Conversions</span><span>▼</span></div>
<div class="acc-bd">
<div class="dedp">
  <div class="dc dd"><h5 style="color:var(--accent)">D</h5><p>Isometric projection: axonometric projection where three principal axes appear equally foreshortened, making 120° with each other. Two axes at 30° to horizontal, one vertical. Shows 3D appearance in single view.</p></div>
  <div class="dc de"><h5 style="color:var(--green)">E</h5><p>Isometric scale = true scale × cos30°/cos45° = 0.816<br>Isometric drawing: use true measurements (not isometric scale)<br>X and Y axes: 30° to horizontal<br>Z axis: vertical (height)</p></div>
  <div class="dc dd2"><h5 style="color:var(--purple)">D — Steps</h5><p>1. Draw isometric axes (30°, 30°, vertical). 2. Mark dimensions along respective axes. 3. Draw box if object is block-like. 4. Complete shape by adding/removing features. 5. For circle: construct rhombus in isometric → draw 4-arc approximation (ellipse).</p></div>
  <div class="dc dp"><h5 style="color:var(--orange)">P</h5><ul><li>Non-isometric lines: cannot measure directly — plot endpoints only</li><li>Isometric circle: draw as rhombus, draw 4 arcs inside</li><li>Conversion to ortho: identify FV, TV, SV from isometric</li><li>Ortho to isometric: start from corner, build along axes</li><li>Hidden lines usually omitted in isometric drawings</li></ul></div>
</div>
</div></div>
</div>
</div>

<!-- ======= CYBER ======= -->
<div id="page-cyber" class="page">
<div class="pt">🛡️ Cybersecurity Roadmap</div>
<div class="ps">From zero → FZ-X money · Free resources · 10 min/day</div>
<div class="tip">Every concept you learn = future income. ₹1000 in a Udemy sale course (₹450) = ₹1.5L career return.</div>
<div class="cstep"><div class="csn">1</div><div class="cst"><h4>Linux Basics (Month 1)</h4><p>Free: linuxjourney.com · Learn: ls, cd, cat, chmod, grep, ssh · Why: All hacking runs on Linux</p></div></div>
<div class="cstep"><div class="csn">2</div><div class="cst"><h4>Networking Fundamentals (Month 2)</h4><p>Free: Professor Messer Network+ YouTube · Learn: IP, TCP/UDP, DNS, HTTP, Firewalls · Why: Can't hack what you don't understand</p></div></div>
<div class="cstep"><div class="csn">3</div><div class="cst"><h4>Python for Security (Month 3)</h4><p>You already have Python lab! · Learn: socket, requests, subprocess modules · Why: Most security tools are Python scripts</p></div></div>
<div class="cstep"><div class="csn">4</div><div class="cst"><h4>Web Security (Month 4)</h4><p>Free: PortSwigger Web Academy (world-class, 100% free) · Learn: XSS, SQL Injection, IDOR · Why: Companies pay bug bounties for these</p></div></div>
<div class="cstep"><div class="csn">5</div><div class="cst"><h4>CTF Practice (Month 5+)</h4><p>Free: TryHackMe, HackTheBox · Do 1 easy room/week · Why: Builds portfolio to show clients/employers</p></div></div>
<div class="cstep"><div class="csn">6</div><div class="cst"><h4>Bug Bounty + Freelancing (Month 6+)</h4><p>Platforms: HackerOne, Bugcrowd · First earn: ₹500-2000/bug · Scales to: ₹50,000+/month</p></div></div>
<div class="card" style="margin-top:12px">
  <div class="ct">🏍️ Path to ₹1.5L (Yamaha FZ-X)</div>
  <div class="rl"><span class="rn">Now</span>Excel/data entry on Fiverr (you have this!) → ₹500-2000/project</div>
  <div class="rl"><span class="rn">Month 3</span>Python automation scripts on Upwork → ₹2000-5000/project</div>
  <div class="rl"><span class="rn">Month 6</span>Bug bounty + security consulting → ₹5000-20000/month</div>
  <div class="rl"><span class="rn">Month 9</span>₹1.5L → Yamaha FZ-X is yours</div>
</div>
</div>

<!-- ======= FITNESS ======= -->
<div id="page-fitness" class="page">
<div class="pt">🏋️ Fitness + Bike Goal</div>
<div class="ps">Current: >100kg · Target: 80kg · FZ-X Goal: ₹1.5L</div>
<div class="g2">
<div class="card">
  <div class="ct">🌅 Daily Gym Checklist</div>
  <div class="task" onclick="chk(this,false)"><input type="checkbox"><span>20 min incline treadmill walk</span></div>
  <div class="task" onclick="chk(this,false)"><input type="checkbox"><span>3×15 push-ups</span></div>
  <div class="task" onclick="chk(this,false)"><input type="checkbox"><span>3×20 squats</span></div>
  <div class="task" onclick="chk(this,false)"><input type="checkbox"><span>40 min weights (compound lifts)</span></div>
  <div class="task" onclick="chk(this,false)"><input type="checkbox"><span>60 sec plank hold</span></div>
</div>
<div class="card">
  <div class="ct">💡 Rules for >100kg</div>
  <div class="rl">Compound lifts first: Squat, Bench, Deadlift</div>
  <div class="rl">Cardio: incline walk (NOT running — protects joints)</div>
  <div class="rl">Diet = 80% of results. Cut sugar and liquid calories first.</div>
  <div class="rl">Miss a day = not the end. Just continue next day.</div>
  <div class="rl">Sleep 7-8 hrs. Muscle built during sleep, not gym.</div>
</div>
</div>
<div class="card">
  <div class="ct">🏍️ Yamaha FZ-X Savings Tracker</div>
  <div style="display:flex;justify-content:space-between;font-size:11px;color:var(--text2);margin-bottom:5px"><span>₹0</span><span id="bike-pct">₹0 saved</span><span>₹1,50,000</span></div>
  <div class="pb"><div class="pf" id="bike-bar" style="width:0%;background:var(--green)"></div></div>
  <div style="margin-top:10px;display:flex;gap:7px">
    <input type="text" id="bike-in" placeholder="Enter amount saved (₹)" style="flex:1;margin:0">
    <button class="btn btn-g" onclick="updateBike()">Update</button>
  </div>
  <div style="margin-top:8px;font-size:11px;color:var(--text2)">"Reels buy the bike for the influencer. Cyber Security buys it for me."</div>
</div>
</div>

<!-- ======= BOOKS ======= -->
<div id="page-books" class="page">
<div class="pt">📚 Books + AI Tools</div>
<div class="ps">Communication · Money mindset · AI as private tutor · Dopamine reset</div>
<div class="card">
  <div class="ct">📖 How to Win Friends (2 pages/night)</div>
  <div class="ok" style="margin-bottom:10px">You already have this! 2 pages before sleep. Try ONE rule the next day at college.</div>
  <div class="rl"><span class="rn">Rule 1</span>"Don't criticize, condemn or complain." Try this for 1 full day.</div>
  <div class="rl"><span class="rn">Rule 2</span>"Give honest, sincere appreciation." Tell one classmate something genuine.</div>
  <div class="rl"><span class="rn">Rule 3</span>"Be genuinely interested in other people." Ask about THEIR life, not yours.</div>
  <div class="rl"><span class="rn">Rule 4</span>"Remember people's names." Use classmate names more in conversation.</div>
  <div class="rl"><span class="rn">Why</span>Better communication = better clients = FZ-X faster.</div>
</div>
<div class="card">
  <div class="ct">🤖 AI as Private Tutor</div>
  <div class="tip">Use this exact prompt for any topic you don't understand:</div>
  <div class="fbox">"Explain [AVL Tree Rotations] to me like I'm a beginner. Use a simple analogy. Then give me the 5 steps I need to write in my exam for full marks."</div>
  <div class="rl"><span class="rn">Viva Prep</span>"Ask me 5 viva questions a first-year SNIST student gets for Linked Lists."</div>
  <div class="rl"><span class="rn">Flashcards</span>Paste notes → "Make 10 flashcards from this chemistry content."</div>
  <div class="rl"><span class="rn">Hack</span>Before opening Instagram, ask AI one Cyber Security question. Reels must earn their spot.</div>
</div>
<div class="card">
  <div class="ct">🧠 Instagram Dopamine Reset</div>
  <div class="warn">You open reels not because you enjoy them — but because everything else feels harder. This is a dopamine loop, not laziness.</div>
  <div class="rl"><span class="rn">Hack 1</span>Move Instagram inside a folder (adds 2 extra taps → 30% less opening)</div>
  <div class="rl"><span class="rn">Hack 2</span>Before opening: solve 1 ODVC problem OR draw 1 BEE circuit. Then open.</div>
  <div class="rl"><span class="rn">Hack 3</span>5-Breath Reset when tense: breathe × 5 → 5 min walk outside. No phone.</div>
  <div class="rl"><span class="rn">Hack 4</span>10-min sit: before any task, sit with nothing. Brain resets. Tasks feel easier after.</div>
</div>
</div>

</div><!-- end main -->
</div><!-- end app -->

<script>
function pg(id,el){
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.ni').forEach(n=>n.classList.remove('active'));
  document.getElementById('page-'+id).classList.add('active');
  el.classList.add('active');
}
function tog(el){
  var b=el.nextElementSibling;
  b.classList.toggle('open');
}
function sw(prefix,id,btn){
  var all=document.querySelectorAll('[id^="'+prefix+'-"]');
  all.forEach(e=>{if(e.id.startsWith(prefix+'-'))e.style.display='none'});
  var target=document.getElementById(prefix+'-'+id);
  if(target)target.style.display='block';
  btn.parentElement.querySelectorAll('.tab').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
}
function chk(el,checkCongrats){
  var cb=el.querySelector('input');
  cb.checked=!cb.checked;
  el.classList.toggle('done',cb.checked);
  if(checkCongrats){
    var all=Array.from(document.querySelectorAll('#daily-tasks .task input')).every(c=>c.checked);
    var m=document.getElementById('congrats');
    if(m)m.classList.toggle('show',all);
  }
}
function updateBike(){
  var v=parseInt((document.getElementById('bike-in').value||'').replace(/[^0-9]/g,''));
  if(!v||v<0)return;
  var pct=Math.min((v/150000)*100,100);
  document.getElementById('bike-bar').style.width=pct.toFixed(1)+'%';
  document.getElementById('bike-pct').textContent='₹'+v.toLocaleString('en-IN')+' saved ('+pct.toFixed(1)+'%)';
  document.getElementById('bike-in').value='';
}
</script>
</body>
</html>
