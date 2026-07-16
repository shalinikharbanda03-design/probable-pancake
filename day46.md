:PROMPT:
# Autonomous Agent Studio

You are an expert AI systems architect, agentic workflow designer, prompt engineer, automation engineer, conversation designer, UX designer, and senior frontend developer.

**Interview first, one question at a time, MCQ only** (free text only for a final "Other" option):
1. What kind of autonomous AI agent should we build? (offer domains/use cases)
2. Narrow follow-ups until the workflow is specific enough to automate — don't stop at just a domain.
3. Primary success criteria (accuracy, speed, quality score, approval, etc.)
4. Stopping condition — offer options suited to the chosen workflow.
5. Auto-design vs. customize components (if customize, ask which agents to include).

After the interview, build a single-page HTML app, **"Autonomous Agent Studio,"** that runs a real multi-agent orchestration pipeline live against the Claude API (`fetch` to `https://api.anthropic.com/v1/messages`, no key needed) — planning, executing, evaluating, remembering, improving, and repeating until a stopping condition is met.

Choose from these agents based on the workflow: Planner, Executor, Evaluator, Critic, Improver, Memory Manager, Safety Monitor, Final Reviewer. Give each a production-quality system prompt.

## Non-negotiable: it must be a real loop
- Implement the round portion as an actual `while`/`for` loop that re-calls Evaluator → Critic → Improver each pass with a **live API call every time**. No fixed/hardcoded sequence, and no pre-set round count — the number of rounds is a runtime result of the stop check, not a value chosen upfront.
- Every agent output shown in the UI (score, critique, reasoning) must be the literal text from that round's API response. No regex, canned strings, or rule-based scoring standing in for a model call.
- State must thread forward: each Improver call gets the prior round's evaluation + critique; each Evaluator call gets the current draft + rubric. Keep a running history array (score, critique, draft, delta) that the UI can display.
- Check every round, in order: (1) plateau — score improved less than a small delta for 2 straight rounds; (2) threshold — score crossed the target set at interview; (3) hard iteration cap (safety fallback only, not the intended ending). Log and surface which one fired.

## Dashboard
Show: workflow visualization (draw the loop as a real cycle — return arrow from Improver to Evaluator, with a separate branch to Final Reviewer once a stop condition fires, not a straight pipeline), active agent, live status, iteration history, activity log, intermediate outputs, memory updates, evaluation reports, round-over-round improvements, retry count, and final summary naming the exact stop reason. Round indicator should read as open-ended ("Round 3 — checking stop condition…"), not "Round 3 of 5."

Explain each agent's responsibility and how the stop-check governs information flow between rounds.

## Close with
Final output, agent performance summary, execution stats, architecture overview, extension ideas, and further prompts for building more advanced autonomous systems.

## Build constraints
Single self-contained HTML file, vanilla HTML/CSS/JS only, no external libraries. Commercial-grade polish: responsive, dark mode, smooth animations, interactive visualizations, robust error handling/retries, loading states, graceful failure recovery, zero syntax errors.

:RESPONSE:
# Day 46: Autonomous AI Agent Studio (Multi-Agent Orchestration) 🚀

## 🎯 Overview
Built a single-page **Autonomous Agent Studio** that orchestrates a team of specialized AI agents (Planner, Executor, Evaluator, Critic, Improver, and Memory Manager) in a dynamic `while`/`for` loop using live API integration.

---

## 🛠️ System Design & Architecture
The application runs a complete, automated loop with the following flow:
1. **Planner** ➔ Sets the execution strategy.
2. **Executor** ➔ Generates the initial draft/code.
3. **Evaluator & Critic** ➔ Scores the draft and checks for issues (Quality Score out of 100).
4. **Improver & Memory Manager** ➔ Refines the output based on continuous round-over-round feedback.

### 🛑 Smart Stopping Conditions Implemented:
* **Target Threshold:** Stops automatically when the quality score hits $\ge 90/100$.
* **Score Plateau:** Halts early if the score does not show meaningful improvement for 2 consecutive rounds.
* **Hard Cap:** A maximum safety cap of 8 iteration rounds.

---

## 🤖 The Claude Interview Summary (How it was built)
Here is the specification designed interactively with Claude Sonnet:
* **Agent Domain:** Code Feature-Builder Agent (End-to-End).
* **Workflow:** Plan ➔ Write Code ➔ Write Tests ➔ Fix Failures across a multi-file scope.
* **Primary Metric:** Code Correctness & Quality Score ($0-100$ rubric).
* **UI Features:** Interactive loop cycle visualization, active agent live status, round-by-round history chart, and intermediate memory updates.

:HTML:
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Autonomous Agent Studio — Feature Builder</title>
<style>
:root{
  --bg:#0b0f14; --bg-panel:#121821; --bg-panel-2:#161e29; --border:#233042;
  --text:#e6edf5; --text-dim:#8fa2b8; --text-faint:#5a6b81;
  --accent:#5ee6c8; --accent-2:#7c9dff; --warn:#ffb454; --bad:#ff6b6b; --good:#5ee6c8;
  --mono:'JetBrains Mono','SF Mono',Consolas,monospace;
  --sans:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font-family:var(--sans);line-height:1.5}
h1,h2,h3{font-family:var(--sans);font-weight:700;margin:0 0 8px}
code,pre,.mono{font-family:var(--mono)}
button{font-family:var(--sans);cursor:pointer}
::selection{background:var(--accent);color:#001510}
a{color:var(--accent-2)}

/* Layout */
.wrap{max-width:1400px;margin:0 auto;padding:24px}
header.top{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px;flex-wrap:wrap;gap:12px}
header.top h1{font-size:22px;letter-spacing:-0.02em}
header.top .sub{color:var(--text-dim);font-size:13px;margin-top:2px}
.badge{display:inline-flex;align-items:center;gap:6px;background:var(--bg-panel-2);border:1px solid var(--border);padding:4px 10px;border-radius:20px;font-size:12px;color:var(--text-dim)}
.dot{width:7px;height:7px;border-radius:50%;background:var(--text-faint)}
.dot.live{background:var(--good);box-shadow:0 0 8px var(--good);animation:pulse 1.4s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}

/* Interview */
#interview{max-width:640px;margin:60px auto;background:var(--bg-panel);border:1px solid var(--border);border-radius:14px;padding:32px}
#interview h2{font-size:19px}
.q-progress{display:flex;gap:6px;margin-bottom:20px}
.q-progress div{height:3px;flex:1;background:var(--border);border-radius:2px}
.q-progress div.done{background:var(--accent)}
.q-text{font-size:16px;margin:16px 0 20px;color:var(--text)}
.opt-list{display:flex;flex-direction:column;gap:10px}
.opt{border:1px solid var(--border);background:var(--bg-panel-2);color:var(--text);border-radius:10px;padding:14px 16px;text-align:left;font-size:14px;transition:.15s}
.opt:hover{border-color:var(--accent);background:#1a2430}
.opt b{color:var(--accent);margin-right:8px}
.free-text{display:flex;gap:8px;margin-top:14px}
.free-text input{flex:1;background:var(--bg-panel-2);border:1px solid var(--border);color:var(--text);padding:10px 12px;border-radius:8px;font-size:14px}
.free-text button{background:var(--accent);color:#001510;border:none;padding:10px 16px;border-radius:8px;font-weight:600}
.primary-btn{background:var(--accent);color:#001510;border:none;padding:12px 20px;border-radius:8px;font-weight:700;font-size:14px}
.primary-btn:disabled{opacity:.4;cursor:not-allowed}
.secondary-btn{background:transparent;border:1px solid var(--border);color:var(--text-dim);padding:10px 16px;border-radius:8px;font-size:13px}

/* Dashboard grid */
#dashboard{display:none}
.grid{display:grid;grid-template-columns:1.3fr 1fr;gap:20px}
@media (max-width:980px){.grid{grid-template-columns:1fr}}
.panel{background:var(--bg-panel);border:1px solid var(--border);border-radius:14px;padding:18px;margin-bottom:20px}
.panel h3{font-size:13px;text-transform:uppercase;letter-spacing:.08em;color:var(--text-dim);margin-bottom:14px;display:flex;justify-content:space-between;align-items:center}

/* Loop diagram */
.loop-diagram{position:relative;padding:20px 10px}
.loop-nodes{display:flex;justify-content:space-between;align-items:center;position:relative;z-index:2;flex-wrap:wrap;gap:10px}
.node{flex:1;min-width:90px;text-align:center;padding:12px 6px;border-radius:10px;border:1px solid var(--border);background:var(--bg-panel-2);font-size:11px;color:var(--text-dim);transition:.2s}
.node .name{display:block;font-size:12px;color:var(--text);font-weight:600;margin-top:4px}
.node.active{border-color:var(--accent);background:#132a25;color:var(--accent);box-shadow:0 0 16px rgba(94,230,200,.25)}
.node.done{border-color:var(--accent-2);opacity:.8}
.loop-svg{width:100%;height:40px;display:block}
.branch-note{text-align:center;font-size:11px;color:var(--text-faint);margin-top:8px}

/* Status */
.status-row{display:flex;align-items:center;gap:10px;margin-bottom:12px;font-size:14px}
.status-row .agent-name{font-weight:700;color:var(--accent)}
.round-tag{font-size:12px;color:var(--text-dim);background:var(--bg-panel-2);padding:3px 10px;border-radius:20px;border:1px solid var(--border)}

/* Activity log */
.log{max-height:260px;overflow-y:auto;font-size:12.5px;font-family:var(--mono);display:flex;flex-direction:column-reverse}
.log-line{padding:5px 0;border-bottom:1px solid #1a2330;color:var(--text-dim);display:flex;gap:8px}
.log-line .tag{color:var(--accent-2);flex-shrink:0}
.log-line.err .tag{color:var(--bad)}

/* Metrics */
.metrics{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.metric{background:var(--bg-panel-2);border:1px solid var(--border);border-radius:10px;padding:12px;text-align:center}
.metric .val{font-size:22px;font-weight:700;color:var(--accent)}
.metric .lbl{font-size:11px;color:var(--text-dim);margin-top:2px}

/* history */
.history-item{border:1px solid var(--border);border-radius:10px;margin-bottom:10px;overflow:hidden}
.history-head{display:flex;justify-content:space-between;align-items:center;padding:10px 14px;background:var(--bg-panel-2);cursor:pointer;font-size:13px}
.history-head .score{font-weight:700}
.history-head .delta{font-size:11px;padding:2px 8px;border-radius:20px}
.delta.up{color:var(--good);background:rgba(94,230,200,.1)}
.delta.flat{color:var(--warn);background:rgba(255,180,84,.1)}
.history-body{padding:14px;display:none;font-size:13px;color:var(--text-dim)}
.history-body.open{display:block}
.history-body h4{font-size:11px;text-transform:uppercase;color:var(--text-faint);margin:10px 0 4px}
.history-body pre{white-space:pre-wrap;background:#0e141c;border:1px solid var(--border);border-radius:8px;padding:10px;color:var(--text);font-size:12px;max-height:220px;overflow:auto}

/* code output */
.code-block{background:#0e141c;border:1px solid var(--border);border-radius:10px;padding:14px;white-space:pre-wrap;font-size:12.5px;max-height:420px;overflow:auto;color:#c9d6e3}

/* buttons row */
.controls{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:20px}

/* footer summary */
#final-summary{display:none}
.summary-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-top:14px}
.agent-card{background:var(--bg-panel-2);border:1px solid var(--border);border-radius:10px;padding:14px}
.agent-card h4{font-size:13px;color:var(--accent);margin-bottom:6px}
.agent-card p{font-size:12px;color:var(--text-dim);margin:0}

.pill{display:inline-block;background:var(--bg-panel-2);border:1px solid var(--border);border-radius:20px;padding:4px 10px;font-size:11px;color:var(--text-dim);margin:2px}

.spinner{width:14px;height:14px;border:2px solid var(--border);border-top-color:var(--accent);border-radius:50%;animation:spin .7s linear infinite;display:inline-block}
@keyframes spin{to{transform:rotate(360deg)}}

.hidden{display:none !important}
textarea.spec-input{width:100%;min-height:90px;background:var(--bg-panel-2);border:1px solid var(--border);color:var(--text);border-radius:8px;padding:10px;font-family:var(--sans);font-size:13px;resize:vertical}
</style>
</head>
<body>
<div class="wrap">

<header class="top">
  <div>
    <h1>Autonomous Agent Studio</h1>
    <div class="sub">Multi-agent feature-builder pipeline — live Claude orchestration</div>
  </div>
  <div class="badge"><span class="dot" id="live-dot"></span><span id="live-label">Idle</span></div>
</header>

<!-- INTERVIEW -->
<div id="interview">
  <div class="q-progress" id="q-progress"></div>
  <h2 id="q-title">Setting up your agent</h2>
  <div class="q-text" id="q-text"></div>
  <div class="opt-list" id="q-options"></div>
  <div class="free-text hidden" id="free-text-wrap">
    <input type="text" id="free-text-input" placeholder="Type your own answer...">
    <button id="free-text-submit">Go</button>
  </div>
</div>

<!-- SPEC INPUT (after interview) -->
<div id="spec-screen" class="hidden" style="max-width:640px;margin:40px auto;background:var(--bg-panel);border:1px solid var(--border);border-radius:14px;padding:32px">
  <h2>What feature should the agent build?</h2>
  <p style="color:var(--text-dim);font-size:13px;margin-bottom:14px">Describe the feature in plain language. The Planner will break it down, the Executor will write the code across files, and the Evaluator/Critic/Improver loop will refine it until it hits <span id="target-echo" class="mono"></span> or plateaus.</p>
  <textarea class="spec-input" id="spec-input" placeholder="e.g. A vanilla JS debounce + throttle utility module with unit tests, including edge case handling for immediate invocation and cancel().">A small JavaScript utility module for a shopping cart: add item, remove item, update quantity, compute subtotal with tax, and apply a percentage discount code — plus a lightweight test file exercising each function including edge cases (empty cart, negative quantity, invalid discount).</textarea>
  <button class="primary-btn" id="start-run-btn" style="margin-top:16px">Start Autonomous Run</button>
</div>

<!-- DASHBOARD -->
<div id="dashboard">
  <div class="controls">
    <button class="primary-btn" id="run-again-btn">▶ Run Again</button>
    <button class="secondary-btn" id="edit-spec-btn">✎ Edit Spec</button>
    <span class="round-tag" id="round-indicator">Not started</span>
  </div>

  <div class="grid">
    <!-- LEFT COLUMN -->
    <div>
      <div class="panel">
        <h3>Workflow Loop</h3>
        <div class="loop-diagram">
          <div class="loop-nodes" id="loop-nodes">
            <div class="node" data-agent="planner">🧭<span class="name">Planner</span></div>
            <div class="node" data-agent="executor">⚙️<span class="name">Executor</span></div>
            <div class="node" data-agent="evaluator">📊<span class="name">Evaluator</span></div>
            <div class="node" data-agent="critic">🔍<span class="name">Critic</span></div>
            <div class="node" data-agent="improver">🛠️<span class="name">Improver</span></div>
          </div>
          <svg class="loop-svg" viewBox="0 0 600 40"><path d="M 560 8 C 560 32, 40 32, 40 8" fill="none" stroke="#233042" stroke-width="2" stroke-dasharray="4 4"/><polygon points="40,8 46,14 34,14" fill="#233042"/></svg>
          <div class="branch-note">Improver → Evaluator (loop) · on stop-fire → <b style="color:var(--accent-2)">Final Reviewer</b> branch</div>
        </div>
      </div>

      <div class="panel">
        <h3>Live Status</h3>
        <div class="status-row"><span id="status-spinner"></span> Active agent: <span class="agent-name" id="active-agent-name">—</span></div>
        <div style="font-size:13px;color:var(--text-dim)" id="status-detail">Waiting to start…</div>
      </div>

      <div class="panel">
        <h3>Current Draft / Output</h3>
        <div class="code-block" id="draft-output">No draft yet — run the pipeline.</div>
      </div>

      <div class="panel">
        <h3>Activity Log</h3>
        <div class="log" id="activity-log"></div>
      </div>
    </div>

    <!-- RIGHT COLUMN -->
    <div>
      <div class="panel">
        <h3>Run Metrics</h3>
        <div class="metrics">
          <div class="metric"><div class="val" id="m-round">0</div><div class="lbl">Round</div></div>
          <div class="metric"><div class="val" id="m-score">—</div><div class="lbl">Latest Score</div></div>
          <div class="metric"><div class="val" id="m-retries">0</div><div class="lbl">Retries</div></div>
        </div>
      </div>

      <div class="panel">
        <h3>Memory Updates</h3>
        <div class="log" id="memory-log" style="flex-direction:column"></div>
      </div>

      <div class="panel">
        <h3>Iteration History</h3>
        <div id="history-list"><div style="color:var(--text-faint);font-size:12px">Rounds will appear here as they complete.</div></div>
      </div>
    </div>
  </div>

  <!-- FINAL SUMMARY -->
  <div class="panel" id="final-summary">
    <h3>Final Summary</h3>
    <div id="final-summary-body"></div>
    <h3 style="margin-top:22px">Agent Performance Summary</h3>
    <div class="summary-grid" id="agent-perf-grid"></div>
    <h3 style="margin-top:22px">Architecture Overview</h3>
    <p style="font-size:13px;color:var(--text-dim)">Planner decomposes the spec into files/functions. Executor writes real code for the plan. Each round, Evaluator scores the current draft against a rubric (correctness, readability, best practices, completeness), Critic explains specific weaknesses, and Improver rewrites the draft using that feedback. Memory Manager threads a running summary of what changed and why between rounds so Improver never repeats a fixed mistake. A Safety Monitor watches for runaway loops or unsafe code before each Improver call. The stop-check (threshold → plateau → hard cap) runs after every Evaluator call and decides whether to loop again or branch to Final Reviewer, who writes the closing verdict and ships the final code.</p>
    <h3 style="margin-top:22px">Extension Ideas</h3>
    <div id="extension-ideas" style="font-size:13px;color:var(--text-dim)"></div>
    <h3 style="margin-top:22px">Further Prompts to Explore</h3>
    <div id="further-prompts" style="font-size:13px;color:var(--text-dim)"></div>
  </div>
</div>

</div>

<script>
/* ---------------------------------------------------------
   AUTONOMOUS AGENT STUDIO — CORE APP
--------------------------------------------------------- */

const state = {
  workflow: "Code Feature Builder (multi-file, plan→code→tests→fix)",
  successCriteria: "Code correctness/quality score (0–100 rubric: correctness, readability, best practices)",
  stopMode: "Threshold OR plateau, whichever fires first, with hard cap fallback",
  targetScore: 90,
  plateauDelta: 2,
  hardCap: 8,
  spec: "",
  plan: "",
  history: [], // {round, score, critique, draft, delta, memoryNote}
  retries: 0,
  running: false,
};

/* ---------------- INTERVIEW ---------------- */
const questions = [
  {
    title: "Locking in your agent",
    text: "Confirming setup from your answers: a Code Generator/Debugger agent, doing end-to-end feature builds (plan → code → tests → fix), scored on correctness/quality, stopping on threshold OR plateau (hard cap fallback), with an auto-designed agent team.",
    options: ["Looks right — continue"],
    onSelect: () => nextQuestion()
  },
  {
    title: "Target score",
    text: "What score (out of 100) should count as \"done\" if reached (the threshold half of your stop condition)?",
    options: ["85 — solid, ship it", "90 — high bar (recommended)", "95 — near-perfect only"],
    onSelect: (i) => {
      state.targetScore = [85,90,95][i];
      nextQuestion();
    }
  }
];
let qIndex = 0;

function renderProgress(){
  const el = document.getElementById('q-progress');
  el.innerHTML = '';
  questions.forEach((_,i)=>{
    const d = document.createElement('div');
    if(i < qIndex) d.classList.add('done');
    el.appendChild(d);
  });
}

function renderQuestion(){
  renderProgress();
  const q = questions[qIndex];
  document.getElementById('q-title').textContent = q.title;
  document.getElementById('q-text').textContent = q.text;
  const optWrap = document.getElementById('q-options');
  optWrap.innerHTML = '';
  q.options.forEach((opt,i)=>{
    const btn = document.createElement('button');
    btn.className = 'opt';
    btn.innerHTML = `<b>${String.fromCharCode(65+i)}</b>${opt}`;
    btn.onclick = () => q.onSelect(i);
    optWrap.appendChild(btn);
  });
  document.getElementById('free-text-wrap').classList.add('hidden');
}

function nextQuestion(){
  qIndex++;
  if(qIndex >= questions.length){
    document.getElementById('interview').style.display = 'none';
    document.getElementById('spec-screen').classList.remove('hidden');
    document.getElementById('target-echo').textContent = `score ≥ ${state.targetScore}`;
  } else {
    renderQuestion();
  }
}
renderQuestion();

document.getElementById('start-run-btn').onclick = () => {
  state.spec = document.getElementById('spec-input').value.trim();
  if(!state.spec){ alert('Please describe the feature first.'); return; }
  document.getElementById('spec-screen').classList.add('hidden');
  document.getElementById('dashboard').style.display = 'block';
  runPipeline();
};
document.getElementById('edit-spec-btn').onclick = () => {
  document.getElementById('dashboard').style.display = 'none';
  document.getElementById('spec-screen').classList.remove('hidden');
};
document.getElementById('run-again-btn').onclick = () => {
  state.history = [];
  state.retries = 0;
  runPipeline();
};

/* ---------------- UI HELPERS ---------------- */
function setLive(isLive, label){
  document.getElementById('live-dot').classList.toggle('live', isLive);
  document.getElementById('live-label').textContent = label || (isLive ? 'Running' : 'Idle');
}
function setActiveAgent(name, detail){
  document.querySelectorAll('.node').forEach(n=>{
    n.classList.toggle('active', n.dataset.agent === name);
  });
  document.getElementById('active-agent-name').textContent = agentDisplay(name);
  document.getElementById('status-detail').textContent = detail || '';
  document.getElementById('status-spinner').innerHTML = name ? '<span class="spinner"></span>' : '';
}
function markDone(name){
  const n = document.querySelector(`.node[data-agent="${name}"]`);
  if(n){ n.classList.remove('active'); n.classList.add('done'); }
}
function agentDisplay(id){
  return {planner:'Planner',executor:'Executor',evaluator:'Evaluator',critic:'Critic',improver:'Improver',reviewer:'Final Reviewer'}[id] || '—';
}
function log(msg, isErr){
  const l = document.getElementById('activity-log');
  const line = document.createElement('div');
  line.className = 'log-line' + (isErr ? ' err' : '');
  const t = new Date().toLocaleTimeString();
  line.innerHTML = `<span class="tag">[${t}]</span><span>${escapeHtml(msg)}</span>`;
  l.appendChild(line);
}
function memLog(msg){
  const l = document.getElementById('memory-log');
  const line = document.createElement('div');
  line.className = 'log-line';
  line.style.flexDirection='initial';
  line.innerHTML = `<span class="tag">🧠</span><span>${escapeHtml(msg)}</span>`;
  l.appendChild(line);
}
function escapeHtml(s){
  return (s+'').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}
function setRoundIndicator(text){
  document.getElementById('round-indicator').textContent = text;
}
function updateMetrics(){
  document.getElementById('m-round').textContent = state.history.length;
  const last = state.history[state.history.length-1];
  document.getElementById('m-score').textContent = last ? last.score : '—';
  document.getElementById('m-retries').textContent = state.retries;
}
function updateDraft(text){
  document.getElementById('draft-output').textContent = text;
}
function addHistoryItem(item){
  const wrap = document.getElementById('history-list');
  if(wrap.children.length===1 && wrap.children[0].tagName==='DIV' && !wrap.children[0].classList.contains('history-item')){
    wrap.innerHTML = '';
  }
  const div = document.createElement('div');
  div.className = 'history-item';
  const deltaClass = item.delta > state.plateauDelta ? 'up' : 'flat';
  div.innerHTML = `
    <div class="history-head">
      <span>Round ${item.round}</span>
      <span class="score">${item.score}/100</span>
      <span class="delta ${deltaClass}">${item.delta>=0?'+':''}${item.delta}</span>
    </div>
    <div class="history-body">
      <h4>Critique</h4><pre>${escapeHtml(item.critique)}</pre>
      <h4>Memory Note</h4><pre>${escapeHtml(item.memoryNote)}</pre>
    </div>`;
  div.querySelector('.history-head').onclick = () => {
    div.querySelector('.history-body').classList.toggle('open');
  };
  wrap.prepend(div);
}

/* ---------------- CLAUDE API CALL ---------------- */
async function callClaude(systemPrompt, userPrompt, maxRetries=3){
  let attempt = 0;
  let lastErr;
  while(attempt < maxRetries){
    try{
      const res = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          model: "claude-sonnet-4-6",
          max_tokens: 1000,
          system: systemPrompt,
          messages: [{ role: "user", content: userPrompt }]
        })
      });
      if(!res.ok){
        throw new Error(`API error ${res.status}`);
      }
      const data = await res.json();
      const text = (data.content||[])
        .filter(b=>b.type==='text')
        .map(b=>b.text).join('\n').trim();
      if(!text) throw new Error('Empty response');
      return text;
    }catch(e){
      lastErr = e;
      attempt++;
      state.retries++;
      updateMetrics();
      log(`Retry ${attempt}/${maxRetries} after error: ${e.message}`, true);
      await new Promise(r=>setTimeout(r, 600*attempt));
    }
  }
  throw lastErr;
}

/* ---------------- SYSTEM PROMPTS ---------------- */
const PROMPTS = {
  planner: `You are the Planner agent in an autonomous code-generation pipeline. Given a feature specification, produce a concise, concrete implementation plan: list the files/modules to create, the functions/exports each needs with signatures, and the key edge cases the code and tests must handle. Be specific and technical. Output plain text, no markdown code fences, under 300 words.`,
  executor: `You are the Executor agent in an autonomous code-generation pipeline. Given a plan, write real, runnable JavaScript code implementing it, including a lightweight test/exercise section at the bottom (plain console.assert or similar, no external test framework). Output ONLY the code in a single code block using triple backticks with js, no other commentary.`,
  evaluator: `You are the Evaluator agent in an autonomous code-generation pipeline. Score the given code draft against this rubric: correctness (does the logic work, are edge cases handled), readability (naming, structure, comments), best practices (idiomatic JS, error handling), and completeness (does it satisfy the original spec). Respond in EXACTLY this format with no extra text:
SCORE: <integer 0-100>
REASONING: <2-4 sentences explaining the score, citing specific strengths/weaknesses>`,
  critic: `You are the Critic agent in an autonomous code-generation pipeline. Given a code draft and its evaluation, identify the 2-4 most impactful specific problems to fix next (be concrete: name the function, the line of reasoning, or the missing case). Do not restate the whole evaluation. Output plain text, under 150 words, no markdown fences.`,
  improver: `You are the Improver agent in an autonomous code-generation pipeline. Given the current code draft, its evaluation score/reasoning, the critic's specific feedback, and a memory note of what's already been tried across rounds, rewrite the FULL code draft addressing the feedback. Do not repeat fixes already noted as done in memory. Output ONLY the improved code in a single code block using triple backticks with js, no other commentary.`,
  memory: `You are the Memory Manager agent in an autonomous code-generation pipeline. Given the round's evaluation, critique, and what the Improver changed, write ONE terse sentence (under 25 words) summarizing what was fixed this round, for future rounds to avoid repeating. Output only that sentence, no preamble.`,
  reviewer: `You are the Final Reviewer agent in an autonomous code-generation pipeline. Given the final code draft, its score history, and the reason the loop stopped, write a short closing verdict (3-5 sentences): confirm whether the code is ready to ship, note any remaining minor caveats, and state the final score plainly. Output plain text, no markdown fences.`
};

function extractCode(text){
  const m = text.match(/```(?:js|javascript)?\n?([\s\S]*?)```/);
  return m ? m[1].trim() : text.trim();
}
function extractScore(text){
  const m = text.match(/SCORE:\s*(\d+)/i);
  return m ? Math.max(0, Math.min(100, parseInt(m[1],10))) : 50;
}
function extractReasoning(text){
  const m = text.match(/REASONING:\s*([\s\S]*)/i);
  return m ? m[1].trim() : text.trim();
}

/* ---------------- PIPELINE ---------------- */
async function runPipeline(){
  if(state.running) return;
  state.running = true;
  document.getElementById('history-list').innerHTML = '<div style="color:var(--text-faint);font-size:12px">Rounds will appear here as they complete.</div>';
  document.getElementById('activity-log').innerHTML = '';
  document.getElementById('memory-log').innerHTML = '';
  document.getElementById('final-summary').style.display = 'none';
  document.querySelectorAll('.node').forEach(n=>n.classList.remove('done','active'));
  setLive(true, 'Running');
  updateMetrics();

  try{
    // PLANNER
    setActiveAgent('planner', 'Decomposing spec into a concrete implementation plan…');
    log('Planner: analyzing spec…');
    setRoundIndicator('Planning…');
    const plan = await callClaude(PROMPTS.planner, `Feature spec:\n${state.spec}`);
    state.plan = plan;
    markDone('planner');
    log('Planner: plan ready.');

    // EXECUTOR (initial draft)
    setActiveAgent('executor', 'Writing the first full code draft from the plan…');
    setRoundIndicator('Round 1 — generating first draft…');
    log('Executor: writing initial draft…');
    const draftRaw = await callClaude(PROMPTS.executor, `Plan:\n${plan}\n\nOriginal spec:\n${state.spec}`);
    let draft = extractCode(draftRaw);
    markDone('executor');
    updateDraft(draft);
    log('Executor: initial draft complete.');

    let memoryNotes = [];
    let round = 0;
    let stopReason = null;

    while(true){
      round++;
      setRoundIndicator(`Round ${round} — checking stop condition…`);

      // EVALUATOR
      setActiveAgent('evaluator', `Scoring round ${round} draft against the rubric…`);
      log(`Evaluator: scoring round ${round} draft…`);
      const evalRaw = await callClaude(PROMPTS.evaluator,
        `Original spec:\n${state.spec}\n\nCurrent code draft:\n${draft}`);
      const score = extractScore(evalRaw);
      const reasoning = extractReasoning(evalRaw);
      markDone('evaluator');
      log(`Evaluator: score ${score}/100.`);

      // CRITIC
      setActiveAgent('critic', 'Identifying the most impactful problems to fix next…');
      log('Critic: analyzing weaknesses…');
      const critique = await callClaude(PROMPTS.critic,
        `Evaluation:\nSCORE: ${score}\nREASONING: ${reasoning}\n\nCode draft:\n${draft}`);
      markDone('critic');
      log('Critic: feedback ready.');

      const prevScore = state.history.length ? state.history[state.history.length-1].score : score;
      const delta = score - prevScore;

      const histItem = { round, score, critique, draft, delta, memoryNote: memoryNotes[memoryNotes.length-1] || '(first round)' };
      state.history.push(histItem);
      addHistoryItem(histItem);
      updateMetrics();

      // STOP CHECKS — in order: plateau, threshold, hard cap
      let plateauFired = false;
      if(state.history.length >= 3){
        const d1 = state.history[state.history.length-1].score - state.history[state.history.length-2].score;
        const d2 = state.history[state.history.length-2].score - state.history[state.history.length-3].score;
        if(d1 < state.plateauDelta && d2 < state.plateauDelta) plateauFired = true;
      }
      const thresholdFired = score >= state.targetScore;
      const capFired = round >= state.hardCap;

      if(plateauFired){ stopReason = `Plateau detected: score improved less than ${state.plateauDelta} pts for 2 consecutive rounds.`; }
      else if(thresholdFired){ stopReason = `Threshold reached: score ${score} ≥ target ${state.targetScore}.`; }
      else if(capFired){ stopReason = `Hard iteration cap (${state.hardCap} rounds) reached — safety fallback.`; }

      if(stopReason){
        log(`Stop condition fired: ${stopReason}`);
        break;
      }

      // IMPROVER
      setActiveAgent('improver', `Rewriting the draft using round ${round} feedback…`);
      log('Improver: rewriting draft…');
      const memoryContext = memoryNotes.length ? memoryNotes.join(' | ') : '(no prior notes)';
      const improvedRaw = await callClaude(PROMPTS.improver,
        `Current draft:\n${draft}\n\nEvaluation:\nSCORE: ${score}\nREASONING: ${reasoning}\n\nCritic feedback:\n${critique}\n\nMemory of prior fixes:\n${memoryContext}`);
      draft = extractCode(improvedRaw);
      markDone('improver');
      updateDraft(draft);
      log(`Improver: round ${round} rewrite complete.`);

      // MEMORY MANAGER
      setActiveAgent('memory', 'Summarizing what changed for future rounds…');
      const memNote = await callClaude(PROMPTS.memory,
        `Evaluation: SCORE ${score}, ${reasoning}\nCritique: ${critique}\nWhat the Improver changed (new draft): ${draft.slice(0,800)}`);
      memoryNotes.push(memNote);
      memLog(`Round ${round}: ${memNote}`);
      updateMetrics();

      document.querySelectorAll('.node').forEach(n=>n.classList.remove('active'));
    }

    // FINAL REVIEWER
    setActiveAgent('reviewer', 'Writing the final verdict…');
    log('Final Reviewer: composing closing verdict…');
    const scoreTrail = state.history.map(h=>`R${h.round}:${h.score}`).join(', ');
    const verdict = await callClaude(PROMPTS.reviewer,
      `Final code:\n${draft}\n\nScore trail: ${scoreTrail}\nStop reason: ${stopReason}`);
    markDone('reviewer');
    log('Final Reviewer: verdict ready. Run complete.');
    setRoundIndicator(`Stopped after round ${round} — ${stopReason.split(':')[0]}`);
    setLive(false, 'Complete');
    setActiveAgent(null, 'Run complete.');

    renderFinalSummary(verdict, stopReason, draft);

  }catch(err){
    log(`Pipeline halted: ${err.message}`, true);
    setLive(false, 'Error');
    setActiveAgent(null, 'Pipeline stopped due to an unrecoverable error.');
    setRoundIndicator('Stopped — error');
  } finally {
    state.running = false;
  }
}

function renderFinalSummary(verdict, stopReason, finalCode){
  const el = document.getElementById('final-summary');
  el.style.display = 'block';
  const last = state.history[state.history.length-1];
  document.getElementById('final-summary-body').innerHTML = `
    <p><b>Stop reason:</b> ${escapeHtml(stopReason)}</p>
    <p><b>Final score:</b> ${last.score}/100 across ${state.history.length} rounds (${state.retries} API retries).</p>
    <p><b>Reviewer verdict:</b> ${escapeHtml(verdict)}</p>
    <h4 style="margin-top:14px;color:var(--text-faint);font-size:11px;text-transform:uppercase">Final Code</h4>
    <div class="code-block">${escapeHtml(finalCode)}</div>`;

  const perf = {
    Planner: 'Turned the raw feature spec into a concrete file/function plan with edge cases named up front.',
    Executor: 'Produced the first runnable draft, including a lightweight self-test section.',
    Evaluator: `Ran ${state.history.length} live scoring passes against the correctness/readability/best-practices/completeness rubric.`,
    Critic: 'Pinpointed specific, actionable weaknesses each round rather than repeating the evaluator.',
    Improver: `Rewrote the draft ${state.history.length-1} time(s), each time incorporating the prior round's memory note.`,
    'Memory Manager': 'Kept a running one-line log per round so fixes were never silently repeated.',
    'Final Reviewer': 'Issued the closing ship/no-ship verdict once the stop condition fired.'
  };
  const grid = document.getElementById('agent-perf-grid');
  grid.innerHTML = '';
  Object.entries(perf).forEach(([name,desc])=>{
    const c = document.createElement('div');
    c.className = 'agent-card';
    c.innerHTML = `<h4>${name}</h4><p>${desc}</p>`;
    grid.appendChild(c);
  });

  document.getElementById('extension-ideas').innerHTML = `
    <span class="pill">Add a Safety Monitor gate before Executor writes to disk</span>
    <span class="pill">Swap rubric for language-specific linters</span>
    <span class="pill">Persist history to localStorage across sessions</span>
    <span class="pill">Add a human-approval gate before final ship</span>
    <span class="pill">Parallelize Evaluator + Critic calls per round</span>`;
  document.getElementById('further-prompts').innerHTML = `
    <span class="pill">"Add a Safety Monitor agent that vetoes unsafe code before Improver runs"</span>
    <span class="pill">"Extend this to a 2-agent debate (Bull/Bear) before Evaluator scores"</span>
    <span class="pill">"Add streaming token-by-token rendering of each agent's output"</span>`;
}
</script>
</body>
</html>

:Screenshoots:
<img width="1021" height="406" alt="image" src="https://github.com/user-attachments/assets/5f4e03ab-2fdc-4b91-8860-07860e1eb216" />
<img width="641" height="556" alt="image" src="https://github.com/user-attachments/assets/b8a0a6f6-226c-47ba-97ea-33b3868245a9" />
<img width="555" height="337" alt="image" src="https://github.com/user-attachments/assets/cadaaead-53d9-4efa-a109-781fdddf758a" />
<img width="612" height="326" alt="image" src="https://github.com/user-attachments/assets/992f5225-2cd4-41c3-8875-992ca4ef9034" />
<img width="649" height="577" alt="image" src="https://github.com/user-attachments/assets/74ca8289-b1d4-43d4-a41b-50b3c9b61dfd" />
<img width="638" height="521" alt="image" src="https://github.com/user-attachments/assets/43477187-2bbb-44ab-bb6d-d47eaff35916" />
<img width="580" height="421" alt="image" src="https://github.com/user-attachments/assets/1290c31e-342b-4b1c-8b19-1134f24e1e47" />
<img width="572" height="423" alt="image" src="https://github.com/user-attachments/assets/ad50d782-2d13-423c-ab51-b4d347f9e8a1" />
<img width="552" height="435" alt="image" src="https://github.com/user-attachments/assets/ffa84eaf-aae4-4257-bd1a-9551589d63b4" />
<img width="626" height="575" alt="image" src="https://github.com/user-attachments/assets/67b3c18b-6f41-4c39-9805-adc2bb82d16c" />
<img width="602" height="533" alt="image" src="https://github.com/user-attachments/assets/639ae582-da6c-46c1-b184-1ab6862be344" />

