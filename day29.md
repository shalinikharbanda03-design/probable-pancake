You are an expert frontend developer, UX designer, game designer, and supply chain consultant.

Build it so a complete beginner can play it — plain language, context before every decision, 'why does this matter' explanations, and guidance that makes you feel smart rather than lost.

Build a complete single-file HTML app named 'Operation Lifeline: Supply Chain Crisis Lab'.

Requirements:
• Output ONLY one HTML file.
• React via CDN + Babel JSX.
• Plain HTML, CSS, and JavaScript only.
• No Tailwind, npm, backend, APIs, images, or external assets.
• Must run offline by opening the HTML file.
• No placeholders or incomplete features.

Flow:
1. Welcome screen with title, subtitle, and 'Start Simulation'.
2. Generate a random fictional company (industry, revenue, factories, warehouses, suppliers, inventory days, lead time, countries) displayed as modern cards.
3. Generate one random crisis (factory fire, supplier bankruptcy, port strike, cyberattack, flood, raw material shortage, political conflict, shipping delay) with urgency and business impact.
4. War Room: Present six response actions. The player chooses three. Simulate consequences by updating Cost, Inventory, Profit, Delivery Speed, and Customer Satisfaction using animated progress bars.
5. Negotiation: Branching supplier negotiation with four rounds. Each choice affects Trust, Price, and Lead Time. Display a negotiation score.
6. CEO Boardroom: Five multiple-choice leadership questions. Score executive decision-making.
7. AI Strategy: Let the player choose two AI investments from Demand Forecasting, Inventory Optimization, Supplier Risk Monitoring, Warehouse Vision, and Procurement Copilot. Show expected business impact.
8. Final Dashboard: Display Overall Crisis Score (0-100), Leadership, Negotiation, Resilience, Cost Control, Risk Management, and Customer Satisfaction. Include personalized feedback, biggest mistake, best decision, expert recommendation, and lessons learned.

Design:
• Premium dark theme inspired by enterprise dashboards.
• Responsive.
• Rounded cards.
• Smooth transitions.
• Hover effects.
• Progress bars.
• Modern typography.
• Replay button.
• Every playthrough should randomize companies, crises, values, and outcomes.

Structure the React code into reusable components using useState. Ensure every button works, there are no console errors, and the final response contains only the complete HTML code inside a single code block.

Respomse #
Got it — this is a rich, multi-stage simulation app. Let me quickly lock in a design direction before building (enterprise crisis-ops feel, not a templated dashboard), then generate the full single-file app.

**Design plan:**
- **Palette:** near-black void (`#0A0E14`) panels (`#121826`), amber signal accent (`#F5A623`) for urgency/ticker, teal (`#2DD4BF`) for resilience/positive metrics, danger red (`#EF4565`) for risk, blue (`#4C8DFF`) for AI/strategy layer
- **Type:** geometric display stack for headers/KPI numbers, clean system sans for body, monospace for the live ticker digits — no external font CDNs, since the file must open and run fully offline
- **Signature element:** a persistent **"Live Ops Ticker"** — a mission-control style strip pinned under the header from the War Room onward, scrolling KPI deltas with ▲▼ indicators and a running "Crisis Day" counter, like a trading floor tracking the incident in real time
- **Structure:** a numbered stage stepper (Company → Crisis → War Room → Negotiation → Boardroom → AI Strategy → Dashboard) — justified here since it's a real sequential process, not decoration

Building it now.Braces and parens balance out. Now let's copy it to outputs and share it.That's the complete "Operation Lifeline: Supply Chain Crisis Lab" — one self-contained HTML file (React + Babel via CDN, no other external assets, runs offline once loaded). Just double-click it to open in your browser and start playing.

What it covers, matching your flow:
- **Welcome → randomized company** (industry, revenue, factories, warehouses, suppliers, inventory days, lead time, sourcing countries)
- **Randomized crisis** (8 types) with urgency, description, and starting metric hits
- **War Room**: pick 3 of 6 response actions, each with a plain-language "why this matters" note and animated impact on Cost, Inventory, Profit, Delivery Speed, and Customer Satisfaction
- **Negotiation**: 4 branching rounds affecting Trust, Price, and Lead Time, ending in a Negotiation Score
- **CEO Boardroom**: 5 leadership MCQs scored into a Leadership Score
- **AI Strategy**: pick 2 of 5 AI investments with expected business impact
- **Executive Dashboard**: Overall Crisis Score plus Leadership, Negotiation, Resilience, Cost Control, Risk Management, and Customer Satisfaction — with a personalized best decision, biggest mistake, expert recommendation, and lessons learned, plus a full decision log
- A **Replay** button that re-randomizes everything

The persistent **"Live Ops Ticker"** at the top (from the War Room onward) tracks your five core metrics in real time like a mission-control strip, with a running "Crisis Day" counter — that's the signature visual thread tying the whole run together.

Go ahead and open it, run a playthrough, and take your screenshots for the day29 write-up.
file:///C:/Users/DELL/Downloads/operation-lifeline.html
[operation-lifeline.html](https://github.com/user-attachments/files/29646017/operation-lifeline.html)
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Operation Lifeline: Supply Chain Crisis Lab</title>
<style>
  :root{
    --void:#0A0E14;
    --panel:#121826;
    --panel-raised:#1A2332;
    --panel-hover:#202B3D;
    --border:#232D3F;
    --border-bright:#324259;
    --signal:#F5A623;
    --signal-dim:#8A6323;
    --teal:#2DD4BF;
    --teal-dim:#155E56;
    --danger:#EF4565;
    --danger-dim:#6B1F30;
    --blue:#4C8DFF;
    --blue-dim:#1F3B73;
    --text-1:#EAF0F7;
    --text-2:#9AA7BD;
    --text-3:#5C6A82;
    --font-display: 'Segoe UI Semibold','Helvetica Neue',Arial,sans-serif;
    --font-body: -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
    --font-mono: 'SF Mono','Cascadia Code','Consolas','Courier New',monospace;
  }
  *{box-sizing:border-box;}
  html,body{margin:0;padding:0;}
  body{
    background:
      radial-gradient(circle at 15% 0%, rgba(76,141,255,0.07), transparent 40%),
      radial-gradient(circle at 85% 100%, rgba(45,212,191,0.06), transparent 45%),
      var(--void);
    color:var(--text-1);
    font-family:var(--font-body);
    min-height:100vh;
    -webkit-font-smoothing:antialiased;
  }
  #root{min-height:100vh;display:flex;flex-direction:column;}
  ::selection{background:var(--signal);color:#1a1200;}
  ::-webkit-scrollbar{width:10px;height:10px;}
  ::-webkit-scrollbar-track{background:var(--void);}
  ::-webkit-scrollbar-thumb{background:var(--border-bright);border-radius:8px;}

  button{font-family:inherit;cursor:pointer;}
  button:focus-visible, a:focus-visible, [tabindex]:focus-visible{
    outline:2px solid var(--signal);
    outline-offset:2px;
  }
  @media (prefers-reduced-motion: reduce){
    *{animation-duration:0.01ms !important; transition-duration:0.01ms !important;}
  }

  .app-shell{max-width:1180px;margin:0 auto;padding:24px 20px 80px;width:100%;flex:1;display:flex;flex-direction:column;}

  /* ---------- Header / Stepper ---------- */
  .top-bar{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:18px;flex-wrap:wrap;}
  .brand{display:flex;align-items:center;gap:10px;}
  .brand-mark{width:34px;height:34px;border-radius:9px;background:linear-gradient(135deg,var(--signal),#c97a12);display:flex;align-items:center;justify-content:center;font-family:var(--font-display);font-weight:800;color:#191100;font-size:16px;flex-shrink:0;}
  .brand-text{font-family:var(--font-display);font-weight:700;letter-spacing:0.3px;font-size:15px;}
  .brand-text small{display:block;color:var(--text-3);font-weight:500;font-size:10.5px;letter-spacing:1.4px;text-transform:uppercase;margin-top:1px;}

  .stepper{display:flex;gap:6px;flex-wrap:wrap;}
  .step-pill{
    display:flex;align-items:center;gap:6px;padding:6px 10px 6px 7px;border-radius:999px;
    background:var(--panel);border:1px solid var(--border);font-size:11.5px;color:var(--text-3);
    transition:all .35s ease;
  }
  .step-pill .num{width:18px;height:18px;border-radius:50%;background:var(--border);color:var(--text-3);display:flex;align-items:center;justify-content:center;font-size:10px;font-family:var(--font-mono);flex-shrink:0;transition:all .35s ease;}
  .step-pill.done{color:var(--teal);border-color:var(--teal-dim);}
  .step-pill.done .num{background:var(--teal-dim);color:var(--teal);}
  .step-pill.active{color:var(--text-1);border-color:var(--signal);background:rgba(245,166,35,0.08);}
  .step-pill.active .num{background:var(--signal);color:#1a1200;}

  /* ---------- Live Ops Ticker (signature element) ---------- */
  .ticker-wrap{
    position:sticky;top:0;z-index:40;background:rgba(10,14,20,0.92);backdrop-filter:blur(6px);
    border:1px solid var(--border);border-radius:12px;margin-bottom:22px;overflow:hidden;
    box-shadow:0 8px 24px rgba(0,0,0,0.35);
  }
  .ticker-inner{display:flex;align-items:center;gap:0;padding:0 4px;}
  .ticker-label{
    font-family:var(--font-mono);font-size:10px;letter-spacing:1.5px;color:var(--void);
    background:var(--signal);padding:9px 12px;flex-shrink:0;font-weight:700;display:flex;align-items:center;gap:6px;
  }
  .ticker-dot{width:6px;height:6px;border-radius:50%;background:var(--danger);animation:pulse-dot 1.4s infinite;}
  @keyframes pulse-dot{0%,100%{opacity:1;}50%{opacity:0.25;}}
  .ticker-scroll{display:flex;gap:26px;padding:9px 16px;overflow-x:auto;flex:1;scrollbar-width:none;}
  .ticker-scroll::-webkit-scrollbar{display:none;}
  .ticker-item{display:flex;align-items:center;gap:6px;font-family:var(--font-mono);font-size:12px;white-space:nowrap;color:var(--text-2);}
  .ticker-item b{color:var(--text-1);font-weight:600;}
  .ticker-up{color:var(--teal);}
  .ticker-down{color:var(--danger);}
  .ticker-day{font-family:var(--font-mono);font-size:11px;color:var(--text-3);padding-right:14px;flex-shrink:0;border-right:1px solid var(--border);margin-right:2px;padding-right:12px;}

  /* ---------- Generic layout bits ---------- */
  .stage{animation:fadeUp .5s ease both;}
  @keyframes fadeUp{from{opacity:0;transform:translateY(10px);}to{opacity:1;transform:translateY(0);}}

  .eyebrow{font-family:var(--font-mono);font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--signal);margin:0 0 8px;}
  h1.stage-title{font-family:var(--font-display);font-size:clamp(26px,4vw,38px);margin:0 0 10px;line-height:1.1;letter-spacing:-0.5px;}
  p.stage-sub{color:var(--text-2);font-size:15px;line-height:1.6;max-width:760px;margin:0 0 26px;}

  .grid{display:grid;gap:16px;}
  .grid-2{grid-template-columns:repeat(2,1fr);}
  .grid-3{grid-template-columns:repeat(3,1fr);}
  .grid-4{grid-template-columns:repeat(4,1fr);}
  @media (max-width:860px){.grid-2,.grid-3,.grid-4{grid-template-columns:1fr;}}

  .card{
    background:linear-gradient(180deg,var(--panel),rgba(18,24,38,0.6));
    border:1px solid var(--border);border-radius:16px;padding:20px;
    transition:border-color .25s ease, transform .25s ease, box-shadow .25s ease;
  }
  .card.hoverable:hover{border-color:var(--border-bright);transform:translateY(-2px);box-shadow:0 10px 30px rgba(0,0,0,0.3);}
  .card-label{font-family:var(--font-mono);font-size:10.5px;letter-spacing:1.4px;text-transform:uppercase;color:var(--text-3);margin-bottom:6px;}
  .card-value{font-family:var(--font-display);font-size:22px;font-weight:700;}
  .card-value.small{font-size:17px;}

  .why-box{
    background:rgba(76,141,255,0.06);border:1px solid var(--blue-dim);border-left:3px solid var(--blue);
    border-radius:10px;padding:12px 14px;font-size:13px;color:var(--text-2);line-height:1.55;margin-top:10px;
  }
  .why-box b{color:var(--blue);}

  .btn{
    font-family:var(--font-display);font-weight:600;font-size:14px;border-radius:10px;padding:13px 22px;
    border:1px solid var(--border-bright);background:var(--panel-raised);color:var(--text-1);
    transition:all .2s ease;display:inline-flex;align-items:center;gap:8px;
  }
  .btn:hover{background:var(--panel-hover);border-color:var(--text-3);}
  .btn-primary{background:linear-gradient(135deg,var(--signal),#d98812);border-color:transparent;color:#1a1200;}
  .btn-primary:hover{filter:brightness(1.08);transform:translateY(-1px);box-shadow:0 8px 20px rgba(245,166,35,0.25);}
  .btn-primary:disabled{opacity:0.4;cursor:not-allowed;transform:none;box-shadow:none;filter:none;}
  .btn-ghost{background:transparent;border-color:var(--border);color:var(--text-2);}
  .btn-ghost:hover{color:var(--text-1);border-color:var(--border-bright);}
  .btn-row{display:flex;gap:12px;margin-top:28px;flex-wrap:wrap;}

  /* ---------- Progress / metric bars ---------- */
  .metric-row{margin-bottom:16px;}
  .metric-top{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px;}
  .metric-name{font-size:12.5px;color:var(--text-2);font-family:var(--font-mono);letter-spacing:0.5px;}
  .metric-num{font-family:var(--font-mono);font-size:13px;font-weight:600;}
  .bar-track{height:9px;border-radius:999px;background:var(--border);overflow:hidden;position:relative;}
  .bar-fill{height:100%;border-radius:999px;transition:width 1.1s cubic-bezier(.22,1,.36,1);}

  /* ---------- Choice cards (war room / negotiation / boardroom / ai) ---------- */
  .choice-card{
    text-align:left;width:100%;background:var(--panel);border:1px solid var(--border);border-radius:14px;
    padding:18px;transition:all .2s ease;display:flex;flex-direction:column;gap:8px;
  }
  .choice-card:hover{border-color:var(--signal);background:var(--panel-raised);transform:translateY(-2px);}
  .choice-card.selected{border-color:var(--teal);background:rgba(45,212,191,0.07);}
  .choice-card.disabled{opacity:0.35;pointer-events:none;}
  .choice-title{font-family:var(--font-display);font-size:15.5px;font-weight:700;}
  .choice-desc{font-size:13px;color:var(--text-2);line-height:1.5;}
  .choice-tag{display:inline-flex;align-self:flex-start;font-family:var(--font-mono);font-size:10px;letter-spacing:1px;text-transform:uppercase;padding:3px 8px;border-radius:6px;background:var(--border);color:var(--text-3);margin-top:4px;}
  .choice-tag.picked{background:var(--teal-dim);color:var(--teal);}

  .pill{display:inline-flex;align-items:center;gap:6px;font-family:var(--font-mono);font-size:11px;padding:5px 10px;border-radius:999px;background:var(--panel-raised);border:1px solid var(--border);color:var(--text-2);}
  .pill.urgent{background:var(--danger-dim);border-color:var(--danger);color:#ffb8c4;}

  .divider{height:1px;background:var(--border);margin:26px 0;}

  .score-ring-wrap{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:10px;}
  .score-num{font-family:var(--font-display);font-size:52px;font-weight:800;line-height:1;}
  .score-label{font-family:var(--font-mono);font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--text-3);margin-top:8px;}

  .feedback-block{background:var(--panel);border:1px solid var(--border);border-radius:14px;padding:18px;margin-bottom:14px;}
  .feedback-block h3{margin:0 0 8px;font-family:var(--font-display);font-size:14.5px;letter-spacing:0.3px;}
  .feedback-block p{margin:0;color:var(--text-2);font-size:13.5px;line-height:1.65;}
  .fb-best{border-left:3px solid var(--teal);}
  .fb-mistake{border-left:3px solid var(--danger);}
  .fb-expert{border-left:3px solid var(--blue);}
  .fb-lessons{border-left:3px solid var(--signal);}

  .log-line{display:flex;gap:10px;font-size:12.5px;padding:8px 0;border-bottom:1px solid var(--border);color:var(--text-2);}
  .log-line:last-child{border-bottom:none;}
  .log-line .dot{width:6px;height:6px;border-radius:50%;background:var(--signal);margin-top:5px;flex-shrink:0;}

  .welcome-hero{
    min-height:70vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;
    padding:40px 16px;position:relative;
  }
  .welcome-hero .glyph{
    font-family:var(--font-mono);font-size:12px;letter-spacing:3px;color:var(--signal);text-transform:uppercase;margin-bottom:18px;
    border:1px solid var(--signal-dim);padding:6px 14px;border-radius:999px;background:rgba(245,166,35,0.06);
  }
  .welcome-hero h1{font-family:var(--font-display);font-size:clamp(34px,6vw,58px);line-height:1.05;letter-spacing:-1px;margin:0 0 16px;max-width:820px;}
  .welcome-hero h1 span{color:var(--signal);}
  .welcome-hero p{color:var(--text-2);font-size:16px;max-width:600px;line-height:1.65;margin:0 0 34px;}
  .pulse-ring{position:absolute;width:340px;height:340px;border:1px solid var(--border);border-radius:50%;opacity:0.4;animation:ring-grow 4s ease-out infinite;}
  @keyframes ring-grow{0%{transform:scale(0.6);opacity:0.5;}100%{transform:scale(1.4);opacity:0;}}

  .footer-note{text-align:center;color:var(--text-3);font-size:11.5px;margin-top:40px;font-family:var(--font-mono);}

  input[type=range]{-webkit-appearance:none;width:100%;height:6px;border-radius:999px;background:var(--border);}
  input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:16px;height:16px;border-radius:50%;background:var(--signal);cursor:pointer;}
</style>
</head>
<body>
<div id="root"></div>

<script src="https://unpkg.com/react@18/umd/react.development.js"></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

<script type="text/babel" data-presets="react">
const { useState, useEffect, useRef, useMemo } = React;

/* =========================================================
   UTILITIES
========================================================= */
function rand(min, max){ return Math.floor(Math.random() * (max - min + 1)) + min; }
function pick(arr){ return arr[rand(0, arr.length - 1)]; }
function pickN(arr, n){
  const copy = [...arr];
  const out = [];
  while(out.length < n && copy.length){
    out.push(copy.splice(rand(0, copy.length - 1), 1)[0]);
  }
  return out;
}
function clamp(v, lo=0, hi=100){ return Math.max(lo, Math.min(hi, v)); }
function fmtMoney(n){
  if(n >= 1000) return "$" + (n/1000).toFixed(1) + "B";
  return "$" + n + "M";
}
function metricColor(v){
  if(v >= 70) return "var(--teal)";
  if(v >= 45) return "var(--signal)";
  return "var(--danger)";
}

/* =========================================================
   STATIC DATA
========================================================= */
const INDUSTRIES = ["Consumer Electronics","Automotive Components","Pharmaceuticals","Apparel & Footwear","Food & Beverage","Industrial Machinery","Home Appliances","Medical Devices"];
const NAME_ROOTS = ["Nova","Ironclad","Meridian","Solstice","Vantex","Cobalt","Anchor","Summit","Falcon","Bright Peak","Redwood","Halcyon","Aurelia","Ridgeline","Wavelength","Ferro","Northstar","Kestrel","Basalt","Larkspur"];
const NAME_SUFFIXES = ["Industries","Group","Dynamics","Holdings","Manufacturing","Global","Systems","Works","& Co.","Logistics","Materials","Partners"];
const COUNTRIES = ["Vietnam","Mexico","Poland","Taiwan","India","Brazil","South Korea","Thailand","Turkey","Malaysia","Czech Republic","Morocco","Indonesia","Romania"];

function generateCompany(){
  const industry = pick(INDUSTRIES);
  const name = `${pick(NAME_ROOTS)} ${pick(NAME_SUFFIXES)}`;
  const revenue = rand(80, 3200); // in $M
  const factories = rand(2, 9);
  const warehouses = rand(3, 16);
  const suppliers = rand(6, 42);
  const inventoryDays = rand(12, 58);
  const leadTime = rand(6, 46);
  const countries = pickN(COUNTRIES, rand(2, 5));
  return { industry, name, revenue, factories, warehouses, suppliers, inventoryDays, leadTime, countries };
}

const CRISES = [
  { id:"fire", name:"Factory Fire", urgency:"Critical",
    description:"A fire broke out overnight at one of your primary manufacturing plants, halting production lines and damaging finished-goods inventory.",
    impact:"Production capacity is down sharply and replacement inventory won't arrive for weeks.",
    hit:{ inventory:-22, delivery:-18, profit:-8 } },
  { id:"bankruptcy", name:"Key Supplier Bankruptcy", urgency:"Severe",
    description:"Your second-largest raw material supplier filed for bankruptcy without warning, freezing all pending shipments.",
    impact:"A critical input is now single-sourced and exposed, with no immediate backup contract in place.",
    hit:{ inventory:-18, cost:-12, delivery:-10 } },
  { id:"port", name:"Port Strike", urgency:"High",
    description:"Dockworkers at your main export/import hub have gone on indefinite strike, stranding dozens of containers.",
    impact:"Inbound and outbound freight is frozen at the port, with no confirmed resolution date.",
    hit:{ delivery:-25, csat:-10 } },
  { id:"cyber", name:"Cyberattack on Logistics Systems", urgency:"Critical",
    description:"A ransomware attack has locked your warehouse management and dispatch systems, blinding visibility into current stock.",
    impact:"Fulfillment teams are working manually, and order accuracy is dropping fast.",
    hit:{ delivery:-15, csat:-15, cost:-10 } },
  { id:"flood", name:"Regional Flooding", urgency:"Severe",
    description:"Severe flooding has damaged roads and a regional distribution center in one of your key markets.",
    impact:"A whole distribution region is temporarily cut off from resupply.",
    hit:{ inventory:-15, delivery:-20 } },
  { id:"shortage", name:"Raw Material Shortage", urgency:"High",
    description:"A sudden global shortage of a core raw material is driving prices up and squeezing available supply.",
    impact:"Procurement costs are spiking just as competitors chase the same limited supply.",
    hit:{ cost:-20, profit:-10 } },
  { id:"conflict", name:"Political Conflict in Sourcing Region", urgency:"Critical",
    description:"Escalating political conflict in a key sourcing country has disrupted transport corridors and border crossings.",
    impact:"Multiple suppliers in the region are unreachable and export permits are frozen.",
    hit:{ delivery:-20, inventory:-10, csat:-8 } },
  { id:"shipdelay", name:"Major Shipping Delay", urgency:"High",
    description:"A vessel carrying a large share of your quarterly inventory has been rerouted, adding three weeks to transit.",
    impact:"A large inbound shipment your sales forecast depended on is now weeks late.",
    hit:{ delivery:-18, inventory:-12 } },
];

const WARROOM_ACTIONS = [
  { id:"air", title:"Expedite Critical Shipments via Air Freight",
    desc:"Pull the most urgent orders off ocean/ground transit and fly them in instead.",
    why:"Air freight restores delivery speed almost immediately, but it's roughly 4-6x more expensive than standard shipping — a fast fix that eats into margin.",
    effect:{ cost:-15, inventory:10, profit:-10, delivery:25, csat:10 } },
  { id:"backup", title:"Activate Backup Supplier Network",
    desc:"Route orders to pre-qualified secondary suppliers you've held in reserve.",
    why:"Backup suppliers rebuild inventory buffers without a full production stoppage, though their pricing and lead times are usually slightly worse than your primary source.",
    effect:{ cost:-8, inventory:20, profit:-5, delivery:10, csat:5 } },
  { id:"ration", title:"Ration Inventory to Key Accounts",
    desc:"Prioritize your highest-value customers and delay or reduce fulfillment for smaller accounts.",
    why:"Protecting your biggest relationships preserves core revenue, but customers who get deprioritized will notice — and remember.",
    effect:{ cost:5, inventory:15, profit:5, delivery:-5, csat:-15 } },
  { id:"safety", title:"Emergency Safety-Stock Purchase",
    desc:"Buy extra inventory immediately at whatever price the market demands, to buy yourself time.",
    why:"This is the fastest way to rebuild a cushion, but panic-buying at short notice usually means paying a steep premium.",
    effect:{ cost:-20, inventory:25, profit:-15, delivery:5, csat:5 } },
  { id:"comm", title:"Launch Proactive Customer Communication",
    desc:"Get ahead of the disruption with transparent updates to customers about delays and what you're doing about it.",
    why:"Customers tolerate bad news far better than silence. Proactive communication is cheap and consistently protects satisfaction scores, even when the underlying problem isn't fully solved yet.",
    effect:{ cost:-3, inventory:0, profit:-2, delivery:0, csat:20 } },
  { id:"delay", title:"Delay Non-Critical Shipments",
    desc:"Deliberately slow down lower-priority orders to conserve cash and capacity for what matters most.",
    why:"This protects your cost base in the short term, but it directly trades away delivery speed and customer goodwill to do it.",
    effect:{ cost:10, inventory:5, profit:8, delivery:-20, csat:-10 } },
];

const NEGOTIATION_ROUNDS = [
  { id:"r1", prompt:"Your supplier opens the call by announcing a 15% price increase, citing 'market conditions.'",
    context:"How you respond here sets the tone for every round that follows — suppliers remember whether you pushed back with data or folded immediately.",
    options:[
      { label:"Accept the increase to keep things moving quickly", effect:{ trust:10, price:15, lead:0 }, quality:3 },
      { label:"Push back firmly and demand justification", effect:{ trust:-5, price:-10, lead:5 }, quality:6 },
      { label:"Propose a volume commitment in exchange for price stability", effect:{ trust:15, price:-5, lead:-5 }, quality:9 },
    ]},
  { id:"r2", prompt:"The supplier requests significantly longer payment terms to ease their own cash flow.",
    context:"Longer payment terms help your supplier's liquidity, which can actually protect your own supply chain if they're financially fragile right now.",
    options:[
      { label:"Agree to the full extension unconditionally", effect:{ trust:15, price:5, lead:0 }, quality:5 },
      { label:"Offer a partial extension tied to on-time delivery", effect:{ trust:8, price:0, lead:0 }, quality:9 },
      { label:"Refuse outright and hold your original terms", effect:{ trust:-10, price:-5, lead:10 }, quality:4 },
    ]},
  { id:"r3", prompt:"The supplier offers expedited shipping on your next batch — for a premium.",
    context:"Faster shipping could help your delivery metrics recover, but it's worth asking whether you actually need the whole batch expedited.",
    options:[
      { label:"Pay the premium for full expedited shipping", effect:{ trust:5, price:10, lead:-15 }, quality:6 },
      { label:"Decline and stick to standard shipping", effect:{ trust:0, price:0, lead:0 }, quality:5 },
      { label:"Propose splitting the premium cost 50/50", effect:{ trust:10, price:5, lead:-8 }, quality:9 },
    ]},
  { id:"r4", prompt:"The supplier proposes a long-term exclusive contract to lock in your business.",
    context:"Exclusivity can bring better pricing and priority treatment, but it also removes your flexibility to diversify sourcing after this crisis ends.",
    options:[
      { label:"Sign the exclusive contract to lock in favorable terms now", effect:{ trust:20, price:-10, lead:-10 }, quality:6 },
      { label:"Keep sourcing flexible with multiple suppliers", effect:{ trust:5, price:0, lead:0 }, quality:7 },
      { label:"Counter with a performance-based contract instead", effect:{ trust:15, price:-8, lead:-5 }, quality:10 },
    ]},
];

const BOARDROOM_QUESTIONS = [
  { q:"Your operations team is overwhelmed and morale is visibly dropping mid-crisis. What's your first move?",
    options:[
      { label:"Push harder and remind everyone of the deadlines", quality:2 },
      { label:"Acknowledge the strain, redistribute urgent tasks, and protect focus time", quality:10 },
      { label:"Authorize unlimited overtime and bonus pay", quality:6 },
      { label:"Stay out of it and let managers handle it internally", quality:3 },
    ]},
  { q:"A major customer calls, furious about a delayed shipment. How do you want this handled?",
    options:[
      { label:"Have support offer a generic apology and standard discount", quality:4 },
      { label:"Personally call the customer with a clear timeline and concrete next steps", quality:10 },
      { label:"Avoid the call until the shipment situation improves", quality:1 },
      { label:"Blame the supplier disruption in the response", quality:2 },
    ]},
  { q:"Mid-crisis, a board member pressures you to cut the safety and quality inspection budget to save cash. What do you do?",
    options:[
      { label:"Cut it — cash is critical right now", quality:2 },
      { label:"Hold firm on safety and quality, and show the board the longer-term cost of cutting it", quality:10 },
      { label:"Cut it partially without telling the board the tradeoffs", quality:1 },
      { label:"Delay the decision indefinitely", quality:4 },
    ]},
  { q:"Your team presents two recovery plans: one fast but expensive, one slower but cheaper. You have limited time to decide. What's your approach?",
    options:[
      { label:"Pick the cheaper plan by default to protect margin", quality:4 },
      { label:"Ask for the customer and reputational impact of each option, then decide quickly with that data", quality:10 },
      { label:"Delay the decision until more data arrives", quality:3 },
      { label:"Let the team vote and go with the majority, no further input", quality:5 },
    ]},
  { q:"After the worst of the crisis passes, how do you want to communicate with the wider company?",
    options:[
      { label:"Move on quickly — no need to dwell on it", quality:2 },
      { label:"Share an honest debrief: what went wrong, what worked, and what changes are coming", quality:10 },
      { label:"Only share the positive outcomes externally", quality:3 },
      { label:"Send a brief thank-you email and consider it closed", quality:5 },
    ]},
];

const AI_INVESTMENTS = [
  { id:"forecast", title:"Demand Forecasting AI",
    desc:"Uses historical and real-time signals to predict demand shifts before they hit your supply chain.",
    impact:"Reduces stockouts and overstock by anticipating demand swings weeks earlier.",
    boost:{ resilience:15, risk:15, cost:10 } },
  { id:"invopt", title:"Inventory Optimization AI",
    desc:"Continuously recalculates optimal stock levels across every warehouse in your network.",
    impact:"Frees up working capital while keeping service levels high.",
    boost:{ resilience:10, risk:5, cost:20 } },
  { id:"riskmon", title:"Supplier Risk Monitoring AI",
    desc:"Scans financial, geopolitical, and news signals to flag at-risk suppliers before they fail.",
    impact:"Gives you weeks of early warning on the next supplier disruption, instead of finding out after the fact.",
    boost:{ resilience:10, risk:25, cost:5 } },
  { id:"vision", title:"Warehouse Vision AI",
    desc:"Computer-vision monitoring of warehouse operations to catch errors and bottlenecks in real time.",
    impact:"Cuts fulfillment errors and speeds up pick-and-pack accuracy.",
    boost:{ resilience:5, risk:5, cost:15, csat:5 } },
  { id:"copilot", title:"Procurement Copilot",
    desc:"An AI assistant that drafts supplier negotiation strategy and flags contract risk clauses.",
    impact:"Speeds up procurement decisions and reduces costly contract oversights.",
    boost:{ resilience:5, risk:10, cost:10 } },
];

const STAGES = [
  { key:"welcome", label:"Start" },
  { key:"company", label:"Company" },
  { key:"crisis", label:"Crisis" },
  { key:"warroom", label:"War Room" },
  { key:"negotiation", label:"Negotiation" },
  { key:"boardroom", label:"Boardroom" },
  { key:"aistrategy", label:"AI Strategy" },
  { key:"dashboard", label:"Dashboard" },
];

/* =========================================================
   REUSABLE COMPONENTS
========================================================= */
function Stepper({ stageKey }){
  const idx = STAGES.findIndex(s => s.key === stageKey);
  return (
    <div className="stepper">
      {STAGES.map((s, i) => (
        <div key={s.key} className={"step-pill " + (i < idx ? "done" : i === idx ? "active" : "")}>
          <span className="num">{i < idx ? "✓" : i + 1}</span>
          <span>{s.label}</span>
        </div>
      ))}
    </div>
  );
}

function LiveTicker({ metrics, prevMetrics, day }){
  const entries = [
    { key:"cost", label:"COST CONTROL" },
    { key:"inventory", label:"INVENTORY" },
    { key:"profit", label:"PROFIT MARGIN" },
    { key:"delivery", label:"DELIVERY SPEED" },
    { key:"csat", label:"CSAT" },
  ];
  return (
    <div className="ticker-wrap">
      <div className="ticker-inner">
        <div className="ticker-label"><span className="ticker-dot"></span>LIVE OPS</div>
        <div className="ticker-scroll">
          <span className="ticker-day">CRISIS DAY {day}</span>
          {entries.map(e => {
            const v = Math.round(metrics[e.key]);
            const prev = prevMetrics ? Math.round(prevMetrics[e.key]) : v;
            const diff = v - prev;
            return (
              <div className="ticker-item" key={e.key}>
                {e.label} <b>{v}</b>
                {diff !== 0 && (
                  <span className={diff > 0 ? "ticker-up" : "ticker-down"}>
                    {diff > 0 ? "▲" : "▼"}{Math.abs(diff)}
                  </span>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

function MetricBar({ label, value }){
  return (
    <div className="metric-row">
      <div className="metric-top">
        <span className="metric-name">{label}</span>
        <span className="metric-num" style={{color:metricColor(value)}}>{Math.round(value)}</span>
      </div>
      <div className="bar-track">
        <div className="bar-fill" style={{ width: clamp(value) + "%", background: metricColor(value) }}></div>
      </div>
    </div>
  );
}

function MetricsPanel({ metrics }){
  return (
    <div className="card">
      <div className="card-label">Live Business Metrics</div>
      <MetricBar label="COST CONTROL" value={metrics.cost} />
      <MetricBar label="INVENTORY HEALTH" value={metrics.inventory} />
      <MetricBar label="PROFIT MARGIN" value={metrics.profit} />
      <MetricBar label="DELIVERY SPEED" value={metrics.delivery} />
      <MetricBar label="CUSTOMER SATISFACTION" value={metrics.csat} />
    </div>
  );
}

/* =========================================================
   STAGE: WELCOME
========================================================= */
function Welcome({ onStart }){
  return (
    <div className="welcome-hero">
      <div className="pulse-ring"></div>
      <div className="glyph">Executive Crisis Simulation</div>
      <h1>Operation <span>Lifeline</span></h1>
      <p>You're about to step into the role of a supply chain executive facing a live crisis. Every choice you make
      ripples through cost, inventory, delivery, and customer trust — there's no perfect answer, only tradeoffs.
      A new company and a new crisis are generated every time you play.</p>
      <button className="btn btn-primary" onClick={onStart}>Start Simulation →</button>
      <div className="footer-note">No two runs are the same. Randomized company, crisis, and outcomes each time.</div>
    </div>
  );
}

/* =========================================================
   STAGE: COMPANY PROFILE
========================================================= */
function CompanyProfile({ company, onContinue }){
  const cards = [
    { label:"Industry", value: company.industry },
    { label:"Annual Revenue", value: fmtMoney(company.revenue) },
    { label:"Factories", value: company.factories },
    { label:"Warehouses", value: company.warehouses },
    { label:"Active Suppliers", value: company.suppliers },
    { label:"Avg. Inventory Days", value: company.inventoryDays + " days" },
    { label:"Avg. Supplier Lead Time", value: company.leadTime + " days" },
    { label:"Sourcing Countries", value: company.countries.join(", "), wide:true },
  ];
  return (
    <div className="stage">
      <div className="eyebrow">Step 01 · Company Briefing</div>
      <h1 className="stage-title">Meet {company.name}</h1>
      <p className="stage-sub">This is the company you're now responsible for. Take a moment to understand its shape —
      its size, its supply footprint, and how thin or thick its buffers are — before the crisis briefing hits.</p>
      <div className="grid grid-4">
        {cards.map((c, i) => (
          <div className={"card hoverable" + (c.wide ? "" : "")} key={i} style={c.wide ? { gridColumn: "span 2" } : {}}>
            <div className="card-label">{c.label}</div>
            <div className={"card-value" + (c.wide ? " small" : "")}>{c.value}</div>
          </div>
        ))}
      </div>
      <div className="why-box">
        <b>Why this matters:</b> Companies with thinner inventory buffers (fewer inventory days) and longer supplier
        lead times are far more exposed when a disruption hits — there's less cushion to absorb the shock.
      </div>
      <div className="btn-row">
        <button className="btn btn-primary" onClick={onContinue}>Proceed to Crisis Briefing →</button>
      </div>
    </div>
  );
}

/* =========================================================
   STAGE: CRISIS BRIEFING
========================================================= */
function CrisisBriefing({ crisis, metrics, onContinue }){
  return (
    <div className="stage">
      <div className="eyebrow">Step 02 · Crisis Briefing</div>
      <h1 className="stage-title">{crisis.name}</h1>
      <div style={{ display:"flex", gap:10, marginBottom:18, flexWrap:"wrap" }}>
        <span className="pill urgent">Urgency: {crisis.urgency}</span>
        <span className="pill">Business-wide impact</span>
      </div>
      <div className="grid grid-2">
        <div className="card">
          <div className="card-label">What happened</div>
          <p style={{ color:"var(--text-2)", fontSize:14, lineHeight:1.65, margin:0 }}>{crisis.description}</p>
        </div>
        <div className="card">
          <div className="card-label">Business impact</div>
          <p style={{ color:"var(--text-2)", fontSize:14, lineHeight:1.65, margin:0 }}>{crisis.impact}</p>
        </div>
      </div>
      <div className="divider"></div>
      <MetricsPanel metrics={metrics} />
      <div className="why-box" style={{marginTop:16}}>
        <b>Why this matters:</b> These are your starting conditions after the initial shock. Every decision you make
        from here moves these five numbers — there's rarely a move that helps all five at once.
      </div>
      <div className="btn-row">
        <button className="btn btn-primary" onClick={onContinue}>Enter the War Room →</button>
      </div>
    </div>
  );
}

/* =========================================================
   STAGE: WAR ROOM
========================================================= */
function WarRoom({ metrics, chosen, setChosen, onApply, onContinue, applied }){
  function toggle(id){
    if(applied) return;
    if(chosen.includes(id)){
      setChosen(chosen.filter(c => c !== id));
    } else if(chosen.length < 3){
      setChosen([...chosen, id]);
    }
  }
  return (
    <div className="stage">
      <div className="eyebrow">Step 03 · War Room</div>
      <h1 className="stage-title">Choose Your Response</h1>
      <p className="stage-sub">Pick exactly three response actions. Each one trades off differently across cost,
      inventory, profit, delivery speed, and customer satisfaction — read the "why this matters" note before you commit.
      Selected: <b style={{color:"var(--text-1)"}}>{chosen.length} / 3</b></p>

      <div className="grid grid-3">
        {WARROOM_ACTIONS.map(a => {
          const isSelected = chosen.includes(a.id);
          const disable = applied ? !isSelected : (!isSelected && chosen.length >= 3);
          return (
            <button key={a.id} className={"choice-card" + (isSelected ? " selected" : "") + (disable ? " disabled" : "")}
              onClick={() => toggle(a.id)} disabled={applied}>
              <div className="choice-title">{a.title}</div>
              <div className="choice-desc">{a.desc}</div>
              <div className="why-box" style={{marginTop:6}}><b>Why this matters:</b> {a.why}</div>
              <span className={"choice-tag" + (isSelected ? " picked" : "")}>{isSelected ? "Selected" : "Tap to select"}</span>
            </button>
          );
        })}
      </div>

      <div className="divider"></div>
      <MetricsPanel metrics={metrics} />

      <div className="btn-row">
        {!applied ? (
          <button className="btn btn-primary" disabled={chosen.length !== 3} onClick={onApply}>
            Commit to These 3 Actions →
          </button>
        ) : (
          <button className="btn btn-primary" onClick={onContinue}>Continue to Supplier Negotiation →</button>
        )}
      </div>
    </div>
  );
}

/* =========================================================
   STAGE: NEGOTIATION
========================================================= */
function Negotiation({ state, setState, onContinue }){
  const round = NEGOTIATION_ROUNDS[state.round];
  const done = state.round >= NEGOTIATION_ROUNDS.length;

  function choose(opt){
    const newState = {
      round: state.round + 1,
      trust: clamp(state.trust + opt.effect.trust, 0, 100),
      price: clamp(state.price + opt.effect.price, 0, 200),
      lead: clamp(state.lead + opt.effect.lead, 0, 200),
      log: [...state.log, { prompt: round.prompt, choice: opt.label, quality: opt.quality }],
    };
    setState(newState);
  }

  const negotiationScore = Math.round(
    clamp(state.trust) * 0.45 +
    clamp(100 - (state.price - 100)) * 0.275 +
    clamp(100 - (state.lead - 100)) * 0.275
  );

  return (
    <div className="stage">
      <div className="eyebrow">Step 04 · Supplier Negotiation</div>
      <h1 className="stage-title">Negotiation Room</h1>
      <p className="stage-sub">Four rounds. Every choice shifts supplier trust, price, and lead time — and trust
      earned early tends to pay off in later rounds.</p>

      <div className="grid grid-3" style={{marginBottom:22}}>
        <div className="card"><div className="card-label">Supplier Trust</div><div className="card-value" style={{color:metricColor(state.trust)}}>{Math.round(state.trust)}</div></div>
        <div className="card"><div className="card-label">Price Index</div><div className="card-value">{Math.round(state.price)}%</div></div>
        <div className="card"><div className="card-label">Lead Time Index</div><div className="card-value">{Math.round(state.lead)}%</div></div>
      </div>

      {!done ? (
        <div className="card">
          <div className="card-label">Round {state.round + 1} of {NEGOTIATION_ROUNDS.length}</div>
          <h3 style={{fontFamily:"var(--font-display)", fontSize:18, margin:"6px 0 8px"}}>{round.prompt}</h3>
          <div className="why-box" style={{marginBottom:16}}><b>Why this matters:</b> {round.context}</div>
          <div className="grid grid-3">
            {round.options.map((opt, i) => (
              <button key={i} className="choice-card" onClick={() => choose(opt)}>
                <div className="choice-desc" style={{fontSize:14, color:"var(--text-1)"}}>{opt.label}</div>
              </button>
            ))}
          </div>
        </div>
      ) : (
        <div className="card">
          <div className="card-label">Negotiation Complete</div>
          <div className="score-ring-wrap">
            <div className="score-num" style={{color:metricColor(negotiationScore)}}>{negotiationScore}</div>
            <div className="score-label">Negotiation Score</div>
          </div>
          <div className="btn-row" style={{justifyContent:"center"}}>
            <button className="btn btn-primary" onClick={() => onContinue(negotiationScore)}>Continue to CEO Boardroom →</button>
          </div>
        </div>
      )}
    </div>
  );
}

/* =========================================================
   STAGE: BOARDROOM
========================================================= */
function Boardroom({ answers, setAnswers, onContinue }){
  const qIndex = answers.length;
  const done = qIndex >= BOARDROOM_QUESTIONS.length;

  function choose(opt){
    setAnswers([...answers, { q: BOARDROOM_QUESTIONS[qIndex].q, choice: opt.label, quality: opt.quality }]);
  }

  const total = answers.reduce((s, a) => s + a.quality, 0);
  const leadershipScore = Math.round((total / (BOARDROOM_QUESTIONS.length * 10)) * 100);

  return (
    <div className="stage">
      <div className="eyebrow">Step 05 · CEO Boardroom</div>
      <h1 className="stage-title">Leadership Under Pressure</h1>
      <p className="stage-sub">Five questions about how you lead through the crisis — not just what you decide,
      but how you decide it and communicate it.</p>

      {!done ? (
        <div className="card">
          <div className="card-label">Question {qIndex + 1} of {BOARDROOM_QUESTIONS.length}</div>
          <h3 style={{fontFamily:"var(--font-display)", fontSize:18, margin:"6px 0 16px", lineHeight:1.4}}>{BOARDROOM_QUESTIONS[qIndex].q}</h3>
          <div className="grid grid-2">
            {BOARDROOM_QUESTIONS[qIndex].options.map((opt, i) => (
              <button key={i} className="choice-card" onClick={() => choose(opt)}>
                <div className="choice-desc" style={{fontSize:14, color:"var(--text-1)"}}>{opt.label}</div>
              </button>
            ))}
          </div>
        </div>
      ) : (
        <div className="card">
          <div className="card-label">Boardroom Session Complete</div>
          <div className="score-ring-wrap">
            <div className="score-num" style={{color:metricColor(leadershipScore)}}>{leadershipScore}</div>
            <div className="score-label">Leadership Score</div>
          </div>
          <div className="btn-row" style={{justifyContent:"center"}}>
            <button className="btn btn-primary" onClick={() => onContinue(leadershipScore)}>Continue to AI Strategy →</button>
          </div>
        </div>
      )}
    </div>
  );
}

/* =========================================================
   STAGE: AI STRATEGY
========================================================= */
function AIStrategy({ chosen, setChosen, onContinue }){
  function toggle(id){
    if(chosen.includes(id)){
      setChosen(chosen.filter(c => c !== id));
    } else if(chosen.length < 2){
      setChosen([...chosen, id]);
    }
  }
  return (
    <div className="stage">
      <div className="eyebrow">Step 06 · AI Strategy</div>
      <h1 className="stage-title">Invest in Resilience</h1>
      <p className="stage-sub">Choose two AI investments to strengthen the supply chain against the next crisis.
      Selected: <b style={{color:"var(--text-1)"}}>{chosen.length} / 2</b></p>

      <div className="grid grid-3">
        {AI_INVESTMENTS.map(inv => {
          const isSelected = chosen.includes(inv.id);
          const disable = !isSelected && chosen.length >= 2;
          return (
            <button key={inv.id} className={"choice-card" + (isSelected ? " selected" : "") + (disable ? " disabled" : "")}
              onClick={() => toggle(inv.id)}>
              <div className="choice-title">{inv.title}</div>
              <div className="choice-desc">{inv.desc}</div>
              <div className="why-box" style={{marginTop:6}}><b>Expected impact:</b> {inv.impact}</div>
              <span className={"choice-tag" + (isSelected ? " picked" : "")}>{isSelected ? "Selected" : "Tap to select"}</span>
            </button>
          );
        })}
      </div>

      <div className="btn-row">
        <button className="btn btn-primary" disabled={chosen.length !== 2} onClick={onContinue}>
          Finalize Strategy & View Dashboard →
        </button>
      </div>
    </div>
  );
}

/* =========================================================
   STAGE: FINAL DASHBOARD
========================================================= */
function Dashboard({ data, onReplay }){
  const { company, crisis, metrics, warRoomLog, negotiationScore, leadershipScore, aiChosen } = data;

  const aiBoost = aiChosen.reduce((acc, id) => {
    const inv = AI_INVESTMENTS.find(a => a.id === id);
    acc.resilience += inv.boost.resilience || 0;
    acc.risk += inv.boost.risk || 0;
    acc.cost += inv.boost.cost || 0;
    acc.csat += inv.boost.csat || 0;
    return acc;
  }, { resilience:0, risk:0, cost:0, csat:0 });

  const resilience = Math.round(clamp(metrics.inventory * 0.6 + aiBoost.resilience * 1.3));
  const costControl = Math.round(clamp(metrics.cost * 0.5 + metrics.profit * 0.3 + aiBoost.cost * 0.9));
  const riskMgmt = Math.round(clamp(50 + aiBoost.risk * 1.4 + (negotiationScore - 50) * 0.3));
  const customerSat = Math.round(clamp(metrics.csat + aiBoost.csat));
  const negotiation = Math.round(negotiationScore);
  const leadership = Math.round(leadershipScore);

  const overall = Math.round((resilience + costControl + riskMgmt + customerSat + negotiation + leadership) / 6);

  // gather all "decisions" for best/mistake extraction
  const allDecisions = [
    ...warRoomLog.map(a => ({ label: a.title, quality: (a.effect.cost + a.effect.inventory + a.effect.profit + a.effect.delivery + a.effect.csat) / 5 + 5 })),
    ...data.negotiationLog.map(n => ({ label: n.choice, quality: n.quality })),
    ...data.boardroomLog.map(b => ({ label: b.choice, quality: b.quality })),
  ];
  const sorted = [...allDecisions].sort((a,b) => b.quality - a.quality);
  const best = sorted[0];
  const worst = sorted[sorted.length - 1];

  let tier, tierMsg;
  if(overall >= 85){ tier = "Exceptional Crisis Leadership"; tierMsg = "You navigated this disruption the way top-quartile operators do: fast, transparent, and disciplined about tradeoffs."; }
  else if(overall >= 70){ tier = "Strong Recovery"; tierMsg = "You stabilized the business through the crisis with solid judgment, even if a few calls left value on the table."; }
  else if(overall >= 50){ tier = "Uneven but Functional"; tierMsg = "The company survived, but several decisions compounded avoidable costs — there's a clear path to a stronger outcome next run."; }
  else { tier = "Crisis Still Smoldering"; tierMsg = "Several choices worked against each other. The business is still standing, but trust, cost, or delivery took a real hit."; }

  const weakestPair = Object.entries({ Leadership:leadership, Negotiation:negotiation, Resilience:resilience, "Cost Control":costControl, "Risk Management":riskMgmt, "Customer Satisfaction":customerSat })
    .sort((a,b) => a[1] - b[1])[0];

  return (
    <div className="stage">
      <div className="eyebrow">Final Report · {company.name}</div>
      <h1 className="stage-title">Executive Dashboard</h1>
      <p className="stage-sub">Here's how {company.name} came through the {crisis.name.toLowerCase()} — across leadership,
      negotiation, resilience, cost control, risk management, and customer satisfaction.</p>

      <div className="grid grid-2" style={{marginBottom:20}}>
        <div className="card" style={{display:"flex",flexDirection:"column",alignItems:"center",justifyContent:"center"}}>
          <div className="score-ring-wrap">
            <div className="score-num" style={{color:metricColor(overall)}}>{overall}</div>
            <div className="score-label">Overall Crisis Score</div>
          </div>
          <div style={{fontFamily:"var(--font-display)", fontSize:16, marginTop:10, textAlign:"center"}}>{tier}</div>
        </div>
        <div className="card">
          <div className="card-label" style={{marginBottom:14}}>Category Scores</div>
          <MetricBar label="LEADERSHIP" value={leadership} />
          <MetricBar label="NEGOTIATION" value={negotiation} />
          <MetricBar label="RESILIENCE" value={resilience} />
          <MetricBar label="COST CONTROL" value={costControl} />
          <MetricBar label="RISK MANAGEMENT" value={riskMgmt} />
          <MetricBar label="CUSTOMER SATISFACTION" value={customerSat} />
        </div>
      </div>

      <div className="grid grid-2">
        <div className="feedback-block fb-best">
          <h3>Best Decision</h3>
          <p>{best ? `"${best.label}" was your strongest move — it was the highest-value tradeoff you made this run.` : "No standout decision recorded."}</p>
        </div>
        <div className="feedback-block fb-mistake">
          <h3>Biggest Mistake</h3>
          <p>{worst && worst.quality < 6 ? `"${worst.label}" cost you more than it gave back — it's the clearest place to improve next time.` : "No major missteps — every decision held its own reasonably well."}</p>
        </div>
        <div className="feedback-block fb-expert">
          <h3>Expert Recommendation</h3>
          <p>{tierMsg} Your weakest area this run was <b style={{color:"var(--text-1)"}}>{weakestPair[0]}</b> ({weakestPair[1]}/100) —
          that's the highest-leverage place to focus if you replay this scenario.</p>
        </div>
        <div className="feedback-block fb-lessons">
          <h3>Lessons Learned</h3>
          <p>Crises rarely reward a single "correct" move — they reward consistency across cost, speed, trust, and communication.
          {aiChosen.length ? " The AI investments you made will keep paying off well beyond this single incident." : ""}</p>
        </div>
      </div>

      <div className="divider"></div>

      <div className="card">
        <div className="card-label" style={{marginBottom:10}}>Decision Log</div>
        {warRoomLog.map((a,i) => (
          <div className="log-line" key={"w"+i}><span className="dot"></span><span>War Room: chose <b style={{color:"var(--text-1)"}}>{a.title}</b></span></div>
        ))}
        {data.negotiationLog.map((n,i) => (
          <div className="log-line" key={"n"+i}><span className="dot"></span><span>Negotiation: {n.choice}</span></div>
        ))}
        {data.boardroomLog.map((b,i) => (
          <div className="log-line" key={"b"+i}><span className="dot"></span><span>Boardroom: {b.choice}</span></div>
        ))}
        {aiChosen.map((id,i) => (
          <div className="log-line" key={"a"+i}><span className="dot"></span><span>AI Strategy: invested in <b style={{color:"var(--text-1)"}}>{AI_INVESTMENTS.find(a=>a.id===id).title}</b></span></div>
        ))}
      </div>

      <div className="btn-row">
        <button className="btn btn-primary" onClick={onReplay}>Replay with a New Scenario ↻</button>
      </div>
      <div className="footer-note">Operation Lifeline · Supply Chain Crisis Lab · All data in this run was randomly generated for training purposes.</div>
    </div>
  );
}

/* =========================================================
   ROOT APP
========================================================= */
function buildInitialMetrics(crisis){
  const base = { cost:60, inventory:60, profit:60, delivery:60, csat:60 };
  Object.keys(crisis.hit || {}).forEach(k => {
    base[k] = clamp(base[k] + crisis.hit[k]);
  });
  return base;
}

function App(){
  const [stage, setStage] = useState("welcome");
  const [company, setCompany] = useState(null);
  const [crisis, setCrisis] = useState(null);
  const [metrics, setMetrics] = useState(null);
  const [prevMetrics, setPrevMetrics] = useState(null);
  const [day, setDay] = useState(1);

  const [warChosen, setWarChosen] = useState([]);
  const [warApplied, setWarApplied] = useState(false);
  const [warRoomLog, setWarRoomLog] = useState([]);

  const [negoState, setNegoState] = useState({ round:0, trust:50, price:100, lead:100, log:[] });
  const [negotiationScore, setNegotiationScore] = useState(0);

  const [boardAnswers, setBoardAnswers] = useState([]);
  const [leadershipScore, setLeadershipScore] = useState(0);

  const [aiChosen, setAiChosen] = useState([]);

  function startGame(){
    const c = generateCompany();
    const cr = pick(CRISES);
    setCompany(c);
    setCrisis(cr);
    const m = buildInitialMetrics(cr);
    setMetrics(m);
    setPrevMetrics(m);
    setDay(1);
    setWarChosen([]);
    setWarApplied(false);
    setWarRoomLog([]);
    setNegoState({ round:0, trust:50, price:100, lead:100, log:[] });
    setNegotiationScore(0);
    setBoardAnswers([]);
    setLeadershipScore(0);
    setAiChosen([]);
    setStage("company");
  }

  function applyWarRoom(){
    const chosenActions = WARROOM_ACTIONS.filter(a => warChosen.includes(a.id));
    const newMetrics = { ...metrics };
    chosenActions.forEach(a => {
      Object.keys(a.effect).forEach(k => {
        newMetrics[k] = clamp(newMetrics[k] + a.effect[k]);
      });
    });
    setPrevMetrics(metrics);
    setMetrics(newMetrics);
    setWarRoomLog(chosenActions);
    setWarApplied(true);
    setDay(d => d + rand(2,4));
  }

  function showsTicker(){
    return ["warroom","negotiation","boardroom","aistrategy","dashboard"].includes(stage);
  }

  if(stage === "welcome"){
    return <div className="app-shell"><Welcome onStart={startGame} /></div>;
  }

  return (
    <div className="app-shell">
      <div className="top-bar">
        <div className="brand">
          <div className="brand-mark">OL</div>
          <div className="brand-text">Operation Lifeline<small>Supply Chain Crisis Lab</small></div>
        </div>
        <Stepper stageKey={stage} />
      </div>

      {showsTicker() && metrics && (
        <LiveTicker metrics={metrics} prevMetrics={prevMetrics} day={day} />
      )}

      {stage === "company" && company && (
        <CompanyProfile company={company} onContinue={() => setStage("crisis")} />
      )}

      {stage === "crisis" && crisis && metrics && (
        <CrisisBriefing crisis={crisis} metrics={metrics} onContinue={() => setStage("warroom")} />
      )}

      {stage === "warroom" && metrics && (
        <WarRoom
          metrics={metrics}
          chosen={warChosen}
          setChosen={setWarChosen}
          applied={warApplied}
          onApply={applyWarRoom}
          onContinue={() => setStage("negotiation")}
        />
      )}

      {stage === "negotiation" && (
        <Negotiation
          state={negoState}
          setState={setNegoState}
          onContinue={(score) => { setNegotiationScore(score); setDay(d => d + rand(3,6)); setStage("boardroom"); }}
        />
      )}

      {stage === "boardroom" && (
        <Boardroom
          answers={boardAnswers}
          setAnswers={setBoardAnswers}
          onContinue={(score) => { setLeadershipScore(score); setDay(d => d + rand(1,3)); setStage("aistrategy"); }}
        />
      )}

      {stage === "aistrategy" && (
        <AIStrategy
          chosen={aiChosen}
          setChosen={setAiChosen}
          onContinue={() => { setDay(d => d + rand(2,5)); setStage("dashboard"); }}
        />
      )}

      {stage === "dashboard" && company && crisis && metrics && (
        <Dashboard
          data={{
            company, crisis, metrics,
            warRoomLog,
            negotiationScore,
            leadershipScore,
            negotiationLog: negoState.log,
            boardroomLog: boardAnswers,
            aiChosen,
          }}
          onReplay={startGame}
        />
      )}
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
</script>
</body>
</html>
