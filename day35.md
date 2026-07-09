:Prompt: You are an expert frontend developer, UX designer, instructional designer, game designer and prompt engineering expert.

Before generating anything, interview the user in chat.

Ask ONLY these two questions:

Question 1:
Which domain would you like to practice prompting for?
Provide options covering all major domains.

Question 2:
Choose your difficulty.

Do not ask any more questions.

Once both answers are received, generate the application.

Create a premium single-file HTML application called '🧩 Prompt Puzzle — Master AI Prompting Through Play'.

The application must work offline by simply opening the HTML file.

Use React via CDN only if it works reliably as a standalone HTML file; otherwise automatically switch to pure HTML, CSS, and vanilla JavaScript.

Everything must exist inside ONE HTML file.

Generate 6–8 randomized scenarios based on the selected domain and difficulty.

Each scenario must include:
- Desired Output
- Correct Prompt Blocks
- Distractor Blocks
- Weak Prompt
- Optimized Prompt
- Over-Engineered Prompt
- Weak AI Output
- Optimized AI Output
- Prompt Principle

Include exactly three challenge types:
1. Build the Prompt
2. Clean the Prompt
3. Choose the Best Prompt

Implement live scoring using Accuracy, Time, Moves, Wrong Placements, Hints Used, and Optimization Bonus.

Generate a Prompt Performance Report including Prompt Score, Rating, Rank, Prompt DNA visualization, personalized feedback, next milestone, and final optimized prompt.

Allow replay with new randomized scenarios.

Use a premium modern UI with drag-and-drop, hover effects, floating notifications, score animations, micro-interactions, and progress indicators.

Store scenarios in reusable JavaScript objects.

Everything must work offline with zero syntax or runtime errors.

If output becomes too large, reduce only the number of scenarios.

Return ONLY the complete HTML inside one code block.

:Response: :html:
Yes — mixed across all domains (Business, Software, Creative Writing, Education, and Gaming/Entertainment), at Intermediate difficulty. Just open the HTML file in any browser, no internet needed. It randomly draws 7 scenarios across those domains, cycles through all three challenge types (Build/Clean/Choose the Prompt), and ends with a full Performance Report + Prompt DNA + replay option.
:HTML:
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>🧩 Prompt Puzzle — Master AI Prompting Through Play</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  :root{
    --bg1:#0f0c29; --bg2:#302b63; --bg3:#24243e;
    --accent:#8b5cf6; --accent2:#06b6d4; --gold:#fbbf24;
    --good:#22c55e; --bad:#ef4444; --card:#1a1735;
    --text:#eef0ff; --muted:#a4a3c4;
  }
  *{box-sizing:border-box; margin:0; padding:0;}
  body{
    font-family:'Segoe UI', system-ui, -apple-system, sans-serif;
    background:linear-gradient(135deg,var(--bg1),var(--bg2) 50%,var(--bg3));
    background-attachment:fixed;
    color:var(--text); min-height:100vh; overflow-x:hidden;
  }
  #app{max-width:1100px;margin:0 auto;padding:24px 16px 80px;}
  h1{font-size:1.9rem;background:linear-gradient(90deg,var(--accent),var(--accent2),var(--gold));
     -webkit-background-clip:text;background-clip:text;color:transparent;text-align:center;margin-bottom:6px;}
  .subtitle{text-align:center;color:var(--muted);margin-bottom:24px;font-size:.95rem;}
  .card{background:rgba(26,23,53,.75);border:1px solid rgba(139,92,246,.25);
        border-radius:16px;padding:22px;backdrop-filter:blur(10px);
        box-shadow:0 8px 32px rgba(0,0,0,.35);margin-bottom:20px;}
  .btn{cursor:pointer;border:none;border-radius:10px;padding:12px 22px;font-weight:600;
       font-size:.95rem;color:#fff;background:linear-gradient(135deg,var(--accent),var(--accent2));
       transition:transform .15s, box-shadow .15s; box-shadow:0 4px 14px rgba(139,92,246,.35);}
  .btn:hover{transform:translateY(-2px) scale(1.02);box-shadow:0 8px 22px rgba(139,92,246,.5);}
  .btn:active{transform:scale(.97);}
  .btn.secondary{background:rgba(255,255,255,.08);box-shadow:none;}
  .btn.secondary:hover{background:rgba(255,255,255,.16);}
  .btn:disabled{opacity:.4;cursor:not-allowed;transform:none;}
  .grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px;}
  @media(max-width:720px){.grid2{grid-template-columns:1fr;}}
  select,input{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.15);
        color:var(--text);padding:10px 14px;border-radius:8px;font-size:.95rem;width:100%;}
  label{font-size:.85rem;color:var(--muted);display:block;margin-bottom:6px;}
  .option-card{background:rgba(255,255,255,.05);border:2px solid rgba(255,255,255,.1);
        border-radius:14px;padding:16px;margin-bottom:20px;}
  .option-card:hover{border-color:var(--accent);}
  .center{text-align:center;}
  .hidden{display:none !important;}
  .badge{display:inline-block;padding:3px 10px;border-radius:20px;font-size:.75rem;font-weight:700;
         background:rgba(139,92,246,.25);color:#c4b5fd;margin-left:8px;}
  .badge.gold{background:rgba(251,191,36,.2);color:var(--gold);}
  .badge.good{background:rgba(34,197,94,.2);color:var(--good);}
  .badge.bad{background:rgba(239,68,68,.2);color:var(--bad);}
  .progress-bar{height:8px;border-radius:10px;background:rgba(255,255,255,.08);overflow:hidden;margin-bottom:6px;}
  .progress-fill{height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));
      transition:width .5s ease; border-radius:10px;}
  .stat-row{display:flex;flex-wrap:wrap;gap:10px;margin-top:12px;}
  .stat-pill{background:rgba(255,255,255,.06);border-radius:10px;padding:8px 14px;font-size:.82rem;
        color:var(--muted); display:flex;gap:6px;align-items:center;}
  .stat-pill b{color:var(--text);}
  .block{cursor:grab;user-select:none;background:linear-gradient(135deg,rgba(139,92,246,.18),rgba(6,182,212,.12));
     border:1.5px solid rgba(139,92,246,.4); border-radius:10px;padding:12px 14px;margin:6px 0;
     font-size:.9rem; transition:all .15s; position:relative;}
  .block:hover{border-color:var(--accent2); transform:translateX(3px);}
  .block.dragging{opacity:.4;}
  .block.placed{cursor:default;}
  .block.correct-flash{animation:flashGood .6s;}
  .block.wrong-flash{animation:flashBad .5s;}
  @keyframes flashGood{0%{background:rgba(34,197,94,.5);}100%{background:rgba(139,92,246,.18);}}
  @keyframes flashBad{0%{background:rgba(239,68,68,.5);}100%{background:rgba(139,92,246,.18);}}
  .dropzone{min-height:60px;border:2px dashed rgba(255,255,255,.2);border-radius:12px;padding:10px;
        background:rgba(255,255,255,.02); transition:all .2s;}
  .dropzone.dragover{border-color:var(--accent2);background:rgba(6,182,212,.08);}
  .dropzone .placeholder{color:var(--muted);font-size:.85rem;text-align:center;padding:14px 0;}
  .col-title{font-size:.85rem;color:var(--muted);text-transform:uppercase;letter-spacing:.05em;margin-bottom:8px;}
  .choice-option{border:2px solid rgba(255,255,255,.12);border-radius:12px;padding:14px 16px;margin-bottom:12px;
      cursor:pointer;transition:all .15s; background:rgba(255,255,255,.03);}
  .choice-option:hover{border-color:var(--accent2);background:rgba(6,182,212,.06);}
  .choice-option.selected-correct{border-color:var(--good);background:rgba(34,197,94,.12);}
  .choice-option.selected-wrong{border-color:var(--bad);background:rgba(239,68,68,.12);}
  .choice-label{font-weight:700;color:var(--accent2);margin-right:6px;}
  pre.prompt-text{white-space:pre-wrap;font-family:'Consolas',monospace;font-size:.85rem;
      background:rgba(0,0,0,.25);padding:10px 12px;border-radius:8px;margin-top:8px;color:#dcdcff;}
  .toast-wrap{position:fixed;top:16px;right:16px;z-index:999;display:flex;flex-direction:column;gap:8px;}
  .toast{background:rgba(26,23,53,.95);border:1px solid rgba(139,92,246,.5);border-radius:10px;
      padding:12px 18px;font-size:.88rem;box-shadow:0 6px 20px rgba(0,0,0,.4);
      animation:slideIn .3s ease, fadeOut .4s ease 2.4s forwards; max-width:280px;}
  @keyframes slideIn{from{transform:translateX(60px);opacity:0;}to{transform:translateX(0);opacity:1;}}
  @keyframes fadeOut{to{opacity:0;transform:translateX(30px);}}
  .toast.good{border-color:var(--good);}
  .toast.bad{border-color:var(--bad);}
  .score-pop{position:fixed;pointer-events:none;font-weight:800;font-size:1.3rem;color:var(--gold);
      animation:popUp 1s ease forwards; z-index:998;}
  @keyframes popUp{0%{opacity:1;transform:translateY(0);}100%{opacity:0;transform:translateY(-50px);}}
  .dna-bar{display:flex;height:26px;border-radius:8px;overflow:hidden;margin:10px 0;}
  .dna-seg{transition:width .6s;}
  .rank-big{font-size:2.6rem;text-align:center;font-weight:800;
      background:linear-gradient(90deg,var(--gold),var(--accent2));-webkit-background-clip:text;
      background-clip:text;color:transparent;margin:8px 0;}
  .report-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin:16px 0;}
  .report-stat{background:rgba(255,255,255,.05);border-radius:12px;padding:14px;text-align:center;}
  .report-stat .val{font-size:1.5rem;font-weight:800;color:var(--accent2);}
  .report-stat .lbl{font-size:.75rem;color:var(--muted);margin-top:4px;}
  .hint-box{background:rgba(251,191,36,.1);border:1px solid rgba(251,191,36,.35);border-radius:10px;
      padding:10px 14px;margin-top:10px;font-size:.85rem;color:#fde68a;}
  .principle-box{background:rgba(6,182,212,.1);border:1px solid rgba(6,182,212,.3);border-radius:10px;
      padding:12px 14px;margin-top:14px;font-size:.87rem;}
  .flex-between{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;}
  .small-muted{font-size:.78rem;color:var(--muted);}
  .scenario-nav{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:14px;}
  .dot{width:12px;height:12px;border-radius:50%;background:rgba(255,255,255,.15);}
  .dot.done{background:var(--good);}
  .dot.current{background:var(--accent2);box-shadow:0 0 8px var(--accent2);}
  .fade-in{animation:fadeInUp .4s ease;}
  @keyframes fadeInUp{from{opacity:0;transform:translateY(12px);}to{opacity:1;transform:translateY(0);}}
</style>
</head>
<body>
<div id="app"></div>
<div class="toast-wrap" id="toastWrap"></div>

<script>
/* =============================================================
   🧩 PROMPT PUZZLE — MASTER AI PROMPTING THROUGH PLAY
   Single-file vanilla JS app. No external dependencies.
============================================================= */

// ---------- STATE ----------
const STATE = {
  domain: null,
  difficulty: null,
  scenarios: [],
  currentIndex: 0,
  score: 0,
  moves: 0,
  wrongPlacements: 0,
  hintsUsed: 0,
  correctPlacements: 0,
  startTime: null,
  scenarioResults: [], // per scenario: {type, correct, wrong, hints, time, optBonus}
  optimizationBonus: 0,
};

// ---------- SCENARIO BANK ----------
// Each scenario is domain-tagged so we can filter/mix
const SCENARIO_BANK = [
  {
    domain:"Business & Marketing",
    title:"Product Launch Email",
    desiredOutput:"A concise, persuasive launch email for a new productivity app, targeted at busy professionals, with a clear CTA.",
    correctBlocks:[
      "Act as an expert email marketer.",
      "Write a launch email for 'FlowTask', a productivity app for busy professionals.",
      "Tone: energetic but professional.",
      "Include one clear call-to-action to start a free trial.",
      "Keep it under 150 words."
    ],
    distractorBlocks:[
      "Explain the entire history of email marketing.",
      "Use as many buzzwords as possible.",
      "Write it in the form of a legal disclaimer.",
      "Make it 2000 words long."
    ],
    weakPrompt:"Write an email about my app.",
    optimizedPrompt:"Act as an expert email marketer. Write a launch email for 'FlowTask', a productivity app for busy professionals. Tone: energetic but professional. Include one clear call-to-action to start a free trial. Keep it under 150 words.",
    overEngineeredPrompt:"As the world's greatest Grammy-winning Pulitzer Prize marketing legend combined with a Harvard MBA and 40 years of experience, using advanced neuro-linguistic persuasion frameworks, psychological triggers, scarcity tactics, urgency multipliers, and a 27-step copywriting checklist, write an email about FlowTask covering every possible feature, testimonial, pricing tier, competitor comparison, and philosophical reflection on productivity itself, formatted in Markdown with emojis, while also including a haiku.",
    weakOutput:"Hey! Check out my app, it's really good and helps you do stuff. Try it today!",
    optimizedOutput:"Subject: Reclaim Your Day with FlowTask 🚀\n\nHi [Name],\n\nBusy professionals lose 5+ hours a week to scattered tasks. FlowTask brings your to-dos, calendar, and notes into one clean view — so you focus on what matters.\n\nStart your free trial today and get your first productive week, guaranteed.\n\n[Start Free Trial →]",
    principle:"Specificity + Role + Constraints = Precision. Defining the role, audience, tone, and length gives the model clear guardrails, while the over-engineered version drowns the actual goal in unnecessary complexity.",
    choices:[
      {label:"A", text:"Write an email about my app.", correct:false, why:"Too vague — no role, audience, tone, or constraints."},
      {label:"B", text:"Act as an expert email marketer. Write a launch email for 'FlowTask', a productivity app for busy professionals. Tone: energetic but professional. Include one clear call-to-action to start a free trial. Keep it under 150 words.", correct:true, why:"Clear role, audience, tone, CTA, and length constraint."},
      {label:"C", text:"As the greatest marketing legend in history, write an infinitely detailed 2000-word email covering every feature, pricing tier, and a haiku.", correct:false, why:"Over-engineered — excessive complexity obscures the goal and ignores brevity."}
    ]
  },
  {
    domain:"Software Engineering & Data",
    title:"Debugging Assistant",
    desiredOutput:"A helpful, structured explanation of why a Python function throws an IndexError, plus a fixed code snippet.",
    correctBlocks:[
      "Act as a senior Python developer reviewing code.",
      "Here is the function: [paste code]",
      "It throws an IndexError on line 5 when the list is empty.",
      "Explain the root cause, then provide a corrected version with comments.",
      "Keep the explanation under 100 words."
    ],
    distractorBlocks:[
      "Rewrite the entire codebase from scratch.",
      "Explain the history of the Python language.",
      "Just say 'it's broken' without details.",
      "Translate the code into 5 other languages."
    ],
    weakPrompt:"My code is broken, fix it.",
    optimizedPrompt:"Act as a senior Python developer reviewing code. Here is the function: [paste code]. It throws an IndexError on line 5 when the list is empty. Explain the root cause, then provide a corrected version with comments. Keep the explanation under 100 words.",
    overEngineeredPrompt:"As a legendary 10x FAANG principal engineer with 50 years of experience across every programming paradigm and language ever created, using formal verification methods, big-O analysis, historical context of exception handling since 1960, and a full academic paper structure with citations, debug my code while also refactoring it for microservices, adding Kubernetes deployment configs, and writing unit tests for 12 edge cases I didn't ask about.",
    weakOutput:"I don't know, maybe check your code? There could be many reasons.",
    optimizedOutput:"Root cause: the function accesses list[0] without checking if the list is empty, causing an IndexError.\n\nFix:\ndef get_first(items):\n    if not items:\n        return None\n    return items[0]\n\nThis checks for an empty list before indexing.",
    principle:"Context + Constraint = Diagnosability. Providing the exact error, code, and line number lets the model pinpoint the issue instead of guessing broadly.",
    choices:[
      {label:"A", text:"My code is broken, fix it.", correct:false, why:"No code, no error message, no context — impossible to diagnose."},
      {label:"B", text:"As a legendary 10x engineer, refactor everything, add Kubernetes configs, write 12 unit tests, and include a research paper on exception history.", correct:false, why:"Massive scope creep unrelated to the actual bug."},
      {label:"C", text:"Act as a senior Python developer. Here is the function, it throws an IndexError on line 5 for empty lists. Explain root cause and give a fixed version, under 100 words.", correct:true, why:"Precise context, clear ask, reasonable constraint."}
    ]
  },
  {
    domain:"Creative Writing & Content",
    title:"Short Fantasy Opening",
    desiredOutput:"An evocative 3-sentence opening for a fantasy short story about a reluctant dragon rider, in a moody tone.",
    correctBlocks:[
      "Act as a fantasy fiction author.",
      "Write a 3-sentence opening for a story about a reluctant dragon rider.",
      "Tone: moody, atmospheric.",
      "Avoid clichés like 'once upon a time'.",
      "Focus on sensory detail."
    ],
    distractorBlocks:[
      "Write a 10,000 word full novel.",
      "Make it a comedy sketch instead.",
      "Include a full character backstory bible.",
      "Use only one-word sentences."
    ],
    weakPrompt:"Write a story about a dragon.",
    optimizedPrompt:"Act as a fantasy fiction author. Write a 3-sentence opening for a story about a reluctant dragon rider. Tone: moody, atmospheric. Avoid clichés like 'once upon a time'. Focus on sensory detail.",
    overEngineeredPrompt:"As the reincarnation of Tolkien merged with a Booker Prize committee, using a 15-act narrative structure, Jungian archetypes, alliterative Old English meter, and a full magic system codex spanning 200 years of lore, write an opening while also including a map description, a prophecy in verse, and footnotes.",
    weakOutput:"There once was a dragon and a rider. They went on an adventure. The end.",
    optimizedOutput:"The saddle still smelled of the last rider's blood. Kael pressed his palm to the dragon's scarred hide, feeling the low growl of a creature that trusted no one — least of all him. Somewhere above the clouds, the sky was waiting to judge them both.",
    principle:"Sensory + Tonal Direction = Voice. Specifying tone and stylistic constraints (avoid clichés, sensory focus) shapes distinctive prose instead of generic filler.",
    choices:[
      {label:"A", text:"Write a story about a dragon.", correct:false, why:"No tone, length, or style guidance — output will be generic."},
      {label:"B", text:"Act as a fantasy author. Write a 3-sentence moody opening about a reluctant dragon rider, avoiding clichés, with sensory detail.", correct:true, why:"Clear length, tone, and stylistic constraints."},
      {label:"C", text:"As Tolkien reincarnated, write a 15-act epic with a full magic codex, prophecy in verse, and footnotes.", correct:false, why:"Wildly over-scoped for a 3-sentence opening request."}
    ]
  },
  {
    domain:"Education & Research",
    title:"Explain a Concept Simply",
    desiredOutput:"A simple, accurate explanation of photosynthesis for a 10-year-old, using an analogy.",
    correctBlocks:[
      "Act as a friendly science teacher.",
      "Explain photosynthesis to a 10-year-old.",
      "Use a simple real-world analogy.",
      "Keep it to 3-4 sentences.",
      "Avoid technical jargon."
    ],
    distractorBlocks:[
      "Include the full biochemical equations with citations.",
      "Write it as a PhD thesis abstract.",
      "Make it 5000 words long.",
      "Use only Latin terminology."
    ],
    weakPrompt:"Explain photosynthesis.",
    optimizedPrompt:"Act as a friendly science teacher. Explain photosynthesis to a 10-year-old. Use a simple real-world analogy. Keep it to 3-4 sentences. Avoid technical jargon.",
    overEngineeredPrompt:"As a Nobel Prize-winning biochemist writing for a peer-reviewed journal, explain photosynthesis using full Calvin cycle equations, electron transport chain diagrams described in text, historical citations back to 1779, and a comparative analysis with C4 vs CAM plants, then simplify it for a child at the end.",
    weakOutput:"Photosynthesis is when plants use light for energy through complex biochemical reactions involving chlorophyll and ATP synthase.",
    optimizedOutput:"Plants are like little chefs who use sunlight as their stove! They take in water from their roots and air through their leaves, then 'cook' it into food using sunlight. As a bonus, they release oxygen for us to breathe — like a kitchen releasing yummy smells!",
    principle:"Audience Calibration = Clarity. Naming the audience (age 10) and requesting an analogy forces the model to simplify rather than default to technical language.",
    choices:[
      {label:"A", text:"Explain photosynthesis.", correct:false, why:"No audience specified — likely too technical or too vague."},
      {label:"B", text:"As a Nobel biochemist, explain with full Calvin cycle equations and C4 vs CAM analysis, then simplify for a child.", correct:false, why:"Backwards approach — overly technical first, contradicts the goal."},
      {label:"C", text:"Act as a friendly science teacher. Explain photosynthesis to a 10-year-old using a simple analogy, in 3-4 sentences, no jargon.", correct:true, why:"Audience, format, and tone are all clearly defined."}
    ]
  },
  {
    domain:"Gaming & Entertainment",
    title:"Boss Fight Design",
    desiredOutput:"A creative design brief for a video game boss fight, including mechanics and phase structure.",
    correctBlocks:[
      "Act as a senior game designer.",
      "Design a 3-phase boss fight for a fantasy action RPG.",
      "Each phase should introduce a new mechanic.",
      "Keep the total description under 200 words.",
      "Include the boss's name and visual theme."
    ],
    distractorBlocks:[
      "Write the full game's source code in C++.",
      "Design an entire 40-hour campaign.",
      "Make it a mobile idle clicker instead.",
      "Include real-world weapon manufacturing specs."
    ],
    weakPrompt:"Make a boss fight.",
    optimizedPrompt:"Act as a senior game designer. Design a 3-phase boss fight for a fantasy action RPG. Each phase should introduce a new mechanic. Keep the total description under 200 words. Include the boss's name and visual theme.",
    overEngineeredPrompt:"As the lead director of every AAA studio combined, using a 12-phase escalation model, full combat math with DPS curves, a 50-page lore codex, orchestral score notes, marketing copy, merchandise ideas, and a Reddit AMA script, design a boss fight while also writing the C++ implementation and a balance patch roadmap for the next 3 years.",
    weakOutput:"There's a big boss. It has a lot of health. You fight it and win.",
    optimizedOutput:"Boss: Ashen Warden, a molten stone titan.\nPhase 1: Slow melee slams — teaches players to dodge telegraphed attacks.\nPhase 2: Summons fire rifts, forcing positioning awareness.\nPhase 3: Enrages, attacks speed up 40%, and players must interrupt a charge attack to prevent a wipe.\nVisual theme: cracked obsidian skin glowing with lava veins.",
    principle:"Structured Scope = Usable Design. Defining phase count, mechanic focus, and word limit produces an actionable brief instead of vague or bloated output.",
    choices:[
      {label:"A", text:"Make a boss fight.", correct:false, why:"No structure, scope, or genre — output will be shallow."},
      {label:"B", text:"Act as a senior game designer. Design a 3-phase boss fight for a fantasy RPG, each phase introducing a new mechanic, under 200 words, with name and visual theme.", correct:true, why:"Clear scope, structure, and constraints for a usable brief."},
      {label:"C", text:"As the lead of every AAA studio, design a 12-phase boss with full DPS math, a 50-page lore codex, and a 3-year balance roadmap.", correct:false, why:"Absurdly over-scoped for a single boss fight brief."}
    ]
  },
  {
    domain:"Business & Marketing",
    title:"Social Media Caption",
    desiredOutput:"An engaging Instagram caption for a coffee shop's new seasonal latte, with hashtags.",
    correctBlocks:[
      "Act as a social media copywriter.",
      "Write an Instagram caption for a new Pumpkin Spice Latte at a local coffee shop.",
      "Tone: warm, playful, cozy.",
      "Include 3-5 relevant hashtags.",
      "Keep it under 40 words."
    ],
    distractorBlocks:[
      "Write a 10-paragraph essay on coffee history.",
      "Make it sound like a legal contract.",
      "Include the full nutritional facts panel.",
      "Use only French language."
    ],
    weakPrompt:"Write a caption for our latte.",
    optimizedPrompt:"Act as a social media copywriter. Write an Instagram caption for a new Pumpkin Spice Latte at a local coffee shop. Tone: warm, playful, cozy. Include 3-5 relevant hashtags. Keep it under 40 words.",
    overEngineeredPrompt:"As the world's top viral growth-hacking social media guru with 100M followers, using the AIDA framework, 7 psychological triggers, A/B test variants for 5 platforms, an influencer outreach plan, and a full quarterly content calendar, write one Instagram caption about a latte while also designing the packaging and a jingle.",
    weakOutput:"New latte! Buy it now!",
    optimizedOutput:"Cozy season just got cozier ☕🍂 Our new Pumpkin Spice Latte is here — warm spices, creamy foam, big vibes. Come wrap your hands around one today.\n#PumpkinSpice #CoffeeLove #FallVibes #CozyCafe",
    principle:"Platform + Tone + Length = Fit-for-Purpose. Specifying the platform and word limit ensures the output matches real-world usage constraints.",
    choices:[
      {label:"A", text:"Write a caption for our latte.", correct:false, why:"No platform, tone, or length — generic and possibly mismatched to Instagram norms."},
      {label:"B", text:"Act as a social copywriter. Write a warm, playful Instagram caption for a new Pumpkin Spice Latte, under 40 words, with 3-5 hashtags.", correct:true, why:"Platform-appropriate, toned, and length-constrained."},
      {label:"C", text:"As a viral guru with 100M followers, write one caption while also designing packaging, a jingle, and a quarterly content calendar.", correct:false, why:"Massively over-scoped beyond the actual ask."}
    ]
  },
  {
    domain:"Software Engineering & Data",
    title:"SQL Query Generation",
    desiredOutput:"A correct SQL query that returns the top 5 customers by total spend, with clear column aliases.",
    correctBlocks:[
      "Act as a SQL expert.",
      "Tables: customers(id, name), orders(id, customer_id, amount).",
      "Write a query to find the top 5 customers by total spend.",
      "Use clear column aliases like total_spent.",
      "Return only the SQL, no explanation."
    ],
    distractorBlocks:[
      "Explain the full history of relational databases.",
      "Write the query in 5 different SQL dialects.",
      "Design a full data warehouse architecture.",
      "Include unrelated NoSQL comparisons."
    ],
    weakPrompt:"Write a SQL query for top customers.",
    optimizedPrompt:"Act as a SQL expert. Tables: customers(id, name), orders(id, customer_id, amount). Write a query to find the top 5 customers by total spend. Use clear column aliases like total_spent. Return only the SQL, no explanation.",
    overEngineeredPrompt:"As a principal database architect with 30 years at every FAANG company, using formal relational algebra notation, query optimization theory, index strategy analysis, and a comparison across PostgreSQL, MySQL, Oracle, SQL Server, and SQLite, write the query while also designing a full star-schema warehouse and a disaster recovery plan.",
    weakOutput:"SELECT * FROM customers ORDER BY spend DESC LIMIT 5; -- (spend column doesn't exist, this is wrong)",
    optimizedOutput:"SELECT c.name, SUM(o.amount) AS total_spent\nFROM customers c\nJOIN orders o ON c.id = o.customer_id\nGROUP BY c.name\nORDER BY total_spent DESC\nLIMIT 5;",
    principle:"Schema Context = Correctness. Providing the exact table/column names prevents hallucinated fields and guarantees a runnable query.",
    choices:[
      {label:"A", text:"Write a SQL query for top customers.", correct:false, why:"No schema provided — high risk of hallucinated column names."},
      {label:"B", text:"Act as a SQL expert. Given tables customers(id, name) and orders(id, customer_id, amount), write a query for top 5 customers by spend with clear aliases, SQL only.", correct:true, why:"Schema, goal, and output format all specified."},
      {label:"C", text:"As a principal architect, compare 5 SQL dialects and design a full data warehouse plus disaster recovery strategy.", correct:false, why:"Wildly out of scope for a single query request."}
    ]
  },
  {
    domain:"Education & Research",
    title:"Literature Review Summary",
    desiredOutput:"A concise, neutral summary of three research paper abstracts, highlighting common themes.",
    correctBlocks:[
      "Act as a research assistant.",
      "Here are 3 abstracts: [paste abstracts]",
      "Summarize the common themes across them in a neutral, academic tone.",
      "Keep the summary to 150 words.",
      "Do not include personal opinions."
    ],
    distractorBlocks:[
      "Write a 20-page dissertation.",
      "Add dramatic, biased commentary.",
      "Translate the abstracts into 10 languages.",
      "Invent additional fake studies to cite."
    ],
    weakPrompt:"Summarize these papers.",
    optimizedPrompt:"Act as a research assistant. Here are 3 abstracts: [paste abstracts]. Summarize the common themes across them in a neutral, academic tone. Keep the summary to 150 words. Do not include personal opinions.",
    overEngineeredPrompt:"As a tenured professor emeritus who has published 500 papers and sits on 12 editorial boards, using full APA 7th edition formatting, a meta-analysis with statistical significance testing, a systematic review methodology (PRISMA), and citations to 40 additional papers not provided, summarize these 3 abstracts while also proposing a new 5-year research agenda.",
    weakOutput:"The papers are about science stuff and they all say similar things I think.",
    optimizedOutput:"All three studies converge on the finding that early intervention improves long-term outcomes, though they differ in methodology — two use longitudinal designs while one relies on cross-sectional data. A shared limitation across all three is small sample size, suggesting a need for larger replication studies before broad conclusions can be drawn.",
    principle:"Bounded Synthesis = Trustworthy Summary. Explicitly limiting scope (given abstracts only, no invented sources) prevents fabrication and keeps the summary grounded.",
    choices:[
      {label:"A", text:"Summarize these papers.", correct:false, why:"No tone, length, or scope constraint — risks vague or biased output."},
      {label:"B", text:"Act as a research assistant. Summarize common themes across the 3 given abstracts in neutral academic tone, 150 words, no personal opinions.", correct:true, why:"Clear scope, tone, and length with no room for fabrication."},
      {label:"C", text:"As a professor emeritus, run a full PRISMA meta-analysis citing 40 additional papers not provided, plus a 5-year research agenda.", correct:false, why:"Invents unavailable sources and vastly exceeds the requested scope."}
    ]
  }
];

// ---------- UTILITIES ----------
function shuffle(arr){
  const a=[...arr];
  for(let i=a.length-1;i>0;i--){
    const j=Math.floor(Math.random()*(i+1));
    [a[i],a[j]]=[a[j],a[i]];
  }
  return a;
}
function pick(arr,n){ return shuffle(arr).slice(0,n); }
function el(tag,attrs={},...children){
  const e=document.createElement(tag);
  for(const k in attrs){
    if(k==='class') e.className=attrs[k];
    else if(k==='html') e.innerHTML=attrs[k];
    else if(k.startsWith('on')) e.addEventListener(k.slice(2),attrs[k]);
    else e.setAttribute(k,attrs[k]);
  }
  children.flat().forEach(c=>{
    if(c===null||c===undefined) return;
    if(typeof c==='string') e.appendChild(document.createTextNode(c));
    else e.appendChild(c);
  });
  return e;
}
function toast(msg, type='good'){
  const wrap=document.getElementById('toastWrap');
  const t=el('div',{class:'toast '+type}, msg);
  wrap.appendChild(t);
  setTimeout(()=>t.remove(),2800);
}
function scorePop(x,y,text){
  const p=el('div',{class:'score-pop', style:`left:${x}px; top:${y}px;`}, text);
  document.body.appendChild(p);
  setTimeout(()=>p.remove(),1000);
}

// ---------- SETUP SCREEN (already gathered via chat, but keep in-app confirmation) ----------
function initGame(domain, difficulty){
  STATE.domain = domain;
  STATE.difficulty = difficulty;
  let pool = domain==='All Domains'
    ? SCENARIO_BANK
    : SCENARIO_BANK.filter(s=>s.domain===domain);
  if(pool.length < 6) pool = SCENARIO_BANK; // fallback ensure enough
  let chosen = pick(pool, Math.min(7, pool.length));
  // assign challenge types round robin across 3 types
  const types=['build','clean','choose'];
  chosen = chosen.map((s,i)=>({...s, challengeType: types[i%3], id:i}));
  STATE.scenarios = chosen;
  STATE.currentIndex = 0;
  STATE.score = 0;
  STATE.moves = 0;
  STATE.wrongPlacements = 0;
  STATE.hintsUsed = 0;
  STATE.correctPlacements = 0;
  STATE.scenarioResults = [];
  STATE.startTime = Date.now();
  renderScenario();
}

// ---------- RENDER: ROOT ----------
function renderRoot(){
  const app=document.getElementById('app');
  app.innerHTML='';
  app.appendChild(el('h1',{}, '🧩 Prompt Puzzle'));
  app.appendChild(el('div',{class:'subtitle'}, 'Master AI Prompting Through Play'));
  renderWelcome();
}

function renderWelcome(){
  const app=document.getElementById('app');
  const card = el('card' in {} ? 'div':'div',{class:'card fade-in'});
  card.appendChild(el('h2',{}, 'Ready to sharpen your prompting skills?'));
  card.appendChild(el('p',{class:'small-muted', style:'margin:8px 0 16px;'},
    `Domain: ${STATE.domain} · Difficulty: ${STATE.difficulty}`));
  card.appendChild(el('p',{}, 'You will face 3 challenge types across several scenarios: Build the Prompt, Clean the Prompt, and Choose the Best Prompt. Score points for accuracy, speed, and clean optimization — avoid unnecessary hints and wrong moves!'));
  const startBtn = el('button',{class:'btn', style:'margin-top:18px;', onclick:()=>{
    initGame(STATE.domain, STATE.difficulty);
  }}, '🚀 Start Challenge');
  card.appendChild(el('div',{class:'center'}, startBtn));
  app.appendChild(card);
}

// ---------- PROGRESS NAV ----------
function renderProgressNav(){
  const nav=el('div',{class:'scenario-nav'});
  STATE.scenarios.forEach((s,i)=>{
    let cls='dot';
    if(i<STATE.currentIndex) cls+=' done';
    else if(i===STATE.currentIndex) cls+=' current';
    nav.appendChild(el('div',{class:cls, title:s.title}));
  });
  return nav;
}

function renderStatsBar(){
  const elapsed = Math.floor((Date.now()-STATE.startTime)/1000);
  const mm = String(Math.floor(elapsed/60)).padStart(2,'0');
  const ss = String(elapsed%60).padStart(2,'0');
  const row = el('div',{class:'stat-row'},
    el('div',{class:'stat-pill'}, '⭐ Score: ', el('b',{},String(STATE.score))),
    el('div',{class:'stat-pill'}, '⏱ Time: ', el('b',{},`${mm}:${ss}`)),
    el('div',{class:'stat-pill'}, '🎯 Moves: ', el('b',{},String(STATE.moves))),
    el('div',{class:'stat-pill'}, '❌ Wrong: ', el('b',{},String(STATE.wrongPlacements))),
    el('div',{class:'stat-pill'}, '💡 Hints: ', el('b',{},String(STATE.hintsUsed))),
  );
  return row;
}

// ---------- MAIN SCENARIO RENDER ----------
function renderScenario(){
  if(STATE.currentIndex >= STATE.scenarios.length){
    renderReport();
    return;
  }
  const app=document.getElementById('app');
  app.innerHTML='';
  app.appendChild(el('h1',{}, '🧩 Prompt Puzzle'));
  app.appendChild(el('div',{class:'subtitle'}, 'Master AI Prompting Through Play'));

  const progWrap = el('div',{class:'card fade-in'});
  const pct = Math.round((STATE.currentIndex/STATE.scenarios.length)*100);
  progWrap.appendChild(el('div',{class:'progress-bar'}, el('div',{class:'progress-fill', style:`width:${pct}%;`})));
  progWrap.appendChild(renderProgressNav());
  progWrap.appendChild(renderStatsBar());
  app.appendChild(progWrap);

  const s = STATE.scenarios[STATE.currentIndex];
  const typeLabel = {build:'🔧 Build the Prompt', clean:'🧹 Clean the Prompt', choose:'✅ Choose the Best Prompt'}[s.challengeType];

  const card = el('div',{class:'card fade-in'});
  card.appendChild(el('div',{class:'flex-between'},
    el('h2',{}, s.title),
    el('span',{class:'badge'}, typeLabel)
  ));
  card.appendChild(el('p',{class:'small-muted', style:'margin-top:6px;'}, s.domain));
  card.appendChild(el('div',{class:'principle-box'},
    el('b',{}, '🎯 Desired Output: '), s.desiredOutput
  ));

  const hintBtn = el('button',{class:'btn secondary', style:'margin-top:14px;', onclick:()=>{
    STATE.hintsUsed++;
    toast('💡 Hint used! -5 potential points', 'bad');
    showHint(s, card);
  }}, '💡 Use Hint (-5 pts)');
  card.appendChild(hintBtn);

  const body = el('div',{style:'margin-top:18px;'});
  card.appendChild(body);
  app.appendChild(card);

  if(s.challengeType==='build') renderBuildChallenge(s, body);
  else if(s.challengeType==='clean') renderCleanChallenge(s, body);
  else renderChooseChallenge(s, body);

  // live timer refresh
  clearInterval(window.__timerInt);
  window.__timerInt = setInterval(()=>{
    const statPill = document.querySelectorAll('.stat-pill b')[1];
    if(!statPill) { clearInterval(window.__timerInt); return; }
    const elapsed = Math.floor((Date.now()-STATE.startTime)/1000);
    const mm = String(Math.floor(elapsed/60)).padStart(2,'0');
    const ss = String(elapsed%60).padStart(2,'0');
    statPill.textContent = `${mm}:${ss}`;
  },1000);
}

function showHint(s, card){
  const existing = card.querySelector('.hint-box');
  if(existing) existing.remove();
  card.appendChild(el('div',{class:'hint-box'}, '💡 ' + s.principle));
}

// ---------- CHALLENGE 1: BUILD THE PROMPT (drag correct blocks into order) ----------
function renderBuildChallenge(s, container){
  const allBlocks = shuffle([...s.correctBlocks, ...pick(s.distractorBlocks, Math.min(3, s.distractorBlocks.length))]);
  let placed = [];

  const grid = el('div',{class:'grid2'});
  const sourceCol = el('div',{},
    el('div',{class:'col-title'}, 'Available Blocks (drag to build order →)'),
  );
  const sourceZone = el('div',{class:'dropzone', id:'sourceZone'});
  sourceCol.appendChild(sourceZone);

  const targetCol = el('div',{},
    el('div',{class:'col-title'}, 'Your Prompt (in order)'),
  );
  const targetZone = el('div',{class:'dropzone', id:'targetZone'});
  targetZone.appendChild(el('div',{class:'placeholder'}, 'Drop blocks here in the right order'));
  targetCol.appendChild(targetZone);

  function makeBlockEl(text, origin){
    const b = el('div',{class:'block', draggable:'true'}, text);
    b.dataset.text = text;
    b.addEventListener('dragstart', e=>{
      b.classList.add('dragging');
      e.dataTransfer.setData('text/plain', text);
    });
    b.addEventListener('dragend', ()=> b.classList.remove('dragging'));
    b.addEventListener('click', ()=>{
      // tap-to-move fallback for touch devices
      if(origin==='source'){ moveToTarget(text, b); }
      else { moveToSource(text, b); }
    });
    return b;
  }

  allBlocks.forEach(t=> sourceZone.appendChild(makeBlockEl(t,'source')));

  function refreshPlaceholder(){
    if(targetZone.children.length===0 || (targetZone.children.length===1 && targetZone.querySelector('.placeholder'))){
      // keep
    }
    const ph = targetZone.querySelector('.placeholder');
    if(placed.length>0 && ph) ph.remove();
    if(placed.length===0 && !targetZone.querySelector('.placeholder')){
      targetZone.appendChild(el('div',{class:'placeholder'}, 'Drop blocks here in the right order'));
    }
  }

  function moveToTarget(text, blockEl){
    blockEl.remove();
    placed.push(text);
    STATE.moves++;
    const isCorrectStep = s.correctBlocks[placed.length-1] === text;
    const nb = makeBlockEl(text,'target');
    nb.classList.add('placed');
    nb.draggable = true;
    if(isCorrectStep){
      nb.classList.add('correct-flash');
      STATE.correctPlacements++;
      STATE.score += 10;
    } else {
      nb.classList.add('wrong-flash');
      STATE.wrongPlacements++;
      STATE.score = Math.max(0, STATE.score - 3);
    }
    refreshPlaceholder();
    targetZone.appendChild(nb);
    updateStatsUI();
    checkBuildComplete();
  }
  function moveToSource(text, blockEl){
    blockEl.remove();
    placed = placed.filter(t=>t!==text);
    const nb = makeBlockEl(text,'source');
    sourceZone.appendChild(nb);
    refreshPlaceholder();
    updateStatsUI();
  }

  [sourceZone, targetZone].forEach(zone=>{
    zone.addEventListener('dragover', e=>{ e.preventDefault(); zone.classList.add('dragover'); });
    zone.addEventListener('dragleave', ()=> zone.classList.remove('dragover'));
    zone.addEventListener('drop', e=>{
      e.preventDefault();
      zone.classList.remove('dragover');
      const text = e.dataTransfer.getData('text/plain');
      const draggingEl = document.querySelector('.block.dragging');
      if(!draggingEl) return;
      if(zone===targetZone && draggingEl.parentElement===sourceZone){
        moveToTarget(text, draggingEl);
      } else if(zone===sourceZone && draggingEl.parentElement===targetZone){
        moveToSource(text, draggingEl);
      }
    });
  });

  grid.appendChild(sourceCol);
  grid.appendChild(targetCol);
  container.appendChild(grid);

  const submitBtn = el('button',{class:'btn', style:'margin-top:16px;', onclick:()=>{
    finalizeBuildChallenge(s, placed);
  }}, '✅ Submit Prompt Order');
  container.appendChild(submitBtn);

  function checkBuildComplete(){
    if(placed.length === s.correctBlocks.length + 0 && placed.length >= s.correctBlocks.length){
      // allow manual submit anyway
    }
  }
}

function finalizeBuildChallenge(s, placed){
  const correctCount = placed.filter((t,i)=> s.correctBlocks[i]===t).length;
  const accuracy = Math.round((correctCount / s.correctBlocks.length) * 100);
  const optBonus = accuracy===100 ? 20 : 0;
  STATE.optimizationBonus += optBonus;
  STATE.score += optBonus;
  STATE.scenarioResults.push({title:s.title, type:'Build the Prompt', accuracy, hints:0, optBonus});
  toast(accuracy===100 ? '🎉 Perfect prompt order! +20 bonus' : `Prompt built — ${accuracy}% accurate`, accuracy===100?'good':'bad');
  showRevealAndNext(s, accuracy);
}

// ---------- CHALLENGE 2: CLEAN THE PROMPT (remove distractors from over-engineered) ----------
function renderCleanChallenge(s, container){
  container.appendChild(el('p',{class:'small-muted'}, 'This prompt is over-engineered. Click each block to KEEP or REMOVE it — build the clean, optimized version.'));

  const messyParts = shuffle([...s.correctBlocks, ...pick(s.distractorBlocks, Math.min(4, s.distractorBlocks.length))]);
  let decisions = {}; // text -> 'keep'|'remove'|null

  const listWrap = el('div',{style:'margin-top:14px;'});
  messyParts.forEach(text=>{
    const row = el('div',{class:'block', style:'display:flex; justify-content:space-between; align-items:center; gap:10px;'},
      el('span',{style:'flex:1;'}, text)
    );
    const btnWrap = el('div',{style:'display:flex; gap:6px;'});
    const keepBtn = el('button',{class:'btn secondary', style:'padding:6px 12px; font-size:.75rem;', onclick:(e)=>{
      e.stopPropagation();
      decisions[text]='keep';
      STATE.moves++;
      const isCorrect = s.correctBlocks.includes(text);
      row.style.borderColor = isCorrect ? 'var(--good)' : 'var(--bad)';
      if(isCorrect){ STATE.score+=8; STATE.correctPlacements++; } else { STATE.score=Math.max(0,STATE.score-5); STATE.wrongPlacements++; }
      updateStatsUI();
    }}, '✅ Keep');
    const removeBtn = el('button',{class:'btn secondary', style:'padding:6px 12px; font-size:.75rem;', onclick:(e)=>{
      e.stopPropagation();
      decisions[text]='remove';
      STATE.moves++;
      const isDistractor = s.distractorBlocks.includes(text);
      row.style.borderColor = isDistractor ? 'var(--good)' : 'var(--bad)';
      row.style.opacity = '0.5';
      if(isDistractor){ STATE.score+=8; STATE.correctPlacements++; } else { STATE.score=Math.max(0,STATE.score-5); STATE.wrongPlacements++; }
      updateStatsUI();
    }}, '🗑 Remove');
    btnWrap.appendChild(keepBtn);
    btnWrap.appendChild(removeBtn);
    row.appendChild(btnWrap);
    listWrap.appendChild(row);
  });
  container.appendChild(listWrap);

  const submitBtn = el('button',{class:'btn', style:'margin-top:16px;', onclick:()=>{
    finalizeCleanChallenge(s, decisions, messyParts);
  }}, '✅ Finalize Clean Prompt');
  container.appendChild(submitBtn);
}

function finalizeCleanChallenge(s, decisions, messyParts){
  let correct=0;
  messyParts.forEach(text=>{
    const shouldKeep = s.correctBlocks.includes(text);
    const decision = decisions[text];
    if((shouldKeep && decision==='keep') || (!shouldKeep && decision==='remove')) correct++;
  });
  const accuracy = Math.round((correct/messyParts.length)*100);
  const optBonus = accuracy===100 ? 20 : 0;
  STATE.optimizationBonus += optBonus;
  STATE.score += optBonus;
  STATE.scenarioResults.push({title:s.title, type:'Clean the Prompt', accuracy, hints:0, optBonus});
  toast(accuracy===100 ? '🎉 Perfectly cleaned prompt! +20 bonus' : `Cleaned — ${accuracy}% accurate`, accuracy===100?'good':'bad');
  showRevealAndNext(s, accuracy);
}

// ---------- CHALLENGE 3: CHOOSE THE BEST PROMPT ----------
function renderChooseChallenge(s, container){
  container.appendChild(el('p',{class:'small-muted'}, 'Which prompt best achieves the desired output? Choose wisely.'));
  const optWrap = el('div',{style:'margin-top:14px;'});
  const options = shuffle(s.choices);
  let answered=false;
  options.forEach(opt=>{
    const card = el('div',{class:'choice-option'},
      el('span',{class:'choice-label'}, opt.label+'.'),
      el('span',{}, opt.text)
    );
    card.addEventListener('click', ()=>{
      if(answered) return;
      answered=true;
      STATE.moves++;
      const allCards = optWrap.querySelectorAll('.choice-option');
      allCards.forEach(c=> c.style.pointerEvents='none');
      if(opt.correct){
        card.classList.add('selected-correct');
        STATE.score += 25;
        STATE.correctPlacements++;
        toast('🎉 Correct choice! +25 pts', 'good');
      } else {
        card.classList.add('selected-wrong');
        STATE.wrongPlacements++;
        STATE.score = Math.max(0, STATE.score-10);
        toast('❌ Not the best choice. -10 pts', 'bad');
        // reveal correct
        const correctCard = [...allCards].find((c,i)=> options[i].correct);
        if(correctCard) correctCard.classList.add('selected-correct');
      }
      card.appendChild(el('div',{class:'small-muted', style:'margin-top:6px;'}, opt.why));
      updateStatsUI();
      const accuracy = opt.correct ? 100 : 0;
      const optBonus = opt.correct ? 20 : 0;
      STATE.optimizationBonus += optBonus;
      STATE.score += optBonus;
      STATE.scenarioResults.push({title:s.title, type:'Choose the Best Prompt', accuracy, hints:0, optBonus});
      setTimeout(()=> showRevealAndNext(s, accuracy), 900);
    });
    optWrap.appendChild(card);
  });
  container.appendChild(optWrap);
}

// ---------- REVEAL PANEL (weak vs optimized vs over-engineered) ----------
function showRevealAndNext(s, accuracy){
  const app=document.getElementById('app');
  const reveal = el('div',{class:'card fade-in', style:'margin-top:16px;'});
  reveal.appendChild(el('h3',{}, '📊 Prompt Comparison'));
  reveal.appendChild(el('div',{class:'grid2', style:'margin-top:12px;'},
    el('div',{},
      el('div',{class:'badge bad'}, 'Weak Prompt'),
      el('pre',{class:'prompt-text'}, s.weakPrompt),
      el('div',{class:'small-muted', style:'margin-top:4px;'}, '↳ Output:'),
      el('pre',{class:'prompt-text'}, s.weakOutput)
    ),
    el('div',{},
      el('div',{class:'badge good'}, 'Optimized Prompt'),
      el('pre',{class:'prompt-text'}, s.optimizedPrompt),
      el('div',{class:'small-muted', style:'margin-top:4px;'}, '↳ Output:'),
      el('pre',{class:'prompt-text'}, s.optimizedOutput)
    )
  ));
  reveal.appendChild(el('div',{class:'badge gold', style:'margin-top:14px;'}, 'Over-Engineered Prompt (avoid this!)'));
  reveal.appendChild(el('pre',{class:'prompt-text'}, s.overEngineeredPrompt));
  reveal.appendChild(el('div',{class:'principle-box'}, el('b',{},'🧠 Principle: '), s.principle));

  const nextBtn = el('button',{class:'btn', style:'margin-top:16px;', onclick:()=>{
    STATE.currentIndex++;
    reveal.remove();
    renderScenario();
  }}, STATE.currentIndex < STATE.scenarios.length-1 ? '➡️ Next Scenario' : '🏁 View Final Report');
  reveal.appendChild(el('div',{class:'center', style:'margin-top:10px;'}, nextBtn));
  app.appendChild(reveal);
  reveal.scrollIntoView({behavior:'smooth', block:'start'});
}

function updateStatsUI(){
  const pills = document.querySelectorAll('.stat-pill b');
  if(pills.length>=5){
    pills[0].textContent = STATE.score;
    pills[2].textContent = STATE.moves;
    pills[3].textContent = STATE.wrongPlacements;
    pills[4].textContent = STATE.hintsUsed;
  }
}

// ---------- FINAL REPORT ----------
function computeRank(finalScore, maxScore){
  const pct = finalScore/maxScore*100;
  if(pct>=90) return {rank:'🏆 Prompt Grandmaster', rating:'Legendary'};
  if(pct>=75) return {rank:'🥇 Prompt Architect', rating:'Excellent'};
  if(pct>=55) return {rank:'🥈 Prompt Strategist', rating:'Good'};
  if(pct>=35) return {rank:'🥉 Prompt Apprentice', rating:'Developing'};
  return {rank:'🌱 Prompt Novice', rating:'Just Starting'};
}

function renderReport(){
  clearInterval(window.__timerInt);
  const app=document.getElementById('app');
  app.innerHTML='';
  app.appendChild(el('h1',{}, '🧩 Prompt Puzzle'));
  app.appendChild(el('div',{class:'subtitle'}, 'Prompt Performance Report'));

  const totalScenarios = STATE.scenarios.length;
  const avgAccuracy = Math.round(STATE.scenarioResults.reduce((a,r)=>a+r.accuracy,0)/totalScenarios);
  const elapsedSec = Math.floor((Date.now()-STATE.startTime)/1000);
  const maxPossible = totalScenarios * (10*5 + 20 + 25) ; // rough ceiling estimate
  const finalScore = Math.max(0, STATE.score);
  const {rank, rating} = computeRank(finalScore, Math.max(maxPossible,100));

  const card = el('div',{class:'card fade-in'});
  card.appendChild(el('div',{class:'rank-big'}, rank));
  card.appendChild(el('div',{class:'center'}, el('span',{class:'badge gold'}, rating + ' Rating')));

  const grid = el('div',{class:'report-grid'});
  grid.appendChild(el('div',{class:'report-stat'}, el('div',{class:'val'}, String(finalScore)), el('div',{class:'lbl'},'Prompt Score')));
  grid.appendChild(el('div',{class:'report-stat'}, el('div',{class:'val'}, avgAccuracy+'%'), el('div',{class:'lbl'},'Accuracy')));
  grid.appendChild(el('div',{class:'report-stat'}, el('div',{class:'val'}, `${Math.floor(elapsedSec/60)}:${String(elapsedSec%60).padStart(2,'0')}`), el('div',{class:'lbl'},'Time')));
  grid.appendChild(el('div',{class:'report-stat'}, el('div',{class:'val'}, String(STATE.moves)), el('div',{class:'lbl'},'Moves')));
  grid.appendChild(el('div',{class:'report-stat'}, el('div',{class:'val'}, String(STATE.wrongPlacements)), el('div',{class:'lbl'},'Wrong Placements')));
  grid.appendChild(el('div',{class:'report-stat'}, el('div',{class:'val'}, String(STATE.hintsUsed)), el('div',{class:'lbl'},'Hints Used')));
  grid.appendChild(el('div',{class:'report-stat'}, el('div',{class:'val'}, '+'+STATE.optimizationBonus), el('div',{class:'lbl'},'Optimization Bonus')));
  card.appendChild(grid);

  // Prompt DNA visualization: proportions of specificity/structure/clarity derived from accuracy & hints
  const specificity = Math.max(10, Math.min(100, avgAccuracy));
  const structure = Math.max(10, Math.min(100, 100 - STATE.wrongPlacements*8));
  const clarity = Math.max(10, Math.min(100, 100 - STATE.hintsUsed*10));
  const total = specificity+structure+clarity;
  card.appendChild(el('div',{class:'col-title', style:'margin-top:18px;'}, '🧬 Prompt DNA'));
  const dna = el('div',{class:'dna-bar'});
  dna.appendChild(el('div',{class:'dna-seg', style:`width:${specificity/total*100}%; background:var(--accent);`}));
  dna.appendChild(el('div',{class:'dna-seg', style:`width:${structure/total*100}%; background:var(--accent2);`}));
  dna.appendChild(el('div',{class:'dna-seg', style:`width:${clarity/total*100}%; background:var(--gold);`}));
  card.appendChild(dna);
  card.appendChild(el('div',{class:'stat-row'},
    el('div',{class:'stat-pill'}, '🟣 Specificity: ', el('b',{},specificity+'%')),
    el('div',{class:'stat-pill'}, '🔵 Structure: ', el('b',{},structure+'%')),
    el('div',{class:'stat-pill'}, '🟡 Clarity: ', el('b',{},clarity+'%')),
  ));

  // Personalized feedback
  let feedback = '';
  if(avgAccuracy>=90) feedback = "Outstanding work! You consistently identify the exact structure a great prompt needs — role, context, constraints, and format — without over- or under-specifying.";
  else if(avgAccuracy>=65) feedback = "Solid performance! You understand the core building blocks of strong prompts. Focus next on cutting unnecessary complexity and being more precise with constraints.";
  else feedback = "You're building your foundation. Revisit the principle boxes for each scenario — pay close attention to role definition, audience, and length constraints, which are the biggest levers for prompt quality.";
  card.appendChild(el('div',{class:'principle-box', style:'margin-top:16px;'}, el('b',{},'📝 Feedback: '), feedback));

  // Next milestone
  const nextMilestoneMap = [
    {min:0,text:'Reach 35% overall to unlock Prompt Apprentice rank!'},
    {min:35,text:'Reach 55% overall to unlock Prompt Strategist rank!'},
    {min:55,text:'Reach 75% overall to unlock Prompt Architect rank!'},
    {min:75,text:'Reach 90% overall to unlock Prompt Grandmaster rank!'},
    {min:90,text:'You have reached the top rank — try Advanced difficulty next for a new challenge!'},
  ];
  const pctScore = Math.min(100, Math.round(finalScore/Math.max(maxPossible,100)*100));
  let milestone = nextMilestoneMap[0].text;
  for(const m of nextMilestoneMap){ if(pctScore>=m.min) milestone = m.text; }
  card.appendChild(el('div',{class:'principle-box'}, el('b',{},'🎯 Next Milestone: '), milestone));

  // Final optimized prompt example (best scenario)
  const bestScenario = STATE.scenarios[STATE.scenarios.length-1];
  card.appendChild(el('div',{class:'col-title', style:'margin-top:18px;'}, '✨ Example Final Optimized Prompt'));
  card.appendChild(el('pre',{class:'prompt-text'}, bestScenario.optimizedPrompt));

  const btnRow = el('div',{class:'center', style:'margin-top:20px; display:flex; gap:12px; justify-content:center; flex-wrap:wrap;'});
  btnRow.appendChild(el('button',{class:'btn', onclick:()=> initGame(STATE.domain, STATE.difficulty)}, '🔁 Replay (New Scenarios)'));
  btnRow.appendChild(el('button',{class:'btn secondary', onclick:()=> renderRoot()}, '🏠 Change Domain / Difficulty'));
  card.appendChild(btnRow);

  app.appendChild(card);
}

// ---------- BOOT ----------
// Domain and difficulty were gathered in chat; set them here directly.
STATE.domain = "All Domains";
STATE.difficulty = "Intermediate";
renderRoot();
</script>
</body>
</html>
<img width="580" height="489" alt="image" src="https://github.com/user-attachments/assets/2d81c502-3bad-4756-892c-7b75a43bd209" />
<img width="538" height="505" alt="image" src="https://github.com/user-attachments/assets/25429280-a9fa-49de-9236-4d588fa0fa94" />
<img width="551" height="154" alt="image" src="https://github.com/user-attachments/assets/5389bbc3-6522-411c-a823-0d1db3998c47" />
<img width="558" height="441" alt="image" src="https://github.com/user-attachments/assets/14cf73b0-e480-41b8-8467-41b6951ce574" />
<img width="602" height="557" alt="image" src="https://github.com/user-attachments/assets/eb143d75-929a-49d6-a3d5-6f3b9a3af0c7" />
<img width="622" height="330" alt="image" src="https://github.com/user-attachments/assets/8e447ab1-74c0-4a59-a48b-be896be84a29" />
<img width="661" height="575" alt="image" src="https://github.com/user-attachments/assets/070be687-a08a-42a6-afef-a22b17fcbec4" />
<img width="625" height="556" alt="image" src="https://github.com/user-attachments/assets/1c07fd20-9ff3-4e69-ab59-d44aec69b86c" />
<img width="562" height="553" alt="image" src="https://github.com/user-attachments/assets/860e68d7-3f0d-4c4a-96a3-218d952f7e04" />
<img width="591" height="565" alt="image" src="https://github.com/user-attachments/assets/e071e7df-6609-4284-9084-190417d5d310" />
<img width="589" height="570" alt="image" src="https://github.com/user-attachments/assets/14d000b6-78b0-468f-bac0-15af700ff36d" />
<img width="593" height="300" alt="image" src="https://github.com/user-attachments/assets/3ec0d203-b9e1-4af8-aef1-43f8b430465a" />
<img width="648" height="577" alt="image" src="https://github.com/user-attachments/assets/0359a882-8460-46de-bd5a-aef90bcfa38a" />
<img width="613" height="270" alt="image" src="https://github.com/user-attachments/assets/6bd132a3-b26f-435e-ad42-a6515299e2aa" />
<img width="618" height="570" alt="image" src="https://github.com/user-attachments/assets/ffe14c81-b6c7-4776-a4cb-335509a81c30" />
<img width="590" height="329" alt="image" src="https://github.com/user-attachments/assets/1dd82ac2-47ef-4360-a23e-05ddcc798a83" />
<img width="625" height="573" alt="image" src="https://github.com/user-attachments/assets/5d4685dc-0763-4753-b8c3-545db11d9ddd" />
<img width="563" height="466" alt="image" src="https://github.com/user-attachments/assets/c476e2e6-f26a-4005-bb92-366f6e786a16" />
<img width="636" height="408" alt="image" src="https://github.com/user-attachments/assets/643ca718-c8f9-41b9-89e6-acb4aa6f3aec" />
<img width="612" height="565" alt="image" src="https://github.com/user-attachments/assets/36d30532-1d91-4bbb-9557-e976f8a6a4e8" />
<img width="597" height="355" alt="image" src="https://github.com/user-attachments/assets/46b0bcc4-c113-4fde-a7bf-4f7a745b2ee6" />
<img width="622" height="574" alt="image" src="https://github.com/user-attachments/assets/cdf51857-b9b6-4b3f-8cbe-f0147e977ba8" />
<img width="562" height="537" alt="image" src="https://github.com/user-attachments/assets/1b9a4ca6-7c39-4110-955f-2eaf68e800f4" />
<img width="606" height="543" alt="image" src="https://github.com/user-attachments/assets/796e0b9c-0b98-40b0-9568-8d9a4b13e14e" />
<img width="587" height="557" alt="image" src="https://github.com/user-attachments/assets/3cbe6422-8c1c-4fad-8098-370d417dd1d6" />
<img width="609" height="304" alt="image" src="https://github.com/user-attachments/assets/220c3bca-c4f7-46f1-aa5d-45f636bda701" />
<img width="583" height="503" alt="image" src="https://github.com/user-attachments/assets/40f43739-f060-47ce-bf07-cbf91c70c456" />
<img width="604" height="571" alt="image" src="https://github.com/user-attachments/assets/1b580377-ae39-48ad-afa2-1391ff168266" />
<img width="596" height="570" alt="image" src="https://github.com/user-attachments/assets/a5dbc06a-5692-4c7c-9df3-c108879ba281" />
<img width="632" height="583" alt="image" src="https://github.com/user-attachments/assets/4993b658-bbe2-4564-9326-5d0b48789ff6" />
<img width="582" height="576" alt="image" src="https://github.com/user-attachments/assets/275a2276-a7da-476f-9f56-b020fdf2a279" />
<img width="584" height="393" alt="image" src="https://github.com/user-attachments/assets/ec981c2e-2a59-483f-82e3-39fd40016d10" />
<img width="603" height="583" alt="image" src="https://github.com/user-attachments/assets/205de832-1b53-4f31-bc56-b64201e963d8" />
<img width="605" height="592" alt="image" src="https://github.com/user-attachments/assets/2e19117a-2a50-4784-8b33-99a26535a7ee" />
