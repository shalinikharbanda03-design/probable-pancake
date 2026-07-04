:Prompt:
Act as an expert Product Designer, Operations Consultant, UX Designer, and Frontend Developer.

Build a complete interactive web application called:

# AI Supply Chain Control Tower

The goal is to simulate the experience of being the Head of Operations in a global supply chain company.

The entire project must be contained inside ONE self-contained HTML file using HTML, CSS, and vanilla JavaScript only.

Do NOT use React, Vue, Angular, Tailwind, Bootstrap, external libraries, APIs, or backend services.

Everything should work offline after opening the HTML file.

--------------------------------------------------
THEME
--------------------------------------------------

Create a premium dark Operations Control Center inspired by modern logistics dashboards.

Use:

• Dark background
• Blue and cyan highlights
• Red warning alerts
• Green success indicators
• Orange medium priority alerts

Animated glowing cards

Modern dashboard layout

Professional typography

Smooth transitions

--------------------------------------------------
GAMEPLAY
--------------------------------------------------

The player becomes:

Head of Operations

A stream of operational alerts appears.

The player must decide which issue to solve first.

Every decision changes business KPIs.

The goal is to maximize operational performance before time runs out.

--------------------------------------------------
KPIs
--------------------------------------------------

Display these live metrics at the top:

Service Level %

Customer Satisfaction

Inventory Health

Transportation Efficiency

Operating Cost

Revenue Protected

Score

Remaining Time

--------------------------------------------------
ALERT TYPES
--------------------------------------------------

Randomly generate alerts like:

🚨 Port Congestion

🚨 Supplier Delay

🚨 Truck Breakdown

🚨 Warehouse Running Out of Stock

🚨 Customs Inspection

🚨 Demand Spike

🚨 Factory Machine Failure

🚨 Weather Disruption

🚨 Wrong Inventory Count

🚨 Damaged Shipment

Each alert should include:

Title

Short description

Priority

Time remaining

Business impact

--------------------------------------------------
PLAYER ACTIONS
--------------------------------------------------

Each alert should provide action buttons such as:

Expedite Shipment

Use Backup Supplier

Reroute Trucks

Increase Production

Transfer Inventory

Approve Air Freight

Ignore

Delay Decision

Each action should have different consequences.

--------------------------------------------------
GAME LOGIC
--------------------------------------------------

Choosing the best action:

Increase score

Improve KPIs

Reduce future risk

Wrong decisions should:

Reduce KPIs

Increase operating cost

Lower customer satisfaction

Some decisions should have delayed consequences after several seconds.

--------------------------------------------------
DIFFICULTY
--------------------------------------------------

Game lasts 3 minutes.

As time progresses:

More alerts appear.

Alert frequency increases.

Multiple alerts stay active simultaneously.

--------------------------------------------------
VISUALS
--------------------------------------------------

Include:

Animated KPI cards

Live scrolling event log

Countdown timer

Priority color coding

Small pulse animation for critical alerts

Hover effects

Professional dashboard layout

--------------------------------------------------
END OF GAME
--------------------------------------------------

When time ends show:

Final Score

Performance Grade

(A+, A, B, C, D)

Final KPI values

Total Alerts Resolved

Correct Decisions

Wrong Decisions

A short operational summary based on performance.

Include a Play Again button.

--------------------------------------------------
EXTRA FEATURES
--------------------------------------------------

Add:

Sound toggle (visual only, no audio required)

Pause button

Help / Instructions modal

Responsive layout for desktop and mobile

--------------------------------------------------
CODE QUALITY
--------------------------------------------------

Write clean, well-commented code.

Keep CSS organized.

Keep JavaScript modular using functions.

Everything must remain inside ONE HTML file.

Return only the complete HTML document.

:Response:
A complete offline dashboard-game in one HTML file — dark blue/cyan control-tower theme, live KPI strip, streaming alert cards with priority pulses and countdown timers, an event log, pause/sound/help controls, escalating difficulty over the 3-minute shift, and an end screen with grade, KPI recap, and a Play Again button.

# Code #
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>AI Supply Chain Control Tower</title>
<style>
  :root{
    --bg:#060a12;
    --panel:#0b1220;
    --panel-2:#101a2c;
    --line:rgba(120,170,255,0.14);
    --text:#dfe8fb;
    --muted:#7b8bab;
    --cyan:#33e6ff;
    --blue:#4d8dff;
    --green:#3ee68a;
    --orange:#ffab3d;
    --red:#ff5a6e;
    --radius:14px;
    --font: 'Segoe UI', system-ui, -apple-system, sans-serif;
    --mono: 'Consolas', 'Courier New', monospace;
  }
  *{box-sizing:border-box;}
  html,body{margin:0;padding:0;}
  body{
    background:
      radial-gradient(1000px 600px at 10% -10%, rgba(77,141,255,0.10), transparent 60%),
      radial-gradient(900px 600px at 100% 0%, rgba(51,230,255,0.08), transparent 55%),
      var(--bg);
    color:var(--text);
    font-family:var(--font);
    min-height:100vh;
  }
  h1,h2,h3{margin:0; font-weight:700;}
  button{font-family:var(--font); cursor:pointer;}
  #app{max-width:1240px; margin:0 auto; padding:18px 16px 60px;}

  /* ---------- HEADER ---------- */
  .topbar{
    display:flex; align-items:center; justify-content:space-between;
    margin-bottom:18px; flex-wrap:wrap; gap:10px;
  }
  .brand{display:flex; align-items:center; gap:12px;}
  .brand .logo{
    width:38px; height:38px; border-radius:10px;
    background:linear-gradient(135deg, var(--cyan), var(--blue));
    display:flex; align-items:center; justify-content:center; font-size:19px;
    box-shadow:0 0 18px rgba(51,230,255,0.4);
  }
  .brand h1{font-size:19px; letter-spacing:0.02em;}
  .brand .sub{font-size:11.5px; color:var(--muted); font-family:var(--mono); text-transform:uppercase; letter-spacing:0.08em;}
  .top-actions{display:flex; gap:8px; flex-wrap:wrap;}
  .icon-btn{
    background:var(--panel-2); border:1px solid var(--line); color:var(--text);
    padding:9px 14px; border-radius:10px; font-size:13px; display:flex; align-items:center; gap:6px;
    transition:all .15s ease;
  }
  .icon-btn:hover{border-color:var(--cyan); color:var(--cyan);}
  .icon-btn.active{border-color:var(--green); color:var(--green);}

  /* ---------- KPI STRIP ---------- */
  .kpi-strip{
    display:grid; grid-template-columns:repeat(8,1fr); gap:10px; margin-bottom:20px;
  }
  @media(max-width:1100px){ .kpi-strip{grid-template-columns:repeat(4,1fr);} }
  @media(max-width:640px){ .kpi-strip{grid-template-columns:repeat(2,1fr);} }
  .kpi-card{
    background:linear-gradient(180deg, var(--panel), var(--panel-2));
    border:1px solid var(--line); border-radius:12px; padding:12px 12px 10px;
    position:relative; overflow:hidden; transition:box-shadow .3s ease;
  }
  .kpi-card::before{
    content:''; position:absolute; inset:0; border-radius:12px; padding:1px;
    background:linear-gradient(120deg, transparent, rgba(77,141,255,0.25), transparent);
    opacity:0; transition:opacity .3s;
  }
  .kpi-card.pulse{ animation:kpiPulse .6s ease; }
  @keyframes kpiPulse{
    0%{box-shadow:0 0 0 0 rgba(51,230,255,0.5);}
    100%{box-shadow:0 0 0 12px rgba(51,230,255,0);}
  }
  .kpi-label{font-family:var(--mono); font-size:10px; color:var(--muted); text-transform:uppercase; letter-spacing:0.06em; margin-bottom:6px;}
  .kpi-value{font-size:20px; font-weight:800; font-family:var(--mono);}
  .kpi-value.good{color:var(--green);}
  .kpi-value.mid{color:var(--orange);}
  .kpi-value.bad{color:var(--red);}
  .kpi-bar{height:4px; border-radius:3px; background:rgba(255,255,255,0.06); margin-top:8px; overflow:hidden;}
  .kpi-bar-fill{height:100%; border-radius:3px; transition:width .4s ease;}

  /* ---------- MAIN GRID ---------- */
  .main-grid{display:grid; grid-template-columns:1.6fr 1fr; gap:18px;}
  @media(max-width:920px){ .main-grid{grid-template-columns:1fr;} }

  .panel{
    background:linear-gradient(180deg, var(--panel), var(--panel-2));
    border:1px solid var(--line); border-radius:var(--radius); padding:18px;
    margin-bottom:18px;
  }
  .panel h2{font-size:14px; text-transform:uppercase; letter-spacing:0.08em; color:var(--cyan); font-family:var(--mono); margin-bottom:14px; display:flex; align-items:center; justify-content:space-between;}

  /* ---------- ALERT CARDS ---------- */
  .alerts-list{display:flex; flex-direction:column; gap:12px; max-height:600px; overflow-y:auto; padding-right:4px;}
  .alert-card{
    border-radius:12px; padding:15px; border:1px solid var(--line);
    background:var(--panel-2); position:relative; animation:slideIn .35s ease;
  }
  @keyframes slideIn{ from{opacity:0; transform:translateX(-14px);} to{opacity:1; transform:translateX(0);} }
  .alert-card.critical{ border-color:rgba(255,90,110,0.55); box-shadow:0 0 0 1px rgba(255,90,110,0.15);}
  .alert-card.critical .pulse-dot{ animation:blink 1s infinite; }
  @keyframes blink{ 0%,100%{opacity:1;} 50%{opacity:0.25;} }
  .alert-card.medium{ border-color:rgba(255,171,61,0.5); }
  .alert-card.low{ border-color:rgba(62,230,138,0.4); }
  .alert-card.resolved{ opacity:0.45; }

  .alert-top{display:flex; justify-content:space-between; align-items:flex-start; gap:10px; margin-bottom:6px;}
  .alert-title-row{display:flex; align-items:center; gap:8px;}
  .pulse-dot{width:8px; height:8px; border-radius:50%; flex-shrink:0;}
  .pulse-dot.critical{background:var(--red);}
  .pulse-dot.medium{background:var(--orange);}
  .pulse-dot.low{background:var(--green);}
  .alert-title{font-size:15px; font-weight:700;}
  .alert-priority{
    font-family:var(--mono); font-size:10px; text-transform:uppercase; padding:3px 8px; border-radius:20px;
    letter-spacing:0.05em; flex-shrink:0;
  }
  .alert-priority.critical{background:rgba(255,90,110,0.16); color:var(--red);}
  .alert-priority.medium{background:rgba(255,171,61,0.16); color:var(--orange);}
  .alert-priority.low{background:rgba(62,230,138,0.16); color:var(--green);}

  .alert-desc{font-size:13px; color:var(--muted); margin-bottom:8px; line-height:1.4;}
  .alert-meta{display:flex; gap:14px; font-family:var(--mono); font-size:11px; color:var(--muted); margin-bottom:10px; flex-wrap:wrap;}
  .alert-meta b{color:var(--text);}
  .alert-timer-bar{height:4px; border-radius:3px; background:rgba(255,255,255,0.07); margin-bottom:12px; overflow:hidden;}
  .alert-timer-fill{height:100%; background:linear-gradient(90deg, var(--cyan), var(--blue)); transition:width 1s linear;}

  .action-row{display:flex; flex-wrap:wrap; gap:8px;}
  .action-btn{
    background:rgba(77,141,255,0.1); border:1px solid rgba(77,141,255,0.35); color:var(--text);
    padding:8px 12px; border-radius:8px; font-size:12.5px; transition:all .15s ease;
  }
  .action-btn:hover{background:rgba(51,230,255,0.18); border-color:var(--cyan); color:var(--cyan);}
  .action-btn.ignore{background:rgba(255,90,110,0.08); border-color:rgba(255,90,110,0.3);}
  .action-btn.ignore:hover{border-color:var(--red); color:var(--red);}
  .action-btn.delay{background:rgba(255,171,61,0.08); border-color:rgba(255,171,61,0.3);}
  .action-btn.delay:hover{border-color:var(--orange); color:var(--orange);}

  .empty-state{color:var(--muted); font-size:13.5px; text-align:center; padding:40px 10px;}

  /* ---------- EVENT LOG ---------- */
  .log-list{display:flex; flex-direction:column-reverse; gap:8px; max-height:280px; overflow-y:auto; font-family:var(--mono); font-size:12px;}
  .log-item{padding:8px 10px; border-radius:8px; background:var(--panel-2); border-left:3px solid var(--line); animation:fadeIn .3s ease;}
  @keyframes fadeIn{ from{opacity:0;} to{opacity:1;} }
  .log-item.good{border-left-color:var(--green);}
  .log-item.bad{border-left-color:var(--red);}
  .log-item.neutral{border-left-color:var(--muted);}
  .log-time{color:var(--muted); margin-right:6px;}

  /* ---------- SCORE / TIMER PANEL ---------- */
  .timer-display{
    text-align:center; font-family:var(--mono); font-size:38px; font-weight:800; color:var(--cyan);
    letter-spacing:0.03em; margin-bottom:6px; text-shadow:0 0 20px rgba(51,230,255,0.35);
  }
  .timer-sub{text-align:center; color:var(--muted); font-size:11.5px; font-family:var(--mono); text-transform:uppercase; letter-spacing:0.08em; margin-bottom:14px;}
  .score-display{text-align:center; font-size:30px; font-weight:800; font-family:var(--mono); color:var(--green); margin-bottom:4px;}
  .score-label{text-align:center; color:var(--muted); font-size:11px; font-family:var(--mono); text-transform:uppercase; letter-spacing:0.08em;}

  .stat-mini-row{display:flex; justify-content:space-between; margin-top:14px; padding-top:14px; border-top:1px solid var(--line);}
  .stat-mini{text-align:center; flex:1;}
  .stat-mini .num{font-size:18px; font-weight:800; font-family:var(--mono);}
  .stat-mini .lbl{font-size:10px; color:var(--muted); text-transform:uppercase; letter-spacing:0.04em; font-family:var(--mono);}

  /* ---------- MODAL ---------- */
  .modal-overlay{
    position:fixed; inset:0; background:rgba(3,6,12,0.78); backdrop-filter:blur(4px);
    display:flex; align-items:center; justify-content:center; z-index:100; padding:20px;
  }
  .modal{
    background:linear-gradient(180deg, var(--panel), var(--panel-2)); border:1px solid var(--line);
    border-radius:18px; padding:30px; max-width:560px; width:100%; max-height:85vh; overflow-y:auto;
    animation:modalIn .3s ease;
  }
  @keyframes modalIn{ from{opacity:0; transform:scale(0.96);} to{opacity:1; transform:scale(1);} }
  .modal h2{font-size:22px; margin-bottom:14px; color:var(--cyan);}
  .modal p, .modal li{font-size:14.5px; line-height:1.6; color:var(--text);}
  .modal ul{padding-left:20px; margin:10px 0;}
  .modal .btn{
    margin-top:18px; background:linear-gradient(120deg, var(--cyan), var(--blue)); border:none; color:#03131c;
    font-weight:800; padding:12px 22px; border-radius:10px; font-size:14.5px;
  }

  /* ---------- START SCREEN ---------- */
  .start-screen{ text-align:center; padding:60px 20px; }
  .start-screen h1{font-size:clamp(28px,5vw,44px); margin-bottom:14px;
    background:linear-gradient(120deg, var(--cyan), var(--blue)); -webkit-background-clip:text; background-clip:text; color:transparent;}
  .start-screen p{color:var(--muted); font-size:15.5px; max-width:560px; margin:0 auto 26px; line-height:1.6;}
  .start-btn{
    background:linear-gradient(120deg, var(--cyan), var(--blue)); border:none; color:#03131c;
    font-weight:800; padding:16px 36px; border-radius:12px; font-size:16px;
    box-shadow:0 0 30px rgba(51,230,255,0.35);
  }
  .start-btn:hover{ transform:translateY(-2px); }

  /* ---------- END SCREEN ---------- */
  .grade-display{
    font-size:80px; font-weight:900; text-align:center; font-family:var(--mono);
    text-shadow:0 0 40px currentColor; margin:10px 0;
  }
  .end-kpi-grid{display:grid; grid-template-columns:repeat(4,1fr); gap:10px; margin:20px 0;}
  @media(max-width:640px){ .end-kpi-grid{grid-template-columns:repeat(2,1fr);} }

  ::-webkit-scrollbar{width:6px;}
  ::-webkit-scrollbar-thumb{background:var(--line); border-radius:4px;}

  .hidden{display:none !important;}
  .paused-banner{
    text-align:center; padding:60px 20px; color:var(--orange); font-family:var(--mono); font-size:20px;
  }
</style>
</head>
<body>
<div id="app"></div>

<script>
/* =====================================================================
   AI SUPPLY CHAIN CONTROL TOWER — vanilla JS single file game
===================================================================== */

/* ---------------------- STATE ---------------------- */
const GAME_LENGTH = 180; // seconds
const state = {
  screen: 'start', // start | playing | paused | end
  soundOn: true,
  timeRemaining: GAME_LENGTH,
  score: 0,
  kpis: {
    serviceLevel: 92,
    satisfaction: 88,
    inventoryHealth: 85,
    transportEfficiency: 80,
    operatingCost: 50,   // lower is better, shown as index
    revenueProtected: 100 // percentage of revenue protected
  },
  alerts: [],
  log: [],
  resolvedCount: 0,
  correctCount: 0,
  wrongCount: 0,
  nextAlertId: 1,
  spawnTimer: null,
  tickTimer: null,
};

let alertTimers = {}; // id -> interval reference for countdown

/* ---------------------- ALERT DEFINITIONS ---------------------- */
const ALERT_TYPES = [
  {
    key:'port', icon:'🚢', title:'Port Congestion',
    desc:'Containers are stuck at the port due to unusually high vessel traffic.',
    impact:'Delivery delays across multiple downstream routes.',
    actions:[
      {label:'Approve Air Freight', effect:{serviceLevel:+6, operatingCost:+18, satisfaction:+4, revenueProtected:+8}, correct:true, log:'Air freight approved — port congestion bypassed at higher cost.'},
      {label:'Reroute Trucks', effect:{serviceLevel:+2, transportEfficiency:+3, satisfaction:+1}, correct:true, log:'Trucks rerouted around the congested port.'},
      {label:'Ignore', effect:{serviceLevel:-10, satisfaction:-8, revenueProtected:-10}, correct:false, log:'Port congestion ignored — deliveries fell badly behind.'},
      {label:'Delay Decision', effect:{serviceLevel:-4, satisfaction:-2}, correct:false, log:'Decision delayed — congestion worsened before action was taken.'},
    ]
  },
  {
    key:'supplier', icon:'🏭', title:'Supplier Delay',
    desc:'A key raw-material supplier has announced a multi-day shipping delay.',
    impact:'Production may stall if inventory buffers run out.',
    actions:[
      {label:'Use Backup Supplier', effect:{inventoryHealth:+10, operatingCost:+10, revenueProtected:+6}, correct:true, log:'Backup supplier activated — production stayed on track.'},
      {label:'Transfer Inventory', effect:{inventoryHealth:+6, transportEfficiency:-2}, correct:true, log:'Inventory transferred from another site to cover the gap.'},
      {label:'Ignore', effect:{inventoryHealth:-14, satisfaction:-6, revenueProtected:-8}, correct:false, log:'Supplier delay ignored — inventory shortages began.'},
      {label:'Delay Decision', effect:{inventoryHealth:-6}, correct:false, log:'Decision delayed — the buffer shrank further.'},
    ]
  },
  {
    key:'truck', icon:'🚛', title:'Truck Breakdown',
    desc:'A delivery truck broke down mid-route with a full load onboard.',
    impact:'Last-mile deliveries in that region are at risk of delay.',
    actions:[
      {label:'Reroute Trucks', effect:{transportEfficiency:+8, serviceLevel:+4, operatingCost:+5}, correct:true, log:'Nearby trucks rerouted to cover the failed delivery.'},
      {label:'Expedite Shipment', effect:{serviceLevel:+5, operatingCost:+8}, correct:true, log:'Replacement shipment expedited to the affected region.'},
      {label:'Ignore', effect:{serviceLevel:-8, satisfaction:-6}, correct:false, log:'Truck breakdown ignored — customers received nothing.'},
      {label:'Delay Decision', effect:{serviceLevel:-3, transportEfficiency:-3}, correct:false, log:'Delay caused the load to sit idle for hours.'},
    ]
  },
  {
    key:'stock', icon:'📦', title:'Warehouse Running Out of Stock',
    desc:'A regional warehouse is projected to run out of a top-selling SKU within hours.',
    impact:'Stockouts will directly hurt sales and satisfaction.',
    actions:[
      {label:'Transfer Inventory', effect:{inventoryHealth:+10, satisfaction:+5, revenueProtected:+6}, correct:true, log:'Inventory transferred just in time to prevent a stockout.'},
      {label:'Increase Production', effect:{inventoryHealth:+6, operatingCost:+10}, correct:true, log:'Production ramped up to refill the warehouse.'},
      {label:'Ignore', effect:{inventoryHealth:-12, satisfaction:-10, revenueProtected:-12}, correct:false, log:'Stockout occurred — lost sales and unhappy customers.'},
      {label:'Delay Decision', effect:{inventoryHealth:-5, satisfaction:-3}, correct:false, log:'Delay meant the shelf sat empty longer than needed.'},
    ]
  },
  {
    key:'customs', icon:'🛃', title:'Customs Inspection',
    desc:'A shipment has been flagged for random customs inspection at the border.',
    impact:'Clearance delays could ripple into downstream schedules.',
    actions:[
      {label:'Expedite Shipment', effect:{serviceLevel:+5, operatingCost:+7}, correct:true, log:'Expedited clearance fees paid to speed up the inspection.'},
      {label:'Delay Decision', effect:{serviceLevel:-2}, correct:true, log:'Waited out the standard inspection — no extra cost incurred.'},
      {label:'Ignore', effect:{serviceLevel:-9, satisfaction:-5}, correct:false, log:'Shipment sat at the border far longer than necessary.'},
      {label:'Approve Air Freight', effect:{operatingCost:+16, serviceLevel:+2}, correct:false, log:'Air freight approved unnecessarily — costs spiked with little benefit.'},
    ]
  },
  {
    key:'demand', icon:'📈', title:'Demand Spike',
    desc:'Social media buzz has triggered an unexpected spike in demand for one product line.',
    impact:'Current inventory and production may not keep pace.',
    actions:[
      {label:'Increase Production', effect:{revenueProtected:+12, inventoryHealth:+4, operatingCost:+9}, correct:true, log:'Production increased to capture the surge in demand.'},
      {label:'Transfer Inventory', effect:{revenueProtected:+7, inventoryHealth:+2}, correct:true, log:'Inventory pooled from other regions to meet demand.'},
      {label:'Ignore', effect:{revenueProtected:-14, satisfaction:-4}, correct:false, log:'Demand spike ignored — a rare growth opportunity was missed.'},
      {label:'Delay Decision', effect:{revenueProtected:-6}, correct:false, log:'By the time a decision was made, the spike had passed.'},
    ]
  },
  {
    key:'machine', icon:'⚙️', title:'Factory Machine Failure',
    desc:'A critical production line machine has failed unexpectedly.',
    impact:'Output will drop until the issue is resolved.',
    actions:[
      {label:'Increase Production', effect:{inventoryHealth:+5, operatingCost:+12}, correct:true, log:'Other lines ramped up to offset the failed machine.'},
      {label:'Use Backup Supplier', effect:{inventoryHealth:+7, operatingCost:+8}, correct:true, log:'A backup contract manufacturer covered the shortfall.'},
      {label:'Ignore', effect:{inventoryHealth:-13, revenueProtected:-9}, correct:false, log:'Machine failure ignored — output fell sharply.'},
      {label:'Delay Decision', effect:{inventoryHealth:-6}, correct:false, log:'Delay allowed inventory levels to slide further.'},
    ]
  },
  {
    key:'weather', icon:'🌪️', title:'Weather Disruption',
    desc:'A storm system is disrupting regional transportation routes.',
    impact:'Multiple shipments risk delay if routes aren\'t adjusted.',
    actions:[
      {label:'Reroute Trucks', effect:{transportEfficiency:+9, serviceLevel:+3, operatingCost:+4}, correct:true, log:'Routes adjusted ahead of the storm — disruption minimized.'},
      {label:'Delay Decision', effect:{transportEfficiency:-1}, correct:true, log:'Waited for the storm to pass rather than overreacting — a reasonable call.'},
      {label:'Ignore', effect:{transportEfficiency:-11, satisfaction:-7}, correct:false, log:'Trucks drove straight into the disruption, causing major delays.'},
      {label:'Approve Air Freight', effect:{operatingCost:+15, transportEfficiency:+2}, correct:false, log:'Costly air freight used when a simple reroute would have worked.'},
    ]
  },
  {
    key:'count', icon:'🔢', title:'Wrong Inventory Count',
    desc:'A cycle count revealed a discrepancy between system and physical stock.',
    impact:'Inaccurate data could cause bad ordering and fulfillment decisions.',
    actions:[
      {label:'Transfer Inventory', effect:{inventoryHealth:+6, satisfaction:+2}, correct:true, log:'Inventory reconciled and rebalanced across locations.'},
      {label:'Delay Decision', effect:{inventoryHealth:+1}, correct:true, log:'Scheduled a full recount before making further changes — cautious and correct.'},
      {label:'Ignore', effect:{inventoryHealth:-10, satisfaction:-4}, correct:false, log:'Data error ignored — future orders will now be wrong too.'},
      {label:'Increase Production', effect:{operatingCost:+10, inventoryHealth:-2}, correct:false, log:'Production increased based on faulty data — wasted cost.'},
    ]
  },
  {
    key:'damage', icon:'📉', title:'Damaged Shipment',
    desc:'A shipment arrived at the distribution center with visible damage.',
    impact:'Customer orders tied to this shipment may be at risk.',
    actions:[
      {label:'Transfer Inventory', effect:{satisfaction:+5, revenueProtected:+5}, correct:true, log:'Replacement stock transferred to fulfill affected orders.'},
      {label:'Expedite Shipment', effect:{satisfaction:+4, operatingCost:+7}, correct:true, log:'A replacement shipment was expedited to the customer.'},
      {label:'Ignore', effect:{satisfaction:-11, revenueProtected:-7}, correct:false, log:'Damaged goods shipped anyway — customer complaints followed.'},
      {label:'Delay Decision', effect:{satisfaction:-4}, correct:false, log:'Delay meant affected customers found out the hard way.'},
    ]
  },
];

/* ---------------------- UTIL ---------------------- */
function clamp(v,min,max){ return Math.max(min, Math.min(max, v)); }
function fmtTime(sec){
  const m = Math.floor(sec/60).toString().padStart(2,'0');
  const s = Math.floor(sec%60).toString().padStart(2,'0');
  return m+':'+s;
}
function kpiClass(val, invert){
  const v = invert ? 100-val : val;
  if(v >= 70) return 'good';
  if(v >= 45) return 'mid';
  return 'bad';
}

/* ---------------------- RENDER ROOT ---------------------- */
const app = document.getElementById('app');

function render(){
  if(state.screen === 'start') return renderStart();
  if(state.screen === 'end') return renderEnd();
  renderGame();
}

/* ---------------------- START SCREEN ---------------------- */
function renderStart(){
  app.innerHTML = `
    <div class="start-screen">
      <h1>AI Supply Chain Control Tower</h1>
      <p>You are the Head of Operations for a global supply chain network. Alerts will stream in — port congestion, supplier delays, demand spikes, and more. Decide fast, protect your KPIs, and keep the network running for 3 minutes.</p>
      <button class="start-btn" id="startBtn">▶ Start Shift</button>
      <div style="margin-top:16px;">
        <button class="icon-btn" id="helpBtnStart">❓ How to Play</button>
      </div>
    </div>
  `;
  document.getElementById('startBtn').onclick = startGame;
  document.getElementById('helpBtnStart').onclick = () => showModal(helpModalContent());
}

/* ---------------------- HELP MODAL ---------------------- */
function helpModalContent(){
  return `
    <h2>How to Play</h2>
    <p>You're managing a live supply chain. Alerts will appear on the left describing real operational problems.</p>
    <ul>
      <li><b>Pick an action</b> for each alert before its timer runs out.</li>
      <li>Smart actions <b>improve KPIs</b> and raise your <b>Score</b>.</li>
      <li>Poor choices — or ignoring an alert — <b>hurt KPIs</b> and increase cost.</li>
      <li>As the 3-minute shift goes on, alerts will arrive faster and multiple will be active at once.</li>
      <li>Some effects are delayed by a few seconds to simulate real operational lag.</li>
    </ul>
    <p>Keep your <b>Service Level</b>, <b>Satisfaction</b>, <b>Inventory Health</b>, and <b>Transport Efficiency</b> high, while keeping <b>Operating Cost</b> low and <b>Revenue Protected</b> high.</p>
    <button class="btn" id="closeModalBtn">Got it</button>
  `;
}

function showModal(html){
  const overlay = document.createElement('div');
  overlay.className = 'modal-overlay';
  overlay.id = 'modalOverlay';
  overlay.innerHTML = `<div class="modal">${html}</div>`;
  document.body.appendChild(overlay);
  const closeBtn = overlay.querySelector('#closeModalBtn');
  if(closeBtn) closeBtn.onclick = closeModal;
  overlay.addEventListener('click', (e)=>{ if(e.target === overlay) closeModal(); });
}
function closeModal(){
  const overlay = document.getElementById('modalOverlay');
  if(overlay) overlay.remove();
}

/* ---------------------- GAME START / LOOP ---------------------- */
function startGame(){
  state.screen = 'playing';
  state.timeRemaining = GAME_LENGTH;
  state.score = 0;
  state.kpis = {
    serviceLevel:92, satisfaction:88, inventoryHealth:85, transportEfficiency:80,
    operatingCost:50, revenueProtected:100
  };
  state.alerts = [];
  state.log = [];
  state.resolvedCount = 0;
  state.correctCount = 0;
  state.wrongCount = 0;
  state.nextAlertId = 1;
  addLog('Shift started. Monitoring supply chain network...', 'neutral');
  render();
  scheduleSpawns();
  state.tickTimer = setInterval(gameTick, 1000);
  spawnAlert(); // first alert immediately
}

function gameTick(){
  if(state.screen !== 'playing') return;
  state.timeRemaining -= 1;

  // countdown each alert
  state.alerts.forEach(a => { a.timeLeft -= 1; });
  // expire alerts whose time ran out (treated like "ignore")
  state.alerts.filter(a => a.timeLeft <= 0 && !a.resolved).forEach(a => {
    resolveAlert(a.id, null, true);
  });

  if(state.timeRemaining <= 0){
    endGame();
    return;
  }
  renderGame();
}

function scheduleSpawns(){
  // spawn frequency increases as time passes
  const spawnNext = () => {
    if(state.screen !== 'playing') return;
    spawnAlert();
    const elapsed = GAME_LENGTH - state.timeRemaining;
    // interval shrinks from ~9s down to ~3.5s
    const progress = clamp(elapsed / GAME_LENGTH, 0, 1);
    const interval = 9000 - progress * 5500;
    state.spawnTimer = setTimeout(spawnNext, interval);
  };
  state.spawnTimer = setTimeout(spawnNext, 6000);
}

function spawnAlert(){
  if(state.screen !== 'playing') return;
  // cap concurrent active alerts based on elapsed time (more chaos later)
  const activeCount = state.alerts.filter(a=>!a.resolved).length;
  const elapsed = GAME_LENGTH - state.timeRemaining;
  const maxActive = elapsed < 40 ? 2 : elapsed < 100 ? 4 : 6;
  if(activeCount >= maxActive) return;

  const type = ALERT_TYPES[Math.floor(Math.random()*ALERT_TYPES.length)];
  const priorities = ['critical','medium','low'];
  const weightRoll = Math.random();
  const priority = weightRoll < 0.4 ? 'critical' : weightRoll < 0.75 ? 'medium' : 'low';
  const baseTime = priority === 'critical' ? 22 : priority === 'medium' ? 30 : 38;

  const alert = {
    id: state.nextAlertId++,
    type,
    priority,
    timeLeft: baseTime,
    totalTime: baseTime,
    resolved: false,
  };
  state.alerts.unshift(alert);
  renderGame();
}

/* ---------------------- RESOLVE ALERT ---------------------- */
function resolveAlert(id, action, expired){
  const alert = state.alerts.find(a=>a.id===id);
  if(!alert || alert.resolved) return;
  alert.resolved = true;
  state.resolvedCount += 1;

  if(expired){
    applyEffect({serviceLevel:-6, satisfaction:-5, revenueProtected:-6});
    state.wrongCount += 1;
    state.score -= 10;
    addLog(`⏱ ${alert.type.title} expired unresolved — network impact absorbed.`, 'bad');
  } else {
    applyEffect(action.effect);
    if(action.correct){
      state.correctCount += 1;
      state.score += 15;
      addLog(`✅ ${alert.type.title}: "${action.label}" — ${action.log}`, 'good');
    } else {
      state.wrongCount += 1;
      state.score -= 6;
      addLog(`⚠ ${alert.type.title}: "${action.label}" — ${action.log}`, 'bad');
    }
  }

  // remove alert from list shortly after so log stays visible
  setTimeout(()=>{
    state.alerts = state.alerts.filter(a=>a.id!==id);
    renderGame();
  }, 500);

  // pulse KPI cards
  pulseKpis();
  renderGame();
}

function applyEffect(effect){
  Object.keys(effect).forEach(key=>{
    if(key === 'operatingCost'){
      state.kpis.operatingCost = clamp(state.kpis.operatingCost + effect[key], 0, 100);
    } else {
      state.kpis[key] = clamp(state.kpis[key] + effect[key], 0, 100);
    }
  });
}

function pulseKpis(){
  document.querySelectorAll('.kpi-card').forEach(el=>{
    el.classList.remove('pulse');
    void el.offsetWidth; // reflow to restart animation
    el.classList.add('pulse');
  });
}

function addLog(text, type){
  const time = fmtTime(state.timeRemaining);
  state.log.push({text, type, time});
  if(state.log.length > 60) state.log.shift();
}

/* ---------------------- PAUSE / SOUND ---------------------- */
function togglePause(){
  if(state.screen === 'playing'){
    state.screen = 'paused';
    clearInterval(state.tickTimer);
    clearTimeout(state.spawnTimer);
  } else if(state.screen === 'paused'){
    state.screen = 'playing';
    state.tickTimer = setInterval(gameTick, 1000);
    scheduleSpawns();
  }
  renderGame();
}
function toggleSound(){
  state.soundOn = !state.soundOn;
  renderGame();
}

/* ---------------------- END GAME ---------------------- */
function endGame(){
  state.screen = 'end';
  clearInterval(state.tickTimer);
  clearTimeout(state.spawnTimer);
  render();
}

function computeGrade(){
  const avgKpi = (
    state.kpis.serviceLevel + state.kpis.satisfaction + state.kpis.inventoryHealth +
    state.kpis.transportEfficiency + (100-state.kpis.operatingCost) + state.kpis.revenueProtected
  ) / 6;
  const combined = avgKpi * 0.6 + clamp(state.score/3, 0, 100) * 0.4;
  if(combined >= 88) return {grade:'A+', color:'var(--green)'};
  if(combined >= 78) return {grade:'A', color:'var(--green)'};
  if(combined >= 64) return {grade:'B', color:'var(--cyan)'};
  if(combined >= 48) return {grade:'C', color:'var(--orange)'};
  return {grade:'D', color:'var(--red)'};
}

function summaryText(gradeInfo){
  const g = gradeInfo.grade;
  if(g === 'A+') return "Exceptional shift. You anticipated disruptions, made fast and correct calls, and kept the entire network healthy under pressure.";
  if(g === 'A') return "Strong performance. Most decisions protected KPIs effectively, with only minor inefficiencies creeping in under pressure.";
  if(g === 'B') return "Solid but uneven shift. Good instincts on several alerts, but a few costly decisions or missed alerts held your score back.";
  if(g === 'C') return "A rocky shift. Several alerts were mishandled or ignored, leaving KPIs and revenue exposed to avoidable risk.";
  return "A difficult shift. Multiple critical alerts went unresolved or were handled poorly, causing significant operational damage.";
}

function renderEnd(){
  const g = computeGrade();
  app.innerHTML = `
    <div class="panel" style="max-width:720px; margin:30px auto;">
      <h2 style="text-align:center; color:var(--muted); letter-spacing:0.1em;">SHIFT COMPLETE</h2>
      <div class="grade-display" style="color:${g.color};">${g.grade}</div>
      <div class="score-display">${Math.max(0,state.score)}</div>
      <div class="score-label">Final Score</div>

      <div class="end-kpi-grid">
        ${kpiTile('Service Level', state.kpis.serviceLevel)}
        ${kpiTile('Satisfaction', state.kpis.satisfaction)}
        ${kpiTile('Inventory Health', state.kpis.inventoryHealth)}
        ${kpiTile('Transport Efficiency', state.kpis.transportEfficiency)}
        ${kpiTile('Operating Cost', state.kpis.operatingCost, true)}
        ${kpiTile('Revenue Protected', state.kpis.revenueProtected)}
      </div>

      <div class="stat-mini-row">
        <div class="stat-mini"><div class="num">${state.resolvedCount}</div><div class="lbl">Alerts Resolved</div></div>
        <div class="stat-mini"><div class="num" style="color:var(--green)">${state.correctCount}</div><div class="lbl">Correct Decisions</div></div>
        <div class="stat-mini"><div class="num" style="color:var(--red)">${state.wrongCount}</div><div class="lbl">Wrong Decisions</div></div>
      </div>

      <p style="margin-top:20px; color:var(--muted); line-height:1.6; font-size:14.5px;">${summaryText(g)}</p>

      <div style="text-align:center; margin-top:20px;">
        <button class="start-btn" id="playAgainBtn">🔁 Play Again</button>
      </div>
    </div>
  `;
  document.getElementById('playAgainBtn').onclick = startGame;
}

function kpiTile(label, value, invert){
  const cls = kpiClass(value, invert);
  return `
    <div class="kpi-card">
      <div class="kpi-label">${label}</div>
      <div class="kpi-value ${cls}">${Math.round(value)}${invert ? '' : '%'}</div>
    </div>
  `;
}

/* ---------------------- GAME SCREEN RENDER ---------------------- */
function renderGame(){
  if(state.screen === 'paused'){
    app.innerHTML = `
      ${topbarHtml()}
      <div class="panel paused-banner">
        ⏸ Shift Paused<br/>
        <button class="start-btn" style="margin-top:20px;" id="resumeBtn">▶ Resume</button>
      </div>
    `;
    bindTopbar();
    document.getElementById('resumeBtn').onclick = togglePause;
    return;
  }

  app.innerHTML = `
    ${topbarHtml()}
    ${kpiStripHtml()}
    <div class="main-grid">
      <div class="panel">
        <h2><span>🚨 Live Alerts</span><span style="color:var(--muted); font-weight:400; font-size:11px;">${state.alerts.filter(a=>!a.resolved).length} active</span></h2>
        <div class="alerts-list" id="alertsList">
          ${state.alerts.length ? state.alerts.map(alertHtml).join('') : '<div class="empty-state">No active alerts. Monitoring network...</div>'}
        </div>
      </div>
      <div>
        <div class="panel">
          <h2>⏱ Shift Status</h2>
          <div class="timer-display">${fmtTime(state.timeRemaining)}</div>
          <div class="timer-sub">Time Remaining</div>
          <div class="score-display">${state.score}</div>
          <div class="score-label">Score</div>
          <div class="stat-mini-row">
            <div class="stat-mini"><div class="num">${state.resolvedCount}</div><div class="lbl">Resolved</div></div>
            <div class="stat-mini"><div class="num" style="color:var(--green)">${state.correctCount}</div><div class="lbl">Correct</div></div>
            <div class="stat-mini"><div class="num" style="color:var(--red)">${state.wrongCount}</div><div class="lbl">Wrong</div></div>
          </div>
        </div>
        <div class="panel">
          <h2>📜 Event Log</h2>
          <div class="log-list" id="logList">
            ${state.log.slice().reverse().map(l => `<div class="log-item ${l.type}"><span class="log-time">[${l.time}]</span>${l.text}</div>`).join('')}
          </div>
        </div>
      </div>
    </div>
  `;

  bindTopbar();
  // bind action buttons
  document.querySelectorAll('.action-btn').forEach(btn=>{
    btn.onclick = () => {
      const alertId = parseInt(btn.dataset.alertId);
      const actionIdx = parseInt(btn.dataset.actionIdx);
      const alert = state.alerts.find(a=>a.id===alertId);
      if(!alert || alert.resolved) return;
      const action = alert.type.actions[actionIdx];
      resolveAlert(alertId, action, false);
    };
  });
}

function topbarHtml(){
  return `
    <div class="topbar">
      <div class="brand">
        <div class="logo">🛰️</div>
        <div>
          <h1>AI Supply Chain Control Tower</h1>
          <div class="sub">Head of Operations Console</div>
        </div>
      </div>
      <div class="top-actions">
        <button class="icon-btn ${state.soundOn ? 'active' : ''}" id="soundBtn">${state.soundOn ? '🔊' : '🔇'} Sound</button>
        <button class="icon-btn" id="pauseBtn">${state.screen === 'paused' ? '▶ Resume' : '⏸ Pause'}</button>
        <button class="icon-btn" id="helpBtn">❓ Help</button>
      </div>
    </div>
  `;
}
function bindTopbar(){
  const s = document.getElementById('soundBtn'); if(s) s.onclick = toggleSound;
  const p = document.getElementById('pauseBtn'); if(p) p.onclick = togglePause;
  const h = document.getElementById('helpBtn'); if(h) h.onclick = () => showModal(helpModalContent());
}

function kpiStripHtml(){
  const k = state.kpis;
  return `
    <div class="kpi-strip">
      ${kpiStripTile('Service Level', k.serviceLevel)}
      ${kpiStripTile('Satisfaction', k.satisfaction)}
      ${kpiStripTile('Inventory Health', k.inventoryHealth)}
      ${kpiStripTile('Transport Eff.', k.transportEfficiency)}
      ${kpiStripTile('Operating Cost', k.operatingCost, true)}
      ${kpiStripTile('Revenue Protected', k.revenueProtected)}
      ${kpiStripTile('Score', clamp(state.score,0,999), false, true)}
      ${kpiStripTile('Time Left', state.timeRemaining, false, true, true)}
    </div>
  `;
}
function kpiStripTile(label, value, invert, isRaw, isTime){
  const display = isTime ? fmtTime(value) : (isRaw ? Math.round(value) : Math.round(value)+'%');
  const cls = isRaw ? (isTime ? (value < 30 ? 'bad' : value < 90 ? 'mid' : 'good') : 'good') : kpiClass(value, invert);
  const barPct = isRaw ? (isTime ? clamp((value/GAME_LENGTH)*100,0,100) : clamp(value/2,0,100)) : (invert ? 100-value : value);
  const barColor = cls === 'good' ? 'var(--green)' : cls === 'mid' ? 'var(--orange)' : 'var(--red)';
  return `
    <div class="kpi-card">
      <div class="kpi-label">${label}</div>
      <div class="kpi-value ${cls}">${display}</div>
      <div class="kpi-bar"><div class="kpi-bar-fill" style="width:${barPct}%; background:${barColor};"></div></div>
    </div>
  `;
}

function alertHtml(alert){
  const t = alert.type;
  const pct = clamp((alert.timeLeft/alert.totalTime)*100, 0, 100);
  const resolvedClass = alert.resolved ? 'resolved' : '';
  const actionsHtml = alert.resolved ? '' : `
    <div class="action-row">
      ${t.actions.map((a,i) => {
        let cls = 'action-btn';
        if(a.label === 'Ignore') cls += ' ignore';
        if(a.label === 'Delay Decision') cls += ' delay';
        return `<button class="${cls}" data-alert-id="${alert.id}" data-action-idx="${i}">${a.label}</button>`;
      }).join('')}
    </div>
  `;
  return `
    <div class="alert-card ${alert.priority} ${resolvedClass}">
      <div class="alert-top">
        <div class="alert-title-row">
          <span class="pulse-dot ${alert.priority}"></span>
          <span class="alert-title">${t.icon} ${t.title}</span>
        </div>
        <span class="alert-priority ${alert.priority}">${alert.priority}</span>
      </div>
      <div class="alert-desc">${t.desc}</div>
      <div class="alert-meta"><span>Impact: <b>${t.impact}</b></span></div>
      ${!alert.resolved ? `<div class="alert-timer-bar"><div class="alert-timer-fill" style="width:${pct}%;"></div></div>` : ''}
      ${actionsHtml}
      ${alert.resolved ? '<div style="font-family:var(--mono); font-size:11px; color:var(--muted);">Resolved</div>' : ''}
    </div>
  `;
}

/* ---------------------- INIT ---------------------- */
render();
</script>
</body>
</html>
<img width="604" height="555" alt="image" src="https://github.com/user-attachments/assets/b665163c-2813-4371-b08f-56a97f94927b" />
<img width="605" height="348" alt="image" src="https://github.com/user-attachments/assets/0e60027e-d0ec-4122-9bfe-f4171c808086" />
<img width="543" height="423" alt="image" src="https://github.com/user-attachments/assets/935223df-f2d9-461e-8acb-7fdd6f009755" />
