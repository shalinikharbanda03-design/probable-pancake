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

:Format: HTML, CSS
Module 1: Foundations for your German Everyday Phrases Interactive Learning Studio.

Here’s the HTML code for Module 1 only, structured with explanations, examples, analogies, diagrams, exercises, misconceptions, key takeaways, and a quiz placeholder. It’s designed to slot into the full single‑page app later:

Module 1: Foundations for your German Everyday Phrases Interactive Learning Studio.


:Response:
<div class="module" id="module1">
  <div class="card">
    <div class="module-header">
      <div><span class="module-tag">Module 1 · Foundations</span><h2>Greetings & Introductions</h2></div>
      <span class="pill" id="xp1">0 XP</span>
    </div>
    <p class="subtitle">We start with the most essential German phrases for everyday use: greetings, polite expressions, and introductions.</p>

    <div class="section">
      <h3>📖 Explanation</h3>
      <p>In German, greetings vary depending on the time of day and level of formality. Common phrases include:</p>
      <ul>
        <li><b>Hallo</b> — Hello (informal)</li>
        <li><b>Guten Morgen</b> — Good morning</li>
        <li><b>Guten Tag</b> — Good day</li>
        <li><b>Guten Abend</b> — Good evening</li>
        <li><b>Wie geht’s?</b> — How are you? (informal)</li>
        <li><b>Wie geht es Ihnen?</b> — How are you? (formal)</li>
      </ul>
    </div>

    <div class="section">
      <h3>🧮 Example Dialogue</h3>
      <div class="example-box">
        <b>Anna:</b> Guten Morgen!<br>
        <b>Ben:</b> Guten Morgen, Anna. Wie geht’s?<br>
        <b>Anna:</b> Mir geht’s gut, danke. Und dir?<br>
        <b>Ben:</b> Auch gut!
      </div>
    </div>

    <div class="section">
      <h3>💡 Analogy</h3>
      <div class="analogy-box">Think of greetings as the “handshake” of conversation. Just as you wouldn’t skip shaking hands in a formal meeting, you wouldn’t skip saying <b>Hallo</b> or <b>Guten Tag</b> in German — it sets the tone for respect and friendliness.</div>
    </div>

    <div class="section">
      <h3>📊 Diagram: Formal vs Informal</h3>
      <div class="diagram-wrap">
        <svg viewBox="0 0 320 160" width="320" height="160">
          <rect x="20" y="40" width="120" height="60" fill="var(--accent)" rx="8"/>
          <text x="80" y="75" fill="#fff" text-anchor="middle">Formal</text>
          <rect x="180" y="40" width="120" height="60" fill="var(--accent2)" rx="8"/>
          <text x="240" y="75" fill="#fff" text-anchor="middle">Informal</text>
        </svg>
      </div>
      <p class="subtitle">Formal greetings (e.g., <b>Guten Tag</b>, <b>Wie geht es Ihnen?</b>) are used with strangers, elders, or in professional settings. Informal greetings (e.g., <b>Hallo</b>, <b>Wie geht’s?</b>) are used with friends and family.</p>
    </div>

    <div class="section">
      <h3>✏️ Practical Exercise</h3>
      <div class="exercise">
        <p>Fill in the blank: You meet your professor in the morning. The correct greeting is <b>_____ Morgen</b>.</p>
        <input type="text" id="ex1input" placeholder="Enter phrase">
        <button class="btn secondary" onclick="checkEx1()">Check</button>
        <div class="fb" id="ex1fb"></div>
      </div>
    </div>

    <div class="section">
      <h3>⚠️ Common Misconception</h3>
      <div class="misconception-box">Many learners think <b>Hallo</b> works everywhere. In fact, using <b>Hallo</b> with a professor or in a job interview may sound too casual. Use <b>Guten Tag</b> or <b>Guten Morgen</b> instead.</div>
    </div>

    <div class="section">
      <h3>🔑 Key Takeaways</h3>
      <div class="takeaway-box">
        <ul style="margin:0;padding-left:18px;">
          <li>German greetings change with time of day and formality.</li>
          <li><b>Hallo</b> is informal; <b>Guten Tag</b> is formal.</li>
          <li>Always match the greeting to the context — respect matters in German culture.</li>
        </ul>
      </div>
    </div>

    <div class="btn-row"><button class="btn" onclick="goToQuiz(1)">Take Module 1 Quiz →</button></div>
  </div>

  <div class="card" id="quiz1card"></div>
</div>

:Module 1: Javascript

<script>
function goToQuiz(moduleNum) {
  if (moduleNum === 1) {
    const quizCard = document.getElementById("quiz1card");
    quizCard.innerHTML = `
      <div class="card">
        <h3>📝 Module 1 Quiz — Greetings & Introductions</h3>

        <div class="quiz-q">
          <p>1. What is the formal way to say "Good morning" in German?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! Guten Morgen is formal.')">Guten Morgen</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Hallo is informal.')">Hallo</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Servus is regional, not standard.')">Servus</button>
        </div>

        <div class="quiz-q">
          <p>2. Which phrase would you use with a professor?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! Guten Tag is formal.')">Guten Tag</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Hallo is too casual.')">Hallo</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Tschüss means goodbye, not hello.')">Tschüss</button>
        </div>

        <div class="quiz-q">
          <p>3. What does "Wie geht’s?" mean?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! It means How are you? (informal).')">How are you? (informal)</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'It does not mean Goodbye.')">Goodbye</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'It does not mean Thank you.')">Thank you</button>
        </div>

        <div class="quiz-q">
          <p>4. Which of these is a common misconception?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! Hallo is not always appropriate.')">Hallo works everywhere</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Guten Abend is correct for evening.')">Guten Abend is wrong</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Guten Tag is formal and correct.')">Guten Tag is informal</button>
        </div>

        <div class="quiz-summary" id="quiz1summary"></div>
      </div>
    `;
  }
}

let quizScore = 0;
let quizAnswered = 0;

function checkQuiz(btn, correct, explain) {
  if (btn.disabled) return;
  quizAnswered++;
  btn.disabled = true;
  btn.classList.add(correct ? "correct" : "incorrect");
  const exp = document.createElement("div");
  exp.className = "quiz-explain show";
  exp.innerText = explain;
  btn.parentNode.appendChild(exp);
  if (correct) quizScore++;

  if (quizAnswered === 4) {
    const summary = document.getElementById("quiz1summary");
    summary.innerHTML = `
      <div class="score">${quizScore}/4</div>
      <p>${quizScore === 4 ? "🎉 Perfect! You mastered greetings." : quizScore >= 2 ? "👍 Good job, review the mistakes." : "📘 Keep practicing, revisit the module."}</p>
    `;
    document.getElementById("xp1").innerText = (quizScore * 25) + " XP";
    document.getElementById("progressFill").style.width = "25%";
    document.getElementById("progressLabel").innerText = "25% complete";
  }
}

function checkEx1() {
  const val = document.getElementById("ex1input").value.trim();
  const fb = document.getElementById("ex1fb");
  if (val.toLowerCase() === "guten") {
    fb.className = "fb correct show";
    fb.innerText = "✅ Correct! The phrase is 'Guten Morgen'.";
  } else {
    fb.className = "fb wrong show";
    fb.innerText = "❌ Not quite. The correct phrase is 'Guten Morgen'.";
  }
}
</script>
<script>
function goToQuiz(moduleNum) {
  if (moduleNum === 1) {
    const quizCard = document.getElementById("quiz1card");
    quizCard.innerHTML = `
      <div class="card">
        <h3>📝 Module 1 Quiz — Greetings & Introductions</h3>

        <div class="quiz-q">
          <p>1. What is the formal way to say "Good morning" in German?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! Guten Morgen is formal.')">Guten Morgen</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Hallo is informal.')">Hallo</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Servus is regional, not standard.')">Servus</button>
        </div>

        <div class="quiz-q">
          <p>2. Which phrase would you use with a professor?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! Guten Tag is formal.')">Guten Tag</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Hallo is too casual.')">Hallo</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Tschüss means goodbye, not hello.')">Tschüss</button>
        </div>

        <div class="quiz-q">
          <p>3. What does "Wie geht’s?" mean?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! It means How are you? (informal).')">How are you? (informal)</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'It does not mean Goodbye.')">Goodbye</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'It does not mean Thank you.')">Thank you</button>
        </div>

        <div class="quiz-q">
          <p>4. Which of these is a common misconception?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! Hallo is not always appropriate.')">Hallo works everywhere</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Guten Abend is correct for evening.')">Guten Abend is wrong</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Guten Tag is formal and correct.')">Guten Tag is informal</button>
        </div>

        <div class="quiz-summary" id="quiz1summary"></div>
      </div>
    `;
  }
}

let quizScore = 0;
let quizAnswered = 0;

function checkQuiz(btn, correct, explain) {
  if (btn.disabled) return;
  quizAnswered++;
  btn.disabled = true;
  btn.classList.add(correct ? "correct" : "incorrect");
  const exp = document.createElement("div");
  exp.className = "quiz-explain show";
  exp.innerText = explain;
  btn.parentNode.appendChild(exp);
  if (correct) quizScore++;

  if (quizAnswered === 4) {
    const summary = document.getElementById("quiz1summary");
    summary.innerHTML = `
      <div class="score">${quizScore}/4</div>
      <p>${quizScore === 4 ? "🎉 Perfect! You mastered greetings." : quizScore >= 2 ? "👍 Good job, review the mistakes." : "📘 Keep practicing, revisit the module."}</p>
    `;
    document.getElementById("xp1").innerText = (quizScore * 25) + " XP";
    document.getElementById("progressFill").style.width = "25%";
    document.getElementById("progressLabel").innerText = "25% complete";
  }
}

function checkEx1() {
  const val = document.getElementById("ex1input").value.trim();
  const fb = document.getElementById("ex1fb");
  if (val.toLowerCase() === "guten") {
    fb.className = "fb correct show";
    fb.innerText = "✅ Correct! The phrase is 'Guten Morgen'.";
  } else {
    fb.className = "fb wrong show";
    fb.innerText = "❌ Not quite. The correct phrase is 'Guten Morgen'.";
  }
}
</script>
<script>
function goToQuiz(moduleNum) {
  if (moduleNum === 1) {
    const quizCard = document.getElementById("quiz1card");
    quizCard.innerHTML = `
      <div class="card">
        <h3>📝 Module 1 Quiz — Greetings & Introductions</h3>

        <div class="quiz-q">
          <p>1. What is the formal way to say "Good morning" in German?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! Guten Morgen is formal.')">Guten Morgen</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Hallo is informal.')">Hallo</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Servus is regional, not standard.')">Servus</button>
        </div>

        <div class="quiz-q">
          <p>2. Which phrase would you use with a professor?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! Guten Tag is formal.')">Guten Tag</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Hallo is too casual.')">Hallo</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Tschüss means goodbye, not hello.')">Tschüss</button>
        </div>

        <div class="quiz-q">
          <p>3. What does "Wie geht’s?" mean?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! It means How are you? (informal).')">How are you? (informal)</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'It does not mean Goodbye.')">Goodbye</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'It does not mean Thank you.')">Thank you</button>
        </div>

        <div class="quiz-q">
          <p>4. Which of these is a common misconception?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! Hallo is not always appropriate.')">Hallo works everywhere</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Guten Abend is correct for evening.')">Guten Abend is wrong</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Guten Tag is formal and correct.')">Guten Tag is informal</button>
        </div>

        <div class="quiz-summary" id="quiz1summary"></div>
      </div>
    `;
  }
}

let quizScore = 0;
let quizAnswered = 0;

function checkQuiz(btn, correct, explain) {
  if (btn.disabled) return;
  quizAnswered++;
  btn.disabled = true;
  btn.classList.add(correct ? "correct" : "incorrect");
  const exp = document.createElement("div");
  exp.className = "quiz-explain show";
  exp.innerText = explain;
  btn.parentNode.appendChild(exp);
  if (correct) quizScore++;

  if (quizAnswered === 4) {
    const summary = document.getElementById("quiz1summary");
    summary.innerHTML = `
      <div class="score">${quizScore}/4</div>
      <p>${quizScore === 4 ? "🎉 Perfect! You mastered greetings." : quizScore >= 2 ? "👍 Good job, review the mistakes." : "📘 Keep practicing, revisit the module."}</p>
    `;
    document.getElementById("xp1").innerText = (quizScore * 25) + " XP";
    document.getElementById("progressFill").style.width = "25%";
    document.getElementById("progressLabel").innerText = "25% complete";
  }
}

function checkEx1() {
  const val = document.getElementById("ex1input").value.trim();
  const fb = document.getElementById("ex1fb");
  if (val.toLowerCase() === "guten") {
    fb.className = "fb correct show";
    fb.innerText = "✅ Correct! The phrase is 'Guten Morgen'.";
  } else {
    fb.className = "fb wrong show";
    fb.innerText = "❌ Not quite. The correct phrase is 'Guten Morgen'.";
  }
}
</script>
<script>
function goToQuiz(moduleNum) {
  if (moduleNum === 1) {
    const quizCard = document.getElementById("quiz1card");
    quizCard.innerHTML = `
      <div class="card">
        <h3>📝 Module 1 Quiz — Greetings & Introductions</h3>

        <div class="quiz-q">
          <p>1. What is the formal way to say "Good morning" in German?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! Guten Morgen is formal.')">Guten Morgen</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Hallo is informal.')">Hallo</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Servus is regional, not standard.')">Servus</button>
        </div>

        <div class="quiz-q">
          <p>2. Which phrase would you use with a professor?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! Guten Tag is formal.')">Guten Tag</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Hallo is too casual.')">Hallo</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Tschüss means goodbye, not hello.')">Tschüss</button>
        </div>

        <div class="quiz-q">
          <p>3. What does "Wie geht’s?" mean?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! It means How are you? (informal).')">How are you? (informal)</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'It does not mean Goodbye.')">Goodbye</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'It does not mean Thank you.')">Thank you</button>
        </div>

        <div class="quiz-q">
          <p>4. Which of these is a common misconception?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! Hallo is not always appropriate.')">Hallo works everywhere</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Guten Abend is correct for evening.')">Guten Abend is wrong</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Guten Tag is formal and correct.')">Guten Tag is informal</button>
        </div>

        <div class="quiz-summary" id="quiz1summary"></div>
      </div>
    `;
  }
}

let quizScore = 0;
let quizAnswered = 0;

function checkQuiz(btn, correct, explain) {
  if (btn.disabled) return;
  quizAnswered++;
  btn.disabled = true;
  btn.classList.add(correct ? "correct" : "incorrect");
  const exp = document.createElement("div");
  exp.className = "quiz-explain show";
  exp.innerText = explain;
  btn.parentNode.appendChild(exp);
  if (correct) quizScore++;

  if (quizAnswered === 4) {
    const summary = document.getElementById("quiz1summary");
    summary.innerHTML = `
      <div class="score">${quizScore}/4</div>
      <p>${quizScore === 4 ? "🎉 Perfect! You mastered greetings." : quizScore >= 2 ? "👍 Good job, review the mistakes." : "📘 Keep practicing, revisit the module."}</p>
    `;
    document.getElementById("xp1").innerText = (quizScore * 25) + " XP";
    document.getElementById("progressFill").style.width = "25%";
    document.getElementById("progressLabel").innerText = "25% complete";
  }
}

function checkEx1() {
  const val = document.getElementById("ex1input").value.trim();
  const fb = document.getElementById("ex1fb");
  if (val.toLowerCase() === "guten") {
    fb.className = "fb correct show";
    fb.innerText = "✅ Correct! The phrase is 'Guten Morgen'.";
  } else {
    fb.className = "fb wrong show";
    fb.innerText = "❌ Not quite. The correct phrase is 'Guten Morgen'.";
  }
}
</script>
<img width="678" height="224" alt="image" src="https://github.com/user-attachments/assets/69fa0d15-e5b5-492a-9abc-6427365d0c00" />

Module 2 :HTML:

<div class="module" id="module2">
  <div class="card">
    <div class="module-header">
      <div><span class="module-tag">Module 2 · Daily Life</span><h2>Shopping, Dining & Directions</h2></div>
      <span class="pill" id="xp2">0 XP</span>
    </div>
    <p class="subtitle">Learn everyday German phrases for shopping, ordering food, and asking for directions — essential for daily interactions.</p>

    <div class="section">
      <h3>📖 Explanation</h3>
      <p>Daily life phrases help you navigate common situations:</p>
      <ul>
        <li><b>Wie viel kostet das?</b> — How much does this cost?</li>
        <li><b>Ich hätte gern …</b> — I would like … (ordering food)</li>
        <li><b>Können Sie mir helfen?</b> — Can you help me?</li>
        <li><b>Wo ist der Bahnhof?</b> — Where is the train station?</li>
        <li><b>Die Rechnung, bitte.</b> — The bill, please.</li>
      </ul>
    </div>

    <div class="section">
      <h3>🧮 Example Dialogue</h3>
      <div class="example-box">
        <b>Customer:</b> Guten Tag! Wie viel kostet das?<br>
        <b>Shopkeeper:</b> Es kostet zehn Euro.<br>
        <b>Customer:</b> Danke. Ich nehme es.<br>
      </div>
    </div>

    <div class="section">
      <h3>💡 Analogy</h3>
      <div class="analogy-box">Think of these phrases as your “toolbox” for daily survival. Just like a traveler carries essentials (map, wallet, phone), these phrases are the essentials for navigating German daily life.</div>
    </div>

    <div class="section">
      <h3>📊 Diagram: Asking Directions</h3>
      <div class="diagram-wrap">
        <svg viewBox="0 0 320 160" width="320" height="160">
          <circle cx="60" cy="80" r="30" fill="var(--accent)" />
          <text x="60" y="85" fill="#fff" text-anchor="middle">You</text>
          <circle cx="260" cy="80" r="30" fill="var(--accent2)" />
          <text x="260" y="85" fill="#fff" text-anchor="middle">Station</text>
          <line x1="90" y1="80" x2="230" y2="80" stroke="var(--good)" stroke-width="3" marker-end="url(#arrow)" />
          <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto">
              <path d="M0,0 L0,6 L9,3 z" fill="var(--good)" />
            </marker>
          </defs>
        </svg>
      </div>
      <p class="subtitle">Phrase: <b>Wo ist der Bahnhof?</b> — “Where is the train station?”</p>
    </div>

    <div class="section">
      <h3>✏️ Practical Exercise</h3>
      <div class="exercise">
        <p>You want to order coffee politely. Type the German phrase for “I would like a coffee.”</p>
        <input type="text" id="ex2input" placeholder="Enter phrase">
        <button class="btn secondary" onclick="checkEx2()">Check</button>
        <div class="fb" id="ex2fb"></div>
      </div>
    </div>

    <div class="section">
      <h3>⚠️ Common Misconception</h3>
      <div class="misconception-box">Many learners think “Ich will …” is polite for ordering. In reality, it sounds demanding (“I want …”). Use <b>Ich hätte gern …</b> or <b>Ich möchte …</b> instead.</div>
    </div>

    <div class="section">
      <h3>🔑 Key Takeaways</h3>
      <div class="takeaway-box">
        <ul style="margin:0;padding-left:18px;">
          <li>Use <b>Wie viel kostet das?</b> for shopping.</li>
          <li>Polite ordering: <b>Ich hätte gern …</b>.</li>
          <li>Asking directions: <b>Wo ist …?</b>.</li>
          <li>Politeness matters — avoid “Ich will …”.</li>
        </ul>
      </div>
    </div>

    <div class="btn-row"><button class="btn" onclick="goToQuiz(2)">Take Module 2 Quiz →</button></div>
  </div>

  <div class="card" id="quiz2card"></div>
</div>
Quiz logic for Module 2
<script>
function goToQuiz(moduleNum) {
  if (moduleNum === 2) {
    const quizCard = document.getElementById("quiz2card");
    quizCard.innerHTML = `
      <div class="card">
        <h3>📝 Module 2 Quiz — Daily Life Phrases</h3>

        <div class="quiz-q">
          <p>1. How do you politely order food?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! Ich hätte gern … is polite.')">Ich hätte gern …</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Ich will … sounds demanding.')">Ich will …</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Hallo is just a greeting.')">Hallo …</button>
        </div>

        <div class="quiz-q">
          <p>2. What does “Wie viel kostet das?” mean?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! It means How much does this cost?')">How much does this cost?</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'It does not mean Where is the station.')">Where is the station?</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'It does not mean I would like …')">I would like …</button>
        </div>

        <div class="quiz-q">
          <p>3. Which phrase is used to ask for directions?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! Wo ist … is for directions.')">Wo ist …?</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Ich hätte gern … is for ordering.')">Ich hätte gern …</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Die Rechnung, bitte is for paying.')">Die Rechnung, bitte</button>
        </div>

        <div class="quiz-q">
          <p>4. Which phrase is used to ask for the bill?</p>
          <button class="quiz-opt" onclick="checkQuiz(this,true,'Correct! Die Rechnung, bitte is polite.')">Die Rechnung, bitte</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Wo ist … is for directions.')">Wo ist …?</button>
          <button class="quiz-opt" onclick="checkQuiz(this,false,'Ich will … is demanding.')">Ich will …</button>
        </div>

        <div class="quiz-summary" id="quiz2summary"></div>
      </div>
    `;
  }
}

function checkEx2() {
  const val = document.getElementById("ex2input").value.trim().toLowerCase();
  const fb = document.getElementById("ex2fb");
  if (val.includes("ich hätte gern") && val.includes("kaffee")) {
    fb.className = "fb correct show";
    fb.innerText = "✅ Correct! 'Ich hätte gern einen Kaffee.' is polite.";
  } else {
    fb.className = "fb wrong show";
    fb.innerText = "❌ Try again. Use 'Ich hätte gern einen Kaffee.'";
  }
}
</script>
✨ With this, Module 2 (Daily Life Phrases) is complete: explanations, examples, analogy, diagram, exercise, misconception, key takeaways, and a working quiz.
<img width="816" height="504" alt="image" src="https://github.com/user-attachments/assets/58164c76-9599-40ed-926c-f71d4303d8aa" />
<img width="1311" height="570" alt="image" src="https://github.com/user-attachments/assets/f702c2b4-34fc-47df-a461-1fe4fb618f8f" />
<img width="1186" height="662" alt="image" src="https://github.com/user-attachments/assets/3d274baa-6d6e-4189-ad5f-8787210bf9d3" />
<img width="1055" height="612" alt="image" src="https://github.com/user-attachments/assets/281afdb4-8cf5-4f7d-b64d-64ed945ca51a" />
