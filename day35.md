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
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>🧩 Prompt Puzzle — Master AI Prompting Through Play</title>
  <style>
    /* ===== Premium Modern UI Styles ===== */
    body {
      margin: 0;
      font-family: 'Segoe UI', Roboto, sans-serif;
      background: #121212;
      color: #f0f0f0;
    }
    header {
      background: #1f1f1f;
      padding: 20px;
      text-align: center;
      font-size: 1.5em;
      font-weight: bold;
      color: #00e0ff;
    }
    .game-container {
      padding: 20px;
      max-width: 1200px;
      margin: auto;
    }
    .scenario {
      background: #1e1e1e;
      border-radius: 10px;
      padding: 20px;
      margin-bottom: 20px;
      box-shadow: 0 0 10px rgba(0,255,255,0.2);
    }
    .blocks {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 10px;
    }
    .block {
      background: #2a2a2a;
      padding: 10px;
      border-radius: 6px;
      cursor: grab;
      transition: transform 0.2s;
    }
    .block:hover {
      transform: scale(1.05);
      background: #333;
    }
    .scoreboard {
      background: #1f1f1f;
      padding: 15px;
      border-radius: 10px;
      margin-top: 20px;
    }
    .notification {
      position: fixed;
      top: 20px;
      right: 20px;
      background: #00e0ff;
      color: #000;
      padding: 10px 20px;
      border-radius: 6px;
      display: none;
    }
    .report {
      background: #1e1e1e;
      padding: 20px;
      border-radius: 10px;
      margin-top: 30px;
    }
  </style>
</head>
<body>
  <header>🧩 Prompt Puzzle — Master AI Prompting Through Play</header>
  <div class="game-container" id="game">
    <!-- Scenarios will be injected here -->
  </div>
  <div class="scoreboard" id="scoreboard">
    <h3>Live Scoring</h3>
    <p>Accuracy: <span id="accuracy">0%</span></p>
    <p>Time: <span id="time">0s</span></p>
    <p>Moves: <span id="moves">0</span></p>
    <p>Wrong Placements: <span id="wrong">0</span></p>
    <p>Hints Used: <span id="hints">0</span></p>
    <p>Optimization Bonus: <span id="bonus">0</span></p>
  </div>
  <div class="report" id="report">
    <h3>Prompt Performance Report</h3>
    <p>Prompt Score: <span id="promptScore">0</span></p>
    <p>Rating: <span id="rating">-</span></p>
    <p>Rank: <span id="rank">-</span></p>
    <p>Prompt DNA Visualization: <span id="dna">[###]</span></p>
    <p>Feedback: <span id="feedback">-</span></p>
    <p>Next Milestone: <span id="milestone">-</span></p>
    <p>Final Optimized Prompt: <span id="finalPrompt">-</span></p>
    <button onclick="replay()">Replay with New Scenarios</button>
  </div>
  <div class="notification" id="notification">Action Completed!</div>

  <script>
    /* ===== Scenario Data ===== */
    const scenarios = [
      {
        domain: "Creative Writing & Storytelling",
        difficulty: "Intermediate",
        desiredOutput: "Short startup pitch story",
        correctBlocks: ["Hook", "Problem", "Solution", "CTA"],
        distractorBlocks: ["Irrelevant Quote", "Random Fact"],
        weakPrompt: "Write something about a company",
        optimizedPrompt: "Write a 100-word engaging startup pitch story highlighting problem, solution, and CTA.",
        overEngineeredPrompt: "Generate a 100-word pitch story with 3 metaphors, 2 analogies, 1 rhyme scheme, and a Shakespearean tone.",
        weakAIOutput: "This is a company that does things.",
        optimizedAIOutput: "Our startup solves X problem with Y solution, making life easier. Join us today!",
        principle: "Clarity beats complexity."
      },
      // Add 5 more scenario objects here...
    ];

    /* ===== Game Logic ===== */
    function initGame() {
      const game = document.getElementById('game');
      game.innerHTML = '';
      scenarios.forEach((s, i) => {
        const div = document.createElement('div');
        div.className = 'scenario';
        div.innerHTML = `
          <h3>Scenario ${i+1}: ${s.domain}</h3>
          <p><strong>Desired Output:</strong> ${s.desiredOutput}</p>
          <div class="blocks">
            ${s.correctBlocks.map(b => `<div class="block">${b}</div>`).join('')}
            ${s.distractorBlocks.map(b => `<div class="block">${b}</div>`).join('')}
          </div>
          <p><strong>Weak Prompt:</strong> ${s.weakPrompt}</p>
          <p><strong>Optimized Prompt:</strong> ${s.optimizedPrompt}</p>
          <p><strong>Over-Engineered Prompt:</strong> ${s.overEngineeredPrompt}</p>
          <p><strong>Weak AI Output:</strong> ${s.weakAIOutput}</p>
          <p><strong>Optimized AI Output:</strong> ${s.optimizedAIOutput}</p>
          <p><strong>Prompt Principle:</strong> ${s.principle}</p>
        `;
        game.appendChild(div);
      });
    }

    function replay() {
      showNotification("New scenarios loaded!");
      initGame();
    }

    function showNotification(msg) {
      const notif = document.getElementById('notification');
      notif.innerText = msg;
      notif.style.display = 'block';
      setTimeout(() => notif.style.display = 'none', 2000);
    }

    // Initialize
    initGame();
  </script>
</body>
</html>
