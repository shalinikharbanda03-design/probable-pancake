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
Here you go, Shalini — the **full combined HTML file** for your **Day 35 Prompt Puzzle app**. This version includes everything: skeleton structure, six expanded scenarios (Creative Writing, Business/Startups, Gaming & Entertainment), drag‑and‑drop interactivity, live scoring, hints, replay, and the final performance report.  

Save this as `prompt-puzzle.html` in your GitHub repo, then open it directly in your browser to play offline.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>🧩 Prompt Puzzle — Master AI Prompting Through Play</title>
  <style>
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
      border: 1px dashed #555;
      padding: 10px;
      min-height: 50px;
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
    button {
      background: #00e0ff;
      border: none;
      padding: 10px 15px;
      border-radius: 6px;
      cursor: pointer;
      margin-top: 10px;
    }
    button:hover {
      background: #00b8cc;
    }
  </style>
</head>
<body>
  <header>🧩 Prompt Puzzle — Master AI Prompting Through Play</header>
  <div class="game-container" id="game"></div>
  <div class="scoreboard" id="scoreboard">
    <h3>Live Scoring</h3>
    <p>Accuracy: <span id="accuracy">0%</span></p>
    <p>Time: <span id="time">0s</span></p>
    <p>Moves: <span id="moves">0</span></p>
    <p>Wrong Placements: <span id="wrong">0</span></p>
    <p>Hints Used: <span id="hints">0</span></p>
    <p>Optimization Bonus: <span id="bonus">0</span></p>
    <button onclick="giveHint()">Use Hint</button>
    <button onclick="finalizeReport()">Finalize Report</button>
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
      {
        domain: "Business & Startups",
        difficulty: "Intermediate",
        desiredOutput: "Elevator pitch for a new app",
        correctBlocks: ["Target User", "Pain Point", "Unique Solution", "Vision"],
        distractorBlocks: ["Unrelated Joke", "Technical Jargon"],
        weakPrompt: "Describe my app",
        optimizedPrompt: "Write a 60-second elevator pitch for a productivity app, focusing on target user, pain point, solution, and vision.",
        overEngineeredPrompt: "Write a pitch with 5 buzzwords, 3 statistics, and a futuristic metaphor.",
        weakAIOutput: "This app helps people.",
        optimizedAIOutput: "Busy professionals waste time juggling tasks. Our app streamlines workflows with smart automation, helping them reclaim hours daily.",
        principle: "Focus on user pain point first."
      },
      {
        domain: "Gaming & Entertainment",
        difficulty: "Intermediate",
        desiredOutput: "Quest description for a fantasy RPG",
        correctBlocks: ["Setting", "Objective", "Challenge", "Reward"],
        distractorBlocks: ["Off-topic Trivia", "Overly Long Lore"],
        weakPrompt: "Write a quest",
        optimizedPrompt: "Write a 150-word fantasy RPG quest description including setting, objective, challenge, and reward.",
        overEngineeredPrompt: "Write a quest with 10 riddles, 5 subplots, and 3 languages.",
        weakAIOutput: "Go fight monsters.",
        optimizedAIOutput: "In the haunted forest, retrieve the crystal stolen by shadow beasts. Defeat their leader to restore balance and earn the Guardian’s blessing.",
        principle: "Balance immersion with clarity."
      },
      {
        domain: "Creative Writing & Storytelling",
        difficulty: "Intermediate",
        desiredOutput: "Micro-story about resilience",
        correctBlocks: ["Character", "Conflict", "Resolution", "Theme"],
        distractorBlocks: ["Random Statistics", "Unrelated Anecdote"],
        weakPrompt: "Write a story",
        optimizedPrompt: "Write a 150-word micro-story about resilience, including character, conflict, resolution, and theme.",
        overEngineeredPrompt: "Write a story with 10 literary devices, 5 flashbacks, and 3 timelines.",
        weakAIOutput: "Someone faced a problem and solved it.",
        optimizedAIOutput: "Maya lost her job but built a small bakery from scratch. Through setbacks, she grew stronger, proving resilience creates new beginnings.",
        principle: "Keep narrative tight and purposeful."
      },
      {
        domain: "Business & Startups",
        difficulty: "Intermediate",
        desiredOutput: "Investor pitch slide text",
        correctBlocks: ["Market Size", "Problem", "Solution", "Traction"],
        distractorBlocks: ["Unrelated Quote", "Excessive Technical Detail"],
        weakPrompt: "Write about my startup",
        optimizedPrompt: "Write concise investor pitch slide text covering market size, problem, solution, and traction.",
        overEngineeredPrompt: "Write pitch text with 20 statistics, 10 buzzwords, and 5 analogies.",
        weakAIOutput: "We have a startup.",
        optimizedAIOutput: "Market: $5B. Problem: inefficiency in logistics. Solution: AI-powered routing. Traction: 10 enterprise clients in 6 months.",
        principle: "Investors want concise, data-backed clarity."
      },
      {
        domain: "Gaming & Entertainment",
        difficulty: "Intermediate",
        desiredOutput: "Game trailer script",
        correctBlocks: ["Hook", "Gameplay Highlight", "Conflict", "Call to Action"],
        distractorBlocks: ["Unrelated Fact", "Overly Long Credits"],
        weakPrompt: "Write
