```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maruti Swift Cost Analytics Dashboard</title>
    <style>
        :root {
            --bg-color: #0a0f1e;
            --card-bg: rgba(16, 22, 46, 0.7);
            --border-color: rgba(255, 255, 255, 0.1);
            --text-main: #f0f4f8;
            --text-muted: #8fa0dd;
            
            --color-e85: #ffb300;
            --color-petrol: #00b0ff;
            --color-diesel: #90a4ae;
            --color-cng: #00e676;
            --color-ev: #d500f9;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            min-height: 100vh;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            overflow-x: hidden;
        }

        header {
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border-color);
            padding: 18px 24px;
            border-radius: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 15px;
        }

        header h1 {
            font-size: 1.4rem;
            font-weight: 600;
            letter-spacing: 0.5px;
            color: #fff;
        }

        .meta-tags {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .tag {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.85rem;
            color: var(--text-muted);
        }

        .tag.active-fuel {
            border-color: var(--color-petrol);
            color: var(--color-petrol);
            box-shadow: 0 0 10px rgba(0, 176, 255, 0.2);
        }

        .kpi-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 15px;
        }

        .kpi-card {
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            position: relative;
            overflow: hidden;
        }

        .kpi-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: var(--border-color);
        }

        .kpi-card.accent-active::before { background: var(--color-petrol); }
        .kpi-card.accent-e85::before { background: var(--color-e85); }

        .kpi-title {
            font-size: 0.8rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .kpi-value {
            font-size: 1.6rem;
            font-weight: 700;
            color: #fff;
        }

        .kpi-sub {
            font-size: 0.75rem;
            color: var(--text-muted);
        }

        .charts-row-1 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }

        @media (max-width: 900px) {
            .charts-row-1 { grid-template-columns: 1fr; }
        }

        .chart-card {
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .chart-title {
            font-size: 1rem;
            font-weight: 600;
            color: #fff;
        }

        .charts-row-2 {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 20px;
        }

        @media (max-width: 900px) {
            .charts-row-2 { grid-template-columns: 1fr; }
        }

        .gauge-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100%;
            gap: 15px;
            padding: 10px 0;
        }

        .gauge-svg {
            width: 180px;
            height: 100px;
        }

        .gauge-bg {
            fill: none;
            stroke: rgba(255, 255, 255, 0.05);
            stroke-width: 12;
            stroke-linecap: round;
        }

        .gauge-fill {
            fill: none;
            stroke: var(--color-e85);
            stroke-width: 12;
            stroke-linecap: round;
            stroke-dasharray: 220;
            stroke-dashoffset: 220;
            animation: fillGauge 1.5s ease-out forwards;
        }

        @keyframes fillGauge {
            to { stroke-dashoffset: var(--gauge-offset); }
        }

        .gauge-text {
            font-size: 24px;
            font-weight: 700;
            fill: #fff;
            text-anchor: middle;
        }

        .verdict-box {
            text-align: center;
            font-size: 0.85rem;
            color: var(--text-muted);
            padding: 0 10px;
            line-height: 1.4;
        }

        .fuel-cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 15px;
        }

        .fuel-card {
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 12px;
            transition: all 0.3s ease;
        }

        .fuel-card.active-glow {
            border-color: var(--color-petrol);
            box-shadow: 0 0 20px rgba(0, 176, 255, 0.15);
            background: rgba(16, 26, 56, 0.85);
        }

        .fuel-card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            padding-bottom: 8px;
        }

        .fuel-name {
            font-weight: 600;
            font-size: 1.1rem;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .fuel-dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
        }

        .pro-con-list {
            display: flex;
            flex-direction: column;
            gap: 6px;
            font-size: 0.8rem;
        }

        .pro-con-item {
            display: flex;
            gap: 8px;
            align-items: flex-start;
            line-height: 1.3;
        }

        .best-for {
            margin-top: auto;
            background: rgba(255, 255, 255, 0.03);
            padding: 8px;
            border-radius: 6px;
            font-size: 0.75rem;
            color: var(--text-muted);
            border-left: 3px solid rgba(255, 255, 255, 0.2);
        }

        .fuel-card.active-glow .best-for {
            border-left-color: var(--color-petrol);
            background: rgba(0, 176, 255, 0.05);
        }

        .tooltip {
            position: absolute;
            background: rgba(5, 8, 22, 0.95);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 6px 10px;
            border-radius: 4px;
            font-size: 0.75rem;
            color: #fff;
            pointer-events: none;
            display: none;
            z-index: 100;
            box-shadow: 0 4px 10px rgba(0,0,0,0.5);
        }

        .bar-group:hover .bar-rect { fill-opacity: 1; }
        .bar-rect { transition: fill-opacity 0.2s; fill-opacity: 0.85; }
        .slice:hover { fill-opacity: 1; cursor: pointer; }
        .slice { transition: fill-opacity 0.2s; fill-opacity: 0.85; }
        .line-dot:hover { r: 6; cursor: pointer; }
        .line-dot { transition: r 0.2s; }
    </style>
</head>
<body>

    <header>
        <h1>Maruti Suzuki Swift Analytics</h1>
        <div class="meta-tags">
            <span class="tag active-fuel">Petrol</span>
            <span class="tag">Mixed City/Highway</span>
            <span class="tag">Age: 3 Years</span>
            <span class="tag">1,200 km/month</span>
        </div>
    </header>

    <div class="kpi-container">
        <div class="kpi-card accent-active">
            <div class="kpi-title">Your Cost / KM</div>
            <div class="kpi-value">₹6.15</div>
            <div class="kpi-sub">Fuel (₹5.55) + Maint (₹0.60)</div>
        </div>
        <div class="kpi-card accent-e85">
            <div class="kpi-title">E85 Cost / KM</div>
            <div class="kpi-value">₹7.10</div>
            <div class="kpi-sub">With 28% efficiency drop</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">E85 Running Penalty</div>
            <div class="kpi-value">+15.4%</div>
            <div class="kpi-sub">Despite cheaper pump price</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">E85 Break-Even Price</div>
            <div class="kpi-value">₹72.40</div>
            <div class="kpi-sub">Target price for actual savings</div>
        </div>
        <div class="kpi-card accent-active">
            <div class="kpi-title">Your Monthly Spend</div>
            <div class="kpi-value">₹7,380</div>
            <div class="kpi-sub">For 1,200 km tracked distance</div>
        </div>
    </div>

    <div class="charts-row-1">
        <div class="chart-card">
            <div class="chart-title">Average Operational Cost per KM (INR)</div>
            <div style="position: relative; width: 100%; height: 220px;">
                <svg width="100%" height="100%" viewBox="0 0 500 220" preserveAspectRatio="xMidYMid meet">
                    <!-- Grid Lines -->
                    <line x1="60" y1="30" x2="480" y2="30" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
                    <line x1="60" y1="80" x2="480" y2="80" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
                    <line x1="60" y1="130" x2="480" y2="130" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
                    <line x1="60" y1="180" x2="480" y2="180" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
                    
                    <!-- Y Axis Labels -->
                    <text x="50" y="34" fill="#8fa0dd" font-size="10" text-anchor="end">₹8.0</text>
                    <text x="50" y="84" fill="#8fa0dd" font-size="10" text-anchor="end">₹5.0</text>
                    <text x="50" y="134" fill="#8fa0dd" font-size="10" text-anchor="end">₹2.0</text>
                    <text x="50" y="184" fill="#8fa0dd" font-size="10" text-anchor="end">₹0.0</text>

                    <!-- Bars -->
                    <!-- Petrol -->
                    <g class="bar-group" data-tip="Petrol: Total ₹6.15/km (Fuel: ₹5.55, Maint: ₹0.60)">
                        <rect class="bar-rect" x="85" y="65" width="40" height="115" fill="#00b0ff" rx="4"/>
                        <text x="105" y="195" fill="#8fa0dd" font-size="10" text-anchor="middle">Petrol</text>
                    </g>
                    <!-- E85 -->
                    <g class="bar-group" data-tip="E85: Total ₹7.10/km (Fuel: ₹6.45, Maint: ₹0.65)">
                        <rect class="bar-rect" x="165" y="45" width="40" height="135" fill="#ffb300" rx="4"/>
                        <text x="185" y="195" fill="#8fa0dd" font-size="10" text-anchor="middle">E85</text>
                    </g>
                    <!-- Diesel -->
                    <g class="bar-group" data-tip="Diesel: Total ₹5.40/km (Fuel: ₹4.60, Maint: ₹0.80)">
                        <rect class="bar-rect" x="245" y="78" width="40" height="102" fill="#90a4ae" rx="4"/>
                        <text x="265" y="195" fill="#8fa0dd" font-size="10" text-anchor="middle">Diesel</text>
                    </g>
                    <!-- CNG -->
                    <g class="bar-group" data-tip="CNG: Total ₹3.80/km (Fuel: ₹3.10, Maint: ₹0.70)">
                        <rect class="bar-rect" x="325" y="108" width="40" height="72" fill="#00e676" rx="4"/>
                        <text x="345" y="195" fill="#8fa0dd" font-size="10" text-anchor="middle">CNG</text>
                    </g>
                    <!-- EV -->
                    <g class="bar-group" data-tip="EV: Total ₹1.20/km (Charge: ₹0.90, Maint: ₹0.30)">
                        <rect class="bar-rect" x="405" y="158" width="40" height="22" fill="#d500f9" rx="4"/>
                        <text x="425" y="195" fill="#8fa0dd" font-size="10" text-anchor="middle">EV</text>
                    </g>
                </svg>
            </div>
        </div>

        <div class="chart-card">
            <div class="chart-title">Carbon Footprint Breakdown (Avg CO₂ g/km)</div>
            <div style="position: relative; width: 100%; height: 220px; display: flex; justify-content: center;">
                <svg width="220" height="220" viewBox="0 0 220 220">
                    <!-- Donut Slices for Car Data -->
                    <circle class="slice" cx="110" cy="110" r="75" fill="none" stroke="#00b0ff" stroke-width="22" stroke-dasharray="180 291" stroke-dashoffset="0" data-tip="Petrol: 145g CO₂/km"/>
                    <circle class="slice" cx="110" cy="110" r="75" fill="none" stroke="#ffb300" stroke-width="22" stroke-dasharray="65 406" stroke-dashoffset="-180" data-tip="E85: 52g CO₂/km"/>
                    <circle class="slice" cx="110" cy="110" r="75" fill="none" stroke="#90a4ae" stroke-width="22" stroke-dasharray="170 301" stroke-dashoffset="-245" data-tip="Diesel: 138g CO₂/km"/>
                    <circle class="slice" cx="110" cy="110" r="75" fill="none" stroke="#00e676" stroke-width="22" stroke-dasharray="56 415" stroke-dashoffset="-415" data-tip="CNG: 45g CO₂/km"/>
                    <circle cx="110" cy="110" r="60" fill="none" stroke="rgba(16, 22, 46, 0.9)" stroke-width="2"/>
                    <text x="110" y="114" fill="#fff" font-size="11" font-weight="600" text-anchor="middle">Total Carbon</text>
                    <text x="110" y="128" fill="#8fa0dd" font-size="10" text-anchor="middle">380g/km</text>
                </svg>
            </div>
        </div>
    </div>

    <div class="charts-row-2">
        <div class="chart-card">
            <div class="chart-title">Cost Curve Progression vs Vehicle Age (Years)</div>
            <div style="position: relative; width: 100%; height: 250px;">
                <svg width="100%" height="100%" viewBox="0 0 650 250" preserveAspectRatio="xMidYMid meet">
                    <!-- Axis Labels -->
                    <text x="50" y="235" fill="#8fa0dd" font-size="10" text-anchor="middle">0y (New)</text>
                    <text x="200" y="235" fill="#8fa0dd" font-size="10" text-anchor="middle">3y (Mid)</text>
                    <text x="350" y="235" fill="#8fa0dd" font-size="10" text-anchor="middle">6y (Aged)</text>
                    <text x="500" y="235" fill="#8fa0dd" font-size="10" text-anchor="middle">10y (Old)</text>
                    
                    <text x="40" y="34" fill="#8fa0dd" font-size="10" text-anchor="end">₹10.0</text>
                    <text x="40" y="109" fill="#8fa0dd" font-size="10" text-anchor="end">₹5.0</text>
                    <text x="40" y="184" fill="#8fa0dd" font-size="10" text-anchor="end">₹1.0</text>
                    
                    <!-- Vertical Line at 3y -->
                    <line x1="200" y1="20" x2="200" y2="210" stroke="#00b0ff" stroke-width="1.5" stroke-dasharray="4 4"/>
                    <rect x="155" y="2" width="90" height="16" fill="rgba(0, 176, 255, 0.2)" rx="3"/>
                    <text x="200" y="13" fill="#00b0ff" font-size="9" font-weight="600" text-anchor="middle">YOUR SWIFT AGE (3y)</text>

                    <!-- Trends Paths for Cars -->
                    <path d="M 50,180 L 200,175 L 350,165 L 500,150" fill="none" stroke="#d500f9" stroke-width="2"/>
                    <path d="M 50,140 L 200,130 L 350,115 L 500,95" fill="none" stroke="#00e676" stroke-width="2"/>
                    <g>
                        <path d="M 50,110 L 200,98 L 350,80 L 500,55" fill="none" stroke="#00b0ff" stroke-width="2.5"/>
                        <circle class="line-dot" cx="200" cy="98" r="5" fill="#00b0ff" stroke="#fff" stroke-width="1" data-tip="Your Current Status (Petrol Swift 3y): Total ₹6.15/km"/>
                    </g>
                    <path d="M 50,90 L 200,78 L 350,60 L 500,30" fill="none" stroke="#ffb300" stroke-width="2"/>
                </svg>
            </div>
        </div>

        <div class="chart-card">
            <div class="chart-title" style="text-align: center;">E85 Index Suitability Score</div>
            <div class="gauge-container">
                <svg class="gauge-svg" viewBox="0 0 200 110">
                    <path class="gauge-bg" d="M 20 100 A 80 80 0 0 1 180 100"/>
                    <path class="gauge-fill" id="e85Gauge" d="M 20 100 A 80 80 0 0 1 180 100" style="--gauge-offset: 88;"/>
                    <text x="100" y="90" class="gauge-text">6.0 / 10</text>
                </svg>
                <div class="verdict-box">
                    <strong>Verdict:</strong> Significant tailpipe CO₂ cuts achieved, but the thermal efficiency drops running costs by 15.4% into the negative zone.
                </div>
            </div>
        </div>
    </div>

    <div class="fuel-cards-grid">
        <div class="fuel-card active-glow">
            <div class="fuel-card-header">
                <div class="fuel-name"><span class="fuel-dot" style="background: var(--color-petrol);"></span>Petrol (Swift Baseline)</div>
                <span class="tag" style="border-color: var(--color-petrol); color: var(--color-petrol);">Active</span>
            </div>
            <div class="pro-con-list">
                <div class="pro-con-item">✅ Best engine responsiveness & refined cabin noise levels.</div>
                <div class="pro-con-item">✅ Highest resale value and ubiquitous fuel station support.</div>
                <div class="pro-con-item">❌ Expensive running cost compared to CNG and EV alternatives.</div>
            </div>
            <div class="best-for">🚗 <strong>Best For:</strong> Balanced city and long-distance family travel.</div>
        </div>

        <div class="fuel-card">
            <div class="fuel-card-header">
                <div class="fuel-name"><span class="fuel-dot" style="background: var(--color-e85);"></span>E85 Flex-Fuel</div>
            </div>
            <div class="pro-con-list">
                <div class="pro-con-item">✅ Excellent ~64% net lifecycle greenhouse gas reduction.</div>
                <div class="pro-con-item">❌ 28% drop in overall vehicle mileage.</div>
                <div class="pro-con-item">❌ Requires anti-corrosive engine modifications to prevent fuel-line damage.</div>
            </div>
            <div class="best-for">🚗 <strong>Best For:</strong> Eco-conscious fleets running inside green zones.</div>
        </div>
    </div>

    <div class="tooltip" id="chartTooltip"></div>

    <script>
        const tooltip = document.getElementById('chartTooltip');
        const elements = document.querySelectorAll('[data-tip]');

        elements.forEach(el => {
            el.addEventListener('mouseover', (e) => {
                tooltip.style.display = 'block';
                tooltip.innerHTML = el.getAttribute('data-tip');
            });
            el.addEventListener('mousemove', (e) => {
                tooltip.style.left = (e.pageX + 12) + 'px';
                tooltip.style.top = (e.pageY - 35) + 'px';
            });
            el.addEventListener('mouseout', () => {
                tooltip.style.display = 'none';
            });
        });
    </script>
</body>
</html>

```
<img width="1323" height="1177" alt="image" src="https://github.com/user-attachments/assets/3958e77c-e6d9-4a8d-bd96-59848c2e3678" />
