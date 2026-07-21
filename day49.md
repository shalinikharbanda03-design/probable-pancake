:Prompt:
Personal AI Playbook

You are an expert AI workflow designer, prompt engineer, productivity consultant, UX designer, and senior frontend developer.

Interview first, one question at a time using MCQs whenever possible (free text only when absolutely necessary). Your goal is to understand how the user actually uses AI.

Discover things like:

* Profession or role
* Primary AI use cases
* Daily repetitive tasks
* Biggest productivity bottlenecks
* Preferred AI models
* Experience level
* Desired outcomes

Only begin building after you have enough context.

Generate a premium, fully interactive Personal AI Playbook as a single self-contained HTML file using only HTML, CSS, and JavaScript (no external libraries).

The playbook should be completely personalized based on the interview. Instead of generic prompts, create reusable AI workflow systems that match the user's needs. Each workflow should include editable templates, customizable variables, practical examples, best practices, and one-click copy.

The application should intelligently organize workflows into relevant categories instead of showing unnecessary ones.

Include a Prompt Builder that lets users assemble prompts from reusable building blocks such as role, objective, context, constraints, reasoning strategy, output format, tone, examples, and quality checks while showing a live preview.

Include a Loop Builder that converts any normal prompt into an autonomous looping prompt by allowing users to define goals, evaluation criteria, improvement strategy, stop conditions, and safety rules.

Rather than storing hundreds of prompts, generate modular building blocks that can be combined into thousands of prompt variations tailored to the user's workflow. Give dropdown options wherever needed, to avoid workload on the user.

Allow users to create, edit, duplicate, favorite, search, filter, and save their own workflows using local storage.

## Make the purpose unmistakable to a first-time viewer
Someone opening this file cold — with no context, possibly just a screenshot — should understand what it is within seconds. To achieve that:
- Include a persistent, plain-language explainer visible on the main view by default (not just a one-time onboarding modal), stating what the tool does and what its main sections are for. It can be dismissible, but only via user action.
- Add a permanent, always-visible "What is this?" affordance (e.g. a small help button) that re-opens the full explanation on demand, at any time — not just on first run.
- Use plain, self-descriptive navigation labels for every section (e.g. "Dashboard," not invented jargon like "Deck" or "Hub"). If you introduce a novel term for a feature, define it in the UI the first time it appears.
- In both the Prompt Builder and Loop Builder, every building block must carry a short, visible explanation of what it does and why it matters — shown both (a) in the block picker before it's added, and (b) inside the assembled block once it's in use. Someone should never have to guess what "Reasoning strategy" or "Stop conditions" means or why it's there.
- Section subtitles and empty states should describe purpose in plain language, not just decorative flavor text (e.g. "Your saved AI prompt workflows, at a glance" rather than "Your AI operating system, at a glance").

The interface should feel like a polished commercial SaaS product with beautiful typography, smooth animations, responsive design, dark mode, keyboard shortcuts, onboarding, import/export, and thoughtful UX throughout.

Focus on teaching users how to build reusable AI systems rather than simply giving them prompts.

:Response:
Your Personal AI Playbook is ready — open the file and it'll walk you through a quick onboarding.

What's inside, tailored to ops/access-management support work:

8 pre-built workflows across Access & Approvals, Ticket Triage, Policy Research, Docs/SOPs, Reports, Meetings, Comms, and Planning — each with {{variables}} you fill in and copy, no rewriting from scratch
Prompt Builder — assemble one-off prompts from labeled blocks (Role, Objective, Context, Reasoning strategy, Format, Tone, etc.), each with a plain explanation of what it does, live preview, one-click copy
Loop Builder — since you wanted to learn how self-checking prompts work: define a Goal, Evaluation criteria, Improvement strategy, Stop conditions, and Safety rules, and watch it assemble into an iterating prompt
Search, filter by category, favorite, duplicate, edit, delete — all saved to your browser via localStorage
Dark mode, keyboard shortcuts (press ? inside the app to see them), import/export for backup, and a persistent "What is this?" explainer so it's never a mystery to anyone who opens it

Everything's local — nothing leaves your browser. Try editing or duplicating the Access Request or Ticket Triage workflows first since those matched your top bottlenecks.

:HTML:
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Your AI Playbook — Ops &amp; Business Support</title>
<style>
:root{
  --ink:#14181F; --paper:#F7F5F0; --slate:#4B5768; --slate-2:#6B7686;
  --accent:#1E9E92; --accent-dim:#DCEEEC; --amber:#E0A458; --amber-dim:#FBEDDA;
  --line:#DCD7C9; --card:#FFFFFF; --danger:#C1524A;
  --shadow: 0 1px 2px rgba(20,24,31,.04), 0 6px 20px rgba(20,24,31,.06);
  --radius: 10px;
  --font-display:'Space Grotesk', 'Segoe UI', sans-serif;
  --font-body:'Inter', 'Segoe UI', sans-serif;
  --font-mono:'JetBrains Mono', 'Consolas', monospace;
}
[data-theme="dark"]{
  --ink:#F2F1EC; --paper:#12151B; --slate:#C7CDD6; --slate-2:#8D97A4;
  --accent:#3FC5B8; --accent-dim:#173230; --amber:#E7B172; --amber-dim:#2E2517;
  --line:#2A2F38; --card:#1A1E26; --danger:#E27C74;
  --shadow: 0 1px 2px rgba(0,0,0,.3), 0 8px 24px rgba(0,0,0,.35);
}
*{box-sizing:border-box; margin:0; padding:0;}
body{
  font-family:var(--font-body); background:var(--paper); color:var(--ink);
  transition:background .25s ease, color .25s ease;
  -webkit-font-smoothing:antialiased;
}
h1,h2,h3,h4{font-family:var(--font-display); letter-spacing:-0.01em;}
button{font-family:inherit; cursor:pointer;}
input,select,textarea{font-family:inherit;}
::selection{background:var(--accent); color:#fff;}
.mono{font-family:var(--font-mono);}

/* ===== Layout ===== */
.app{display:flex; min-height:100vh;}
.sidebar{
  width:230px; flex-shrink:0; background:var(--card); border-right:1px solid var(--line);
  display:flex; flex-direction:column; padding:20px 14px; position:sticky; top:0; height:100vh; overflow-y:auto;
  z-index:20;
}
.brand{display:flex; align-items:center; gap:10px; padding:6px 8px 22px 8px;}
.brand-mark{
  width:34px; height:34px; border-radius:9px; background:linear-gradient(135deg,var(--accent),#0d6e66);
  display:flex; align-items:center; justify-content:center; color:#fff; font-family:var(--font-display); font-weight:700; font-size:15px;
  flex-shrink:0;
}
.brand-text{line-height:1.2;}
.brand-text .t1{font-family:var(--font-display); font-weight:600; font-size:14.5px;}
.brand-text .t2{font-size:11px; color:var(--slate-2);}

.nav{display:flex; flex-direction:column; gap:2px; flex:1;}
.nav-item{
  display:flex; align-items:center; gap:10px; padding:9px 10px; border-radius:8px; border:none;
  background:transparent; color:var(--slate); font-size:13.5px; font-weight:500; text-align:left; width:100%;
  transition:background .15s, color .15s;
}
.nav-item svg{width:17px; height:17px; flex-shrink:0; opacity:.85;}
.nav-item:hover{background:var(--accent-dim); color:var(--ink);}
.nav-item.active{background:var(--accent); color:#fff;}
.nav-item.active svg{opacity:1;}
.nav-divider{height:1px; background:var(--line); margin:12px 4px;}
.nav-label{font-size:10.5px; text-transform:uppercase; letter-spacing:.08em; color:var(--slate-2); padding:8px 10px 4px;}

.sidebar-foot{display:flex; flex-direction:column; gap:6px; padding-top:10px;}
.mini-btn{
  display:flex; align-items:center; gap:8px; padding:8px 10px; border-radius:8px; border:1px solid var(--line);
  background:transparent; color:var(--slate); font-size:12.5px; font-weight:500;
}
.mini-btn:hover{border-color:var(--accent); color:var(--ink);}
.mini-btn svg{width:15px; height:15px;}

.main{flex:1; min-width:0; display:flex; flex-direction:column;}
.topbar{
  position:sticky; top:0; z-index:10; background:var(--paper)ee; backdrop-filter:blur(8px);
  border-bottom:1px solid var(--line); padding:14px 28px; display:flex; align-items:center; justify-content:space-between; gap:16px;
}
.topbar-title{font-size:19px; font-weight:600; font-family:var(--font-display);}
.topbar-sub{font-size:12.5px; color:var(--slate-2); margin-top:1px;}
.topbar-actions{display:flex; align-items:center; gap:8px;}
.icon-btn{
  width:34px; height:34px; border-radius:8px; border:1px solid var(--line); background:var(--card);
  display:flex; align-items:center; justify-content:center; color:var(--slate); flex-shrink:0;
}
.icon-btn:hover{border-color:var(--accent); color:var(--accent);}
.icon-btn svg{width:16px; height:16px;}

.content{padding:24px 28px 60px; max-width:1180px; width:100%; margin:0 auto;}
.view{display:none; animation:fade .25s ease;}
.view.active{display:block;}
@keyframes fade{from{opacity:0; transform:translateY(4px);} to{opacity:1; transform:translateY(0);}}

/* ===== Explainer banner ===== */
.explainer{
  background:linear-gradient(135deg, var(--accent-dim), var(--paper)); border:1px solid var(--line);
  border-radius:var(--radius); padding:16px 18px; margin-bottom:22px; display:flex; gap:14px; align-items:flex-start;
  position:relative;
}
.explainer-icon{
  width:32px; height:32px; border-radius:8px; background:var(--accent); color:#fff; flex-shrink:0;
  display:flex; align-items:center; justify-content:center;
}
.explainer-icon svg{width:17px; height:17px;}
.explainer h4{font-size:14px; margin-bottom:4px;}
.explainer p{font-size:13px; color:var(--slate); line-height:1.5; max-width:820px;}
.explainer-close{
  position:absolute; top:10px; right:10px; width:24px; height:24px; border-radius:6px; border:none; background:transparent;
  color:var(--slate-2); display:flex; align-items:center; justify-content:center;
}
.explainer-close:hover{background:rgba(0,0,0,.06); color:var(--ink);}

/* ===== Cards / Grid ===== */
.section-head{display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:16px; gap:12px; flex-wrap:wrap;}
.section-head h2{font-size:20px;}
.section-head .sub{font-size:12.5px; color:var(--slate-2); margin-top:3px;}

.stat-grid{display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin-bottom:26px;}
.stat-card{background:var(--card); border:1px solid var(--line); border-radius:var(--radius); padding:16px; box-shadow:var(--shadow);}
.stat-card .num{font-family:var(--font-display); font-size:26px; font-weight:600;}
.stat-card .lbl{font-size:12px; color:var(--slate-2); margin-top:2px;}

.cat-row{display:flex; gap:8px; flex-wrap:wrap; margin-bottom:18px;}
.chip{
  padding:7px 13px; border-radius:20px; border:1px solid var(--line); background:var(--card); font-size:12.5px; font-weight:500;
  color:var(--slate); display:flex; align-items:center; gap:6px;
}
.chip:hover{border-color:var(--accent);}
.chip.active{background:var(--ink); color:var(--paper); border-color:var(--ink);}
.chip .dot{width:7px; height:7px; border-radius:50%; flex-shrink:0;}

.toolbar{display:flex; gap:8px; align-items:center; margin-bottom:16px; flex-wrap:wrap;}
.search-box{
  flex:1; min-width:200px; display:flex; align-items:center; gap:8px; background:var(--card); border:1px solid var(--line);
  border-radius:8px; padding:8px 12px;
}
.search-box svg{width:15px; height:15px; color:var(--slate-2); flex-shrink:0;}
.search-box input{border:none; background:transparent; outline:none; font-size:13px; width:100%; color:var(--ink);}
.btn{
  padding:9px 15px; border-radius:8px; border:1px solid var(--line); background:var(--card); color:var(--ink);
  font-size:13px; font-weight:500; display:inline-flex; align-items:center; gap:7px; white-space:nowrap;
}
.btn:hover{border-color:var(--accent); color:var(--accent);}
.btn.primary{background:var(--ink); color:var(--paper); border-color:var(--ink);}
.btn.primary:hover{opacity:.88; color:var(--paper);}
.btn.accent{background:var(--accent); color:#fff; border-color:var(--accent);}
.btn.accent:hover{opacity:.9; color:#fff;}
.btn svg{width:14px; height:14px;}
.btn.sm{padding:6px 10px; font-size:12px;}

.workflow-grid{display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:14px;}
.wf-card{
  background:var(--card); border:1px solid var(--line); border-radius:var(--radius); padding:16px; box-shadow:var(--shadow);
  position:relative; display:flex; flex-direction:column; gap:10px; border-top:3px solid var(--accent);
}
.wf-top{display:flex; justify-content:space-between; align-items:flex-start; gap:8px;}
.wf-title{font-size:14.5px; font-weight:600; font-family:var(--font-display); line-height:1.3;}
.wf-cat{font-size:10.5px; color:var(--accent); font-weight:600; text-transform:uppercase; letter-spacing:.05em; margin-bottom:3px;}
.fav-btn{background:none; border:none; color:var(--slate-2); flex-shrink:0; padding:2px;}
.fav-btn svg{width:17px; height:17px;}
.fav-btn.active{color:var(--amber);}
.wf-desc{font-size:12.5px; color:var(--slate); line-height:1.5;}
.wf-tags{display:flex; gap:5px; flex-wrap:wrap;}
.tag{font-size:10.5px; background:var(--accent-dim); color:var(--accent); padding:3px 8px; border-radius:5px; font-weight:600;}
.wf-actions{display:flex; gap:6px; margin-top:auto; padding-top:8px; border-top:1px dashed var(--line);}

/* ===== Empty state ===== */
.empty-state{
  text-align:center; padding:50px 20px; color:var(--slate-2); border:1px dashed var(--line); border-radius:var(--radius);
}
.empty-state svg{width:38px; height:38px; margin-bottom:10px; opacity:.5;}
.empty-state h4{color:var(--slate); font-size:14px; margin-bottom:4px;}
.empty-state p{font-size:12.5px; max-width:340px; margin:0 auto;}

/* ===== Modal ===== */
.modal-overlay{
  display:none; position:fixed; inset:0; background:rgba(10,12,16,.55); z-index:100; align-items:center; justify-content:center;
  padding:20px; backdrop-filter:blur(2px);
}
.modal-overlay.active{display:flex;}
.modal{
  background:var(--card); border-radius:14px; width:100%; max-width:640px; max-height:88vh; overflow-y:auto;
  box-shadow:0 20px 60px rgba(0,0,0,.3); border:1px solid var(--line); animation:pop .2s ease;
}
@keyframes pop{from{opacity:0; transform:scale(.97) translateY(6px);} to{opacity:1; transform:scale(1) translateY(0);}}
.modal.wide{max-width:920px;}
.modal-head{
  display:flex; justify-content:space-between; align-items:center; padding:18px 22px; border-bottom:1px solid var(--line);
  position:sticky; top:0; background:var(--card); z-index:2;
}
.modal-head h3{font-size:16px;}
.modal-close{background:none; border:none; color:var(--slate-2); width:28px; height:28px; border-radius:7px; display:flex; align-items:center; justify-content:center;}
.modal-close:hover{background:var(--accent-dim); color:var(--ink);}
.modal-body{padding:20px 22px;}
.modal-foot{padding:16px 22px; border-top:1px solid var(--line); display:flex; justify-content:flex-end; gap:8px; position:sticky; bottom:0; background:var(--card);}

.field{margin-bottom:15px;}
.field label{display:block; font-size:12.5px; font-weight:600; margin-bottom:6px; color:var(--ink);}
.field .hint{font-size:11.5px; color:var(--slate-2); margin-bottom:6px; line-height:1.4;}
.field input[type=text], .field textarea, .field select{
  width:100%; padding:9px 11px; border:1px solid var(--line); border-radius:8px; background:var(--paper); color:var(--ink);
  font-size:13px; outline:none; resize:vertical;
}
.field input:focus, .field textarea:focus, .field select:focus{border-color:var(--accent);}
.field textarea{min-height:90px; font-family:var(--font-mono); font-size:12.5px; line-height:1.6;}
.row2{display:grid; grid-template-columns:1fr 1fr; gap:12px;}

/* ===== Prompt Builder / Loop Builder ===== */
.builder-layout{display:grid; grid-template-columns:340px 1fr; gap:20px; align-items:start;}
@media (max-width:900px){.builder-layout{grid-template-columns:1fr;}}
.block-picker{background:var(--card); border:1px solid var(--line); border-radius:var(--radius); padding:14px; box-shadow:var(--shadow); position:sticky; top:80px;}
.block-picker h4{font-size:13px; margin-bottom:10px;}
.picker-item{
  border:1px solid var(--line); border-radius:8px; padding:10px 11px; margin-bottom:8px; cursor:pointer; transition:.15s;
}
.picker-item:hover{border-color:var(--accent); background:var(--accent-dim);}
.picker-item .pi-top{display:flex; justify-content:space-between; align-items:center; margin-bottom:3px;}
.picker-item .pi-name{font-size:12.5px; font-weight:600;}
.picker-item .pi-desc{font-size:11px; color:var(--slate-2); line-height:1.4;}
.pi-add{color:var(--accent); font-size:16px; font-weight:700;}

.assembled{background:var(--card); border:1px solid var(--line); border-radius:var(--radius); padding:16px; box-shadow:var(--shadow); min-height:200px;}
.assembled-empty{padding:40px 10px; text-align:center; color:var(--slate-2); font-size:13px;}
.ab-item{border:1px solid var(--line); border-left:3px solid var(--accent); border-radius:8px; padding:12px; margin-bottom:10px; background:var(--paper);}
.ab-item.loop{border-left-color:var(--amber);}
.ab-head{display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:4px;}
.ab-name{font-size:12.5px; font-weight:700; text-transform:uppercase; letter-spacing:.04em; color:var(--accent);}
.ab-item.loop .ab-name{color:var(--amber);}
.ab-why{font-size:11px; color:var(--slate-2); margin-bottom:8px; line-height:1.4;}
.ab-remove{background:none; border:none; color:var(--slate-2); font-size:16px; line-height:1; padding:0 2px;}
.ab-remove:hover{color:var(--danger);}
.ab-item select, .ab-item textarea, .ab-item input{
  width:100%; padding:7px 9px; border:1px solid var(--line); border-radius:6px; background:var(--card); font-size:12.5px; color:var(--ink); outline:none;
}
.ab-item textarea{min-height:56px; font-family:var(--font-mono); font-size:12px;}
.ab-item select:focus, .ab-item textarea:focus, .ab-item input:focus{border-color:var(--accent);}

.preview-box{
  margin-top:20px; background:var(--ink); color:#E9E7DF; border-radius:var(--radius); padding:16px 18px; position:relative;
}
[data-theme="dark"] .preview-box{background:#0B0D11;}
.preview-box h4{font-size:12px; text-transform:uppercase; letter-spacing:.08em; color:#9CA6B4; margin-bottom:10px; font-family:var(--font-body); font-weight:600;}
.preview-text{font-family:var(--font-mono); font-size:12.5px; line-height:1.7; white-space:pre-wrap; word-break:break-word; max-height:340px; overflow-y:auto;}
.copy-float{position:absolute; top:12px; right:14px;}
.copy-float button{
  background:rgba(255,255,255,.1); color:#fff; border:1px solid rgba(255,255,255,.2); border-radius:7px; padding:6px 11px; font-size:11.5px; font-weight:600;
  display:flex; align-items:center; gap:5px;
}
.copy-float button:hover{background:rgba(255,255,255,.18);}
.copy-float svg{width:13px; height:13px;}

/* ===== Toast ===== */
.toast{
  position:fixed; bottom:24px; left:50%; transform:translateX(-50%) translateY(20px); background:var(--ink); color:var(--paper);
  padding:11px 20px; border-radius:9px; font-size:13px; font-weight:500; box-shadow:0 10px 30px rgba(0,0,0,.25); z-index:200;
  opacity:0; pointer-events:none; transition:.25s ease; display:flex; align-items:center; gap:8px;
}
.toast.show{opacity:1; transform:translateX(-50%) translateY(0);}
.toast svg{width:15px; height:15px; color:var(--accent);}

/* ===== Onboarding ===== */
.onboard-overlay{position:fixed; inset:0; background:rgba(10,12,16,.6); z-index:300; display:flex; align-items:center; justify-content:center; padding:20px;}
.onboard{background:var(--card); border-radius:16px; max-width:480px; width:100%; padding:30px 28px; box-shadow:0 30px 80px rgba(0,0,0,.3);}
.onboard .steps{display:flex; gap:5px; margin-bottom:18px;}
.onboard .steps span{height:4px; flex:1; background:var(--line); border-radius:3px;}
.onboard .steps span.done{background:var(--accent);}
.onboard h3{font-size:19px; margin-bottom:8px;}
.onboard p{font-size:13.5px; color:var(--slate); line-height:1.6; margin-bottom:18px;}
.onboard-foot{display:flex; justify-content:space-between; align-items:center;}
.onboard-icon{width:44px; height:44px; border-radius:11px; background:var(--accent); color:#fff; display:flex; align-items:center; justify-content:center; margin-bottom:16px;}
.onboard-icon svg{width:22px; height:22px;}

/* ===== misc ===== */
kbd{background:var(--paper); border:1px solid var(--line); border-bottom-width:2px; border-radius:4px; padding:1px 6px; font-size:11px; font-family:var(--font-mono);}
.help-list{display:flex; flex-direction:column; gap:8px; margin-top:6px;}
.help-list .hrow{display:flex; justify-content:space-between; align-items:center; font-size:12.5px; padding:6px 0; border-bottom:1px solid var(--line);}
.badge-count{background:var(--accent); color:#fff; font-size:10px; font-weight:700; padding:1px 6px; border-radius:9px; margin-left:4px;}
.small-note{font-size:11.5px; color:var(--slate-2); line-height:1.5;}
.guide-section{margin-bottom:18px;}
.guide-section h5{font-size:12.5px; font-weight:700; margin-bottom:5px; color:var(--accent);}
.footer-note{text-align:center; font-size:11.5px; color:var(--slate-2); margin-top:40px; padding-top:20px; border-top:1px solid var(--line);}
@media (max-width:820px){
  .sidebar{position:fixed; left:-240px; z-index:50; transition:left .2s;} .sidebar.open{left:0;}
  .stat-grid{grid-template-columns:repeat(2,1fr);}
  .content{padding:18px 16px;}
  .topbar{padding:12px 16px;}
}
</style>
</head>
<body data-theme="light">

<div class="app">
  <!-- SIDEBAR -->
  <aside class="sidebar" id="sidebar">
    <div class="brand">
      <div class="brand-mark">AI</div>
      <div class="brand-text">
        <div class="t1">AI Playbook</div>
        <div class="t2">Ops &amp; Business Support</div>
      </div>
    </div>
    <nav class="nav">
      <button class="nav-item active" data-view="dashboard">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="9" rx="1.5"/><rect x="14" y="3" width="7" height="5" rx="1.5"/><rect x="14" y="12" width="7" height="9" rx="1.5"/><rect x="3" y="16" width="7" height="5" rx="1.5"/></svg>
        Dashboard
      </button>
      <button class="nav-item" data-view="workflows">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-4"/><path d="M17 3h4v4"/><path d="M21 3l-9 9"/></svg>
        Workflows
      </button>
      <button class="nav-item" data-view="promptbuilder">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 8h10M7 12h6M7 16h4"/></svg>
        Prompt Builder
      </button>
      <button class="nav-item" data-view="loopbuilder">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 2l4 4-4 4"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><path d="M7 22l-4-4 4-4"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>
        Loop Builder
      </button>
      <button class="nav-item" data-view="library">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
        Building Blocks
      </button>
      <div class="nav-divider"></div>
      <div class="nav-label">Learn</div>
      <button class="nav-item" data-view="guide">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 2-3 4"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
        How This Works
      </button>
    </nav>
    <div class="sidebar-foot">
      <button class="mini-btn" id="themeToggle">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"/></svg>
        <span id="themeLabel">Dark mode</span>
      </button>
      <button class="mini-btn" id="exportBtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
        Export data
      </button>
      <button class="mini-btn" id="importBtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
        Import data
      </button>
      <input type="file" id="importFile" accept=".json" style="display:none">
    </div>
  </aside>

  <!-- MAIN -->
  <div class="main">
    <div class="topbar">
      <div>
        <div class="topbar-title" id="topbarTitle">Dashboard</div>
        <div class="topbar-sub" id="topbarSub">Your saved AI prompt workflows, at a glance</div>
      </div>
      <div class="topbar-actions">
        <button class="icon-btn" id="whatIsThisBtn" title="What is this? (Shift+/)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 2-3 4"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
        </button>
        <button class="icon-btn" id="shortcutsBtn" title="Keyboard shortcuts (?)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="6" width="20" height="12" rx="2"/><path d="M6 10h.01M10 10h.01M14 10h.01M18 10h.01M6 14h12"/></svg>
        </button>
        <button class="btn primary sm" id="newWorkflowBtn">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
          New workflow
        </button>
        <button class="icon-btn" id="menuToggle" style="display:none;">☰</button>
      </div>
    </div>

    <div class="content">

      <!-- Persistent explainer -->
      <div class="explainer" id="explainerBanner">
        <button class="explainer-close" id="explainerClose" title="Dismiss">✕</button>
        <div class="explainer-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 2-3 4"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
        </div>
        <div>
          <h4>What is this tool?</h4>
          <p>This is your personal system for reusing AI prompts instead of rewriting them every time. <strong>Workflows</strong> are ready-made, editable prompt templates for tasks you do often (like access requests or SOP drafts). The <strong>Prompt Builder</strong> lets you assemble a custom prompt piece by piece — pick a role, a goal, some rules — and see it build itself as you go. The <strong>Loop Builder</strong> does the same, but for prompts that ask the AI to check its own work and improve it automatically. <strong>Building Blocks</strong> is the raw library those two builders pull from. Nothing here leaves your browser — everything saves to this device only.</p>
        </div>
      </div>

      <!-- ============ DASHBOARD ============ -->
      <section class="view active" id="view-dashboard">
        <div class="stat-grid">
          <div class="stat-card"><div class="num" id="statTotal">0</div><div class="lbl">Saved workflows</div></div>
          <div class="stat-card"><div class="num" id="statFav">0</div><div class="lbl">Favorited</div></div>
          <div class="stat-card"><div class="num" id="statCats">0</div><div class="lbl">Categories in use</div></div>
          <div class="stat-card"><div class="num" id="statCopies">0</div><div class="lbl">Prompts copied</div></div>
        </div>

        <div class="section-head">
          <div>
            <h2>Favorites</h2>
            <div class="sub">The workflows you've starred for quick access</div>
          </div>
        </div>
        <div class="workflow-grid" id="favGrid"></div>

        <div class="section-head" style="margin-top:30px;">
          <div>
            <h2>All workflows</h2>
            <div class="sub">Every saved workflow, newest first</div>
          </div>
          <button class="btn sm" data-view-link="workflows">View all →</button>
        </div>
        <div class="workflow-grid" id="recentGrid"></div>
      </section>

      <!-- ============ WORKFLOWS ============ -->
      <section class="view" id="view-workflows">
        <div class="section-head">
          <div>
            <h2>Workflows</h2>
            <div class="sub">Reusable, editable prompt systems for your recurring tasks</div>
          </div>
        </div>
        <div class="toolbar">
          <div class="search-box">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            <input type="text" id="wfSearch" placeholder="Search workflows by name, tag, or content…">
          </div>
          <button class="btn sm" id="favFilterBtn">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
            Favorites only
          </button>
        </div>
        <div class="cat-row" id="catFilterRow"></div>
        <div class="workflow-grid" id="allGrid"></div>
      </section>

      <!-- ============ PROMPT BUILDER ============ -->
      <section class="view" id="view-promptbuilder">
        <div class="section-head">
          <div>
            <h2>Prompt Builder</h2>
            <div class="sub">Assemble a one-off prompt from reusable pieces — pick blocks on the left, fill in the details, and copy the finished prompt.</div>
          </div>
        </div>
        <div class="builder-layout">
          <div class="block-picker">
            <h4>Add a block</h4>
            <div id="pbPicker"></div>
          </div>
          <div>
            <div class="assembled" id="pbAssembled"></div>
            <div class="preview-box">
              <h4>Live preview — this is what gets copied</h4>
              <div class="preview-text" id="pbPreview"></div>
              <div class="copy-float">
                <button id="pbCopy"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy prompt</button>
              </div>
            </div>
            <div style="margin-top:12px; display:flex; gap:8px;">
              <button class="btn sm accent" id="pbSaveAsWorkflow">Save as a workflow</button>
              <button class="btn sm" id="pbReset">Clear all blocks</button>
            </div>
          </div>
        </div>
      </section>

      <!-- ============ LOOP BUILDER ============ -->
      <section class="view" id="view-loopbuilder">
        <div class="section-head">
          <div>
            <h2>Loop Builder</h2>
            <div class="sub">Turn a normal prompt into a self-checking one. "Looping" means the AI produces a draft, evaluates it against your criteria, and revises — repeating until it meets your bar or hits a stop condition.</div>
          </div>
        </div>
        <div class="builder-layout">
          <div class="block-picker">
            <h4>Add a loop element</h4>
            <div id="lbPicker"></div>
          </div>
          <div>
            <div class="assembled" id="lbAssembled"></div>
            <div class="preview-box">
              <h4>Live preview — this is what gets copied</h4>
              <div class="preview-text" id="lbPreview"></div>
              <div class="copy-float">
                <button id="lbCopy"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy loop prompt</button>
              </div>
            </div>
            <div style="margin-top:12px; display:flex; gap:8px;">
              <button class="btn sm accent" id="lbSaveAsWorkflow">Save as a workflow</button>
              <button class="btn sm" id="lbReset">Clear all elements</button>
            </div>
          </div>
        </div>
      </section>

      <!-- ============ BUILDING BLOCKS LIBRARY ============ -->
      <section class="view" id="view-library">
        <div class="section-head">
          <div>
            <h2>Building Blocks</h2>
            <div class="sub">The reference library of pieces used by the Prompt Builder and Loop Builder — browse what each one means.</div>
          </div>
        </div>
        <div id="libraryList"></div>
      </section>

      <!-- ============ GUIDE ============ -->
      <section class="view" id="view-guide">
        <div class="section-head"><div><h2>How this works</h2><div class="sub">A short walkthrough of every section, in plain language</div></div></div>
        <div id="guideContent"></div>
      </section>

      <div class="footer-note">Everything on this page is stored locally in your browser (localStorage). Nothing is uploaded anywhere. Use "Export data" to back up or move your workflows.</div>
    </div>
  </div>
</div>

<!-- Workflow modal -->
<div class="modal-overlay" id="wfModalOverlay">
  <div class="modal wide">
    <div class="modal-head">
      <h3 id="wfModalTitle">New workflow</h3>
      <button class="modal-close" id="wfModalClose">✕</button>
    </div>
    <div class="modal-body">
      <div class="row2">
        <div class="field">
          <label>Workflow name</label>
          <input type="text" id="fName" placeholder="e.g. Access Request Justification Writer">
        </div>
        <div class="field">
          <label>Category</label>
          <select id="fCategory"></select>
        </div>
      </div>
      <div class="field">
        <label>Short description</label>
        <div class="hint">One sentence explaining what this workflow does — shown on the card.</div>
        <input type="text" id="fDesc" placeholder="e.g. Turns a raw access request into a policy-ready justification email">
      </div>
      <div class="field">
        <label>Tags (comma separated)</label>
        <input type="text" id="fTags" placeholder="e.g. access, email, compliance">
      </div>
      <div class="field">
        <label>Prompt template</label>
        <div class="hint">Use <span class="mono">{{variable}}</span> for anything you'll want to swap each time — variables become editable fields when you use the workflow.</div>
        <textarea id="fTemplate" style="min-height:180px;" placeholder="You are ..."></textarea>
      </div>
      <div class="field">
        <label>Best practice notes (optional)</label>
        <textarea id="fNotes" style="min-height:70px; font-family:var(--font-body);" placeholder="Tips for getting the best result from this workflow"></textarea>
      </div>
    </div>
    <div class="modal-foot">
      <button class="btn sm" id="wfCancelBtn">Cancel</button>
      <button class="btn sm primary" id="wfSaveBtn">Save workflow</button>
    </div>
  </div>
</div>

<!-- Use workflow modal -->
<div class="modal-overlay" id="useModalOverlay">
  <div class="modal wide">
    <div class="modal-head">
      <h3 id="useModalTitle">Use workflow</h3>
      <button class="modal-close" id="useModalClose">✕</button>
    </div>
    <div class="modal-body">
      <div id="useVarFields"></div>
      <div class="field" style="margin-top:6px;">
        <label>Notes</label>
        <div class="small-note" id="useNotesText">—</div>
      </div>
      <div class="preview-box" style="margin-top:6px;">
        <h4>Filled-in prompt</h4>
        <div class="preview-text" id="useFilledPreview"></div>
      </div>
    </div>
    <div class="modal-foot">
      <button class="btn sm" id="useCloseBtn">Close</button>
      <button class="btn sm primary" id="useCopyBtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:14px;height:14px;"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
        Copy filled prompt
      </button>
    </div>
  </div>
</div>

<!-- What is this modal -->
<div class="modal-overlay" id="helpModalOverlay">
  <div class="modal">
    <div class="modal-head">
      <h3>What is this?</h3>
      <button class="modal-close" id="helpModalClose">✕</button>
    </div>
    <div class="modal-body">
      <p style="font-size:13.5px; line-height:1.6; color:var(--slate); margin-bottom:14px;">
        This is your <strong>Personal AI Playbook</strong> — a private, local system for turning the AI prompts you write over and over into reusable templates, built specifically around your work in <strong>business operations &amp; access management support</strong>.
      </p>
      <div class="help-list">
        <div class="hrow"><span><strong>Dashboard</strong> — quick overview of your saved workflows and favorites</span></div>
        <div class="hrow"><span><strong>Workflows</strong> — your library of saved, reusable prompt templates, organized by category</span></div>
        <div class="hrow"><span><strong>Prompt Builder</strong> — assemble a one-off custom prompt from labeled building blocks with a live preview</span></div>
        <div class="hrow"><span><strong>Loop Builder</strong> — turn a prompt into a self-checking, iterating prompt with goals and stop conditions</span></div>
        <div class="hrow"><span><strong>Building Blocks</strong> — reference list explaining every block used above</span></div>
      </div>
      <p style="font-size:12.5px; color:var(--slate-2); margin-top:14px;">Everything is saved to this browser only (localStorage). Use Export/Import in the sidebar to back up or transfer your data.</p>
    </div>
    <div class="modal-foot"><button class="btn sm primary" id="helpGotIt">Got it</button></div>
  </div>
</div>

<!-- Shortcuts modal -->
<div class="modal-overlay" id="shortcutsModalOverlay">
  <div class="modal">
    <div class="modal-head"><h3>Keyboard shortcuts</h3><button class="modal-close" id="shortcutsModalClose">✕</button></div>
    <div class="modal-body">
      <div class="help-list">
        <div class="hrow"><span>New workflow</span><kbd>N</kbd></div>
        <div class="hrow"><span>Search workflows</span><kbd>/</kbd></div>
        <div class="hrow"><span>Go to Dashboard</span><kbd>G</kbd> then <kbd>D</kbd></div>
        <div class="hrow"><span>Go to Workflows</span><kbd>G</kbd> then <kbd>W</kbd></div>
        <div class="hrow"><span>Go to Prompt Builder</span><kbd>G</kbd> then <kbd>P</kbd></div>
        <div class="hrow"><span>Go to Loop Builder</span><kbd>G</kbd> then <kbd>L</kbd></div>
        <div class="hrow"><span>Toggle dark mode</span><kbd>Shift</kbd> + <kbd>D</kbd></div>
        <div class="hrow"><span>Close any modal</span><kbd>Esc</kbd></div>
        <div class="hrow"><span>Open "What is this?"</span><kbd>?</kbd></div>
      </div>
    </div>
    <div class="modal-foot"><button class="btn sm primary" id="shortcutsGotIt">Got it</button></div>
  </div>
</div>

<!-- Onboarding -->
<div class="onboard-overlay" id="onboardOverlay">
  <div class="onboard">
    <div class="steps" id="onboardSteps"></div>
    <div id="onboardContent"></div>
  </div>
</div>

<div class="toast" id="toast"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span id="toastMsg">Copied</span></div>

<script>
/* ================= FONTS (system fallback fine, but try to load) ================= */
(function(){
  var link=document.createElement('link');
  link.rel='stylesheet';
  link.href='https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap';
  try{document.head.appendChild(link);}catch(e){}
})();

/* ================= DATA MODEL ================= */
const CATEGORIES = [
  {id:'access', name:'Access & Approvals', color:'#1E9E92'},
  {id:'triage', name:'Ticket Triage & Responses', color:'#E0A458'},
  {id:'compliance', name:'Policy & Compliance Research', color:'#8E6FCE'},
  {id:'comms', name:'Emails & Communication', color:'#4C8DE0'},
  {id:'docs', name:'Documentation & SOPs', color:'#C1524A'},
  {id:'reports', name:'Reports & Status Updates', color:'#3FA65C'},
  {id:'meetings', name:'Meeting Notes & Follow-ups', color:'#B5842C'},
  {id:'planning', name:'Planning & Strategy', color:'#5C6BC0'},
];
function catInfo(id){return CATEGORIES.find(c=>c.id===id) || {id:id,name:id,color:'#888'};}

const SEED_WORKFLOWS = [
  {
    id:'seed-1', category:'access', favorite:true, uses:0,
    name:'Access Request Justification Writer',
    desc:'Turns a raw, informal access request into a clear, policy-ready justification for approval.',
    tags:['access','approvals','email'],
    template:`You are an operations assistant helping write access/permission requests that get approved quickly and cleanly.

Request details:
- Requestor: {{requestor_name}}, {{requestor_role}}
- System/resource requested: {{system_or_resource}}
- Business reason: {{business_reason}}
- Duration needed: {{duration}}
- Urgency: {{urgency_level}}

Write a formal access request justification that:
1. States exactly what access is needed and for how long
2. Explains the business reason in terms an approver/auditor would accept
3. Notes any least-privilege consideration (why this scope, not broader access)
4. Uses a professional, concise tone suitable for a compliance-reviewed approval workflow

Output as a ready-to-send message, no more than 150 words.`,
    notes:'Fill in "urgency_level" honestly — approvers de-prioritize requests that overstate urgency. Keep duration specific (e.g. "90 days" not "temporary").'
  },
  {
    id:'seed-2', category:'triage', favorite:false, uses:0,
    name:'Ticket Triage & First-Response Drafter',
    desc:'Classifies an incoming ticket and drafts a first response with next steps.',
    tags:['tickets','triage','support'],
    template:`You are triaging an operations support ticket.

Ticket text:
"""
{{ticket_text}}
"""

Do the following:
1. Classify the ticket: category = one of [Access Request, Bug/System Issue, Policy Question, Escalation, Other], priority = one of [Low, Medium, High, Urgent]
2. In 1-2 sentences, summarize what the requester actually needs (not just what they wrote)
3. Draft a first-response reply in a {{tone}} tone that acknowledges the request, sets expectations on timing, and asks for any missing information needed to resolve it
4. List any missing information as a short bullet list

Keep the reply itself under 100 words.`,
    notes:'Good for high ticket volume days — paste the raw ticket text and get classification + response in one pass.'
  },
  {
    id:'seed-3', category:'compliance', favorite:true, uses:0,
    name:'Policy Question Research Brief',
    desc:'Researches a policy/compliance question and produces a plain-language answer with caveats.',
    tags:['compliance','policy','research'],
    template:`You are a research assistant supporting an operations team with a policy/compliance question. You are not a lawyer and should not give legal advice — flag anything that needs legal/compliance sign-off.

Question: {{policy_question}}
Relevant policy or framework (if known): {{policy_reference}}
Context/situation: {{situation_context}}

Provide:
1. A plain-language answer to the question, in 3-5 sentences
2. Key factors that could change the answer (edge cases, exceptions)
3. Whether this needs formal compliance/legal review before acting, and why
4. Suggested next step

Cite general principles rather than asserting specific legal conclusions.`,
    notes:'Always route the final answer through your actual compliance/legal contact before acting — this is a research starting point, not a ruling.'
  },
  {
    id:'seed-4', category:'docs', favorite:false, uses:0,
    name:'SOP / Process Doc Drafter',
    desc:'Converts a messy process description or notes into a clean, numbered SOP.',
    tags:['sop','documentation','process'],
    template:`You are a technical writer creating a Standard Operating Procedure (SOP) for internal operations use.

Raw process notes:
"""
{{raw_notes}}
"""

Audience: {{audience}}
Process name: {{process_name}}

Produce an SOP with this structure:
1. Purpose (1-2 sentences)
2. Scope (who/what this applies to)
3. Prerequisites (access, tools, approvals needed before starting)
4. Numbered step-by-step procedure (imperative voice, one action per step)
5. Common issues & how to resolve them
6. Owner / who to contact with questions: {{owner}}

Use plain, unambiguous language a new team member could follow without extra context.`,
    notes:'Paste even rough bullet points or a stream-of-consciousness explanation — the model will structure it.'
  },
  {
    id:'seed-5', category:'reports', favorite:false, uses:0,
    name:'Weekly Status Report Summarizer',
    desc:'Turns scattered updates/notes into a structured status report for stakeholders.',
    tags:['reports','status','summary'],
    template:`You are helping prepare a weekly operations status report.

Raw updates/notes from the week:
"""
{{weekly_notes}}
"""

Audience for this report: {{audience}}

Produce a status report with:
1. Headline summary (2 sentences max — the "so what")
2. Completed this week (bullets)
3. In progress / blocked, with what's needed to unblock
4. Metrics or numbers mentioned, called out clearly
5. Next week's priorities (bullets)

Tone: {{tone}}. Keep it scannable — stakeholders should get the gist in under 30 seconds.`,
    notes:'Drop in raw Slack messages, ticket closures, or bullet notes as-is; no need to pre-clean them.'
  },
  {
    id:'seed-6', category:'meetings', favorite:false, uses:0,
    name:'Meeting Notes → Action Items',
    desc:'Converts raw meeting notes/transcript into clear owners, deadlines, and follow-up email.',
    tags:['meetings','followup','actions'],
    template:`You are converting meeting notes into clear outcomes.

Raw notes or transcript:
"""
{{meeting_notes}}
"""

Meeting purpose: {{meeting_purpose}}

Produce:
1. A 3-sentence summary of what was discussed and decided
2. Action items as a table: Owner | Action | Deadline (infer reasonable deadlines if not stated, and mark them as inferred)
3. Open questions that were not resolved
4. A short follow-up email draft recapping the above, ready to send to attendees

Tone: professional, concise, no fluff.`,
    notes:'Works well even with messy, unstructured notes — be as literal as possible when pasting them in.'
  },
  {
    id:'seed-7', category:'comms', favorite:false, uses:0,
    name:'Difficult Email Rewriter',
    desc:'Rewrites a blunt/frustrated draft into a professional, de-escalated version.',
    tags:['email','tone','communication'],
    template:`You are helping rewrite a difficult email to be professional and effective without losing the core message.

Original draft or key points:
"""
{{original_draft}}
"""

Recipient relationship: {{recipient_relationship}}
Desired outcome: {{desired_outcome}}
Tone to aim for: {{target_tone}}

Rewrite the email so it:
1. Keeps the core ask/message intact — do not soften it into vagueness
2. Removes accusatory or emotionally charged language
3. Ends with a clear, specific next step or ask
4. Matches the target tone

Output just the rewritten email with a subject line.`,
    notes:'Great for access-denial explanations or escalation emails where tone matters as much as content.'
  },
  {
    id:'seed-8', category:'planning', favorite:false, uses:0,
    name:'Process Improvement Brainstorm',
    desc:'Generates and prioritizes ideas to fix a recurring operational bottleneck.',
    tags:['planning','strategy','brainstorm'],
    template:`You are a business operations strategist helping solve a recurring bottleneck.

Bottleneck description: {{bottleneck_description}}
Current process (brief): {{current_process}}
Constraints (budget, tools, headcount, etc.): {{constraints}}

Do the following:
1. Identify the likely root cause(s) of the bottleneck, not just symptoms
2. Generate 5 possible improvements, ranging from quick fixes to structural changes
3. For each, note effort (Low/Med/High) and expected impact (Low/Med/High)
4. Recommend the single best next step to try first, and why

Be specific and practical — avoid generic advice like "improve communication."`,
    notes:'Best used when you already sense something is broken but haven\'t pinned down why.'
  },
];

/* ---- Prompt Builder block definitions ---- */
const PB_BLOCKS = [
  {key:'role', name:'Role', desc:'Tells the AI who to act as. Sets its expertise, vocabulary, and vantage point before it does anything else.', type:'select',
    options:['Senior Business Operations Analyst','Access & Compliance Reviewer','Executive Assistant / Ops Coordinator','Customer/Internal Support Triage Lead','Process Documentation Specialist','Custom role (type below)'],
    allowCustom:true, template:(v)=>`You are a ${v}.`},
  {key:'objective', name:'Objective', desc:'The single clear outcome you want. Vague objectives produce vague answers — this is usually the most important block.', type:'text',
    placeholder:'e.g. Draft a justification for extending database access by 90 days', template:(v)=>`Your objective: ${v}.`},
  {key:'context', name:'Context', desc:'Background info the AI needs but shouldn\'t have to guess — situation, audience, constraints, what already happened.', type:'textarea',
    placeholder:'e.g. This is for an internal auditor review; the requester already has read-only access.', template:(v)=>`Context:\n${v}`},
  {key:'constraints', name:'Constraints', desc:'Hard rules or limits the output must respect — length, format, things to avoid, compliance boundaries.', type:'textarea',
    placeholder:'e.g. Under 150 words. No legal claims. Do not mention specific employee names.', template:(v)=>`Constraints:\n${v}`},
  {key:'reasoning', name:'Reasoning strategy', desc:'How the AI should think before answering. This is separate from the output itself — it shapes the process, catching errors before they reach you.', type:'select',
    options:['Think step by step before answering','List assumptions first, then answer','Consider 2-3 options and pick the best one, explaining why','Identify risks/edge cases before finalizing','No special reasoning needed — answer directly'],
    template:(v)=> v==='No special reasoning needed — answer directly' ? '' : `Reasoning approach: ${v}.`},
  {key:'format', name:'Output format', desc:'The literal shape of the answer — email, table, bullet list, JSON, etc. Prevents having to reformat the response yourself.', type:'select',
    options:['A ready-to-send email with subject line','A numbered step-by-step list','A short paragraph (under 150 words)','A table with clear columns','Bullet points grouped under headers','Plain prose, no formatting'],
    template:(v)=>`Format your response as: ${v}.`},
  {key:'tone', name:'Tone', desc:'The voice and register of the writing — matters a lot for anything going to stakeholders, approvers, or customers.', type:'select',
    options:['Professional and neutral','Warm but firm','Concise and direct, no small talk','Formal / compliance-appropriate','Friendly and approachable'],
    template:(v)=>`Tone: ${v}.`},
  {key:'examples', name:'Examples', desc:'A sample of the kind of output you want. Even one good example dramatically improves consistency.', type:'textarea',
    placeholder:'Paste a past example of good output here (optional but powerful).', template:(v)=>`Example of the style/quality expected:\n"""\n${v}\n"""`},
  {key:'qualitycheck', name:'Quality checks', desc:'A self-review step — asks the AI to check its own output against criteria before giving it to you, catching mistakes early.', type:'textarea',
    placeholder:'e.g. Check that no confidential system names are mentioned; check tone is not accusatory.', template:(v)=>`Before finalizing, check your answer against these criteria and fix anything that fails:\n${v}`},
];

const LB_BLOCKS = [
  {key:'basetask', name:'Base task', desc:'The underlying task the loop will repeatedly attempt and refine — this is the "what" the loop is working on.', type:'textarea',
    placeholder:'e.g. Write a policy-compliant justification for this access request.', template:(v)=>`Task to iterate on:\n${v}`},
  {key:'goal', name:'Goal', desc:'The definition of "done." Loops need a concrete target, not just "make it better" — otherwise they never stop or never improve meaningfully.', type:'textarea',
    placeholder:'e.g. A justification an auditor would approve on first read, under 150 words.', template:(v)=>`Goal (definition of success):\n${v}`},
  {key:'evalcriteria', name:'Evaluation criteria', desc:'The specific yardstick the AI checks its own draft against each round. Without this, "self-improvement" is just guessing.', type:'textarea',
    placeholder:'e.g. 1) States exact access and duration 2) Explains business reason clearly 3) Notes least-privilege scope 4) Under 150 words', template:(v)=>`On each iteration, score the draft against this criteria (list what passes and what fails):\n${v}`},
  {key:'strategy', name:'Improvement strategy', desc:'How the AI should revise between rounds — e.g. fix only what failed, or rewrite from scratch. Keeps iterations efficient instead of random.', type:'select',
    options:['Fix only the specific criteria that failed, keep the rest unchanged','Rewrite fully each round using lessons from the previous attempt','Try 2 different approaches and keep the stronger one','Simplify and shorten with each pass'],
    template:(v)=>`Improvement strategy between rounds: ${v}.`},
  {key:'stopcond', name:'Stop conditions', desc:'When the loop must stop — either because it succeeded, or to prevent it from running forever. Every loop needs at least one.', type:'textarea',
    placeholder:'e.g. Stop when all evaluation criteria pass, or after 4 attempts — whichever comes first.', template:(v)=>`Stop the loop when:\n${v}`},
  {key:'safety', name:'Safety rules', desc:'Guardrails that apply no matter what round it is — things the loop should never do while trying to "improve," like inventing facts to satisfy criteria.', type:'textarea',
    placeholder:'e.g. Never invent policy details not provided. Never remove required disclaimers to shorten text.', template:(v)=>`Safety rules that apply on every iteration, even under pressure to pass evaluation:\n${v}`},
  {key:'showwork', name:'Show your work', desc:'Asks the AI to output its scoring/reasoning at each round, not just the final answer — so you can see why it stopped and trust the result.', type:'select',
    options:['Yes — show the score and reasoning for every round','No — only show the final passing draft'],
    template:(v)=> v.startsWith('Yes') ? 'After each iteration, briefly show: the draft, its score against each criterion, and what changed next round.' : 'Only output the final draft once stop conditions are met — do not show intermediate rounds.'},
];

/* ================= STATE ================= */
let workflows = [];
let pbBlocks = []; // {key, value}
let lbBlocks = [];
let currentEditId = null;
let currentUseId = null;
let activeCatFilter = null;
let favOnly = false;
let copyCount = 0;

/* ================= STORAGE ================= */
const LS_KEY = 'aiplaybook_workflows_v1';
const LS_META = 'aiplaybook_meta_v1';
const LS_ONBOARD = 'aiplaybook_onboarded_v1';
const LS_EXPLAINER = 'aiplaybook_explainer_dismissed_v1';
const LS_THEME = 'aiplaybook_theme_v1';

function loadWorkflows(){
  const raw = localStorage.getItem(LS_KEY);
  if(raw){ try{ workflows = JSON.parse(raw); return; }catch(e){} }
  workflows = JSON.parse(JSON.stringify(SEED_WORKFLOWS));
  saveWorkflows();
}
function saveWorkflows(){ localStorage.setItem(LS_KEY, JSON.stringify(workflows)); }
function loadMeta(){
  const raw = localStorage.getItem(LS_META);
  if(raw){ try{ const m = JSON.parse(raw); copyCount = m.copyCount||0; }catch(e){} }
}
function saveMeta(){ localStorage.setItem(LS_META, JSON.stringify({copyCount})); }

/* ================= UTIL ================= */
function uid(){ return 'wf-' + Date.now() + '-' + Math.random().toString(36).slice(2,7); }
function escapeHtml(s){ return (s||'').replace(/[&<>"']/g, c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
function extractVars(tpl){
  const set = new Set(); const re=/\{\{(.*?)\}\}/g; let m;
  while(m=re.exec(tpl||'')){ set.add(m[1].trim()); }
  return Array.from(set);
}
function fillTemplate(tpl, values){
  return (tpl||'').replace(/\{\{(.*?)\}\}/g, (m,k)=>{ k=k.trim(); return values[k]!==undefined && values[k]!=='' ? values[k] : `[${k}]`; });
}
function showToast(msg){
  const t = document.getElementById('toast');
  document.getElementById('toastMsg').textContent = msg;
  t.classList.add('show');
  clearTimeout(window._toastTimer);
  window._toastTimer = setTimeout(()=>t.classList.remove('show'), 2200);
}
function copyText(text, msg){
  navigator.clipboard.writeText(text).then(()=>{
    copyCount++; saveMeta(); renderStats();
    showToast(msg || 'Copied to clipboard');
  }).catch(()=>{
    const ta=document.createElement('textarea'); ta.value=text; document.body.appendChild(ta); ta.select();
    document.execCommand('copy'); document.body.removeChild(ta);
    copyCount++; saveMeta(); renderStats();
    showToast(msg || 'Copied to clipboard');
  });
}

/* ================= NAVIGATION ================= */
const VIEW_TITLES = {
  dashboard:['Dashboard','Your saved AI prompt workflows, at a glance'],
  workflows:['Workflows','Reusable, editable prompt systems for your recurring tasks'],
  promptbuilder:['Prompt Builder','Assemble a custom prompt from labeled building blocks'],
  loopbuilder:['Loop Builder','Turn any prompt into a self-checking, iterating one'],
  library:['Building Blocks','Reference library of every block used above'],
  guide:['How this works','A plain-language walkthrough of the whole tool'],
};
function goView(name){
  document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));
  document.getElementById('view-'+name).classList.add('active');
  document.querySelectorAll('.nav-item').forEach(b=>b.classList.toggle('active', b.dataset.view===name));
  document.getElementById('topbarTitle').textContent = VIEW_TITLES[name][0];
  document.getElementById('topbarSub').textContent = VIEW_TITLES[name][1];
  window.scrollTo({top:0,behavior:'smooth'});
  if(window.innerWidth<=820) document.getElementById('sidebar').classList.remove('open');
}
document.querySelectorAll('.nav-item[data-view]').forEach(b=>b.addEventListener('click', ()=>goView(b.dataset.view)));
document.querySelectorAll('[data-view-link]').forEach(b=>b.addEventListener('click', ()=>goView(b.dataset.viewLink)));

/* ================= RENDER: DASHBOARD & WORKFLOWS ================= */
function renderStats(){
  document.getElementById('statTotal').textContent = workflows.length;
  document.getElementById('statFav').textContent = workflows.filter(w=>w.favorite).length;
  document.getElementById('statCats').textContent = new Set(workflows.map(w=>w.category)).size;
  document.getElementById('statCopies').textContent = copyCount;
}

function wfCardHtml(w){
  const c = catInfo(w.category);
  return `
  <div class="wf-card" style="border-top-color:${c.color}" data-id="${w.id}">
    <div class="wf-top">
      <div>
        <div class="wf-cat" style="color:${c.color}">${escapeHtml(c.name)}</div>
        <div class="wf-title">${escapeHtml(w.name)}</div>
      </div>
      <button class="fav-btn ${w.favorite?'active':''}" data-fav="${w.id}" title="Favorite">
        <svg viewBox="0 0 24 24" fill="${w.favorite?'currentColor':'none'}" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
      </button>
    </div>
    <div class="wf-desc">${escapeHtml(w.desc||'')}</div>
    <div class="wf-tags">${(w.tags||[]).map(t=>`<span class="tag">${escapeHtml(t)}</span>`).join('')}</div>
    <div class="wf-actions">
      <button class="btn sm accent" data-use="${w.id}" style="flex:1;">Use workflow</button>
      <button class="btn sm" data-edit="${w.id}" title="Edit">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:13px;height:13px;"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.12 2.12 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
      </button>
      <button class="btn sm" data-dup="${w.id}" title="Duplicate">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:13px;height:13px;"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
      </button>
      <button class="btn sm" data-del="${w.id}" title="Delete">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:13px;height:13px;"><polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"/><path d="M10 11v6M14 11v6"/></svg>
      </button>
    </div>
  </div>`;
}

function emptyStateHtml(msg, sub){
  return `<div class="empty-state" style="grid-column:1/-1;">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-4"/><path d="M17 3h4v4"/><path d="M21 3l-9 9"/></svg>
    <h4>${msg}</h4><p>${sub}</p>
  </div>`;
}

function renderDashboard(){
  const favs = workflows.filter(w=>w.favorite).slice(0,3);
  const favGrid = document.getElementById('favGrid');
  favGrid.innerHTML = favs.length ? favs.map(wfCardHtml).join('') : emptyStateHtml('No favorites yet','Star a workflow from the Workflows tab to pin it here for quick access.');
  const recent = [...workflows].reverse().slice(0,6);
  document.getElementById('recentGrid').innerHTML = recent.length ? recent.map(wfCardHtml).join('') : emptyStateHtml('No workflows yet','Create your first workflow, or build one in the Prompt Builder and save it.');
  renderStats();
}

function renderCatRow(){
  const row = document.getElementById('catFilterRow');
  const used = CATEGORIES.filter(c=>workflows.some(w=>w.category===c.id));
  let html = `<button class="chip ${activeCatFilter===null?'active':''}" data-cat="all">All categories</button>`;
  html += used.map(c=>`<button class="chip ${activeCatFilter===c.id?'active':''}" data-cat="${c.id}"><span class="dot" style="background:${c.color}"></span>${escapeHtml(c.name)}</button>`).join('');
  row.innerHTML = html;
  row.querySelectorAll('[data-cat]').forEach(b=>b.addEventListener('click', ()=>{
    activeCatFilter = b.dataset.cat==='all' ? null : b.dataset.cat;
    renderWorkflowsView();
  }));
}

function renderWorkflowsView(){
  renderCatRow();
  const q = (document.getElementById('wfSearch').value||'').toLowerCase().trim();
  let list = workflows.filter(w=>{
    if(activeCatFilter && w.category!==activeCatFilter) return false;
    if(favOnly && !w.favorite) return false;
    if(q){
      const hay = (w.name+' '+w.desc+' '+(w.tags||[]).join(' ')+' '+w.template).toLowerCase();
      if(!hay.includes(q)) return false;
    }
    return true;
  });
  const grid = document.getElementById('allGrid');
  grid.innerHTML = list.length ? [...list].reverse().map(wfCardHtml).join('') : emptyStateHtml('No workflows match', 'Try a different search term or clear filters.');
}

document.getElementById('wfSearch').addEventListener('input', renderWorkflowsView);
document.getElementById('favFilterBtn').addEventListener('click', function(){
  favOnly = !favOnly; this.classList.toggle('primary', favOnly); this.style.background = favOnly?'var(--accent)':''; this.style.color = favOnly?'#fff':'';
  this.style.borderColor = favOnly?'var(--accent)':''; renderWorkflowsView();
});

// event delegation for card actions
document.addEventListener('click', function(e){
  const fav = e.target.closest('[data-fav]');
  const use = e.target.closest('[data-use]');
  const edit = e.target.closest('[data-edit]');
  const dup = e.target.closest('[data-dup]');
  const del = e.target.closest('[data-del]');
  if(fav){ toggleFav(fav.dataset.fav); }
  if(use){ openUseModal(use.dataset.use); }
  if(edit){ openEditModal(edit.dataset.edit); }
  if(dup){ duplicateWorkflow(dup.dataset.dup); }
  if(del){ deleteWorkflow(del.dataset.del); }
});

function toggleFav(id){
  const w = workflows.find(x=>x.id===id); if(!w) return;
  w.favorite = !w.favorite; saveWorkflows(); renderAll();
}
function duplicateWorkflow(id){
  const w = workflows.find(x=>x.id===id); if(!w) return;
  const copy = JSON.parse(JSON.stringify(w));
  copy.id = uid(); copy.name = w.name + ' (copy)'; copy.favorite=false;
  workflows.push(copy); saveWorkflows(); renderAll();
  showToast('Workflow duplicated');
}
function deleteWorkflow(id){
  if(!confirm('Delete this workflow? This cannot be undone.')) return;
  workflows = workflows.filter(x=>x.id!==id); saveWorkflows(); renderAll();
  showToast('Workflow deleted');
}

/* ============ Create/Edit Workflow Modal ============ */
const catSelect = document.getElementById('fCategory');
catSelect.innerHTML = CATEGORIES.map(c=>`<option value="${c.id}">${escapeHtml(c.name)}</option>`).join('');

function openNewModal(prefill){
  currentEditId = null;
  document.getElementById('wfModalTitle').textContent = 'New workflow';
  document.getElementById('fName').value = prefill?.name || '';
  document.getElementById('fCategory').value = prefill?.category || CATEGORIES[0].id;
  document.getElementById('fDesc').value = prefill?.desc || '';
  document.getElementById('fTags').value = (prefill?.tags||[]).join(', ');
  document.getElementById('fTemplate').value = prefill?.template || '';
  document.getElementById('fNotes').value = prefill?.notes || '';
  document.getElementById('wfModalOverlay').classList.add('active');
  setTimeout(()=>document.getElementById('fName').focus(),50);
}
function openEditModal(id){
  const w = workflows.find(x=>x.id===id); if(!w) return;
  currentEditId = id;
  document.getElementById('wfModalTitle').textContent = 'Edit workflow';
  document.getElementById('fName').value = w.name;
  document.getElementById('fCategory').value = w.category;
  document.getElementById('fDesc').value = w.desc||'';
  document.getElementById('fTags').value = (w.tags||[]).join(', ');
  document.getElementById('fTemplate').value = w.template||'';
  document.getElementById('fNotes').value = w.notes||'';
  document.getElementById('wfModalOverlay').classList.add('active');
}
function closeWfModal(){ document.getElementById('wfModalOverlay').classList.remove('active'); }
document.getElementById('newWorkflowBtn').addEventListener('click', ()=>openNewModal());
document.getElementById('wfModalClose').addEventListener('click', closeWfModal);
document.getElementById('wfCancelBtn').addEventListener('click', closeWfModal);
document.getElementById('wfSaveBtn').addEventListener('click', function(){
  const name = document.getElementById('fName').value.trim();
  if(!name){ showToast('Please enter a workflow name'); return; }
  const data = {
    name, category: document.getElementById('fCategory').value,
    desc: document.getElementById('fDesc').value.trim(),
    tags: document.getElementById('fTags').value.split(',').map(t=>t.trim()).filter(Boolean),
    template: document.getElementById('fTemplate').value,
    notes: document.getElementById('fNotes').value.trim(),
  };
  if(currentEditId){
    const w = workflows.find(x=>x.id===currentEditId);
    Object.assign(w, data);
  } else {
    workflows.push(Object.assign({id:uid(), favorite:false, uses:0}, data));
  }
  saveWorkflows(); closeWfModal(); renderAll();
  showToast(currentEditId ? 'Workflow updated' : 'Workflow created');
});

/* ============ Use Workflow Modal ============ */
function openUseModal(id){
  const w = workflows.find(x=>x.id===id); if(!w) return;
  currentUseId = id;
  document.getElementById('useModalTitle').textContent = w.name;
  document.getElementById('useNotesText').textContent = w.notes || 'No additional notes for this workflow.';
  const vars = extractVars(w.template);
  const wrap = document.getElementById('useVarFields');
  wrap.innerHTML = vars.map(v=>`
    <div class="field">
      <label>${escapeHtml(v.replace(/_/g,' '))}</label>
      <textarea data-var="${escapeHtml(v)}" style="min-height:44px; font-family:var(--font-body);" placeholder="Enter ${escapeHtml(v.replace(/_/g,' '))}…"></textarea>
    </div>`).join('') || '<div class="small-note">This workflow has no variables — the prompt is ready to copy as-is.</div>';
  wrap.querySelectorAll('textarea').forEach(t=>t.addEventListener('input', updateUsePreview));
  updateUsePreview();
  document.getElementById('useModalOverlay').classList.add('active');
}
function updateUsePreview(){
  const w = workflows.find(x=>x.id===currentUseId); if(!w) return;
  const values = {};
  document.querySelectorAll('#useVarFields [data-var]').forEach(el=>values[el.dataset.var]=el.value);
  document.getElementById('useFilledPreview').textContent = fillTemplate(w.template, values);
}
document.getElementById('useModalClose').addEventListener('click', ()=>document.getElementById('useModalOverlay').classList.remove('active'));
document.getElementById('useCloseBtn').addEventListener('click', ()=>document.getElementById('useModalOverlay').classList.remove('active'));
document.getElementById('useCopyBtn').addEventListener('click', ()=>{
  const text = document.getElementById('useFilledPreview').textContent;
  const w = workflows.find(x=>x.id===currentUseId);
  if(w){ w.uses = (w.uses||0)+1; saveWorkflows(); }
  copyText(text, 'Filled prompt copied');
});

/* ================= BUILDING BLOCKS LIBRARY VIEW ================= */
function renderLibrary(){
  const el = document.getElementById('libraryList');
  function group(title, blocks, cls){
    return `<div class="section-head" style="margin-top:24px;"><div><h2 style="font-size:16px;">${title}</h2></div></div>
    <div class="workflow-grid">${blocks.map(b=>`
      <div class="wf-card" style="border-top-color:${cls==='loop'?'var(--amber)':'var(--accent)'}">
        <div class="wf-title">${escapeHtml(b.name)}</div>
        <div class="wf-desc">${escapeHtml(b.desc)}</div>
      </div>`).join('')}</div>`;
  }
  el.innerHTML = group('Prompt Builder blocks', PB_BLOCKS, 'prompt') + group('Loop Builder elements', LB_BLOCKS, 'loop');
}

/* ================= GUIDE VIEW ================= */
function renderGuide(){
  document.getElementById('guideContent').innerHTML = `
    <div class="guide-section">
      <h5>Dashboard</h5>
      <p class="small-note">A quick snapshot: how many workflows you've saved, which are favorited, and your most recent ones. It's the "home base" — start here to jump into anything.</p>
    </div>
    <div class="guide-section">
      <h5>Workflows</h5>
      <p class="small-note">Your library of saved, reusable prompt templates. Each one has editable variables (shown as blanks like <span class="mono">{{business_reason}}</span>) that you fill in when you click "Use workflow" — no retyping the whole prompt each time. Filter by category, search, favorite, duplicate, edit, or delete any of them.</p>
    </div>
    <div class="guide-section">
      <h5>Prompt Builder</h5>
      <p class="small-note">For one-off prompts you haven't saved as a workflow yet. Add blocks (Role, Objective, Context, etc.) from the left panel — each has a short explanation of what it does. Fill them in and watch the prompt assemble itself in the live preview. Copy it, or save it as a permanent workflow.</p>
    </div>
    <div class="guide-section">
      <h5>Loop Builder</h5>
      <p class="small-note"><strong>"Looping"</strong> means asking the AI to draft, self-evaluate against your criteria, revise, and repeat — instead of accepting the first answer. You define the Goal (what "done" looks like), Evaluation criteria (the checklist), Stop conditions (when to stop trying), and Safety rules (limits that apply on every attempt). This is more advanced than a normal prompt, but produces higher-quality results for tasks where "good enough on the first try" isn't good enough.</p>
    </div>
    <div class="guide-section">
      <h5>Building Blocks</h5>
      <p class="small-note">A plain reference list of every block used in the two builders above, in case you want to understand them without building anything yet.</p>
    </div>
    <div class="guide-section">
      <h5>Your data</h5>
      <p class="small-note">Everything saves to this browser's local storage automatically. Use "Export data" in the sidebar to download a backup JSON file, and "Import data" to restore it (e.g. on a new device or browser).</p>
    </div>
  `;
}

/* ================= PROMPT BUILDER ================= */
function renderPicker(containerId, blockDefs, currentList, isLoop){
  const el = document.getElementById(containerId);
  el.innerHTML = blockDefs.map(b=>{
    const already = currentList.some(x=>x.key===b.key);
    return `<div class="picker-item" data-add="${b.key}" style="opacity:${already?0.45:1}">
      <div class="pi-top"><span class="pi-name">${escapeHtml(b.name)}</span><span class="pi-add">${already?'✓':'+'}</span></div>
      <div class="pi-desc">${escapeHtml(b.desc)}</div>
    </div>`;
  }).join('');
  el.querySelectorAll('[data-add]').forEach(item=>{
    item.addEventListener('click', ()=>{
      const key = item.dataset.add;
      if(currentList.some(x=>x.key===key)) return;
      currentList.push({key, value:''});
      if(isLoop){ renderLB(); } else { renderPB(); }
    });
  });
}

function renderAssembled(containerId, blockDefs, currentList, isLoop, onChange){
  const el = document.getElementById(containerId);
  if(!currentList.length){
    el.innerHTML = `<div class="assembled-empty">No blocks added yet. Pick some from the left to start building your ${isLoop?'looping':''} prompt.</div>`;
    return;
  }
  el.innerHTML = currentList.map((item,idx)=>{
    const def = blockDefs.find(b=>b.key===item.key);
    let inputHtml = '';
    if(def.type==='select'){
      inputHtml = `<select data-idx="${idx}" data-field="value">
        <option value="">Choose…</option>
        ${def.options.map(o=>`<option value="${escapeHtml(o)}" ${item.value===o?'selected':''}>${escapeHtml(o)}</option>`).join('')}
      </select>`;
      if(def.allowCustom){
        inputHtml += `<input type="text" style="margin-top:6px;" data-idx="${idx}" data-field="custom" placeholder="Or type a custom value…" value="${item.value && !def.options.includes(item.value)?escapeHtml(item.value):''}">`;
      }
    } else if(def.type==='textarea'){
      inputHtml = `<textarea data-idx="${idx}" data-field="value" placeholder="${escapeHtml(def.placeholder||'')}">${escapeHtml(item.value)}</textarea>`;
    } else {
      inputHtml = `<input type="text" data-idx="${idx}" data-field="value" placeholder="${escapeHtml(def.placeholder||'')}" value="${escapeHtml(item.value)}">`;
    }
    return `<div class="ab-item ${isLoop?'loop':''}">
      <div class="ab-head">
        <span class="ab-name">${escapeHtml(def.name)}</span>
        <button class="ab-remove" data-remove="${idx}">✕</button>
      </div>
      <div class="ab-why">${escapeHtml(def.desc)}</div>
      ${inputHtml}
    </div>`;
  }).join('');
  el.querySelectorAll('[data-remove]').forEach(btn=>btn.addEventListener('click', ()=>{
    currentList.splice(parseInt(btn.dataset.remove),1);
    onChange();
  }));
  el.querySelectorAll('select,textarea,input').forEach(inp=>inp.addEventListener('input', ()=>{
    const idx = parseInt(inp.dataset.idx);
    if(inp.dataset.field==='custom'){ currentList[idx].value = inp.value; }
    else { currentList[idx].value = inp.value; }
    updatePreview(isLoop);
  }));
}

function buildPreviewText(blockDefs, currentList){
  return currentList.map(item=>{
    const def = blockDefs.find(b=>b.key===item.key);
    if(!item.value) return '';
    return def.template(item.value);
  }).filter(Boolean).join('\n\n');
}
function updatePreview(isLoop){
  if(isLoop){ document.getElementById('lbPreview').textContent = buildPreviewText(LB_BLOCKS, lbBlocks) || 'Your assembled loop prompt will appear here as you fill in blocks.'; }
  else { document.getElementById('pbPreview').textContent = buildPreviewText(PB_BLOCKS, pbBlocks) || 'Your assembled prompt will appear here as you fill in blocks.'; }
}
function renderPB(){
  renderPicker('pbPicker', PB_BLOCKS, pbBlocks, false);
  renderAssembled('pbAssembled', PB_BLOCKS, pbBlocks, false, renderPB);
  updatePreview(false);
}
function renderLB(){
  renderPicker('lbPicker', LB_BLOCKS, lbBlocks, true);
  renderAssembled('lbAssembled', LB_BLOCKS, lbBlocks, true, renderLB);
  updatePreview(true);
}
document.getElementById('pbCopy').addEventListener('click', ()=>{
  const t = buildPreviewText(PB_BLOCKS, pbBlocks);
  if(!t){ showToast('Add some blocks first'); return; }
  copyText(t, 'Prompt copied');
});
document.getElementById('lbCopy').addEventListener('click', ()=>{
  const t = buildPreviewText(LB_BLOCKS, lbBlocks);
  if(!t){ showToast('Add some elements first'); return; }
  copyText(t, 'Loop prompt copied');
});
document.getElementById('pbReset').addEventListener('click', ()=>{ pbBlocks=[]; renderPB(); });
document.getElementById('lbReset').addEventListener('click', ()=>{ lbBlocks=[]; renderLB(); });
document.getElementById('pbSaveAsWorkflow').addEventListener('click', ()=>{
  const t = buildPreviewText(PB_BLOCKS, pbBlocks);
  if(!t){ showToast('Add some blocks first'); return; }
  goView('workflows');
  openNewModal({name:'New prompt-builder workflow', category:'planning', desc:'Created from Prompt Builder', tags:['custom'], template:t});
});
document.getElementById('lbSaveAsWorkflow').addEventListener('click', ()=>{
  const t = buildPreviewText(LB_BLOCKS, lbBlocks);
  if(!t){ showToast('Add some elements first'); return; }
  goView('workflows');
  openNewModal({name:'New looping workflow', category:'planning', desc:'Created from Loop Builder', tags:['custom','loop'], template:t});
});

/* ================= THEME ================= */
function setTheme(t){
  document.body.setAttribute('data-theme', t);
  document.getElementById('themeLabel').textContent = t==='dark' ? 'Light mode' : 'Dark mode';
  localStorage.setItem(LS_THEME, t);
}
document.getElementById('themeToggle').addEventListener('click', ()=>{
  setTheme(document.body.getAttribute('data-theme')==='dark' ? 'light' : 'dark');
});

/* ================= EXPLAINER BANNER ================= */
document.getElementById('explainerClose').addEventListener('click', ()=>{
  document.getElementById('explainerBanner').style.display = 'none';
  localStorage.setItem(LS_EXPLAINER, '1');
});
document.getElementById('whatIsThisBtn').addEventListener('click', ()=>document.getElementById('helpModalOverlay').classList.add('active'));
document.getElementById('helpModalClose').addEventListener('click', ()=>document.getElementById('helpModalOverlay').classList.remove('active'));
document.getElementById('helpGotIt').addEventListener('click', ()=>document.getElementById('helpModalOverlay').classList.remove('active'));

/* ================= SHORTCUTS MODAL ================= */
document.getElementById('shortcutsBtn').addEventListener('click', ()=>document.getElementById('shortcutsModalOverlay').classList.add('active'));
document.getElementById('shortcutsModalClose').addEventListener('click', ()=>document.getElementById('shortcutsModalOverlay').classList.remove('active'));
document.getElementById('shortcutsGotIt').addEventListener('click', ()=>document.getElementById('shortcutsModalOverlay').classList.remove('active'));

document.querySelectorAll('.modal-overlay').forEach(ov=>{
  ov.addEventListener('click', (e)=>{ if(e.target===ov) ov.classList.remove('active'); });
});

/* ================= KEYBOARD SHORTCUTS ================= */
let gPending = false;
document.addEventListener('keydown', (e)=>{
  const tag = document.activeElement.tagName;
  const typing = tag==='INPUT' || tag==='TEXTAREA' || tag==='SELECT';
  if(e.key==='Escape'){ document.querySelectorAll('.modal-overlay.active').forEach(m=>m.classList.remove('active')); gPending=false; return; }
  if(typing) return;
  if(gPending){
    gPending=false;
    if(e.key==='d') goView('dashboard');
    if(e.key==='w') goView('workflows');
    if(e.key==='p') goView('promptbuilder');
    if(e.key==='l') goView('loopbuilder');
    return;
  }
  if(e.key==='g' || e.key==='G'){ gPending=true; setTimeout(()=>gPending=false,1200); return; }
  if(e.key==='n' || e.key==='N'){ openNewModal(); return; }
  if(e.key==='/'){ e.preventDefault(); goView('workflows'); setTimeout(()=>document.getElementById('wfSearch').focus(),100); return; }
  if(e.key==='?'){ document.getElementById('helpModalOverlay').classList.add('active'); return; }
  if(e.key==='D' && e.shiftKey){ setTheme(document.body.getAttribute('data-theme')==='dark'?'light':'dark'); return; }
});

/* ================= IMPORT / EXPORT ================= */
document.getElementById('exportBtn').addEventListener('click', ()=>{
  const data = {workflows, exportedAt:new Date().toISOString()};
  const blob = new Blob([JSON.stringify(data,null,2)], {type:'application/json'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob); a.download = 'ai-playbook-backup.json'; a.click();
  showToast('Backup downloaded');
});
document.getElementById('importBtn').addEventListener('click', ()=>document.getElementById('importFile').click());
document.getElementById('importFile').addEventListener('change', (e)=>{
  const file = e.target.files[0]; if(!file) return;
  const reader = new FileReader();
  reader.onload = (ev)=>{
    try{
      const data = JSON.parse(ev.target.result);
      if(data.workflows && Array.isArray(data.workflows)){
        workflows = data.workflows; saveWorkflows(); renderAll();
        showToast('Data imported successfully');
      } else { showToast('That file doesn\'t look like a valid backup'); }
    }catch(err){ showToast('Could not read that file'); }
  };
  reader.readAsText(file);
  e.target.value='';
});

/* ================= MOBILE MENU ================= */
if(window.innerWidth<=820){ document.getElementById('menuToggle').style.display='flex'; }
document.getElementById('menuToggle').addEventListener('click', ()=>document.getElementById('sidebar').classList.toggle('open'));

/* ================= ONBOARDING ================= */
const ONBOARD_STEPS = [
  {icon:`<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 2-3 4"/><line x1="12" y1="17" x2="12.01" y2="17"/>`,
   title:'Welcome to your AI Playbook', body:'This is a personal system built around how you actually use AI in ops &amp; access management support — for reusing prompts instead of rewriting them each time. It\'s pre-loaded with 8 workflows tailored to your role. Everything stays on this device.'},
  {icon:`<path d="M9 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-4"/><path d="M17 3h4v4"/><path d="M21 3l-9 9"/>`,
   title:'Workflows are your starting point', body:'Head to <strong>Workflows</strong> to browse ready-made templates like "Access Request Justification Writer" or "Ticket Triage" — click "Use workflow" to fill in the blanks and copy a finished prompt in seconds.'},
  {icon:`<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 8h10M7 12h6M7 16h4"/>`,
   title:'Build custom prompts from pieces', body:'Need something new? Use the <strong>Prompt Builder</strong> to assemble a prompt from labeled pieces — role, objective, tone, and more — with a live preview as you go. Save any result as a new workflow.'},
  {icon:`<path d="M17 2l4 4-4 4"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><path d="M7 22l-4-4 4-4"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/>`,
   title:'Loop Builder, when you want more rigor', body:'For tasks where the first draft isn\'t good enough, the <strong>Loop Builder</strong> teaches you to build prompts that self-check against your own criteria before finishing. Look for the "What is this?" button any time you need a refresher.'},
];
let onboardIdx = 0;
function renderOnboard(){
  const step = ONBOARD_STEPS[onboardIdx];
  document.getElementById('onboardSteps').innerHTML = ONBOARD_STEPS.map((_,i)=>`<span class="${i<=onboardIdx?'done':''}"></span>`).join('');
  document.getElementById('onboardContent').innerHTML = `
    <div class="onboard-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">${step.icon}</svg></div>
    <h3>${step.title}</h3>
    <p>${step.body}</p>
    <div class="onboard-foot">
      <button class="btn sm" id="onboardSkip">Skip intro</button>
      <button class="btn sm primary" id="onboardNext">${onboardIdx===ONBOARD_STEPS.length-1 ? 'Get started' : 'Next'}</button>
    </div>`;
  document.getElementById('onboardSkip').addEventListener('click', finishOnboard);
  document.getElementById('onboardNext').addEventListener('click', ()=>{
    if(onboardIdx===ONBOARD_STEPS.length-1){ finishOnboard(); } else { onboardIdx++; renderOnboard(); }
  });
}
function finishOnboard(){
  document.getElementById('onboardOverlay').style.display='none';
  localStorage.setItem(LS_ONBOARD,'1');
}

/* ================= INIT ================= */
function renderAll(){
  renderDashboard();
  renderWorkflowsView();
  renderLibrary();
}
function init(){
  loadWorkflows();
  loadMeta();
  const savedTheme = localStorage.getItem(LS_THEME);
  if(savedTheme) setTheme(savedTheme);
  if(localStorage.getItem(LS_EXPLAINER)) document.getElementById('explainerBanner').style.display='none';
  renderAll();
  renderPB();
  renderLB();
  renderGuide();
  if(!localStorage.getItem(LS_ONBOARD)){
    document.getElementById('onboardOverlay').style.display='flex';
    onboardIdx=0; renderOnboard();
  } else {
    document.getElementById('onboardOverlay').style.display='none';
  }
}
init();
</script>
</body>
</html>
<img width="1325" height="1259" alt="image" src="https://github.com/user-attachments/assets/36fc39ff-bc7f-463f-9e7f-e9e2e20b3c91" />
<img width="1330" height="1261" alt="image" src="https://github.com/user-attachments/assets/e087fe7a-4a0b-4bb4-92a3-3f878211a6e1" />
<img width="900" height="540" alt="image" src="https://github.com/user-attachments/assets/a87d810a-2553-4205-ac04-4554cf6d39e9" />
<img width="900" height="540" alt="image" src="https://github.com/user-attachments/assets/eaa73bf5-7bb8-4b34-b075-a8e50307b9da" />
Last one's screenshot's internal matter:-
Rewrite the email so it:
1. Keeps the core ask/message intact — do not soften it into vagueness
2. Removes accusatory or emotionally charged language
3. Ends with a clear, specific next step or ask
4. Matches the target tone
Final out come on Claude:- 
<img width="752" height="278" alt="image" src="https://github.com/user-attachments/assets/4988858e-610a-475a-8f57-b057234f3798" />

Output just the rewritten email with a subject line.
