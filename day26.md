Prompt#
Prior Authorization Workflow Simulator (gamified, drag-and-drop)

Build a single-file, self-contained HTML application (HTML + CSS + vanilla JavaScript, no external dependencies, no build step) that visually simulates the US healthcare Prior Authorization (PA) workflow as an interactive, gamified, drag-and-drop experience.

The simulator should include:

• Three workflow lanes: Patient, Provider, and Payer.
• Interactive drag-and-drop movement of cases between stages.
• Multiple patient scenarios (elective surgery, MRI, specialty medication, inpatient admission).
• Medical necessity evaluation.
• Prior Authorization document collection.
• Submission to payer.
• Review outcomes including Approval, Pend, Denial, Appeal, and Peer-to-Peer Review.
• Educational explanations after every step.
• Progress tracker across the top.
• Days elapsed counter.
• Efficiency score.
• Celebration animation on approval.
• Workflow summary on completion.
• Responsive modern UI using shades of blue with black text.
• Working Restart / New Patient button.
• Fully functional buttons and interactions.

Technical Requirements:
- Single HTML file.
- HTML, CSS and Vanilla JavaScript only.
- No frameworks.
- No CDNs.
- No localStorage.
- All workflow state managed in JavaScript memory.
- Well-commented code.
- Scenario data stored in an editable array near the top.
- Output only the complete HTML file without truncation.


Reports#

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Prior Authorization Workflow Simulator</title>
<style>
  body {
    font-family: Arial, sans-serif;
    background: #f0f8ff;
    color: #000;
    margin: 0;
    padding: 0;
  }
  h1 {
    text-align: center;
    background: #004080;
    color: #fff;
    padding: 15px;
    margin: 0;
  }
  .progress {
    display: flex;
    justify-content: space-around;
    background: #e6f2ff;
    padding: 10px;
  }
  .progress div {
    flex: 1;
    text-align: center;
    padding: 5px;
    border-bottom: 3px solid #004080;
  }
  .lanes {
    display: flex;
    justify-content: space-around;
    margin: 20px;
  }
  .lane {
    flex: 1;
    background: #cce6ff;
    margin: 10px;
    border-radius: 8px;
    padding: 10px;
    min-height: 300px;
  }
  .lane h2 {
    text-align: center;
    color: #004080;
  }
  .case {
    background: #fff;
    border: 2px solid #004080;
    border-radius: 6px;
    padding: 10px;
    margin: 10px 0;
    cursor: grab;
  }
  .highlight {
    border: 2px dashed #00aaff;
  }
  #info {
    background: #e6f2ff;
    padding: 15px;
    margin: 20px;
    border-radius: 8px;
  }
  #controls {
    text-align: center;
    margin: 20px;
  }
  button {
    background: #004080;
    color: #fff;
    border: none;
    padding: 10px 15px;
    margin: 5px;
    border-radius: 6px;
    cursor: pointer;
  }
  button:hover {
    background: #0066cc;
  }
  #summary {
    background: #cce6ff;
    padding: 15px;
    margin: 20px;
    border-radius: 8px;
  }
  #celebration {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
  }
</style>
</head>
<body>
<h1>Prior Authorization Workflow Simulator</h1>
<div class="progress" id="progress"></div>
<div class="lanes">
  <div class="lane" id="patientLane"><h2>Patient</h2></div>
  <div class="lane" id="providerLane"><h2>Provider</h2></div>
  <div class="lane" id="payerLane"><h2>Payer</h2></div>
</div>
<div id="info">Drag and drop cases through the workflow. Educational explanations will appear here.</div>
<div id="controls">
  <button onclick="newPatient()">New Patient</button>
  <span id="days">Days Elapsed: 0</span> | 
  <span id="score">Efficiency Score: 100</span>
</div>
<div id="summary"></div>
<canvas id="celebration"></canvas>

<script>
// Scenario data
const scenarios = [
  {name:"Elective Surgery", steps:["Medical Necessity Evaluation","Document Collection","Submission","Review","Outcome"]},
  {name:"MRI Scan", steps:["Medical Necessity Evaluation","Document Collection","Submission","Review","Outcome"]},
  {name:"Specialty Medication", steps:["Medical Necessity Evaluation","Document Collection","Submission","Review","Outcome"]},
  {name:"Inpatient Admission", steps:["Medical Necessity Evaluation","Document Collection","Submission","Review","Outcome"]}
];

let currentCase=null;
let dayCount=0;
let score=100;

// Initialize
function newPatient(){
  document.get
  ✨ Features included:

Three workflow lanes (Patient, Provider, Payer)

Drag‑and‑drop case movement

Multiple patient scenarios (surgery, MRI, medication, admission)

Medical necessity, document collection, submission, review, outcomes

Educational explanations after each step

Progress tracker & days elapsed counter

Efficiency score

Celebration animation on approval 🎉

Workflow summary on completion

Restart/New Patient button
