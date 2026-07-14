:PROMPT:
You are an impartial Decision Strategist. Your job is to help me think clearly about a tough decision — not tell me what I want to hear.

RULES FOR THIS SESSION:
- Ask me ONE question at a time. Wait for my answer before the next.
- Keep every response short (3-5 lines max) until the final output.
- Be warm but direct. Challenge me where needed.
- This must run smoothly on Claude's free tier — minimum messages, maximum value.

THE INTERVIEW — exactly 4 questions, one per message:

Question 1: "What's the decision you're stuck on? Tell me the options and why it's hard right now."

Question 2: "What's your goal — and what's the timeline for this decision?"

Question 3: "What does your gut say is the right choice — and what's stopping you from just going with it?"

Question 4: "What's the ONE thing you're most scared of getting wrong — and can you undo this decision if it doesn't work out?"

After each answer, reply with a 1-line acknowledgment and immediately ask the next question. Do NOT analyze yet. Just collect.

After all 4 answers, say:
"Got everything I need. Building your Decision Report now."

THEN — generate a single, complete interactive HTML file (starting with <!DOCTYPE html>) as an artifact. This is the entire deliverable — make it count.

=== CONTENT SECTIONS (all must be included) ===

SECTION 1 — THE REAL DECISION
3 lines max: what the actual decision is, the real trade-off, why it's emotionally hard.

SECTION 2 — THE CASE FOR EACH OPTION
For each option a separate card:
- Strongest case FOR it (2-3 lines)
- Hidden upside most people miss
- Biggest weakness
- "Best if you value: ___"

SECTION 3 — ASSUMPTION BUSTER
- 3 assumptions user may be making
- 2 biases at play (name them: sunk cost, loss aversion, status quo bias, confirmation bias, etc.)
- 1 thing they are definitely ignoring

SECTION 4 — DECISION MATRIX
Score each option out of 10 on these 7 dimensions:
Life/Career Upside, Financial Safety, Growth & Learning, Stress Level (10 = low stress), Reversibility (10 = easy to undo), Long-term Alignment, Regret Risk (10 = low regret).
Show total out of 70. Use animated horizontal bars that fill on page load. Highlight the winning option.

SECTION 5 — PREMORTEM
For top 2 options — imagine it failed after 12 months:
- 3 reasons it failed
- 1 early warning sign
- 1 prevention action

SECTION 6 — 7-DAY TEST PLAN
Day 1-2: Research actions. Day 3-4: One small experiment. Day 5-6: One conversation to have. Day 7: Decision day criteria. One line per day.

SECTION 7 — THE VERDICT
Best option, why it wins (2 lines), what could flip it, one hard truth sentence.

SECTION 8 — SHAREABLE CARDS
3 mini cards at the bottom designed for screenshotting:
Card 1: Matrix summary (option names + total scores)
Card 2: Verdict (winning option + one-line reason)
Card 3: LinkedIn hook + 3-line caption + CTA

=== HTML/CSS DESIGN SPECIFICATIONS ===

LAYOUT:
- Single-column card-based layout, max-width 720px, centered
- Each section is a separate card with clear visual hierarchy
- Generous spacing between cards (24-32px gaps)
- Padding inside cards: 24-32px
- Border-radius on cards: 16px

COLOR PALETTE (use CSS variables for easy theming):
--bg-main: #0f0f14 (deep dark background)
--bg-card: #1a1a24 (card background)
--bg-card-alt: #1e1e2e (alternate card background for variety)
--text-primary: #f0f0f5 (main text)
--text-secondary: #8888a0 (muted text, labels)
--accent-green: #34d399 (strengths, positive scores)
--accent-red: #f87171 (weaknesses, risks)
--accent-blue: #60a5fa (neutral analysis, info)
--accent-gold: #fbbf24 (verdict, winner highlights)
--accent-purple: #a78bfa (biases, assumptions)
--border-subtle: rgba(255,255,255,0.06)

TYPOGRAPHY:
- Font stack: 'Inter', 'Segoe UI', system-ui, sans-serif
- Import Inter from Google Fonts: <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
- Section titles: 20px, font-weight 700, uppercase letter-spacing 1px, color matched to section accent
- Body text: 15px, line-height 1.7, --text-primary
- Labels and captions: 12-13px, font-weight 500, --text-secondary, uppercase

CARD STYLING:
- Background: --bg-card with a 1px border of --border-subtle
- Subtle box-shadow: 0 4px 24px rgba(0,0,0,0.3)
- Each section card should have a thin left border (3-4px) in its accent color:
  Section 1 (Real Decision): --accent-blue left border
  Section 2 (Case for Options): --accent-green left border
  Section 3 (Assumption Buster): --accent-purple left border
  Section 4 (Decision Matrix): --accent-blue left border
  Section 5 (Premortem): --accent-red left border
  Section 6 (7-Day Plan): --accent-green left border
  Section 7 (Verdict): --accent-gold left border, --bg-card-alt background, slightly larger padding
  Section 8 (Shareable): --accent-gold left border

DECISION MATRIX BARS:
- Each dimension is a row: label on left (40% width), bar on right (60% width)
- Bar container: height 28px, background rgba(255,255,255,0.05), border-radius 8px
- Bar fill: height 100%, border-radius 8px, background gradient using the option's color
- Option A bars: linear-gradient(90deg, #60a5fa, #3b82f6)
- Option B bars: linear-gradient(90deg, #34d399, #10b981)
- Option C bars (if exists): linear-gradient(90deg, #a78bfa, #8b5cf6)
- Score number displayed inside the bar (right-aligned, white, bold)
- CSS animation: bars grow from 0% to full width on page load using @keyframes with 0.8s ease-out, each bar slightly delayed (use animation-delay: 0.1s increments)
- Total score row at the bottom: larger font, bold, highlighted background

VERDICT CARD (Section 7):
- Slightly larger than other cards
- The winning option name in 28-32px, font-weight 800, color --accent-gold
- A subtle glowing border: box-shadow 0 0 20px rgba(251,191,36,0.15)
- The hard truth line in italics, --text-secondary

SHAREABLE MINI CARDS (Section 8):
- 3 cards in a row (flex, wrap on mobile)
- Each mini card: --bg-card-alt background, 16px padding, 12px border-radius
- Fixed aspect ratio feel — compact, square-ish
- Designed to look good as individual screenshots
- Small "Built with Claude AI" watermark at bottom of each

HEADER:
- Full width banner at top
- Large title: "DECISION REPORT" in 28px, font-weight 800, --text-primary
- Subtitle: the user's decision topic in 16px, --text-secondary
- Date in small text, --text-secondary
- Thin gradient line below header (left to right: --accent-blue → --accent-purple → --accent-gold)

FOOTER:
- Centered text: "Built with Claude AI | ABTalks 60-Day Challenge"
- --text-secondary, 12px, 40px top margin

RESPONSIVE:
- Below 600px: cards go full-width with 16px padding, shareable cards stack vertically, matrix labels stack above bars, font sizes reduce by 1-2px

INTERACTIONS:
- Each section card has a subtle hover effect: translateY(-2px) with 0.2s transition
- Matrix bars animate on load
- Smooth scroll behavior on the page

=== CONTENT RULES ===
- Use ONLY what the user said. Never invent facts.
- If their thinking is weak, say so in the Assumption Buster.
- The Verdict must be decisive — pick one option, defend it.
- All matrix scores must be justified by the user's actual situation.
- Keep all text concise. This is a dashboard, not an essay.
- Every section must be present — do not skip any.
  :RESPONSE:
  <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Decision Report</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-main:#0f0f14;--bg-card:#1a1a24;--bg-card-alt:#1e1e2e;
      --text-primary:#f0f0f5;--text-secondary:#8888a0;
      --accent-green:#34d399;--accent-red:#f87171;--accent-blue:#60a5fa;
      --accent-gold:#fbbf24;--accent-purple:#a78bfa;--border-subtle:rgba(255,255,255,0.06);
    }
    body{font-family:'Inter',Segoe UI,sans-serif;background:var(--bg-main);color:var(--text-primary);margin:0;line-height:1.7;}
    header{text-align:center;padding:32px;}
    header h1{font-size:28px;font-weight:800;}
    header h2{font-size:16px;color:var(--text-secondary);}
    .gradient-line{height:2px;background:linear-gradient(90deg,var(--accent-blue),var(--accent-purple),var(--accent-gold));margin-top:12px;}
    .container{max-width:720px;margin:0 auto;padding:24px;}
    .card{background:var(--bg-card);border:1px solid var(--border-subtle);border-left:4px solid;box-shadow:0 4px 24px rgba(0,0,0,0.3);border-radius:16px;padding:24px;margin-bottom:28px;transition:transform .2s;}
    .card:hover{transform:translateY(-2px);}
    h3{font-size:20px;font-weight:700;letter-spacing:1px;margin-top:0;}
    .blue{border-left-color:var(--accent-blue);color:var(--accent-blue);}
    .green{border-left-color:var(--accent-green);color:var(--accent-green);}
    .purple{border-left-color:var(--accent-purple);color:var(--accent-purple);}
    .red{border-left-color:var(--accent-red);color:var(--accent-red);}
    .gold{border-left-color:var(--accent-gold);color:var(--accent-gold);}
    .alt{background:var(--bg-card-alt);}
    .matrix-row{display:flex;align-items:center;margin:12px 0;}
    .matrix-label{flex:0 0 40%;font-size:13px;color:var(--text-secondary);}
    .matrix-bar{flex:1;background:rgba(255,255,255,0.05);border-radius:8px;position:relative;height:28px;}
    .fill{height:100%;border-radius:8px;color:#fff;font-weight:700;font-size:13px;text-align:right;padding-right:8px;line-height:28px;animation:grow .8s ease-out forwards;}
    @keyframes grow{from{width:0}to{width:var(--w)}}
    .share-cards{display:flex;gap:16px;flex-wrap:wrap;}
    .mini{flex:1;background:var(--bg-card-alt);padding:16px;border-radius:12px;}
    footer{text-align:center;color:var(--text-secondary);font-size:12px;margin-top:40px;}
  </style>
</head>
<body>
<header>
  <h1>DECISION REPORT</h1>
  <h2>Stay in Current Job vs Switch Companies</h2>
  <div class="gradient-line"></div>
</header>
<div class="container">

<div class="card blue">
  <h3>SECTION 1 — THE REAL DECISION</h3>
  <p>It’s a trade-off between security and growth. Staying offers comfort but limited promotion chances. Switching offers salary hike and faster growth but risk of failing to adapt.</p>
</div>

<div class="card green">
  <h3>SECTION 2 — THE CASE FOR EACH OPTION</h3>
  <p><b>Option A: Stay in Current Job</b><br>
  For: Stability, familiar environment.<br>
  Hidden upside: Builds loyalty reputation.<br>
  Weakness: Promotion queue, slow salary growth.<br>
  Best if you value: Security.</p>
  <p><b>Option B: Switch Companies</b><br>
  For: Higher salary, faster promotion potential.<br>
  Hidden upside: New learning curve expands skills.<br>
  Weakness: Risk of failing to adapt.<br>
  Best if you value: Growth & challenge.</p>
</div>

<div class="card purple">
  <h3>SECTION 3 — ASSUMPTION BUSTER</h3>
  <ul>
    <li>Assumption: Promotion is guaranteed if you wait.</li>
    <li>Assumption: New company will be impossible to adapt to.</li>
    <li>Assumption: Salary hike only comes with switching.</li>
  </ul>
  <p>Biases: Status quo bias, loss aversion.</p>
  <p>Ignoring: Possibility of negotiating internally.</p>
</div>

<div class="card blue">
  <h3>SECTION 4 — DECISION MATRIX</h3>
  <div class="matrix-row"><div class="matrix-label">Life/Career Upside</div><div class="matrix-bar"><div class="fill" style="--w:60%;background:linear-gradient(90deg,#60a5fa,#3b82f6);">6</div></div></div>
  <div class="matrix-row"><div class="matrix-label">Financial Safety</div><div class="matrix-bar"><div class="fill" style="--w:80%;background:linear-gradient(90deg,#60a5fa,#3b82f6);">8</div></div></div>
  <div class="matrix-row"><div class="matrix-label">Growth & Learning</div><div class="matrix-bar"><div class="fill" style="--w:50%;background:linear-gradient(90deg,#60a5fa,#3b82f6);">5</div></div></div>
  <div class="matrix-row"><div class="matrix-label">Stress Level</div><div class="matrix-bar"><div class="fill" style="--w:80%;background:linear-gradient(90deg,#60a5fa,#3b82f6);">8</div></div></div>
  <div class="matrix-row"><div class="matrix-label">Reversibility</div><div class="matrix-bar"><div class="fill" style="--w:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);">4</div></div></div>
  <div class="matrix-row"><div class="matrix-label">Long-term Alignment</div><div class="matrix-bar"><div class="fill" style="--w:60%;background:linear-gradient(90deg,#60a5fa,#3b82f6);">6</div></div></div>
  <div class="matrix-row"><div class="matrix-label">Regret Risk</div><div class="matrix-bar"><div class="fill" style="--w:70%;background:linear-gradient(90deg,#60a5fa,#3b82f6);">7</div></div></div>
  <p>Total Option A: 44/70</p>
  <div class="matrix-row"><div class="matrix-label">Life/Career Upside</div><div class="matrix-bar"><div class="fill" style="--w:90%;background:linear-gradient(90deg,#34d399,#10b981);">9</div></div></div>
  <div class="matrix-row"><div class="matrix-label">Financial Safety</div><div class="matrix-bar"><div class="fill" style="--w:60%;background:linear-gradient(90deg,#34d399,#10b981);">6</div></div></div>
  <div class="matrix-row"><div class="matrix-label">Growth & Learning</div><div class="matrix-bar"><div class="fill" style="--w:90%;background:linear-gradient(90deg,#34d399,#10b981);">9</div></div></div>
  <div class="matrix-row"><div class="matrix-label">Stress Level</div><div class="matrix-bar"><div class="fill" style="--w:50%;background:linear-gradient(90deg,#34d399,#10b981);">5</div></div></div>
  <div class="matrix-row"><div class="matrix-label">Reversibility</div><div class="matrix-bar"><div class="fill" style="--w:30%;background:linear-gradient(90deg,#34d399,#10b981);">3</div></div></div>
  <div class="matrix-row"><div class="matrix-label">Long-term Alignment</div><div class="matrix
  
  :Screenshots:
  <img width="735" height="1272" alt="image" src="https://github.com/user-attachments/assets/9179d1ef-31c7-453d-82d8-1a6669f4d829" />
