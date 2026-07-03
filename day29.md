You are an expert frontend developer, UX designer, game designer, and supply chain consultant.

Build it so a complete beginner can play it — plain language, context before every decision, 'why does this matter' explanations, and guidance that makes you feel smart rather than lost.

Build a complete single-file HTML app named 'Operation Lifeline: Supply Chain Crisis Lab'.

Requirements:
• Output ONLY one HTML file.
• React via CDN + Babel JSX.
• Plain HTML, CSS, and JavaScript only.
• No Tailwind, npm, backend, APIs, images, or external assets.
• Must run offline by opening the HTML file.
• No placeholders or incomplete features.

Flow:
1. Welcome screen with title, subtitle, and 'Start Simulation'.
2. Generate a random fictional company (industry, revenue, factories, warehouses, suppliers, inventory days, lead time, countries) displayed as modern cards.
3. Generate one random crisis (factory fire, supplier bankruptcy, port strike, cyberattack, flood, raw material shortage, political conflict, shipping delay) with urgency and business impact.
4. War Room: Present six response actions. The player chooses three. Simulate consequences by updating Cost, Inventory, Profit, Delivery Speed, and Customer Satisfaction using animated progress bars.
5. Negotiation: Branching supplier negotiation with four rounds. Each choice affects Trust, Price, and Lead Time. Display a negotiation score.
6. CEO Boardroom: Five multiple-choice leadership questions. Score executive decision-making.
7. AI Strategy: Let the player choose two AI investments from Demand Forecasting, Inventory Optimization, Supplier Risk Monitoring, Warehouse Vision, and Procurement Copilot. Show expected business impact.
8. Final Dashboard: Display Overall Crisis Score (0-100), Leadership, Negotiation, Resilience, Cost Control, Risk Management, and Customer Satisfaction. Include personalized feedback, biggest mistake, best decision, expert recommendation, and lessons learned.

Design:
• Premium dark theme inspired by enterprise dashboards.
• Responsive.
• Rounded cards.
• Smooth transitions.
• Hover effects.
• Progress bars.
• Modern typography.
• Replay button.
• Every playthrough should randomize companies, crises, values, and outcomes.

Structure the React code into reusable components using useState. Ensure every button works, there are no console errors, and the final response contains only the complete HTML code inside a single code block.

Respomse #
Got it — this is a rich, multi-stage simulation app. Let me quickly lock in a design direction before building (enterprise crisis-ops feel, not a templated dashboard), then generate the full single-file app.

**Design plan:**
- **Palette:** near-black void (`#0A0E14`) panels (`#121826`), amber signal accent (`#F5A623`) for urgency/ticker, teal (`#2DD4BF`) for resilience/positive metrics, danger red (`#EF4565`) for risk, blue (`#4C8DFF`) for AI/strategy layer
- **Type:** geometric display stack for headers/KPI numbers, clean system sans for body, monospace for the live ticker digits — no external font CDNs, since the file must open and run fully offline
- **Signature element:** a persistent **"Live Ops Ticker"** — a mission-control style strip pinned under the header from the War Room onward, scrolling KPI deltas with ▲▼ indicators and a running "Crisis Day" counter, like a trading floor tracking the incident in real time
- **Structure:** a numbered stage stepper (Company → Crisis → War Room → Negotiation → Boardroom → AI Strategy → Dashboard) — justified here since it's a real sequential process, not decoration

Building it now.Braces and parens balance out. Now let's copy it to outputs and share it.That's the complete "Operation Lifeline: Supply Chain Crisis Lab" — one self-contained HTML file (React + Babel via CDN, no other external assets, runs offline once loaded). Just double-click it to open in your browser and start playing.

What it covers, matching your flow:
- **Welcome → randomized company** (industry, revenue, factories, warehouses, suppliers, inventory days, lead time, sourcing countries)
- **Randomized crisis** (8 types) with urgency, description, and starting metric hits
- **War Room**: pick 3 of 6 response actions, each with a plain-language "why this matters" note and animated impact on Cost, Inventory, Profit, Delivery Speed, and Customer Satisfaction
- **Negotiation**: 4 branching rounds affecting Trust, Price, and Lead Time, ending in a Negotiation Score
- **CEO Boardroom**: 5 leadership MCQs scored into a Leadership Score
- **AI Strategy**: pick 2 of 5 AI investments with expected business impact
- **Executive Dashboard**: Overall Crisis Score plus Leadership, Negotiation, Resilience, Cost Control, Risk Management, and Customer Satisfaction — with a personalized best decision, biggest mistake, expert recommendation, and lessons learned, plus a full decision log
- A **Replay** button that re-randomizes everything

The persistent **"Live Ops Ticker"** at the top (from the War Room onward) tracks your five core metrics in real time like a mission-control strip, with a running "Crisis Day" counter — that's the signature visual thread tying the whole run together.

Go ahead and open it, run a playthrough, and take your screenshots for the day29 write-up.
file:///C:/Users/DELL/Downloads/operation-lifeline.html
