:Prompt: 
You are an expert frontend developer, UX designer, game designer, and supply chain consultant.

Build a complete single-file HTML app named 'Supply Chain Builder'.

Design it so a complete beginner can understand supply chains. Before every decision, explain what the concept means, why it matters, and how it affects a business.

Requirements:

* Output ONLY one HTML file.
* React via CDN + Babel JSX.
* Plain HTML, CSS, and JavaScript only.
* No Tailwind, npm, backend, APIs, images, or external assets.
* Runs offline by opening the HTML file.
* No placeholders or incomplete features.

Flow:

1. Welcome screen introducing supply chains in simple language.
2. Generate a random company (industry, products, countries served, demand level).
3. Guide the player through building their supply chain by choosing:
   * Number of suppliers (single or multiple)
   * Factory location
   * Warehouse strategy
   * Transportation method (road, rail, sea, air)
   * Inventory strategy (low, balanced, high)
4. After every choice, explain the trade-offs in plain English.
5. Display live business metrics that update after each decision:
   * Cost
   * Delivery Speed
   * Risk
   * Customer Satisfaction
   * Sustainability
6. At the end, generate a dashboard with an Overall Supply Chain Score (0-100), strengths, weaknesses, biggest risk, and three practical improvements.


Design:

* Premium enterprise dashboard.
* Dark theme.
* Responsive.
* Smooth transitions.
* Rounded cards.
* Hover effects.
* Animated progress bars.
* Replay button.

Randomize company details each playthrough. Organize the app into reusable React components using useState. Ensure every button works and return ONLY the complete HTML inside one code block.
:Response:
You are an expert frontend developer, UX designer, game designer, and supply chain consultant.
Build a complete single-file HTML app named 'Supply Chain Builder'.
Design it so a complete beginner can understand supply chains. Before every decision, explain what the concept means, why it matters, and how it affects a business.
Requirements:
* Output ONLY one HTML file.
* React via CDN + Babel JSX.
* Plain HTML, CSS, and JavaScript only.
* No Tailwind, npm, backend, APIs, images, or external assets.
* Runs offline by opening the HTML file.
* No placeholders or incomplete features.
Flow:
1. Welcome screen introducing supply chains in simple language.
2. Generate a random company (industry, products, countries served, demand level).
3. Guide the player through building their supply chain by choosing:
   * Number of suppliers (single or multiple)
   * Factory location
   * Warehouse strategy
   * Transportation method (road, rail, sea, air)
   * Inventory strategy (low, balanced, high)
4. After every choice, explain the trade-offs in plain English.
5. Display live business metrics that update after each decision:
   * Cost
   * Delivery Speed
   * Risk
   * Customer Satisfaction
   * Sustainability
6. At the end, generate a dashboard with an Overall Supply Chain Score (0-100), strengths, weaknesses, biggest risk, and three practical improvements.
Design:
* Premium enterprise dashboard.
* Dark theme.
* Responsive.
* Smooth transitions.
* Rounded cards.
* Hover effects.
* Animated progress bars.
* Replay button.
Randomize company details each playthrough. Organize the app into reusable React components using useState. Ensure every button works and return ONLY the complete HTML inside one code block.
You are an expert frontend developer, UX designer, game designer, and supply chain consultant.
Build a complete single-file HTML app named 'Supply Chain Builder'.
Design it so a complete beginner can understand supply chains. Before every decision, explain what the concept means, why it matters, and how it affects a business.
Requirements:
* Output ONLY one HTML file.
* React via CDN + Babel JSX.
* Plain HTML, CSS, and JavaScript only.
* No Tailwind, npm, backend, APIs, images, or external assets.
* Runs offline by opening the HTML file.
* No placeholders or incomplete features.
Flow:
1. Welcome screen introducing supply chains in simple language.
2. Generate a random company (industry, products, countries served, demand level).
3. Guide the player through building their supply chain by choosing:
   * Number of suppliers (single or multiple)
   * Factory location
   * Warehouse strategy
   * Transportation method (road, rail, sea, air)
   * Inventory strategy (low, balanced, high)
4. After every choice, explain the trade-offs in plain English.
5. Display live business metrics that update after each decision:
   * Cost
   * Delivery Speed
   * Risk
   * Customer Satisfaction
   * Sustainability
6. At the end, generate a dashboard with an Overall Supply Chain Score (0-100), strengths, weaknesses, biggest risk, and three practical improvements.
Design:
* Premium enterprise dashboard.
* Dark theme.
* Responsive.
* Smooth transitions.
* Rounded cards.
* Hover effects.
* Animated progress bars.
* Repl<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Supply Chain Builder</title>
<style>
  :root{
    --void:#080B12;
    --panel:#0F1420;
    --panel-raised:#161D2C;
    --panel-hover:#1D2638;
    --border:#232D40;
    --border-bright:#34415C;
    --primary:#7C86FF;
    --primary-dim:#333972;
    --teal:#2DD9B9;
    --teal-dim:#155A4C;
    --rose:#FB4D6B;
    --rose-dim:#5A1F2C;
    --amber:#F2B84B;
    --amber-dim:#5C4818;
    --text-1:#EDF1F9;
    --text-2:#98A2BE;
    --text-3:#57607A;
    --font-display:'Segoe UI Semibold','Helvetica Neue',Arial,sans-serif;
    --font-body:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
    --font-mono:'SF Mono','Cascadia Code','Consolas','Courier New',monospace;
  }
  *{box-sizing:border-box;}
  html,body{margin:0;padding:0;}
  body{
    background:
      radial-gradient(circle at 10% 0%, rgba(124,134,255,0.08), transparent 42%),
      radial-gradient(circle at 90% 100%, rgba(45,217,185,0.06), transparent 45%),
      var(--void);
    color:var(--text-1);
    font-family:var(--font-body);
    min-height:100vh;
    -webkit-font-smoothing:antialiased;
  }
  #root{min-height:100vh;display:flex;flex-direction:column;}
  ::selection{background:var(--primary);color:#0a0d16;}
  ::-webkit-scrollbar{width:10px;height:10px;}
  ::-webkit-scrollbar-track{background:var(--void);}
  ::-webkit-scrollbar-thumb{background:var(--border-bright);border-radius:8px;}
  button{font-family:inherit;cursor:pointer;}
  button:focus-visible, a:focus-visible{outline:2px solid var(--primary);outline-offset:2px;}
  @media (prefers-reduced-motion: reduce){*{animation-duration:0.01ms !important;transition-duration:0.01ms !important;}}

  .app-shell{max-width:1180px;margin:0 auto;padding:24px 20px 80px;width:100%;flex:1;display:flex;flex-direction:column;}

  .top-bar{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:18px;flex-wrap:wrap;}
  .brand{display:flex;align-items:center;gap:10px;}
  .brand-mark{width:34px;height:34px;border-radius:9px;background:linear-gradient(135deg,var(--primary),#4d57c9);display:flex;align-items:center;justify-content:center;font-family:var(--font-display);font-weight:800;color:#0a0d16;font-size:14px;flex-shrink:0;}
  .brand-text{font-family:var(--font-display);font-weight:700;letter-spacing:0.3px;font-size:15px;}
  .brand-text small{display:block;color:var(--text-3);font-weight:500;font-size:10.5px;letter-spacing:1.4px;text-transform:uppercase;margin-top:1px;}

  .progress-count{font-family:var(--font-mono);font-size:11.5px;color:var(--text-3);background:var(--panel);border:1px solid var(--border);padding:6px 12px;border-radius:999px;}

  /* ---------- Chain Map (signature element) ---------- */
  .chainmap-wrap{
    position:sticky;top:0;z-index:40;background:rgba(8,11,18,0.92);backdrop-filter:blur(6px);
    border:1px solid var(--border);border-radius:14px;margin-bottom:22px;padding:16px 18px 12px;
    box-shadow:0 8px 24px rgba(0,0,0,0.35);
  }
  .chainmap-title{font-family:var(--font-mono);font-size:10px;letter-spacing:1.6px;text-transform:uppercase;color:var(--text-3);margin-bottom:12px;}
  .chainmap-row{display:flex;align-items:center;}
  .chain-node{display:flex;flex-direction:column;align-items:center;gap:6px;flex-shrink:0;width:96px;}
  .chain-dot{width:34px;height:34px;border-radius:50%;background:var(--panel-raised);border:2px solid var(--border);display:flex;align-items:center;justify-content:center;font-size:14px;transition:all .5s ease;color:var(--text-3);}
  .chain-dot.done{border-color:var(--teal);background:var(--teal-dim);color:var(--teal);box-shadow:0 0 0 4px rgba(45,217,185,0.12);}
  .chain-dot.active{border-color:var(--primary);background:var(--primary-dim);color:var(--primary);animation:node-pulse 1.6s infinite;}
  @keyframes node-pulse{0%,100%{box-shadow:0 0 0 0 rgba(124,134,255,0.35);}50%{box-shadow:0 0 0 8px rgba(124,134,255,0);}}
  .chain-label{font-size:10.5px;color:var(--text-3);text-align:center;font-family:var(--font-mono);letter-spacing:0.3px;}
  .chain-label.done{color:var(--teal);}
  .chain-label.active{color:var(--text-1);}
  .chain-line{flex:1;height:2px;background:var(--border);margin:0 -2px;position:relative;top:-15px;transition:background .5s ease;}
  .chain-line.done{background:var(--teal);}

  .stage{animation:fadeUp .5s ease both;}
  @keyframes fadeUp{from{opacity:0;transform:translateY(10px);}to{opacity:1;transform:translateY(0);}}

  .eyebrow{font-family:var(--font-mono);font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--primary);margin:0 0 8px;}
  h1.stage-title{font-family:var(--font-display);font-size:clamp(24px,4vw,36px);margin:0 0 10px;line-height:1.1;letter-spacing:-0.5px;}
  p.stage-sub{color:var(--text-2);font-size:15px;line-height:1.6;max-width:760px;margin:0 0 24px;}

  .grid{display:grid;gap:16px;}
  .grid-2{grid-template-columns:repeat(2,1fr);}
  .grid-3{grid-template-columns:repeat(3,1fr);}
  .grid-4{grid-template-columns:repeat(4,1fr);}
  @media (max-width:860px){.grid-2,.grid-3,.grid-4{grid-template-columns:1fr;}}

  .card{
    background:linear-gradient(180deg,var(--panel),rgba(15,20,32,0.6));
    border:1px solid var(--border);border-radius:16px;padding:20px;
    transition:border-color .25s ease, transform .25s ease, box-shadow .25s ease;
  }
  .card.hoverable:hover{border-color:var(--border-bright);transform:translateY(-2px);box-shadow:0 10px 30px rgba(0,0,0,0.3);}
  .card-label{font-family:var(--font-mono);font-size:10.5px;letter-spacing:1.4px;text-transform:uppercase;color:var(--text-3);margin-bottom:6px;}
  .card-value{font-family:var(--font-display);font-size:22px;font-weight:700;}
  .card-value.small{font-size:16px;}

  .concept-box{
    background:rgba(124,134,255,0.07);border:1px solid var(--primary-dim);border-left:3px solid var(--primary);
    border-radius:10px;padding:16px 18px;margin-bottom:22px;
  }
  .concept-box .k{font-family:var(--font-mono);font-size:10.5px;letter-spacing:1.4px;text-transform:uppercase;color:var(--primary);margin-bottom:6px;}
  .concept-box p{margin:0 0 8px;color:var(--text-2);font-size:13.5px;line-height:1.65;}
  .concept-box p:last-child{margin-bottom:0;}
  .concept-box b{color:var(--text-1);}

  .tradeoff-box{
    background:rgba(45,217,185,0.06);border:1px solid var(--teal-dim);border-left:3px solid var(--teal);
    border-radius:10px;padding:14px 16px;margin-top:16px;font-size:13.5px;color:var(--text-2);line-height:1.6;
  }
  .tradeoff-box b{color:var(--teal);}

  .btn{
    font-family:var(--font-display);font-weight:600;font-size:14px;border-radius:10px;padding:13px 22px;
    border:1px solid var(--border-bright);background:var(--panel-raised);color:var(--text-1);
    transition:all .2s ease;display:inline-flex;align-items:center;gap:8px;
  }
  .btn:hover{background:var(--panel-hover);border-color:var(--text-3);}
  .btn-primary{background:linear-gradient(135deg,var(--primary),#5b64d9);border-color:transparent;color:#fff;}
  .btn-primary:hover{filter:brightness(1.1);transform:translateY(-1px);box-shadow:0 8px 20px rgba(124,134,255,0.28);}
  .btn-primary:disabled{opacity:0.4;cursor:not-allowed;transform:none;box-shadow:none;filter:none;}
  .btn-row{display:flex;gap:12px;margin-top:26px;flex-wrap:wrap;}

  .metric-row{margin-bottom:16px;}
  .metric-top{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px;}
  .metric-name{font-size:12.5px;color:var(--text-2);font-family:var(--font-mono);letter-spacing:0.5px;}
  .metric-num{font-family:var(--font-mono);font-size:13px;font-weight:600;}
  .bar-track{height:9px;border-radius:999px;background:var(--border);overflow:hidden;}
  .bar-fill{height:100%;border-radius:999px;transition:width 1.1s cubic-bezier(.22,1,.36,1);}

  .choice-card{
    text-align:left;width:100%;background:var(--panel);border:1px solid var(--border);border-radius:14px;
    padding:18px;transition:all .2s ease;display:flex;flex-direction:column;gap:8px;
  }
  .choice-card:hover{border-color:var(--primary);background:var(--panel-raised);transform:translateY(-2px);}
  .choice-card.selected{border-color:var(--teal);background:rgba(45,217,185,0.07);}
  .choice-card.disabled{opacity:0.4;pointer-events:none;}
  .choice-title{font-family:var(--font-display);font-size:15.5px;font-weight:700;}
  .choice-desc{font-size:13px;color:var(--text-2);line-height:1.5;}
  .choice-tag{display:inline-flex;align-self:flex-start;font-family:var(--font-mono);font-size:10px;letter-spacing:1px;text-transform:uppercase;padding:3px 8px;border-radius:6px;background:var(--border);color:var(--text-3);margin-top:4px;}
  .choice-tag.picked{background:var(--teal-dim);color:var(--teal);}

  .pill{display:inline-flex;align-items:center;gap:6px;font-family:var(--font-mono);font-size:11px;padding:5px 10px;border-radius:999px;background:var(--panel-raised);border:1px solid var(--border);color:var(--text-2);}

  .divider{height:1px;background:var(--border);margin:26px 0;}

  .score-ring-wrap{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:10px;}
  .score-num{font-family:var(--font-display);font-size:52px;font-weight:800;line-height:1;}
  .score-label{font-family:var(--font-mono);font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--text-3);margin-top:8px;}

  .feedback-block{background:var(--panel);border:1px solid var(--border);border-radius:14px;padding:18px;margin-bottom:14px;}
  .feedback-block h3{margin:0 0 8px;font-family:var(--font-display);font-size:14.5px;letter-spacing:0.3px;}
  .feedback-block p, .feedback-block li{margin:0;color:var(--text-2);font-size:13.5px;line-height:1.65;}
  .feedback-block ul{margin:0;padding-left:18px;}
  .feedback-block li{margin-bottom:6px;}
  .fb-strength{border-left:3px solid var(--teal);}
  .fb-weakness{border-left:3px solid var(--rose);}
  .fb-risk{border-left:3px solid var(--amber);}
  .fb-improve{border-left:3px solid var(--primary);}

  .log-line{display:flex;gap:10px;font-size:12.5px;padding:8px 0;border-bottom:1px solid var(--border);color:var(--text-2);}
  .log-line:last-child{border-bottom:none;}
  .log-line .dot{width:6px;height:6px;border-radius:50%;background:var(--primary);margin-top:5px;flex-shrink:0;}

  .welcome-hero{min-height:70vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:40px 16px;position:relative;}
  .welcome-hero .glyph{font-family:var(--font-mono);font-size:12px;letter-spacing:3px;color:var(--primary);text-transform:uppercase;margin-bottom:18px;border:1px solid var(--primary-dim);padding:6px 14px;border-radius:999px;background:rgba(124,134,255,0.07);}
  .welcome-hero h1{font-family:var(--font-display);font-size:clamp(32px,6vw,54px);line-height:1.05;letter-spacing:-1px;margin:0 0 16px;max-width:800px;}
  .welcome-hero h1 span{color:var(--primary);}
  .welcome-hero p{color:var(--text-2);font-size:16px;max-width:620px;line-height:1.65;margin:0 0 20px;}
  .welcome-explain{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;max-width:820px;margin:14px 0 34px;width:100%;}
  @media (max-width:760px){.welcome-explain{grid-template-columns:1fr;}}
  .welcome-explain .card{text-align:left;}
  .pulse-ring{position:absolute;width:340px;height:340px;border:1px solid var(--border);border-radius:50%;opacity:0.4;animation:ring-grow 4s ease-out infinite;}
  @keyframes ring-grow{0%{transform:scale(0.6);opacity:0.5;}100%{transform:scale(1.4);opacity:0;}}

  .footer-note{text-align:center;color:var(--text-3);font-size:11.5px;margin-top:40px;font-family:var(--font-mono);}
</style>
</head>
<body>
<div id="root"></div>

<script src="https://unpkg.com/react@18/umd/react.development.js"></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

<script type="text/babel" data-presets="react">
const { useState } = React;

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
function metricColor(v){
  if(v >= 70) return "var(--teal)";
  if(v >= 45) return "var(--amber)";
  return "var(--rose)";
}

/* =========================================================
   COMPANY GENERATION
========================================================= */
const INDUSTRIES = [
  { industry:"Consumer Electronics", products:"wireless earbuds and smart home gadgets" },
  { industry:"Apparel & Footwear", products:"everyday sneakers and outdoor jackets" },
  { industry:"Food & Beverage", products:"packaged snacks and cold-pressed juices" },
  { industry:"Furniture", products:"flat-pack furniture and home decor" },
  { industry:"Beauty & Personal Care", products:"skincare and haircare products" },
  { industry:"Toys & Games", products:"educational toys and board games" },
  { industry:"Sporting Goods", products:"fitness equipment and outdoor gear" },
];
const NAME_ROOTS = ["Nova","Meridian","Solstice","Vantex","Cobalt","Anchor","Summit","Falcon","Redwood","Halcyon","Aurelia","Ridgeline","Kestrel","Larkspur","Brightwell","Northfield"];
const NAME_SUFFIXES = ["Goods","Co.","Collective","Brands","& Sons","Supply Co.","Studio","Works","Group","Trading Co."];
const COUNTRIES = ["the United States","Canada","the United Kingdom","Germany","France","Japan","Australia","Brazil","South Korea","India","Mexico","the Netherlands"];
const DEMAND_LEVELS = [
  { level:"Steady", note:"Demand is predictable and grows slowly quarter over quarter." },
  { level:"Seasonal Spikes", note:"Demand surges sharply around a few key periods each year." },
  { level:"Rapid Growth", note:"Demand is climbing fast as the brand gains popularity." },
];

function generateCompany(){
  const ind = pick(INDUSTRIES);
  const name = `${pick(NAME_ROOTS)} ${pick(NAME_SUFFIXES)}`;
  const countries = pickN(COUNTRIES, rand(2,4));
  const demand = pick(DEMAND_LEVELS);
  return { name, industry:ind.industry, products:ind.products, countries, demand };
}

/* =========================================================
   DECISION DATA
   Every decision includes a concept explainer (shown before choosing)
   and each option includes a plain-English tradeoff (shown after choosing).
========================================================= */
const DECISIONS = [
  {
    id:"suppliers",
    label:"Suppliers",
    title:"How Many Suppliers Should You Use?",
    concept:"A supplier is a company you buy raw materials, parts, or products from. This is the very first link in your supply chain — nothing else can happen until materials arrive.",
    why:"The number of suppliers you rely on changes how exposed you are to a single problem. Relying on one supplier is simple, but if anything goes wrong with them — a strike, a bankruptcy, a bad batch — your entire operation can stall.",
    options:[
      { id:"single", title:"Single Supplier", desc:"Work with one trusted supplier for your key materials.",
        effect:{ cost:12, delivery:6, risk:-18, csat:2, sustain:6 },
        tradeoff:"A single supplier is easier to manage and usually gets you better pricing through a closer relationship — but it's a single point of failure. If that one supplier has a problem, your whole supply chain feels it immediately." },
      { id:"multi", title:"Multiple Suppliers", desc:"Split sourcing across two or more suppliers.",
        effect:{ cost:-8, delivery:-2, risk:18, csat:4, sustain:-4 },
        tradeoff:"Spreading purchases across suppliers protects you if one fails — but it costs more to manage multiple relationships, and you lose some of the pricing power that comes with buying in bulk from one place." },
    ]
  },
  {
    id:"factory",
    label:"Factory",
    title:"Where Should Your Factory Be Located?",
    concept:"Factory location is where your products actually get made or assembled. Distance from your factory to your customers directly affects both cost and speed.",
    why:"Manufacturing close to home (domestic) tends to be faster and easier to inspect, but more expensive. Manufacturing far away (offshore) is usually cheaper on labor, but adds weeks of shipping time and more risk along the way.",
    options:[
      { id:"domestic", title:"Domestic Factory", desc:"Manufacture in the same country you sell in.",
        effect:{ cost:-14, delivery:20, risk:10, csat:10, sustain:12 },
        tradeoff:"Domestic manufacturing gives you fast, reliable delivery and easier quality control — but domestic labor and facility costs are usually higher, which eats into your margins." },
      { id:"nearshore", title:"Nearshore Factory", desc:"Manufacture in a nearby country, a short flight or drive away.",
        effect:{ cost:0, delivery:6, risk:2, csat:2, sustain:2 },
        tradeoff:"Nearshoring is a balanced middle ground — moderate costs, reasonably fast shipping, and easier oversight than manufacturing on the other side of the world." },
      { id:"offshore", title:"Offshore Factory", desc:"Manufacture overseas where labor costs are lower.",
        effect:{ cost:18, delivery:-20, risk:-12, csat:-8, sustain:-14 },
        tradeoff:"Offshoring usually cuts your production costs significantly — but long ocean transit adds weeks to delivery, and you're more exposed to port delays, customs issues, and currency swings." },
    ]
  },
  {
    id:"warehouse",
    label:"Warehousing",
    title:"How Should You Store Inventory?",
    concept:"A warehouse strategy is how — and where — you store finished products before they reach customers. This is the buffer between 'made' and 'delivered.'",
    why:"Centralizing storage in one big warehouse is efficient, but every order has to travel farther. Spreading storage across many regional warehouses gets products closer to customers, at the cost of running more facilities.",
    options:[
      { id:"centralized", title:"One Central Warehouse", desc:"Store everything in a single large warehouse.",
        effect:{ cost:14, delivery:-10, risk:-6, csat:-4, sustain:4 },
        tradeoff:"A single warehouse is cheaper to run and easier to manage — but every shipment travels farther on average, slowing delivery, and a disruption there affects your entire country or region at once." },
      { id:"regional", title:"Regional Warehouses", desc:"Store inventory across several smaller warehouses near customers.",
        effect:{ cost:-12, delivery:18, risk:8, csat:12, sustain:-8 },
        tradeoff:"Regional warehouses get products to customers much faster and reduce the impact if one location has an issue — but running multiple facilities costs more and uses more energy overall." },
      { id:"jit", title:"Just-In-Time (Minimal Storage)", desc:"Keep very little stock on hand; produce closer to when it's needed.",
        effect:{ cost:16, delivery:-4, risk:-16, csat:-6, sustain:14 },
        tradeoff:"Just-in-time storage keeps costs low and reduces waste since you're not sitting on excess stock — but it leaves almost no cushion if demand spikes or a shipment is delayed, so stockouts become a real risk." },
    ]
  },
  {
    id:"transport",
    label:"Transport",
    title:"How Should You Ship Your Products?",
    concept:"Transportation is how goods physically move between suppliers, factories, warehouses, and customers. Each mode trades speed against cost and environmental impact differently.",
    why:"Air is fast but expensive and carbon-heavy. Sea is cheap but slow. Road and rail sit in between, each with their own strengths depending on distance and geography.",
    options:[
      { id:"road", title:"Road Freight", desc:"Move goods by truck across regional or national distances.",
        effect:{ cost:0, delivery:6, risk:2, csat:2, sustain:-2 },
        tradeoff:"Road freight is flexible and reasonably fast for shorter distances, but it doesn't scale efficiently over very long distances and can be affected by traffic, fuel prices, and driver shortages." },
      { id:"rail", title:"Rail Freight", desc:"Move large volumes overland by train.",
        effect:{ cost:8, delivery:-4, risk:4, csat:-2, sustain:16 },
        tradeoff:"Rail is one of the most fuel-efficient ways to move large volumes over land, and fairly reliable — but it's slower than road or air and only works well where rail infrastructure already exists." },
      { id:"sea", title:"Sea Freight", desc:"Move large volumes overseas by container ship.",
        effect:{ cost:16, delivery:-20, risk:-8, csat:-8, sustain:6 },
        tradeoff:"Sea freight is by far the cheapest way to move large volumes internationally, and reasonably fuel-efficient per unit — but it's slow, and vulnerable to port congestion, strikes, and weather delays." },
      { id:"air", title:"Air Freight", desc:"Move goods quickly by cargo plane.",
        effect:{ cost:-20, delivery:22, risk:6, csat:10, sustain:-18 },
        tradeoff:"Air freight is by far the fastest option and keeps deliveries reliable even under pressure — but it's the most expensive mode by a wide margin, and has the largest carbon footprint per shipment." },
    ]
  },
  {
    id:"inventory",
    label:"Inventory",
    title:"How Much Inventory Should You Keep?",
    concept:"Inventory strategy is how much extra stock you keep on hand as a buffer against uncertainty — whether that's a demand spike or a delayed shipment.",
    why:"Holding a lot of inventory protects you from running out, but ties up cash and warehouse space in products that might not sell right away. Holding very little keeps things lean, but leaves you exposed if anything unexpected happens.",
    options:[
      { id:"low", title:"Low Inventory", desc:"Keep minimal buffer stock; restock frequently.",
        effect:{ cost:14, delivery:-6, risk:-14, csat:-8, sustain:8 },
        tradeoff:"Low inventory frees up cash and reduces waste from unsold stock — but you're one delayed shipment or demand spike away from a stockout that frustrates customers." },
      { id:"balanced", title:"Balanced Inventory", desc:"Keep a moderate buffer sized to typical demand.",
        effect:{ cost:0, delivery:2, risk:6, csat:6, sustain:0 },
        tradeoff:"A balanced approach covers normal fluctuations in demand without tying up excessive cash — it won't fully protect you from a major spike, but it handles day-to-day variability well." },
      { id:"high", title:"High Inventory", desc:"Keep a large buffer stock at all times.",
        effect:{ cost:-16, delivery:10, risk:14, csat:10, sustain:-12 },
        tradeoff:"High inventory makes you very resilient to demand spikes and delays, and keeps products consistently in stock — but it ties up significant cash in storage and increases waste if products go unsold or become outdated." },
    ]
  },
];

/* =========================================================
   REUSABLE COMPONENTS
========================================================= */
function ChainMap({ activeIndex }){
  const nodes = ["Suppliers","Factory","Warehouse","Transport","Inventory","Result"];
  return (
    <div className="chainmap-wrap">
      <div className="chainmap-title">Your Supply Chain</div>
      <div className="chainmap-row">
        {nodes.map((n, i) => (
          <React.Fragment key={n}>
            <div className="chain-node">
              <div className={"chain-dot " + (i < activeIndex ? "done" : i === activeIndex ? "active" : "")}>
                {i < activeIndex ? "✓" : i + 1}
              </div>
              <div className={"chain-label " + (i < activeIndex ? "done" : i === activeIndex ? "active" : "")}>{n}</div>
            </div>
            {i < nodes.length - 1 && <div className={"chain-line " + (i < activeIndex ? "done" : "")}></div>}
          </React.Fragment>
        ))}
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
      <MetricBar label="COST EFFICIENCY" value={metrics.cost} />
      <MetricBar label="DELIVERY SPEED" value={metrics.delivery} />
      <MetricBar label="RISK MANAGEMENT" value={metrics.risk} />
      <MetricBar label="CUSTOMER SATISFACTION" value={metrics.csat} />
      <MetricBar label="SUSTAINABILITY" value={metrics.sustain} />
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
      <div className="glyph">Learn by Building</div>
      <h1>Supply Chain <span>Builder</span></h1>
      <p>A supply chain is simply every step it takes to get a product from raw materials into a customer's hands —
      suppliers, factories, warehouses, transportation, and inventory. Every choice along the way is a tradeoff.
      You'll build one from scratch, decision by decision, and see exactly how it affects cost, speed, risk,
      customers, and sustainability.</p>
      <div className="welcome-explain">
        <div className="card">
          <div className="card-label">No experience needed</div>
          <div style={{fontSize:13.5, color:"var(--text-2)", lineHeight:1.6}}>Every decision starts with a plain-English explanation before you choose anything.</div>
        </div>
        <div className="card">
          <div className="card-label">See real tradeoffs</div>
          <div style={{fontSize:13.5, color:"var(--text-2)", lineHeight:1.6}}>Watch five live business metrics shift in real time as you build.</div>
        </div>
        <div className="card">
          <div className="card-label">A new run each time</div>
          <div style={{fontSize:13.5, color:"var(--text-2)", lineHeight:1.6}}>Your company, products, and markets are randomized every playthrough.</div>
        </div>
      </div>
      <button className="btn btn-primary" onClick={onStart}>Start Building →</button>
      <div className="footer-note">Operation: Supply Chain Builder · a hands-on introduction to supply chain strategy</div>
    </div>
  );
}

/* =========================================================
   STAGE: COMPANY PROFILE
========================================================= */
function CompanyProfile({ company, onContinue }){
  return (
    <div className="stage">
      <div className="eyebrow">Step 01 · Your Company</div>
      <h1 className="stage-title">Meet {company.name}</h1>
      <p className="stage-sub">This is the company whose supply chain you're about to design. Every decision from here
      on should be made with this business in mind — its products, its markets, and how demand behaves for it.</p>
      <div className="grid grid-4">
        <div className="card hoverable"><div className="card-label">Industry</div><div className="card-value small">{company.industry}</div></div>
        <div className="card hoverable" style={{gridColumn:"span 2"}}><div className="card-label">Products</div><div className="card-value small">{company.products}</div></div>
        <div className="card hoverable"><div className="card-label">Demand Pattern</div><div className="card-value small">{company.demand.level}</div></div>
        <div className="card hoverable" style={{gridColumn:"span 4"}}>
          <div className="card-label">Markets Served</div>
          <div className="card-value small">{company.countries.join(", ")}</div>
        </div>
      </div>
      <div className="concept-box" style={{marginTop:20}}>
        <div className="k">Why this matters</div>
        <p><b>{company.demand.note}</b> The shape of demand changes which supply chain choices make sense — a business
        with sudden spikes needs more flexibility built in than one with slow, steady growth.</p>
      </div>
      <div className="btn-row">
        <button className="btn btn-primary" onClick={onContinue}>Start Building the Supply Chain →</button>
      </div>
    </div>
  );
}

/* =========================================================
   STAGE: FINAL DASHBOARD
========================================================= */
function Dashboard({ company, metrics, choiceLog, onReplay }){
  const overall = Math.round((metrics.cost + metrics.delivery + metrics.risk + metrics.csat + metrics.sustain) / 5);

  const labeled = [
    { key:"Cost Efficiency", value: metrics.cost },
    { key:"Delivery Speed", value: metrics.delivery },
    { key:"Risk Management", value: metrics.risk },
    { key:"Customer Satisfaction", value: metrics.csat },
    { key:"Sustainability", value: metrics.sustain },
  ];
  const strengths = labeled.filter(m => m.value >= 65).sort((a,b) => b.value - a.value);
  const weaknesses = labeled.filter(m => m.value < 45).sort((a,b) => a.value - b.value);
  const biggestRisk = [...labeled].sort((a,b) => a.value - b.value)[0];

  let tier, tierMsg;
  if(overall >= 80){ tier = "Well-Architected Supply Chain"; tierMsg = "Your choices reinforced each other well — this is close to how experienced supply chain leaders balance cost, speed, and resilience."; }
  else if(overall >= 60){ tier = "Solid, With Room to Tighten"; tierMsg = "This is a workable supply chain with a couple of soft spots worth revisiting."; }
  else if(overall >= 40){ tier = "Stretched Thin"; tierMsg = "Several choices pulled in different directions, leaving real gaps in how this supply chain would perform under pressure."; }
  else { tier = "High-Risk Configuration"; tierMsg = "This combination of choices creates serious exposure — in a real business, this setup would struggle the moment something went wrong."; }

  const improvements = [];
  if(metrics.risk < 55) improvements.push("Diversify suppliers or add a backup source to reduce single-point-of-failure risk.");
  if(metrics.delivery < 55) improvements.push("Move storage or transportation closer to your customers to cut delivery time.");
  if(metrics.cost < 55) improvements.push("Revisit your highest-cost decision (factory location or transport mode) for a cheaper alternative.");
  if(metrics.csat < 55) improvements.push("Increase inventory buffer or delivery speed — stockouts and slow shipping hurt customer satisfaction the most.");
  if(metrics.sustain < 55) improvements.push("Shift toward lower-emission transport (rail or sea) or reduce unnecessary warehouse footprint.");
  while(improvements.length < 3){
    improvements.push("Revisit your lowest-scoring metric above and try a different choice on your next run.");
  }

  return (
    <div className="stage">
      <div className="eyebrow">Final Report · {company.name}</div>
      <h1 className="stage-title">Your Supply Chain Dashboard</h1>
      <p className="stage-sub">Here's how the supply chain you built for {company.name} performs across the five metrics
      that matter most in the real world.</p>

      <div className="grid grid-2" style={{marginBottom:20}}>
        <div className="card" style={{display:"flex",flexDirection:"column",alignItems:"center",justifyContent:"center"}}>
          <div className="score-ring-wrap">
            <div className="score-num" style={{color:metricColor(overall)}}>{overall}</div>
            <div className="score-label">Overall Supply Chain Score</div>
          </div>
          <div style={{fontFamily:"var(--font-display)", fontSize:16, marginTop:10, textAlign:"center"}}>{tier}</div>
        </div>
        <div className="card">
          <div className="card-label" style={{marginBottom:14}}>Metric Breakdown</div>
          <MetricBar label="COST EFFICIENCY" value={metrics.cost} />
          <MetricBar label="DELIVERY SPEED" value={metrics.delivery} />
          <MetricBar label="RISK MANAGEMENT" value={metrics.risk} />
          <MetricBar label="CUSTOMER SATISFACTION" value={metrics.csat} />
          <MetricBar label="SUSTAINABILITY" value={metrics.sustain} />
        </div>
      </div>

      <div className="grid grid-2">
        <div className="feedback-block fb-strength">
          <h3>Strengths</h3>
          {strengths.length ? (
            <ul>{strengths.map(s => <li key={s.key}>{s.key} ({Math.round(s.value)}/100)</li>)}</ul>
          ) : <p>No standout strengths yet — most metrics are sitting in the middle of the range.</p>}
        </div>
        <div className="feedback-block fb-weakness">
          <h3>Weaknesses</h3>
          {weaknesses.length ? (
            <ul>{weaknesses.map(s => <li key={s.key}>{s.key} ({Math.round(s.value)}/100)</li>)}</ul>
          ) : <p>No serious weak points — every metric is holding up reasonably well.</p>}
        </div>
        <div className="feedback-block fb-risk">
          <h3>Biggest Risk</h3>
          <p><b style={{color:"var(--text-1)"}}>{biggestRisk.key}</b> is your lowest-scoring metric at {Math.round(biggestRisk.value)}/100.
          {tierMsg} That's the area most likely to cause problems first if this supply chain were tested by a real disruption.</p>
        </div>
        <div className="feedback-block fb-improve">
          <h3>Three Practical Improvements</h3>
          <ul>{improvements.slice(0,3).map((imp,i) => <li key={i}>{imp}</li>)}</ul>
        </div>
      </div>

      <div className="divider"></div>

      <div className="card">
        <div className="card-label" style={{marginBottom:10}}>Your Decisions</div>
        {choiceLog.map((c,i) => (
          <div className="log-line" key={i}><span className="dot"></span><span><b style={{color:"var(--text-1)"}}>{c.decisionLabel}:</b> {c.title}</span></div>
        ))}
      </div>

      <div className="btn-row">
        <button className="btn btn-primary" onClick={onReplay}>Build a New Supply Chain ↻</button>
      </div>
      <div className="footer-note">Supply Chain Builder · a hands-on learning tool · All company data in this run was randomly generated.</div>
    </div>
  );
}

/* =========================================================
   ROOT APP
========================================================= */
function baseMetrics(){
  return { cost:50, delivery:50, risk:50, csat:50, sustain:50 };
}

function App(){
  const [stage, setStage] = useState("welcome"); // welcome | company | decision | dashboard
  const [company, setCompany] = useState(null);
  const [metrics, setMetrics] = useState(baseMetrics());
  const [decisionIndex, setDecisionIndex] = useState(0);
  const [chosenOption, setChosenOption] = useState(null);
  const [choiceLog, setChoiceLog] = useState([]);

  function startGame(){
    setCompany(generateCompany());
    setMetrics(baseMetrics());
    setDecisionIndex(0);
    setChosenOption(null);
    setChoiceLog([]);
    setStage("company");
  }

  function beginDecisions(){
    setStage("decision");
  }

  function chooseOption(opt){
    const decision = DECISIONS[decisionIndex];
    const newMetrics = { ...metrics };
    Object.keys(opt.effect).forEach(k => {
      newMetrics[k] = clamp(newMetrics[k] + opt.effect[k]);
    });
    setMetrics(newMetrics);
    setChosenOption(opt);
    setChoiceLog([...choiceLog, { decisionLabel: decision.label, title: opt.title }]);
  }

  function nextDecision(){
    if(decisionIndex < DECISIONS.length - 1){
      setDecisionIndex(decisionIndex + 1);
      setChosenOption(null);
    } else {
      setStage("dashboard");
    }
  }

  const chainActiveIndex = stage === "welcome" ? -1
    : stage === "company" ? 0
    : stage === "decision" ? decisionIndex
    : DECISIONS.length;

  if(stage === "welcome"){
    return <div className="app-shell"><Welcome onStart={startGame} /></div>;
  }

  return (
    <div className="app-shell">
      <div className="top-bar">
        <div className="brand">
          <div className="brand-mark">SC</div>
          <div className="brand-text">Supply Chain Builder<small>Learn by building, decision by decision</small></div>
        </div>
        {stage === "decision" && (
          <div className="progress-count">Decision {decisionIndex + 1} of {DECISIONS.length}</div>
        )}
      </div>

      {stage !== "company" && <ChainMap activeIndex={chainActiveIndex} />}

      {stage === "company" && company && (
        <React.Fragment>
          <ChainMap activeIndex={0} />
          <CompanyProfile company={company} onContinue={beginDecisions} />
        </React.Fragment>
      )}

      {stage === "decision" && (
        <div>
          <div className="eyebrow">Step {decisionIndex + 2} · {DECISIONS[decisionIndex].label}</div>
          <h1 className="stage-title">{DECISIONS[decisionIndex].title}</h1>

          <div className="concept-box">
            <div className="k">What this means</div>
            <p>{DECISIONS[decisionIndex].concept}</p>
            <div className="k" style={{marginTop:10}}>Why it matters</div>
            <p>{DECISIONS[decisionIndex].why}</p>
          </div>

          <div className={"grid " + (DECISIONS[decisionIndex].options.length === 4 ? "grid-4" : DECISIONS[decisionIndex].options.length === 3 ? "grid-3" : "grid-2")}>
            {DECISIONS[decisionIndex].options.map(opt => {
              const isSelected = chosenOption && chosenOption.id === opt.id;
              const disabled = chosenOption && !isSelected;
              return (
                <button key={opt.id} className={"choice-card" + (isSelected ? " selected" : "") + (disabled ? " disabled" : "")}
                  onClick={() => chooseOption(opt)} disabled={!!chosenOption}>
                  <div className="choice-title">{opt.title}</div>
                  <div className="choice-desc">{opt.desc}</div>
                  <span className={"choice-tag" + (isSelected ? " picked" : "")}>{isSelected ? "Selected" : "Tap to choose"}</span>
                </button>
              );
            })}
          </div>

          {chosenOption && (
            <div className="tradeoff-box"><b>In plain English:</b> {chosenOption.tradeoff}</div>
          )}

          <div className="divider"></div>
          <MetricsPanel metrics={metrics} />

          {chosenOption && (
            <div className="btn-row">
              <button className="btn btn-primary" onClick={nextDecision}>
                {decisionIndex < DECISIONS.length - 1 ? "Continue to Next Decision →" : "View Final Dashboard →"}
              </button>
            </div>
          )}
        </div>
      )}

      {stage === "dashboard" && company && (
        <Dashboard company={company} metrics={metrics} choiceLog={choiceLog} onReplay={startGame} />
      )}
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
</script>
</body>
</html>
ay button.
Randomize company details each playthrough. Organize the app into reusable React components using useState. Ensure every button works and return ONLY the complete HTML inside one code block.
Open it in your browser to play — every decision (suppliers, factory, warehouse, transport, inventory) explains the concept and why it matters before you choose, then shows the plain-English tradeoff after, while the sticky Chain Map and live metrics update as you go
[supply-chain-builder.html](https://github.com/user-attachments/files/29646926/supply-chain-builder.html)
