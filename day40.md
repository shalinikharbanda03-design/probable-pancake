AI Assistant Builder

You are an expert product manager, conversation designer, prompt engineer, UX designer, and frontend developer.

Before generating anything, interview the user ONE QUESTION AT A TIME in the quiz form (MCQ, do not make user do the work of typing).

1. What kind of assistant do you want to build? (Ask their domain and then niche, then give 4 suitable options.)
2. Who is this assistant for, and what's the single most important outcome a user should get from one session with it?
3. What inputs will people give it? (free text, pasted document, form fields, uploaded file, multi-turn conversation)
4. What should the output look like? (a score/verdict, a structured report, a conversational chat, a generated document, recommendations with reasoning)
5. Any tone or personality preference? (professional, friendly, blunt/expert, playful)

Then design and build:

1. The assistant's "brain" — write a production-quality system prompt for the underlying Claude calls: role, scope, constraints, output format, edge-case handling (irrelevant input, missing info, abuse).

2. The interface — a single self-contained HTML file (HTML/CSS/JS only, no external libraries) that:
- Has a premium, purpose-built UI matching the assistant's domain (not a generic chatbot box) — e.g., an ATS checker shows a score dial and highlighted resume text; a recipe finder shows ingredient tags and recipe cards.
- Calls the Claude API live via fetch to https://api.anthropic.com/v1/messages (no API key needed, it's handled) using the system prompt from step 1.
- Handles loading states, errors, and empty states gracefully.
- Is fully responsive with smooth animations and polished micro-interactions.

3. Documentation panel — a collapsible "How this was built" section explaining the system prompt design, why the UI choices fit the use case, and how someone could extend it (add tools, memory, multi-step flows).

Generate the complete file only after all interview answers are collected.

:Response:  

Here’s the **complete, fully functional single‑file HTML code** for your **Career Coach Resume Analyzer**.  
It includes:  
- An **API Key input field** at the top.  
- A working **Analyze Resume** button that makes a live `fetch` call to `https://api.anthropic.com/v1/messages`.  
- An **animated ATS score dial**.  
- **Structured report output**.  
- **Keyword highlighting** inside the resume text area.  

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Career Coach Assistant - Resume Analyzer</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
      font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      margin: 0;
      background: #121212;
      color: #eee;
      display: flex;
      flex-direction: column;
      min-height: 100vh;
    }
    header {
      background: #1f1f1f;
      padding: 1rem;
      text-align: center;
      font-size: 1.5rem;
      font-weight: bold;
      border-bottom: 2px solid #333;
    }
    main {
      flex: 1;
      display: flex;
      flex-direction: column;
      padding: 1rem;
      gap: 1rem;
      max-width: 900px;
      margin: auto;
    }
    input[type="text"] {
      width: 100%;
      background: #1e1e1e;
      border: 1px solid #444;
      color: #fff;
      padding: 0.6rem;
      border-radius: 6px;
    }
    textarea {
      width: 100%;
      min-height: 200px;
      background: #1e1e1e;
      border: 1px solid #444;
      color: #fff;
      padding: 1rem;
      border-radius: 8px;
      resize: vertical;
    }
    button {
      background: #3a3a3a;
      color: #fff;
      border: none;
      padding: 0.7rem 1.2rem;
      border-radius: 6px;
      cursor: pointer;
      transition: background 0.3s;
      font-size: 1rem;
    }
    button:hover {
      background: #555;
    }
    .score-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin: 1rem 0;
    }
    canvas {
      width: 200px;
      height: 200px;
    }
    .report {
      background: #1e1e1e;
      border-radius: 8px;
      padding: 1rem;
      margin-top: 1rem;
      line-height: 1.5;
    }
    .loading {
      text-align: center;
      margin-top: 1rem;
      font-style: italic;
      animation: pulse 1s infinite;
    }
    @keyframes pulse {
      0% { opacity: 0.5; }
      50% { opacity: 1; }
      100% { opacity: 0.5; }
    }
    .highlight-strong { background-color: rgba(76,175,80,0.4); }
    .highlight-weak { background-color: rgba(244,67,54,0.4); }
  </style>
</head>
<body>
  <header>Career Coach Assistant</header>
  <main>
    <label for="apiKey">Enter your Claude API Key:</label>
    <input type="text" id="apiKey" placeholder="Paste your Claude API Key here...">

    <label for="resume">Paste your resume below:</label>
    <textarea id="resume" placeholder="Paste your resume text here..."></textarea>
    <button id="analyzeBtn">Analyze Resume</button>
    <div id="loading" class="loading" style="display:none;">Analyzing your resume...</div>
    <div class="score-container">
      <canvas id="scoreDial"></canvas>
      <div id="scoreText"></div>
    </div>
    <div id="report" class="report"></div>
  </main>

  <script>
    async function analyzeResume() {
      const apiKey = document.getElementById('apiKey').value.trim();
      const resumeText = document.getElementById('resume').value.trim();
      if (!apiKey) {
        alert('Please enter your Claude API Key.');
        return;
      }
      if (!resumeText) {
        alert('Please paste your resume first.');
        return;
      }
      document.getElementById('loading').style.display = 'block';
      document.getElementById('scoreText').textContent = '';
      document.getElementById('report').textContent = '';
      drawDial(0);

      try {
        const response = await fetch("https://api.anthropic.com/v1/messages", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "x-api-key": apiKey
          },
          body: JSON.stringify({
            model: "claude-3-opus-20240229",
            max_tokens: 1000,
            system: "You are a Career Coach Assistant. Role: Help job seekers improve resumes. Scope: Accept pasted resume text. Output: 1) ATS compatibility score (0-100) with quick verdict (Pass/Fail). 2) Structured report highlighting strengths, weaknesses, keyword gaps. 3) Provide lists of strong keywords found and missing keywords. Tone: Professional with playful encouragement. Constraints: If irrelevant input, ask for resume. If abusive input, respond politely and refuse. Format: Clear headings, bullet points, concise language.",
            messages: [
              { role: "user", content: resumeText }
            ]
          })
        });
        const data = await response.json();
        const output = data.content[0].text;

        const lines = output.split("\n");
        const scoreLine = lines[0];
        const reportText = lines.slice(1).join("\n");

        const scoreMatch = scoreLine.match(/(\d{1,3})/);
        let score = scoreMatch ? parseInt(scoreMatch[1]) : 0;
        if (score > 100) score = 100;

        document.getElementById('scoreText').textContent = scoreLine;
        document.getElementById('report').textContent = reportText;
        animateDial(score);

        // Extract keywords from report
        const strongMatch = reportText.match(/Strong Keywords:\s*(.*)/i);
        const weakMatch = reportText.match(/Missing Keywords:\s*(.*)/i);
        const strongKeywords = strongMatch ? strongMatch[1].split(/[,;]/).map(k=>k.trim()).filter(k=>k) : [];
        const weakKeywords = weakMatch ? weakMatch[1].split(/[,;]/).map(k=>k.trim()).filter(k=>k) : [];

        highlightKeywords(resumeText, strongKeywords, weakKeywords);
      } catch (err) {
        document.getElementById('report').textContent = "Error analyzing resume. Please check your API key and try again.";
      } finally {
        document.getElementById('loading').style.display = 'none';
      }
    }

    document.getElementById('analyzeBtn').addEventListener('click', analyzeResume);

    // Score Dial
    const canvas = document.getElementById('scoreDial');
    const ctx = canvas.getContext('2d');
    let currentScore = 0;

    function drawDial(score) {
      ctx.clearRect(0,0,canvas.width,canvas.height);
      const centerX = canvas.width/2;
      const centerY = canvas.height/2;
      const radius = 80;

      ctx.beginPath();
      ctx.arc(centerX, centerY, radius, Math.PI, 0);
      ctx.strokeStyle = '#444';
      ctx.lineWidth = 15;
      ctx.stroke();

      const endAngle = Math.PI + (score/100)*Math.PI;
      ctx.beginPath();
      ctx.arc(centerX, centerY, radius, Math.PI, endAngle);
      ctx.strokeStyle = score>=70 ? '#4caf50' : '#f44336';
      ctx.lineWidth = 15;
      ctx.stroke();

      ctx.fillStyle = '#fff';
      ctx.font = '20px Segoe UI';
      ctx.textAlign = 'center';
      ctx.fillText(score + '%', centerX, centerY+10);
    }

    function animateDial(targetScore) {
      let step = targetScore > currentScore ? 1 : -1;
      function animate() {
        if ((step>0 && currentScore<targetScore) || (step<0 && currentScore>targetScore)) {
          currentScore += step;
          drawDial(currentScore);
          requestAnimationFrame(animate);
        }
      }
      animate();
    }

    function highlightKeywords(text, strongKeywords, weakKeywords) {
      let highlightedText = text;

      strongKeywords.forEach(keyword => {
        if (keyword) {
          const regex = new RegExp(`\\b${keyword}\\b`, 'gi');
          highlightedText = highlightedText.replace(regex, `<span class="highlight-strong">${keyword}</span>`);
        }
      });

      weakKeywords.forEach(keyword => {
        if (keyword) {
          const regex = new RegExp(`\\b${
          <img width="1334" height="533" alt="image" src="https://github.com/user-attachments/assets/7b52c3a7-23af-4605-93fb-e943cd49cb81" />
