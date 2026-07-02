:Target:
Hospital Admission Readiness Simulator

Single-file HTML app. HTML, Tailwind CSS CDN, Vanilla JavaScript.
style: same as previously established
Healthcare simulation design system. Task-first — no dashboard on load.
User plays Hospital Admission Coordinator.

Setup — collect:
- Provider, Attending Physician
- Diagnosis: Acute MI / CHF / Pneumonia / Elective Surgery / Hip Fracture
- Admission Type: Inpatient / Observation / Emergency / ICU / Same-Day Surgery
- PA Status, Admission Date

Observation Status must always show: 'CMS 2-Midnight Rule applies — different cost-sharing, SNF eligibility, and billing than inpatient. Medicare patients require written MOON notification.'
Label all provider/payer names as illustrative training data.

Button: 🏥 Analyze Admission Readiness

Initial Analysis
Generate status for: PA, Insurance, Bed, Documentation, Physician Orders, Consent.
Readiness Score 30–60%. Do not reveal final decision yet.

Score Weighting:
PA Status 25% · Clinical Documentation 20% · Physician Orders 20% · Insurance 15% · Consent 10% · Bed 10%
Denied PA + ICU admission cannot reach 70% from admin tasks alone.

PA Branches:
Approved → continue.
Pending → Follow Up, Upload Docs, Contact Physician.
Denied → Review Reason, Contact Insurance, Submit Appeal.
Successful appeal converts to Approved.

Workflow Actions:
Assign Bed / Verify Insurance / Upload Documentation / Complete Consent / Contact Physician / Notify Nursing / Prepare Patient Arrival

Acute MI and CHF trigger a criteria note:
'InterQual/Milliman thresholds apply — ensure documentation meets medical necessity standards before UR review.'

Timeline milestones:
PA Review → Insurance Verification → Bed Assignment → Documentation → Consent → Patient Arrival → Registration → Clinical Assessment → Admission Complete

Care Coordination Cards:
Attending / Case Manager / Nursing / Utilization Review / Discharge Planner
UR card must name: concurrent review, denial risk identification, InterQual, Milliman.

Risk Tracking:
Documentation Risk / Insurance Risk / Bed Risk / Clinical Risk
Clinical Risk weighted higher for Acute MI, CHF, ICU.

At Readiness ≥ 75% show Governance Snapshot:
'Industry benchmarks (estimates only): PA turnaround 3–5 days · Inpatient denial rate ~8–10% (CMS) · PA rework cost ~$11/transaction (CAQH)'

Final Decision:
≥ 90% → ✅ Admit — full summary.
< 90% → ⚠ Not Ready — missing items, required actions, remaining risks.

:Robot:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hospital Admission Readiness Simulator</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; }
        .custom-scrollbar::-webkit-scrollbar { width: 6px; height: 6px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: #f1f5f9; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
    </style>
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen flex flex-col antialiased selection:bg-teal-500 selection:text-slate-900">

    <header class="border-b border-slate-800 bg-slate-900/80 backdrop-blur sticky top-0 z-50 px-6 py-4 flex items-center justify-between">
        <div class="flex items-center space-x-3">
            <div class="p-2 bg-gradient-to-br from-teal-500 to-emerald-600 rounded-lg text-slate-900 font-bold shadow-lg shadow-teal-500/10">
                🏥
            </div>
            <div>
                <h1 class="text-lg font-semibold tracking-tight text-white flex items-center gap-2">
                    Hospital Admission Readiness Simulator
                </h1>
                <p class="text-xs text-slate-400">Role: <span class="text-teal-400 font-medium">Admission Coordinator</span> &middot; Instructive Training Platform</p>
            </div>
        </div>
        <div class="flex items-center space-x-2 bg-slate-800/60 px-3 py-1.5 rounded-md border border-slate-700/60 text-xs">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            <span class="text-slate-300 font-mono tracking-wider">SYSTEM ACTIVE</span>
        </div>
    </header>

    <main class="flex-1 max-w-7xl w-full mx-auto p-4 md:p-6 grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        
        <section class="lg:col-span-5 bg-slate-950 border border-slate-800 rounded-xl p-5 shadow-xl space-y-5">
            <div class="border-b border-slate-800 pb-3 flex justify-between items-center">
                <div class="flex items-center gap-2">
                    <span class="text-xs uppercase tracking-wider text-teal-400 font-bold bg-teal-950/60 px-2 py-0.5 rounded border border-teal-800/40">Step 1</span>
                    <h2 class="text-sm font-semibold text-slate-200">Admission Parameter Matrix</h2>
                </div>
                <span class="text-[10px] text-amber-500/90 font-medium bg-amber-500/10 border border-amber-500/20 px-2 py-0.5 rounded">
                    ⚠️ Illustrative Training Data
                </span>
            </div>

            <div class="space-y-4 text-xs">
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-slate-400 font-medium mb-1.5">Payer/Provider Organization</label>
                        <select id="input-provider" class="w-full bg-slate-900 border border-slate-700 rounded-md p-2 text-slate-200 focus:outline-none focus:border-teal-500">
                            <option value="Apex Health Mutual">Apex Health Mutual</option>
                            <option value="Beacon Care Network">Beacon Care Network</option>
                            <option value="Summit Medicare Advantage">Summit Medicare Advantage</option>
                            <option value="Horizon Assurance Corp">Horizon Assurance Corp</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-slate-400 font-medium mb-1.5">Attending Physician</label>
                        <select id="input-physician" class="w-full bg-slate-900 border border-slate-700 rounded-md p-2 text-slate-200 focus:outline-none focus:border-teal-500">
                            <option value="Dr. Evelyn Vance, MD (Cardiology)">Dr. Evelyn Vance, MD</option>
                            <option value="Dr. Marcus Thorne, MD (Internal Medicine)">Dr. Marcus Thorne, MD</option>
                            <option value="Dr. Alistair Vance, MD (Orthopedics)">Dr. Alistair Vance, MD</option>
                            <option value="Dr. Sarah Jenkins, MD (General Surgery)">Dr. Sarah Jenkins, MD</option>
                        </select>
                    </div>
                </div>

                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-slate-400 font-medium mb-1.5">Principal Diagnosis</label>
                        <select id="input-diagnosis" onchange="checkTriggers()" class="w-full bg-slate-900 border border-slate-700 rounded-md p-2 text-slate-200 focus:outline-none focus:border-teal-500">
                            <option value="Acute MI">Acute MI (Myocardial Infarction)</option>
                            <option value="CHF">CHF (Congestive Heart Failure)</option>
                            <option value="Pneumonia">Pneumonia</option>
                            <option value="Elective Surgery">Elective Surgery</option>
                            <option value="Hip Fracture">Hip Fracture</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-slate-400 font-medium mb-1.5">Admission Designation</label>
                        <select id="input-admission-type" onchange="checkTriggers()" class="w-full bg-slate-900 border border-slate-700 rounded-md p-2 text-slate-200 focus:outline-none focus:border-teal-500">
                            <option value="Inpatient">Inpatient Admission</option>
                            <option value="Observation">Observation Status</option>
                            <option value="Emergency">Emergency Tracking</option>
                            <option value="ICU">ICU Placement</option>
                            <option value="Same-Day Surgery">Same-Day Surgery</option>
                        </select>
                    </div>
                </div>

                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-slate-400 font-medium mb-1.5">Initial Prior Auth (PA) Status</label>
                        <select id="input-pa-status" class="w-full bg-slate-900 border border-slate-700 rounded-md p-2 text-slate-200 font-semibold focus:outline-none focus:border-teal-500">
                            <option value="Approved" class="text-emerald-400">Approved</option>
                            <option value="Pending" class="text-amber-400" selected>Pending Verification</option>
                            <option value="Denied" class="text-rose-400">Denied / Rejected</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-slate-400 font-medium mb-1.5">Admission Scheduled Date</label>
                        <input type="date" id="input-date" class="w-full bg-slate-900 border border-slate-700 rounded-md p-2 text-slate-200 focus:outline-none focus:border-teal-500">
                    </div>
                </div>

                <div id="observation-banner" class="hidden bg-amber-500/10 border border-amber-500/30 rounded-lg p-3 text-amber-300 space-y-1">
                    <div class="flex items-center gap-1.5 font-semibold text-[11px]">
                        <span>⚖️</span> Regulatory Mandate: CMS 2-Midnight Rule
                    </div>
                    <p class="text-[11px] leading-relaxed opacity-90">
                        CMS 2-Midnight Rule applies — different cost-sharing, SNF eligibility, and billing than inpatient. Medicare patients require written MOON notification.
                    </p>
                </div>

                <div id="criteria-banner" class="hidden bg-blue-500/10 border border-blue-500/30 rounded-lg p-3 text-blue-300 space-y-1">
                    <div class="flex items-center gap-1.5 font-semibold text-[11px]">
                        <span>📋</span> Clinical Guideline Triggered
                    </div>
                    <p class="text-[11px] leading-relaxed opacity-90">
                        InterQual/Milliman thresholds apply — ensure documentation meets medical necessity standards before UR review.
                    </p>
                </div>

                <button onclick="analyzeAdmission()" class="w-full bg-gradient-to-r from-teal-500 to-emerald-600 hover:from-teal-400 hover:to-emerald-500 text-slate-950 font-bold py-2.5 px-4 rounded-md transition duration-200 flex items-center justify-center gap-2 text-sm shadow-md shadow-emerald-950/50 mt-2">
                    🏥 Analyze Admission Readiness
                </button>
            </div>
        </section>

        <section class="lg:col-span-7 space-y-6">
            
            <div id="placeholder-view" class="bg-slate-950 border border-slate-800 border-dashed rounded-xl p-12 text-center flex flex-col items-center justify-center min-h-[350px]">
                <div class="text-4xl opacity-40 mb-3">📋</div>
                <h3 class="text-slate-300 font-medium text-sm">Awaiting Case Submission</h3>
                <p class="text-xs text-slate-500 max-w-sm mt-1 mx-auto">
                    Fill in the required provider matrix on the left panel and activate analysis to populate metrics, milestones, and workflow configurations.
                </p>
            </div>

            <div id="simulation-view" class="hidden space-y-6">
                
                <div class="bg-slate-950 border border-slate-800 rounded-xl p-5 shadow-xl grid grid-cols-1 md:grid-cols-12 gap-5 items-center">
                    <div class="md:col-span-4 text-center md:text-left border-b md:border-b-0 md:border-r border-slate-800 pb-4 md:pb-0 md:pr-4">
                        <div class="text-xs text-slate-400 font-medium">Readiness Index Evaluation</div>
                        <div class="flex items-baseline justify-center md:justify-start gap-1 mt-1">
                            <span id="readiness-score" class="text-4xl font-extrabold tracking-tight text-white">0%</span>
                            <span class="text-xs text-slate-500">/100%</span>
                        </div>
                        <div class="mt-2 text-[11px]">
                            Status: <span id="readiness-status-badge" class="font-bold uppercase tracking-wider px-1.5 py-0.5 rounded text-[10px]">Evaluating</span>
                        </div>
                    </div>
                    
                    <div class="md:col-span-8 space-y-2">
                        <div class="text-[11px] uppercase tracking-wider font-semibold text-slate-400 flex justify-between">
                            <span>System Attribute Weighting Matrix</span>
                            <span class="text-[10px] text-teal-400 lowercase italic">Realtime Impact Mapping</span>
                        </div>
                        <div class="grid grid-cols-3 gap-2 text-[10px] text-slate-300">
                            <div class="bg-slate-900 border border-slate-800 p-1.5 rounded flex flex-col justify-between">
                                <span class="text-slate-500">Prior Auth</span>
                                <span class="font-bold mt-1 text-slate-200">25% Weight</span>
                            </div>
                            <div class="bg-slate-900 border border-slate-800 p-1.5 rounded flex flex-col justify-between">
                                <span class="text-slate-500">Clinical Docs</span>
                                <span class="font-bold mt-1 text-slate-200">20% Weight</span>
                            </div>
                            <div class="bg-slate-900 border border-slate-800 p-1.5 rounded flex flex-col justify-between">
                                <span class="text-slate-500">MD Orders</span>
                                <span class="font-bold mt-1 text-slate-200">20% Weight</span>
                            </div>
                            <div class="bg-slate-900 border border-slate-800 p-1.5 rounded flex flex-col justify-between">
                                <span class="text-slate-500">Insurance Verify</span>
                                <span class="font-bold mt-1 text-slate-200">15% Weight</span>
                            </div>
                            <div class="bg-slate-900 border border-slate-800 p-1.5 rounded flex flex-col justify-between">
                                <span class="text-slate-500">Patient Consent</span>
                                <span class="font-bold mt-1 text-slate-200">10% Weight</span>
                            </div>
                            <div class="bg-slate-900 border border-slate-800 p-1.5 rounded flex flex-col justify-between">
                                <span class="text-slate-500">Bed Allocation</span>
                                <span class="font-bold mt-1 text-slate-200">10% Weight</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div id="pa-resolution-module" class="bg-slate-950 border-l-4 border border-slate-800 rounded-xl p-4 shadow-md">
                    </div>

                <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 shadow-xl space-y-3">
                    <h3 class="text-xs uppercase tracking-wider text-slate-400 font-bold">Admission Timeline & Milestones Progress</h3>
                    <div class="relative flex justify-between items-center overflow-x-auto custom-scrollbar pb-2 pt-1 gap-2">
                        <div id="timeline-container" class="flex items-center w-full min-w-[700px] justify-between"></div>
                    </div>
                </div>

                <div class="bg-slate-950 border border-slate-800 rounded-xl p-5 shadow-xl space-y-4">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                        <h3 class="text-xs uppercase tracking-wider text-slate-400 font-bold">Coordinator Action Desk</h3>
                        <span class="text-[10px] text-slate-500">Execute tasks to accumulate checklist accuracy</span>
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2" id="workflow-actions-grid">
                        </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 space-y-3 shadow-md">
                        <h3 class="text-xs uppercase tracking-wider text-red-400 font-bold flex items-center gap-1">
                            <span>⚠️</span> Real-time At-Risk Metrics
                        </h3>
                        <div class="space-y-2 text-xs" id="risk-metrics-stack">
                            </div>
                    </div>

                    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 space-y-3 shadow-md">
                        <h3 class="text-xs uppercase tracking-wider text-teal-400 font-bold flex items-center gap-1">
                            <span>🤝</span> Interdisciplinary Care Matrix
                        </h3>
                        <div class="space-y-2 max-h-[220px] overflow-y-auto custom-scrollbar pr-1" id="coordination-stack">
                            </div>
                    </div>
                </div>

                <div id="governance-snapshot-panel" class="hidden bg-slate-950 border border-teal-800/60 rounded-xl p-4 shadow-xl text-xs space-y-2">
                    <div class="text-teal-400 font-semibold tracking-tight text-[11px] uppercase flex items-center gap-2">
                        <span>📊</span> Administrative Governance Snapshot (Industry Benchmarks)
                    </div>
                    <p class="text-slate-400 text-[11px] leading-relaxed">
                        Estimates provided for organizational auditing and validation metrics only:
                    </p>
                    <div class="grid grid-cols-3 gap-2 text-center text-[10px] font-mono mt-1">
                        <div class="bg-slate-900 border border-slate-800 p-2 rounded">
                            <div class="text-slate-500 mb-0.5">PA Turnaround</div>
                            <div class="text-slate-200 font-bold">3–5 Business Days</div>
                        </div>
                        <div class="bg-slate-900 border border-slate-800 p-2 rounded">
                            <div class="text-slate-500 mb-0.5">IP Denial Rate</div>
                            <div class="text-slate-200 font-bold">~8–10% (CMS Avg)</div>
                        </div>
                        <div class="bg-slate-900 border border-slate-800 p-2 rounded">
                            <div class="text-slate-500 mb-0.5">PA Rework Cost</div>
                            <div class="text-slate-200 font-bold">~$11 / Trans (CAQH)</div>
                        </div>
                    </div>
                </div>

                <div id="final-decision-gate" class="rounded-xl p-5 border shadow-20xl">
                    </div>

            </div>
        </section>
    </main>

    <footer class="mt-auto border-t border-slate-800 py-3 text-center text-[10px] text-slate-500 bg-slate-950">
        Simulated Operational Software Environment &bull; For Educational Training Use Only &bull; CMS Compliance Standard Mapping Applied.
    </footer>

    <script>
        // Internal State Storage
        let state = {
            provider: '',
            physician: '',
            diagnosis: '',
            admissionType: '',
            paStatus: '',
            date: '',
            tasks: {
                bed: false,
                insurance: false,
                documentation: false,
                consent: false,
                physicianOrders: false,
                notifyNursing: false,
                prepareArrival: false
            },
            appealResolved: false
        };

        const milestones = [
            "PA Review", "Insurance Verification", "Bed Assignment", "Documentation", 
            "Consent", "Patient Arrival", "Registration", "Clinical Assessment", "Admission Complete"
        ];

        // Form monitoring logic
        function checkTriggers() {
            const diag = document.getElementById('input-diagnosis').value;
            const admType = document.getElementById('input-admission-type').value;

            // Trigger CMS Banner
            const obsBanner = document.getElementById('observation-banner');
            if (admType === 'Observation') {
                obsBanner.classList.remove('hidden');
            } else {
                obsBanner.classList.add('hidden');
            }

            // Trigger Clinical Guideline Banner
            const critBanner = document.getElementById('criteria-banner');
            if (diag === 'Acute MI' || diag === 'CHF') {
                critBanner.classList.remove('hidden');
            } else {
                critBanner.classList.add('hidden');
            }
        }

        // Action Trigger from Input Data Matrix
        function analyzeAdmission() {
            // Map inputs to active state
            state.provider = document.getElementById('input-provider').value;
            state.physician = document.getElementById('input-physician').value;
            state.diagnosis = document.getElementById('input-diagnosis').value;
            state.admissionType = document.getElementById('input-admission-type').value;
            state.paStatus = document.getElementById('input-pa-status').value;
            state.date = document.getElementById('input-date').value || "Undated";

            // Reset workflows if analyzing fresh setup
            state.appealResolved = false;

            // Switch views
            document.getElementById('placeholder-view').classList.add('hidden');
            document.getElementById('simulation-view').classList.remove('hidden');

            recalculateReadiness();
        }

        function toggleTask(taskKey) {
            state.tasks[taskKey] = !state.tasks[taskKey];
            recalculateReadiness();
        }

        function resolvePAAppeal() {
            state.appealResolved = true;
            state.paStatus = "Approved";
            recalculateReadiness();
        }

        function recalculateReadiness() {
            let score = 0;

            // 1. Prior Auth Segment Weights (25%)
            let paScore = 0;
            if (state.paStatus === "Approved") {
                paScore = 25;
            } else if (state.paStatus === "Pending") {
                paScore = 10;
            } else if (state.paStatus === "Denied") {
                paScore = 0;
            }
            score += paScore;

            // Task Mapping Weights
            // Clinical Docs: 20%
            if (state.tasks.documentation) score += 20;
            // Physician Orders: 20%
            if (state.tasks.physicianOrders) score += 20;
            // Insurance Verification: 15%
            if (state.tasks.insurance) score += 15;
            // Patient Consent: 10%
            if (state.tasks.consent) score += 10;
            // Bed Allocation: 10%
            if (state.tasks.bed) score += 10;

            // Hard Stop Constraint Gate Rule: Denied PA + ICU admission cannot reach 70% from admin tasks alone.
            if (document.getElementById('input-pa-status').value === "Denied" && !state.appealResolved && state.admissionType === "ICU") {
                if (score >= 70) {
                    score = 68; // Hard Capped maximum ceiling
                }
            }

            // Display updates
            updateUI(score);
        }

        function updateUI(score) {
            // Update Score counter
            const scoreEl = document.getElementById('readiness-score');
            scoreEl.innerText = `${score}%`;

            // Adjust Color badge depending on current bounds
            const badge = document.getElementById('readiness-status-badge');
            if (score < 60) {
                badge.className = "font-bold uppercase tracking-wider px-1.5 py-0.5 rounded text-[10px] bg-red-500/20 text-red-400 border border-red-500/30";
                badge.innerText = "Critical Impediment";
            } else if (score < 90) {
                badge.className = "font-bold uppercase tracking-wider px-1.5 py-0.5 rounded text-[10px] bg-amber-500/20 text-amber-400 border border-amber-500/30";
                badge.innerText = "Incomplete Workflows";
            } else {
                badge.className = "font-bold uppercase tracking-wider px-1.5 py-0.5 rounded text-[10px] bg-emerald-500/20 text-emerald-400 border border-emerald-500/30";
                badge.innerText = "Ready For Intake";
            }

            // Render Prior Auth Control Card Content Dynamically
            renderPAControl();

            // Render Milestones Roadmap Component
            renderMilestones(score);

            // Render Operational Actions Checkboxes
            renderActionsGrid();

            // Render Risk Assessment Panel
            renderRiskProfile();

            // Render Care Collaboration Network
            renderCareNetwork();

            // Check Governance Snapshot Condition (Threshold >= 75%)
            const govPanel = document.getElementById('governance-snapshot-panel');
            if (score >= 75) {
                govPanel.classList.remove('hidden');
            } else {
                govPanel.classList.add('hidden');
            }

            // Final Decision Component Mapping
            renderFinalDecisionGate(score);
        }

        function renderPAControl() {
            const container = document.getElementById('pa-resolution-module');
            const origStatus = document.getElementById('input-pa-status').value;
            
            if (state.appealResolved) {
                container.className = "bg-slate-950 border-l-4 border-emerald-500 border border-slate-800 rounded-xl p-4 shadow-md text-xs space-y-2";
                container.innerHTML = `
                    <div class="flex items-center justify-between">
                        <span class="font-bold text-emerald-400 flex items-center gap-1">🛡️ Appeal Successfully Processed</span>
                        <span class="text-[10px] bg-emerald-500/10 text-emerald-400 px-2 py-0.5 rounded font-mono">Status Override: Approved</span>
                    </div>
                    <p class="text-slate-400 text-[11px]">The operational bottleneck has been mitigated. The original administrative denial record has been converted via formal authorization escalation.</p>
                `;
                return;
            }

            if (origStatus === "Approved") {
                container.className = "bg-slate-950 border-l-4 border-emerald-500 border border-slate-800 rounded-xl p-4 shadow-md text-xs space-y-1";
                container.innerHTML = `
                    <span class="font-bold text-emerald-400 block">✓ Prior Authorization Verified</span>
                    <p class="text-slate-400 text-[11px]">Payer network clears medical necessity requirements for immediate treatment progression tracking.</p>
                `;
            } else if (origStatus === "Pending") {
                container.className = "bg-slate-950 border-l-4 border-amber-500 border border-slate-800 rounded-xl p-4 shadow-md text-xs space-y-3";
                container.innerHTML = `
                    <div>
                        <span class="font-bold text-amber-400 block">⏳ Attention Required: Prior Authorization Pending</span>
                        <p class="text-slate-400 text-[11px] mt-0.5">Insurance network verification pipeline requires active data facilitation protocols.</p>
                    </div>
                    <div class="flex flex-wrap gap-2">
                        <button onclick="toggleTask('documentation')" class="bg-slate-900 border border-slate-700 hover:border-slate-500 text-slate-300 px-2 py-1 rounded text-[10px] font-medium transition">⚡ Follow Up Status</button>
                        <button onclick="toggleTask('documentation')" class="bg-slate-900 border border-slate-700 hover:border-slate-500 text-slate-300 px-2 py-1 rounded text-[10px] font-medium transition">📁 Upload Clinical Docs</button>
                        <button onclick="toggleTask('physicianOrders')" class="bg-slate-900 border border-slate-700 hover:border-slate-500 text-slate-300 px-2 py-1 rounded text-[10px] font-medium transition">📞 Contact Attending MD</button>
                    </div>
                `;
            } else if (origStatus === "Denied") {
                container.className = "bg-slate-950 border-l-4 border-rose-500 border border-slate-800 rounded-xl p-4 shadow-md text-xs space-y-3";
                container.innerHTML = `
                    <div>
                        <span class="font-bold text-rose-400 block">🛑 Escalation Notice: Prior Authorization Denied</span>
                        <p class="text-slate-400 text-[11px] mt-0.5">Payer flags admission request as failing basic administrative validation matrix items.</p>
                    </div>
                    <div class="flex flex-wrap gap-2">
                        <button class="bg-slate-900 border border-slate-700 text-slate-400 px-2 py-1 rounded text-[10px] font-medium cursor-not-allowed">🔍 Review Code Reasons</button>
                        <button class="bg-slate-900 border border-slate-700 text-slate-400 px-2 py-1 rounded text-[10px] font-medium cursor-not-allowed">🏢 Contact Payer Auditor</button>
                        <button onclick="resolvePAAppeal()" class="bg-rose-500/20 text-rose-300 border border-rose-500/40 hover:bg-rose-500 hover:text-slate-950 px-2.5 py-1 rounded text-[10px] font-bold transition">⚖️ Execute Formal Appeal Escalation</button>
                    </div>
                `;
            }
        }

        function renderMilestones(score) {
            const container = document.getElementById('timeline-container');
            container.innerHTML = '';

            // Calculate active steps based on score bounds
            let completedSteps = 1; 
            if (score >= 40) completedSteps = 3;
            if (score >= 60) completedSteps = 5;
            if (score >= 75) completedSteps = 7;
            if (score >= 90) completedSteps = 9;

            milestones.forEach((name, idx) => {
                const isComplete = idx < completedSteps;
                const isLast = idx === milestones.length - 1;

                const stepHtml = `
                    <div class="flex items-center space-x-1 text-[10px]">
                        <span class="w-4 h-4 rounded-full flex items-center justify-center font-bold font-mono ${isComplete ? 'bg-teal-500 text-slate-900' : 'bg-slate-800 text-slate-500 border border-slate-700'}">
                            ${isComplete ? '✓' : idx + 1}
                        </span>
                        <span class="${isComplete ? 'text-slate-200 font-medium' : 'text-slate-500'} tracking-tight whitespace-nowrap">${name}</span>
                        ${!isLast ? `<span class="text-slate-700 mx-1 font-mono text-[9px]">&rarr;</span>` : ''}
                    </div>
                `;
                container.innerHTML += stepHtml;
            });
        }

        function renderActionsGrid() {
            const container = document.getElementById('workflow-actions-grid');
            container.innerHTML = '';

            const actionConfig = [
                { key: 'bed', label: 'Assign & Verify Bed Bedside Match' },
                { key: 'insurance', label: 'Complete Eligibility Verification' },
                { key: 'documentation', label: 'Compile Intake Documentation Bundle' },
                { key: 'consent', label: 'Execute Signatures For Legal Consent' },
                { key: 'physicianOrders', label: 'Re-verify Signed Attending Orders' },
                { key: 'notifyNursing', label: 'Notify Receiving Nursing Floor Coordinator' },
                { key: 'prepareArrival', label: 'Flag Patient Arrival Status Log' }
            ];

            actionConfig.forEach(item => {
                const isChecked = state.tasks[item.key];
                const cardHtml = `
                    <label class="flex items-center gap-3 bg-slate-900 border ${isChecked ? 'border-teal-500/40 bg-teal-950/10' : 'border-slate-800'} p-2.5 rounded-lg cursor-pointer hover:bg-slate-850 transition select-none text-xs">
                        <input type="checkbox" ${isChecked ? 'checked' : ''} onchange="toggleTask('${item.key}')" class="w-3.5 h-3.5 accent-teal-500 bg-slate-950 border-slate-700 rounded focus:ring-0 focus:ring-offset-0">
                        <span class="${isChecked ? 'text-teal-300 font-medium' : 'text-slate-400'}">${item.label}</span>
                    </label>
                `;
                container.innerHTML += cardHtml;
            });
        }

        function renderRiskProfile() {
            const container = document.getElementById('risk-metrics-stack');
            container.innerHTML = '';

            // Higher weight if specific triggers match
            const isHighClinical = (state.diagnosis === 'Acute MI' || state.diagnosis === 'CHF' || state.admissionType === 'ICU');

            const risks = [
                { name: 'Documentation Deficit Risk', active: !state.tasks.documentation, severity: 'Medium' },
                { name: 'Insurance Coverage Audit Risk', active: !state.tasks.insurance || state.paStatus !== 'Approved', severity: state.paStatus === 'Denied' ? 'Critical' : 'High' },
                { name: 'Bed Availability Conflict Risk', active: !state.tasks.bed, severity: 'Low' },
                { name: 'Clinical Safety & Necessity Risk', active: true, severity: isHighClinical ? 'High Priority' : 'Routine' }
            ];

            risks.forEach(r => {
                let badgeClass = "bg-slate-800 text-slate-400";
                if (r.severity === 'Critical') badgeClass = "bg-rose-500/20 text-rose-400 border border-rose-500/30 font-bold";
                if (r.severity === 'High' || r.severity === 'High Priority') badgeClass = "bg-orange-500/20 text-orange-400 border border-orange-500/30 font-bold";
                if (r.severity === 'Medium') badgeClass = "bg-amber-500/20 text-amber-400 border border-amber-500/30";

                const row = `
                    <div class="flex items-center justify-between p-1.5 rounded bg-slate-900/60 border border-slate-850 ${r.active ? 'opacity-100' : 'opacity-40 line-through text-slate-600'}">
                        <span>${r.name}</span>
                        <span class="text-[9px] uppercase tracking-wider px-1.5 py-0.2 rounded font-mono ${badgeClass}">${r.active ? r.severity : 'Resolved'}</span>
                    </div>
                `;
                container.innerHTML += row;
            });
        }

        function renderCareNetwork() {
            const container = document.getElementById('coordination-stack');
            container.innerHTML = '';

            const roles = [
                { title: 'Attending Physician', desc: `Assigned: ${state.physician}. Responsible for signing official intake authorization metrics.` },
                { title: 'Case Manager', desc: 'Monitors ongoing transition targets and clinical safety status parameters.' },
                { title: 'Nursing Lead Shift Supervisor', desc: 'Requires proactive bed coordination notification prior to emergency vehicle offload vectors.' },
                { title: 'Utilization Review (UR) Specialist', desc: 'Reviews documentation under concurrent review frameworks to mitigate denial risk identification using InterQual and Milliman criteria suites.' },
                { title: 'Discharge Planner', desc: 'Triggers active evaluation models to maintain safe structural exit criteria compliance.' }
            ];

            roles.forEach(role => {
                const card = `
                    <div class="bg-slate-900 border border-slate-800 p-2 rounded text-[11px] space-y-0.5">
                        <div class="font-bold text-slate-300 tracking-tight">${role.title}</div>
                        <p class="text-slate-400 text-[10px] leading-tight">${role.desc}</p>
                    </div>
                `;
                container.innerHTML += card;
            });
        }

        function renderFinalDecisionGate(score) {
            const container = document.getElementById('final-decision-gate');
            
            if (score >= 90) {
                container.className = "rounded-xl p-5 border border-emerald-500/40 bg-gradient-to-br from-slate-950 to-emerald-950/20 shadow-2xl text-xs space-y-3";
                container.innerHTML = `
                    <div class="flex items-center gap-2 text-emerald-400 text-sm font-bold">
                        <span>✅</span> ADMISSION GATEWAY CLEAR: Case Ready For Execution
                    </div>
                    <div class="text-slate-300 space-y-2 leading-relaxed">
                        <p>All core governance validation standards have been checked successfully. Prior Authorization has been captured, medical necessity criteria aligned with care tracking guidelines, and systemic checks stand resolved.</p>
                        <div class="bg-slate-900/80 border border-slate-800 p-3 rounded-md space-y-1 text-[11px] font-mono">
                            <div class="text-slate-500 font-semibold uppercase tracking-wider text-[10px] mb-1">Intake Metadata Summary File</div>
                            <div>&middot; Designated Service: <span class="text-teal-400">${state.admissionType}</span></div>
                            <div>&middot; Target Specialty: <span class="text-teal-400">${state.diagnosis}</span></div>
                            <div>&middot; Responsible Clinician: <span class="text-slate-300">${state.physician}</span></div>
                            <div>&middot; Verified Insurance Carrier: <span class="text-slate-300">${state.provider}</span></div>
                        </div>
                    </div>
                `;
            } else {
                // Compile remaining missing checklist requirements text dynamically
                let remainingNeeds = [];
                if (state.paStatus !== 'Approved') remainingNeeds.push("Resolve pending/denied prior auth insurance authorization");
                if (!state.tasks.documentation) remainingNeeds.push("Compile complete intake documentation bundle data");
                if (!state.tasks.physicianOrders) remainingNeeds.push("Obtain signed physician intake credentials updates");
                if (!state.tasks.insurance) remainingNeeds.push("Execute comprehensive insurance eligibility processing checks");
                if (!state.tasks.consent) remainingNeeds.push("Collect signed patient validation legal consent sheets");
                if (!state.tasks.bed) remainingNeeds.push("Allocate structural bedside placement unit targets");

                container.className = "rounded-xl p-5 border border-amber-500/30 bg-gradient-to-br from-slate-950 to-amber-950/10 shadow-xl text-xs space-y-3";
                container.innerHTML = `
                    <div class="flex items-center gap-2 text-amber-400 text-sm font-bold">
                        <span>⚠️</span> SYSTEM TIMEOUT: Administrative Intake Hold Required
                    </div>
                    <p class="text-slate-300 leading-relaxed text-[11px]">
                        The aggregate readiness index (${score}%) rests beneath the standard regulatory target boundary of 90%. Processing intake now incurs substantial systemic institutional financial and denial exposure risk vectors.
                    </p>
                    <div class="space-y-1.5 text-[11px]">
                        <span class="block font-bold text-slate-400 uppercase tracking-wide text-[10px]">Blocking Actions Required:</span>
                        <ul class="list-disc list-inside space-y-1 text-amber-300 font-medium">
                            ${remainingNeeds.map(item => `<li>${item}</li>`).join('')}
                        </ul>
                    </div>
                `;
            }
        }
    </script>
</body>
</html>

```
[day28.hospital.html](https://github.com/user-attachments/files/29608056/day28.hospital.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hospital Admission Readiness Simulator</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; }
        .custom-scrollbar::-webkit-scrollbar { width: 6px; height: 6px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: #f1f5f9; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
    </style>
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen flex flex-col antialiased selection:bg-teal-500 selection:text-slate-900">

    <header class="border-b border-slate-800 bg-slate-900/80 backdrop-blur sticky top-0 z-50 px-6 py-4 flex items-center justify-between">
        <div class="flex items-center space-x-3">
            <div class="p-2 bg-gradient-to-br from-teal-500 to-emerald-600 rounded-lg text-slate-900 font-bold shadow-lg shadow-teal-500/10">
                🏥
            </div>
            <div>
                <h1 class="text-lg font-semibold tracking-tight text-white flex items-center gap-2">
                    Hospital Admission Readiness Simulator
                </h1>
                <p class="text-xs text-slate-400">Role: <span class="text-teal-400 font-medium">Admission Coordinator</span> &middot; Instructive Training Platform</p>
            </div>
        </div>
        <div class="flex items-center space-x-2 bg-slate-800/60 px-3 py-1.5 rounded-md border border-slate-700/60 text-xs">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            <span class="text-slate-300 font-mono tracking-wider">SYSTEM ACTIVE</span>
        </div>
    </header>

    <main class="flex-1 max-w-7xl w-full mx-auto p-4 md:p-6 grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        
        <section class="lg:col-span-5 bg-slate-950 border border-slate-800 rounded-xl p-5 shadow-xl space-y-5">
            <div class="border-b border-slate-800 pb-3 flex justify-between items-center">
                <div class="flex items-center gap-2">
                    <span class="text-xs uppercase tracking-wider text-teal-400 font-bold bg-teal-950/60 px-2 py-0.5 rounded border border-teal-800/40">Step 1</span>
                    <h2 class="text-sm font-semibold text-slate-200">Admission Parameter Matrix</h2>
                </div>
                <span class="text-[10px] text-amber-500/90 font-medium bg-amber-500/10 border border-amber-500/20 px-2 py-0.5 rounded">
                    ⚠️ Illustrative Training Data
                </span>
            </div>

            <div class="space-y-4 text-xs">
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-slate-400 font-medium mb-1.5">Payer/Provider Organization</label>
                        <select id="input-provider" class="w-full bg-slate-900 border border-slate-700 rounded-md p-2 text-slate-200 focus:outline-none focus:border-teal-500">
                            <option value="Apex Health Mutual">Apex Health Mutual</option>
                            <option value="Beacon Care Network">Beacon Care Network</option>
                            <option value="Summit Medicare Advantage">Summit Medicare Advantage</option>
                            <option value="Horizon Assurance Corp">Horizon Assurance Corp</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-slate-400 font-medium mb-1.5">Attending Physician</label>
                        <select id="input-physician" class="w-full bg-slate-900 border border-slate-700 rounded-md p-2 text-slate-200 focus:outline-none focus:border-teal-500">
                            <option value="Dr. Evelyn Vance, MD (Cardiology)">Dr. Evelyn Vance, MD</option>
                            <option value="Dr. Marcus Thorne, MD (Internal Medicine)">Dr. Marcus Thorne, MD</option>
                            <option value="Dr. Alistair Vance, MD (Orthopedics)">Dr. Alistair Vance, MD</option>
                            <option value="Dr. Sarah Jenkins, MD (General Surgery)">Dr. Sarah Jenkins, MD</option>
                        </select>
                    </div>
                </div>

                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-slate-400 font-medium mb-1.5">Principal Diagnosis</label>
                        <select id="input-diagnosis" onchange="checkTriggers()" class="w-full bg-slate-900 border border-slate-700 rounded-md p-2 text-slate-200 focus:outline-none focus:border-teal-500">
                            <option value="Acute MI">Acute MI (Myocardial Infarction)</option>
                            <option value="CHF">CHF (Congestive Heart Failure)</option>
                            <option value="Pneumonia">Pneumonia</option>
                            <option value="Elective Surgery">Elective Surgery</option>
                            <option value="Hip Fracture">Hip Fracture</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-slate-400 font-medium mb-1.5">Admission Designation</label>
                        <select id="input-admission-type" onchange="checkTriggers()" class="w-full bg-slate-900 border border-slate-700 rounded-md p-2 text-slate-200 focus:outline-none focus:border-teal-500">
                            <option value="Inpatient">Inpatient Admission</option>
                            <option value="Observation">Observation Status</option>
                            <option value="Emergency">Emergency Tracking</option>
                            <option value="ICU">ICU Placement</option>
                            <option value="Same-Day Surgery">Same-Day Surgery</option>
                        </select>
                    </div>
                </div>

                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-slate-400 font-medium mb-1.5">Initial Prior Auth (PA) Status</label>
                        <select id="input-pa-status" class="w-full bg-slate-900 border border-slate-700 rounded-md p-2 text-slate-200 font-semibold focus:outline-none focus:border-teal-500">
                            <option value="Approved" class="text-emerald-400">Approved</option>
                            <option value="Pending" class="text-amber-400" selected>Pending Verification</option>
                            <option value="Denied" class="text-rose-400">Denied / Rejected</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-slate-400 font-medium mb-1.5">Admission Scheduled Date</label>
                        <input type="date" id="input-date" class="w-full bg-slate-900 border border-slate-700 rounded-md p-2 text-slate-200 focus:outline-none focus:border-teal-500">
                    </div>
                </div>

                <div id="observation-banner" class="hidden bg-amber-500/10 border border-amber-500/30 rounded-lg p-3 text-amber-300 space-y-1">
                    <div class="flex items-center gap-1.5 font-semibold text-[11px]">
                        <span>⚖️</span> Regulatory Mandate: CMS 2-Midnight Rule
                    </div>
                    <p class="text-[11px] leading-relaxed opacity-90">
                        CMS 2-Midnight Rule applies — different cost-sharing, SNF eligibility, and billing than inpatient. Medicare patients require written MOON notification.
                    </p>
                </div>

                <div id="criteria-banner" class="hidden bg-blue-500/10 border border-blue-500/30 rounded-lg p-3 text-blue-300 space-y-1">
                    <div class="flex items-center gap-1.5 font-semibold text-[11px]">
                        <span>📋</span> Clinical Guideline Triggered
                    </div>
                    <p class="text-[11px] leading-relaxed opacity-90">
                        InterQual/Milliman thresholds apply — ensure documentation meets medical necessity standards before UR review.
                    </p>
                </div>

                <button onclick="analyzeAdmission()" class="w-full bg-gradient-to-r from-teal-500 to-emerald-600 hover:from-teal-400 hover:to-emerald-500 text-slate-950 font-bold py-2.5 px-4 rounded-md transition duration-200 flex items-center justify-center gap-2 text-sm shadow-md shadow-emerald-950/50 mt-2">
                    🏥 Analyze Admission Readiness
                </button>
            </div>
        </section>

        <section class="lg:col-span-7 space-y-6">
            
            <div id="placeholder-view" class="bg-slate-950 border border-slate-800 border-dashed rounded-xl p-12 text-center flex flex-col items-center justify-center min-h-[350px]">
                <div class="text-4xl opacity-40 mb-3">📋</div>
                <h3 class="text-slate-300 font-medium text-sm">Awaiting Case Submission</h3>
                <p class="text-xs text-slate-500 max-w-sm mt-1 mx-auto">
                    Fill in the required provider matrix on the left panel and activate analysis to populate metrics, milestones, and workflow configurations.
                </p>
            </div>

            <div id="simulation-view" class="hidden space-y-6">
                
                <div class="bg-slate-950 border border-slate-800 rounded-xl p-5 shadow-xl grid grid-cols-1 md:grid-cols-12 gap-5 items-center">
                    <div class="md:col-span-4 text-center md:text-left border-b md:border-b-0 md:border-r border-slate-800 pb-4 md:pb-0 md:pr-4">
                        <div class="text-xs text-slate-400 font-medium">Readiness Index Evaluation</div>
                        <div class="flex items-baseline justify-center md:justify-start gap-1 mt-1">
                            <span id="readiness-score" class="text-4xl font-extrabold tracking-tight text-white">0%</span>
                            <span class="text-xs text-slate-500">/100%</span>
                        </div>
                        <div class="mt-2 text-[11px]">
                            Status: <span id="readiness-status-badge" class="font-bold uppercase tracking-wider px-1.5 py-0.5 rounded text-[10px]">Evaluating</span>
                        </div>
                    </div>
                    
                    <div class="md:col-span-8 space-y-2">
                        <div class="text-[11px] uppercase tracking-wider font-semibold text-slate-400 flex justify-between">
                            <span>System Attribute Weighting Matrix</span>
                            <span class="text-[10px] text-teal-400 lowercase italic">Realtime Impact Mapping</span>
                        </div>
                        <div class="grid grid-cols-3 gap-2 text-[10px] text-slate-300">
                            <div class="bg-slate-900 border border-slate-800 p-1.5 rounded flex flex-col justify-between">
                                <span class="text-slate-500">Prior Auth</span>
                                <span class="font-bold mt-1 text-slate-200">25% Weight</span>
                            </div>
                            <div class="bg-slate-900 border border-slate-800 p-1.5 rounded flex flex-col justify-between">
                                <span class="text-slate-500">Clinical Docs</span>
                                <span class="font-bold mt-1 text-slate-200">20% Weight</span>
                            </div>
                            <div class="bg-slate-900 border border-slate-800 p-1.5 rounded flex flex-col justify-between">
                                <span class="text-slate-500">MD Orders</span>
                                <span class="font-bold mt-1 text-slate-200">20% Weight</span>
                            </div>
                            <div class="bg-slate-900 border border-slate-800 p-1.5 rounded flex flex-col justify-between">
                                <span class="text-slate-500">Insurance Verify</span>
                                <span class="font-bold mt-1 text-slate-200">15% Weight</span>
                            </div>
                            <div class="bg-slate-900 border border-slate-800 p-1.5 rounded flex flex-col justify-between">
                                <span class="text-slate-500">Patient Consent</span>
                                <span class="font-bold mt-1 text-slate-200">10% Weight</span>
                            </div>
                            <div class="bg-slate-900 border border-slate-800 p-1.5 rounded flex flex-col justify-between">
                                <span class="text-slate-500">Bed Allocation</span>
                                <span class="font-bold mt-1 text-slate-200">10% Weight</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div id="pa-resolution-module" class="bg-slate-950 border-l-4 border border-slate-800 rounded-xl p-4 shadow-md">
                    </div>

                <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 shadow-xl space-y-3">
                    <h3 class="text-xs uppercase tracking-wider text-slate-400 font-bold">Admission Timeline & Milestones Progress</h3>
                    <div class="relative flex justify-between items-center overflow-x-auto custom-scrollbar pb-2 pt-1 gap-2">
                        <div id="timeline-container" class="flex items-center w-full min-w-[700px] justify-between"></div>
                    </div>
                </div>

                <div class="bg-slate-950 border border-slate-800 rounded-xl p-5 shadow-xl space-y-4">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                        <h3 class="text-xs uppercase tracking-wider text-slate-400 font-bold">Coordinator Action Desk</h3>
                        <span class="text-[10px] text-slate-500">Execute tasks to accumulate checklist accuracy</span>
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2" id="workflow-actions-grid">
                        </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 space-y-3 shadow-md">
                        <h3 class="text-xs uppercase tracking-wider text-red-400 font-bold flex items-center gap-1">
                            <span>⚠️</span> Real-time At-Risk Metrics
                        </h3>
                        <div class="space-y-2 text-xs" id="risk-metrics-stack">
                            </div>
                    </div>

                    <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 space-y-3 shadow-md">
                        <h3 class="text-xs uppercase tracking-wider text-teal-400 font-bold flex items-center gap-1">
                            <span>🤝</span> Interdisciplinary Care Matrix
                        </h3>
                        <div class="space-y-2 max-h-[220px] overflow-y-auto custom-scrollbar pr-1" id="coordination-stack">
                            </div>
                    </div>
                </div>

                <div id="governance-snapshot-panel" class="hidden bg-slate-950 border border-teal-800/60 rounded-xl p-4 shadow-xl text-xs space-y-2">
                    <div class="text-teal-400 font-semibold tracking-tight text-[11px] uppercase flex items-center gap-2">
                        <span>📊</span> Administrative Governance Snapshot (Industry Benchmarks)
                    </div>
                    <p class="text-slate-400 text-[11px] leading-relaxed">
                        Estimates provided for organizational auditing and validation metrics only:
                    </p>
                    <div class="grid grid-cols-3 gap-2 text-center text-[10px] font-mono mt-1">
                        <div class="bg-slate-900 border border-slate-800 p-2 rounded">
                            <div class="text-slate-500 mb-0.5">PA Turnaround</div>
                            <div class="text-slate-200 font-bold">3–5 Business Days</div>
                        </div>
                        <div class="bg-slate-900 border border-slate-800 p-2 rounded">
                            <div class="text-slate-500 mb-0.5">IP Denial Rate</div>
                            <div class="text-slate-200 font-bold">~8–10% (CMS Avg)</div>
                        </div>
                        <div class="bg-slate-900 border border-slate-800 p-2 rounded">
                            <div class="text-slate-500 mb-0.5">PA Rework Cost</div>
                            <div class="text-slate-200 font-bold">~$11 / Trans (CAQH)</div>
                        </div>
                    </div>
                </div>

                <div id="final-decision-gate" class="rounded-xl p-5 border shadow-20xl">
                    </div>

            </div>
        </section>
    </main>

    <footer class="mt-auto border-t border-slate-800 py-3 text-center text-[10px] text-slate-500 bg-slate-950">
        Simulated Operational Software Environment &bull; For Educational Training Use Only &bull; CMS Compliance Standard Mapping Applied.
    </footer>

    <script>
        // Internal State Storage
        let state = {
            provider: '',
            physician: '',
            diagnosis: '',
            admissionType: '',
            paStatus: '',
            date: '',
            tasks: {
                bed: false,
                insurance: false,
                documentation: false,
                consent: false,
                physicianOrders: false,
                notifyNursing: false,
                prepareArrival: false
            },
            appealResolved: false
        };

        const milestones = [
            "PA Review", "Insurance Verification", "Bed Assignment", "Documentation", 
            "Consent", "Patient Arrival", "Registration", "Clinical Assessment", "Admission Complete"
        ];

        // Form monitoring logic
        function checkTriggers() {
            const diag = document.getElementById('input-diagnosis').value;
            const admType = document.getElementById('input-admission-type').value;

            // Trigger CMS Banner
            const obsBanner = document.getElementById('observation-banner');
            if (admType === 'Observation') {
                obsBanner.classList.remove('hidden');
            } else {
                obsBanner.classList.add('hidden');
            }

            // Trigger Clinical Guideline Banner
            const critBanner = document.getElementById('criteria-banner');
            if (diag === 'Acute MI' || diag === 'CHF') {
                critBanner.classList.remove('hidden');
            } else {
                critBanner.classList.add('hidden');
            }
        }

        // Action Trigger from Input Data Matrix
        function analyzeAdmission() {
            // Map inputs to active state
            state.provider = document.getElementById('input-provider').value;
            state.physician = document.getElementById('input-physician').value;
            state.diagnosis = document.getElementById('input-diagnosis').value;
            state.admissionType = document.getElementById('input-admission-type').value;
            state.paStatus = document.getElementById('input-pa-status').value;
            state.date = document.getElementById('input-date').value || "Undated";

            // Reset workflows if analyzing fresh setup
            state.appealResolved = false;

            // Switch views
            document.getElementById('placeholder-view').classList.add('hidden');
            document.getElementById('simulation-view').classList.remove('hidden');

            recalculateReadiness();
        }

        function toggleTask(taskKey) {
            state.tasks[taskKey] = !state.tasks[taskKey];
            recalculateReadiness();
        }

        function resolvePAAppeal() {
            state.appealResolved = true;
            state.paStatus = "Approved";
            recalculateReadiness();
        }

        function recalculateReadiness() {
            let score = 0;

            // 1. Prior Auth Segment Weights (25%)
            let paScore = 0;
            if (state.paStatus === "Approved") {
                paScore = 25;
            } else if (state.paStatus === "Pending") {
                paScore = 10;
            } else if (state.paStatus === "Denied") {
                paScore = 0;
            }
            score += paScore;

            // Task Mapping Weights
            // Clinical Docs: 20%
            if (state.tasks.documentation) score += 20;
            // Physician Orders: 20%
            if (state.tasks.physicianOrders) score += 20;
            // Insurance Verification: 15%
            if (state.tasks.insurance) score += 15;
            // Patient Consent: 10%
            if (state.tasks.consent) score += 10;
            // Bed Allocation: 10%
            if (state.tasks.bed) score += 10;

            // Hard Stop Constraint Gate Rule: Denied PA + ICU admission cannot reach 70% from admin tasks alone.
            if (document.getElementById('input-pa-status').value === "Denied" && !state.appealResolved && state.admissionType === "ICU") {
                if (score >= 70) {
                    score = 68; // Hard Capped maximum ceiling
                }
            }

            // Display updates
            updateUI(score);
        }

        function updateUI(score) {
            // Update Score counter
            const scoreEl = document.getElementById('readiness-score');
            scoreEl.innerText = `${score}%`;

            // Adjust Color badge depending on current bounds
            const badge = document.getElementById('readiness-status-badge');
            if (score < 60) {
                badge.className = "font-bold uppercase tracking-wider px-1.5 py-0.5 rounded text-[10px] bg-red-500/20 text-red-400 border border-red-500/30";
                badge.innerText = "Critical Impediment";
            } else if (score < 90) {
                badge.className = "font-bold uppercase tracking-wider px-1.5 py-0.5 rounded text-[10px] bg-amber-500/20 text-amber-400 border border-amber-500/30";
                badge.innerText = "Incomplete Workflows";
            } else {
                badge.className = "font-bold uppercase tracking-wider px-1.5 py-0.5 rounded text-[10px] bg-emerald-500/20 text-emerald-400 border border-emerald-500/30";
                badge.innerText = "Ready For Intake";
            }

            // Render Prior Auth Control Card Content Dynamically
            renderPAControl();

            // Render Milestones Roadmap Component
            renderMilestones(score);

            // Render Operational Actions Checkboxes
            renderActionsGrid();

            // Render Risk Assessment Panel
            renderRiskProfile();

            // Render Care Collaboration Network
            renderCareNetwork();

            // Check Governance Snapshot Condition (Threshold >= 75%)
            const govPanel = document.getElementById('governance-snapshot-panel');
            if (score >= 75) {
                govPanel.classList.remove('hidden');
            } else {
                govPanel.classList.add('hidden');
            }

            // Final Decision Component Mapping
            renderFinalDecisionGate(score);
        }

        function renderPAControl() {
            const container = document.getElementById('pa-resolution-module');
            const origStatus = document.getElementById('input-pa-status').value;
            
            if (state.appealResolved) {
                container.className = "bg-slate-950 border-l-4 border-emerald-500 border border-slate-800 rounded-xl p-4 shadow-md text-xs space-y-2";
                container.innerHTML = `
                    <div class="flex items-center justify-between">
                        <span class="font-bold text-emerald-400 flex items-center gap-1">🛡️ Appeal Successfully Processed</span>
                        <span class="text-[10px] bg-emerald-500/10 text-emerald-400 px-2 py-0.5 rounded font-mono">Status Override: Approved</span>
                    </div>
                    <p class="text-slate-400 text-[11px]">The operational bottleneck has been mitigated. The original administrative denial record has been converted via formal authorization escalation.</p>
                `;
                return;
            }

            if (origStatus === "Approved") {
                container.className = "bg-slate-950 border-l-4 border-emerald-500 border border-slate-800 rounded-xl p-4 shadow-md text-xs space-y-1";
                container.innerHTML = `
                    <span class="font-bold text-emerald-400 block">✓ Prior Authorization Verified</span>
                    <p class="text-slate-400 text-[11px]">Payer network clears medical necessity requirements for immediate treatment progression tracking.</p>
                `;
            } else if (origStatus === "Pending") {
                container.className = "bg-slate-950 border-l-4 border-amber-500 border border-slate-800 rounded-xl p-4 shadow-md text-xs space-y-3";
                container.innerHTML = `
                    <div>
                        <span class="font-bold text-amber-400 block">⏳ Attention Required: Prior Authorization Pending</span>
                        <p class="text-slate-400 text-[11px] mt-0.5">Insurance network verification pipeline requires active data facilitation protocols.</p>
                    </div>
                    <div class="flex flex-wrap gap-2">
                        <button onclick="toggleTask('documentation')" class="bg-slate-900 border border-slate-700 hover:border-slate-500 text-slate-300 px-2 py-1 rounded text-[10px] font-medium transition">⚡ Follow Up Status</button>
                        <button onclick="toggleTask('documentation')" class="bg-slate-900 border border-slate-700 hover:border-slate-500 text-slate-300 px-2 py-1 rounded text-[10px] font-medium transition">📁 Upload Clinical Docs</button>
                        <button onclick="toggleTask('physicianOrders')" class="bg-slate-900 border border-slate-700 hover:border-slate-500 text-slate-300 px-2 py-1 rounded text-[10px] font-medium transition">📞 Contact Attending MD</button>
                    </div>
                `;
            } else if (origStatus === "Denied") {
                container.className = "bg-slate-950 border-l-4 border-rose-500 border border-slate-800 rounded-xl p-4 shadow-md text-xs space-y-3";
                container.innerHTML = `
                    <div>
                        <span class="font-bold text-rose-400 block">🛑 Escalation Notice: Prior Authorization Denied</span>
                        <p class="text-slate-400 text-[11px] mt-0.5">Payer flags admission request as failing basic administrative validation matrix items.</p>
                    </div>
                    <div class="flex flex-wrap gap-2">
                        <button class="bg-slate-900 border border-slate-700 text-slate-400 px-2 py-1 rounded text-[10px] font-medium cursor-not-allowed">🔍 Review Code Reasons</button>
                        <button class="bg-slate-900 border border-slate-700 text-slate-400 px-2 py-1 rounded text-[10px] font-medium cursor-not-allowed">🏢 Contact Payer Auditor</button>
                        <button onclick="resolvePAAppeal()" class="bg-rose-500/20 text-rose-300 border border-rose-500/40 hover:bg-rose-500 hover:text-slate-950 px-2.5 py-1 rounded text-[10px] font-bold transition">⚖️ Execute Formal Appeal Escalation</button>
                    </div>
                `;
            }
        }

        function renderMilestones(score) {
            const container = document.getElementById('timeline-container');
            container.innerHTML = '';

            // Calculate active steps based on score bounds
            let completedSteps = 1; 
            if (score >= 40) completedSteps = 3;
            if (score >= 60) completedSteps = 5;
            if (score >= 75) completedSteps = 7;
            if (score >= 90) completedSteps = 9;

            milestones.forEach((name, idx) => {
                const isComplete = idx < completedSteps;
                const isLast = idx === milestones.length - 1;

                const stepHtml = `
                    <div class="flex items-center space-x-1 text-[10px]">
                        <span class="w-4 h-4 rounded-full flex items-center justify-center font-bold font-mono ${isComplete ? 'bg-teal-500 text-slate-900' : 'bg-slate-800 text-slate-500 border border-slate-700'}">
                            ${isComplete ? '✓' : idx + 1}
                        </span>
                        <span class="${isComplete ? 'text-slate-200 font-medium' : 'text-slate-500'} tracking-tight whitespace-nowrap">${name}</span>
                        ${!isLast ? `<span class="text-slate-700 mx-1 font-mono text-[9px]">&rarr;</span>` : ''}
                    </div>
                `;
                container.innerHTML += stepHtml;
            });
        }

        function renderActionsGrid() {
            const container = document.getElementById('workflow-actions-grid');
            container.innerHTML = '';

            const actionConfig = [
                { key: 'bed', label: 'Assign & Verify Bed Bedside Match' },
                { key: 'insurance', label: 'Complete Eligibility Verification' },
                { key: 'documentation', label: 'Compile Intake Documentation Bundle' },
                { key: 'consent', label: 'Execute Signatures For Legal Consent' },
                { key: 'physicianOrders', label: 'Re-verify Signed Attending Orders' },
                { key: 'notifyNursing', label: 'Notify Receiving Nursing Floor Coordinator' },
                { key: 'prepareArrival', label: 'Flag Patient Arrival Status Log' }
            ];

            actionConfig.forEach(item => {
                const isChecked = state.tasks[item.key];
                const cardHtml = `
                    <label class="flex items-center gap-3 bg-slate-900 border ${isChecked ? 'border-teal-500/40 bg-teal-950/10' : 'border-slate-800'} p-2.5 rounded-lg cursor-pointer hover:bg-slate-850 transition select-none text-xs">
                        <input type="checkbox" ${isChecked ? 'checked' : ''} onchange="toggleTask('${item.key}')" class="w-3.5 h-3.5 accent-teal-500 bg-slate-950 border-slate-700 rounded focus:ring-0 focus:ring-offset-0">
                        <span class="${isChecked ? 'text-teal-300 font-medium' : 'text-slate-400'}">${item.label}</span>
                    </label>
                `;
                container.innerHTML += cardHtml;
            });
        }

        function renderRiskProfile() {
            const container = document.getElementById('risk-metrics-stack');
            container.innerHTML = '';

            // Higher weight if specific triggers match
            const isHighClinical = (state.diagnosis === 'Acute MI' || state.diagnosis === 'CHF' || state.admissionType === 'ICU');

            const risks = [
                { name: 'Documentation Deficit Risk', active: !state.tasks.documentation, severity: 'Medium' },
                { name: 'Insurance Coverage Audit Risk', active: !state.tasks.insurance || state.paStatus !== 'Approved', severity: state.paStatus === 'Denied' ? 'Critical' : 'High' },
                { name: 'Bed Availability Conflict Risk', active: !state.tasks.bed, severity: 'Low' },
                { name: 'Clinical Safety & Necessity Risk', active: true, severity: isHighClinical ? 'High Priority' : 'Routine' }
            ];

            risks.forEach(r => {
                let badgeClass = "bg-slate-800 text-slate-400";
                if (r.severity === 'Critical') badgeClass = "bg-rose-500/20 text-rose-400 border border-rose-500/30 font-bold";
                if (r.severity === 'High' || r.severity === 'High Priority') badgeClass = "bg-orange-500/20 text-orange-400 border border-orange-500/30 font-bold";
                if (r.severity === 'Medium') badgeClass = "bg-amber-500/20 text-amber-400 border border-amber-500/30";

                const row = `
                    <div class="flex items-center justify-between p-1.5 rounded bg-slate-900/60 border border-slate-850 ${r.active ? 'opacity-100' : 'opacity-40 line-through text-slate-600'}">
                        <span>${r.name}</span>
                        <span class="text-[9px] uppercase tracking-wider px-1.5 py-0.2 rounded font-mono ${badgeClass}">${r.active ? r.severity : 'Resolved'}</span>
                    </div>
                `;
                container.innerHTML += row;
            });
        }

        function renderCareNetwork() {
            const container = document.getElementById('coordination-stack');
            container.innerHTML = '';

            const roles = [
                { title: 'Attending Physician', desc: `Assigned: ${state.physician}. Responsible for signing official intake authorization metrics.` },
                { title: 'Case Manager', desc: 'Monitors ongoing transition targets and clinical safety status parameters.' },
                { title: 'Nursing Lead Shift Supervisor', desc: 'Requires proactive bed coordination notification prior to emergency vehicle offload vectors.' },
                { title: 'Utilization Review (UR) Specialist', desc: 'Reviews documentation under concurrent review frameworks to mitigate denial risk identification using InterQual and Milliman criteria suites.' },
                { title: 'Discharge Planner', desc: 'Triggers active evaluation models to maintain safe structural exit criteria compliance.' }
            ];

            roles.forEach(role => {
                const card = `
                    <div class="bg-slate-900 border border-slate-800 p-2 rounded text-[11px] space-y-0.5">
                        <div class="font-bold text-slate-300 tracking-tight">${role.title}</div>
                        <p class="text-slate-400 text-[10px] leading-tight">${role.desc}</p>
                    </div>
                `;
                container.innerHTML += card;
            });
        }

        function renderFinalDecisionGate(score) {
            const container = document.getElementById('final-decision-gate');
            
            if (score >= 90) {
                container.className = "rounded-xl p-5 border border-emerald-500/40 bg-gradient-to-br from-slate-950 to-emerald-950/20 shadow-2xl text-xs space-y-3";
                container.innerHTML = `
                    <div class="flex items-center gap-2 text-emerald-400 text-sm font-bold">
                        <span>✅</span> ADMISSION GATEWAY CLEAR: Case Ready For Execution
                    </div>
                    <div class="text-slate-300 space-y-2 leading-relaxed">
                        <p>All core governance validation standards have been checked successfully. Prior Authorization has been captured, medical necessity criteria aligned with care tracking guidelines, and systemic checks stand resolved.</p>
                        <div class="bg-slate-900/80 border border-slate-800 p-3 rounded-md space-y-1 text-[11px] font-mono">
                            <div class="text-slate-500 font-semibold uppercase tracking-wider text-[10px] mb-1">Intake Metadata Summary File</div>
                            <div>&middot; Designated Service: <span class="text-teal-400">${state.admissionType}</span></div>
                            <div>&middot; Target Specialty: <span class="text-teal-400">${state.diagnosis}</span></div>
                            <div>&middot; Responsible Clinician: <span class="text-slate-300">${state.physician}</span></div>
                            <div>&middot; Verified Insurance Carrier: <span class="text-slate-300">${state.provider}</span></div>
                        </div>
                    </div>
                `;
            } else {
                // Compile remaining missing checklist requirements text dynamically
                let remainingNeeds = [];
                if (state.paStatus !== 'Approved') remainingNeeds.push("Resolve pending/denied prior auth insurance authorization");
                if (!state.tasks.documentation) remainingNeeds.push("Compile complete intake documentation bundle data");
                if (!state.tasks.physicianOrders) remainingNeeds.push("Obtain signed physician intake credentials updates");
                if (!state.tasks.insurance) remainingNeeds.push("Execute comprehensive insurance eligibility processing checks");
                if (!state.tasks.consent) remainingNeeds.push("Collect signed patient validation legal consent sheets");
                if (!state.tasks.bed) remainingNeeds.push("Allocate structural bedside placement unit targets");

                container.className = "rounded-xl p-5 border border-amber-500/30 bg-gradient-to-br from-slate-950 to-amber-950/10 shadow-xl text-xs space-y-3";
                container.innerHTML = `
                    <div class="flex items-center gap-2 text-amber-400 text-sm font-bold">
                        <span>⚠️</span> SYSTEM TIMEOUT: Administrative Intake Hold Required
                    </div>
                    <p class="text-slate-300 leading-relaxed text-[11px]">
                        The aggregate readiness index (${score}%) rests beneath the standard regulatory target boundary of 90%. Processing intake now incurs substantial systemic institutional financial and denial exposure risk vectors.
                    </p>
                    <div class="space-y-1.5 text-[11px]">
                        <span class="block font-bold text-slate-400 uppercase tracking-wide text-[10px]">Blocking Actions Required:</span>
                        <ul class="list-disc list-inside space-y-1 text-amber-300 font-medium">
                            ${remainingNeeds.map(item => `<li>${item}</li>`).join('')}
                        </ul>
                    </div>
                `;
            }
        }
    </script>
</body>
</html>

```
<img width="553" height="485" alt="image" src="https://github.com/user-attachments/assets/e3b4d47a-4083-40bf-8b93-e0a09409115a" />
<img width="1298" height="469" alt="image" src="https://github.com/user-attachments/assets/1b9780a5-2056-4053-8f47-7bc543021a8c" />
<img width="743" height="567" alt="image" src="https://github.com/user-attachments/assets/43a0cb39-9798-4734-ac6d-15c3418f594a" />
<img width="730" height="411" alt="image" src="https://github.com/user-attachments/assets/71c284fa-3892-4234-b2f0-6b4363bcbeed" />
<img width="773" height="439" alt="image" src="https://github.com/user-attachments/assets/c8ebb106-dbcd-4ced-a3da-624030de85a3" />
