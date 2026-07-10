:Prompt: 
Create a single-file offline web app called 'Cognitive Pattern Explorer' using only HTML, CSS, and vanilla JavaScript (no frameworks). Combine HTML, CSS, and JS into one responsive file.

Purpose:
Build a psychology-inspired self-reflection experience that explores thinking patterns through interactive scenarios. It must feel calm, game-like, and exploratory rather than like a test.

This is educational only. Never diagnose or clinically assess mental health. Use reflective language ('you often...', 'this suggests...') instead of absolute labels.

Thinking Tendencies:
- Analytical Thinker
- Emotional Intuitive
- Overthinking Loop Style
- Action-First Decision Maker
- Balanced Reflective Thinker

Flow:
1. Start Screen with Calm/Stress Mode.
2. Chapter 1 – Discover Your Thinking Style.
3. Chapter 2 – Choose Your Priorities using draggable cards.
4. Chapter 3 – Map Your Thinking using draggable timelines.
5. Final Reflection Journal with personalized insights and percentage breakdown.

Design:
- Calm modern aesthetic.
- Smooth transitions.
- Progress indicators.
- Responsive layout.
- Ambient animations.
- Keyboard accessibility.
- Reduced motion support.

Technical Requirements:
- Single HTML file.
- Vanilla JavaScript only.
- Native drag-and-drop with touch fallback.
- Works completely offline.
- Store all scenarios as JavaScript objects.
- Reuse drag-and-drop components.
- Verify there are no syntax errors, scoring works, progress tracking works, and the layout is responsive.

Return only one complete HTML file.

:Response:
JS syntax checks out. The app is complete and fully self-contained (no external fonts/CDNs, works offline).Presented filePresented fileBuilt as one offline file — calm sage/clay palette, serif display type, three chapters (scenario picks, drag-to-rank priority cards, drag-to-timeline stage mapping), then a journal screen with animated percentage bars and reflective (non-diagnostic) insights. Drag-and-drop works via native HTML5 DnD plus a touch-event fallback that clones a floating "ghost" element, and every draggable is also keyboard-operable (Enter/Space to place, focus-visible outlines throughout). Progress bar and step label update at each chapter, prefers-reduced-motion disables ambient drift and softens transitions, and Quick Mode shortens all transition durations for a snappier feel.
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cognitive Pattern Explorer</title>
<style>
  :root{
    --bg-0:#f3f1ea;
    --bg-1:#eae6da;
    --ink-0:#2b2b26;
    --ink-1:#5b5850;
    --moss:#6f8a72;
    --moss-dark:#526455;
    --clay:#b98a63;
    --sky:#7c94a8;
    --lav:#9a8bab;
    --sun:#c9a24b;
    --card-bg:#fffdf7;
    --line:#d9d3c2;
    --radius:18px;
    --shadow: 0 10px 30px -14px rgba(43,43,38,0.25);
    --dur-1:420ms;
    --dur-2:680ms;
    --ease: cubic-bezier(.22,.61,.36,1);
    --focus: 3px solid #4d6b9b;
  }
  [data-mode="stress"]{
    --bg-0:#efece3;
    --bg-1:#e5e0d1;
    --dur-1:200ms;
    --dur-2:280ms;
  }
  *,*::before,*::after{ box-sizing:border-box; }
  html,body{ height:100%; }
  body{
    margin:0;
    font-family: "Iowan Old Style","Palatino Linotype",Palatino,Georgia,"Times New Roman",serif;
    background: radial-gradient(1200px 800px at 20% -10%, var(--bg-1), var(--bg-0) 60%);
    color: var(--ink-0);
    min-height:100vh;
    overflow-x:hidden;
    -webkit-font-smoothing:antialiased;
  }
  .label-font{ font-family: "Avenir Next","Segoe UI",system-ui,-apple-system,sans-serif; }

  /* ambient background motion */
  .ambient{
    position:fixed; inset:0; z-index:0; pointer-events:none; overflow:hidden;
  }
  .ambient span{
    position:absolute; border-radius:50%;
    background: radial-gradient(circle at 30% 30%, rgba(111,138,114,0.18), rgba(111,138,114,0) 70%);
    filter: blur(2px);
    animation: drift 24s ease-in-out infinite;
  }
  .ambient span:nth-child(1){ width:420px; height:420px; top:-100px; left:-80px; animation-duration:28s; }
  .ambient span:nth-child(2){ width:300px; height:300px; bottom:-60px; right:-40px; background:radial-gradient(circle at 30% 30%, rgba(154,139,171,0.16), rgba(154,139,171,0) 70%); animation-duration:32s; }
  .ambient span:nth-child(3){ width:220px; height:220px; top:40%; right:10%; background:radial-gradient(circle at 30% 30%, rgba(124,148,168,0.14), rgba(124,148,168,0) 70%); animation-duration:26s; }
  @keyframes drift{
    0%,100%{ transform: translate(0,0) scale(1); }
    50%{ transform: translate(30px,-20px) scale(1.08); }
  }
  @media (prefers-reduced-motion: reduce){
    .ambient span{ animation: none !important; }
  }

  #app{ position:relative; z-index:1; min-height:100vh; display:flex; flex-direction:column; }

  header.top-bar{
    display:flex; align-items:center; justify-content:space-between;
    padding: 18px clamp(16px,4vw,48px);
    gap:16px;
  }
  .brand{
    display:flex; align-items:center; gap:10px;
    font-family: "Avenir Next","Segoe UI",system-ui,sans-serif;
    letter-spacing:.04em;
    font-weight:600;
    color:var(--moss-dark);
    font-size:.95rem;
  }
  .brand .dot{ width:10px;height:10px;border-radius:50%; background: var(--moss); box-shadow:0 0 0 4px rgba(111,138,114,.18); }

  .progress-track{
    flex:1; max-width:420px; height:6px; border-radius:99px; background:var(--line);
    overflow:hidden; margin:0 12px;
  }
  .progress-fill{
    height:100%; width:0%; border-radius:99px;
    background: linear-gradient(90deg, var(--moss), var(--sky));
    transition: width var(--dur-2) var(--ease);
  }
  .step-count{ font-family:"Avenir Next","Segoe UI",system-ui,sans-serif; font-size:.8rem; color:var(--ink-1); white-space:nowrap; }

  main{ flex:1; display:flex; flex-direction:column; align-items:center; padding: 8px clamp(16px,5vw,48px) 60px; }

  .screen{
    width:100%; max-width:920px;
    opacity:0; transform: translateY(14px);
    animation: rise var(--dur-2) var(--ease) forwards;
  }
  @keyframes rise{ to{ opacity:1; transform:translateY(0); } }
  @media (prefers-reduced-motion: reduce){
    .screen{ animation: fadeonly var(--dur-1) linear forwards; }
  }
  @keyframes fadeonly{ to{ opacity:1; transform:none; } }

  h1.title{
    font-size: clamp(2rem, 5vw, 3.2rem);
    line-height:1.05;
    margin: 10px 0 6px;
    font-weight:600;
    color: var(--ink-0);
  }
  p.sub{
    font-family:"Avenir Next","Segoe UI",system-ui,sans-serif;
    color: var(--ink-1);
    font-size:1.05rem;
    max-width:56ch;
    margin: 0 0 28px;
    line-height:1.6;
  }
  .eyebrow{
    font-family:"Avenir Next","Segoe UI",system-ui,sans-serif;
    text-transform:uppercase; letter-spacing:.14em; font-size:.72rem;
    color: var(--moss-dark); font-weight:700; margin-bottom:10px; display:block;
  }

  /* Buttons */
  button{ font-family: inherit; cursor:pointer; }
  .btn{
    font-family:"Avenir Next","Segoe UI",system-ui,sans-serif;
    border:none; border-radius: 99px;
    padding: 14px 28px;
    font-size:1rem; font-weight:600;
    background: var(--ink-0); color: var(--bg-0);
    transition: transform var(--dur-1) var(--ease), box-shadow var(--dur-1) var(--ease);
    box-shadow: var(--shadow);
  }
  .btn:hover{ transform: translateY(-2px); }
  .btn:active{ transform: translateY(0px) scale(.98); }
  .btn:focus-visible{ outline: var(--focus); outline-offset:3px; }
  .btn.secondary{
    background: transparent; color: var(--ink-0);
    border: 1.5px solid var(--line);
    box-shadow:none;
  }
  .btn.ghost{
    background:transparent; color:var(--moss-dark); box-shadow:none;
    padding: 10px 16px;
  }
  .btn:disabled{ opacity:.45; cursor:not-allowed; transform:none; }

  /* Mode toggle */
  .mode-toggle{
    display:inline-flex; background: var(--card-bg); border:1px solid var(--line);
    border-radius:99px; padding:4px; gap:4px; margin: 18px 0 30px;
  }
  .mode-toggle button{
    font-family:"Avenir Next","Segoe UI",system-ui,sans-serif;
    border:none; background:transparent; border-radius:99px;
    padding: 9px 18px; font-size:.88rem; color:var(--ink-1); font-weight:600;
    transition: background var(--dur-1) var(--ease), color var(--dur-1) var(--ease);
  }
  .mode-toggle button[aria-pressed="true"]{ background: var(--moss); color:#fff; }
  .mode-toggle button:focus-visible{ outline: var(--focus); outline-offset:2px; }

  .start-card{
    background: var(--card-bg); border-radius: var(--radius); box-shadow: var(--shadow);
    padding: clamp(24px,5vw,48px); border:1px solid var(--line);
  }
  .chapter-preview-list{ list-style:none; padding:0; margin: 22px 0 0; display:grid; gap:10px; }
  .chapter-preview-list li{
    display:flex; align-items:center; gap:12px;
    font-family:"Avenir Next","Segoe UI",system-ui,sans-serif;
    font-size:.92rem; color:var(--ink-1);
    padding: 10px 14px; border-radius:12px; background: var(--bg-1);
  }
  .chapter-preview-list .num{
    width:26px;height:26px;border-radius:50%; background:#fff; border:1px solid var(--line);
    display:flex; align-items:center; justify-content:center; font-size:.78rem; font-weight:700; color:var(--moss-dark);
    flex-shrink:0;
  }

  /* Chapter shell */
  .chapter-head{ margin-bottom: 22px; }

  .card{
    background: var(--card-bg); border-radius: var(--radius); border:1px solid var(--line);
    box-shadow: var(--shadow); padding: clamp(20px,4vw,36px);
  }

  /* Scenario (Chapter 1) */
  .scenario-prompt{
    font-size: clamp(1.15rem, 2.4vw, 1.5rem); line-height:1.5; margin:0 0 22px; font-weight:500;
  }
  .options{ display:grid; gap:12px; }
  .option-btn{
    text-align:left; background: var(--bg-1); border: 1.5px solid transparent;
    border-radius:14px; padding:16px 18px; font-size:1rem; color:var(--ink-0);
    font-family:"Avenir Next","Segoe UI",system-ui,sans-serif; line-height:1.45;
    transition: border-color var(--dur-1) var(--ease), background var(--dur-1) var(--ease), transform var(--dur-1) var(--ease);
    display:flex; align-items:flex-start; gap:12px;
  }
  .option-btn .marker{
    width:20px;height:20px;border-radius:50%; border:2px solid var(--line); flex-shrink:0; margin-top:2px;
    transition: border-color var(--dur-1), background var(--dur-1);
  }
  .option-btn:hover{ border-color: var(--moss); transform: translateX(2px); }
  .option-btn:focus-visible{ outline: var(--focus); outline-offset:2px; }
  .option-btn.selected{ border-color: var(--moss); background:#eef3ec; }
  .option-btn.selected .marker{ background: var(--moss); border-color:var(--moss); }

  .nav-row{ display:flex; justify-content:space-between; align-items:center; margin-top:26px; gap:12px; flex-wrap:wrap; }

  /* Drag cards - Chapter 2 */
  .rank-layout{ display:grid; grid-template-columns: 1fr; gap: 26px; }
  @media(min-width:760px){ .rank-layout{ grid-template-columns: 1.1fr 1fr; } }
  .pool, .ranks{ min-height: 60px; }
  .zone-label{ font-family:"Avenir Next","Segoe UI",system-ui,sans-serif; font-size:.8rem; text-transform:uppercase; letter-spacing:.1em; color:var(--ink-1); margin-bottom:10px; display:block; font-weight:700; }
  .drag-list{ list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:10px; min-height: 64px; }
  .drop-slot{
    border: 1.5px dashed var(--line); border-radius:14px; min-height:58px;
    display:flex; align-items:center; padding: 0 14px; color: var(--ink-1);
    font-family:"Avenir Next","Segoe UI",system-ui,sans-serif; font-size:.85rem;
    transition: border-color var(--dur-1), background var(--dur-1);
  }
  .drop-slot .slot-idx{ font-weight:700; color:var(--moss-dark); margin-right:10px; }
  .drop-slot.drag-over{ border-color: var(--moss); background: #eef3ec; }
  .drop-slot.filled{ border-style:solid; padding:0; }

  .drag-card{
    background:#fff; border:1.5px solid var(--line); border-radius:12px;
    padding:12px 14px; font-family:"Avenir Next","Segoe UI",system-ui,sans-serif;
    font-size:.92rem; display:flex; align-items:center; gap:10px; cursor:grab;
    user-select:none; touch-action:none;
    box-shadow: 0 4px 10px -6px rgba(0,0,0,.18);
    transition: box-shadow var(--dur-1), transform var(--dur-1), opacity var(--dur-1);
    width:100%;
  }
  .drag-card:active{ cursor:grabbing; }
  .drag-card:focus-visible{ outline: var(--focus); outline-offset:2px; }
  .drag-card .grip{ color:var(--line); font-size:1.1rem; line-height:1; }
  .drag-card.dragging{ opacity:.35; }
  .drag-card.floating{
    position:fixed; z-index:999; pointer-events:none; box-shadow: 0 14px 30px -10px rgba(0,0,0,.35);
    width: var(--float-w, 240px);
  }
  .drag-card .tag{
    margin-left:auto; font-size:.7rem; color:var(--ink-1); background:var(--bg-1);
    padding:3px 8px; border-radius:99px;
  }

  .hint-text{ font-family:"Avenir Next","Segoe UI",system-ui,sans-serif; font-size:.85rem; color:var(--ink-1); margin: 4px 0 18px; }

  /* Timeline - Chapter 3 */
  .timeline-wrap{ position:relative; padding-top: 10px; }
  .timeline-track{
    position:relative; border-radius:16px; background: var(--bg-1); padding: 18px;
    display:flex; flex-direction:column; gap:10px;
  }
  .timeline-slot{
    display:flex; align-items:center; gap:14px; min-height:64px;
    border: 1.5px dashed var(--line); border-radius:14px; padding: 8px 14px;
    background: rgba(255,255,255,.5);
    transition: border-color var(--dur-1), background var(--dur-1);
  }
  .timeline-slot.drag-over{ border-color: var(--sky); background:#eef2f5; }
  .timeline-slot .stage-label{
    font-family:"Avenir Next","Segoe UI",system-ui,sans-serif; font-size:.72rem; color: var(--ink-1);
    text-transform:uppercase; letter-spacing:.08em; width:78px; flex-shrink:0;
  }
  .timeline-slot.filled{ border-style:solid; background:#fff; }

  .pill-pool{ display:flex; flex-wrap:wrap; gap:10px; margin-top:18px; }
  .drag-pill{
    background:#fff; border:1.5px solid var(--line); border-radius:99px;
    padding:10px 16px; font-family:"Avenir Next","Segoe UI",system-ui,sans-serif; font-size:.88rem;
    cursor:grab; user-select:none; touch-action:none;
    box-shadow: 0 4px 10px -6px rgba(0,0,0,.18);
    transition: opacity var(--dur-1), box-shadow var(--dur-1);
  }
  .drag-pill:focus-visible{ outline: var(--focus); outline-offset:2px; }
  .drag-pill.dragging{ opacity:.35; }
  .drag-pill.floating{ position:fixed; z-index:999; pointer-events:none; box-shadow: 0 14px 30px -10px rgba(0,0,0,.35); }

  /* Journal / results */
  .result-header{ text-align:center; margin-bottom: 30px; }
  .breakdown{ display:grid; gap:14px; margin: 22px 0 30px; }
  .bar-row{ display:grid; grid-template-columns: 170px 1fr 52px; align-items:center; gap:12px; }
  .bar-row .name{ font-family:"Avenir Next","Segoe UI",system-ui,sans-serif; font-size:.9rem; font-weight:600; color: var(--ink-0); }
  .bar-track{ background: var(--bg-1); border-radius:99px; height:12px; overflow:hidden; }
  .bar-fill{ height:100%; border-radius:99px; width:0%; transition: width 900ms var(--ease); }
  .bar-row .pct{ font-family:"Avenir Next","Segoe UI",system-ui,sans-serif; font-size:.85rem; color:var(--ink-1); text-align:right; }

  .insight-block{
    background: var(--bg-1); border-radius:16px; padding: 22px 24px; margin-bottom:18px;
  }
  .insight-block h3{ margin:0 0 8px; font-size:1.2rem; color:var(--moss-dark); }
  .insight-block p{ margin:0; line-height:1.65; color: var(--ink-0); font-size:1rem; }

  .journal-area label{ display:block; font-family:"Avenir Next","Segoe UI",system-ui,sans-serif; font-size:.85rem; color:var(--ink-1); margin-bottom:8px; font-weight:600; }
  textarea#journalNotes{
    width:100%; min-height:120px; border-radius:14px; border:1.5px solid var(--line);
    padding:14px 16px; font-family: inherit; font-size:1rem; resize:vertical;
    background: #fffdf9; color: var(--ink-0);
  }
  textarea#journalNotes:focus-visible{ outline: var(--focus); outline-offset:2px; }

  .sr-only{
    position:absolute; width:1px;height:1px; padding:0;margin:-1px;overflow:hidden;
    clip:rect(0,0,0,0); white-space:nowrap; border:0;
  }
  .live-status{ font-family:"Avenir Next","Segoe UI",system-ui,sans-serif; font-size:.82rem; color: var(--moss-dark); min-height:1.2em; margin-top:10px; }

  footer.appfoot{
    text-align:center; padding: 18px; font-family:"Avenir Next","Segoe UI",system-ui,sans-serif;
    font-size:.75rem; color: var(--ink-1);
  }

  @media (max-width:600px){
    .bar-row{ grid-template-columns: 108px 1fr 40px; }
    header.top-bar{ flex-wrap:wrap; }
    .progress-track{ order:3; width:100%; max-width:none; margin: 6px 0 0; }
  }
</style>
</head>
<body data-mode="calm">
<div class="ambient" aria-hidden="true"><span></span><span></span><span></span></div>
<div id="app">
  <header class="top-bar">
    <div class="brand"><span class="dot"></span> Cognitive Pattern Explorer</div>
    <div class="progress-track" role="progressbar" aria-label="Overall progress" aria-valuemin="0" aria-valuemax="100" id="progressBar" aria-valuenow="0">
      <div class="progress-fill" id="progressFill"></div>
    </div>
    <div class="step-count label-font" id="stepCount">Start</div>
  </header>

  <main id="main"></main>

  <footer class="appfoot">A reflective, educational exploration — not a clinical assessment.</footer>
</div>

<div class="sr-only" aria-live="polite" id="liveRegion"></div>

<script>
(function(){
  "use strict";

  /* ---------------------------------------------------------
     DATA
  --------------------------------------------------------- */
  var TENDENCIES = {
    analytical: { name: "Analytical Thinker", color: "#7c94a8",
      blurb: "You tend to slow down, gather evidence, and reason through options step by step before committing. Structure and clarity help you feel grounded." },
    emotional: { name: "Emotional Intuitive", color: "#9a8bab",
      blurb: "You often lead with how something feels before you explain why. Your instincts pick up on nuance quickly, and emotional signals guide your first read of a situation." },
    overthinking: { name: "Overthinking Loop Style", color: "#c9a24b",
      blurb: "You may notice yourself revisiting the same decision from different angles, searching for certainty. This suggests a deep care for getting things right — sometimes at the cost of momentum." },
    action: { name: "Action-First Decision Maker", color: "#b98a63",
      blurb: "You tend to move quickly once a direction feels reasonable, preferring to learn by doing rather than waiting for a perfect plan." },
    balanced: { name: "Balanced Reflective Thinker", color: "#6f8a72",
      blurb: "You often weigh logic and feeling together, adjusting your pace to the situation rather than defaulting to one mode. This suggests flexibility across different kinds of decisions." }
  };

  var CH1_QUESTIONS = [
    {
      prompt: "A close friend asks for advice about leaving their job. What's your first instinct?",
      options: [
        { text: "Ask about the practical details — savings, timeline, backup plan.", scores:{analytical:2} },
        { text: "Ask how they've been feeling about it lately.", scores:{emotional:2} },
        { text: "Wonder about every possible outcome before saying anything.", scores:{overthinking:2} },
        { text: "Tell them to trust their gut and go for it.", scores:{action:2} },
        { text: "Ask a few questions, then offer a mix of pros, cons, and encouragement.", scores:{balanced:2} }
      ]
    },
    {
      prompt: "You receive unexpected, slightly critical feedback on something you made.",
      options: [
        { text: "You look for the specific, factual points you can act on.", scores:{analytical:2} },
        { text: "You feel it first — a wave of reaction before you can think clearly.", scores:{emotional:2} },
        { text: "You replay the feedback for hours, imagining different meanings.", scores:{overthinking:2} },
        { text: "You make a quick fix and move on to the next thing.", scores:{action:2} },
        { text: "You sit with the feeling briefly, then look at it objectively.", scores:{balanced:2} }
      ]
    },
    {
      prompt: "You're choosing between two very different paths and neither is clearly 'better'.",
      options: [
        { text: "You make a pros-and-cons list to compare them properly.", scores:{analytical:2} },
        { text: "You imagine how each choice would feel a year from now.", scores:{emotional:2} },
        { text: "You keep gathering more information, hoping for total certainty.", scores:{overthinking:2} },
        { text: "You pick the one that feels right in the moment and adjust later.", scores:{action:2} },
        { text: "You give yourself a short deadline, weigh both, then decide.", scores:{balanced:2} }
      ]
    },
    {
      prompt: "A plan falls apart at the last minute. What happens next?",
      options: [
        { text: "You start mapping out a new, logical sequence of steps.", scores:{analytical:2} },
        { text: "You notice frustration or worry rising before anything else.", scores:{emotional:2} },
        { text: "You mentally rehearse what went wrong, again and again.", scores:{overthinking:2} },
        { text: "You improvise something new almost immediately.", scores:{action:2} },
        { text: "You pause, take stock, then calmly figure out next steps.", scores:{balanced:2} }
      ]
    },
    {
      prompt: "When learning something completely new, you prefer to...",
      options: [
        { text: "Read the manual or theory first, then apply it.", scores:{analytical:2} },
        { text: "Follow your curiosity wherever it feels most alive.", scores:{emotional:2} },
        { text: "Research extensively before ever starting, just in case.", scores:{overthinking:2} },
        { text: "Jump in and learn through trial and error.", scores:{action:2} },
        { text: "Skim the basics, then learn more as questions come up.", scores:{balanced:2} }
      ]
    }
  ];

  var PRIORITY_CARDS = [
    { id:"logic", label:"Logic & Evidence", tag:"clarity", tendency:"analytical" },
    { id:"gut", label:"Gut Feeling", tag:"instinct", tendency:"emotional" },
    { id:"certainty", label:"Getting It Just Right", tag:"precision", tendency:"overthinking" },
    { id:"speed", label:"Taking Action Fast", tag:"momentum", tendency:"action" },
    { id:"harmony", label:"Weighing All Sides", tag:"balance", tendency:"balanced" }
  ];

  var TIMELINE_STAGES = ["1st","2nd","3rd","4th","5th"];
  var TIMELINE_STEPS = [
    { id:"notice", label:"Notice the situation", tendency:null },
    { id:"feel", label:"Feel a reaction", tendency:"emotional" },
    { id:"analyze", label:"Analyze the options", tendency:"analytical" },
    { id:"decide", label:"Decide and act", tendency:"action" },
    { id:"reflect", label:"Reflect afterward", tendency:"balanced" }
  ];

  /* ---------------------------------------------------------
     STATE
  --------------------------------------------------------- */
  var state = {
    mode: "calm",
    step: 0, // 0 start, 1 ch1, 2 ch2, 3 ch3, 4 results
    ch1Answers: new Array(CH1_QUESTIONS.length).fill(null),
    ch1Index: 0,
    scores: { analytical:0, emotional:0, overthinking:0, action:0, balanced:0 },
    ch2Order: [], // array of card ids in ranked order (index0 = rank1)
    ch3Order: [], // array of step ids placed in timeline order
    ch3Reorders: 0
  };

  var TOTAL_STEPS = 4; // ch1, ch2, ch3, results (start not counted)

  var main = document.getElementById("main");
  var liveRegion = document.getElementById("liveRegion");
  var progressFill = document.getElementById("progressFill");
  var progressBar = document.getElementById("progressBar");
  var stepCount = document.getElementById("stepCount");

  function announce(msg){ liveRegion.textContent = msg; }

  function setProgress(){
    var pct = Math.round((state.step / TOTAL_STEPS) * 100);
    progressFill.style.width = pct + "%";
    progressBar.setAttribute("aria-valuenow", String(pct));
    var labels = ["Start","Chapter 1 of 3","Chapter 2 of 3","Chapter 3 of 3","Your Journal"];
    stepCount.textContent = labels[state.step];
  }

  function addScores(obj){
    Object.keys(obj).forEach(function(k){
      state.scores[k] = (state.scores[k] || 0) + obj[k];
    });
  }

  /* ---------------------------------------------------------
     RENDER HELPERS
  --------------------------------------------------------- */
  function clearMain(){ main.innerHTML = ""; }

  function el(tag, opts){
    opts = opts || {};
    var e = document.createElement(tag);
    if(opts.className) e.className = opts.className;
    if(opts.text) e.textContent = opts.text;
    if(opts.html) e.innerHTML = opts.html;
    if(opts.attrs){ Object.keys(opts.attrs).forEach(function(k){ e.setAttribute(k, opts.attrs[k]); }); }
    return e;
  }

  /* ---------------------------------------------------------
     SCREEN: START
  --------------------------------------------------------- */
  function renderStart(){
    clearMain();
    var wrap = el("div", { className:"screen" });

    var card = el("div", { className:"start-card" });
    card.appendChild(el("span", { className:"eyebrow", text:"A calm, exploratory self-reflection" }));
    card.appendChild(el("h1", { className:"title", text:"Cognitive Pattern Explorer" }));
    card.appendChild(el("p", { className:"sub", text:"Wander through three short chapters of scenarios, choices, and gentle mapping exercises. At the end, you'll receive a personalized reflection on your thinking tendencies — not a diagnosis, just a mirror." }));

    var modeLabel = el("span", { className:"eyebrow", text:"Choose your pace" });
    card.appendChild(modeLabel);
    var toggle = el("div", { className:"mode-toggle", attrs:{ role:"group", "aria-label":"Select experience pace" } });
    var calmBtn = el("button", { text:"Calm Mode", attrs:{ type:"button", "aria-pressed": state.mode==="calm" ? "true":"false" } });
    var stressBtn = el("button", { text:"Quick Mode", attrs:{ type:"button", "aria-pressed": state.mode==="stress" ? "true":"false" } });
    calmBtn.addEventListener("click", function(){ setMode("calm"); calmBtn.setAttribute("aria-pressed","true"); stressBtn.setAttribute("aria-pressed","false"); });
    stressBtn.addEventListener("click", function(){ setMode("stress"); stressBtn.setAttribute("aria-pressed","true"); calmBtn.setAttribute("aria-pressed","false"); });
    toggle.appendChild(calmBtn); toggle.appendChild(stressBtn);
    card.appendChild(toggle);

    var list = el("ul", { className:"chapter-preview-list" });
    var previews = [
      "Discover your thinking style through short scenarios",
      "Choose your priorities using draggable cards",
      "Map your natural decision timeline",
      "Receive your personalized reflection journal"
    ];
    previews.forEach(function(p, i){
      var li = document.createElement("li");
      var num = el("span", { className:"num", text: String(i+1) });
      li.appendChild(num);
      li.appendChild(document.createTextNode(p));
      list.appendChild(li);
    });
    card.appendChild(list);

    var startBtn = el("button", { className:"btn", text:"Begin the exploration", attrs:{ type:"button" } });
    startBtn.style.marginTop = "26px";
    startBtn.addEventListener("click", function(){
      state.step = 1;
      state.ch1Index = 0;
      renderRoute();
    });
    card.appendChild(startBtn);

    wrap.appendChild(card);
    main.appendChild(wrap);
    setProgress();
  }

  function setMode(m){
    state.mode = m;
    document.body.setAttribute("data-mode", m);
  }

  /* ---------------------------------------------------------
     SCREEN: CHAPTER 1 — Scenarios
  --------------------------------------------------------- */
  function renderChapter1(){
    clearMain();
    var q = CH1_QUESTIONS[state.ch1Index];
    var wrap = el("div", { className:"screen" });

    var head = el("div", { className:"chapter-head" });
    head.appendChild(el("span", { className:"eyebrow", text:"Chapter 1 · Discover Your Thinking Style" }));
    head.appendChild(el("h1", { className:"title", text:"Scenario " + (state.ch1Index+1) + " of " + CH1_QUESTIONS.length }));
    wrap.appendChild(head);

    var card = el("div", { className:"card" });
    card.appendChild(el("p", { className:"scenario-prompt", text:q.prompt }));

    var optionsWrap = el("div", { className:"options", attrs:{ role:"radiogroup", "aria-label":"Choose the response closest to your instinct" } });
    q.options.forEach(function(opt, idx){
      var btn = el("button", { className:"option-btn", attrs:{ type:"button", role:"radio", "aria-checked": state.ch1Answers[state.ch1Index]===idx ? "true":"false" } });
      var marker = el("span", { className:"marker", attrs:{ "aria-hidden":"true" } });
      btn.appendChild(marker);
      btn.appendChild(el("span", { text: opt.text }));
      if(state.ch1Answers[state.ch1Index]===idx) btn.classList.add("selected");
      btn.addEventListener("click", function(){
        selectCh1Option(idx);
      });
      optionsWrap.appendChild(btn);
    });
    card.appendChild(optionsWrap);

    var nav = el("div", { className:"nav-row" });
    var backBtn = el("button", { className:"btn secondary", text:"Back", attrs:{ type:"button" } });
    backBtn.disabled = state.ch1Index === 0 && state.step === 1 ? false : false;
    backBtn.addEventListener("click", function(){
      if(state.ch1Index > 0){ state.ch1Index--; renderChapter1(); }
      else { state.step = 0; renderRoute(); }
    });
    var nextBtn = el("button", { className:"btn", text: state.ch1Index === CH1_QUESTIONS.length-1 ? "Continue to Chapter 2" : "Next", attrs:{ type:"button" } });
    nextBtn.disabled = state.ch1Answers[state.ch1Index] === null;
    nextBtn.addEventListener("click", function(){
      if(state.ch1Index < CH1_QUESTIONS.length-1){
        state.ch1Index++;
        renderChapter1();
      } else {
        state.step = 2;
        renderRoute();
      }
    });
    nav.appendChild(backBtn);
    nav.appendChild(nextBtn);
    card.appendChild(nav);

    wrap.appendChild(card);
    main.appendChild(wrap);
    setProgress();
  }

  function selectCh1Option(idx){
    var prevIdx = state.ch1Answers[state.ch1Index];
    if(prevIdx !== null && prevIdx === idx) return;
    // undo previous score contribution if changing an answer
    if(prevIdx !== null){
      var prevOpt = CH1_QUESTIONS[state.ch1Index].options[prevIdx];
      Object.keys(prevOpt.scores).forEach(function(k){ state.scores[k] -= prevOpt.scores[k]; });
    }
    state.ch1Answers[state.ch1Index] = idx;
    addScores(CH1_QUESTIONS[state.ch1Index].options[idx].scores);
    announce("Selected: " + CH1_QUESTIONS[state.ch1Index].options[idx].text);
    renderChapter1();
  }

  /* ---------------------------------------------------------
     SCREEN: CHAPTER 2 — Draggable priority ranking
  --------------------------------------------------------- */
  function renderChapter2(){
    clearMain();
    var wrap = el("div", { className:"screen" });

    var head = el("div", { className:"chapter-head" });
    head.appendChild(el("span", { className:"eyebrow", text:"Chapter 2 · Choose Your Priorities" }));
    head.appendChild(el("h1", { className:"title", text:"Rank what matters most to you" }));
    head.appendChild(el("p", { className:"sub", text:"Drag each card into the ranking on the right, from what guides your decisions most (1st) to least (5th). On touch devices, press and hold, then drag." }));
    wrap.appendChild(head);

    var card = el("div", { className:"card" });
    var layout = el("div", { className:"rank-layout" });

    // pool column
    var poolCol = document.createElement("div");
    poolCol.appendChild(el("span", { className:"zone-label", text:"Available cards" }));
    var poolList = el("ul", { className:"drag-list", attrs:{ id:"poolList", "aria-label":"Unranked priority cards" } });
    poolCol.appendChild(poolList);
    layout.appendChild(poolCol);

    // ranks column
    var rankCol = document.createElement("div");
    rankCol.appendChild(el("span", { className:"zone-label", text:"Your ranking" }));
    var ranksWrap = el("div", { className:"drag-list", attrs:{ id:"ranksWrap" } });
    for(var i=0;i<5;i++){
      var slot = el("div", { className:"drop-slot", attrs:{ "data-rank": String(i), id:"rank-slot-"+i } });
      slot.appendChild(el("span", { className:"slot-idx", text: (i+1)+"." }));
      ranksWrap.appendChild(slot);
    }
    rankCol.appendChild(ranksWrap);
    layout.appendChild(rankCol);

    card.appendChild(layout);
    card.appendChild(el("p", { className:"live-status", attrs:{ id:"ch2Status" }, text: "" }));

    var nav = el("div", { className:"nav-row" });
    var backBtn = el("button", { className:"btn secondary", text:"Back", attrs:{ type:"button" } });
    backBtn.addEventListener("click", function(){ state.step = 1; state.ch1Index = CH1_QUESTIONS.length-1; renderRoute(); });
    var nextBtn = el("button", { className:"btn", text:"Continue to Chapter 3", attrs:{ type:"button", id:"ch2NextBtn" } });
    nextBtn.disabled = state.ch2Order.length < PRIORITY_CARDS.length;
    nextBtn.addEventListener("click", function(){
      applyCh2Scores();
      state.step = 3;
      renderRoute();
    });
    nav.appendChild(backBtn); nav.appendChild(nextBtn);
    card.appendChild(nav);

    wrap.appendChild(card);
    main.appendChild(wrap);
    setProgress();

    buildRankingDnd(poolList, ranksWrap);
  }

  function buildRankingDnd(poolList, ranksWrap){
    // Determine current placement from state.ch2Order (array of card ids by rank)
    var placed = {}; // rank index -> card id
    state.ch2Order.forEach(function(id, idx){ placed[idx] = id; });

    var placedIds = state.ch2Order.slice();

    function cardData(id){ return PRIORITY_CARDS.filter(function(c){ return c.id===id; })[0]; }

    function makeCardEl(c){
      var li = document.createElement("li");
      li.className = "drag-card";
      li.setAttribute("draggable", "true");
      li.setAttribute("tabindex", "0");
      li.setAttribute("data-id", c.id);
      li.setAttribute("role", "button");
      li.setAttribute("aria-label", c.label + ". Press Enter to place into the next open rank slot.");
      li.innerHTML = '<span class="grip" aria-hidden="true">⠿</span><span>'+c.label+'</span><span class="tag">'+c.tag+'</span>';
      return li;
    }

    function refresh(){
      // pool
      poolList.innerHTML = "";
      PRIORITY_CARDS.forEach(function(c){
        if(placedIds.indexOf(c.id) === -1){
          poolList.appendChild(makeCardEl(c));
        }
      });
      // slots
      var slots = ranksWrap.querySelectorAll(".drop-slot");
      slots.forEach(function(slot, idx){
        var idxLabel = slot.querySelector(".slot-idx");
        slot.innerHTML = "";
        slot.appendChild(idxLabel || el("span", { className:"slot-idx", text:(idx+1)+"." }));
        var id = placed[idx];
        if(id){
          slot.classList.add("filled");
          var c = cardData(id);
          var cardEl = makeCardEl(c);
          cardEl.setAttribute("aria-label", c.label + ", ranked " + (idx+1) + ". Press Enter to send back to the pool.");
          slot.appendChild(cardEl);
        } else {
          slot.classList.remove("filled");
          var ph = el("span", { text:"Drop a card here" });
          slot.appendChild(ph);
        }
      });
      state.ch2Order = [];
      for(var i=0;i<5;i++){ if(placed[i]) state.ch2Order.push(placed[i]); }
      var statusEl = document.getElementById("ch2Status");
      if(statusEl) statusEl.textContent = state.ch2Order.length + " of " + PRIORITY_CARDS.length + " ranked.";
      var nextBtn = document.getElementById("ch2NextBtn");
      if(nextBtn) nextBtn.disabled = state.ch2Order.length < PRIORITY_CARDS.length;
      attachHandlers();
    }

    function firstOpenSlotIndex(){
      for(var i=0;i<5;i++){ if(!placed[i]) return i; }
      return -1;
    }

    function placeCard(id, targetIdx){
      // remove from any existing slot
      Object.keys(placed).forEach(function(k){ if(placed[k]===id) delete placed[k]; });
      var pIdx = placedIds.indexOf(id);
      if(pIdx>-1) placedIds.splice(pIdx,1);
      if(targetIdx === null || targetIdx === undefined){
        // return to pool
      } else {
        // if slot occupied, move that occupant back to pool
        if(placed[targetIdx]){
          var displaced = placed[targetIdx];
          // no-op: displaced goes to pool implicitly since we rebuild placedIds from `placed`
        }
        placed[targetIdx] = id;
      }
      placedIds = Object.keys(placed).map(function(k){ return placed[k]; });
      refresh();
    }

    function attachHandlers(){
      // Pool cards
      Array.prototype.forEach.call(poolList.querySelectorAll(".drag-card"), function(cardEl){
        setupDraggable(cardEl, {
          onDrop: function(targetSlot){
            var idx = targetSlot ? parseInt(targetSlot.getAttribute("data-rank"),10) : firstOpenSlotIndex();
            if(idx > -1) placeCard(cardEl.getAttribute("data-id"), idx);
          },
          onKeyActivate: function(){
            var idx = firstOpenSlotIndex();
            if(idx > -1){ placeCard(cardEl.getAttribute("data-id"), idx); announce(cardEl.textContent + " placed at rank " + (idx+1)); }
          }
        });
      });
      // Slot-held cards (click/enter to unplace)
      Array.prototype.forEach.call(ranksWrap.querySelectorAll(".drop-slot .drag-card"), function(cardEl){
        setupDraggable(cardEl, {
          onDrop: function(targetSlot){
            if(targetSlot){
              var idx = parseInt(targetSlot.getAttribute("data-rank"),10);
              placeCard(cardEl.getAttribute("data-id"), idx);
            } else {
              placeCard(cardEl.getAttribute("data-id"), null);
            }
          },
          onKeyActivate: function(){
            placeCard(cardEl.getAttribute("data-id"), null);
            announce(cardEl.textContent + " returned to pool");
          }
        });
      });
      // Slots as drop targets
      Array.prototype.forEach.call(ranksWrap.querySelectorAll(".drop-slot"), function(slot){
        registerDropTarget(slot);
      });
      registerDropTarget(poolList, true);
    }

    refresh();
  }

  function applyCh2Scores(){
    // weight rank1 = 5pts down to rank5 = 1pt
    state.ch2Order.forEach(function(id, idx){
      var card = PRIORITY_CARDS.filter(function(c){ return c.id===id; })[0];
      if(!card) return;
      var weight = 5 - idx;
      var s = {}; s[card.tendency] = weight;
      addScores(s);
    });
  }

  /* ---------------------------------------------------------
     SCREEN: CHAPTER 3 — Timeline mapping
  --------------------------------------------------------- */
  function renderChapter3(){
    clearMain();
    var wrap = el("div", { className:"screen" });

    var head = el("div", { className:"chapter-head" });
    head.appendChild(el("span", { className:"eyebrow", text:"Chapter 3 · Map Your Thinking" }));
    head.appendChild(el("h1", { className:"title", text:"Arrange your natural decision flow" }));
    head.appendChild(el("p", { className:"sub", text:"Drag each stage onto the timeline in the order they usually happen for you when facing a meaningful decision." }));
    wrap.appendChild(head);

    var card = el("div", { className:"card" });
    var timelineWrap = el("div", { className:"timeline-wrap" });
    var track = el("div", { className:"timeline-track", attrs:{ id:"timelineTrack" } });
    TIMELINE_STAGES.forEach(function(stage, i){
      var slot = el("div", { className:"timeline-slot", attrs:{ "data-rank": String(i), id:"tl-slot-"+i } });
      slot.appendChild(el("span", { className:"stage-label", text: stage }));
      slot.appendChild(el("span", { text:"Drop a stage here" }));
      track.appendChild(slot);
    });
    timelineWrap.appendChild(track);
    card.appendChild(timelineWrap);

    card.appendChild(el("span", { className:"zone-label", text:"Stages to place", attrs:{ style:"margin-top:20px;display:block;" } }));
    var pool = el("div", { className:"pill-pool", attrs:{ id:"timelinePool" } });
    card.appendChild(pool);

    card.appendChild(el("p", { className:"live-status", attrs:{ id:"ch3Status" }, text:"" }));

    var nav = el("div", { className:"nav-row" });
    var backBtn = el("button", { className:"btn secondary", text:"Back", attrs:{ type:"button" } });
    backBtn.addEventListener("click", function(){ state.step = 2; renderRoute(); });
    var nextBtn = el("button", { className:"btn", text:"See my reflection journal", attrs:{ type:"button", id:"ch3NextBtn" } });
    nextBtn.disabled = state.ch3Order.length < TIMELINE_STEPS.length;
    nextBtn.addEventListener("click", function(){
      applyCh3Scores();
      state.step = 4;
      renderRoute();
    });
    nav.appendChild(backBtn); nav.appendChild(nextBtn);
    card.appendChild(nav);

    wrap.appendChild(card);
    main.appendChild(wrap);
    setProgress();

    buildTimelineDnd(pool, track);
  }

  function buildTimelineDnd(pool, track){
    var placed = {};
    state.ch3Order.forEach(function(id, idx){ placed[idx] = id; });
    var placedIds = state.ch3Order.slice();

    function stepData(id){ return TIMELINE_STEPS.filter(function(s){ return s.id===id; })[0]; }

    function makePill(s){
      var d = document.createElement("div");
      d.className = "drag-pill";
      d.setAttribute("draggable", "true");
      d.setAttribute("tabindex", "0");
      d.setAttribute("data-id", s.id);
      d.setAttribute("role", "button");
      d.setAttribute("aria-label", s.label + ". Press Enter to place into the next open timeline slot.");
      d.textContent = s.label;
      return d;
    }

    function firstOpenSlotIndex(){
      for(var i=0;i<TIMELINE_STEPS.length;i++){ if(!placed[i]) return i; }
      return -1;
    }

    function refresh(){
      pool.innerHTML = "";
      TIMELINE_STEPS.forEach(function(s){
        if(placedIds.indexOf(s.id) === -1) pool.appendChild(makePill(s));
      });
      var slots = track.querySelectorAll(".timeline-slot");
      slots.forEach(function(slot, idx){
        var label = slot.querySelector(".stage-label");
        slot.innerHTML = "";
        slot.appendChild(label);
        var id = placed[idx];
        if(id){
          slot.classList.add("filled");
          var s = stepData(id);
          var pillEl = makePill(s);
          pillEl.setAttribute("aria-label", s.label + ", placed " + TIMELINE_STAGES[idx] + ". Press Enter to send back to the pool.");
          slot.appendChild(pillEl);
        } else {
          slot.classList.remove("filled");
          slot.appendChild(el("span", { text:"Drop a stage here" }));
        }
      });
      state.ch3Order = [];
      for(var i=0;i<TIMELINE_STEPS.length;i++){ if(placed[i]) state.ch3Order.push(placed[i]); }
      var statusEl = document.getElementById("ch3Status");
      if(statusEl) statusEl.textContent = state.ch3Order.length + " of " + TIMELINE_STEPS.length + " placed.";
      var nextBtn = document.getElementById("ch3NextBtn");
      if(nextBtn) nextBtn.disabled = state.ch3Order.length < TIMELINE_STEPS.length;
      attachHandlers();
    }

    function placeStep(id, targetIdx, isReorder){
      Object.keys(placed).forEach(function(k){ if(placed[k]===id) delete placed[k]; });
      var pIdx = placedIds.indexOf(id);
      if(pIdx>-1) placedIds.splice(pIdx,1);
      if(targetIdx !== null && targetIdx !== undefined){
        placed[targetIdx] = id;
      }
      placedIds = Object.keys(placed).map(function(k){ return placed[k]; });
      if(isReorder) state.ch3Reorders++;
      refresh();
    }

    function attachHandlers(){
      Array.prototype.forEach.call(pool.querySelectorAll(".drag-pill"), function(pillEl){
        setupDraggable(pillEl, {
          onDrop: function(targetSlot){
            var idx = targetSlot ? parseInt(targetSlot.getAttribute("data-rank"),10) : firstOpenSlotIndex();
            if(idx > -1) placeStep(pillEl.getAttribute("data-id"), idx, false);
          },
          onKeyActivate: function(){
            var idx = firstOpenSlotIndex();
            if(idx > -1){ placeStep(pillEl.getAttribute("data-id"), idx, false); announce(pillEl.textContent + " placed at " + TIMELINE_STAGES[idx]); }
          }
        });
      });
      Array.prototype.forEach.call(track.querySelectorAll(".timeline-slot .drag-pill"), function(pillEl){
        setupDraggable(pillEl, {
          onDrop: function(targetSlot){
            if(targetSlot){
              var idx = parseInt(targetSlot.getAttribute("data-rank"),10);
              placeStep(pillEl.getAttribute("data-id"), idx, true);
            } else {
              placeStep(pillEl.getAttribute("data-id"), null, true);
            }
          },
          onKeyActivate: function(){
            placeStep(pillEl.getAttribute("data-id"), null, true);
            announce(pillEl.textContent + " returned to pool");
          }
        });
      });
      Array.prototype.forEach.call(track.querySelectorAll(".timeline-slot"), function(slot){ registerDropTarget(slot); });
      registerDropTarget(pool, true);
    }

    refresh();
  }

  function applyCh3Scores(){
    state.ch3Order.forEach(function(id, idx){
      var step = TIMELINE_STEPS.filter(function(s){ return s.id===id; })[0];
      if(!step || !step.tendency) return;
      var weight = TIMELINE_STEPS.length - idx; // earlier placement = more weight
      var s = {}; s[step.tendency] = weight;
      addScores(s);
    });
    if(state.ch3Reorders >= 4){
      addScores({ overthinking: 2 });
    }
  }

  /* ---------------------------------------------------------
     GENERIC DRAG & DROP ENGINE (mouse/native + touch fallback)
  --------------------------------------------------------- */
  var dropTargets = [];
  var activeDrag = null; // { el, ghost, sourceParentSelector }

  function registerDropTarget(node, isPool){
    node.__isPool = !!isPool;
    if(dropTargets.indexOf(node) === -1) dropTargets.push(node);

    node.addEventListener("dragover", function(e){
      e.preventDefault();
      node.classList.add("drag-over");
    });
    node.addEventListener("dragleave", function(){
      node.classList.remove("drag-over");
    });
    node.addEventListener("drop", function(e){
      e.preventDefault();
      node.classList.remove("drag-over");
      if(activeDrag && activeDrag.onDrop){
        activeDrag.onDrop(node.__isPool ? null : node);
      }
    });
  }

  function setupDraggable(node, handlers){
    node.__handlers = handlers;

    node.addEventListener("dragstart", function(e){
      activeDrag = { node: node, onDrop: handlers.onDrop };
      node.classList.add("dragging");
      try{ e.dataTransfer.setData("text/plain", node.getAttribute("data-id")); }catch(err){}
      e.dataTransfer.effectAllowed = "move";
    });
    node.addEventListener("dragend", function(){
      node.classList.remove("dragging");
      dropTargets.forEach(function(t){ t.classList.remove("drag-over"); });
      activeDrag = null;
    });

    node.addEventListener("keydown", function(e){
      if(e.key === "Enter" || e.key === " "){
        e.preventDefault();
        handlers.onKeyActivate();
      }
    });

    // Touch fallback
    var touchGhost = null;
    var startX, startY, lastTarget = null;

    node.addEventListener("touchstart", function(e){
      if(e.touches.length !== 1) return;
      var t = e.touches[0];
      startX = t.clientX; startY = t.clientY;
      var rect = node.getBoundingClientRect();
      touchGhost = node.cloneNode(true);
      touchGhost.classList.add("floating");
      touchGhost.style.setProperty("--float-w", rect.width + "px");
      touchGhost.style.left = rect.left + "px";
      touchGhost.style.top = rect.top + "px";
      touchGhost.style.width = rect.width + "px";
      document.body.appendChild(touchGhost);
      node.classList.add("dragging");
    }, { passive: true });

    node.addEventListener("touchmove", function(e){
      if(!touchGhost) return;
      var t = e.touches[0];
      var dx = t.clientX - startX, dy = t.clientY - startY;
      var rect = node.getBoundingClientRect();
      touchGhost.style.left = (rect.left + dx) + "px";
      touchGhost.style.top = (rect.top + dy) + "px";
      touchGhost.style.transform = "translate(" + dx + "px," + dy + "px)";

      touchGhost.style.display = "none";
      var underEl = document.elementFromPoint(t.clientX, t.clientY);
      touchGhost.style.display = "";

      var target = underEl ? underEl.closest(".drop-slot, .drag-list, .pill-pool, .timeline-slot") : null;
      if(lastTarget && lastTarget !== target) lastTarget.classList.remove("drag-over");
      if(target){ target.classList.add("drag-over"); }
      lastTarget = target;
      e.preventDefault();
    }, { passive: false });

    node.addEventListener("touchend", function(){
      if(!touchGhost) return;
      document.body.removeChild(touchGhost);
      touchGhost = null;
      node.classList.remove("dragging");
      if(lastTarget){
        lastTarget.classList.remove("drag-over");
        var isPool = lastTarget.__isPool;
        handlers.onDrop(isPool ? null : (lastTarget.classList.contains("drop-slot") || lastTarget.classList.contains("timeline-slot") ? lastTarget : null));
      }
      lastTarget = null;
    });
  }

  /* ---------------------------------------------------------
     SCREEN: RESULTS / JOURNAL
  --------------------------------------------------------- */
  function renderResults(){
    clearMain();
    var wrap = el("div", { className:"screen" });

    var totalRaw = Object.keys(state.scores).reduce(function(sum,k){ return sum + Math.max(state.scores[k],0); }, 0);
    if(totalRaw <= 0) totalRaw = 1;
    var percentages = {};
    Object.keys(state.scores).forEach(function(k){
      percentages[k] = Math.round((Math.max(state.scores[k],0) / totalRaw) * 100);
    });
    // fix rounding drift to sum to 100
    var sumPct = Object.keys(percentages).reduce(function(s,k){ return s+percentages[k]; },0);
    var drift = 100 - sumPct;
    if(drift !== 0){
      var topKey = Object.keys(percentages).sort(function(a,b){ return percentages[b]-percentages[a]; })[0];
      percentages[topKey] += drift;
    }

    var sortedKeys = Object.keys(percentages).sort(function(a,b){ return percentages[b]-percentages[a]; });
    var primary = sortedKeys[0];
    var secondary = sortedKeys[1];

    var head = el("div", { className:"result-header" });
    head.appendChild(el("span", { className:"eyebrow", text:"Your Reflection Journal" }));
    head.appendChild(el("h1", { className:"title", text:"A mirror, not a verdict" }));
    head.appendChild(el("p", { className:"sub", text:"Here's what this exploration noticed. Thinking patterns shift with context, mood, and practice — treat this as a starting point for curiosity, not a fixed label.", attrs:{ style:"margin-left:auto;margin-right:auto;" } }));
    head.style.margin = "0 auto 10px";
    wrap.appendChild(head);

    var card = el("div", { className:"card" });

    var breakdown = el("div", { className:"breakdown" });
    sortedKeys.forEach(function(key){
      var t = TENDENCIES[key];
      var row = el("div", { className:"bar-row" });
      row.appendChild(el("span", { className:"name", text: t.name }));
      var track = el("div", { className:"bar-track" });
      var fill = el("div", { className:"bar-fill" });
      fill.style.background = t.color;
      track.appendChild(fill);
      row.appendChild(track);
      row.appendChild(el("span", { className:"pct", text: percentages[key] + "%" }));
      breakdown.appendChild(row);
      // animate after mount
      setTimeout(function(){ fill.style.width = percentages[key] + "%"; }, 60);
    });
    card.appendChild(breakdown);

    var primaryBlock = el("div", { className:"insight-block" });
    primaryBlock.appendChild(el("h3", { text: "Your leading pattern: " + TENDENCIES[primary].name }));
    primaryBlock.appendChild(el("p", { text: TENDENCIES[primary].blurb }));
    card.appendChild(primaryBlock);

    var secondaryBlock = el("div", { className:"insight-block" });
    secondaryBlock.style.background = "#fff";
    secondaryBlock.style.border = "1px solid var(--line)";
    secondaryBlock.appendChild(el("h3", { text: "A secondary thread: " + TENDENCIES[secondary].name }));
    secondaryBlock.appendChild(el("p", { text: TENDENCIES[secondary].blurb + " This suggests your thinking style flexes between these two modes depending on the situation." }));
    card.appendChild(secondaryBlock);

    var journal = el("div", { className:"journal-area" });
    journal.style.marginTop = "24px";
    var label = el("label", { text:"Journal reflection (optional, stays on this device only while open)", attrs:{ for:"journalNotes" } });
    var textarea = el("textarea", { attrs:{ id:"journalNotes", placeholder:"What felt true about this reflection? What surprised you?" } });
    journal.appendChild(label);
    journal.appendChild(textarea);
    card.appendChild(journal);

    var nav = el("div", { className:"nav-row" });
    var backBtn = el("button", { className:"btn secondary", text:"Back", attrs:{ type:"button" } });
    backBtn.addEventListener("click", function(){ state.step = 3; renderRoute(); });
    var restartBtn = el("button", { className:"btn", text:"Start over", attrs:{ type:"button" } });
    restartBtn.addEventListener("click", resetAll);
    nav.appendChild(backBtn); nav.appendChild(restartBtn);
    card.appendChild(nav);

    wrap.appendChild(card);
    main.appendChild(wrap);
    setProgress();
    announce("Your reflection journal is ready. Leading pattern: " + TENDENCIES[primary].name);
  }

  function resetAll(){
    state.step = 0;
    state.ch1Answers = new Array(CH1_QUESTIONS.length).fill(null);
    state.ch1Index = 0;
    state.scores = { analytical:0, emotional:0, overthinking:0, action:0, balanced:0 };
    state.ch2Order = [];
    state.ch3Order = [];
    state.ch3Reorders = 0;
    renderRoute();
  }

  /* ---------------------------------------------------------
     ROUTER
  --------------------------------------------------------- */
  function renderRoute(){
    switch(state.step){
      case 0: renderStart(); break;
      case 1: renderChapter1(); break;
      case 2: renderChapter2(); break;
      case 3: renderChapter3(); break;
      case 4: renderResults(); break;
      default: renderStart();
    }
  }

  renderRoute();
})();
</script>
</body>
</html>
<img width="584" height="573" alt="image" src="https://github.com/user-attachments/assets/cac9fb3c-a6b9-4685-aa55-47f75482c6b4" />
<img width="568" height="455" alt="image" src="https://github.com/user-attachments/assets/9af6a99f-ee14-4f1b-b1a1-6102f8eec178" />
<img width="1013" height="585" alt="image" src="https://github.com/user-attachments/assets/b611bc5b-1f80-4132-9283-daa1d0813e74" />
<img width="1013" height="630" alt="image" src="https://github.com/user-attachments/assets/23f3c61e-783d-4dfd-8bf1-958c47238f2a" />
<img width="999" height="622" alt="image" src="https://github.com/user-attachments/assets/99fd8fab-6483-42f1-88ba-4603a9e963f2" />
<img width="934" height="605" alt="image" src="https://github.com/user-attachments/assets/2f278573-9cfb-4d18-9b56-e5eef9e15dad" />
<img width="969" height="608" alt="image" src="https://github.com/user-attachments/assets/0c8bd36b-de49-4dd7-90e2-ecd5188e55af" />
<img width="908" height="636" alt="image" src="https://github.com/user-attachments/assets/0e0575a6-621a-481f-88ab-f08fc0c2097a" />
<img width="936" height="601" alt="image" src="https://github.com/user-attachments/assets/d0b8042e-3dbb-4190-aa6e-3f9184c8768a" />
<img width="936" height="603" alt="image" src="https://github.com/user-attachments/assets/998c1c3d-ef9a-4a53-b043-98370090c090" />
<img width="935" height="693" alt="image" src="https://github.com/user-attachments/assets/aab5908b-3bd5-4cc7-a72f-be99b2183909" />
<img width="972" height="530" alt="image" src="https://github.com/user-attachments/assets/e0263c97-e26f-410f-ba03-8b133f3bd126" />
<img width="950" height="817" alt="image" src="https://github.com/user-attachments/assets/4ceee647-ef0b-4bd4-8c5d-16b729e61f46" />
<img width="949" height="776" alt="image" src="https://github.com/user-attachments/assets/f584ab2f-9464-4095-bd24-d8bd5e968bf0" />
<img width="1293" height="1056" alt="image" src="https://github.com/user-attachments/assets/e13c5034-dc0e-4ce9-968f-c0c015fdcfe2" />
<img width="858" height="647" alt="image" src="https://github.com/user-attachments/assets/fb8a29d6-5d27-4645-83e5-8c7c60b71e35" />
<img width="1308" height="1078" alt="image" src="https://github.com/user-attachments/assets/60de1ae9-ee2c-40a1-b583-a165ddba5cea" />
