:Prompt:
You are an expert educational game designer, UI/UX designer, organizational consultant and frontend developer.

Before generating anything, ask the user ONE question:

"What type of workplace would you like to explore?"

Options: Tech Company, Startup, Corporate Office, Café / Restaurant, Retail Business, Hospital / Healthcare, School / University, Manufacturing, Media / Creative Agency, Freelancer / Small Business, Other (one sentence).

Wait for the user's answer.

Then generate a beautiful single-file HTML application called: Task Compass

Subtitle:
Learn how work flows through real organizations.

IMPORTANT

Generate ONLY one self-contained HTML file.

Use only: HTML, CSS, Vanilla JavaScript.

Do NOT use: React, Tailwind, npm, Babel, external libraries or APIs.

Everything must work completely offline.

Internally verify there are no syntax or runtime errors before returning the code.

OBJECTIVE

The goal is NOT to test job titles.

The goal is to teach: ownership, delegation, collaboration, escalation and how work moves through organizations.

The experience should feel like a management simulation rather than a quiz.

GAMEPLAY

The application contains THREE stages.

Each stage becomes slightly more realistic.

Display progress throughout.

STAGE 1

Who Owns This? (do 3 questions of this only)

Display one realistic workplace task at a time.

Example:

"A customer reports that payments fail only on iPhones."

Present 6-8 role cards.

Examples for a tech company: Frontend Developer, Backend Developer, QA Engineer, Product Manager, UX Designer, Customer Support, Engineering Manager.

The player drags ONE role into the highlighted ownership slot.

After submission reveal:

✓ Primary Owner

✓ Why they own it

✓ Which roles may assist.

Never simply say Correct or Wrong.

Always explain the reasoning.

Include 8-10 different task cards.

STAGE 2

Task Routing (do 3 questions of this only)

Now the player manages incoming work.

A task appears.

The player must build the workflow.

Example:

Customer Support ↓ QA ↓ Backend ↓ Product Manager ↓ Customer

The player drags role cards into the correct order.

Some tasks may only need three steps.

Others may need five.

After submission animate the task moving through the organization.

Explain why this order is commonly used.

STAGE 3

Collaboration Challenge (do 3 questions of this only)

Present larger situations.

Examples:

Customer satisfaction suddenly drops

Sales increase dramatically

Negative reviews appear online

A major feature is delayed.

Instead of choosing one owner, allow players to assign up to FOUR departments or roles.

The player should think about collaboration.

After submission display:

Primary Owner

Supporting Teams

Reasoning

Possible Communication Flow.

Emphasize that complex problems usually require multiple people.

SCORING

Instead of points, award understanding.

Categories:

Ownership

Delegation

Collaboration

Workflow Thinking.

Display a radar or bar chart at the end using only HTML, CSS and JavaScript.

FINAL REFLECTION

Instead of a score, generate:

What you understood well

Where you tended to over-assign responsibility

Where you underestimated collaboration

One insight about how organizations actually work.

Example:

"Many real workplace problems are solved by teams rather than individuals."

Avoid absolute language.

GAME FEEL

The experience should feel satisfying.

Use:

drag-and-drop

animated cards

smooth transitions

satisfying snap animations

subtle sounds using CSS/JS only if possible (optional)

hover effects

progress indicator

completion celebration.

Avoid making it feel like an exam.

It should feel like a modern strategy game.

DESIGN

Premium modern UI.

Dark mode.

Glassmorphism.

Rounded cards.

Animated gradients.

Distinct colors for each department.

Role cards should feel collectible.

Task cards should resemble work tickets.

Use icons or emojis where appropriate.

TECHNICAL REQUIREMENTS

Store all scenarios in JavaScript objects.

Reuse components wherever possible.

Optimize code size for Claude Free.

If necessary, reduce the number of scenarios instead of reducing functionality.

Everything must remain offline.

Before returning:

Verify drag-and-drop works.

Verify scoring works.

Verify animations work.

Verify no syntax errors.

Verify responsive layout.

Return ONLY the complete HTML inside one code block.

:Response:
Let me verify it quickly for basic issues.Found real bugs — the escaped apostrophes inside template literals. Let me fix both occurrences.Syntax is clean now.Task Compass is ready — themed around a 100%-environmentally-friendly business, with roles like Sustainability Lead, Supply Chain Manager, R&D, Facilities & Logistics, etc. It runs fully offline as a single HTML file: drag-and-drop (or tap-to-place) ownership calls, task routing chains with animated playback, a 4-role collaboration picker for bigger crises, and a canvas-drawn radar chart plus written reflection at the end.
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Task Compass — Green Business Edition</title>
<style>
:root{
  --bg-deep:#0e1f16;
  --bg-panel:#152a1d;
  --bg-panel-2:#1b3324;
  --moss:#4f7942;
  --leaf:#8fbc6a;
  --clay:#c98a4b;
  --sky:#6ec6b8;
  --cream:#f2ede1;
  --cream-dim:#cdc7b8;
  --danger:#d9714e;
  --glass:rgba(242,237,225,0.06);
  --glass-border:rgba(242,237,225,0.14);
  --radius:18px;
}
*{box-sizing:border-box;}
html,body{margin:0;padding:0;}
body{
  min-height:100vh;
  background:
    radial-gradient(circle at 15% 10%, rgba(143,188,106,0.15), transparent 45%),
    radial-gradient(circle at 85% 85%, rgba(110,198,184,0.12), transparent 50%),
    linear-gradient(160deg, var(--bg-deep), #0a1710 70%);
  color:var(--cream);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  overflow-x:hidden;
}
.display{
  font-family:Georgia,"Iowan Old Style","Palatino Linotype",serif;
  letter-spacing:0.01em;
}
#app{
  max-width:980px;
  margin:0 auto;
  padding:28px 20px 80px;
}
/* ---------- Header / vine progress ---------- */
header.top{
  text-align:center;
  margin-bottom:22px;
}
header.top h1{
  font-size:2.4rem;
  margin:0 0 6px;
  background:linear-gradient(100deg,var(--leaf),var(--sky) 60%,var(--clay));
  -webkit-background-clip:text;
  background-clip:text;
  color:transparent;
}
header.top p{
  margin:0;
  color:var(--cream-dim);
  font-size:1rem;
}
.vine-wrap{
  margin:22px auto 0;
  max-width:640px;
  position:relative;
}
.vine-track{
  height:10px;
  border-radius:99px;
  background:var(--glass);
  border:1px solid var(--glass-border);
  overflow:hidden;
  position:relative;
}
.vine-fill{
  height:100%;
  width:0%;
  border-radius:99px;
  background:linear-gradient(90deg,var(--moss),var(--leaf));
  transition:width 0.7s cubic-bezier(.4,1.4,.4,1);
  position:relative;
}
.vine-fill::after{
  content:"🌱";
  position:absolute;
  right:-10px;
  top:50%;
  transform:translateY(-50%);
  font-size:1.1rem;
}
.stage-labels{
  display:flex;
  justify-content:space-between;
  margin-top:8px;
  font-size:0.78rem;
  color:var(--cream-dim);
  text-transform:uppercase;
  letter-spacing:0.06em;
}
.stage-labels span.active{color:var(--leaf); font-weight:600;}

/* ---------- Panels ---------- */
.panel{
  background:var(--glass);
  border:1px solid var(--glass-border);
  backdrop-filter:blur(14px);
  border-radius:var(--radius);
  padding:26px;
  margin-top:22px;
  animation:fadeUp 0.5s ease both;
}
@keyframes fadeUp{
  from{opacity:0; transform:translateY(14px);}
  to{opacity:1; transform:translateY(0);}
}
.q-select label{display:block;}
.choice-grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(190px,1fr));
  gap:12px;
  margin-top:18px;
}
.choice-card{
  background:var(--bg-panel);
  border:1px solid var(--glass-border);
  border-radius:14px;
  padding:16px;
  cursor:pointer;
  transition:transform 0.2s, border-color 0.2s, background 0.2s;
  text-align:left;
}
.choice-card:hover{
  transform:translateY(-3px);
  border-color:var(--leaf);
  background:var(--bg-panel-2);
}
.choice-card .emoji{font-size:1.4rem;}
.choice-card .title{font-weight:600; margin-top:6px;}

button.primary{
  background:linear-gradient(100deg,var(--moss),var(--leaf));
  color:#0e1f16;
  border:none;
  font-weight:700;
  padding:12px 22px;
  border-radius:99px;
  cursor:pointer;
  font-size:0.95rem;
  transition:transform 0.15s, box-shadow 0.15s;
  box-shadow:0 6px 18px rgba(143,188,106,0.25);
}
button.primary:hover{transform:translateY(-2px); box-shadow:0 10px 22px rgba(143,188,106,0.35);}
button.primary:disabled{opacity:0.4; cursor:not-allowed; transform:none; box-shadow:none;}
button.ghost{
  background:transparent;
  border:1px solid var(--glass-border);
  color:var(--cream);
  padding:10px 18px;
  border-radius:99px;
  cursor:pointer;
  font-size:0.9rem;
}
button.ghost:hover{border-color:var(--leaf); color:var(--leaf);}

/* ---------- Ticket / task card ---------- */
.ticket{
  position:relative;
  background:linear-gradient(135deg,var(--bg-panel-2),var(--bg-panel));
  border:1px dashed rgba(242,237,225,0.25);
  border-radius:14px;
  padding:20px;
  margin-bottom:10px;
}
.ticket .tag{
  display:inline-block;
  font-size:0.7rem;
  text-transform:uppercase;
  letter-spacing:0.08em;
  background:rgba(143,188,106,0.15);
  color:var(--leaf);
  padding:4px 10px;
  border-radius:99px;
  margin-bottom:10px;
}
.ticket .body{font-size:1.08rem; line-height:1.5;}

/* ---------- Role cards (collectible) ---------- */
.role-pool{
  display:flex;
  flex-wrap:wrap;
  gap:10px;
  margin:18px 0;
}
.role-card{
  --rc:var(--leaf);
  background:linear-gradient(150deg, rgba(255,255,255,0.05), rgba(255,255,255,0));
  border:1.5px solid var(--rc);
  border-radius:12px;
  padding:10px 14px;
  cursor:grab;
  user-select:none;
  display:flex;
  align-items:center;
  gap:8px;
  font-size:0.92rem;
  transition:transform 0.15s, box-shadow 0.15s, opacity 0.2s;
  box-shadow:0 0 0 rgba(0,0,0,0);
}
.role-card:hover{transform:translateY(-3px) scale(1.02); box-shadow:0 8px 16px rgba(0,0,0,0.3);}
.role-card.selected{outline:2px solid var(--sky); outline-offset:2px;}
.role-card.dragging{opacity:0.35;}
.role-card.used{opacity:0.25; pointer-events:none;}
.role-card .emoji{font-size:1.15rem;}

/* ---------- Ownership slot ---------- */
.slot-zone{
  margin:18px 0;
  border:2px dashed rgba(242,237,225,0.28);
  border-radius:14px;
  padding:22px;
  text-align:center;
  color:var(--cream-dim);
  transition:border-color 0.2s, background 0.2s;
  min-height:64px;
  display:flex;
  align-items:center;
  justify-content:center;
}
.slot-zone.dragover{border-color:var(--leaf); background:rgba(143,188,106,0.08);}
.slot-zone.filled{border-style:solid; border-color:var(--leaf); color:var(--cream);}

/* ---------- Routing chain ---------- */
.chain-wrap{
  display:flex;
  align-items:center;
  gap:8px;
  flex-wrap:wrap;
  margin:18px 0;
}
.chain-node{
  background:var(--bg-panel);
  border:1px solid var(--glass-border);
  border-radius:12px;
  padding:10px 14px;
  font-size:0.85rem;
  min-width:60px;
  text-align:center;
}
.chain-node.fixed{background:rgba(110,198,184,0.12); border-color:var(--sky); color:var(--sky); font-weight:600;}
.chain-node.slot{
  border-style:dashed;
  color:var(--cream-dim);
  min-height:44px;
  display:flex;
  align-items:center;
  justify-content:center;
}
.chain-node.slot.filled{border-style:solid; border-color:var(--leaf); color:var(--cream);}
.chain-arrow{color:var(--cream-dim); font-size:1.1rem;}

/* ---------- Multi-select (stage 3) ---------- */
.role-card.picked{border-color:var(--clay); background:rgba(201,138,75,0.18);}
.pick-count{font-size:0.8rem; color:var(--cream-dim); margin-top:6px;}

/* ---------- Reveal panel ---------- */
.reveal{
  margin-top:20px;
  padding:18px;
  border-radius:14px;
  background:rgba(143,188,106,0.08);
  border:1px solid rgba(143,188,106,0.3);
  animation:fadeUp 0.4s ease both;
}
.reveal h3{margin:0 0 10px; color:var(--leaf); font-size:1.05rem;}
.reveal p{margin:6px 0; line-height:1.55; font-size:0.95rem;}
.reveal .label{color:var(--sky); font-weight:600;}

.actions-row{display:flex; justify-content:flex-end; gap:10px; margin-top:18px;}

/* ---------- Animated route playback ---------- */
.route-anim{
  display:flex;
  align-items:center;
  gap:6px;
  margin:16px 0;
  flex-wrap:wrap;
}
.route-anim .node{
  padding:8px 12px;
  border-radius:10px;
  background:var(--bg-panel);
  border:1px solid var(--glass-border);
  font-size:0.85rem;
  opacity:0.25;
  transition:opacity 0.4s, transform 0.4s, background 0.4s;
}
.route-anim .node.lit{opacity:1; background:rgba(143,188,106,0.18); border-color:var(--leaf); transform:scale(1.05);}

/* ---------- Radar chart & summary ---------- */
.summary-grid{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:20px;
  align-items:center;
}
@media (max-width:640px){.summary-grid{grid-template-columns:1fr;}}
.reflection-list{list-style:none; padding:0; margin:0;}
.reflection-list li{
  padding:12px 14px;
  margin-bottom:10px;
  border-radius:12px;
  background:var(--glass);
  border:1px solid var(--glass-border);
  font-size:0.92rem;
  line-height:1.5;
}
.reflection-list li b{color:var(--leaf);}

/* ---------- Celebration ---------- */
.confetti{
  position:fixed;
  top:-20px;
  font-size:1.4rem;
  pointer-events:none;
  animation:fall linear forwards;
  z-index:999;
}
@keyframes fall{
  to{transform:translateY(105vh) rotate(360deg); opacity:0.2;}
}

footer.credit{
  text-align:center;
  margin-top:36px;
  font-size:0.78rem;
  color:var(--cream-dim);
  opacity:0.6;
}

.small-note{font-size:0.82rem; color:var(--cream-dim); margin-top:4px;}
</style>
</head>
<body>
<div id="app"></div>

<script>
(function(){

/* ============================= DATA ============================= */

const ROLES = [
  {id:'sustain', name:'Sustainability Lead', emoji:'🌱', color:'#8fbc6a'},
  {id:'supply', name:'Supply Chain Manager', emoji:'🚚', color:'#c98a4b'},
  {id:'ops', name:'Operations Manager', emoji:'⚙️', color:'#6ec6b8'},
  {id:'rd', name:'R&D / Product Designer', emoji:'🔬', color:'#8fbc6a'},
  {id:'marketing', name:'Marketing & Communications', emoji:'📣', color:'#c98a4b'},
  {id:'support', name:'Customer Support', emoji:'💬', color:'#6ec6b8'},
  {id:'finance', name:'Finance & Compliance', emoji:'💰', color:'#8fbc6a'},
  {id:'facilities', name:'Facilities & Logistics', emoji:'🏭', color:'#c98a4b'}
];
function roleById(id){ return ROLES.find(r=>r.id===id); }

const STAGE1_POOL = [
  {task:"A supplier switched to non-recyclable packaging material without telling anyone.",
   owner:'supply', why:"The Supply Chain Manager owns supplier relationships and contract terms, including material specifications.",
   assist:['sustain','ops']},
  {task:"Customers keep messaging that they don't understand how to recycle the product packaging.",
   owner:'marketing', why:"Marketing & Communications owns the customer-facing labeling and instructions that reduce confusion.",
   assist:['sustain','support']},
  {task:"The company's carbon offset certificate is about to expire.",
   owner:'sustain', why:"The Sustainability Lead owns environmental certifications and compliance renewals.",
   assist:['finance','ops']},
  {task:"A newly discovered biodegradable material could replace a current plastic component.",
   owner:'rd', why:"R&D / Product Designer owns material selection and how the product is engineered.",
   assist:['sustain','supply']},
  {task:"The main facility's energy bill spiked because of aging, inefficient machinery.",
   owner:'facilities', why:"Facilities & Logistics owns the physical infrastructure and its energy consumption.",
   assist:['ops','finance']},
  {task:"A journalist is requesting the company's official emissions data for a story.",
   owner:'marketing', why:"Marketing & Communications owns external, public-facing statements and press relations.",
   assist:['sustain','finance']},
  {task:"Delivery trucks are frequently running half-empty on regional routes.",
   owner:'ops', why:"Operations Manager owns day-to-day logistics efficiency and route planning.",
   assist:['supply','facilities']},
  {task:"A customer asks whether the company's 'eco-friendly' claim is independently verified.",
   owner:'sustain', why:"The Sustainability Lead owns the accuracy and verification of environmental claims.",
   assist:['support','marketing']},
  {task:"Investors are requesting this year's sustainability impact report.",
   owner:'finance', why:"Finance & Compliance owns formal financial and regulatory reporting, including audited impact figures.",
   assist:['sustain','marketing']},
  {task:"A batch of solar panel components arrived damaged from a supplier.",
   owner:'supply', why:"Supply Chain Manager owns supplier quality issues and resolving shipment problems.",
   assist:['ops','facilities']}
];

const STAGE2_POOL = [
  {task:"A customer complains their 'compostable' packaging never broke down in their home compost bin.",
   steps:['support','sustain','rd','marketing'],
   reasoning:"Support logs the complaint, Sustainability checks the certification standard being used, R&D reviews the material's real-world specs, and Marketing updates the customer-facing usage instructions."},
  {task:"A large retail chain wants to place a bulk order but requires proof of carbon-neutral shipping.",
   steps:['support','finance','supply','marketing'],
   reasoning:"Support routes the enterprise request, Finance & Compliance confirms certifications and contract terms, Supply Chain arranges a low-carbon shipping option, and Marketing communicates the finalized offer."},
  {task:"A supplier defect causes a delay in an upcoming order shipment.",
   steps:['supply','ops','support'],
   reasoning:"Supply Chain identifies the source of the delay, Operations adjusts the production and delivery schedule, and Support communicates the updated timeline to the customer."},
  {task:"A viral social post claims the company's supply chain uses unethical labor practices.",
   steps:['support','marketing','sustain','supply','finance'],
   reasoning:"Support flags the incoming volume, Marketing manages the public response, Sustainability and Supply Chain investigate the actual supplier practices, and Finance & Compliance documents findings for accountability."},
  {task:"A regional office reports its recycling bins are being contaminated with non-recyclable waste.",
   steps:['facilities','ops','sustain'],
   reasoning:"Facilities identifies the on-site issue, Operations coordinates a fix with the office routine, and the Sustainability Lead confirms the process now meets company standards."}
];

const STAGE3_POOL = [
  {task:"Customer satisfaction with the 'eco' product line suddenly drops.",
   primary:'sustain', support:['support','rd','marketing'],
   reasoning:"Support surfaces the complaint patterns, R&D investigates whether a material or manufacturing change caused the issue, Sustainability confirms whether standards are still being met, and Marketing adjusts messaging if claims need clarifying.",
   flow:"Customer Support logs volume and patterns → Sustainability & R&D investigate the root cause together → Marketing communicates any needed correction."},
  {task:"Sales for the reusable product line increase dramatically after a viral video.",
   primary:'ops', support:['supply','facilities','finance'],
   reasoning:"Operations manages the sudden scale-up, Supply Chain secures more raw materials without compromising sourcing standards, Facilities & Logistics scales fulfillment capacity, and Finance tracks the financial impact.",
   flow:"Operations sets a scale-up plan → Supply Chain & Facilities execute in parallel → Finance monitors budget and cash flow."},
  {task:"Negative reviews claim the company's packaging isn't actually recyclable in most areas.",
   primary:'sustain', support:['rd','marketing','support'],
   reasoning:"The Sustainability Lead verifies the claim against real recycling infrastructure, R&D checks if the material needs to change, Marketing corrects any overstated claims, and Support handles the inbound questions.",
   flow:"Sustainability investigates and verifies → R&D proposes a material fix if needed → Marketing corrects messaging → Support responds to customers with accurate information."},
  {task:"A major clean-energy retrofit project at the main facility is running behind schedule.",
   primary:'facilities', support:['ops','finance','sustain'],
   reasoning:"Facilities & Logistics coordinates the contractors and timeline, Operations adjusts production around the disruption, Finance manages the revised budget, and Sustainability ensures the emissions targets tied to the project are still on track.",
   flow:"Facilities re-plans the schedule with contractors → Operations adapts daily workflows → Finance approves budget changes → Sustainability confirms targets remain achievable."}
];

const WORKPLACE_INTRO = "You're steering operations for a company built entirely around 100% environmentally-friendly practices. Every task, hand-off, and crisis tests whether the org actually understands who does what — and when to work together.";

/* ============================= STATE ============================= */

let state = {
  stage: 0, // 0 = intro, 1/2/3 = stages, 4 = summary
  s1: {tasks:[], index:0, results:[]},
  s2: {tasks:[], index:0, results:[]},
  s3: {tasks:[], index:0, results:[]},
  scores: {ownership:0, delegation:0, collaboration:0, workflow:0},
  maxScores: {ownership:3, delegation:3, collaboration:3, workflow:3}
};

function shuffle(arr){
  const a = arr.slice();
  for(let i=a.length-1;i>0;i--){
    const j = Math.floor(Math.random()*(i+1));
    [a[i],a[j]]=[a[j],a[i]];
  }
  return a;
}

function pickN(pool,n){ return shuffle(pool).slice(0,n); }

/* ============================= RENDER ROOT ============================= */

const app = document.getElementById('app');

function render(){
  app.innerHTML = '';
  app.appendChild(buildHeader());
  if(state.stage===0) app.appendChild(buildIntro());
  else if(state.stage===1) app.appendChild(buildStage1());
  else if(state.stage===2) app.appendChild(buildStage2());
  else if(state.stage===3) app.appendChild(buildStage3());
  else if(state.stage===4) app.appendChild(buildSummary());
  app.appendChild(buildFooter());
}

function buildHeader(){
  const wrap = document.createElement('div');
  const h = document.createElement('header');
  h.className='top';
  h.innerHTML = `
    <h1 class="display">🧭 Task Compass</h1>
    <p>Learn how work flows through real organizations.</p>
  `;
  wrap.appendChild(h);

  if(state.stage>0){
    const vine = document.createElement('div');
    vine.className='vine-wrap';
    let pct = 0;
    let totalDone = 0, totalNeeded = 9;
    if(state.stage>=1) totalDone += state.s1.results.length;
    if(state.stage>=2) totalDone += state.s2.results.length;
    if(state.stage>=3) totalDone += state.s3.results.length;
    if(state.stage===4) totalDone = 9;
    pct = Math.min(100, Math.round(totalDone/totalNeeded*100));
    vine.innerHTML = `
      <div class="vine-track"><div class="vine-fill" style="width:${pct}%"></div></div>
      <div class="stage-labels">
        <span class="${state.stage===1?'active':''}">1. Who Owns This?</span>
        <span class="${state.stage===2?'active':''}">2. Task Routing</span>
        <span class="${state.stage===3?'active':''}">3. Collaboration</span>
        <span class="${state.stage===4?'active':''}">Reflection</span>
      </div>
    `;
    wrap.appendChild(vine);
  }
  return wrap;
}

function buildFooter(){
  const f = document.createElement('footer');
  f.className='credit';
  f.textContent = 'Task Compass — a management simulation, not a quiz.';
  return f;
}

/* ============================= INTRO ============================= */

function buildIntro(){
  const p = document.createElement('div');
  p.className='panel';
  p.innerHTML = `
    <p class="small-note" style="font-size:1rem; color:var(--cream-dim); line-height:1.6;">${WORKPLACE_INTRO}</p>
    <p style="line-height:1.6;">You'll move through three stages: figuring out who owns a task, routing work through the right hand-offs, and coordinating a full team response to a bigger challenge. There are no wrong-answer buzzers here — every choice gets explained.</p>
    <div style="margin-top:20px;">
      <button class="primary" id="startBtn">Begin the simulation 🌿</button>
    </div>
  `;
  p.querySelector('#startBtn').addEventListener('click', ()=>{
    state.s1.tasks = pickN(STAGE1_POOL,3);
    state.s2.tasks = pickN(STAGE2_POOL,3);
    state.s3.tasks = pickN(STAGE3_POOL,3);
    state.stage = 1;
    render();
  });
  return p;
}

/* ============================= STAGE 1 ============================= */

let s1Selected = null; // role id currently selected/dragged
let s1Revealed = false;

function buildStage1(){
  const wrap = document.createElement('div');
  const idx = state.s1.index;
  if(idx >= state.s1.tasks.length){
    // move to stage 2
    state.stage = 2; return buildStage2();
  }
  const data = state.s1.tasks[idx];
  s1Revealed = false;

  const panel = document.createElement('div');
  panel.className='panel';

  panel.innerHTML = `
    <div class="ticket">
      <span class="tag">Task ${idx+1} of ${state.s1.tasks.length} · Who Owns This?</span>
      <div class="body">${data.task}</div>
    </div>
    <p class="small-note">Drag (or tap, then tap the box) the role that should <b>primarily own</b> this task.</p>
    <div class="role-pool" id="rolePool"></div>
    <div class="slot-zone" id="ownerSlot">Drop the owning role here</div>
    <div id="revealArea"></div>
    <div class="actions-row" id="actionsRow"></div>
  `;
  wrap.appendChild(panel);

  const pool = panel.querySelector('#rolePool');
  ROLES.forEach(r=>{
    const c = makeRoleCard(r);
    c.addEventListener('dragstart', e=>{
      e.dataTransfer.setData('text/plain', r.id);
      c.classList.add('dragging');
    });
    c.addEventListener('dragend', ()=>c.classList.remove('dragging'));
    c.addEventListener('click', ()=>{
      if(s1Revealed) return;
      document.querySelectorAll('#rolePool .role-card').forEach(x=>x.classList.remove('selected'));
      c.classList.add('selected');
      s1Selected = r.id;
    });
    pool.appendChild(c);
  });

  const slot = panel.querySelector('#ownerSlot');
  slot.addEventListener('dragover', e=>{ e.preventDefault(); slot.classList.add('dragover'); });
  slot.addEventListener('dragleave', ()=> slot.classList.remove('dragover'));
  slot.addEventListener('drop', e=>{
    e.preventDefault();
    slot.classList.remove('dragover');
    const rid = e.dataTransfer.getData('text/plain');
    if(rid) placeOwner(rid, data, panel);
  });
  slot.addEventListener('click', ()=>{
    if(s1Selected && !s1Revealed) placeOwner(s1Selected, data, panel);
  });

  return wrap;
}

function placeOwner(rid, data, panel){
  if(s1Revealed) return;
  s1Revealed = true;
  const r = roleById(rid);
  const slot = panel.querySelector('#ownerSlot');
  slot.classList.add('filled');
  slot.innerHTML = `<span class="emoji">${r.emoji}</span>&nbsp; <b>${r.name}</b>`;

  const correct = rid === data.owner;
  if(correct) state.scores.ownership++;
  state.s1.results.push({correct, chosen:rid, correctId:data.owner});

  const correctRole = roleById(data.owner);
  const assistNames = data.assist.map(a=>roleById(a).name).join(', ');

  const reveal = panel.querySelector('#revealArea');
  reveal.innerHTML = `
    <div class="reveal">
      <h3>${correct ? '🌿 Nice instinct.' : "🔎 Here's how it usually plays out."}</h3>
      <p><span class="label">Primary owner:</span> ${correctRole.emoji} ${correctRole.name}</p>
      <p><span class="label">Why they own it:</span> ${data.why}</p>
      <p><span class="label">Who may assist:</span> ${assistNames}</p>
    </div>
  `;

  const actions = panel.querySelector('#actionsRow');
  const btn = document.createElement('button');
  btn.className='primary';
  btn.textContent = state.s1.index < state.s1.tasks.length-1 ? 'Next task →' : 'Continue to Stage 2 →';
  btn.addEventListener('click', ()=>{
    state.s1.index++;
    s1Selected = null;
    render();
  });
  actions.appendChild(btn);
}

function makeRoleCard(r){
  const c = document.createElement('div');
  c.className='role-card';
  c.draggable = true;
  c.style.setProperty('--rc', r.color);
  c.innerHTML = `<span class="emoji">${r.emoji}</span><span>${r.name}</span>`;
  return c;
}

/* ============================= STAGE 2 ============================= */

let s2Chain = []; // array of role ids in order, length = data.steps.length, filled progressively
let s2Selected = null;
let s2Revealed = false;

function buildStage2(){
  const wrap = document.createElement('div');
  const idx = state.s2.index;
  if(idx >= state.s2.tasks.length){
    state.stage = 3; return buildStage3();
  }
  const data = state.s2.tasks[idx];
  s2Chain = new Array(data.steps.length).fill(null);
  s2Selected = null;
  s2Revealed = false;

  const panel = document.createElement('div');
  panel.className='panel';
  panel.innerHTML = `
    <div class="ticket">
      <span class="tag">Task ${idx+1} of ${state.s2.tasks.length} · Task Routing</span>
      <div class="body">${data.task}</div>
    </div>
    <p class="small-note">Build the hand-off chain. Drag roles into order between "Customer" and "Customer" — this one needs <b>${data.steps.length}</b> step${data.steps.length>1?'s':''}.</p>
    <div class="chain-wrap" id="chainWrap"></div>
    <div class="role-pool" id="rolePool2"></div>
    <div id="revealArea2"></div>
    <div class="actions-row" id="actionsRow2"></div>
  `;
  wrap.appendChild(panel);

  renderChain(panel, data);

  const pool = panel.querySelector('#rolePool2');
  ROLES.forEach(r=>{
    const c = makeRoleCard(r);
    c.dataset.roleId = r.id;
    c.addEventListener('dragstart', e=>{
      e.dataTransfer.setData('text/plain', r.id);
      c.classList.add('dragging');
    });
    c.addEventListener('dragend', ()=>c.classList.remove('dragging'));
    c.addEventListener('click', ()=>{
      if(s2Revealed) return;
      document.querySelectorAll('#rolePool2 .role-card').forEach(x=>x.classList.remove('selected'));
      c.classList.add('selected');
      s2Selected = r.id;
    });
    pool.appendChild(c);
  });

  return wrap;
}

function renderChain(panel, data){
  const chainWrap = panel.querySelector('#chainWrap');
  chainWrap.innerHTML = '';
  const startNode = document.createElement('div');
  startNode.className='chain-node fixed';
  startNode.textContent = '🧑 Customer';
  chainWrap.appendChild(startNode);

  data.steps.forEach((_, i)=>{
    const arrow = document.createElement('span');
    arrow.className='chain-arrow';
    arrow.textContent='→';
    chainWrap.appendChild(arrow);

    const slot = document.createElement('div');
    slot.className='chain-node slot';
    slot.dataset.index = i;
    if(s2Chain[i]){
      const r = roleById(s2Chain[i]);
      slot.classList.add('filled');
      slot.innerHTML = `${r.emoji} ${r.name}`;
    } else {
      slot.textContent = `Step ${i+1}`;
    }
    slot.addEventListener('dragover', e=>{ e.preventDefault(); slot.classList.add('dragover'); });
    slot.addEventListener('dragleave', ()=> slot.classList.remove('dragover'));
    slot.addEventListener('drop', e=>{
      e.preventDefault();
      slot.classList.remove('dragover');
      const rid = e.dataTransfer.getData('text/plain');
      if(rid) fillChainSlot(i, rid, panel, data);
    });
    slot.addEventListener('click', ()=>{
      if(s2Selected && !s2Revealed) fillChainSlot(i, s2Selected, panel, data);
    });
    chainWrap.appendChild(slot);
  });

  const arrow2 = document.createElement('span');
  arrow2.className='chain-arrow';
  arrow2.textContent='→';
  chainWrap.appendChild(arrow2);
  const endNode = document.createElement('div');
  endNode.className='chain-node fixed';
  endNode.textContent = '🧑 Customer';
  chainWrap.appendChild(endNode);
}

function fillChainSlot(i, rid, panel, data){
  if(s2Revealed) return;
  s2Chain[i] = rid;
  renderChain(panel, data);
  // mark used in pool visually
  const allFilled = s2Chain.every(x=>x!==null);
  if(allFilled){
    const btn = document.createElement('button');
    btn.className='primary';
    btn.textContent='Submit route';
    const actions = panel.querySelector('#actionsRow2');
    actions.innerHTML='';
    btn.addEventListener('click', ()=> revealStage2(panel, data));
    actions.appendChild(btn);
  }
}

function revealStage2(panel, data){
  if(s2Revealed) return;
  s2Revealed = true;
  const correctOrder = data.steps.join(',');
  const chosenOrder = s2Chain.join(',');
  const correct = correctOrder === chosenOrder;
  if(correct) state.scores.workflow++;
  state.s2.results.push({correct});

  // animate playback
  const reveal = panel.querySelector('#revealArea2');
  reveal.innerHTML = `
    <div class="reveal">
      <h3>${correct ? "✅ That's the flow teams commonly use." : "🔁 Here's how this one commonly flows."}</h3>
      <div class="route-anim" id="routeAnim"></div>
      <p><span class="label">Why this order works:</span> ${data.reasoning}</p>
    </div>
  `;
  const anim = reveal.querySelector('#routeAnim');
  const nodes = ['Customer', ...data.steps.map(s=>roleById(s).name), 'Customer'];
  nodes.forEach(n=>{
    const el = document.createElement('div');
    el.className='node';
    el.textContent = n;
    anim.appendChild(el);
  });
  let i=0;
  const nodeEls = anim.querySelectorAll('.node');
  const timer = setInterval(()=>{
    if(i<nodeEls.length){ nodeEls[i].classList.add('lit'); i++; }
    else clearInterval(timer);
  }, 350);

  const actions = panel.querySelector('#actionsRow2');
  actions.innerHTML='';
  const nextBtn = document.createElement('button');
  nextBtn.className='primary';
  nextBtn.textContent = state.s2.index < state.s2.tasks.length-1 ? 'Next task →' : 'Continue to Stage 3 →';
  nextBtn.addEventListener('click', ()=>{
    state.s2.index++;
    render();
  });
  actions.appendChild(nextBtn);
}

/* ============================= STAGE 3 ============================= */

let s3Picked = [];
let s3Revealed = false;

function buildStage3(){
  const wrap = document.createElement('div');
  const idx = state.s3.index;
  if(idx >= state.s3.tasks.length){
    state.stage = 4; return buildSummary();
  }
  const data = state.s3.tasks[idx];
  s3Picked = [];
  s3Revealed = false;

  const panel = document.createElement('div');
  panel.className='panel';
  panel.innerHTML = `
    <div class="ticket">
      <span class="tag">Challenge ${idx+1} of ${state.s3.tasks.length} · Collaboration Challenge</span>
      <div class="body">${data.task}</div>
    </div>
    <p class="small-note">Select up to <b>4</b> roles you'd involve. Big problems are rarely solved by one person.</p>
    <div class="role-pool" id="rolePool3"></div>
    <div class="pick-count" id="pickCount">0 / 4 selected</div>
    <div id="revealArea3"></div>
    <div class="actions-row" id="actionsRow3"></div>
  `;
  wrap.appendChild(panel);

  const pool = panel.querySelector('#rolePool3');
  ROLES.forEach(r=>{
    const c = makeRoleCard(r);
    c.draggable = false;
    c.style.cursor='pointer';
    c.addEventListener('click', ()=>{
      if(s3Revealed) return;
      if(s3Picked.includes(r.id)){
        s3Picked = s3Picked.filter(x=>x!==r.id);
        c.classList.remove('picked');
      } else {
        if(s3Picked.length>=4) return;
        s3Picked.push(r.id);
        c.classList.add('picked');
      }
      panel.querySelector('#pickCount').textContent = `${s3Picked.length} / 4 selected`;
      let actions = panel.querySelector('#actionsRow3');
      if(s3Picked.length>0 && !panel.querySelector('#submit3')){
        actions.innerHTML = `<button class="primary" id="submit3">Submit team</button>`;
        panel.querySelector('#submit3').addEventListener('click', ()=> revealStage3(panel, data));
      } else if(s3Picked.length===0){
        actions.innerHTML='';
      }
    });
    pool.appendChild(c);
  });

  return wrap;
}

function revealStage3(panel, data){
  if(s3Revealed) return;
  s3Revealed = true;
  const hitPrimary = s3Picked.includes(data.primary);
  const supportHits = data.support.filter(s=>s3Picked.includes(s)).length;
  const collabScore = (hitPrimary?1:0) + (supportHits>=2?1:0);
  // count toward collaboration (max 1 per challenge) and delegation
  if(hitPrimary) state.scores.collaboration++;
  if(supportHits>=1) state.scores.delegation++;
  state.s3.results.push({hitPrimary, supportHits});

  const primaryRole = roleById(data.primary);
  const supportNames = data.support.map(s=>roleById(s).name).join(', ');

  const reveal = panel.querySelector('#revealArea3');
  reveal.innerHTML = `
    <div class="reveal">
      <h3>🤝 How this typically plays out</h3>
      <p><span class="label">Primary owner:</span> ${primaryRole.emoji} ${primaryRole.name}</p>
      <p><span class="label">Supporting teams:</span> ${supportNames}</p>
      <p><span class="label">Reasoning:</span> ${data.reasoning}</p>
      <p><span class="label">Possible communication flow:</span> ${data.flow}</p>
    </div>
  `;

  const actions = panel.querySelector('#actionsRow3');
  actions.innerHTML='';
  const btn = document.createElement('button');
  btn.className='primary';
  btn.textContent = state.s3.index < state.s3.tasks.length-1 ? 'Next challenge →' : 'See your reflection →';
  btn.addEventListener('click', ()=>{
    state.s3.index++;
    render();
    if(state.stage===4) launchConfetti();
  });
  actions.appendChild(btn);
}

/* ============================= SUMMARY ============================= */

function buildSummary(){
  const wrap = document.createElement('div');
  const panel = document.createElement('div');
  panel.className='panel';

  const pct = k => Math.round((state.scores[k]/state.maxScores[k])*100);

  panel.innerHTML = `
    <h2 class="display" style="margin-top:0;">Your Understanding, Mapped</h2>
    <p class="small-note" style="font-size:0.95rem;">Not a score — a picture of how you think about ownership, delegation, collaboration and workflow.</p>
    <div class="summary-grid">
      <div><canvas id="radar" width="320" height="320" style="max-width:100%;"></canvas></div>
      <div id="barList"></div>
    </div>
  `;
  wrap.appendChild(panel);

  // bars
  const bars = panel.querySelector('#barList');
  const cats = [['ownership','Ownership','🎯'],['delegation','Delegation','🤲'],['collaboration','Collaboration','🤝'],['workflow','Workflow Thinking','🔄']];
  cats.forEach(([k,label,emoji])=>{
    const row = document.createElement('div');
    row.style.marginBottom='14px';
    row.innerHTML = `
      <div style="display:flex; justify-content:space-between; font-size:0.9rem; margin-bottom:4px;">
        <span>${emoji} ${label}</span><span>${pct(k)}%</span>
      </div>
      <div class="vine-track"><div class="vine-fill" style="width:${pct(k)}%; animation-delay:0.2s;"></div></div>
    `;
    bars.appendChild(row);
  });

  // reflection panel
  const reflectPanel = document.createElement('div');
  reflectPanel.className='panel';
  reflectPanel.innerHTML = `<h2 class="display" style="margin-top:0;">Reflection</h2>`;
  const list = document.createElement('ul');
  list.className='reflection-list';

  const strong = Object.keys(pct).length ? null : null;
  const catPercents = {ownership:pct('ownership'), delegation:pct('delegation'), collaboration:pct('collaboration'), workflow:pct('workflow')};
  const best = Object.keys(catPercents).reduce((a,b)=>catPercents[a]>=catPercents[b]?a:b);
  const worst = Object.keys(catPercents).reduce((a,b)=>catPercents[a]<=catPercents[b]?a:b);
  const labelMap = {ownership:'Ownership', delegation:'Delegation', collaboration:'Collaboration', workflow:'Workflow Thinking'};

  const overAssignCount = state.s1.results.filter(r=>!r.correct).length;
  const underCollabCount = state.s3.results.filter(r=>!r.hitPrimary || r.supportHits<2).length;

  const li1 = document.createElement('li');
  li1.innerHTML = `<b>What you understood well:</b> Your strongest area tended to be <b>${labelMap[best]}</b> — you often picked up on who a task naturally belongs to or how teams typically coordinate.`;
  list.appendChild(li1);

  const li2 = document.createElement('li');
  li2.innerHTML = overAssignCount>0
    ? `<b>Where you may have over- or under-assigned responsibility:</b> In ${overAssignCount} of ${state.s1.results.length} ownership calls, the primary owner tended to land somewhere other than your first instinct — a reminder that ownership often follows who's closest to the root cause, not who's most visible.`
    : `<b>Ownership calls:</b> You consistently matched the roles that own each task in this org — a good sign for reading responsibility boundaries.`;
  list.appendChild(li2);

  const li3 = document.createElement('li');
  li3.innerHTML = underCollabCount>0
    ? `<b>Where collaboration tends to get underestimated:</b> In some larger challenges, involving more than one or two roles usually produced a fuller response — complex problems rarely stay inside one department for long.`
    : `<b>Collaboration:</b> You consistently pulled in supporting teams for bigger challenges, reflecting how cross-functional response tends to work in practice.`;
  list.appendChild(li3);

  const li4 = document.createElement('li');
  li4.innerHTML = `<b>One insight:</b> Many real workplace problems are solved by teams rather than individuals — ownership usually means coordinating the right people, not doing all the work alone.`;
  list.appendChild(li4);

  reflectPanel.appendChild(list);

  const restart = document.createElement('div');
  restart.className='actions-row';
  restart.innerHTML = `<button class="ghost" id="restartBtn">Run the simulation again ↺</button>`;
  reflectPanel.appendChild(restart);

  wrap.appendChild(reflectPanel);

  setTimeout(()=>drawRadar(panel.querySelector('#radar'), catPercents), 50);

  wrap.querySelector('#restartBtn')?.addEventListener('click', ()=>{
    state = {
      stage: 0,
      s1:{tasks:[],index:0,results:[]},
      s2:{tasks:[],index:0,results:[]},
      s3:{tasks:[],index:0,results:[]},
      scores:{ownership:0,delegation:0,collaboration:0,workflow:0},
      maxScores:{ownership:3,delegation:3,collaboration:3,workflow:3}
    };
    render();
  });

  return wrap;
}

function drawRadar(canvas, catPercents){
  if(!canvas) return;
  const ctx = canvas.getContext('2d');
  const cx = canvas.width/2, cy = canvas.height/2, R = Math.min(cx,cy)-40;
  const labels = ['Ownership','Delegation','Collaboration','Workflow'];
  const keys = ['ownership','delegation','collaboration','workflow'];
  const N = 4;
  ctx.clearRect(0,0,canvas.width,canvas.height);

  // rings
  ctx.strokeStyle='rgba(242,237,225,0.15)';
  ctx.fillStyle='rgba(242,237,225,0.7)';
  ctx.font='11px sans-serif';
  for(let ring=1; ring<=4; ring++){
    ctx.beginPath();
    for(let i=0;i<=N;i++){
      const ang = (Math.PI*2*i/N) - Math.PI/2;
      const r = R*ring/4;
      const x = cx + r*Math.cos(ang);
      const y = cy + r*Math.sin(ang);
      if(i===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
    }
    ctx.stroke();
  }
  // axes + labels
  for(let i=0;i<N;i++){
    const ang = (Math.PI*2*i/N) - Math.PI/2;
    const x = cx + R*Math.cos(ang);
    const y = cy + R*Math.sin(ang);
    ctx.beginPath();
    ctx.moveTo(cx,cy);
    ctx.lineTo(x,y);
    ctx.strokeStyle='rgba(242,237,225,0.15)';
    ctx.stroke();
    const lx = cx + (R+22)*Math.cos(ang);
    const ly = cy + (R+22)*Math.sin(ang);
    ctx.textAlign='center';
    ctx.fillText(labels[i], lx, ly);
  }
  // data poly
  ctx.beginPath();
  keys.forEach((k,i)=>{
    const ang = (Math.PI*2*i/N) - Math.PI/2;
    const val = catPercents[k]/100;
    const r = R*val;
    const x = cx + r*Math.cos(ang);
    const y = cy + r*Math.sin(ang);
    if(i===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
  });
  ctx.closePath();
  ctx.fillStyle='rgba(143,188,106,0.35)';
  ctx.strokeStyle='#8fbc6a';
  ctx.lineWidth=2;
  ctx.fill();
  ctx.stroke();
}

function launchConfetti(){
  const emojis = ['🌿','🍃','✨','🌱','💚'];
  for(let i=0;i<26;i++){
    const el = document.createElement('div');
    el.className='confetti';
    el.textContent = emojis[Math.floor(Math.random()*emojis.length)];
    el.style.left = Math.random()*100+'vw';
    el.style.animationDuration = (2.5+Math.random()*1.8)+'s';
    document.body.appendChild(el);
    setTimeout(()=>el.remove(), 4500);
  }
}

render();
})();
</script>
</body>
</html>
<img width="600" height="459" alt="image" src="https://github.com/user-attachments/assets/c09145aa-5792-4d3f-b267-882ef302f6b8" />
<img width="611" height="584" alt="image" src="https://github.com/user-attachments/assets/2ca286d4-4b1e-485c-bcce-200a4756f9b1" />
<img width="632" height="409" alt="image" src="https://github.com/user-attachments/assets/98ff125c-6a57-4c44-88ba-0e4200eaafbb" />
<img width="606" height="589" alt="image" src="https://github.com/user-attachments/assets/3101fa1a-18df-4a8b-ac80-5963f89bb08e" />
<img width="611" height="583" alt="image" src="https://github.com/user-attachments/assets/98c38a09-f5f7-40bd-970c-ddda8d16f129" />
<img width="619" height="581" alt="image" src="https://github.com/user-attachments/assets/29eb8cd1-3c57-4697-929c-35b2d9e3ae8b" />
<img width="607" height="575" alt="image" src="https://github.com/user-attachments/assets/ef8c50a5-a117-4603-af7a-31e14e0737ce" />
<img width="577" height="584" alt="image" src="https://github.com/user-attachments/assets/5cf74ab8-4716-4f3b-a935-a06fbcc9bfe5" />
<img width="643" height="554" alt="image" src="https://github.com/user-attachments/assets/b968c1d2-13d6-4cf6-aa66-0cd7b800cbc8" />
<img width="633" height="593" alt="image" src="https://github.com/user-attachments/assets/f667dd33-0fab-48c5-b034-2c0094088b98" />
<img width="635" height="545" alt="image" src="https://github.com/user-attachments/assets/b9c0cb42-061d-4281-abe5-a15d279c9cf2" />
<img width="583" height="587" alt="image" src="https://github.com/user-attachments/assets/4cec4a4b-9743-4f9f-8506-55000fa1a46c" />
<img width="603" height="588" alt="image" src="https://github.com/user-attachments/assets/7eb01c32-993a-4d68-b19c-73c652cc7919" />
<img width="615" height="451" alt="image" src="https://github.com/user-attachments/assets/9100a5d3-8966-4e73-bf45-b896e0aaefcd" />
<img width="603" height="564" alt="image" src="https://github.com/user-attachments/assets/d94b93e6-2247-452e-b02c-702addfc870a" />
<img width="603" height="564" alt="image" src="https://github.com/user-attachments/assets/07e80c66-116a-46ad-8ba7-393f02782fd5" />
<img width="649" height="578" alt="image" src="https://github.com/user-attachments/assets/da9e493a-496c-414b-8ec7-d79da8bbb804" />

