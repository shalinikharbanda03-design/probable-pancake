:Prompt: You are an expert frontend developer, UX designer, instructional designer, and media literacy analyst.

Ask the user to choose a color theme from a few options (including Claude Orange).

Create a beautiful single-file HTML application called 'Media Integrity Analyzer'.

Use pure vanilla CSS and JS. No Tailwind, npm, backend, APIs, images, or external assets. Everything must work offline in one HTML file.

The goal is to teach media literacy through interactive discovery, not test prior knowledge. The experience should feel like a guided lesson where users learn by observing, thinking, and then revealing the answer.

Make it interactive.

Before each challenge, briefly explain the concept in simple language, why it matters, and how it applies to everyday life.

Challenge 1: Headline Detective
- Generate a fictional news headline and matching article.
- Ask: Would you click this? (Yes / Maybe / No)
- Ask the user to identify exaggerated or misleading parts.
- Reveal the Headline Accuracy Score, highlighted mismatches, explanation, fair rewritten headline, and key takeaway.

Challenge 2: Emotion Detector
- Generate a fictional social media post, reel caption, or article excerpt.
- Ask how it made the user feel and which words influenced that feeling.
- Reveal the target audience, intended emotional response, manipulation technique, highlighted emotional phrases, neutral rewrite, and key takeaway.

Display live Media Integrity metrics:
- Headline Accuracy
- Source Reliability
- Emotional Manipulation
- Audience Targeting

Finish with a Media Integrity Dashboard containing:
- Overall Media Integrity Score
- What the user learned
- Biggest red flag
- Three practical media literacy habits
- Replay with completely new scenarios

Design a premium editorial-style dark interface with smooth animations, progress indicators, hover effects, modern cards, and responsive layout.

Ensure there are zero syntax errors.

Return ONLY the complete HTML inside one code block.

:Response: Here's your Media Integrity Analyzer with a yellow accent on a dark editorial theme — self-contained, offline-ready, with both challenges, live metrics, and a final dashboard with replay.
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Media Integrity Analyzer</title>
<style>
  :root{
    --bg:#0e0e10;
    --bg-alt:#161618;
    --card:#1b1b1e;
    --card-hover:#212124;
    --border:#2c2c30;
    --text:#f1efe9;
    --text-dim:#a8a6a1;
    --accent:#f5c518;
    --accent-dim:#c9a415;
    --accent-glow: rgba(245,197,24,0.25);
    --danger:#ef5350;
    --good:#4caf82;
    --warn:#f0a94c;
    --radius:16px;
    --serif: 'Georgia', 'Iowan Old Style', serif;
    --sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
  }

  *{box-sizing:border-box;}
  html,body{margin:0;padding:0;}
  body{
    background:
      radial-gradient(circle at 15% 0%, rgba(245,197,24,0.06), transparent 40%),
      radial-gradient(circle at 85% 100%, rgba(245,197,24,0.04), transparent 40%),
      var(--bg);
    color:var(--text);
    font-family:var(--sans);
    line-height:1.6;
    min-height:100vh;
    -webkit-font-smoothing:antialiased;
  }

  .wrap{
    max-width:880px;
    margin:0 auto;
    padding:40px 24px 120px;
  }

  header.top{
    text-align:center;
    margin-bottom:36px;
    animation: fadeDown .7s ease both;
  }
  header.top .kicker{
    text-transform:uppercase;
    letter-spacing:3px;
    font-size:12px;
    color:var(--accent);
    font-weight:700;
    margin-bottom:10px;
  }
  header.top h1{
    font-family:var(--serif);
    font-size:2.6rem;
    margin:0 0 10px;
    letter-spacing:-0.5px;
  }
  header.top p{
    color:var(--text-dim);
    max-width:560px;
    margin:0 auto;
    font-size:1.02rem;
  }

  /* progress bar */
  .progress-track{
    height:6px;
    background:var(--card);
    border-radius:999px;
    overflow:hidden;
    margin:28px 0 8px;
    border:1px solid var(--border);
  }
  .progress-fill{
    height:100%;
    background:linear-gradient(90deg, var(--accent-dim), var(--accent));
    width:0%;
    transition:width .6s cubic-bezier(.65,0,.35,1);
    box-shadow:0 0 12px var(--accent-glow);
  }
  .progress-label{
    display:flex;
    justify-content:space-between;
    font-size:12px;
    color:var(--text-dim);
    text-transform:uppercase;
    letter-spacing:1px;
    margin-bottom:24px;
  }

  /* metrics dashboard (persistent) */
  .metrics{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:12px;
    margin:28px 0 40px;
  }
  .metric-card{
    background:var(--card);
    border:1px solid var(--border);
    border-radius:12px;
    padding:14px 12px;
    text-align:center;
    transition:transform .25s ease, border-color .25s ease;
  }
  .metric-card:hover{
    transform:translateY(-3px);
    border-color:var(--accent-dim);
  }
  .metric-label{
    font-size:10.5px;
    text-transform:uppercase;
    letter-spacing:0.8px;
    color:var(--text-dim);
    margin-bottom:6px;
  }
  .metric-value{
    font-family:var(--serif);
    font-size:1.5rem;
    font-weight:700;
    color:var(--accent);
    transition: color .3s ease;
  }
  .metric-bar{
    height:4px;
    border-radius:999px;
    background:#2c2c30;
    margin-top:8px;
    overflow:hidden;
  }
  .metric-bar-fill{
    height:100%;
    background:var(--accent);
    width:0%;
    transition:width .8s ease;
  }

  /* cards / sections */
  .card{
    background:var(--card);
    border:1px solid var(--border);
    border-radius:var(--radius);
    padding:28px;
    margin-bottom:24px;
    animation: fadeUp .5s ease both;
    transition: box-shadow .3s ease, border-color .3s ease;
  }
  .card:hover{
    border-color:#3a3a3f;
  }

  .concept-card{
    background:linear-gradient(160deg, rgba(245,197,24,0.08), rgba(245,197,24,0.01));
    border:1px solid rgba(245,197,24,0.25);
  }
  .concept-card .tag{
    display:inline-block;
    background:var(--accent);
    color:#141414;
    font-weight:700;
    font-size:11px;
    letter-spacing:1px;
    text-transform:uppercase;
    padding:4px 10px;
    border-radius:999px;
    margin-bottom:14px;
  }
  .concept-card h2{
    font-family:var(--serif);
    margin:0 0 10px;
    font-size:1.5rem;
  }
  .concept-card p{color:var(--text-dim); margin:0 0 10px; font-size:0.98rem;}
  .concept-card .why{
    border-left:3px solid var(--accent);
    padding-left:14px;
    margin-top:14px;
    font-size:0.93rem;
    color:var(--text);
  }

  .headline-box{
    font-family:var(--serif);
    font-size:1.7rem;
    line-height:1.35;
    padding:22px;
    background:var(--bg-alt);
    border-radius:12px;
    border:1px solid var(--border);
    margin:18px 0;
  }
  .article-body{
    font-size:0.98rem;
    color:var(--text-dim);
    padding:0 4px;
  }
  .source-line{
    font-size:12px;
    text-transform:uppercase;
    letter-spacing:1px;
    color:var(--accent);
    margin-bottom:6px;
  }

  .social-post{
    background:var(--bg-alt);
    border:1px solid var(--border);
    border-radius:14px;
    padding:20px;
    margin:18px 0;
  }
  .social-post .handle{
    font-weight:700;
    margin-bottom:8px;
  }
  .social-post .handle span{
    color:var(--text-dim);
    font-weight:400;
    font-size:0.85rem;
  }
  .social-post .caption{
    font-size:1.05rem;
  }

  /* buttons */
  .btn-row{
    display:flex;
    gap:12px;
    flex-wrap:wrap;
    margin-top:20px;
  }
  button{
    font-family:var(--sans);
    cursor:pointer;
    border:none;
    outline:none;
  }
  .choice-btn{
    background:var(--bg-alt);
    color:var(--text);
    border:1px solid var(--border);
    padding:12px 22px;
    border-radius:10px;
    font-size:0.95rem;
    font-weight:600;
    transition: all .2s ease;
  }
  .choice-btn:hover{
    border-color:var(--accent);
    background:rgba(245,197,24,0.08);
    transform:translateY(-2px);
  }
  .choice-btn.selected{
    background:var(--accent);
    color:#141414;
    border-color:var(--accent);
  }
  .primary-btn{
    background:var(--accent);
    color:#141414;
    padding:14px 28px;
    border-radius:10px;
    font-weight:700;
    font-size:0.98rem;
    transition: all .2s ease;
    box-shadow:0 4px 20px var(--accent-glow);
  }
  .primary-btn:hover{
    transform:translateY(-2px);
    box-shadow:0 8px 28px var(--accent-glow);
  }
  .primary-btn:disabled{
    opacity:0.4;
    cursor:not-allowed;
    box-shadow:none;
    transform:none;
  }
  .ghost-btn{
    background:transparent;
    color:var(--text-dim);
    border:1px solid var(--border);
    padding:14px 28px;
    border-radius:10px;
    font-weight:600;
    transition:all .2s ease;
  }
  .ghost-btn:hover{
    color:var(--text);
    border-color:var(--text-dim);
  }

  textarea, input[type=text]{
    width:100%;
    background:var(--bg-alt);
    border:1px solid var(--border);
    color:var(--text);
    border-radius:10px;
    padding:14px;
    font-family:var(--sans);
    font-size:0.95rem;
    resize:vertical;
    min-height:70px;
    transition:border-color .2s ease;
  }
  textarea:focus, input[type=text]:focus{
    border-color:var(--accent);
  }

  .word-pick-area{
    display:flex;
    flex-wrap:wrap;
    gap:8px;
    margin:16px 0;
  }
  .word-chip{
    background:var(--bg-alt);
    border:1px solid var(--border);
    padding:8px 14px;
    border-radius:999px;
    font-size:0.9rem;
    transition:all .2s ease;
  }
  .word-chip:hover{
    border-color:var(--accent);
  }
  .word-chip.picked{
    background:var(--accent);
    color:#141414;
    border-color:var(--accent);
    font-weight:700;
  }

  /* reveal */
  .reveal{
    margin-top:22px;
    padding-top:22px;
    border-top:1px dashed var(--border);
    animation: fadeUp .5s ease both;
  }
  .score-hero{
    display:flex;
    align-items:center;
    gap:20px;
    margin-bottom:20px;
  }
  .score-ring{
    width:90px;height:90px;
    border-radius:50%;
    display:flex;align-items:center;justify-content:center;
    font-family:var(--serif);
    font-size:1.6rem;
    font-weight:700;
    background: conic-gradient(var(--accent) calc(var(--pct,50)*1%), #2c2c30 0);
    position:relative;
    flex-shrink:0;
  }
  .score-ring::before{
    content:'';
    position:absolute;
    inset:7px;
    background:var(--card);
    border-radius:50%;
  }
  .score-ring span{position:relative;z-index:1;}
  .score-hero .desc h3{margin:0 0 4px;font-family:var(--serif);font-size:1.2rem;}
  .score-hero .desc p{margin:0;color:var(--text-dim);font-size:0.9rem;}

  .mismatch{
    background:rgba(239,83,80,0.08);
    border:1px solid rgba(239,83,80,0.3);
    border-radius:10px;
    padding:14px 16px;
    margin-bottom:10px;
    font-size:0.92rem;
  }
  .mismatch b{color:var(--danger);}

  .rewrite-box{
    background:rgba(76,175,130,0.08);
    border:1px solid rgba(76,175,130,0.3);
    border-radius:10px;
    padding:16px;
    font-family:var(--serif);
    font-size:1.15rem;
    margin:14px 0;
  }
  .rewrite-box .label{
    font-family:var(--sans);
    font-size:11px;
    text-transform:uppercase;
    letter-spacing:1px;
    color:var(--good);
    display:block;
    margin-bottom:6px;
    font-weight:700;
  }

  .takeaway{
    background:linear-gradient(160deg, rgba(245,197,24,0.1), transparent);
    border-left:4px solid var(--accent);
    padding:16px 18px;
    border-radius:0 10px 10px 0;
    margin-top:18px;
    font-size:0.95rem;
  }
  .takeaway b{color:var(--accent);}

  .tech-badge{
    display:inline-block;
    background:var(--bg-alt);
    border:1px solid var(--accent-dim);
    color:var(--accent);
    padding:6px 14px;
    border-radius:999px;
    font-size:0.85rem;
    font-weight:700;
    margin-bottom:14px;
  }

  .emo-word{
    background:rgba(245,197,24,0.18);
    color:var(--accent);
    padding:1px 4px;
    border-radius:4px;
    font-weight:700;
  }

  /* dashboard */
  .dashboard-hero{
    text-align:center;
    padding:40px 20px;
  }
  .dashboard-hero .big-score{
    font-family:var(--serif);
    font-size:4.5rem;
    font-weight:700;
    color:var(--accent);
    line-height:1;
    margin:10px 0;
    text-shadow:0 0 40px var(--accent-glow);
  }
  .habit-list{
    list-style:none;
    padding:0;
    margin:0;
    display:grid;
    gap:12px;
  }
  .habit-list li{
    background:var(--bg-alt);
    border:1px solid var(--border);
    border-radius:10px;
    padding:14px 18px;
    display:flex;
    gap:12px;
    align-items:flex-start;
  }
  .habit-list li .num{
    background:var(--accent);
    color:#141414;
    font-weight:800;
    width:26px;height:26px;
    border-radius:50%;
    display:flex;align-items:center;justify-content:center;
    flex-shrink:0;
    font-size:0.85rem;
  }
  .redflag-box{
    background:rgba(239,83,80,0.08);
    border:1px solid rgba(239,83,80,0.3);
    border-radius:12px;
    padding:18px;
    margin:16px 0;
  }

  .fade-hidden{display:none;}

  @keyframes fadeUp{
    from{opacity:0; transform:translateY(14px);}
    to{opacity:1; transform:translateY(0);}
  }
  @keyframes fadeDown{
    from{opacity:0; transform:translateY(-14px);}
    to{opacity:1; transform:translateY(0);}
  }
  @keyframes pulse{
    0%,100%{opacity:1;}
    50%{opacity:0.5;}
  }
  .pulse{animation:pulse 1.6s ease infinite;}

  footer.credit{
    text-align:center;
    color:var(--text-dim);
    font-size:12px;
    margin-top:60px;
    letter-spacing:0.5px;
  }

  @media (max-width:640px){
    .metrics{grid-template-columns:repeat(2,1fr);}
    header.top h1{font-size:2rem;}
    .headline-box{font-size:1.3rem;}
    .score-hero{flex-direction:column; text-align:center;}
    .dashboard-hero .big-score{font-size:3.2rem;}
  }
</style>
</head>
<body>
<div class="wrap">

  <header class="top">
    <div class="kicker">Media Literacy Lab</div>
    <h1>Media Integrity Analyzer</h1>
    <p>A guided lesson in reading between the lines — learn to spot misleading headlines and emotional manipulation before you react to them.</p>
  </header>

  <div class="progress-track"><div class="progress-fill" id="progressFill"></div></div>
  <div class="progress-label">
    <span id="progressText">Step 1 of 3</span>
    <span id="progressPct">0%</span>
  </div>

  <div class="metrics">
    <div class="metric-card">
      <div class="metric-label">Headline Accuracy</div>
      <div class="metric-value" id="m-headline">—</div>
      <div class="metric-bar"><div class="metric-bar-fill" id="m-headline-bar" style="background:var(--accent)"></div></div>
    </div>
    <div class="metric-card">
      <div class="metric-label">Source Reliability</div>
      <div class="metric-value" id="m-source">—</div>
      <div class="metric-bar"><div class="metric-bar-fill" id="m-source-bar" style="background:var(--accent)"></div></div>
    </div>
    <div class="metric-card">
      <div class="metric-label">Emotional Manipulation</div>
      <div class="metric-value" id="m-emotion">—</div>
      <div class="metric-bar"><div class="metric-bar-fill" id="m-emotion-bar" style="background:var(--danger)"></div></div>
    </div>
    <div class="metric-card">
      <div class="metric-label">Audience Targeting</div>
      <div class="metric-value" id="m-audience">—</div>
      <div class="metric-bar"><div class="metric-bar-fill" id="m-audience-bar" style="background:var(--accent)"></div></div>
    </div>
  </div>

  <!-- ============ CHALLENGE 1 ============ -->
  <div id="section1">

    <div class="card concept-card">
      <span class="tag">Concept 01</span>
      <h2>Headlines Are Sales Pitches</h2>
      <p>A headline's job isn't to inform you — it's to make you click. Writers and algorithms often stretch, exaggerate, or twist facts to grab attention, even when the actual story is far less dramatic.</p>
      <div class="why"><b>Why it matters:</b> Most people only read the headline, not the article. If the headline misleads, that becomes the "fact" they remember and share — even if it's wrong.</div>
    </div>

    <div class="card" id="challenge1Card">
      <div class="source-line" id="c1-source">DAILY PULSE NEWS</div>
      <div class="headline-box" id="c1-headline">Loading headline...</div>
      <div class="article-body" id="c1-article"></div>

      <div style="margin-top:24px;">
        <p style="font-weight:600; margin-bottom:10px;">🤔 Would you click this headline?</p>
        <div class="btn-row" id="c1-click-choices">
          <button class="choice-btn" data-val="Yes">Yes</button>
          <button class="choice-btn" data-val="Maybe">Maybe</button>
          <button class="choice-btn" data-val="No">No</button>
        </div>
      </div>

      <div style="margin-top:24px;">
        <p style="font-weight:600; margin-bottom:10px;">✏️ What parts feel exaggerated or misleading? (type a few words/phrases, or click any that stand out)</p>
        <div class="word-pick-area" id="c1-word-chips"></div>
        <textarea id="c1-notes" placeholder="Optional: describe in your own words what feels off..."></textarea>
      </div>

      <div class="btn-row">
        <button class="primary-btn" id="c1-reveal-btn" disabled>Reveal Analysis</button>
      </div>

      <div class="reveal fade-hidden" id="c1-reveal"></div>
    </div>

    <div class="btn-row fade-hidden" id="c1-next-row">
      <button class="primary-btn" id="goTo2">Continue to Challenge 2 →</button>
    </div>
  </div>

  <!-- ============ CHALLENGE 2 ============ -->
  <div id="section2" class="fade-hidden">

    <div class="card concept-card">
      <span class="tag">Concept 02</span>
      <h2>Emotions Drive Engagement</h2>
      <p>Content that makes you feel fear, outrage, awe, or urgency spreads faster than calm, balanced content. That's not an accident — it's a design choice, whether by a person or an algorithm optimizing for reactions.</p>
      <div class="why"><b>Why it matters:</b> When you're emotionally activated, you're less likely to fact-check and more likely to share. Recognizing the pull is the first step to resisting it.</div>
    </div>

    <div class="card" id="challenge2Card">
      <div class="social-post">
        <div class="handle" id="c2-handle">@account <span>· sponsored reach</span></div>
        <div class="caption" id="c2-caption">Loading post...</div>
      </div>

      <div style="margin-top:20px;">
        <p style="font-weight:600; margin-bottom:10px;">💭 How did this make you feel?</p>
        <div class="btn-row" id="c2-feel-choices">
          <button class="choice-btn" data-val="Anxious">Anxious</button>
          <button class="choice-btn" data-val="Excited">Excited</button>
          <button class="choice-btn" data-val="Angry">Angry</button>
          <button class="choice-btn" data-val="Inspired">Inspired</button>
          <button class="choice-btn" data-val="Suspicious">Suspicious</button>
          <button class="choice-btn" data-val="Nothing">Nothing much</button>
        </div>
      </div>

      <div style="margin-top:22px;">
        <p style="font-weight:600; margin-bottom:10px;">🔍 Which words influenced that feeling? (click any that stand out)</p>
        <div class="word-pick-area" id="c2-word-chips"></div>
      </div>

      <div class="btn-row">
        <button class="primary-btn" id="c2-reveal-btn" disabled>Reveal Analysis</button>
      </div>

      <div class="reveal fade-hidden" id="c2-reveal"></div>
    </div>

    <div class="btn-row fade-hidden" id="c2-next-row">
      <button class="primary-btn" id="goTo3">See My Media Integrity Dashboard →</button>
    </div>
  </div>

  <!-- ============ DASHBOARD ============ -->
  <div id="section3" class="fade-hidden">
    <div class="card dashboard-hero">
      <div class="kicker" style="color:var(--accent)">Final Report</div>
      <h2 style="font-family:var(--serif); margin:6px 0;">Your Media Integrity Score</h2>
      <div class="big-score" id="finalScore">--</div>
      <p style="color:var(--text-dim);" id="finalScoreDesc">Complete the challenges to see your results.</p>
    </div>

    <div class="card">
      <h3 style="font-family:var(--serif); margin-top:0;">📘 What You Learned</h3>
      <p id="learnedText" style="color:var(--text-dim);"></p>
    </div>

    <div class="card">
      <h3 style="font-family:var(--serif); margin-top:0;">🚩 Your Biggest Red Flag</h3>
      <div class="redflag-box" id="redFlagBox"></div>
    </div>

    <div class="card">
      <h3 style="font-family:var(--serif); margin-top:0;">✅ Three Habits to Build</h3>
      <ul class="habit-list">
        <li><span class="num">1</span><div>Read the full article before reacting or sharing — headlines are written to provoke a click, not to summarize accurately.</div></li>
        <li><span class="num">2</span><div>Notice your emotional reaction. If a post makes you feel intense fear, anger, or excitement, pause before you engage.</div></li>
        <li><span class="num">3</span><div>Check the source and look for a second, independent source before trusting a claim as fact.</div></li>
      </ul>
    </div>

    <div class="btn-row" style="justify-content:center;">
      <button class="primary-btn" id="replayBtn">🔄 Replay with New Scenarios</button>
    </div>
  </div>

  <footer class="credit">Media Integrity Analyzer · A self-contained media literacy exercise · No data leaves your browser</footer>
</div>

<script>
(function(){

  /* ---------------- DATA POOLS ---------------- */

  const headlinePool = [
    {
      source: "THE DAILY PULSE",
      headline: "Local Café Owner's SHOCKING Decision Leaves Entire Town in Uproar",
      article: "A neighborhood café owner in Millbrook announced this week that the shop will close on Sundays starting next month, citing staff wellbeing. Several regular customers expressed mild disappointment on the community Facebook page, while others supported the move. The owner said the change would let staff 'rest and recharge.'",
      accuracy: 28,
      mismatches: [
        { phrase: "SHOCKING Decision", issue: "Closing one day a week is a routine business choice, not shocking." },
        { phrase: "Entire Town in Uproar", issue: "The article only mentions a few comments on a local Facebook page — not town-wide outrage." }
      ],
      fairHeadline: "Local Café to Close on Sundays for Staff Wellbeing",
      takeaway: "Words like 'shocking' and 'uproar' create drama that the actual facts don't support. Always check whether the emotional intensity of a headline matches the substance of the story."
    },
    {
      source: "GLOBAL WATCH DAILY",
      headline: "Scientists Say New Discovery Could CHANGE EVERYTHING We Know About Sleep",
      article: "Researchers at a university sleep lab found that a specific breathing pattern was associated with slightly faster onset of deep sleep in a small study of 40 participants. The lead researcher noted that larger studies are needed before drawing firm conclusions, and called the results 'an interesting but early finding.'",
      accuracy: 22,
      mismatches: [
        { phrase: "CHANGE EVERYTHING", issue: "The researchers themselves call it an 'early finding' from a small study — the opposite of a field-changing breakthrough." },
        { phrase: "Scientists Say", issue: "Implies broad scientific consensus, but this is one small study from one lab." }
      ],
      fairHeadline: "Small Study Finds Possible Link Between Breathing Pattern and Faster Sleep Onset",
      takeaway: "Preliminary research is often inflated into sweeping claims. Look for sample size, replication, and how confident the researchers themselves actually sound."
    },
    {
      source: "METRO REPORT",
      headline: "City Council QUIETLY Votes to Raise Parking Fees While No One Was Watching",
      article: "At Tuesday's publicly announced and live-streamed council meeting, members voted 5-2 to raise downtown parking fees by 50 cents per hour starting in the fall, to fund sidewalk repairs. The meeting agenda was published a week in advance on the city's website.",
      accuracy: 18,
      mismatches: [
        { phrase: "QUIETLY", issue: "The meeting was publicly announced, live-streamed, and posted in advance — it wasn't quiet at all." },
        { phrase: "While No One Was Watching", issue: "This implies secrecy, but the process was fully public and documented." }
      ],
      fairHeadline: "City Council Approves 50-Cent Parking Fee Increase to Fund Sidewalk Repairs",
      takeaway: "Language implying secrecy ('quietly', 'while no one was watching') is often used to make routine government processes sound scandalous."
    }
  ];

  const socialPool = [
    {
      handle: "@wellnesswithkira",
      caption: "I can't believe more people aren't talking about this. Doctors are TERRIFIED of what this one habit does to your body after age 30. Everyone needs to see this before it's too late. 😱🚨",
      audience: "Adults 25–45 interested in health and wellness content, especially those anxious about aging.",
      targetEmotion: "Fear and urgency",
      technique: "Fear appeal + false scarcity ('before it's too late') + appeal to hidden authority ('doctors are terrified')",
      emoWords: ["TERRIFIED", "before it's too late", "can't believe", "🚨"],
      neutralRewrite: "A new habit may have some health effects after age 30. Here's what current research actually says.",
      takeaway: "Phrases like 'doctors are terrified' and 'before it's too late' manufacture urgency without giving any real evidence. Strong fear language is a signal to slow down, not speed up."
    },
    {
      handle: "@moneymindsetmax",
      caption: "This is the ONLY way normal people are building wealth in 2026 and the banks don't want you to know about it. I wasted 5 years not knowing this. Link in bio before it's taken down. 💸🔥",
      audience: "Young adults feeling financially anxious or behind on savings/investing.",
      targetEmotion: "Urgency and FOMO (fear of missing out)",
      technique: "False scarcity ('before it's taken down') + conspiracy framing ('banks don't want you to know') + social proof pressure",
      emoWords: ["ONLY way", "banks don't want you to know", "before it's taken down", "🔥"],
      neutralRewrite: "Here's one approach to saving and investing that worked for me — it may not work for everyone.",
      takeaway: "Claims of secret knowledge being hidden by powerful institutions are a common manipulation pattern used to create urgency and distrust of normal sources."
    },
    {
      handle: "@dailyoutragewire",
      caption: "You will NOT believe what they just did. This is absolutely disgusting and everyone needs to see it RIGHT NOW before they delete it. Share before it's gone!!",
      audience: "Users prone to sharing viral outrage content, often across political or social divides.",
      targetEmotion: "Outrage and moral urgency",
      technique: "Vague outrage bait (no actual details given) + artificial urgency ('before they delete it') + call to mass sharing",
      emoWords: ["disgusting", "RIGHT NOW", "before they delete it", "NOT believe"],
      neutralRewrite: "A new development has some people upset. Here are the details as reported so far.",
      takeaway: "Notice that this post never says *what* actually happened. Content that provokes strong reactions without giving concrete details is a red flag for engagement bait."
    }
  ];

  /* ---------------- STATE ---------------- */
  let state = {
    step: 1,
    c1: { pick: null, chosenWords: [], data: null },
    c2: { feel: null, chosenWords: [], data: null },
    metrics: { headline: null, source: null, emotion: null, audience: null }
  };

  function rand(arr){ return arr[Math.floor(Math.random()*arr.length)]; }

  /* ---------------- PROGRESS ---------------- */
  function updateProgress(){
    const pct = state.step===1?5:state.step===2?50:100;
    document.getElementById('progressFill').style.width = pct+'%';
    document.getElementById('progressText').textContent = 'Step '+state.step+' of 3';
    document.getElementById('progressPct').textContent = pct+'%';
  }

  /* ---------------- METRICS ---------------- */
  function setMetric(key, value, barId, valId){
    state.metrics[key] = value;
    document.getElementById(valId).textContent = value + '%';
    const bar = document.getElementById(barId);
    requestAnimationFrame(()=>{ bar.style.width = value+'%'; });
  }

  /* ================= CHALLENGE 1 ================= */
  function loadChallenge1(){
    const data = rand(headlinePool);
    state.c1.data = data;
    state.c1.pick = null;
    state.c1.chosenWords = [];
    document.getElementById('c1-source').textContent = data.source;
    document.getElementById('c1-headline').textContent = data.headline;
    document.getElementById('c1-article').textContent = data.article;
    document.getElementById('c1-reveal').innerHTML = '';
    document.getElementById('c1-reveal').classList.add('fade-hidden');
    document.getElementById('c1-next-row').classList.add('fade-hidden');
    document.getElementById('c1-reveal-btn').disabled = true;
    document.getElementById('c1-reveal-btn').textContent = 'Reveal Analysis';

    // reset click choices
    document.querySelectorAll('#c1-click-choices .choice-btn').forEach(b=>b.classList.remove('selected'));

    // build word chips from headline words
    const chipWrap = document.getElementById('c1-word-chips');
    chipWrap.innerHTML = '';
    const words = data.headline.replace(/[^a-zA-Z0-9\s]/g,'').split(' ').filter(w=>w.length>3);
    const uniqueWords = [...new Set(words)];
    uniqueWords.forEach(w=>{
      const chip = document.createElement('div');
      chip.className = 'word-chip';
      chip.textContent = w;
      chip.addEventListener('click', ()=>{
        chip.classList.toggle('picked');
        const idx = state.c1.chosenWords.indexOf(w);
        if(idx>-1) state.c1.chosenWords.splice(idx,1);
        else state.c1.chosenWords.push(w);
      });
      chipWrap.appendChild(chip);
    });
    document.getElementById('c1-notes').value = '';
  }

  document.querySelectorAll('#c1-click-choices .choice-btn').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      document.querySelectorAll('#c1-click-choices .choice-btn').forEach(b=>b.classList.remove('selected'));
      btn.classList.add('selected');
      state.c1.pick = btn.dataset.val;
      document.getElementById('c1-reveal-btn').disabled = false;
    });
  });

  document.getElementById('c1-reveal-btn').addEventListener('click', ()=>{
    const data = state.c1.data;
    const reveal = document.getElementById('c1-reveal');
    let mismatchHtml = data.mismatches.map(m=>
      `<div class="mismatch"><b>"${m.phrase}"</b> — ${m.issue}</div>`
    ).join('');

    reveal.innerHTML = `
      <div class="score-hero">
        <div class="score-ring" style="--pct:${data.accuracy}"><span>${data.accuracy}%</span></div>
        <div class="desc">
          <h3>Headline Accuracy Score</h3>
          <p>How closely the headline reflects the actual article content.</p>
        </div>
      </div>
      <p style="font-weight:600; margin-bottom:8px;">Highlighted Mismatches</p>
      ${mismatchHtml}
      <div class="rewrite-box">
        <span class="label">Fair, Accurate Rewrite</span>
        ${data.fairHeadline}
      </div>
      <div class="takeaway"><b>Key takeaway:</b> ${data.takeaway}</div>
    `;
    reveal.classList.remove('fade-hidden');
    document.getElementById('c1-next-row').classList.remove('fade-hidden');
    document.getElementById('c1-reveal-btn').disabled = true;
    document.getElementById('c1-reveal-btn').textContent = 'Analysis Revealed ✓';

    setMetric('headline', data.accuracy, 'm-headline-bar', 'm-headline');
    const sourceScore = Math.max(20, data.accuracy - 5 + Math.floor(Math.random()*10));
    setMetric('source', sourceScore, 'm-source-bar', 'm-source');

    reveal.scrollIntoView({behavior:'smooth', block:'nearest'});
  });

  document.getElementById('goTo2').addEventListener('click', ()=>{
    state.step = 2;
    updateProgress();
    document.getElementById('section1').classList.add('fade-hidden');
    document.getElementById('section2').classList.remove('fade-hidden');
    window.scrollTo({top:0, behavior:'smooth'});
  });

  /* ================= CHALLENGE 2 ================= */
  function loadChallenge2(){
    const data = rand(socialPool);
    state.c2.data = data;
    state.c2.feel = null;
    state.c2.chosenWords = [];
    document.getElementById('c2-handle').innerHTML = data.handle + ' <span>· sponsored reach</span>';
    document.getElementById('c2-caption').textContent = data.caption;
    document.getElementById('c2-reveal').innerHTML = '';
    document.getElementById('c2-reveal').classList.add('fade-hidden');
    document.getElementById('c2-next-row').classList.add('fade-hidden');
    document.getElementById('c2-reveal-btn').disabled = true;
    document.getElementById('c2-reveal-btn').textContent = 'Reveal Analysis';

    document.querySelectorAll('#c2-feel-choices .choice-btn').forEach(b=>b.classList.remove('selected'));

    const chipWrap = document.getElementById('c2-word-chips');
    chipWrap.innerHTML = '';
    const words = data.caption.replace(/[^a-zA-Z0-9\s]/g,'').split(' ').filter(w=>w.length>3);
    const uniqueWords = [...new Set(words)];
    uniqueWords.forEach(w=>{
      const chip = document.createElement('div');
      chip.className = 'word-chip';
      chip.textContent = w;
      chip.addEventListener('click', ()=>{
        chip.classList.toggle('picked');
        const idx = state.c2.chosenWords.indexOf(w);
        if(idx>-1) state.c2.chosenWords.splice(idx,1);
        else state.c2.chosenWords.push(w);
      });
      chipWrap.appendChild(chip);
    });
  }

  document.querySelectorAll('#c2-feel-choices .choice-btn').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      document.querySelectorAll('#c2-feel-choices .choice-btn').forEach(b=>b.classList.remove('selected'));
      btn.classList.add('selected');
      state.c2.feel = btn.dataset.val;
      document.getElementById('c2-reveal-btn').disabled = false;
    });
  });

  document.getElementById('c2-reveal-btn').addEventListener('click', ()=>{
    const data = state.c2.data;
    const reveal = document.getElementById('c2-reveal');

    let captionHtml = data.caption;
    data.emoWords.forEach(w=>{
      const escaped = w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      const re = new RegExp('('+escaped+')', 'gi');
      captionHtml = captionHtml.replace(re, '<span class="emo-word">$1</span>');
    });

    const emotionScore = 65 + Math.floor(Math.random()*25);
    const audienceScore = 55 + Math.floor(Math.random()*30);

    reveal.innerHTML = `
      <div class="tech-badge">${data.technique.split('+')[0].trim()}</div>
      <p style="font-weight:600; margin-bottom:6px;">Full manipulation technique</p>
      <p style="color:var(--text-dim); margin-top:0;">${data.technique}</p>

      <p style="font-weight:600; margin:16px 0 8px;">Post with emotional triggers highlighted</p>
      <div class="social-post" style="background:var(--bg);">
        <div class="caption">${captionHtml}</div>
      </div>

      <p style="font-weight:600; margin:16px 0 4px;">🎯 Likely target audience</p>
      <p style="color:var(--text-dim); margin-top:0;">${data.audience}</p>

      <p style="font-weight:600; margin:16px 0 4px;">Intended emotional response</p>
      <p style="color:var(--text-dim); margin-top:0;">${data.targetEmotion}</p>

      <div class="rewrite-box">
        <span class="label">Neutral Rewrite</span>
        ${data.neutralRewrite}
      </div>

      <div class="takeaway"><b>Key takeaway:</b> ${data.takeaway}</div>
    `;
    reveal.classList.remove('fade-hidden');
    document.getElementById('c2-next-row').classList.remove('fade-hidden');
    document.getElementById('c2-reveal-btn').disabled = true;
    document.getElementById('c2-reveal-btn').textContent = 'Analysis Revealed ✓';

    setMetric('emotion', emotionScore, 'm-emotion-bar', 'm-emotion');
    setMetric('audience', audienceScore, 'm-audience-bar', 'm-audience');

    reveal.scrollIntoView({behavior:'smooth', block:'nearest'});
  });

  document.getElementById('goTo3').addEventListener('click', ()=>{
    state.step = 3;
    updateProgress();
    document.getElementById('section2').classList.add('fade-hidden');
    document.getElementById('section3').classList.remove('fade-hidden');
    buildDashboard();
    window.scrollTo({top:0, behavior:'smooth'});
  });

  /* ================= DASHBOARD ================= */
  function buildDashboard(){
    const m = state.metrics;
    const overall = Math.round(
      (m.headline*0.3) + (m.source*0.2) + ((100-m.emotion)*0.3) + ((100-m.audience)*0.2)
    );
    document.getElementById('finalScore').textContent = overall + '%';

    let desc = '';
    if(overall >= 70) desc = "Sharp eye! You spotted exaggeration and emotional pull with strong instincts.";
    else if(overall >= 45) desc = "Good start — you noticed some red flags, but a few manipulation tactics still landed.";
    else desc = "This content pulled you in more than it should have. That's normal — now you know what to look for.";
    document.getElementById('finalScoreDesc').textContent = desc;

    document.getElementById('learnedText').textContent =
      "You practiced spotting the gap between a headline's promise and an article's actual content, and you identified how specific words are engineered to trigger fear, urgency, or outrage. Both techniques rely on getting you to react before you think.";

    const worstMetric = m.emotion >= (100-m.headline) ? 'emotion' : 'headline';
    let redFlagText = '';
    if(worstMetric === 'emotion'){
      redFlagText = `Your biggest red flag: <b>Emotional Manipulation (${m.emotion}%)</b>. The social post you reviewed used urgency and fear language designed to bypass careful thinking. Next time you feel a strong reaction to a post, pause for ten seconds before sharing or reacting.`;
    } else {
      redFlagText = `Your biggest red flag: <b>Headline Accuracy (${m.headline}%)</b>. The headline you reviewed significantly oversold the actual story. Get in the habit of reading past the headline before forming an opinion.`;
    }
    document.getElementById('redFlagBox').innerHTML = redFlagText;
  }

  document.getElementById('replayBtn').addEventListener('click', ()=>{
    state = {
      step: 1,
      c1: { pick: null, chosenWords: [], data: null },
      c2: { feel: null, chosenWords: [], data: null },
      metrics: { headline: null, source: null, emotion: null, audience: null }
    };
    ['m-headline','m-source','m-emotion','m-audience'].forEach(id=>{
      document.getElementById(id).textContent = '—';
    });
    ['m-headline-bar','m-source-bar','m-emotion-bar','m-audience-bar'].forEach(id=>{
      document.getElementById(id).style.width = '0%';
    });
    loadChallenge1();
    loadChallenge2();
    document.getElementById('section3').classList.add('fade-hidden');
    document.getElementById('section2').classList.add('fade-hidden');
    document.getElementById('section1').classList.remove('fade-hidden');
    updateProgress();
    window.scrollTo({top:0, behavior:'smooth'});
  });

  /* ---------------- INIT ---------------- */
  loadChallenge1();
  loadChallenge2();
  updateProgress();

})();
</script>
</body>
</html>
<img width="611" height="584" alt="Screenshot_5-7-2026_1686_claude ai" src="https://github.com/user-attachments/assets/26db7c21-ceb4-4d04-a097-e3c5871da0b4" />
<img width="566" height="528" alt="image" src="https://github.com/user-attachments/assets/fb307e95-7370-4bc9-9969-922f5029432b" />
<img width="550" height="552" alt="image" src="https://github.com/user-attachments/assets/a2c44968-346c-4c42-b763-a06c47c6b0e9" />
<img width="607" height="565" alt="image" src="https://github.com/user-attachments/assets/5891b395-a208-4f0d-ab1d-1afb7b696c31" />
<img width="619" height="573" alt="image" src="https://github.com/user-attachments/assets/4faebc62-e461-4717-bd2d-5f0c8a942928" />
<img width="622" height="577" alt="image" src="https://github.com/user-attachments/assets/4a88473d-4a80-4a01-9f89-e33a3a00e8df" />
<img width="567" height="556" alt="image" src="https://github.com/user-attachments/assets/a6e3e5e0-1ac9-44d7-a863-41147b4d85f4" />
<img width="571" height="441" alt="image" src="https://github.com/user-attachments/assets/c9a8a841-bc69-4f9a-a1bc-1c7a1fceef9e" />
<img width="585" height="576" alt="image" src="https://github.com/user-attachments/assets/eef41224-7a58-425e-8be0-a0ec8fd4288a" />
<img width="609" height="583" alt="image" src="https://github.com/user-attachments/assets/ce37b89c-ea4a-4507-9bff-c8be7d945416" />
<img width="600" height="556" alt="image" src="https://github.com/user-attachments/assets/5e019c40-b88c-448d-8fc6-4499a2975dbd" />
<img width="603" height="570" alt="image" src="https://github.com/user-attachments/assets/48b2f831-bd91-4998-af23-344c4a593c0c" />
<img width="601" height="502" alt="image" src="https://github.com/user-attachments/assets/bb5c6aec-0184-477d-afb9-ae56bca595fd" />
<img width="596" height="576" alt="image" src="https://github.com/user-attachments/assets/5dfc527d-67f4-44b9-9d9e-f5dca73e1870" />
<img width="582" height="479" alt="image" src="https://github.com/user-attachments/assets/3a6a393f-ee13-41a0-bfd0-06b0c08a36f3" />

