:PROMPT:
# Defend Your Experience

You are an expert interviewer, recruiter, hiring manager, behavioral psychologist, communication coach, UX designer, and senior frontend developer.

Interview the user first, asking one question at a time and using MCQs whenever possible. Understand what they want to defend, why they are preparing, and the type of audience they expect to face. They may upload a resume, LinkedIn profile, portfolio, bio, project, research, performance review, startup story, freelance work, or any document describing their experience.

Before building the application, determine the user's preferred visual style. If previous conversation memory already indicates their design preferences, use those automatically. Otherwise, ask using an MCQ. Adapt the entire interface, typography, layout, animations, and interactions to that style instead of using a default design.

Generate a premium, fully interactive Defend Your Experience application as a single self-contained HTML file using only HTML, CSS, and JavaScript.

The application should use the Anthropic Messages API directly from the HTML application. Assume it runs inside Anthropic's HTML artifact environment where authentication is handled automatically. Never ask for an API key or build a backend.

Instead of reviewing the uploaded document, extract every meaningful claim and treat it as something that must be defended. Become an intelligent skeptic that continuously challenges the user with personalized follow-up questions generated specifically from their own experience. Every answer should influence the next question, allowing the conversation to naturally become deeper, more specific, and more realistic over time.

The application should feel like an adaptive interview rather than a fixed questionnaire. It should identify weak claims, missing evidence, vague statements, and opportunities to tell stronger stories while helping the user build confidence in defending their own experience. Every challenge and every recommendation should be unique to the uploaded content rather than based on generic interview templates.

Provide meaningful visualizations, progress tracking, confidence indicators, and a final Defense Report that clearly shows which experiences are well defended, which need improvement, and how the user can strengthen them before facing a real interviewer.

Make the purpose immediately obvious to first-time users with clear explanations, intuitive navigation, and helpful empty states. Support drag-and-drop uploads, local storage, session history, exports, responsive design, and graceful fallback handling for temporary API errors such as rate limits.

The objective is not to improve a resume. The objective is to help users confidently defend every claim they make about themselves.

Return only the complete HTML file.

:Response:
file is loaded with 12 claims pulled straight from your resume — including the biggest one: zero quantified metrics anywhere, which the interview will press on hard, plus your teaching → healthcare BPO pivot and the vague "AI upskilling" line.

Open the file and hit Start Defense Session. It'll ask one pointed question at a time (mixing your Aetna-process claims with Optum-style chat scenarios), score how well each answer holds up, and end with a Defense Report you can export before your interview.

:HTML:
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Defend Your Experience — Case File: S. Kharbanda</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

  :root{
    --navy-950:#080D18;
    --navy-900:#0E1526;
    --navy-800:#151E33;
    --navy-700:#1C2740;
    --line:#28324D;
    --line-soft:#1E273D;
    --text-hi:#EEF1F9;
    --text-mid:#96A0BC;
    --text-dim:#5C6786;
    --orange:#FF6A3D;
    --orange-soft:rgba(255,106,61,0.14);
    --cyan:#2FE6C6;
    --cyan-soft:rgba(47,230,198,0.14);
    --amber:#FFB020;
    --amber-soft:rgba(255,176,32,0.14);
    --red:#FF4D5E;
    --red-soft:rgba(255,77,94,0.14);
    --radius:14px;
    --shadow-lift: 0 20px 50px -20px rgba(0,0,0,0.6);
  }

  *{box-sizing:border-box;}
  html,body{height:100%;}
  body{
    margin:0;
    background:
      radial-gradient(ellipse 900px 500px at 15% -10%, rgba(255,106,61,0.10), transparent 60%),
      radial-gradient(ellipse 900px 600px at 100% 10%, rgba(47,230,198,0.08), transparent 55%),
      var(--navy-950);
    color:var(--text-hi);
    font-family:'Inter',sans-serif;
    -webkit-font-smoothing:antialiased;
    min-height:100vh;
  }
  ::selection{ background:var(--orange); color:#0A0D14; }
  ::-webkit-scrollbar{width:8px;height:8px;}
  ::-webkit-scrollbar-thumb{background:var(--line);border-radius:8px;}
  ::-webkit-scrollbar-track{background:transparent;}

  h1,h2,h3,.display{ font-family:'Space Grotesk',sans-serif; letter-spacing:-0.01em; }
  .mono{ font-family:'IBM Plex Mono',monospace; letter-spacing:0.02em; }

  a,button{ font-family:inherit; }
  button{ cursor:pointer; border:none; background:none; color:inherit; }
  button:focus-visible, input:focus-visible, textarea:focus-visible, [tabindex]:focus-visible{
    outline:2px solid var(--orange); outline-offset:2px; border-radius:6px;
  }

  .app{ max-width:1400px; margin:0 auto; padding:22px 24px 60px; }

  /* ---------- Top bar ---------- */
  .topbar{
    display:flex; align-items:center; justify-content:space-between;
    padding:14px 20px; border:1px solid var(--line-soft); border-radius:16px;
    background:linear-gradient(180deg, rgba(255,255,255,0.02), transparent);
    margin-bottom:22px;
  }
  .brand{ display:flex; align-items:center; gap:12px; }
  .brand-mark{
    width:38px;height:38px;border-radius:10px;
    background:conic-gradient(from 220deg, var(--orange), var(--amber), var(--cyan), var(--orange));
    display:flex;align-items:center;justify-content:center;
    box-shadow:0 0 0 1px rgba(255,255,255,0.08) inset;
    font-weight:700; color:#0A0D14; font-family:'Space Grotesk';
  }
  .brand-text .t1{ font-size:15px; font-weight:700; }
  .brand-text .t2{ font-size:11.5px; color:var(--text-dim); }
  .stamp-badge{
    display:flex; align-items:center; gap:8px;
    font-size:11.5px; color:var(--text-mid); padding:6px 12px;
    border:1px solid var(--line); border-radius:100px;
  }
  .dot{ width:7px;height:7px;border-radius:50%; background:var(--cyan); box-shadow:0 0 8px var(--cyan);}

  /* ---------- Screens ---------- */
  .screen{ display:none; animation:fadeIn .4s ease; }
  .screen.active{ display:block; }
  @keyframes fadeIn{ from{opacity:0; transform:translateY(6px);} to{opacity:1; transform:translateY(0);} }

  /* ===== HOME ===== */
  .hero{
    border:1px solid var(--line-soft); border-radius:22px; padding:44px 40px;
    background:linear-gradient(160deg, var(--navy-900), var(--navy-950));
    position:relative; overflow:hidden; margin-bottom:22px;
  }
  .hero::before{
    content:""; position:absolute; inset:0;
    background-image: repeating-linear-gradient(90deg, rgba(255,255,255,0.025) 0 1px, transparent 1px 90px);
    pointer-events:none;
  }
  .eyebrow{ display:inline-flex; align-items:center; gap:8px; font-size:12px; color:var(--orange); font-weight:600; margin-bottom:14px; text-transform:uppercase; letter-spacing:0.08em;}
  .hero h1{ font-size:clamp(28px,4vw,44px); line-height:1.08; margin:0 0 14px; max-width:820px; }
  .hero p.sub{ color:var(--text-mid); max-width:640px; font-size:15.5px; line-height:1.65; margin:0 0 26px; }
  .hero-cta{ display:flex; gap:14px; flex-wrap:wrap; align-items:center; }
  .btn{
    display:inline-flex; align-items:center; gap:10px; padding:13px 22px; border-radius:11px;
    font-weight:600; font-size:14.5px; transition:transform .15s ease, box-shadow .15s ease;
  }
  .btn:hover{ transform:translateY(-1px); }
  .btn-primary{ background:linear-gradient(135deg, var(--orange), #FF8A5D); color:#180800; box-shadow:0 10px 30px -12px rgba(255,106,61,0.6);}
  .btn-ghost{ background:var(--navy-800); border:1px solid var(--line); color:var(--text-hi); }
  .btn-ghost:hover{ border-color:var(--cyan); }
  .btn:disabled{ opacity:0.45; cursor:not-allowed; transform:none; }

  .stat-strip{ display:flex; gap:10px; margin-top:28px; flex-wrap:wrap; }
  .stat-chip{ background:var(--navy-800); border:1px solid var(--line-soft); border-radius:12px; padding:12px 16px; min-width:130px; }
  .stat-chip .n{ font-family:'Space Grotesk'; font-size:22px; font-weight:700; }
  .stat-chip .l{ font-size:11px; color:var(--text-dim); margin-top:2px; }

  .grid-2{ display:grid; grid-template-columns:1.3fr 1fr; gap:22px; }
  @media(max-width:900px){ .grid-2{ grid-template-columns:1fr; } }

  .panel{ border:1px solid var(--line-soft); border-radius:18px; background:var(--navy-900); padding:24px; }
  .panel h3{ margin:0 0 6px; font-size:17px; }
  .panel .desc{ color:var(--text-mid); font-size:13.5px; margin-bottom:16px; line-height:1.6;}

  .claim-list{ display:flex; flex-direction:column; gap:10px; max-height:340px; overflow-y:auto; padding-right:4px;}
  .claim-row{ display:flex; align-items:flex-start; gap:12px; padding:12px 14px; border:1px solid var(--line-soft); border-radius:12px; background:var(--navy-800); }
  .claim-row .txt{ font-size:13px; color:var(--text-hi); line-height:1.5; flex:1; }
  .claim-row .cat{ font-size:10.5px; color:var(--text-dim); text-transform:uppercase; letter-spacing:0.06em; margin-bottom:3px; display:block;}

  .stamp{
    font-family:'Space Grotesk'; font-size:9.5px; font-weight:700; letter-spacing:0.08em;
    padding:4px 9px; border-radius:5px; text-transform:uppercase; white-space:nowrap;
    transform:rotate(-3deg); border:1.5px solid currentColor; flex-shrink:0; margin-top:1px;
  }
  .stamp.pending{ color:var(--text-dim); }
  .stamp.verified{ color:var(--cyan); background:var(--cyan-soft); }
  .stamp.watch{ color:var(--amber); background:var(--amber-soft); }
  .stamp.flagged{ color:var(--red); background:var(--red-soft); }

  .upload-zone{
    border:1.5px dashed var(--line); border-radius:14px; padding:22px; text-align:center;
    color:var(--text-mid); font-size:13px; transition:border-color .15s, background .15s; cursor:pointer;
  }
  .upload-zone.drag{ border-color:var(--orange); background:var(--orange-soft); color:var(--text-hi); }
  .upload-zone input{ display:none; }
  textarea.paste-box{
    width:100%; margin-top:12px; min-height:90px; background:var(--navy-950); border:1px solid var(--line);
    border-radius:10px; color:var(--text-hi); padding:10px 12px; font-size:12.5px; font-family:'IBM Plex Mono'; resize:vertical;
  }

  .history-item{ display:flex; justify-content:space-between; align-items:center; padding:12px 14px; border:1px solid var(--line-soft); border-radius:12px; background:var(--navy-800); margin-bottom:8px; font-size:13px;}
  .history-item .hd{ color:var(--text-dim); font-size:11.5px; }
  .empty-state{ text-align:center; padding:30px 10px; color:var(--text-dim); font-size:13px; }

  /* ===== INTERVIEW ===== */
  .interview-wrap{ display:grid; grid-template-columns:280px 1fr; gap:20px; }
  @media(max-width:920px){ .interview-wrap{ grid-template-columns:1fr; } .ledger{ order:2; } }

  .ledger{ border:1px solid var(--line-soft); border-radius:18px; background:var(--navy-900); padding:18px; height:fit-content; position:sticky; top:20px; }
  .ledger h4{ font-size:11px; text-transform:uppercase; letter-spacing:0.08em; color:var(--text-dim); margin:0 0 12px; }
  .ledger-row{ display:flex; align-items:center; gap:9px; padding:9px 8px; border-radius:9px; font-size:12px; margin-bottom:3px; transition:background .2s; }
  .ledger-row.active{ background:var(--orange-soft); }
  .ledger-row .idot{ width:9px;height:9px; border-radius:50%; flex-shrink:0; }
  .ledger-row .idot.pending{ background:var(--text-dim); }
  .ledger-row .idot.verified{ background:var(--cyan); box-shadow:0 0 6px var(--cyan); }
  .ledger-row .idot.watch{ background:var(--amber); box-shadow:0 0 6px var(--amber); }
  .ledger-row .idot.flagged{ background:var(--red); box-shadow:0 0 6px var(--red); }
  .ledger-row .lbl{ color:var(--text-mid); line-height:1.35; }
  .ledger-row.active .lbl{ color:var(--text-hi); }

  .gauge-wrap{ display:flex; align-items:center; gap:12px; margin-top:16px; padding-top:16px; border-top:1px solid var(--line-soft); }
  .gauge{ width:56px;height:56px; }
  .gauge-num{ font-family:'Space Grotesk'; font-size:20px; font-weight:700; }
  .gauge-lbl{ font-size:10.5px; color:var(--text-dim); }

  .chat-panel{ border:1px solid var(--line-soft); border-radius:18px; background:var(--navy-900); display:flex; flex-direction:column; min-height:560px; }
  .chat-head{ display:flex; align-items:center; justify-content:space-between; padding:16px 20px; border-bottom:1px solid var(--line-soft); }
  .chat-head .turn{ font-size:12px; color:var(--text-dim); }
  .progress-track{ width:120px; height:6px; border-radius:6px; background:var(--navy-700); overflow:hidden; }
  .progress-fill{ height:100%; background:linear-gradient(90deg, var(--orange), var(--amber)); width:0%; transition:width .5s ease; }

  .chat-body{ flex:1; padding:20px 22px; overflow-y:auto; display:flex; flex-direction:column; gap:16px; max-height:520px; }
  .msg{ max-width:82%; padding:13px 16px; border-radius:14px; font-size:14px; line-height:1.6; }
  .msg.interviewer{ align-self:flex-start; background:var(--navy-800); border:1px solid var(--line-soft); border-bottom-left-radius:4px; }
  .msg.candidate{ align-self:flex-end; background:linear-gradient(135deg, rgba(255,106,61,0.18), rgba(255,106,61,0.08)); border:1px solid rgba(255,106,61,0.3); border-bottom-right-radius:4px; }
  .msg .feedback{ margin-top:9px; padding-top:9px; border-top:1px solid var(--line-soft); font-size:12px; color:var(--text-mid); display:flex; gap:8px; align-items:flex-start;}
  .flagchip{ font-size:9.5px; font-weight:700; text-transform:uppercase; padding:3px 7px; border-radius:5px; flex-shrink:0; letter-spacing:0.04em;}
  .flagchip.strong{ background:var(--cyan-soft); color:var(--cyan); }
  .flagchip.vague{ background:var(--amber-soft); color:var(--amber); }
  .flagchip.missing-evidence{ background:var(--red-soft); color:var(--red); }
  .flagchip.exaggeration-risk{ background:var(--red-soft); color:var(--red); }
  .flagchip.good-recovery{ background:var(--cyan-soft); color:var(--cyan); }
  .flagchip.none{ display:none; }

  .typing{ display:flex; gap:4px; padding:6px 4px; }
  .typing span{ width:6px;height:6px; border-radius:50%; background:var(--text-dim); animation:blink 1.2s infinite; }
  .typing span:nth-child(2){ animation-delay:.2s; } .typing span:nth-child(3){ animation-delay:.4s; }
  @keyframes blink{ 0%,80%,100%{opacity:.3;} 40%{opacity:1;} }

  .chat-input{ display:flex; gap:10px; padding:16px 20px; border-top:1px solid var(--line-soft); }
  .chat-input textarea{
    flex:1; background:var(--navy-950); border:1px solid var(--line); border-radius:12px; color:var(--text-hi);
    padding:12px 14px; font-size:14px; resize:none; min-height:48px; max-height:140px; font-family:inherit;
  }
  .chat-input textarea:focus{ border-color:var(--orange); outline:none; }
  .send-btn{ background:var(--orange); color:#180800; border-radius:12px; padding:0 20px; font-weight:700; font-size:13px; flex-shrink:0; }
  .send-btn:disabled{ opacity:0.35; }

  .banner{ margin:0 20px 14px; padding:10px 14px; border-radius:10px; font-size:12.5px; display:flex; align-items:center; justify-content:space-between; gap:10px;}
  .banner.err{ background:var(--red-soft); color:var(--red); border:1px solid rgba(255,77,94,0.35); }
  .banner button{ text-decoration:underline; font-size:12px; color:inherit; flex-shrink:0; }

  /* ===== REPORT ===== */
  .report-hero{ display:flex; align-items:center; gap:30px; flex-wrap:wrap; border:1px solid var(--line-soft); border-radius:20px; padding:32px; background:linear-gradient(160deg, var(--navy-900), var(--navy-950)); margin-bottom:22px;}
  .big-gauge{ width:140px; height:140px; flex-shrink:0; }
  .report-hero h2{ margin:0 0 6px; font-size:24px; }
  .report-hero p{ color:var(--text-mid); font-size:14px; max-width:520px; line-height:1.6; margin:0;}

  .report-grid{ display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-bottom:22px;}
  @media(max-width:800px){ .report-grid{ grid-template-columns:1fr; } }
  .rcard{ border:1px solid var(--line-soft); border-radius:16px; padding:18px; background:var(--navy-900); }
  .rcard .n{ font-family:'Space Grotesk'; font-size:28px; font-weight:700; }
  .rcard .l{ font-size:12px; color:var(--text-dim); margin-top:4px; }
  .rcard.orange .n{ color:var(--orange); } .rcard.cyan .n{ color:var(--cyan); } .rcard.amber .n{ color:var(--amber); }

  .claim-report{ border:1px solid var(--line-soft); border-radius:14px; padding:16px 18px; background:var(--navy-800); margin-bottom:12px; }
  .cr-head{ display:flex; justify-content:space-between; align-items:flex-start; gap:12px; margin-bottom:8px;}
  .cr-head .txt{ font-size:13.5px; font-weight:500; line-height:1.5; }
  .cr-bar-track{ height:6px; border-radius:6px; background:var(--navy-700); overflow:hidden; margin:8px 0 10px;}
  .cr-bar-fill{ height:100%; border-radius:6px; }
  .cr-note{ font-size:12.5px; color:var(--text-mid); line-height:1.55; }

  .report-actions{ display:flex; gap:12px; flex-wrap:wrap; margin-top:8px; }

  footer.note{ text-align:center; color:var(--text-dim); font-size:11.5px; margin-top:30px; line-height:1.6; }

  @media (prefers-reduced-motion: reduce){
    *{ animation:none !important; transition:none !important; }
  }
</style>
</head>
<body>
<div class="app">

  <div class="topbar">
    <div class="brand">
      <div class="brand-mark">DX</div>
      <div class="brand-text">
        <div class="t1">Defend Your Experience</div>
        <div class="t2">Case file — Optum Healthcare Chat Process, Interview Prep</div>
      </div>
    </div>
    <div class="stamp-badge"><span class="dot"></span><span id="topbarStatus">Case open · 12 claims on record</span></div>
  </div>

  <!-- ============ HOME SCREEN ============ -->
  <section id="screen-home" class="screen active">
    <div class="hero">
      <span class="eyebrow">● Not a resume review</span>
      <h1>This isn't about making your resume prettier.<br>It's about making sure you can defend every word in it.</h1>
      <p class="sub">Every bullet on your resume is a claim. In a real Optum interview, someone will poke at each one — the 3 years, the "audit activities," the AI upskilling. This session runs an adaptive, skeptical interview built from your own document, tracks how well each claim holds up, and hands you a Defense Report before you walk in the room.</p>
      <div class="hero-cta">
        <button class="btn btn-primary" id="btnStart">Start Defense Session →</button>
        <button class="btn btn-ghost" id="btnUploadToggle">Use a different document</button>
      </div>
      <div class="stat-strip">
        <div class="stat-chip"><div class="n" id="statClaims">12</div><div class="l">Claims on file</div></div>
        <div class="stat-chip"><div class="n" id="statMetrics">0</div><div class="l">Quantified metrics found</div></div>
        <div class="stat-chip"><div class="n" id="statSessions">0</div><div class="l">Past sessions</div></div>
      </div>
    </div>

    <div class="grid-2">
      <div class="panel">
        <h3>Case file: claims extracted</h3>
        <p class="desc">Pulled directly from the uploaded resume. Each one becomes fair game in the interview.</p>
        <div class="claim-list" id="claimListHome"></div>
      </div>
      <div class="panel">
        <h3>Session history</h3>
        <p class="desc">Your past defense sessions, saved to this case file.</p>
        <div id="historyList"></div>
        <div id="uploadArea" style="display:none; margin-top:18px; border-top:1px solid var(--line-soft); padding-top:16px;">
          <h3 style="font-size:14px;">Replace the document</h3>
          <p class="desc">Drop a resume/LinkedIn text file, or paste the text below. Claims will be re-extracted.</p>
          <div class="upload-zone" id="dropZone">
            Drag & drop a .txt file here, or click to choose one
            <input type="file" id="fileInput" accept=".txt,.md">
          </div>
          <textarea class="paste-box" id="pasteBox" placeholder="...or paste resume / LinkedIn text here"></textarea>
          <button class="btn btn-primary" style="margin-top:10px; width:100%; justify-content:center;" id="btnExtract">Extract claims from this text</button>
        </div>
      </div>
    </div>
  </section>

  <!-- ============ INTERVIEW SCREEN ============ -->
  <section id="screen-interview" class="screen">
    <div class="interview-wrap">
      <aside class="ledger">
        <h4>Audit Ledger</h4>
        <div id="ledgerList"></div>
        <div class="gauge-wrap">
          <svg class="gauge" viewBox="0 0 56 56">
            <circle cx="28" cy="28" r="24" fill="none" stroke="var(--navy-700)" stroke-width="6"/>
            <circle id="gaugeRing" cx="28" cy="28" r="24" fill="none" stroke="var(--orange)" stroke-width="6" stroke-linecap="round" stroke-dasharray="150.8" stroke-dashoffset="150.8" transform="rotate(-90 28 28)"/>
          </svg>
          <div>
            <div class="gauge-num" id="gaugeNum">0%</div>
            <div class="gauge-lbl">Overall readiness</div>
          </div>
        </div>
      </aside>

      <div class="chat-panel">
        <div class="chat-head">
          <div class="turn" id="turnLabel">Question 0 of ~12</div>
          <div class="progress-track"><div class="progress-fill" id="turnProgress"></div></div>
        </div>
        <div id="errBanner"></div>
        <div class="chat-body" id="chatBody"></div>
        <div class="chat-input">
          <textarea id="answerInput" placeholder="Type your answer as you would say it out loud..." rows="1"></textarea>
          <button class="btn send-btn" id="sendBtn">Answer</button>
        </div>
      </div>
    </div>
    <div style="text-align:center; margin-top:16px;">
      <button class="btn btn-ghost" id="btnEndEarly">End session & generate report now</button>
    </div>
  </section>

  <!-- ============ REPORT SCREEN ============ -->
  <section id="screen-report" class="screen">
    <div class="report-hero">
      <svg class="big-gauge" viewBox="0 0 140 140">
        <circle cx="70" cy="70" r="58" fill="none" stroke="var(--navy-700)" stroke-width="14"/>
        <circle id="bigGaugeRing" cx="70" cy="70" r="58" fill="none" stroke="var(--orange)" stroke-width="14" stroke-linecap="round" stroke-dasharray="364.4" stroke-dashoffset="364.4" transform="rotate(-90 70 70)"/>
        <text id="bigGaugeText" x="70" y="78" text-anchor="middle" font-family="Space Grotesk" font-size="30" font-weight="700" fill="#EEF1F9">0%</text>
      </svg>
      <div>
        <h2 id="reportTitle">Defense Report</h2>
        <p id="reportSub">Here's how your case file held up under questioning, and exactly where to reinforce it before the real thing.</p>
      </div>
    </div>

    <div class="report-grid">
      <div class="rcard cyan"><div class="n" id="rWellDefended">0</div><div class="l">Well-defended claims</div></div>
      <div class="rcard amber"><div class="n" id="rNeedsWork">0</div><div class="l">Need more work</div></div>
      <div class="rcard orange"><div class="n" id="rFlagged">0</div><div class="l">Flagged / weak</div></div>
    </div>

    <div class="panel" style="margin-bottom:20px;">
      <h3>Claim-by-claim breakdown</h3>
      <p class="desc">Ordered weakest first — start reinforcing here.</p>
      <div id="claimReportList"></div>
    </div>

    <div class="panel">
      <h3>Before the real interview</h3>
      <p class="desc" id="strategyNotes">—</p>
      <div class="report-actions">
        <button class="btn btn-primary" id="btnExport">Export Defense Report</button>
        <button class="btn btn-ghost" id="btnRetry">Run another session</button>
      </div>
    </div>
  </section>

  <footer class="note">
    Session data is saved to this case file's private storage so it's here next time you open this app.<br>
    If a question fails to load (rate limit or network hiccup), use Retry — nothing you've said is lost.
  </footer>
</div>

<script>
(function(){
  const MODEL = "claude-sonnet-4-6";

  const DEFAULT_RESUME_TEXT = `SHALINI KHARBANDA — US Healthcare Operations Professional | Business Analyst
Business Analyst – US Healthcare (Aetna Process), EXL Service Pvt. Ltd., August 2023 – Present.
Manage healthcare policy updates and comprehensive member benefit administration for the Aetna process.
Process policy renewals, benefit modifications, and plan terminations based on premium eligibility and strict business guidelines.
Accurately update Medical, Dental, and Vision benefits according to dynamic member eligibility criteria.
Provide, modify, and manage system access for employees joining, transferring, or changing operational processes.
Perform precise audit activities to verify user access records, data accuracy, and absolute process compliance.
Review complex operational records to identify discrepancies, ensuring accuracy while meeting stringent quality and productivity standards.
Expert Fevicryl Certified Professional Trainer, Pidilite Industries Ltd. Conducted art and craft training sessions and professional workshops across diverse institutional setups.
Over 6 years of classroom teaching experience (Reputed Schools, Prayagraj & Buxar), building organizational communication, training, mentoring, and interpersonal skills.
Actively upskilling through the ABTalksOnAI 60-Day LinkedIn Challenge to integrate AI tools and prompt engineering into daily workflows.
Skills: US Healthcare Operations & Policy Administration, Member Benefits & Access Management, Audit/Compliance & Data Validation, Basic MS Excel (Pivot Tables), Basic MS Word.`;

  const DEFAULT_CLAIMS = [
    {id:"c1", cat:"Tenure", text:"Nearly 3 years of experience at EXL supporting the Aetna process (Aug 2023–Present)."},
    {id:"c2", cat:"Core duty", text:"Manages healthcare policy updates and comprehensive member benefit administration for the Aetna process."},
    {id:"c3", cat:"Core duty", text:"Processes policy renewals, benefit modifications, and plan terminations based on premium eligibility and business guidelines."},
    {id:"c4", cat:"Core duty", text:"Accurately updates Medical, Dental, and Vision benefits per dynamic member eligibility criteria."},
    {id:"c5", cat:"Access mgmt", text:"Provides, modifies, and manages system access for employees joining, transferring, or changing processes."},
    {id:"c6", cat:"Audit", text:"Performs precise audit activities to verify user access records, data accuracy, and process compliance."},
    {id:"c7", cat:"Quality", text:"Reviews complex operational records to identify discrepancies while meeting stringent quality and productivity standards."},
    {id:"c8", cat:"No metrics on file", text:"Resume contains zero quantified evidence anywhere — no accuracy %, volume/day, CSAT, or resolution time backing any bullet."},
    {id:"c9", cat:"Career pivot", text:"Expert Fevicryl Certified Professional Trainer (Pidilite) — art & craft workshops, prior to healthcare BPO."},
    {id:"c10", cat:"Career pivot", text:"Over 6 years classroom teaching experience, framed as building communication/training/mentoring skills."},
    {id:"c11", cat:"Upskilling", text:"Actively upskilling via the ABTalksOnAI 60-Day LinkedIn Challenge in AI tools and prompt engineering."},
    {id:"c12", cat:"Scenario readiness", text:"Implicit claim: capable of handling live member/patient chat interactions professionally under Optum-style pressure."}
  ];

  // ---------- state ----------
  let claims = [];         // working set with confidence/status/notes
  let resumeText = DEFAULT_RESUME_TEXT;
  let conversation = [];   // {role, content} sent to API
  let turnCount = 0;
  const MAX_TURNS = 12;
  let sessionActive = false;
  let lastTargetClaim = null;
  let sessionLog = [];     // {question, answer, feedback, confidenceScore, flag, claimId}

  function freshClaimState(list){
    return list.map(c => ({...c, confidence:0, assessed:false, status:"pending", notes:[]}));
  }

  function statusFromConfidence(score){
    if(score >= 72) return "verified";
    if(score >= 45) return "watch";
    return "flagged";
  }

  // ---------- storage ----------
  async function loadCaseFile(){
    try{
      const r = await window.storage.get('case-file', false);
      if(r && r.value){
        const data = JSON.parse(r.value);
        resumeText = data.resumeText || DEFAULT_RESUME_TEXT;
        claims = data.claims && data.claims.length ? data.claims : freshClaimState(DEFAULT_CLAIMS);
        return;
      }
    }catch(e){ /* no case file yet */ }
    resumeText = DEFAULT_RESUME_TEXT;
    claims = freshClaimState(DEFAULT_CLAIMS);
    await saveCaseFile();
  }

  async function saveCaseFile(){
    try{
      await window.storage.set('case-file', JSON.stringify({resumeText, claims}), false);
    }catch(e){ console.error("save case-file failed", e); }
  }

  async function saveSession(report){
    try{
      const key = 'session:' + Date.now();
      await window.storage.set(key, JSON.stringify(report), false);
    }catch(e){ console.error("save session failed", e); }
  }

  async function listSessions(){
    try{
      const r = await window.storage.list('session:', false);
      return (r && r.keys) ? r.keys.sort().reverse() : [];
    }catch(e){ return []; }
  }

  // ---------- rendering: home ----------
  function renderHome(){
    document.getElementById('statClaims').textContent = claims.length;
    document.getElementById('statMetrics').textContent = 0; // known: this resume has none
    const list = document.getElementById('claimListHome');
    list.innerHTML = claims.map(c => `
      <div class="claim-row">
        <div class="txt"><span class="cat">${c.cat}</span>${escapeHtml(c.text)}</div>
        <div class="stamp ${c.status}">${stampLabel(c.status)}</div>
      </div>`).join('');
    renderHistory();
  }

  function stampLabel(s){
    return {pending:"Pending", verified:"Verified", watch:"Needs work", flagged:"Flagged"}[s] || "Pending";
  }

  async function renderHistory(){
    const keys = await listSessions();
    document.getElementById('statSessions').textContent = keys.length;
    const el = document.getElementById('historyList');
    if(!keys.length){
      el.innerHTML = `<div class="empty-state">No sessions yet. Run your first defense session — it'll show up here so you can track progress over time.</div>`;
      return;
    }
    let html = '';
    for(const k of keys.slice(0,6)){
      try{
        const r = await window.storage.get(k, false);
        const d = JSON.parse(r.value);
        const dt = new Date(parseInt(k.split(':')[1])).toLocaleString();
        html += `<div class="history-item"><div><div>Readiness: ${d.overallScore}%</div><div class="hd">${dt}</div></div><div class="hd">${d.wellDefended}✓ / ${d.needsWork}~ / ${d.flagged}✕</div></div>`;
      }catch(e){}
    }
    el.innerHTML = html;
  }

  function escapeHtml(s){
    return s.replace(/[&<>"']/g, m => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
  }

  // ---------- screen switching ----------
  function showScreen(id){
    document.querySelectorAll('.screen').forEach(s=>s.classList.remove('active'));
    document.getElementById(id).classList.add('active');
  }

  // ---------- claim extraction (for replaced documents) ----------
  async function extractClaimsFromText(text){
    const sys = `Extract every meaningful, checkable claim a job candidate makes in the document below (skills, responsibilities, durations, achievements, tools, soft-skill statements). Merge trivial duplicates. Flag if there are no quantified metrics anywhere.
Respond ONLY with a strict JSON array, no prose, no markdown fences. Each item: {"id":"c1","cat":"short 1-3 word category","text":"the claim, rewritten as one clear sentence, max 22 words"}. Produce between 8 and 14 items.`;
    const resp = await fetch("https://api.anthropic.com/v1/messages", {
      method:"POST", headers:{"Content-Type":"application/json"},
      body: JSON.stringify({
        model: MODEL, max_tokens: 1000,
        system: sys,
        messages: [{role:"user", content: text}]
      })
    });
    const data = await resp.json();
    const raw = (data.content||[]).map(b=>b.text||'').join('').trim().replace(/^```json|```$/g,'').trim();
    const parsed = JSON.parse(raw);
    return freshClaimState(parsed);
  }

  // ---------- interview API ----------
  function buildSystemPrompt(){
    const claimsJson = JSON.stringify(claims.map(c=>({id:c.id, cat:c.cat, text:c.text, status:c.status})));
    return `You are a sharp, professional, mildly skeptical interview panelist helping a candidate prepare to defend their resume claims before a real interview for a healthcare chat-process role at Optum (member/patient support, insurance-adjacent, US healthcare).

CLAIMS ON FILE (JSON): ${claimsJson}

Interview rules:
- Ask exactly ONE question per turn. Never stack multiple questions.
- Every question must be built from a SPECIFIC detail in the claims above — never generic ("tell me about yourself" is banned).
- Prioritize claims still "pending". Revisit "watch"/"flagged" claims with a sharper follow-up before moving on.
- This resume has ZERO quantified metrics anywhere (no accuracy %, daily volume, CSAT, resolution time). Directly press for real numbers at least once early on.
- Ask at least one question about the career pivot from teaching / craft training into healthcare BPO — interviewers notice this and will ask.
- Include at least two realistic chat-process SCENARIO simulations relevant to Optum (e.g. an upset member disputing a benefit denial in chat, a system-access request that looks slightly irregular) and ask how the candidate would respond, in chat, concisely.
- If an answer is vague or unquantified, flag it and ask a sharper, more specific follow-up on the SAME claim.
- If an answer is strong and specific, acknowledge briefly and move to a new claim.
- Keep questions concise (max ~40 words), professional, and a little pointed — like a real interviewer who has read the resume closely.
- After roughly 10-12 solid exchanges covering the major claims and both scenarios, set interviewComplete to true.

Respond with STRICT JSON ONLY. No markdown fences, no prose outside the JSON object. Schema:
{"feedback": "1-2 sentence evaluation of the candidate's PREVIOUS answer (empty string on the very first turn)", "confidenceScore": integer 0-100 (quality of the previous answer as a defense; 0 on first turn), "flag": "none|vague|strong|exaggeration-risk|missing-evidence|good-recovery", "targetClaimId": "the claim id this NEW question targets, or 'scenario' for a simulation question", "question": "the single next question", "interviewComplete": boolean}`;
  }

  async function callInterviewAPI(){
    const resp = await fetch("https://api.anthropic.com/v1/messages", {
      method:"POST", headers:{"Content-Type":"application/json"},
      body: JSON.stringify({
        model: MODEL, max_tokens: 1000,
        system: buildSystemPrompt(),
        messages: conversation.length ? conversation : [{role:"user", content:"Begin the interview with your first question."}]
      })
    });
    if(!resp.ok){
      throw new Error("HTTP " + resp.status);
    }
    const data = await resp.json();
    const raw = (data.content||[]).map(b=>b.text||'').join('').trim().replace(/^```json|```$/g,'').trim();
    return JSON.parse(raw);
  }

  function showBanner(msg, retryFn){
    const el = document.getElementById('errBanner');
    el.innerHTML = `<div class="banner err"><span>${escapeHtml(msg)}</span><button id="retryBtn">Retry</button></div>`;
    document.getElementById('retryBtn').onclick = () => { el.innerHTML=''; retryFn(); };
  }
  function clearBanner(){ document.getElementById('errBanner').innerHTML=''; }

  function appendMsg(role, text, feedbackData){
    const body = document.getElementById('chatBody');
    const div = document.createElement('div');
    div.className = 'msg ' + (role === 'interviewer' ? 'interviewer' : 'candidate');
    let inner = `<div>${escapeHtml(text)}</div>`;
    if(feedbackData && feedbackData.feedback){
      inner += `<div class="feedback"><span class="flagchip ${feedbackData.flag}">${feedbackData.flag.replace('-',' ')}</span><span>${escapeHtml(feedbackData.feedback)}</span></div>`;
    }
    div.innerHTML = inner;
    body.appendChild(div);
    body.scrollTop = body.scrollHeight;
  }

  function showTyping(){
    const body = document.getElementById('chatBody');
    const div = document.createElement('div');
    div.className = 'msg interviewer'; div.id = 'typingIndicator';
    div.innerHTML = `<div class="typing"><span></span><span></span><span></span></div>`;
    body.appendChild(div); body.scrollTop = body.scrollHeight;
  }
  function hideTyping(){ const t = document.getElementById('typingIndicator'); if(t) t.remove(); }

  function renderLedger(){
    const el = document.getElementById('ledgerList');
    el.innerHTML = claims.map(c => `
      <div class="ledger-row ${c.id===lastTargetClaim ? 'active':''}">
        <div class="idot ${c.status}"></div>
        <div class="lbl">${escapeHtml(c.cat)}</div>
      </div>`).join('');
    const assessed = claims.filter(c=>c.assessed);
    const overall = assessed.length ? Math.round(assessed.reduce((s,c)=>s+c.confidence,0)/assessed.length) : 0;
    document.getElementById('gaugeNum').textContent = overall + '%';
    const circumference = 150.8;
    document.getElementById('gaugeRing').setAttribute('stroke-dashoffset', circumference - (circumference*overall/100));
  }

  function updateTurnUI(){
    document.getElementById('turnLabel').textContent = `Question ${turnCount} of ~${MAX_TURNS}`;
    document.getElementById('turnProgress').style.width = Math.min(100, (turnCount/MAX_TURNS)*100) + '%';
  }

  async function runInterviewTurn(){
    clearBanner();
    showTyping();
    document.getElementById('sendBtn').disabled = true;
    try{
      const result = await callInterviewAPI();
      hideTyping();

      // apply feedback about the PREVIOUS answer to lastTargetClaim
      if(lastTargetClaim && lastTargetClaim !== 'scenario'){
        const claim = claims.find(c=>c.id===lastTargetClaim);
        if(claim){
          claim.assessed = true;
          claim.confidence = claim.notes.length ? Math.round((claim.confidence + result.confidenceScore)/2) : result.confidenceScore;
          claim.status = statusFromConfidence(claim.confidence);
          if(result.feedback) claim.notes.push({flag: result.flag, note: result.feedback});
          sessionLog.push({claimId: lastTargetClaim, feedback: result.feedback, confidenceScore: result.confidenceScore, flag: result.flag});
        }
      }

      if(turnCount > 0){
        // attach feedback bubble to the previous candidate message region by appending as separate line
        appendMsg('interviewer', result.question, {feedback: result.feedback, flag: result.flag});
      } else {
        appendMsg('interviewer', result.question, null);
      }

      lastTargetClaim = result.targetClaimId;
      turnCount++;
      conversation.push({role:'assistant', content: JSON.stringify(result)});
      updateTurnUI();
      renderLedger();
      await saveCaseFile();

      if(result.interviewComplete || turnCount >= MAX_TURNS){
        setTimeout(()=> finishSession(), 900);
      }
    }catch(e){
      hideTyping();
      showBanner("Couldn't reach the interviewer — likely a temporary rate limit or network hiccup.", runInterviewTurn);
    }
    document.getElementById('sendBtn').disabled = false;
  }

  async function submitAnswer(){
    const input = document.getElementById('answerInput');
    const text = input.value.trim();
    if(!text) return;
    appendMsg('candidate', text, null);
    conversation.push({role:'user', content:text});
    input.value = '';
    input.style.height = 'auto';
    await runInterviewTurn();
  }

  // ---------- report ----------
  function finishSession(){
    const sorted = [...claims].sort((a,b)=> a.confidence - b.confidence);
    const wellDefended = claims.filter(c=>c.status==='verified').length;
    const needsWork = claims.filter(c=>c.status==='watch').length;
    const flagged = claims.filter(c=>c.status==='flagged' || c.status==='pending').length;
    const assessed = claims.filter(c=>c.assessed);
    const overall = assessed.length ? Math.round(assessed.reduce((s,c)=>s+c.confidence,0)/assessed.length) : 0;

    document.getElementById('bigGaugeText').textContent = overall + '%';
    const circ = 364.4;
    document.getElementById('bigGaugeRing').setAttribute('stroke-dashoffset', circ - (circ*overall/100));
    document.getElementById('rWellDefended').textContent = wellDefended;
    document.getElementById('rNeedsWork').textContent = needsWork;
    document.getElementById('rFlagged').textContent = flagged;

    document.getElementById('reportSub').textContent = overall >= 70
      ? "Strong showing — most claims held up under pressure. Tighten the remaining gaps below and you're interview-ready."
      : overall >= 45
      ? "A mixed defense. Several claims are solid, but a few will crack under a sharper interviewer. Focus your prep on the list below."
      : "Several claims are still unproven or vague. That's normal on a first pass — use the breakdown below to rebuild each one with a specific example and a number.";

    const listEl = document.getElementById('claimReportList');
    listEl.innerHTML = sorted.map(c => {
      const color = c.status==='verified' ? 'var(--cyan)' : c.status==='watch' ? 'var(--amber)' : 'var(--red)';
      const pct = c.assessed ? c.confidence : 0;
      const noteText = c.assessed
        ? (c.notes[c.notes.length-1]?.note || "Assessed during the session.")
        : "Not explored this session — bring your own concrete example for this before the interview.";
      return `<div class="claim-report">
        <div class="cr-head">
          <div class="txt">${escapeHtml(c.text)}</div>
          <div class="stamp ${c.status}">${stampLabel(c.status)}</div>
        </div>
        <div class="cr-bar-track"><div class="cr-bar-fill" style="width:${pct}%; background:${color};"></div></div>
        <div class="cr-note">${escapeHtml(noteText)}</div>
      </div>`;
    }).join('');

    document.getElementById('strategyNotes').textContent =
      "Your biggest structural gap is the total absence of numbers on this resume. Before the interview, write down three real figures: roughly how many member records or access requests you handle per day, your audit accuracy rate, and how quickly you typically resolve a discrepancy. Also prepare a 20-second answer for 'why did you move from teaching into healthcare operations' — interviewers will ask, and a confident, honest answer reads as self-awareness, not a weakness.";

    const report = {
      overallScore: overall, wellDefended, needsWork, flagged,
      claims: claims.map(c=>({id:c.id, text:c.text, status:c.status, confidence:c.confidence})),
      log: sessionLog, timestamp: Date.now()
    };
    saveSession(report);
    sessionActive = false;
    showScreen('screen-report');
  }

  function exportReport(){
    const lines = [];
    lines.push("DEFEND YOUR EXPERIENCE — DEFENSE REPORT");
    lines.push("Candidate: Shalini Kharbanda — Target: Optum Healthcare Chat Process");
    lines.push("Generated: " + new Date().toLocaleString());
    lines.push("");
    lines.push("Overall readiness: " + document.getElementById('bigGaugeText').textContent);
    lines.push("Well-defended: " + document.getElementById('rWellDefended').textContent +
      " | Needs work: " + document.getElementById('rNeedsWork').textContent +
      " | Flagged: " + document.getElementById('rFlagged').textContent);
    lines.push("");
    claims.forEach(c=>{
      lines.push("[" + stampLabel(c.status).toUpperCase() + "] (" + c.confidence + "%) " + c.text);
      const lastNote = c.notes[c.notes.length-1];
      if(lastNote) lines.push("   note: " + lastNote.note);
    });
    lines.push("");
    lines.push("Strategy notes:");
    lines.push(document.getElementById('strategyNotes').textContent);

    const blob = new Blob([lines.join("\n")], {type:"text/plain"});
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = "defense-report.txt";
    document.body.appendChild(a); a.click(); a.remove();
  }

  // ---------- session lifecycle ----------
  async function startSession(){
    claims = freshClaimState(claims.map(({id,cat,text})=>({id,cat,text}))); // reset confidence for a fresh run
    conversation = []; turnCount = 0; sessionLog = []; lastTargetClaim = null; sessionActive = true;
    document.getElementById('chatBody').innerHTML = '';
    updateTurnUI();
    renderLedger();
    showScreen('screen-interview');
    await runInterviewTurn();
  }

  // ---------- events ----------
  document.getElementById('btnStart').addEventListener('click', startSession);
  document.getElementById('btnRetry').addEventListener('click', startSession);
  document.getElementById('btnExport').addEventListener('click', exportReport);
  document.getElementById('btnEndEarly').addEventListener('click', ()=>{ if(sessionActive) finishSession(); });

  document.getElementById('sendBtn').addEventListener('click', submitAnswer);
  const answerInput = document.getElementById('answerInput');
  answerInput.addEventListener('keydown', (e)=>{
    if(e.key === 'Enter' && !e.shiftKey){ e.preventDefault(); submitAnswer(); }
  });
  answerInput.addEventListener('input', ()=>{
    answerInput.style.height = 'auto';
    answerInput.style.height = Math.min(140, answerInput.scrollHeight) + 'px';
  });

  document.getElementById('btnUploadToggle').addEventListener('click', ()=>{
    const a = document.getElementById('uploadArea');
    a.style.display = a.style.display === 'none' ? 'block' : 'none';
  });

  const dropZone = document.getElementById('dropZone');
  const fileInput = document.getElementById('fileInput');
  dropZone.addEventListener('click', ()=> fileInput.click());
  dropZone.addEventListener('dragover', (e)=>{ e.preventDefault(); dropZone.classList.add('drag'); });
  dropZone.addEventListener('dragleave', ()=> dropZone.classList.remove('drag'));
  dropZone.addEventListener('drop', (e)=>{
    e.preventDefault(); dropZone.classList.remove('drag');
    const file = e.dataTransfer.files[0];
    if(file) file.text().then(t => document.getElementById('pasteBox').value = t);
  });
  fileInput.addEventListener('change', (e)=>{
    const file = e.target.files[0];
    if(file) file.text().then(t => document.getElementById('pasteBox').value = t);
  });

  document.getElementById('btnExtract').addEventListener('click', async ()=>{
    const text = document.getElementById('pasteBox').value.trim();
    if(!text){ alert("Paste or drop some text first."); return; }
    const btn = document.getElementById('btnExtract');
    btn.disabled = true; btn.textContent = "Extracting claims...";
    try{
      const newClaims = await extractClaimsFromText(text);
      claims = newClaims; resumeText = text;
      await saveCaseFile();
      renderHome();
      document.getElementById('uploadArea').style.display = 'none';
    }catch(e){
      alert("Couldn't extract claims — try again in a moment.");
    }
    btn.disabled = false; btn.textContent = "Extract claims from this text";
  });

  // ---------- init ----------
  (async function init(){
    await loadCaseFile();
    renderHome();
  })();
})();
</script>
</body>
</html>
<img width="1287" height="1262" alt="image" src="https://github.com/user-attachments/assets/399184c2-d7e1-4b28-ab96-1ac2047db0a6" />
<img width="1338" height="476" alt="image" src="https://github.com/user-attachments/assets/b8296b66-46de-47e5-95cc-391ac11a7631" />

