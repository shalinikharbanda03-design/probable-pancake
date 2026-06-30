Prompt#
Prior Authorization Story Simulator

Single-file HTML app. HTML, Tailwind CSS CDN, Vanilla JavaScript.
Use createElement + appendChild for every new chat bubble. Never call innerHTML = on the chat container.
Design: same as previously established.

Characters
👦 Rahul — patient. Appears left.
👧 Priya — healthcare operations specialist. Appears right.
Narrators and doctors appear as centered italic text only, never chat bubbles.

Story — 8 scenes with append-only chat feed and progress bar:

1. Doctor Visit — Rahul visits City Medical Center. Dr. Patel diagnoses Rheumatoid Arthritis, prescribes Humira.

2. Insurance Roadblock — Dr. Patel's office submits PA directly to StarCare Health (payer). No pharmacy involved. Flow: Provider → PA Request → Payer. Approved PA is saved on file permanently.

3. What is PA? — Priya explains in plain language. Include: step therapy isn't just bureaucracy — for aggressive diagnoses, delays can affect disease progression. Cite: 'AMA 2023 PA Survey: PA causes treatment delays in the majority of cases.'

4. Insurance Review — Priya walks through what StarCare Health checks: eligibility, clinical documentation, ICD-10 diagnosis match, step therapy history. Explain why each matters.

5. Denial — Denied: missing step therapy documentation. Denial ≠ permanent. Priya notes the system side: 'PA denials cost physician offices 2+ staff hours to resolve.'

6. Appeal — Gather documents, Letter of Medical Necessity, formal appeal filing.

7. Approval — PA approved, saved on file. Reference number issued. No repeat PA needed for Humira.

8. Takeaways — Two perspectives: Patient (what Rahul learned) + System (how health systems track denial rate, appeal rate, resolution time).

After each scene show 2 choices that influence dialogue and progression.
Label StarCare Health as an illustrative example throughout.
Beginner-friendly language.
Healthcare education design system.
Result#
Done — the full story simulator is built and saved as a single self-contained HTML file.What it does, matching your prompt:

- **Tailwind CDN + vanilla JS**, single file, no other dependencies
- Chat feed is built **only** with `createElement`/`appendChild` — `chatFeed.innerHTML` is never set (restart clears it via a `removeChild` loop)
- Rahul (left, light blue bubble) and Priya (right, navy bubble); Dr. Patel and narrator lines render as centered italic text, never bubbles
- All 8 scenes included with the required facts: provider→PA→payer flow, AMA 2023 PA Survey citation, the four review checks, the denial reason + "2+ staff hours" stat, the appeal/Letter of Medical Necessity, the approval reference number (saved on file, no repeat PA), and the final Patient vs. System takeaways
- Two choices after every scene (1–7) that append a follow-up exchange before a "Continue" button advances the story; scene 8 shows the takeaway cards + Restart
- Progress bar updates each scene; "StarCare Health" is labeled as an illustrative example throughout

Just download the file and open it in a browser to play through it.

