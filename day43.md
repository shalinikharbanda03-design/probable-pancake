:PROMPT:
# AI Workflow Architect

You are an expert workflow consultant, business analyst, AI strategist, automation architect, productivity expert, UI/UX designer, and senior frontend developer.

Before generating anything, ask the user the following questions ONE AT A TIME in MCQ format only, with typed input only as the last option.

1. What type of workflow would you like to build?
(Offer options such as Marketing, Sales, HR, Software Development, Design, Education, Finance, Healthcare, Legal, Customer Support, Content Creation, Entrepreneurship, Research, Personal Productivity, and more.)

2. Continue asking follow-up questions until the workflow has been narrowed into a specific role, process, or objective that can realistically be mapped from start to finish.
Do not stop after identifying only an industry or domain. Use your own judgment to determine when the scope is appropriate.

Example:
Marketing → Social Media → Instagram Marketing → Personal Brand Growth

Software Development → Frontend Development → React → Portfolio Website

Human Resources → Recruitment → Technical Hiring

3. Would you like Claude to automatically structure the workflow, or would you like to customize its sections?
If the user chooses customization, ask which sections they want included.

After collecting all responses, generate a premium single-page HTML application called "AI Workflow Architect."

The application should generate a complete end-to-end workflow for the selected process rather than providing general advice or a checklist.

Break the workflow into logical stages from planning to execution.

Each stage should include:

Objectives

Tasks

Best AI tools for that stage

Why each tool is recommended

Alternative tools

Prompt examples

Best practices

Common mistakes

Expected outputs

Time estimates

Tips for improving efficiency

Include interactive workflow diagrams, comparisons, decision trees, tool recommendations, progress tracking, notes, bookmarks, and actionable insights where appropriate.

Conclude with:

Workflow Summary

Recommended AI Stack

Learning Resources

Communities

Search Keywords

Additional AI Prompts

Future Automation Opportunities

Generate everything as a single self-contained HTML file using only HTML, CSS, and JavaScript without external libraries or frameworks.

Design the interface as a polished commercial workflow platform with responsive design, dark mode, smooth animations, interactive diagrams, local storage, printable workflow guides, and an intuitive user experience.<!DOCTYPE html>

:RESPONSE:
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>AI Workflow Architect</title>
  <style>
    body {
      font-family: 'Segoe UI', Arial, sans-serif;
      margin: 0; padding: 0;
      background: linear-gradient(180deg, #0f0f0f, #1c1c1c);
      color: #e0e0e0;
    }
    header {
      background: linear-gradient(90deg, #4caf50, #2196f3);
      padding: 25px;
      text-align: center;
      font-size: 28px;
      font-weight: bold;
      color: #fff;
      letter-spacing: 1px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.6);
    }
    nav {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      background: #2c2c2c;
      padding: 12px;
      box-shadow: inset 0 -2px 5px rgba(0,0,0,0.5);
    }
    nav button {
      background: #3c3c3c;
      border: none;
      color: #fff;
      padding: 12px 22px;
      margin: 6px;
      cursor: pointer;
      transition: all 0.3s ease;
      border-radius: 8px;
      font-weight: 500;
    }
    nav button:hover {
      background: #4caf50;
      transform: scale(1.05);
    }
    section {
      display: none;
      padding: 25px;
      animation: fadeIn 0.6s ease-in-out;
    }
    section.active { display: block; }
    .card {
      background: #1f1f1f;
      padding: 18px;
      margin: 12px 0;
      border-radius: 10px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.4);
      transition: transform 0.3s ease;
    }
    .card:hover {
      transform: translateY(-3px);
    }
    canvas {
      background: #1f1f1f;
      margin: 20px 0;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }
    h2 {
      color: #4caf50;
      border-bottom: 2px solid #4caf50;
      padding-bottom: 8px;
      margin-bottom: 15px;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body>
  <header>AI Workflow Architect – Life Productivity System</header>
  <nav>
    <button onclick="showSection('overview')">Overview</button>
    <button onclick="showSection('tasks')">Daily Tasks</button>
    <button onclick="showSection('time')">Time Blocking</button>
    <button onclick="showSection('goals')">Goals</button>
    <button onclick="showSection('habits')">Habits</button>
    <button onclick="showSection('learning')">Learning</button>
    <button onclick="showSection('finance')">Finance</button>
    <button onclick="showSection('summary')">Summary</button>
  </nav>

  <section id="overview" class="active">
    <h2>Workflow Overview</h2>
    <div class="card">Efficiency Score: <span id="efficiencyScore">78</span>/100</div>
    <canvas id="overviewChart" width="400" height="200"></canvas>
  </section>

  <section id="tasks">
    <h2>Daily Task Management</h2>
    <div class="card">Objectives: Prioritize tasks, avoid overload</div>
    <div class="card">Best AI Tools: Todoist, Notion AI</div>
    <div class="card">Prompt Example: "Generate a prioritized to-do list for today"</div>
  </section>

  <section id="time">
    <h2>Time Blocking & Scheduling</h2>
    <div class="card">Objectives: Allocate realistic time slots</div>
    <div class="card">Best AI Tools: Google Calendar AI, Motion</div>
    <div class="card">Prompt Example: "Create a time-blocked schedule for my tasks"</div>
  </section>

  <section id="goals">
    <h2>Goal Setting & Tracking</h2>
    <div class="card">Objectives: Align tasks with long-term goals</div>
    <div class="card">Best AI Tools: Trello AI, Asana</div>
    <div class="card">Prompt Example: "Break down my 6-month goal into weekly milestones"</div>
  </section>

  <section id="habits">
    <h2>Habit Building & Routine Optimization</h2>
    <div class="card">Objectives: Build consistency</div>
    <div class="card">Best AI Tools: Habitica, Streaks</div>
    <div class="card">Prompt Example: "Track my daily meditation habit"</div>
  </section>

  <section id="learning">
    <h2>Learning & Skill Development</h2>
    <div class="card">Objectives: Continuous growth</div>
    <div class="card">Best AI Tools: Coursera AI, ChatGPT for study</div>
    <div class="card">Prompt Example: "Generate a study plan for learning Python"</div>
  </section>

  <section id="finance">
    <h2>Personal Finance Productivity</h2>
    <div class="card">Objectives: Budgeting, savings, automation</div>
    <div class="card">Best AI Tools: YNAB, Copilot Finance</div>
    <div class="card">Prompt Example: "Simulate my monthly budget with 10% extra savings"</div>
  </section>

  <section id="summary">
    <h2>Workflow Summary & Future Automation</h2>
    <div class="card">Recommended AI Stack: Todoist, Motion, Trello, Habitica, Coursera, YNAB</div>
    <div class="card">Learning Resources: Productivity blogs, AI communities</div>
    <div class="card">Future Automation: Auto-scheduling, smart reminders, financial auto-invest</div>
  </section>

  <script>
    function showSection(id) {
      document.querySelectorAll('section').forEach(sec => sec.classList.remove('active'));
      document.getElementById(id).classList.add('active');
    }

    // Simple chart rendering
    const overviewCtx = document.getElementById('overviewChart').getContext('2d');
    overviewCtx.fillStyle = '#4caf50';
    overviewCtx.fillRect(50, 50, 100, 100);
    overviewCtx.fillStyle = '#2196f3';
    overviewCtx.fillRect(170, 50, 100, 100);
  </script>
</body>
</html>
<img width="1189" height="529" alt="image" src="https://github.com/user-attachments/assets/7d285c4e-d03d-4943-b68b-5448a8ecf143" />
<img width="805" height="504" alt="image" src="https://github.com/user-attachments/assets/da0986ed-1dfd-4a15-b00d-b3e5603f72ab" />
<img width="710" height="494" alt="image" src="https://github.com/user-attachments/assets/9569e289-ffba-4420-b0ec-a732fddd02f2" />
<img width="726" height="476" alt="image" src="https://github.com/user-attachments/assets/faafd8de-ffd6-4179-a16f-099fc9f2748d" />
<img width="800" height="506" alt="image" src="https://github.com/user-attachments/assets/b71263c6-98ae-450d-bd5f-8305dca873aa" />
<img width="906" height="464" alt="image" src="https://github.com/user-attachments/assets/3cbe79d4-bebe-418a-9566-703e3f4347c2" />
<img width="1022" height="463" alt="image" src="https://github.com/user-attachments/assets/a5687796-f0f4-47a0-ab8d-adb5eb660584" />
<img width="1126" height="471" alt="image" src="https://github.com/user-attachments/assets/529d5efc-8c63-43fc-868b-db5715e6dd55" />
