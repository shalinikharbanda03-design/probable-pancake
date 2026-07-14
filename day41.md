:Prompt:
# Interactive Learning Studio

You are an expert educator, curriculum designer, instructional designer, subject matter expert, UI/UX designer, and senior frontend developer.

Before generating anything, ask the user the following questions ONE AT A TIME, in MCQ format only, no user typed input (keep that as last option).

1. What kind of Interactive Learning Studio would you like to build?
(Offer domains and subjects.)

2. Continue asking follow-up questions until the requested subject has been narrowed to a topic that can realistically be taught in a single comprehensive interactive tutorial.
Do not stop after identifying only a domain or subject. Use your own judgment to determine when the scope is appropriate.
Example:
Programming → Python → Object-Oriented Programming.

The topic should be broad enough to include multiple related concepts but focused enough to be completely taught within one tutorial.

3. Would you like Claude to automatically structure the tutorial, or would you like to customize its sections?
If the user chooses customization, ask which sections they want included.

After collecting all responses, generate a premium single-page interactive HTML application called 'Interactive Learning Studio'.

The application should teach the selected topic completely rather than creating a learning roadmap or summary. The chosen topic should already be known and must not be requested again inside the HTML.

Begin with an introduction containing learning objectives, estimated completion time, prerequisites (if any), expected outcomes, and a reward system.

Divide the tutorial into four progressively difficult modules, moving from foundational understanding to practical application and mastery.

Each module should include:
- Detailed explanations
- Topic-specific examples
- Analogies
- HTML/CSS/SVG diagrams where appropriate
- Comparisons
- Practical exercises
- Common misconceptions
- Key takeaways
- Interactive elements

After each module, include a 4-question interactive quiz with automatic scoring, instant feedback, explanations for every answer, and a short performance summary before unlocking the next module.

Conclude with:
- Final practical challenge
- Cheat sheet
- Summary notes
- Continue Learning section
- Books
- Documentation
- Research papers (where appropriate)
- Communities
- Practice platforms
- Search keywords
- Additional AI prompts for further learning.

Every lesson, example, analogy, diagram, exercise, quiz, and challenge must be generated specifically for the selected topic.

Generate everything as a single self-contained HTML file using only HTML, CSS, and JavaScript only, without external libraries or frameworks.

Design the interface as a polished commercial learning platform with responsive design, dark mode, smooth animations, progress tracking, quiz scoring, completion tracking, printable notes, and an intuitive user experience.

:Response:

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Interactive Learning Studio · Linear Equations & Systems</title>
<style>
:root{
  --bg:#0b0f1a; --bg2:#121829; --card:#161d30; --card2:#1c2440;
  --border:#2a3452; --text:#e8ecf7; --muted:#93a1c4; --accent:#6c8bff;
  --accent2:#9b6cff; --good:#33d69f; --warn:#ffb24d; --bad:#ff6b6b;
  --shadow: 0 10px 30px rgba(0,0,0,.35);
  --radius:16px;
}
*{box-sizing:border-box;}
body.light{
  --bg:#f4f6fb; --bg2:#ffffff; --card:#ffffff; --card2:#eef1fa;
  --border:#dbe1f2; --text:#1b2340; --muted:#5a6482; --accent:#3f5eff;
  --accent2:#8b3fff; --good:#0f9d6b; --warn:#c9761a; --bad:#d63b3b;
  --shadow: 0 10px 30px rgba(30,40,80,.10);
}
html,body{margin:0;padding:0;}
body{
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  background: radial-gradient(1200px 800px at 80% -10%, rgba(108,139,255,.15), transparent),
              radial-gradient(1000px 700px at -10% 20%, rgba(155,108,255,.12), transparent),
              var(--bg);
  color:var(--text);
  transition: background .3s, color .3s;
  min-height:100vh;
}
a{color:var(--accent);}
.container{max-width:980px;margin:0 auto;padding:20px 20px 80px;}
.topbar{
  position:sticky; top:0; z-index:50; backdrop-filter: blur(10px);
  background: linear-gradient(to bottom, rgba(11,15,26,.9), rgba(11,15,26,.6));
  border-bottom:1px solid var(--border);
}
body.light .topbar{ background: linear-gradient(to bottom, rgba(244,246,251,.95), rgba(244,246,251,.7)); }
.topbar-inner{max-width:980px;margin:0 auto;padding:12px 20px;display:flex;align-items:center;gap:14px;justify-content:space-between;flex-wrap:wrap;}
.brand{display:flex;align-items:center;gap:10px;font-weight:700;font-size:15px;}
.brand .logo{width:30px;height:30px;border-radius:9px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;font-size:15px;box-shadow:var(--shadow);}
.progress-wrap{flex:1;min-width:180px;display:flex;align-items:center;gap:10px;}
.progress-track{flex:1;height:8px;border-radius:6px;background:var(--card2);overflow:hidden;border:1px solid var(--border);}
.progress-fill{height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));width:0%;transition:width .5s ease;}
.progress-label{font-size:12px;color:var(--muted);white-space:nowrap;}
.icon-btn{
  border:1px solid var(--border); background:var(--card2); color:var(--text);
  width:36px;height:36px;border-radius:10px;cursor:pointer;font-size:16px;
  display:flex;align-items:center;justify-content:center;transition:.2s;
}
.icon-btn:hover{border-color:var(--accent);transform:translateY(-1px);}
.pill{
  display:inline-flex;align-items:center;gap:6px;padding:4px 10px;border-radius:999px;
  background:var(--card2);border:1px solid var(--border);font-size:12px;color:var(--muted);
}
.card{
  background:var(--card); border:1px solid var(--border); border-radius:var(--radius);
  padding:24px; margin:22px 0; box-shadow:var(--shadow);
  animation:fadein .5s ease;
}
@keyframes fadein{from{opacity:0;transform:translateY(8px);}to{opacity:1;transform:translateY(0);}}
h1{font-size:28px;margin:.2em 0;}
h2{font-size:22px;margin-top:0;display:flex;align-items:center;gap:10px;}
h3{font-size:17px;color:var(--accent);margin-bottom:6px;}
.subtitle{color:var(--muted);font-size:15px;line-height:1.6;}
.badge-row{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0;}
.stat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:18px 0;}
.stat{background:var(--card2);border:1px solid var(--border);border-radius:12px;padding:14px;text-align:center;}
.stat .num{font-size:20px;font-weight:700;color:var(--accent);}
.stat .lbl{font-size:12px;color:var(--muted);margin-top:2px;}
.btn{
  background:linear-gradient(135deg,var(--accent),var(--accent2)); color:#fff; border:none;
  padding:12px 22px;border-radius:10px;font-size:15px;font-weight:600;cursor:pointer;
  transition:.2s; box-shadow:0 6px 18px rgba(108,139,255,.3);
}
.btn:hover{transform:translateY(-2px);box-shadow:0 10px 22px rgba(108,139,255,.4);}
.btn:disabled{opacity:.4;cursor:not-allowed;transform:none;}
.btn.secondary{background:var(--card2);color:var(--text);border:1px solid var(--border);box-shadow:none;}
.btn.secondary:hover{border-color:var(--accent);}
.btn-row{display:flex;gap:10px;flex-wrap:wrap;margin-top:16px;}
.module{display:none;}
.module.active{display:block;}
.module-header{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;margin-bottom:6px;}
.module-tag{font-size:12px;letter-spacing:.5px;text-transform:uppercase;color:var(--accent2);font-weight:700;}
.section{margin:22px 0;padding-top:6px;border-top:1px dashed var(--border);}
.section:first-child{border-top:none;}
.example-box{
  background:var(--card2);border:1px solid var(--border);border-left:4px solid var(--accent);
  border-radius:10px; padding:14px 16px; margin:12px 0; font-size:14.5px;
}
.analogy-box{
  background:linear-gradient(135deg, rgba(155,108,255,.10), rgba(108,139,255,.06));
  border:1px solid var(--border); border-left:4px solid var(--accent2);
  border-radius:10px; padding:14px 16px; margin:12px 0; font-size:14.5px;
}
.misconception-box{
  background:rgba(255,178,77,.08); border:1px solid var(--border); border-left:4px solid var(--warn);
  border-radius:10px; padding:14px 16px; margin:12px 0; font-size:14.5px;
}
.takeaway-box{
  background:rgba(51,214,159,.08); border:1px solid var(--border); border-left:4px solid var(--good);
  border-radius:10px; padding:14px 16px; margin:12px 0; font-size:14.5px;
}
.math{font-family:"Cambria Math", Georgia, serif; font-size:1.05em;}
table.compare{width:100%;border-collapse:collapse;margin:12px 0;font-size:14px;}
table.compare th,table.compare td{border:1px solid var(--border);padding:8px 10px;text-align:left;}
table.compare th{background:var(--card2);color:var(--accent);}
.diagram-wrap{background:var(--card2);border:1px solid var(--border);border-radius:12px;padding:14px;margin:14px 0;overflow-x:auto;}
.diagram-wrap svg{max-width:100%;height:auto;display:block;margin:0 auto;}
.exercise{
  background:var(--card2);border:1px solid var(--border);border-radius:12px;padding:16px;margin:14px 0;
}
.exercise input[type=text], .exercise input[type=number]{
  background:var(--bg2);border:1px solid var(--border);color:var(--text);padding:9px 12px;border-radius:8px;font-size:14px;width:160px;
}
.exercise .fb{margin-top:10px;font-size:14px;padding:8px 12px;border-radius:8px;display:none;}
.exercise .fb.show{display:block;}
.fb.correct{background:rgba(51,214,159,.12);color:var(--good);border:1px solid rgba(51,214,159,.3);}
.fb.wrong{background:rgba(255,107,107,.12);color:var(--bad);border:1px solid rgba(255,107,107,.3);}
.slider-row{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin:10px 0;}
input[type=range]{accent-color:var(--accent);flex:1;min-width:160px;}
.quiz-q{margin:18px 0;padding:16px;background:var(--card2);border:1px solid var(--border);border-radius:12px;}
.quiz-opt{
  display:block;width:100%;text-align:left;background:var(--bg2);border:1px solid var(--border);color:var(--text);
  padding:10px 14px;border-radius:9px;margin:8px 0;cursor:pointer;font-size:14px;transition:.15s;
}
.quiz-opt:hover{border-color:var(--accent);}
.quiz-opt.selected{border-color:var(--accent);background:rgba(108,139,255,.12);}
.quiz-opt.correct{border-color:var(--good);background:rgba(51,214,159,.15);}
.quiz-opt.incorrect{border-color:var(--bad);background:rgba(255,107,107,.15);}
.quiz-opt:disabled{cursor:default;}
.quiz-explain{margin-top:10px;font-size:13.5px;color:var(--muted);padding:10px;border-radius:8px;background:var(--bg2);display:none;}
.quiz-explain.show{display:block;}
.quiz-summary{text-align:center;padding:24px;}
.quiz-summary .score{font-size:42px;font-weight:800;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;background-clip:text;color:transparent;}
.lock-msg{text-align:center;color:var(--muted);padding:40px 10px;}
.lock-msg .lockicon{font-size:34px;margin-bottom:10px;}
.toc{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;margin:16px 0;}
.toc-item{
  background:var(--card2);border:1px solid var(--border);border-radius:12px;padding:14px;cursor:pointer;transition:.2s;
  display:flex;flex-direction:column;gap:6px;
}
.toc-item:hover{border-color:var(--accent);transform:translateY(-2px);}
.toc-item.done{border-color:var(--good);}
.toc-item .num{width:26px;height:26px;border-radius:50%;background:var(--card);display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;border:1px solid var(--border);}
.toc-item.done .num{background:var(--good);color:#04231a;border:none;}
footer.cs{margin-top:40px;font-size:12.5px;color:var(--muted);text-align:center;}
.resource-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;}
.resource-card{background:var(--card2);border:1px solid var(--border);border-radius:12px;padding:16px;}
.resource-card h4{margin:0 0 8px;font-size:14px;color:var(--accent);}
.resource-card ul{margin:0;padding-left:18px;font-size:13.5px;color:var(--muted);}
.resource-card li{margin:4px 0;}
.kw{display:inline-block;background:var(--bg2);border:1px solid var(--border);border-radius:6px;padding:3px 8px;margin:3px 4px 0 0;font-size:12.5px;}
.print-btn{position:fixed;bottom:20px;right:20px;z-index:40;}
@media print{
  .topbar,.print-btn,.btn-row,.icon-btn{display:none !important;}
  .module{display:block !important;}
  .card{box-shadow:none;border:1px solid #ccc;}
}
.confetti{position:fixed;inset:0;pointer-events:none;z-index:100;overflow:hidden;}
.confetti span{position:absolute;top:-20px;font-size:18px;animation:fall linear forwards;}
@keyframes fall{to{transform:translateY(110vh) rotate(360deg);opacity:0;}}
.cheat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;}
.cheat-card{background:var(--card2);border:1px solid var(--border);border-radius:10px;padding:12px 14px;font-size:13.5px;}
.cheat-card h4{margin:0 0 6px;color:var(--accent2);font-size:13px;}
</style>
</head>
<body>

<div class="topbar">
  <div class="topbar-inner">
    <div class="brand"><div class="logo">∑</div> Interactive Learning Studio</div>
    <div class="progress-wrap">
      <div class="progress-track"><div class="progress-fill" id="progressFill"></div></div>
      <div class="progress-label" id="progressLabel">0% complete</div>
    </div>
    <div style="display:flex;gap:8px;">
      <button class="icon-btn" id="themeToggle" title="Toggle dark/light mode">🌙</button>
      <button class="icon-btn" id="printBtn" title="Print / Save notes">🖨️</button>
    </div>
  </div>
</div>

<div class="container">

  <!-- INTRO -->
  <div class="card" id="introCard">
    <span class="pill">📘 Algebra · Linear Equations & Systems</span>
    <h1>Linear Equations & Systems — Complete Mastery Tutorial</h1>
    <p class="subtitle">A single, self-contained course that takes you from "what is a linear equation" all the way to solving real systems with elimination, substitution, matrices, and word problems — with diagrams, quizzes, and hands-on exercises built specifically for this topic.</p>

    <h3 style="margin-top:22px;">🎯 Learning Objectives</h3>
    <ul class="subtitle">
      <li>Define linear equations and recognize them in one and two variables</li>
      <li>Graph lines using slope-intercept and point-slope forms, and interpret slope as rate of change</li>
      <li>Solve systems of two linear equations using graphing, substitution, and elimination</li>
      <li>Classify systems as one solution, no solution, or infinite solutions — and explain why</li>
      <li>Translate real-world word problems into systems of equations and solve them</li>
      <li>Understand matrix representation of systems and solve small systems with matrices</li>
    </ul>

    <div class="stat-grid">
      <div class="stat"><div class="num">~55 min</div><div class="lbl">Estimated time</div></div>
      <div class="stat"><div class="num">4</div><div class="lbl">Modules</div></div>
      <div class="stat"><div class="num">16</div><div class="lbl">Quiz questions</div></div>
      <div class="stat"><div class="num">🏆 500 XP</div><div class="lbl">Max reward</div></div>
    </div>

    <h3>✅ Prerequisites</h3>
    <p class="subtitle">Basic arithmetic (add, subtract, multiply, divide) and comfort with simple algebraic notation like <span class="math">x + 3 = 7</span>. No prior graphing knowledge required.</p>

    <h3>🚀 Expected Outcomes</h3>
    <p class="subtitle">By the end, you'll be able to confidently solve any system of two linear equations by hand, choose the most efficient method, graph lines instantly from an equation, and model simple real-world scenarios (budgets, mixtures, speeds) as systems.</p>

    <h3>🏅 Reward System</h3>
    <p class="subtitle">Earn <b>XP</b> for completing each module's quiz (up to 100 XP each) and the final challenge (100 XP). Track your progress bar at the top. Unlock a completion certificate at the end!</p>

    <div class="toc" id="tocGrid"></div>

    <div class="btn-row">
      <button class="btn" id="startBtn">Start Learning →</button>
    </div>
  </div>

  <!-- MODULE 1 -->
  <div class="module" id="module1">
    <div class="card">
      <div class="module-header">
        <div><span class="module-tag">Module 1 · Foundations</span><h2>What Is a Linear Equation?</h2></div>
        <span class="pill" id="xp1">0 XP</span>
      </div>
      <p class="subtitle">We start from the ground up: what makes an equation "linear," how to solve one-variable equations, and how to graph two-variable linear equations.</p>

      <div class="section">
        <h3>📖 Explanation</h3>
        <p>A <b>linear equation</b> is an equation where every variable appears only to the first power (no <span class="math">x²</span>, no <span class="math">1/x</span>, no <span class="math">√x</span>), and variables aren't multiplied together. In one variable it looks like <span class="math">ax + b = c</span>. In two variables it looks like <span class="math">ax + by = c</span>, and its graph is always a straight line — that's exactly why it's called "linear."</p>
        <p>Solving a one-variable linear equation means isolating the variable using inverse operations: whatever you do to one side, you do to the other, to keep the equation balanced.</p>
      </div>

      <div class="section">
        <h3>🧮 Example</h3>
        <div class="example-box">
          Solve <span class="math">3x + 5 = 20</span><br>
          Step 1: Subtract 5 from both sides → <span class="math">3x = 15</span><br>
          Step 2: Divide both sides by 3 → <span class="math">x = 5</span><br>
          Check: <span class="math">3(5) + 5 = 20</span> ✓
        </div>
      </div>

      <div class="section">
        <h3>💡 Analogy</h3>
        <div class="analogy-box">Think of an equation as a <b>balance scale</b>. Both sides must weigh the same. If you add, remove, multiply, or divide weight on one side, you must do the exact same thing on the other side, or the scale tips and the equation becomes false.</div>
      </div>

      <div class="section">
        <h3>📊 Diagram: Slope-Intercept Form Live Graph</h3>
        <p class="subtitle">The equation <span class="math">y = mx + b</span> describes every non-vertical line. <b>m</b> is the slope (steepness/direction) and <b>b</b> is the y-intercept (where the line crosses the y-axis). Drag the sliders to see how each changes the line.</p>
        <div class="diagram-wrap">
          <svg id="lineSvg" viewBox="0 0 320 320" width="320" height="320">
            <line x1="10" y1="160" x2="310" y2="160" stroke="var(--muted)" stroke-width="1"/>
            <line x1="160" y1="10" x2="160" y2="310" stroke="var(--muted)" stroke-width="1"/>
            <text x="300" y="152" fill="var(--muted)" font-size="10">x</text>
            <text x="168" y="20" fill="var(--muted)" font-size="10">y</text>
            <line id="graphLine" x1="0" y1="160" x2="320" y2="160" stroke="var(--accent)" stroke-width="3"/>
            <circle id="interceptDot" cx="160" cy="160" r="4" fill="var(--accent2)"/>
          </svg>
        </div>
        <div class="slider-row">
          <label for="mSlider">m (slope): <span id="mVal">0</span></label>
          <input type="range" id="mSlider" min="-5" max="5" step="0.5" value="0">
        </div>
        <div class="slider-row">
          <label for="bSlider">b (intercept): <span id="bVal">0</span></label>
          <input type="range" id="bSlider" min="-5" max="5" step="1" value="0">
        </div>
        <p class="subtitle" id="lineEqDisplay" style="text-align:center;font-weight:600;">y = 0x + 0</p>
      </div>

      <div class="section">
        <h3>⚖️ Comparison: Equation Forms</h3>
        <table class="compare">
          <tr><th>Form</th><th>Structure</th><th>Best used when...</th></tr>
          <tr><td>Slope-Intercept</td><td><span class="math">y = mx + b</span></td><td>You know the slope and y-intercept, or want to graph quickly</td></tr>
          <tr><td>Point-Slope</td><td><span class="math">y - y₁ = m(x - x₁)</span></td><td>You know the slope and one point on the line</td></tr>
          <tr><td>Standard Form</td><td><span class="math">Ax + By = C</span></td><td>Working with systems of equations, especially elimination</td></tr>
        </table>
      </div>

      <div class="section">
        <h3>✏️ Practical Exercise</h3>
        <div class="exercise">
          <p>A line has slope <b>2</b> and passes through <b>(1, 3)</b>. Using point-slope form, what is <b>b</b> (the y-intercept) when converted to slope-intercept form?</p>
          <input type="text" id="ex1input" placeholder="Enter b">
          <button class="btn secondary" onclick="checkEx1()">Check</button>
          <div class="fb" id="ex1fb"></div>
        </div>
      </div>

      <div class="section">
        <h3>⚠️ Common Misconception</h3>
        <div class="misconception-box">Many students think slope means "how high the line is." Slope is actually the <b>rate of change</b> — how much y changes per unit of x — not the line's height or position. A line can be high up on the graph and still have zero slope (flat).</div>
      </div>

      <div class="section">
        <h3>🔑 Key Takeaways</h3>
        <div class="takeaway-box">
          <ul style="margin:0;padding-left:18px;">
            <li>Linear equations produce straight-line graphs and have variables raised only to the power of 1.</li>
            <li>Solve one-variable equations by isolating x using inverse operations, keeping both sides balanced.</li>
            <li><span class="math">y = mx + b</span>: m controls steepness/direction, b controls vertical position.</li>
          </ul>
        </div>
      </div>

      <div class="btn-row"><button class="btn" onclick="goToQuiz(1)">Take Module 1 Quiz →</button></div>
    </div>

    <div class="card" id="quiz1card"></div>
  </div>

  <!-- MODULE 2 -->
  <div class="module" id="module2">
    <div class="card">
      <div class="module-header">
        <div><span class="module-tag">Module 2 · Core Skills</span><h2>Solving Systems: Graphing, Substitution & Elimination</h2></div>
        <span class="pill" id="xp2">0 XP</span>
      </div>
      <p class="subtitle">A system of linear equations is a set of two (or more) equations sharing variables. Solving the system means finding the point(s) that satisfy <em>all</em> equations at once.</p>

      <div class="section">
        <h3>📖 Explanation</h3>
        <p>Three classic methods solve a 2-equation system:</p>
        <ul>
          <li><b>Graphing:</b> plot both lines; their intersection is the solution.</li>
          <li><b>Substitution:</b> solve one equation for one variable, then substitute that expression into the other equation.</li>
          <li><b>Elimination:</b> add or subtract the equations (after scaling) so one variable cancels out.</li>
        </ul>
      </div>

      <div class="section">
        <h3>🧮 Example — Substitution</h3>
        <div class="example-box">
          Solve: <span class="math">y = 2x + 1</span> and <span class="math">3x + y = 11</span><br>
          Substitute y: <span class="math">3x + (2x + 1) = 11 → 5x + 1 = 11 → 5x = 10 → x = 2</span><br>
          Back-substitute: <span class="math">y = 2(2)+1 = 5</span> → Solution: <span class="math">(2, 5)</span>
        </div>
      </div>

      <div class="section">
        <h3>🧮 Example — Elimination</h3>
        <div class="example-box">
          Solve: <span class="math">2x + 3y = 12</span> and <span class="math">2x - y = 0</span><br>
          Subtract equations: <span class="math">(2x+3y) - (2x-y) = 12 - 0 → 4y = 12 → y = 3</span><br>
          Back-substitute: <span class="math">2x - 3 = 0 → x = 1.5</span> → Solution: <span class="math">(1.5, 3)</span>
        </div>
      </div>

      <div class="section">
        <h3>💡 Analogy</h3>
        <div class="analogy-box">Substitution is like <b>swapping ingredients</b> in a recipe: if you know sugar = 2×flour, you replace "sugar" everywhere with "2×flour" so only one unknown remains. Elimination is like <b>canceling matching items</b> when comparing two grocery receipts — if both carts have the same 2 apples, subtracting the receipts removes the apples and reveals the price difference of what's left.</div>
      </div>

      <div class="section">
        <h3>📊 Diagram: Two Lines Intersecting</h3>
        <p class="subtitle">Adjust the two lines below and watch the intersection point (the system's solution) update live.</p>
        <div class="diagram-wrap">
          <svg viewBox="0 0 320 320" width="320" height="320">
            <line x1="10" y1="160" x2="310" y2="160" stroke="var(--muted)" stroke-width="1"/>
            <line x1="160" y1="10" x2="160" y2="310" stroke="var(--muted)" stroke-width="1"/>
            <line id="sysLine1" stroke="var(--accent)" stroke-width="3"/>
            <line id="sysLine2" stroke="var(--accent2)" stroke-width="3"/>
            <circle id="sysDot" r="5" fill="var(--good)"/>
          </svg>
        </div>
        <div class="slider-row"><label>Line A slope: <span id="sm1v">1</span></label><input type="range" id="sm1" min="-3" max="3" step="0.5" value="1"></div>
        <div class="slider-row"><label>Line A intercept: <span id="sb1v">0</span></label><input type="range" id="sb1" min="-4" max="4" step="1" value="0"></div>
        <div class="slider-row"><label>Line B slope: <span id="sm2v">-1</span></label><input type="range" id="sm2" min="-3" max="3" step="0.5" value="-1"></div>
        <div class="slider-row"><label>Line B intercept: <span id="sb2v">4</span></label><input type="range" id="sb2" min="-4" max="4" step="1" value="4"></div>
        <p class="subtitle" id="sysSolutionDisplay" style="text-align:center;font-weight:600;"></p>
      </div>

      <div class="section">
        <h3>⚖️ Comparison: When to use each method</h3>
        <table class="compare">
          <tr><th>Method</th><th>Best when...</th><th>Downside</th></tr>
          <tr><td>Graphing</td><td>You want visual intuition or an approximate answer</td><td>Imprecise for non-integer solutions</td></tr>
          <tr><td>Substitution</td><td>One equation is already solved for a variable (or easy to isolate)</td><td>Can get messy with fractions</td></tr>
          <tr><td>Elimination</td><td>Coefficients line up nicely or can be scaled to match</td><td>Requires careful sign management</td></tr>
        </table>
      </div>

      <div class="section">
        <h3>✏️ Practical Exercise</h3>
        <div class="exercise">
          <p>Solve using elimination: <span class="math">x + y = 10</span> and <span class="math">x - y = 2</span>. What is <b>x</b>?</p>
          <input type="text" id="ex2input" placeholder="Enter x">
          <button class="btn secondary" onclick="checkEx2()">Check</button>
          <div class="fb" id="ex2fb"></div>
        </div>
      </div>

      <div class="section">
        <h3>⚠️ Common Misconception</h3>
        <div class="misconception-box">Students often forget to distribute a negative sign when subtracting equations in elimination, e.g. turning <span class="math">(2x+3y)-(2x-y)</span> into <span class="math">2y</span> instead of the correct <span class="math">4y</span>. Always distribute the subtraction across every term of the second equation.</div>
      </div>

      <div class="section">
        <h3>🔑 Key Takeaways</h3>
        <div class="takeaway-box">
          <ul style="margin:0;padding-left:18px;">
            <li>A system's solution is the point where all equations are simultaneously true.</li>
            <li>Substitution and elimination are algebraic (exact); graphing is visual (approximate).</li>
            <li>Choose your method based on how the equations are structured — no single method is always fastest.</li>
          </ul>
        </div>
      </div>

      <div class="btn-row"><button class="btn" onclick="goToQuiz(2)">Take Module 2 Quiz →</button></div>
    </div>
    <div class="card" id="quiz2card"></div>
  </div>

  <!-- MODULE 3 -->
  <div class="module" id="module3">
    <div class="card">
      <div class="module-header">
        <div><span class="module-tag">Module 3 · Practical Application</span><h2>Special Cases & Real-World Word Problems</h2></div>
        <span class="pill" id="xp3">0 XP</span>
      </div>
      <p class="subtitle">Not every system has exactly one solution — and real systems come from real situations: budgets, mixtures, speeds. This module bridges theory and application.</p>

      <div class="section">
        <h3>📖 Explanation</h3>
        <p>Systems fall into three categories:</p>
        <ul>
          <li><b>One solution (consistent, independent):</b> lines cross at exactly one point — different slopes.</li>
          <li><b>No solution (inconsistent):</b> lines are parallel — same slope, different intercepts. During elimination you'll get a false statement like <span class="math">0 = 5</span>.</li>
          <li><b>Infinite solutions (consistent, dependent):</b> lines are identical — same slope and same intercept. Elimination gives a true statement like <span class="math">0 = 0</span>.</li>
        </ul>
        <p>Word problems become systems once you define variables clearly and translate each sentence into an equation.</p>
      </div>

      <div class="section">
        <h3>🧮 Example — Word Problem</h3>
        <div class="example-box">
          "A movie theater sells adult tickets for $12 and child tickets for $8. One night, 150 tickets were sold for a total of $1,560. How many of each were sold?"<br><br>
          Let a = adult tickets, c = child tickets.<br>
          <span class="math">a + c = 150</span><br>
          <span class="math">12a + 8c = 1560</span><br>
          From eq 1: <span class="math">c = 150 - a</span>. Substitute: <span class="math">12a + 8(150-a) = 1560 → 4a + 1200 = 1560 → a = 90</span><br>
          So <span class="math">c = 60</span>: 90 adult tickets, 60 child tickets.
        </div>
      </div>

      <div class="section">
        <h3>💡 Analogy</h3>
        <div class="analogy-box">Parallel lines with no solution are like two people running the <b>same pace</b> starting at different points on a track — they'll never meet, no matter how far they run. Identical lines (infinite solutions) are like <b>two labels for the same runner</b> — every point that's true for one is automatically true for the other.</div>
      </div>

      <div class="section">
        <h3>📊 Diagram: Three System Types</h3>
        <div class="diagram-wrap">
          <svg viewBox="0 0 480 180" width="480" height="180">
            <!-- one solution -->
            <g transform="translate(10,10)">
              <line x1="0" y1="80" x2="140" y2="80" stroke="var(--border)" stroke-width="1"/>
              <line x1="70" y1="0" x2="70" y2="160" stroke="var(--border)" stroke-width="1"/>
              <line x1="10" y1="150" x2="130" y2="10" stroke="var(--accent)" stroke-width="3"/>
              <line x1="10" y1="10" x2="130" y2="150" stroke="var(--accent2)" stroke-width="3"/>
              <circle cx="70" cy="80" r="4" fill="var(--good)"/>
              <text x="35" y="175" fill="var(--muted)" font-size="11">One Solution</text>
            </g>
            <!-- no solution -->
            <g transform="translate(180,10)">
              <line x1="0" y1="80" x2="140" y2="80" stroke="var(--border)" stroke-width="1"/>
              <line x1="70" y1="0" x2="70" y2="160" stroke="var(--border)" stroke-width="1"/>
              <line x1="10" y1="130" x2="130" y2="30" stroke="var(--accent)" stroke-width="3"/>
              <line x1="10" y1="150" x2="130" y2="50" stroke="var(--accent2)" stroke-width="3"/>
              <text x="45" y="175" fill="var(--muted)" font-size="11">No Solution</text>
            </g>
            <!-- infinite -->
            <g transform="translate(350,10)">
              <line x1="0" y1="80" x2="140" y2="80" stroke="var(--border)" stroke-width="1"/>
              <line x1="70" y1="0" x2="70" y2="160" stroke="var(--border)" stroke-width="1"/>
              <line x1="10" y1="130" x2="130" y2="30" stroke="var(--accent)" stroke-width="4"/>
              <line x1="10" y1="130" x2="130" y2="30" stroke="var(--good)" stroke-width="1.5" stroke-dasharray="4 4"/>
              <text x="25" y="175" fill="var(--muted)" font-size="11">Infinite Solutions</text>
            </g>
          </svg>
        </div>
      </div>

      <div class="section">
        <h3>⚖️ Comparison Table</h3>
        <table class="compare">
          <tr><th>Type</th><th>Slopes</th><th>Intercepts</th><th>Elimination result</th></tr>
          <tr><td>One solution</td><td>Different</td><td>Any</td><td>Finds unique x, y</td></tr>
          <tr><td>No solution</td><td>Same</td><td>Different</td><td>False statement (e.g. 0 = 5)</td></tr>
          <tr><td>Infinite solutions</td><td>Same</td><td>Same</td><td>True statement (e.g. 0 = 0)</td></tr>
        </table>
      </div>

      <div class="section">
        <h3>✏️ Practical Exercise</h3>
        <div class="exercise">
          <p>Two systems: (a) <span class="math">y = 3x + 2</span> & <span class="math">y = 3x - 1</span> (b) <span class="math">y = 3x + 2</span> & <span class="math">y = -x + 2</span>. Which one has <b>no solution</b>? Type "a" or "b".</p>
          <input type="text" id="ex3input" placeholder="a or b">
          <button class="btn secondary" onclick="checkEx3()">Check</button>
          <div class="fb" id="ex3fb"></div>
        </div>
      </div>

      <div class="section">
        <h3>⚠️ Common Misconception</h3>
        <div class="misconception-box">Students sometimes assume any system without an "obvious" solution is automatically wrong or unsolvable. Getting <span class="math">0 = 0</span> or <span class="math">0 = 5</span> isn't a mistake — it's meaningful information telling you the system has infinite solutions or no solution, respectively.</div>
      </div>

      <div class="section">
        <h3>🔑 Key Takeaways</h3>
        <div class="takeaway-box">
          <ul style="margin:0;padding-left:18px;">
            <li>Compare slopes and intercepts to predict solution type before solving.</li>
            <li>A false result during elimination means no solution; a true result means infinite solutions.</li>
            <li>Word problems require careful variable definition — write down what each letter represents.</li>
          </ul>
        </div>
      </div>

      <div class="btn-row"><button class="btn" onclick="goToQuiz(3)">Take Module 3 Quiz →</button></div>
    </div>
    <div class="card" id="quiz3card"></div>
  </div>

  <!-- MODULE 4 -->
  <div class="module" id="module4">
    <div class="card">
      <div class="module-header">
        <div><span class="module-tag">Module 4 · Mastery</span><h2>Matrices & Larger Systems</h2></div>
        <span class="pill" id="xp4">0 XP</span>
      </div>
      <p class="subtitle">At the mastery level, we represent systems compactly using matrices, and extend beyond two variables.</p>

      <div class="section">
        <h3>📖 Explanation</h3>
        <p>A system like <span class="math">2x + 3y = 8</span>, <span class="math">x - y = 1</span> can be written as a matrix equation <span class="math">AX = B</span>, where A holds the coefficients, X holds the variables, and B holds the constants. For two equations in two unknowns, we can solve using Cramer's Rule, which uses determinants: <span class="math">D = a₁b₂ - a₂b₁</span>, and each variable equals a modified determinant divided by D.</p>
        <p>This same matrix idea extends naturally to three or more variables, which is how computers solve large systems in engineering, economics, and machine learning.</p>
      </div>

      <div class="section">
        <h3>🧮 Example — Cramer's Rule</h3>
        <div class="example-box">
          System: <span class="math">2x + 3y = 8</span>, <span class="math">x - y = 1</span><br>
          <span class="math">D = (2)(-1) - (1)(3) = -2 - 3 = -5</span><br>
          <span class="math">Dx = (8)(-1) - (1)(3) = -8-3 = -11 → x = -11/-5 = 2.2</span><br>
          <span class="math">Dy = (2)(1) - (1)(8) = 2-8 = -6 → y = -6/-5 = 1.2</span>
        </div>
      </div>

      <div class="section">
        <h3>💡 Analogy</h3>
        <div class="analogy-box">A matrix is like a <b>spreadsheet of instructions</b> — instead of writing "2x + 3y = 8" as a sentence, you store the numbers 2, 3, 8 in a neat grid. Computers love grids because they can process rows and columns extremely fast, which is why matrices scale to systems with hundreds of variables.</div>
      </div>

      <div class="section">
        <h3>📊 Diagram: Matrix Representation</h3>
        <div class="diagram-wrap">
          <svg viewBox="0 0 380 140" width="380" height="140">
            <text x="10" y="75" fill="var(--text)" font-size="22">[</text>
            <text x="30" y="55" fill="var(--accent)" font-size="16">2</text>
            <text x="55" y="55" fill="var(--accent)" font-size="16">3</text>
            <text x="30" y="90" fill="var(--accent)" font-size="16">1</text>
            <text x="55" y="90" fill="var(--accent)" font-size="16">-1</text>
            <text x="80" y="75" fill="var(--text)" font-size="22">]</text>
            <text x="95" y="75" fill="var(--text)" font-size="22">[</text>
            <text x="112" y="55" fill="var(--accent2)" font-size="16">x</text>
            <text x="112" y="90" fill="var(--accent2)" font-size="16">y</text>
            <text x="128" y="75" fill="var(--text)" font-size="22">]</text>
            <text x="145" y="75" fill="var(--text)" font-size="20">=</text>
            <text x="170" y="75" fill="var(--text)" font-size="22">[</text>
            <text x="188" y="55" fill="var(--good)" font-size="16">8</text>
            <text x="188" y="90" fill="var(--good)" font-size="16">1</text>
            <text x="205" y="75" fill="var(--text)" font-size="22">]</text>
            <text x="230" y="30" fill="var(--muted)" font-size="11">A</text>
            <text x="105" y="30" fill="var(--muted)" font-size="11">X</text>
            <text x="185" y="30" fill="var(--muted)" font-size="11">B</text>
          </svg>
        </div>
      </div>

      <div class="section">
        <h3>⚖️ Comparison: Solving Methods at Scale</h3>
        <table class="compare">
          <tr><th>Method</th><th>2 variables</th><th>3+ variables</th></tr>
          <tr><td>Substitution/Elimination</td><td>Fast, easy by hand</td><td>Gets tedious quickly</td></tr>
          <tr><td>Cramer's Rule (determinants)</td><td>Clean formula</td><td>Works but determinants grow complex</td></tr>
          <tr><td>Matrix row-reduction (computers)</td><td>Overkill</td><td>Standard approach for large systems</td></tr>
        </table>
      </div>

      <div class="section">
        <h3>✏️ Practical Exercise</h3>
        <div class="exercise">
          <p>Using Cramer's Rule for <span class="math">x + y = 5</span>, <span class="math">2x - y = 1</span>: compute <span class="math">D = a₁b₂ - a₂b₁</span>. What is D?</p>
          <input type="text" id="ex4input" placeholder="Enter D">
          <button class="btn secondary" onclick="checkEx4()">Check</button>
          <div class="fb" id="ex4fb"></div>
        </div>
      </div>

      <div class="section">
        <h3>⚠️ Common Misconception</h3>
        <div class="misconception-box">Students often mix up rows and columns when reading coefficients into a matrix, flipping which numbers belong to x vs y. Always keep coefficients aligned by which variable and which equation (row) they came from — write the matrix directly beside the original equations the first few times.</div>
      </div>

      <div class="section">
        <h3>🔑 Key Takeaways</h3>
        <div class="takeaway-box">
          <ul style="margin:0;padding-left:18px;">
            <li>Matrices compactly represent systems as AX = B.</li>
            <li>Cramer's Rule solves 2-variable systems using determinants: D, Dx, Dy.</li>
            <li>Matrix methods generalize elegantly to systems with many variables — the foundation of computational linear algebra.</li>
          </ul>
        </div>
      </div>

      <div class="btn-row"><button class="btn" onclick="goToQuiz(4)">Take Module 4 Quiz →</button></div>
    </div>
    <div class="card" id="quiz4card"></div>
  </div>

  <!-- FINAL -->
  <div class="module" id="moduleFinal">
    <div class="card">
      <h2>🏁 Final Practical Challenge</h2>
      <p class="subtitle">Bring it all together: solve this multi-part real-world system without help, then reveal the solution to check your work.</p>
      <div class="exercise">
        <p><b>Scenario:</b> A café sells coffee for $4 and tea for $3. On Saturday, it sold 80 drinks total for $290. On Sunday, using the same prices, it sold 20 more coffees than teas, totaling 100 drinks. Set up and solve <em>both</em> days as systems. How many coffees were sold Saturday, and how many teas were sold Sunday?</p>
        <button class="btn secondary" id="revealBtn">Reveal Solution</button>
        <div id="finalSolution" style="display:none;margin-top:12px;">
          <div class="example-box">
            <b>Saturday:</b> c + t = 80, 4c + 3t = 290 → t = 80-c → 4c+3(80-c)=290 → c+240=290 → c=50, t=30.<br>
            <b>Sunday:</b> c + t = 100, c = t + 20 → (t+20)+t=100 → 2t=80 → t=40, c=60.<br>
            <b>Answer:</b> 50 coffees sold Saturday; 40 teas sold Sunday.
          </div>
        </div>
      </div>
      <div class="btn-row"><button class="btn" onclick="completeCourse()">Complete Course & Get Certificate 🎓</button></div>
    </div>

    <div class="card">
      <h2>📋 Cheat Sheet</h2>
      <div class="cheat-grid">
        <div class="cheat-card"><h4>Slope-Intercept</h4><span class="math">y = mx + b</span></div>
        <div class="cheat-card"><h4>Point-Slope</h4><span class="math">y - y₁ = m(x - x₁)</span></div>
        <div class="cheat-card"><h4>Standard Form</h4><span class="math">Ax + By = C</span></div>
        <div class="cheat-card"><h4>Slope Formula</h4><span class="math">m = (y₂-y₁)/(x₂-x₁)</span></div>
        <div class="cheat-card"><h4>Substitution</h4>Solve one eq for a variable, plug into the other.</div>
        <div class="cheat-card"><h4>Elimination</h4>Scale equations so a variable cancels when added/subtracted.</div>
        <div class="cheat-card"><h4>No Solution</h4>Same slope, different intercept → parallel lines</div>
        <div class="cheat-card"><h4>Infinite Solutions</h4>Same slope, same intercept → identical lines</div>
        <div class="cheat-card"><h4>Cramer's Rule</h4><span class="math">D = a₁b₂-a₂b₁</span>, <span class="math">x=Dx/D</span>, <span class="math">y=Dy/D</span></div>
      </div>
    </div>

    <div class="card">
      <h2>📝 Summary Notes</h2>
      <p class="subtitle">A linear equation graphs as a straight line and involves variables to the first power only. Systems of two linear equations can be solved by graphing (visual), substitution (algebraic swap), or elimination (canceling a variable). Systems can have one solution (intersecting lines), no solution (parallel lines), or infinite solutions (identical lines) — you can predict which by comparing slopes and intercepts. Real-world word problems become systems once variables are clearly defined. At scale, systems are represented with matrices (AX=B), and small systems can be solved exactly with Cramer's Rule using determinants — the same core idea that powers computational linear algebra for much larger systems.</p>
    </div>

    <div class="card">
      <h2>🔭 Continue Learning</h2>
      <div class="resource-grid">
        <div class="resource-card">
          <h4>📚 Books</h4>
          <ul>
            <li>"Algebra" by I.M. Gelfand & A. Shen</li>
            <li>"Linear Algebra and Its Applications" by David C. Lay</li>
            <li>"No-Nonsense Algebra" by Richard W. Fisher</li>
          </ul>
        </div>
        <div class="resource-card">
          <h4>📄 Documentation & Courses</h4>
          <ul>
            <li>Khan Academy — Systems of Equations unit</li>
            <li>Paul's Online Math Notes — Linear Algebra</li>
            <li>MIT OpenCourseWare 18.06 Linear Algebra</li>
          </ul>
        </div>
        <div class="resource-card">
          <h4>🔬 Research & Deeper Reading</h4>
          <ul>
            <li>Strang, G. "Linear Algebra and Its Applications" (foundational text, not a paper, but widely cited)</li>
            <li>Explore Gaussian elimination and row-reduction algorithms for larger systems</li>
          </ul>
        </div>
        <div class="resource-card">
          <h4>👥 Communities</h4>
          <ul>
            <li>r/learnmath (Reddit)</li>
            <li>Math Stack Exchange</li>
            <li>Art of Problem Solving forums</li>
          </ul>
        </div>
        <div class="resource-card">
          <h4>🧪 Practice Platforms</h4>
          <ul>
            <li>Khan Academy exercises</li>
            <li>IXL Algebra 1</li>
            <li>Brilliant.org — Algebra courses</li>
          </ul>
        </div>
        <div class="resource-card">
          <h4>🔎 Search Keywords</h4>
          <span class="kw">systems of linear equations</span>
          <span class="kw">substitution method</span>
          <span class="kw">elimination method</span>
          <span class="kw">Cramer's rule</span>
          <span class="kw">slope-intercept form</span>
          <span class="kw">consistent vs inconsistent systems</span>
        </div>
        <div class="resource-card">
          <h4>🤖 AI Prompts for Further Learning</h4>
          <ul>
            <li>"Give me 5 word problems that translate into systems of linear equations, with solutions."</li>
            <li>"Explain Gaussian elimination step-by-step for a 3x3 system."</li>
            <li>"Quiz me on identifying whether a system has one, no, or infinite solutions."</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="card" style="text-align:center;" id="certificateCard" style="display:none;">
    </div>
  </div>

  <footer class="cs">Interactive Learning Studio · Linear Equations & Systems · Built for focused, single-session mastery.</footer>
</div>

<button class="btn print-btn" id="printFloating" title="Print notes">🖨️ Print Notes</button>

<script>
/* ---------- THEME ---------- */
const themeToggle = document.getElementById('themeToggle');
themeToggle.addEventListener('click', ()=>{
  document.body.classList.toggle('light');
  themeToggle.textContent = document.body.classList.contains('light') ? '☀️' : '🌙';
});
document.getElementById('printBtn').onclick = ()=>window.print();
document.getElementById('printFloating').onclick = ()=>window.print();

/* ---------- STATE ---------- */
const state = {
  unlocked: [true,false,false,false,false], // module1..4, final
  xp: 0,
  quizScores: {1:null,2:null,3:null,4:null}
};

const totalModules = 4;
function updateProgress(){
  let completed = Object.values(state.quizScores).filter(s=>s!==null).length;
  let pct = Math.round((completed/totalModules)*100);
  document.getElementById('progressFill').style.width = pct+'%';
  document.getElementById('progressLabel').textContent = pct+'% complete · '+state.xp+' XP';
  buildTOC();
}

function buildTOC(){
  const toc = document.getElementById('tocGrid');
  const titles = ['Foundations','Core Skills','Practical Application','Mastery'];
  toc.innerHTML='';
  titles.forEach((t,i)=>{
    const done = state.quizScores[i+1]!==null;
    const div = document.createElement('div');
    div.className = 'toc-item'+(done?' done':'');
    div.innerHTML = `<div class="num">${done?'✓':(i+1)}</div><div>Module ${i+1}: ${t}</div>`;
    div.onclick = ()=>showModule(i+1);
    toc.appendChild(div);
  });
}
buildTOC();

document.getElementById('startBtn').onclick = ()=>showModule(1);

function showModule(n){
  document.querySelectorAll('.module').forEach(m=>m.classList.remove('active'));
  document.getElementById('module'+n).classList.add('active');
  document.getElementById('module'+n).scrollIntoView({behavior:'smooth'});
}

/* ---------- MODULE 1 DIAGRAM ---------- */
const mSlider = document.getElementById('mSlider');
const bSlider = document.getElementById('bSlider');
function updateLineGraph(){
  const m = parseFloat(mSlider.value);
  const b = parseFloat(bSlider.value);
  document.getElementById('mVal').textContent = m;
  document.getElementById('bVal').textContent = b;
  document.getElementById('lineEqDisplay').textContent = `y = ${m}x + ${b}`;
  // viewbox 320x320, origin at (160,160), scale 20px per unit, y flipped
  const scale=20;
  const x1=-8, x2=8;
  const y1 = m*x1+b, y2 = m*x2+b;
  const sx1=160+x1*scale, sy1=160-y1*scale;
  const sx2=160+x2*scale, sy2=160-y2*scale;
  document.getElementById('graphLine').setAttribute('x1',sx1);
  document.getElementById('graphLine').setAttribute('y1',sy1);
  document.getElementById('graphLine').setAttribute('x2',sx2);
  document.getElementById('graphLine').setAttribute('y2',sy2);
  document.getElementById('interceptDot').setAttribute('cx',160);
  document.getElementById('interceptDot').setAttribute('cy',160-b*scale);
}
mSlider.oninput = updateLineGraph;
bSlider.oninput = updateLineGraph;
updateLineGraph();

/* ---------- MODULE 2 DIAGRAM ---------- */
const sSliders = ['sm1','sb1','sm2','sb2'].map(id=>document.getElementById(id));
function updateSysGraph(){
  const m1=parseFloat(document.getElementById('sm1').value);
  const b1=parseFloat(document.getElementById('sb1').value);
  const m2=parseFloat(document.getElementById('sm2').value);
  const b2=parseFloat(document.getElementById('sb2').value);
  document.getElementById('sm1v').textContent=m1;
  document.getElementById('sb1v').textContent=b1;
  document.getElementById('sm2v').textContent=m2;
  document.getElementById('sb2v').textContent=b2;
  const scale=20, x1=-8,x2=8;
  function coords(m,b){
    const y1=m*x1+b, y2=m*x2+b;
    return [160+x1*scale,160-y1*scale,160+x2*scale,160-y2*scale];
  }
  const c1=coords(m1,b1), c2=coords(m2,b2);
  const l1=document.getElementById('sysLine1');
  l1.setAttribute('x1',c1[0]);l1.setAttribute('y1',c1[1]);l1.setAttribute('x2',c1[2]);l1.setAttribute('y2',c1[3]);
  const l2=document.getElementById('sysLine2');
  l2.setAttribute('x1',c2[0]);l2.setAttribute('y1',c2[1]);l2.setAttribute('x2',c2[2]);l2.setAttribute('y2',c2[3]);
  const dot=document.getElementById('sysDot');
  const disp=document.getElementById('sysSolutionDisplay');
  if(Math.abs(m1-m2)<1e-9){
    dot.setAttribute('cx',-100); dot.setAttribute('cy',-100);
    disp.textContent = (Math.abs(b1-b2)<1e-9) ? 'Same line → Infinite solutions' : 'Parallel lines → No solution';
  } else {
    const ix = (b2-b1)/(m1-m2);
    const iy = m1*ix+b1;
    dot.setAttribute('cx',160+ix*scale);
    dot.setAttribute('cy',160-iy*scale);
    disp.textContent = `Solution: (${ix.toFixed(2)}, ${iy.toFixed(2)})`;
  }
}
sSliders.forEach(s=>s.oninput=updateSysGraph);
updateSysGraph();

/* ---------- EXERCISES ---------- */
function checkEx1(){
  const v = document.getElementById('ex1input').value.trim();
  const fb = document.getElementById('ex1fb');
  fb.classList.add('show');
  if(v==='1'){
    fb.className='fb show correct'; fb.textContent='Correct! y-3=2(x-1) → y=2x+1, so b=1.';
  } else {
    fb.className='fb show wrong'; fb.textContent='Not quite. y-3=2(x-1) → y=2x-2+3=2x+1 → b=1.';
  }
}
function checkEx2(){
  const v = document.getElementById('ex2input').value.trim();
  const fb = document.getElementById('ex2fb');
  fb.classList.add('show');
  if(v==='6'){
    fb.className='fb show correct'; fb.textContent='Correct! Adding both equations: 2x=12 → x=6, then y=4.';
  } else {
    fb.className='fb show wrong'; fb.textContent='Not quite. Add the equations: (x+y)+(x-y)=10+2 → 2x=12 → x=6.';
  }
}
function checkEx3(){
  const v = document.getElementById('ex3input').value.trim().toLowerCase();
  const fb = document.getElementById('ex3fb');
  fb.classList.add('show');
  if(v==='a'){
    fb.className='fb show correct'; fb.textContent='Correct! Both have slope 3 but different intercepts (2 vs -1) → parallel, no solution.';
  } else {
    fb.className='fb show wrong'; fb.textContent='Not quite. System (a) has matching slopes (3 and 3) with different intercepts — that\\'s the parallel, no-solution case.';
  }
}
function checkEx4(){
  const v = document.getElementById('ex4input').value.trim();
  const fb = document.getElementById('ex4fb');
  fb.classList.add('show');
  if(v==='-3'||v==='-3.0'){
    fb.className='fb show correct'; fb.textContent='Correct! D = (1)(-1) - (2)(1) = -1-2 = -3.';
  } else {
    fb.className='fb show wrong'; fb.textContent='Not quite. D = a1*b2 - a2*b1 = (1)(-1) - (2)(1) = -3.';
  }
}

/* ---------- QUIZZES ---------- */
const quizData = {
  1: [
    {q:"Which of these is a linear equation?", opts:["y = x² + 2","y = 3x - 4","y = 1/x","y = √x + 1"], correct:1, explain:"Linear equations have variables raised only to the first power — y = 3x - 4 fits; the others involve squares, reciprocals, or roots."},
    {q:"Solve for x: 4x - 7 = 9", opts:["x = 2","x = 3","x = 4","x = 16"], correct:2, explain:"4x - 7 = 9 → 4x = 16 → x = 4."},
    {q:"In y = mx + b, what does 'b' represent?", opts:["The slope","The x-intercept","The y-intercept","The domain"], correct:2, explain:"'b' is the y-intercept — the value of y when x = 0."},
    {q:"A line with slope 0 is:", opts:["Vertical","Horizontal","Undefined","Diagonal"], correct:1, explain:"A slope of 0 means no vertical change as x changes — the line is horizontal."}
  ],
  2: [
    {q:"What is the goal when solving a system of equations?", opts:["Find where one equation equals zero","Find values that satisfy all equations simultaneously","Simplify each equation separately","Graph only one line"], correct:1, explain:"A system's solution must satisfy every equation in the system at the same time."},
    {q:"Solve by substitution: y = x + 2, and 2x + y = 11. What is x?", opts:["x = 2","x = 3","x = 4","x = 5"], correct:1, explain:"2x + (x+2) = 11 → 3x + 2 = 11 → 3x = 9 → x = 3."},
    {q:"Elimination works best when:", opts:["One variable is already isolated","Coefficients can be matched to cancel by adding/subtracting","You want a rough visual answer","The system has no solution"], correct:1, explain:"Elimination relies on scaling equations so a variable's coefficients cancel when added or subtracted."},
    {q:"Solve: x - y = 4 and x + y = 10. What is y?", opts:["y = 2","y = 3","y = 4","y = 7"], correct:1, explain:"Adding: 2x = 14 → x = 7. Then y = 10 - 7 = 3."}
  ],
  3: [
    {q:"Two lines with the same slope but different y-intercepts have:", opts:["One solution","No solution","Infinite solutions","Undefined solution"], correct:1, explain:"Same slope + different intercept = parallel lines that never intersect = no solution."},
    {q:"Getting '0 = 0' while solving a system means:", opts:["No solution","Infinite solutions","An error was made","One solution"], correct:1, explain:"A true statement with no variables left (0=0) means the equations describe the same line — infinite solutions."},
    {q:"In a word problem with adult and child tickets, what should you do first?", opts:["Guess the answer", "Clearly define variables for each unknown", "Immediately graph", "Skip to elimination"], correct:1, explain:"Always start word problems by clearly defining what each variable represents."},
    {q:"If a + c = 150 and 12a + 8c = 1560, solving gives a = 90. What is c?", opts:["40","50","60","70"], correct:2, explain:"c = 150 - a = 150 - 90 = 60."}
  ],
  4: [
    {q:"In AX = B, what does the matrix A represent?", opts:["The variables","The coefficients","The constants","The solutions"], correct:1, explain:"A holds the coefficients of the variables from each equation."},
    {q:"Cramer's Rule uses which mathematical concept?", opts:["Derivatives","Determinants","Integrals","Logarithms"], correct:1, explain:"Cramer's Rule computes solutions using determinants (D, Dx, Dy)."},
    {q:"For 2x + 3y = 8 and x - y = 1, D = a1*b2 - a2*b1 equals:", opts:["-5","5","1","-1"], correct:0, explain:"D = (2)(-1) - (1)(3) = -2 - 3 = -5."},
    {q:"Why do matrices matter for large systems?", opts:["They make equations linear", "They allow computers to efficiently process many equations at once", "They eliminate the need for variables", "They only work for 2 variables"], correct:1, explain:"Matrices let computers systematically process rows/columns, scaling efficiently to many equations and variables."}
  ]
};

function buildQuiz(n){
  const card = document.getElementById('quiz'+n+'card');
  const data = quizData[n];
  let html = `<h2>📝 Module ${n} Quiz</h2><p class="subtitle">Answer all 4 questions. You'll get instant feedback and an explanation for each.</p>`;
  data.forEach((item,qi)=>{
    html += `<div class="quiz-q" data-qi="${qi}">
      <p><b>Q${qi+1}.</b> ${item.q}</p>`;
    item.opts.forEach((opt,oi)=>{
      html += `<button class="quiz-opt" onclick="answerQuiz(${n},${qi},${oi},this)">${opt}</button>`;
    });
    html += `<div class="quiz-explain" id="explain-${n}-${qi}">${item.explain}</div></div>`;
  });
  html += `<div id="quizResult-${n}"></div>`;
  card.innerHTML = html;
  card.dataset.answers = JSON.stringify(new Array(data.length).fill(null));
}

function goToQuiz(n){
  buildQuiz(n);
  showModule(n);
  setTimeout(()=>{document.getElementById('quiz'+n+'card').scrollIntoView({behavior:'smooth'});},300);
}

function answerQuiz(n,qi,oi,btn){
  const card = document.getElementById('quiz'+n+'card');
  const answers = JSON.parse(card.dataset.answers);
  if(answers[qi]!==null) return; // already answered
  answers[qi]=oi;
  card.dataset.answers = JSON.stringify(answers);
  const qBlock = card.querySelector(`.quiz-q[data-qi="${qi}"]`);
  const opts = qBlock.querySelectorAll('.quiz-opt');
  const correct = quizData[n][qi].correct;
  opts.forEach((o,idx)=>{
    o.disabled = true;
    if(idx===correct) o.classList.add('correct');
    else if(idx===oi) o.classList.add('incorrect');
  });
  document.getElementById(`explain-${n}-${qi}`).classList.add('show');

  if(answers.every(a=>a!==null)){
    finishQuiz(n,answers);
  }
}

function finishQuiz(n,answers){
  let score=0;
  answers.forEach((a,qi)=>{ if(a===quizData[n][qi].correct) score++; });
  state.quizScores[n]=score;
  const xpEarned = score*25;
  state.xp += xpEarned;
  document.getElementById('xp'+n).textContent = xpEarned+' XP';
  const resultDiv = document.getElementById('quizResult-'+n);
  let msg = score===4 ? "Perfect score! You've mastered this module." :
            score>=3 ? "Great work! Solid understanding." :
            score>=2 ? "Good effort — consider reviewing the explanations above." :
            "Review the module content above, then feel free to retry your understanding.";
  resultDiv.innerHTML = `<div class="quiz-summary">
    <div class="score">${score}/4</div>
    <p>${msg}</p>
    <p class="subtitle">+${xpEarned} XP earned</p>
    <div class="btn-row" style="justify-content:center;">
      <button class="btn" onclick="unlockNext(${n})">Continue →</button>
    </div>
  </div>`;
  updateProgress();
  launchConfetti();
}

function unlockNext(n){
  if(n<4){
    showModule(n+1);
  } else {
    showModule('Final');
  }
}

function completeCourse(){
  const totalScore = Object.values(state.quizScores).reduce((a,b)=>a+(b||0),0);
  const card = document.getElementById('certificateCard');
  card.style.display='block';
  card.innerHTML = `<h2>🎓 Certificate of Completion</h2>
    <p class="subtitle">This certifies that you have completed the <b>Linear Equations & Systems</b> Interactive Learning Studio.</p>
    <div class="stat-grid">
      <div class="stat"><div class="num">${state.xp} XP</div><div class="lbl">Total earned</div></div>
      <div class="stat"><div class="num">${totalScore}/16</div><div class="lbl">Quiz questions correct</div></div>
      <div class="stat"><div class="num">4/4</div><div class="lbl">Modules completed</div></div>
    </div>
    <p class="subtitle">🎉 Congratulations — print this page to save your notes and certificate!</p>`;
  card.scrollIntoView({behavior:'smooth'});
  launchConfetti(30);
}

function launchConfetti(count=16){
  const wrap = document.createElement('div');
  wrap.className='confetti';
  document.body.appendChild(wrap);
  const emojis=['🎉','✨','⭐','🎊','🏆'];
  for(let i=0;i<count;i++){
    const s=document.createElement('span');
    s.textContent = emojis[Math.floor(Math.random()*emojis.length)];
    s.style.left = Math.random()*100+'vw';
    s.style.animationDuration = (2+Math.random()*2)+'s';
    s.style.fontSize = (14+Math.random()*14)+'px';
    wrap.appendChild(s);
  }
  setTimeout(()=>wrap.remove(),4000);
}

document.getElementById('revealBtn').onclick = function(){
  document.getElementById('finalSolution').style.display='block';
  this.disabled=true;
};

updateProgress();
</script>
</body>
</html>
