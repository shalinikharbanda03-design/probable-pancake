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
:Response: #
# Day 27 Challenge: Prior Authorization Story Simulator

## 📌 Project Overview
Today's challenge focuses on understanding the complex healthcare workflow of **Prior Authorization (PA)** through an interactive, story-based web application. Using a single-file HTML application built with Tailwind CSS and Vanilla JavaScript, we follow the healthcare journey of Rahul (a patient) and Priya (a healthcare operations specialist).

---

## 💡 Key Learnings
1. **Prior Authorization Workflow:** Learned how the administrative workflow moves directly from the Provider (Doctor) to the Payer (Insurance Company) for approval before specific treatments can begin.
2. **Impact of Delays:** Understood from the *AMA 2023 PA Survey* that PA causes treatment delays in the vast majority of cases, which can severely affect disease progression in aggressive diagnoses like Rheumatoid Arthritis.
3. **Insurance Checkpoints:** StarCare Health (used as an illustrative example) evaluates requests based on eligibility, thorough clinical documentation, exact ICD-10 diagnosis match, and step therapy history.
4. **Denial and Appeal Process:** A denial is never permanent. Even though resolving a PA denial costs physician offices an average of 2+ staff hours, it can be overturned through a formal appeal backed by a Letter of Medical Necessity.
5. **System Metrics:** Health systems actively track metrics such as denial rates, appeal success rates, and resolution times to optimize their workflows and reduce administrative friction.

---

## 📖 Simulator Story Structure (The 8 Chapters Explained)

The interactive application tracks a sequential 8-stage educational journey:

### Chapter 1: Doctor Visit
* **Plot:** Rahul visits City Medical Center. Dr. Patel diagnoses him with Rheumatoid Arthritis and prescribes a specialized biologic medication, Humira.
* **Choices:** Discuss medication details or inquire immediately about insurance coverage.

### Chapter 2: Insurance Roadblock
* **Plot:** Dr. Patel's office submits the PA request directly to StarCare Health (payer) on file permanently. No retail pharmacy is involved in this direct provider-to-payer channel.
* **Choices:** Advise Rahul to wait patiently or prompt Priya to step in and manage the case.

### Chapter 3: What is PA?
* **Plot:** Priya explains the mechanics of Prior Authorization in plain language. She highlights that step therapy delays are critical because, for aggressive conditions, waiting can permanently affect disease progression. (Citing AMA 2023 PA Survey).
* **Choices:** Ask Priya about further system impacts or proceed directly to the next workflow step.

### Chapter 4: Insurance Review
* **Plot:** Priya breaks down exactly what StarCare Health checks during a review: member eligibility, clinical documentation, ICD-10 diagnosis match, and step therapy history.
* **Choices:** Double-check the submitted paperwork or await the formal insurance determination.

### Chapter 5: Denial
* **Plot:** The request is denied due to missing step therapy documentation. Priya explains that a denial is not a permanent dead end, though resolving it typically costs physician offices 2+ staff hours.
* **Choices:** Initiate a formal appeal immediately or review alternative documentation options.

### Chapter 6: Appeal
* **Plot:** Priya and the clinic team gather missing medical records, draft a comprehensive Letter of Medical Necessity, and file a formal appeal.
* **Choices:** Track the appeal status dynamically or follow up directly with StarCare Health.

### Chapter 7: Approval
* **Plot:** The appeal is successful! StarCare Health approves the PA and issues a permanent reference number. No repeat PA will be required for Rahul's ongoing Humira treatment.
* **Choices:** Deliver the good news to Rahul or review the final case summary.

### Chapter 8: Takeaways
* **Plot:** A dual perspective wrap-up. The Patient perspective covers self-advocacy, while the System perspective highlights how health networks track denial rates and resolution times.
* **Choices:** Restart the simulator to explore alternate dialogue paths or complete the session. 
*
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prior Authorization Story Simulator - Day 27</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Smooth scrolling for the chat container */
        #chat-container {
            scroll-behavior: smooth;
        }
    </style>
</head>
<body class="bg-slate-50 font-sans min-h-screen flex flex-col">

    <!-- Header Section (Healthcare Education Design System) -->
    <header class="bg-blue-800 text-white shadow-md p-4 sticky top-0 z-10">
        <div class="max-w-3xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-2">
            <div>
                <h1 class="text-xl font-bold tracking-wide">Prior Authorization Simulator</h1>
                <p class="text-xs text-blue-200">Interactive Learning Journey • Illustrative Example: StarCare Health</p>
            </div>
            <!-- Progress Bar Tracker -->
            <div class="w-full sm:w-48 bg-blue-900 rounded-full h-4 overflow-hidden border border-blue-700 relative">
                <div id="progress-bar" class="bg-emerald-500 h-full transition-all duration-500 ease-out" style="width: 12.5%;"></div>
                <span id="progress-text" class="absolute inset-0 flex items-center justify-center text-[10px] font-bold text-white">Chapter 1/8</span>
            </div>
        </div>
    </header>

    <!-- Main Simulator Viewport -->
    <main class="flex-1 max-w-3xl w-full mx-auto p-4 flex flex-col gap-4">
        
        <!-- Interactive Chat Feed Box -->
        <div id="chat-container" class="flex-1 bg-white border border-slate-200 rounded-xl shadow-sm p-4 overflow-y-auto min-h-[400px] max-h-[550px] flex flex-col gap-4">
            <!-- Chat bubbles will dynamically append here via Vanilla JS -->
        </div>

        <!-- Choice Controls Panel -->
        <div id="controls-panel" class="bg-slate-100 border border-slate-200 rounded-xl p-4 shadow-inner flex flex-col gap-3">
            <p id="choice-prompt" class="text-sm font-semibold text-slate-700 text-center">What should Rahul or the team do next?</p>
            <div id="choices-box" class="flex flex-col sm:flex-row gap-3 justify-center">
                <!-- Choice buttons will dynamically render here -->
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-slate-800 text-slate-400 text-center text-xs py-3 mt-auto border-t border-slate-700">
        AV Talks Claude AI 60 Days Challenge • Day 27 Task Completed
    </footer>

    <!-- Core Simulator Logic (Vanilla JS) -->
    <script>
        // Story Data Structure tracking all 8 sequential scenes
        const storyData = {
            1: {
                title: "Chapter 1: Doctor Visit",
                narration: "Rahul visits City Medical Center experiencing severe, continuous joint pain. After a thorough physical exam and blood panels, Dr. Patel diagnoses him with Rheumatoid Arthritis and prescribes a specialized biologic medication, Humira.",
                choices: [
                    { text: "Ask Dr. Patel about how Humira works", nextDialogue: "rahul_q1" },
                    { text: "Inquire immediately about insurance coverage", nextDialogue: "rahul_q2" }
                ],
                dialogues: {
                    rahul_q1: [
                        { speaker: "Rahul", text: "Dr. Patel, how exactly will Humira help my joints? Is it a standard pill?" },
                        { speaker: "Narrator", text: "Dr. Patel explains that Humira is an injectable biologic that blocks specific proteins causing inflammation, targeting the root cause rather than just masking pain." }
                    ],
                    rahul_q2: [
                        { speaker: "Rahul", text: "Doctor, I've heard biologic drugs are incredibly expensive. Will my insurance plan cover this?" },
                        { speaker: "Narrator", text: "Dr. Patel nods knowingly. 'It is costly, Rahul. We will submit the prescription, but because it's a specialty biologic, your payer StarCare Health will require Prior Authorization first.'" }
                    ]
                }
            },
            2: {
                title: "Chapter 2: Insurance Roadblock",
                narration: "Dr. Patel's administrative staff packages the prescription details. Instead of routing through a local retail pharmacy, the clinic submits the Prior Authorization (PA) paperwork directly to StarCare Health. This establishes a direct Provider → PA Request → Payer communication channel.",
                choices: [
                    { text: "Advise Rahul to wait at home for a notification", nextDialogue: "wait_path" },
                    { text: "Introduce Priya, the clinic's healthcare operations specialist", nextDialogue: "priya_intro" }
                ],
                dialogues: {
                    wait_path: [
                        { speaker: "Rahul", text: "Okay, I guess I will just go home and wait for StarCare Health to send a letter or text message." },
                        { speaker: "Narrator", text: "A week passes with complete silence. Rahul's morning joint stiffness begins to worsen significantly, making everyday tasks difficult." }
                    ],
                    priya_intro: [
                        { speaker: "Priya", text: "Hi Rahul! I'm Priya from the clinic's care coordination team. I see Dr. Patel ordered Humira. I'm taking over your case to track StarCare Health's response closely." },
                        { speaker: "Rahul", text: "Thank you, Priya! I was feeling completely lost looking at these complex insurance terms." }
                    ]
                }
            },
            3: {
                title: "Chapter 3: What is PA?",
                narration: "Seeing Rahul's confusion regarding the administrative delay, Priya sits down to explain the systemic mechanics of Prior Authorization in plain, beginner-friendly terms.",
                choices: [
                    { text: "Ask Priya why insurance companies implement these barriers", nextDialogue: "why_pa" },
                    { text: "Ask about the clinical consequences of waiting for approval", nextDialogue: "clinical_impact" }
                ],
                dialogues: {
                    why_pa: [
                        { speaker: "Priya", text: "Prior Authorization is a process where payers like StarCare Health verify that a high-cost treatment is medically necessary before agreeing to pay for it. They use protocols like 'step therapy' to ensure cheaper options are tried first." }
                    ],
                    clinical_impact: [
                        { speaker: "Priya", text: "Step therapy isn't just harmless corporate bureaucracy. For aggressive, destructive diagnoses like Rheumatoid Arthritis, administrative delays directly delay active treatment, which can cause permanent joint damage and affect overall disease progression." },
                        { speaker: "Narrator", text: "Priya references data to highlight the scale: 'According to the AMA 2023 PA Survey, prior authorization requirements cause documented treatment delays in the vast majority of cases.'" }
                    ]
                }
            },
            4: {
                title: "Chapter 4: Insurance Review",
                narration: "Inside StarCare Health's clinical review department, a utilization management team receives Rahul's formal digital application packet and begins cross-referencing it against their strict medical policies.",
                choices: [
                    { text: "Review the checklist of what StarCare Health evaluates", nextDialogue: "checklist_view" },
                    { text: "Proceed directly to checking the submission status", nextDialogue: "status_check" }
                ],
                dialogues: {
                    checklist_view: [
                        { speaker: "Priya", text: "When StarCare Health reviews our request, they evaluate four major checkpoints: active member eligibility, complete clinical chart notes, an exact ICD-10 diagnosis code match, and a verified step therapy history showing safer or cheaper drugs failed first." },
                        { speaker: "Rahul", text: "Wow, so if even one piece of that clinical puzzle is missing, the whole review stalls?" },
                        { speaker: "Priya", text: "Exactly. Everything must align perfectly with their specific corporate medical policy criteria." }
                    ],
                    status_check: [
                        { speaker: "Narrator", text: "Priya logs into the StarCare Health provider portal on day three to check the live status. The portal screen displays a flashing amber status indicator: 'Review in Progress - Pending Medical Director Evaluation.'" }
                    ]
                }
            },
            5: {
                title: "Chapter 5: Denial",
                narration: "A notification arrives via the portal. StarCare Health has officially issued an administrative DENIAL for Rahul's Humira prescription request.",
                choices: [
                    { text: "Examine the specific reason stated for the denial", nextDialogue: "denial_reason" },
                    { text: "Discuss the operational burden this places on the clinic", nextDialogue: "burden_stats" }
                ],
                dialogues: {
                    denial_reason: [
                        { speaker: "Priya", text: "The formal letter says: 'Denied due to missing step therapy documentation.' They claim we didn't explicitly prove Rahul tried and failed first-line anti-inflammatory medications." },
                        { speaker: "Rahul", text: "But I did take those pills months ago with my previous doctor! Does this mean I can never get Humira?" },
                        { speaker: "Priya", text: "Don't panic, Rahul! A denial is never a permanent dead end. It just means we have to enter the appeal phase." }
                    ],
                    burden_stats: [
                        { speaker: "Priya", text: "Dealing with this administrative pushback takes a toll. Studies show PA denials cost physician offices an average of 2+ dedicated staff hours per single request just to resolve through phone calls and paperwork rewriting." }
                    ]
                }
            },
            6: {
                title: "Chapter 6: Appeal",
                narration: "Priya spring into action to build a formal appeal packet. She coordinates directly with Dr. Patel to override StarCare Health's structural rejection.",
                choices: [
                    { text: "Gather old medical charts from Rahul's past clinic", nextDialogue: "charts_path" },
                    { text: "Draft a formal Letter of Medical Necessity", nextDialogue: "letter_path" }
                ],
                dialogues: {
                    charts_path: [
                        { speaker: "Priya", text: "I tracked down your previous medical records from your former family practitioner. It clearly documents 6 months of failed first-line therapy. I'm attaching this as indisputable proof." }
                    ],
                    letter_path: [
                        { speaker: "Narrator", text: "Dr. Patel drafts a comprehensive 'Letter of Medical Necessity'. The letter explicitly explains that Rahul's severe radiographic joint erosions mean any further delays forced by step therapy will cause irreversible physical disability." }
                    ]
                }
            },
            7: {
                title: "Chapter 7: Approval",
                narration: "Forty-eight hours after submitting the robust appeal packet, Priya logs into the portal. The status has shifted from a red denial indicator to a vibrant green indicator: PRIOR AUTHORIZATION APPROVED.",
                choices: [
                    { text: "Review the approval parameters and tracking metrics", nextDialogue: "auth_details" },
                    { text: "Deliver the successful news directly to Rahul", nextDialogue: "good_news" }
                ],
                dialogues: {
                    auth_details: [
                        { speaker: "Priya", text: "Excellent! StarCare Health has issued a unique Authorization Reference Number. Crucially, this approved PA is saved permanently on file. No repeat PA requests will be required for this specific Humira regimen moving forward." }
                    ],
                    good_news: [
                        { speaker: "Priya", text: "Rahul, great news! The insurance company approved the appeal. Your specialty medication is fully covered and ready for delivery." },
                        { speaker: "Rahul", text: "Oh wow, what a massive relief! I couldn't have navigated this complex maze without your team's constant support, Priya." }
                    ]
                }
            },
            8: {
                title: "Chapter 8: Takeaways",
                narration: "With the approval secured and treatment successfully underway, Rahul and the clinic evaluate the broader, high-level lessons learned from navigating the modern healthcare insurance landscape.",
                choices: [
                    { text: "Review the Patient Perspective takeaway", nextDialogue: "patient_view" },
                    { text: "Review the System & Operational Perspective takeaway", nextDialogue: "system_view" }
                ],
                dialogues: {
                    patient_view: [
                        { speaker: "Rahul", text: "As a patient, I realized how vital self-advocacy and expert guidance are. If I had simply given up after the initial denial, my health would have paid the price." }
                    ],
                    system_view: [
                        { speaker: "Priya", text: "From an operational standpoint, health systems must track systemic metrics like baseline denial rates, appeal success rates, and total resolution times to optimize workflows and actively shield patients from severe administrative friction." }
                    ]
                }
            }
        };

        let currentChapter = 1;
        const chatContainer = document.getElementById('chat-container');
        const choicesBox = document.getElementById('choices-box');
        const progressBar = document.getElementById('progress-bar');
        const progressText = document.getElementById('progress-text');

        // Function to safely create and append chat elements without using innerHTML
        function appendBubble(type, speaker, text) {
            const wrapper = document.createElement('div');
            wrapper.className = "w-full flex flex-col mb-2 transition-all duration-300 transform translate-y-2 opacity-0 animate-[fadeIn_0.3s_forwards]";

            if (type === 'narrator') {
                wrapper.className += " items-center text-center px-6";
                const p = document.createElement('p');
                p.className = "text-sm text-slate-500 italic leading-relaxed bg-slate-100 p-3 rounded-lg border border-slate-200 w-full";
                p.textContent = text;
                wrapper.appendChild(p);
            } else {
                const bubble = document.createElement('div');
                const nameLabel = document.createElement('span');
                nameLabel.className = "text-xs font-bold text-slate-500 mb-1 px-1";
                nameLabel.textContent = speaker;

                if (speaker === 'Rahul') {
                    wrapper.className += " items-start";
                    bubble.className = "bg-blue-100 text-blue-900 rounded-2xl rounded-tl-none p-3 max-w-[85%] text-sm shadow-sm border border-blue-200";
                    // Add emoji avatar representation contextually
                    nameLabel.textContent = "👦 " + speaker;
                } else if (speaker === 'Priya') {
                    wrapper.className += " items-end";
                    bubble.className = "bg-emerald-100 text-emerald-900 rounded-2xl rounded-tr-none p-3 max-w-[85%] text-sm shadow-sm border border-emerald-200";
                    nameLabel.textContent = speaker + " 👧";
                }
                
                bubble.textContent = text;
                wrapper.appendChild(nameLabel);
                wrapper.appendChild(bubble);
            }

            chatContainer.appendChild(wrapper);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }

        // Custom animation utility keyframes handled via injection style safely
        const style = document.createElement('style');
        style.textContent = `@keyframes fadeIn { to { opacity: 1; transform: translateY(0); } }`;
        document.head.appendChild(style);

        // Function to update header system trackers
        function updateProgress() {
            const percentage = (currentChapter / 8) * 100;
            progressBar.style.width = `${percentage}%`;
            progressText.textContent = `Chapter ${currentChapter}/8`;
        }

        // Renders the scenario narration and choice nodes
        function loadScene(chapterNum) {
            updateProgress();
            const scene = storyData[chapterNum];
            
            // Append separation line for clear chapter transitions
            if (chapterNum > 1) {
                const hr = document.createElement('div');
                hr.className = "border-t border-dashed border-slate-200 my-4 text-center text-xs text-slate-400 font-bold tracking-wider";
                hr.textContent = `--- ${scene.title} ---`;
                chatContainer.appendChild(hr);
            } else {
                const welcomeMsg = document.createElement('p');
                welcomeMsg.className = "text-xs text-center text-slate-400 font-semibold mb-2";
                welcomeMsg.textContent = "Beginning Simulator Framework...";
                chatContainer.appendChild(welcomeMsg);
            }

            // Append main chapter context
            appendBubble('narrator', null, scene.narration);

            // Clean past control buttons
            choicesBox.innerHTML = '';

            // Generate choice elements using safe DOM elements
            scene.choices.forEach(choice => {
                const btn = document.createElement('button');
                btn.className = "flex-1 bg-white hover:bg-blue-50 border border-slate-300 hover:border-blue-400 text-slate-800 hover:text-blue-900 font-medium py-2.5 px-4 rounded-xl text-xs sm:text-sm shadow-sm transition-all text-center focus:outline-none focus:ring-2 focus:ring-blue-500";
                btn.textContent = choice.text;
                btn.onclick = () => handleChoice(choice, scene);
                choicesBox.appendChild(btn);
            });
        }

        // Handles button selections, plays corresponding dialogues, then increments chapter loops
        function handleChoice(choice, scene) {
            // Disable buttons temporarily to prevent double click anomalies
            const buttons = choicesBox.querySelectorAll('button');
            buttons.forEach(b => b.disabled = true);

            // Run dialogues attached to specific branch path chosen
            const dialogueLines = scene.dialogues[choice.nextDialogue];
            dialogueLines.forEach((line, index) => {
                setTimeout(() => {
                    if (line.speaker === 'Narrator') {
                        appendBubble('narrator', null, line.text);
                    } else {
                        appendBubble('character', line.speaker, line.text);
                    }
                }, index * 600); // Slight stagger delay for conversational pacing feel
            });

            // Set timeout loop to transition to next chapter smoothly
            const totalDelay = dialogueLines.length * 600 + 800;
            setTimeout(() => {
                if (currentChapter < 8) {
                    currentChapter++;
                    loadScene(currentChapter);
                } else {
                    // Story wrap up screen options
                    showEndGameOptions();
                }
            }, totalDelay);
        }

        // End of simulator restart reset hooks
        function showEndGameOptions() {
            choicesBox.innerHTML = '';
            document.getElementById('choice-prompt').textContent = "Simulation Concluded! Final clinical workflow benchmarks met.";
            
            const restartBtn = document.createElement('button');
            restartBtn.className = "bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-3 px-6 rounded-xl text-sm shadow transition-all transform hover:scale-[1.02]";
            restartBtn.textContent = "🔄 Restart Story (Explore Alternative Dialogue Paths)";
            restartBtn.onclick = () => {
                chatContainer.innerHTML = '';
                currentChapter = 1;
                document.getElementById('choice-prompt').textContent = "What should Rahul or the team do next?";
                loadScene(currentChapter);
            };
            choicesBox.appendChild(restartBtn);
        }

        // Initialize App Session on viewport window load automatically
        window.onload = () => {
            loadScene(currentChapter);
        };
    </script>
</body>
</html>
[Day.27index.html](https://github.com/user-attachments/files/29607341/Day.27index.html)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prior Authorization Story Simulator - Day 27</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Smooth scrolling for the chat container */
        #chat-container {
            scroll-behavior: smooth;
        }
    </style>
</head>
<body class="bg-slate-50 font-sans min-h-screen flex flex-col">

    <!-- Header Section (Healthcare Education Design System) -->
    <header class="bg-blue-800 text-white shadow-md p-4 sticky top-0 z-10">
        <div class="max-w-3xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-2">
            <div>
                <h1 class="text-xl font-bold tracking-wide">Prior Authorization Simulator</h1>
                <p class="text-xs text-blue-200">Interactive Learning Journey • Illustrative Example: StarCare Health</p>
            </div>
            <!-- Progress Bar Tracker -->
            <div class="w-full sm:w-48 bg-blue-900 rounded-full h-4 overflow-hidden border border-blue-700 relative">
                <div id="progress-bar" class="bg-emerald-500 h-full transition-all duration-500 ease-out" style="width: 12.5%;"></div>
                <span id="progress-text" class="absolute inset-0 flex items-center justify-center text-[10px] font-bold text-white">Chapter 1/8</span>
            </div>
        </div>
    </header>

    <!-- Main Simulator Viewport -->
    <main class="flex-1 max-w-3xl w-full mx-auto p-4 flex flex-col gap-4">
        
        <!-- Interactive Chat Feed Box -->
        <div id="chat-container" class="flex-1 bg-white border border-slate-200 rounded-xl shadow-sm p-4 overflow-y-auto min-h-[400px] max-h-[550px] flex flex-col gap-4">
            <!-- Chat bubbles will dynamically append here via Vanilla JS -->
        </div>

        <!-- Choice Controls Panel -->
        <div id="controls-panel" class="bg-slate-100 border border-slate-200 rounded-xl p-4 shadow-inner flex flex-col gap-3">
            <p id="choice-prompt" class="text-sm font-semibold text-slate-700 text-center">What should Rahul or the team do next?</p>
            <div id="choices-box" class="flex flex-col sm:flex-row gap-3 justify-center">
                <!-- Choice buttons will dynamically render here -->
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-slate-800 text-slate-400 text-center text-xs py-3 mt-auto border-t border-slate-700">
        AV Talks Claude AI 60 Days Challenge • Day 27 Task Completed
    </footer>

    <!-- Core Simulator Logic (Vanilla JS) -->
    <script>
        // Story Data Structure tracking all 8 sequential scenes
        const storyData = {
            1: {
                title: "Chapter 1: Doctor Visit",
                narration: "Rahul visits City Medical Center experiencing severe, continuous joint pain. After a thorough physical exam and blood panels, Dr. Patel diagnoses him with Rheumatoid Arthritis and prescribes a specialized biologic medication, Humira.",
                choices: [
                    { text: "Ask Dr. Patel about how Humira works", nextDialogue: "rahul_q1" },
                    { text: "Inquire immediately about insurance coverage", nextDialogue: "rahul_q2" }
                ],
                dialogues: {
                    rahul_q1: [
                        { speaker: "Rahul", text: "Dr. Patel, how exactly will Humira help my joints? Is it a standard pill?" },
                        { speaker: "Narrator", text: "Dr. Patel explains that Humira is an injectable biologic that blocks specific proteins causing inflammation, targeting the root cause rather than just masking pain." }
                    ],
                    rahul_q2: [
                        { speaker: "Rahul", text: "Doctor, I've heard biologic drugs are incredibly expensive. Will my insurance plan cover this?" },
                        { speaker: "Narrator", text: "Dr. Patel nods knowingly. 'It is costly, Rahul. We will submit the prescription, but because it's a specialty biologic, your payer StarCare Health will require Prior Authorization first.'" }
                    ]
                }
            },
            2: {
                title: "Chapter 2: Insurance Roadblock",
                narration: "Dr. Patel's administrative staff packages the prescription details. Instead of routing through a local retail pharmacy, the clinic submits the Prior Authorization (PA) paperwork directly to StarCare Health. This establishes a direct Provider → PA Request → Payer communication channel.",
                choices: [
                    { text: "Advise Rahul to wait at home for a notification", nextDialogue: "wait_path" },
                    { text: "Introduce Priya, the clinic's healthcare operations specialist", nextDialogue: "priya_intro" }
                ],
                dialogues: {
                    wait_path: [
                        { speaker: "Rahul", text: "Okay, I guess I will just go home and wait for StarCare Health to send a letter or text message." },
                        { speaker: "Narrator", text: "A week passes with complete silence. Rahul's morning joint stiffness begins to worsen significantly, making everyday tasks difficult." }
                    ],
                    priya_intro: [
                        { speaker: "Priya", text: "Hi Rahul! I'm Priya from the clinic's care coordination team. I see Dr. Patel ordered Humira. I'm taking over your case to track StarCare Health's response closely." },
                        { speaker: "Rahul", text: "Thank you, Priya! I was feeling completely lost looking at these complex insurance terms." }
                    ]
                }
            },
            3: {
                title: "Chapter 3: What is PA?",
                narration: "Seeing Rahul's confusion regarding the administrative delay, Priya sits down to explain the systemic mechanics of Prior Authorization in plain, beginner-friendly terms.",
                choices: [
                    { text: "Ask Priya why insurance companies implement these barriers", nextDialogue: "why_pa" },
                    { text: "Ask about the clinical consequences of waiting for approval", nextDialogue: "clinical_impact" }
                ],
                dialogues: {
                    why_pa: [
                        { speaker: "Priya", text: "Prior Authorization is a process where payers like StarCare Health verify that a high-cost treatment is medically necessary before agreeing to pay for it. They use protocols like 'step therapy' to ensure cheaper options are tried first." }
                    ],
                    clinical_impact: [
                        { speaker: "Priya", text: "Step therapy isn't just harmless corporate bureaucracy. For aggressive, destructive diagnoses like Rheumatoid Arthritis, administrative delays directly delay active treatment, which can cause permanent joint damage and affect overall disease progression." },
                        { speaker: "Narrator", text: "Priya references data to highlight the scale: 'According to the AMA 2023 PA Survey, prior authorization requirements cause documented treatment delays in the vast majority of cases.'" }
                    ]
                }
            },
            4: {
                title: "Chapter 4: Insurance Review",
                narration: "Inside StarCare Health's clinical review department, a utilization management team receives Rahul's formal digital application packet and begins cross-referencing it against their strict medical policies.",
                choices: [
                    { text: "Review the checklist of what StarCare Health evaluates", nextDialogue: "checklist_view" },
                    { text: "Proceed directly to checking the submission status", nextDialogue: "status_check" }
                ],
                dialogues: {
                    checklist_view: [
                        { speaker: "Priya", text: "When StarCare Health reviews our request, they evaluate four major checkpoints: active member eligibility, complete clinical chart notes, an exact ICD-10 diagnosis code match, and a verified step therapy history showing safer or cheaper drugs failed first." },
                        { speaker: "Rahul", text: "Wow, so if even one piece of that clinical puzzle is missing, the whole review stalls?" },
                        { speaker: "Priya", text: "Exactly. Everything must align perfectly with their specific corporate medical policy criteria." }
                    ],
                    status_check: [
                        { speaker: "Narrator", text: "Priya logs into the StarCare Health provider portal on day three to check the live status. The portal screen displays a flashing amber status indicator: 'Review in Progress - Pending Medical Director Evaluation.'" }
                    ]
                }
            },
            5: {
                title: "Chapter 5: Denial",
                narration: "A notification arrives via the portal. StarCare Health has officially issued an administrative DENIAL for Rahul's Humira prescription request.",
                choices: [
                    { text: "Examine the specific reason stated for the denial", nextDialogue: "denial_reason" },
                    { text: "Discuss the operational burden this places on the clinic", nextDialogue: "burden_stats" }
                ],
                dialogues: {
                    denial_reason: [
                        { speaker: "Priya", text: "The formal letter says: 'Denied due to missing step therapy documentation.' They claim we didn't explicitly prove Rahul tried and failed first-line anti-inflammatory medications." },
                        { speaker: "Rahul", text: "But I did take those pills months ago with my previous doctor! Does this mean I can never get Humira?" },
                        { speaker: "Priya", text: "Don't panic, Rahul! A denial is never a permanent dead end. It just means we have to enter the appeal phase." }
                    ],
                    burden_stats: [
                        { speaker: "Priya", text: "Dealing with this administrative pushback takes a toll. Studies show PA denials cost physician offices an average of 2+ dedicated staff hours per single request just to resolve through phone calls and paperwork rewriting." }
                    ]
                }
            },
            6: {
                title: "Chapter 6: Appeal",
                narration: "Priya spring into action to build a formal appeal packet. She coordinates directly with Dr. Patel to override StarCare Health's structural rejection.",
                choices: [
                    { text: "Gather old medical charts from Rahul's past clinic", nextDialogue: "charts_path" },
                    { text: "Draft a formal Letter of Medical Necessity", nextDialogue: "letter_path" }
                ],
                dialogues: {
                    charts_path: [
                        { speaker: "Priya", text: "I tracked down your previous medical records from your former family practitioner. It clearly documents 6 months of failed first-line therapy. I'm attaching this as indisputable proof." }
                    ],
                    letter_path: [
                        { speaker: "Narrator", text: "Dr. Patel drafts a comprehensive 'Letter of Medical Necessity'. The letter explicitly explains that Rahul's severe radiographic joint erosions mean any further delays forced by step therapy will cause irreversible physical disability." }
                    ]
                }
            },
            7: {
                title: "Chapter 7: Approval",
                narration: "Forty-eight hours after submitting the robust appeal packet, Priya logs into the portal. The status has shifted from a red denial indicator to a vibrant green indicator: PRIOR AUTHORIZATION APPROVED.",
                choices: [
                    { text: "Review the approval parameters and tracking metrics", nextDialogue: "auth_details" },
                    { text: "Deliver the successful news directly to Rahul", nextDialogue: "good_news" }
                ],
                dialogues: {
                    auth_details: [
                        { speaker: "Priya", text: "Excellent! StarCare Health has issued a unique Authorization Reference Number. Crucially, this approved PA is saved permanently on file. No repeat PA requests will be required for this specific Humira regimen moving forward." }
                    ],
                    good_news: [
                        { speaker: "Priya", text: "Rahul, great news! The insurance company approved the appeal. Your specialty medication is fully covered and ready for delivery." },
                        { speaker: "Rahul", text: "Oh wow, what a massive relief! I couldn't have navigated this complex maze without your team's constant support, Priya." }
                    ]
                }
            },
            8: {
                title: "Chapter 8: Takeaways",
                narration: "With the approval secured and treatment successfully underway, Rahul and the clinic evaluate the broader, high-level lessons learned from navigating the modern healthcare insurance landscape.",
                choices: [
                    { text: "Review the Patient Perspective takeaway", nextDialogue: "patient_view" },
                    { text: "Review the System & Operational Perspective takeaway", nextDialogue: "system_view" }
                ],
                dialogues: {
                    patient_view: [
                        { speaker: "Rahul", text: "As a patient, I realized how vital self-advocacy and expert guidance are. If I had simply given up after the initial denial, my health would have paid the price." }
                    ],
                    system_view: [
                        { speaker: "Priya", text: "From an operational standpoint, health systems must track systemic metrics like baseline denial rates, appeal success rates, and total resolution times to optimize workflows and actively shield patients from severe administrative friction." }
                    ]
                }
            }
        };

        let currentChapter = 1;
        const chatContainer = document.getElementById('chat-container');
        const choicesBox = document.getElementById('choices-box');
        const progressBar = document.getElementById('progress-bar');
        const progressText = document.getElementById('progress-text');

        // Function to safely create and append chat elements without using innerHTML
        function appendBubble(type, speaker, text) {
            const wrapper = document.createElement('div');
            wrapper.className = "w-full flex flex-col mb-2 transition-all duration-300 transform translate-y-2 opacity-0 animate-[fadeIn_0.3s_forwards]";

            if (type === 'narrator') {
                wrapper.className += " items-center text-center px-6";
                const p = document.createElement('p');
                p.className = "text-sm text-slate-500 italic leading-relaxed bg-slate-100 p-3 rounded-lg border border-slate-200 w-full";
                p.textContent = text;
                wrapper.appendChild(p);
            } else {
                const bubble = document.createElement('div');
                const nameLabel = document.createElement('span');
                nameLabel.className = "text-xs font-bold text-slate-500 mb-1 px-1";
                nameLabel.textContent = speaker;

                if (speaker === 'Rahul') {
                    wrapper.className += " items-start";
                    bubble.className = "bg-blue-100 text-blue-900 rounded-2xl rounded-tl-none p-3 max-w-[85%] text-sm shadow-sm border border-blue-200";
                    // Add emoji avatar representation contextually
                    nameLabel.textContent = "👦 " + speaker;
                } else if (speaker === 'Priya') {
                    wrapper.className += " items-end";
                    bubble.className = "bg-emerald-100 text-emerald-900 rounded-2xl rounded-tr-none p-3 max-w-[85%] text-sm shadow-sm border border-emerald-200";
                    nameLabel.textContent = speaker + " 👧";
                }
                
                bubble.textContent = text;
                wrapper.appendChild(nameLabel);
                wrapper.appendChild(bubble);
            }

            chatContainer.appendChild(wrapper);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }

        // Custom animation utility keyframes handled via injection style safely
        const style = document.createElement('style');
        style.textContent = `@keyframes fadeIn { to { opacity: 1; transform: translateY(0); } }`;
        document.head.appendChild(style);

        // Function to update header system trackers
        function updateProgress() {
            const percentage = (currentChapter / 8) * 100;
            progressBar.style.width = `${percentage}%`;
            progressText.textContent = `Chapter ${currentChapter}/8`;
        }

        // Renders the scenario narration and choice nodes
        function loadScene(chapterNum) {
            updateProgress();
            const scene = storyData[chapterNum];
            
            // Append separation line for clear chapter transitions
            if (chapterNum > 1) {
                const hr = document.createElement('div');
                hr.className = "border-t border-dashed border-slate-200 my-4 text-center text-xs text-slate-400 font-bold tracking-wider";
                hr.textContent = `--- ${scene.title} ---`;
                chatContainer.appendChild(hr);
            } else {
                const welcomeMsg = document.createElement('p');
                welcomeMsg.className = "text-xs text-center text-slate-400 font-semibold mb-2";
                welcomeMsg.textContent = "Beginning Simulator Framework...";
                chatContainer.appendChild(welcomeMsg);
            }

            // Append main chapter context
            appendBubble('narrator', null, scene.narration);

            // Clean past control buttons
            choicesBox.innerHTML = '';

            // Generate choice elements using safe DOM elements
            scene.choices.forEach(choice => {
                const btn = document.createElement('button');
                btn.className = "flex-1 bg-white hover:bg-blue-50 border border-slate-300 hover:border-blue-400 text-slate-800 hover:text-blue-900 font-medium py-2.5 px-4 rounded-xl text-xs sm:text-sm shadow-sm transition-all text-center focus:outline-none focus:ring-2 focus:ring-blue-500";
                btn.textContent = choice.text;
                btn.onclick = () => handleChoice(choice, scene);
                choicesBox.appendChild(btn);
            });
        }

        // Handles button selections, plays corresponding dialogues, then increments chapter loops
        function handleChoice(choice, scene) {
            // Disable buttons temporarily to prevent double click anomalies
            const buttons = choicesBox.querySelectorAll('button');
            buttons.forEach(b => b.disabled = true);

            // Run dialogues attached to specific branch path chosen
            const dialogueLines = scene.dialogues[choice.nextDialogue];
            dialogueLines.forEach((line, index) => {
                setTimeout(() => {
                    if (line.speaker === 'Narrator') {
                        appendBubble('narrator', null, line.text);
                    } else {
                        appendBubble('character', line.speaker, line.text);
                    }
                }, index * 600); // Slight stagger delay for conversational pacing feel
            });

            // Set timeout loop to transition to next chapter smoothly
            const totalDelay = dialogueLines.length * 600 + 800;
            setTimeout(() => {
                if (currentChapter < 8) {
                    currentChapter++;
                    loadScene(currentChapter);
                } else {
                    // Story wrap up screen options
                    showEndGameOptions();
                }
            }, totalDelay);
        }

        // End of simulator restart reset hooks
        function showEndGameOptions() {
            choicesBox.innerHTML = '';
            document.getElementById('choice-prompt').textContent = "Simulation Concluded! Final clinical workflow benchmarks met.";
            
            const restartBtn = document.createElement('button');
            restartBtn.className = "bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-3 px-6 rounded-xl text-sm shadow transition-all transform hover:scale-[1.02]";
            restartBtn.textContent = "🔄 Restart Story (Explore Alternative Dialogue Paths)";
            restartBtn.onclick = () => {
                chatContainer.innerHTML = '';
                currentChapter = 1;
                document.getElementById('choice-prompt').textContent = "What should Rahul or the team do next?";
                loadScene(currentChapter);
            };
            choicesBox.appendChild(restartBtn);
        }

        // Initialize App Session on viewport window load automatically
        window.onload = () => {
            loadScene(currentChapter);
        };
    </script>
</body>
</html>
<img width="692" height="513" alt="image" src="https://github.com/user-attachments/assets/bd34219e-38f5-4eae-9302-3331ffa19dc2" />
<img width="761" height="356" alt="image" src="https://github.com/user-attachments/assets/b424a274-6530-48b4-9b41-d798e47aa41f" />
<img width="732" height="434" alt="image" src="https://github.com/user-attachments/assets/8a96c9e1-ec38-457e-9e63-2e8e2bf406a4" />
<img width="683" height="413" alt="image" src="https://github.com/user-attachments/assets/9b5d585d-3608-41e6-940a-603cc3c42bf9" />

