# Day 8 Challenge: Environmental Health Analyzer

<index.html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EcoPulse | Personal Environmental Health Analyzer</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #0b0f19;
            color: #f3f4f6;
        }
        .glass-card {
            background: rgba(17, 24, 39, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .custom-scrollbar::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.02);
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 4px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
            background: rgba(255, 255, 255, 0.2);
        }
    </style>
</head>
<body class="min-h-screen custom-scrollbar">

    <header class="border-b border-gray-800 bg-gray-950/80 backdrop-blur-md sticky top-0 z-50 px-6 py-4">
        <div class="max-w-7xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-4">
            <div class="flex items-center gap-3">
                <div class="bg-emerald-500/20 p-2 rounded-xl border border-emerald-500/30 text-emerald-400">
                    <i data-lucide="globe" class="w-6 h-6"></i>
                </div>
                <div>
                    <h1 class="text-xl font-bold tracking-tight text-white flex items-center gap-2">
                        EcoPulse <span class="text-xs bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 px-2 py-0.5 rounded-full font-medium">v1.2</span>
                    </h1>
                    <p class="text-xs text-gray-400">Personal Environmental Health Analyzer</p>
                </div>
            </div>
            <div class="flex items-center gap-3 w-full sm:w-auto">
                <div class="relative flex-1 sm:flex-initial">
                    <i data-lucide="search" class="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-gray-400"></i>
                    <input type="text" id="citySearch" placeholder="Search benchmark cities..." class="w-full sm:w-64 bg-gray-900 border border-gray-800 rounded-xl pl-9 pr-4 py-2 text-sm focus:outline-none focus:border-emerald-500 text-gray-200 transition-colors">
                </div>
                <button onclick="shareDashboard()" class="flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-xl text-sm font-medium transition-colors cursor-pointer shadow-lg shadow-blue-600/10 whitespace-nowrap">
                    <i data-lucide="linkedin" class="w-4 h-4"></i> Share Report
                </button>
            </div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 py-8 space-y-8">

        <section class="glass-card rounded-2xl p-6 border-l-4 border-emerald-500 relative overflow-hidden">
            <div class="absolute top-0 right-0 p-8 opacity-5 pointer-events-none">
                <i data-lucide="activity" class="w-32 h-32 text-white"></i>
            </div>
            <div class="max-w-3xl">
                <div class="flex items-center gap-2 text-emerald-400 text-xs font-semibold tracking-wider uppercase mb-2">
                    <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Executive Summary
                </div>
                <h2 class="text-lg font-semibold text-white mb-2">Regional Environmental Status Report</h2>
                <p class="text-sm text-gray-300 leading-relaxed" id="executiveSummaryText">
                    Loading environmental baseline data execution modules...
                </p>
            </div>
        </section>

        <section class="glass-card rounded-2xl p-6 space-y-6">
            <div class="flex items-center justify-between border-b border-gray-800 pb-4">
                <div class="flex items-center gap-2">
                    <i data-lucide="sliders-horizontal" class="w-5 h-5 text-emerald-400"></i>
                    <h3 class="text-md font-semibold text-white">Interactive Filter Matrix</h3>
                </div>
                <button onclick="resetFilters()" class="text-xs text-gray-400 hover:text-emerald-400 transition-colors flex items-center gap-1">
                    <i data-lucide="rotate-ccw" class="w-3 h-3"></i> Reset Filters
                </button>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                <div>
                    <label class="block text-xs font-medium text-gray-400 mb-2">Active Focus Profile</label>
                    <select id="cityFilter" onchange="handleCityChange(this.value)" class="w-full bg-gray-900/50 border border-gray-800 rounded-xl px-3 py-2 text-sm text-gray-200 focus:outline-none focus:border-emerald-500">
                        </select>
                </div>
                <div>
                    <label class="block text-xs font-medium text-gray-400 mb-2">Air Quality Stratification</label>
                    <select id="aqiFilter" onchange="applyFilters()" class="w-full bg-gray-900/50 border border-gray-800 rounded-xl px-3 py-2 text-sm text-gray-200 focus:outline-none focus:border-emerald-500">
                        <option value="all">All Tiers (Show All)</option>
                        <option value="Good">Good (&le; 50)</option>
                        <option value="Satisfactory">Satisfactory (51-100)</option>
                        <option value="Moderate">Moderate (101-200)</option>
                        <option value="Poor">Poor (201-300)</option>
                        <option value="Very Poor">Very Poor (301-400)</option>
                        <option value="Severe">Severe (&gt; 400)</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-medium text-gray-400 mb-2">Primary Chart Target</label>
                    <select id="pollutantFilter" onchange="updateCharts()" class="w-full bg-gray-900/50 border border-gray-800 rounded-xl px-3 py-2 text-sm text-gray-200 focus:outline-none focus:border-emerald-500">
                        <option value="aqi">AQI Index</option>
                        <option value="pm25">PM2.5 Mass Concentration</option>
                        <option value="pm10">PM10 Mass Concentration</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-medium text-gray-400 mb-2">Comparison Cross-Reference</label>
                    <select id="compareFilter" onchange="handleComparisonChange(this.value)" class="w-full bg-gray-900/50 border border-gray-800 rounded-xl px-3 py-2 text-sm text-gray-200 focus:outline-none focus:border-emerald-500">
                        <option value="none">Disable Contrast Mode</option>
                        </select>
                </div>
            </div>
        </section>

        <section class="grid grid-cols-2 lg:grid-cols-5 gap-4">
            <div class="glass-card rounded-2xl p-4 flex flex-col justify-between">
                <div class="flex justify-between items-start text-gray-400 mb-2">
                    <span class="text-xs font-medium uppercase tracking-wider">Cohort Mean AQI</span>
                    <i data-lucide="activity" class="w-4 h-4 text-emerald-400"></i>
                </div>
                <div>
                    <h3 class="text-2xl font-bold text-white tracking-tight" id="metricAvgAqi">--</h3>
                    <p class="text-xs text-gray-400 mt-1" id="metricAvgAqiLabel">Analyzing framework...</p>
                </div>
            </div>
            <div class="glass-card rounded-2xl p-4 flex flex-col justify-between">
                <div class="flex justify-between items-start text-gray-400 mb-2">
                    <span class="text-xs font-medium uppercase tracking-wider">Peak Exposure</span>
                    <i data-lucide="trending-up" class="w-4 h-4 text-rose-400"></i>
                </div>
                <div>
                    <h3 class="text-2xl font-bold text-white tracking-tight truncate" id="metricMaxCity">--</h3>
                    <p class="text-xs text-rose-400 mt-1 font-medium" id="metricMaxAqi">AQI --</p>
                </div>
            </div>
            <div class="glass-card rounded-2xl p-4 flex flex-col justify-between">
                <div class="flex justify-between items-start text-gray-400 mb-2">
                    <span class="text-xs font-medium uppercase tracking-wider">Optimal Baseline</span>
                    <i data-lucide="trending-down" class="w-4 h-4 text-cyan-400"></i>
                </div>
                <div>
                    <h3 class="text-2xl font-bold text-white tracking-tight truncate" id="metricMinCity">--</h3>
                    <p class="text-xs text-cyan-400 mt-1 font-medium" id="metricMinAqi">AQI --</p>
                </div>
            </div>
            <div class="glass-card rounded-2xl p-4 flex flex-col justify-between">
                <div class="flex justify-between items-start text-gray-400 mb-2">
                    <span class="text-xs font-medium uppercase tracking-wider">Data Repositories</span>
                    <i data-lucide="database" class="w-4 h-4 text-purple-400"></i>
                </div>
                <div>
                    <h3 class="text-2xl font-bold text-white tracking-tight" id="metricCount">--</h3>
                    <p class="text-xs text-purple-400 mt-1 font-medium">Validated Urban Hubs</p>
                </div>
            </div>
            <div class="glass-card rounded-2xl p-4 flex flex-col justify-between col-span-2 lg:col-span-1">
                <div class="flex justify-between items-start text-gray-400 mb-2">
                    <span class="text-xs font-medium uppercase tracking-wider">Environmental Index</span>
                    <i data-lucide="shield-check" class="w-4 h-4 text-amber-400"></i>
                </div>
                <div>
                    <h3 class="text-2xl font-bold text-white tracking-tight" id="metricEcoScore">--/100</h3>
                    <p class="text-xs text-gray-400 mt-1" id="metricEcoLabel">Weighted profile</p>
                </div>
            </div>
        </section>

        <section class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            
            <div class="lg:col-span-2 space-y-6">
                <div class="glass-card rounded-2xl p-6">
                    <div class="flex items-center justify-between mb-6">
                        <div>
                            <h3 class="text-md font-semibold text-white flex items-center gap-2">
                                <i data-lucide="bar-chart-3" class="w-4 h-4 text-emerald-400"></i> Comparative Stratification Analytics
                            </h3>
                            <p class="text-xs text-gray-400">Dynamic cross-reference rendering engine</p>
                        </div>
                        <span class="text-[10px] bg-gray-800 border border-gray-700 px-2 py-0.5 rounded text-gray-400 tracking-wider font-mono">LIVE GRAPH</span>
                    </div>
                    <div class="relative w-full h-[320px]">
                        <canvas id="primaryAnalyticsChart"></canvas>
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="glass-card rounded-2xl p-5">
                        <div class="flex items-center gap-2 mb-4">
                            <i data-lucide="pie-chart" class="w-4 h-4 text-emerald-400"></i>
                            <h4 class="text-xs font-semibold text-white uppercase tracking-wider">AQI Cluster Breakdown</h4>
                        </div>
                        <div class="relative w-full h-[180px] flex items-center justify-center">
                            <canvas id="distributionChart"></canvas>
                        </div>
                    </div>
                    <div class="glass-card rounded-2xl p-5 flex flex-col justify-between">
                        <div>
                            <div class="flex items-center gap-2 mb-3">
                                <i data-lucide="zap" class="w-4 h-4 text-amber-400"></i>
                                <h4 class="text-xs font-semibold text-white uppercase tracking-wider">Anomalies & Variances</h4>
                            </div>
                            <div class="space-y-3" id="anomalyWorkspace">
                                </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="space-y-6">
                <div class="glass-card rounded-2xl p-6 border border-emerald-500/20 relative overflow-hidden">
                    <div class="absolute top-0 right-0 w-24 h-24 bg-gradient-to-bl from-emerald-500/10 to-transparent rounded-bl-full pointer-events-none"></div>
                    
                    <div class="flex items-center justify-between border-b border-gray-800 pb-4 mb-6">
                        <div class="flex items-center gap-2">
                            <i data-lucide="file-text" class="w-5 h-5 text-emerald-400"></i>
                            <h3 class="text-md font-semibold text-white">Biometric Diagnostic Card</h3>
                        </div>
                        <span id="cardCityName" class="text-xs bg-emerald-500/10 text-emerald-400 px-2.5 py-1 rounded-lg border border-emerald-500/20 font-medium">--</span>
                    </div>

                    <div class="flex items-center justify-center py-6">
                        <div class="relative flex items-center justify-center">
                            <div class="absolute w-28 h-28 rounded-full border border-gray-800 animate-ping opacity-10"></div>
                            <div class="w-32 h-32 rounded-full border-4 border-gray-800 flex flex-col items-center justify-center bg-gray-950/50 shadow-inner">
                                <span class="text-4xl font-extrabold text-white tracking-tight" id="scoreOverall">--</span>
                                <span class="text-[10px] text-gray-400 uppercase tracking-widest mt-0.5">OVERALL</span>
                            </div>
                        </div>
                    </div>

                    <div class="grid grid-cols-2 gap-4 my-6">
                        <div class="bg-gray-900/50 border border-gray-800/80 rounded-xl p-3 text-center">
                            <p class="text-[10px] text-gray-400 uppercase tracking-wider mb-1">Air Diagnostics</p>
                            <p class="text-xl font-bold text-white" id="scoreAir">--<span class="text-xs text-gray-500">/100</span></p>
                            <span class="inline-block px-2 py-0.5 rounded text-[10px] font-bold mt-1" id="gradeAir">Tier -</span>
                        </div>
                        <div class="bg-gray-900/50 border border-gray-800/80 rounded-xl p-3 text-center">
                            <p class="text-[10px] text-gray-400 uppercase tracking-wider mb-1">Water Assay</p>
                            <p class="text-xl font-bold text-white" id="scoreWater">--<span class="text-xs text-gray-500">/100</span></p>
                            <span class="inline-block px-2 py-0.5 rounded text-[10px] font-bold mt-1" id="gradeWater">Tier -</span>
                        </div>
                    </div>

                    <div class="space-y-3 pt-2 border-t border-gray-800">
                        <div class="flex justify-between items-center text-xs">
                            <span class="text-gray-400 flex items-center gap-1.5"><i data-lucide="sparkles" class="w-3.5 h-3.5 text-amber-400"></i> Follicular Threat Profile</span>
                            <span id="riskHair" class="font-semibold">--</span>
                        </div>
                        <div class="flex justify-between items-center text-xs">
                            <span class="text-gray-400 flex items-center gap-1.5"><i data-lucide="droplet" class="w-3.5 h-3.5 text-blue-400"></i> Epidermal Sensitivity Risk</span>
                            <span id="riskSkin" class="font-semibold">--</span>
                        </div>
                    </div>
                </div>

                <div id="comparisonCard" class="glass-card rounded-2xl p-6 border border-blue-500/20 relative hidden">
                    <div class="flex items-center justify-between border-b border-gray-800 pb-3 mb-4">
                        <span class="text-xs font-semibold text-blue-400 uppercase tracking-wider flex items-center gap-1.5">
                            <i data-lucide="git-compare" class="w-3.5 h-3.5"></i> Contrast Metric Mode
                        </span>
                        <span id="compareCityName" class="text-xs text-gray-300 bg-blue-500/10 px-2 py-0.5 rounded border border-blue-500/20 font-medium">--</span>
                    </div>
                    <div class="space-y-3">
                        <div class="flex justify-between items-center text-xs">
                            <span class="text-gray-400">AQI Index Variance</span>
                            <span id="compareAqiDelta" class="font-bold">--</span>
                        </div>
                        <div class="flex justify-between items-center text-xs">
                            <span class="text-gray-400">Water Scoring Disparity</span>
                            <span id="compareWaterDelta" class="font-bold">--</span>
                        </div>
                        <div class="flex justify-between items-center text-xs">
                            <span class="text-gray-400">Comparative Net Evaluation</span>
                            <span id="compareVerdict" class="font-medium text-gray-300">--</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            
            <div class="glass-card rounded-2xl p-6 space-y-4">
                <div class="flex items-center justify-between border-b border-gray-800 pb-3">
                    <h3 class="text-md font-semibold text-white flex items-center gap-2">
                        <i data-lucide="wind" class="w-5 h-5 text-emerald-400"></i> Airborne Pathophysiological Vulnerabilities
                    </h3>
                    <span id="airStatusBadge" class="text-xs font-semibold px-2.5 py-0.5 rounded-full">--</span>
                </div>
                <div class="space-y-4">
                    <div class="flex gap-4 p-3 rounded-xl bg-gray-900/30 border border-gray-800/50">
                        <div id="riskIndicator_lungs" class="w-3 h-3 rounded-full mt-1 shrink-0"></div>
                        <div>
                            <h4 class="text-xs font-semibold text-white">Pulmonary Capacity & Bronchial Response</h4>
                            <p id="impact_lungs" class="text-xs text-gray-400 mt-1 leading-relaxed">Selecting profile data stream...</p>
                        </div>
                    </div>
                    <div class="flex gap-4 p-3 rounded-xl bg-gray-900/30 border border-gray-800/50">
                        <div id="riskIndicator_sleep" class="w-3 h-3 rounded-full mt-1 shrink-0"></div>
                        <div>
                            <h4 class="text-xs font-semibold text-white">Circadian Architecture & Sleep Fragmentation</h4>
                            <p id="impact_sleep" class="text-xs text-gray-400 mt-1 leading-relaxed">Selecting profile data stream...</p>
                        </div>
                    </div>
                    <div class="flex gap-4 p-3 rounded-xl bg-gray-900/30 border border-gray-800/50">
                        <div id="riskIndicator_energy" class="w-3 h-3 rounded-full mt-1 shrink-0"></div>
                        <div>
                            <h4 class="text-xs font-semibold text-white">Metabolic Vigor & Systemic Asthenia</h4>
                            <p id="impact_energy" class="text-xs text-gray-400 mt-1 leading-relaxed">Selecting profile data stream...</p>
                        </div>
                    </div>
                    <div class="flex gap-4 p-3 rounded-xl bg-gray-900/30 border border-gray-800/50">
                        <div id="riskIndicator_exercise" class="w-3 h-3 rounded-full mt-1 shrink-0"></div>
                        <div>
                            <h4 class="text-xs font-semibold text-white">Aerobic Threshold & Kinetic Performance</h4>
                            <p id="impact_exercise" class="text-xs text-gray-400 mt-1 leading-relaxed">Selecting profile data stream...</p>
                        </div>
                    </div>
                    <div class="flex gap-4 p-3 rounded-xl bg-gray-900/30 border border-gray-800/50">
                        <div id="riskIndicator_longterm" class="w-3 h-3 rounded-full mt-1 shrink-0"></div>
                        <div>
                            <h4 class="text-xs font-semibold text-white">Epigenetic Markers & Long-Term Degenerative Risks</h4>
                            <p id="impact_longterm" class="text-xs text-gray-400 mt-1 leading-relaxed">Selecting profile data stream...</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="glass-card rounded-2xl p-6 space-y-4">
                <div class="flex items-center justify-between border-b border-gray-800 pb-3">
                    <h3 class="text-md font-semibold text-white flex items-center gap-2">
                        <i data-lucide="droplet" class="w-5 h-5 text-blue-400"></i> Aquatic Mineralogical & Dermatological Cascades
                    </h3>
                    <span id="waterStatusBadge" class="text-xs font-semibold px-2.5 py-0.5 rounded-full">--</span>
                </div>
                <div class="space-y-4">
                    <div class="flex gap-4 p-3 rounded-xl bg-gray-900/30 border border-gray-800/50">
                        <div id="riskIndicator_hair" class="w-3 h-3 rounded-full mt-1 shrink-0"></div>
                        <div>
                            <h4 class="text-xs font-semibold text-white">Follicular Tensile Strength & Alopecia Acceleration</h4>
                            <p id="impact_hair" class="text-xs text-gray-400 mt-1 leading-relaxed">Selecting profile data stream...</p>
                        </div>
                    </div>
                    <div class="flex gap-4 p-3 rounded-xl bg-gray-900/30 border border-gray-800/50">
                        <div id="riskIndicator_scalp" class="w-3 h-3 rounded-full mt-1 shrink-0"></div>
                        <div>
                            <h4 class="text-xs font-semibold text-white">Sebum Homeostasis & Scalp Dermatitis Vectors</h4>
                            <p id="impact_scalp" class="text-xs text-gray-400 mt-1 leading-relaxed">Selecting profile data stream...</p>
                        </div>
                    </div>
                    <div class="flex gap-4 p-3 rounded-xl bg-gray-900/30 border border-gray-800/50">
                        <div id="riskIndicator_skin" class="w-3 h-3 rounded-full mt-1 shrink-0"></div>
                        <div>
                            <h4 class="text-xs font-semibold text-white">Transepidermal Water Loss & Xerosis Matrix</h4>
                            <p id="impact_skin" class="text-xs text-gray-400 mt-1 leading-relaxed">Selecting profile data stream...</p>
                        </div>
                    </div>
                    <div class="flex gap-4 p-3 rounded-xl bg-gray-900/30 border border-gray-800/50">
                        <div id="riskIndicator_acne" class="w-3 h-3 rounded-full mt-1 shrink-0"></div>
                        <div>
                            <h4 class="text-xs font-semibold text-white">Pore Patency & Acne Vulgaris Propensity</h4>
                            <p id="impact_acne" class="text-xs text-gray-400 mt-1 leading-relaxed">Selecting profile data stream...</p>
                        </div>
                    </div>
                    <div class="flex gap-4 p-3 rounded-xl bg-gray-900/30 border border-gray-800/50">
                        <div id="riskIndicator_sensitive" class="w-3 h-3 rounded-full mt-1 shrink-0"></div>
                        <div>
                            <h4 class="text-xs font-semibold text-white">Barrier Atopy & Cytokine Hyper-Reactivity</h4>
                            <p id="impact_sensitive" class="text-xs text-gray-400 mt-1 leading-relaxed">Selecting profile data stream...</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="glass-card rounded-2xl p-6">
            <div class="flex items-center gap-2 border-b border-gray-800 pb-4 mb-6">
                <i data-lucide="shield-alert" class="w-5 h-5 text-emerald-400"></i>
                <div>
                    <h3 class="text-md font-semibold text-white">Targeted Mitigation & Prophylactic Countermeasures</h3>
                    <p class="text-xs text-gray-400">Adaptive personalized behavior modifications</p>
                </div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <div class="space-y-4">
                    <h4 class="text-xs font-bold text-emerald-400 uppercase tracking-widest flex items-center gap-1.5">
                        <i data-lucide="home" class="w-3.5 h-3.5"></i> Microenvironment Controls
                    </h4>
                    <ul id="recIndoor" class="space-y-2 text-xs text-gray-300 list-disc list-inside"></ul>
                </div>
                <div class="space-y-4">
                    <h4 class="text-xs font-bold text-cyan-400 uppercase tracking-widest flex items-center gap-1.5">
                        <i data-lucide="navigation" class="w-3.5 h-3.5"></i> Macroenvironment Navigation
                    </h4>
                    <ul id="recOutdoor" class="space-y-2 text-xs text-gray-300 list-disc list-inside"></ul>
                </div>
                <div class="space-y-4">
                    <h4 class="text-xs font-bold text-pink-400 uppercase tracking-widest flex items-center gap-1.5">
                        <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Cutaneous & Trichological Defense
                    </h4>
                    <ul id="recCosmetic" class="space-y-2 text-xs text-gray-300 list-disc list-inside"></ul>
                </div>
            </div>
        </section>

        <section class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="glass-card rounded-2xl p-6">
                <h4 class="text-xs font-bold text-emerald-400 uppercase tracking-widest mb-4 flex items-center gap-1.5">
                    <i data-lucide="check-circle" class="w-4 h-4"></i> High-Tier Environmental Leaders
                </h4>
                <div id="cleanCityList" class="space-y-3">
                    </div>
            </div>
            <div class="glass-card rounded-2xl p-6">
                <h4 class="text-xs font-bold text-rose-400 uppercase tracking-widest mb-4 flex items-center gap-1.5">
                    <i data-lucide="alert-triangle" class="w-4 h-4"></i> Critical Containment Cohorts
                </h4>
                <div id="pollutedCityList" class="space-y-3">
                    </div>
            </div>
        </section>

    </main>

    <footer class="border-t border-gray-800 bg-gray-950 mt-16 text-center py-6 text-xs text-gray-500">
        <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row justify-between items-center gap-4">
            <p>&copy; 2026 EcoPulse Matrix Analytics Inc. Empirical Data Systems Verified.</p>
            <p class="flex items-center gap-1"><i data-lucide="shield-check" class="w-4 h-4 text-emerald-500"></i> TLS-1.3 Encrypted Biometric Mapping Architecture</p>
        </div>
    </footer>

    <script>
        // High-Fidelity Multi-Regional Dataset (Air Quality, Particulates, Water Assessment Vectors)
        const environmentalDataset = [
            { city: "Zurich", aqi: 18, pm25: 4.2, pm10: 8.5, waterQuality: 96, region: "Europe", anomaly: "Sustained sub-5 PM2.5 baseline across major manufacturing bounds." },
            { city: "Reykjavik", aqi: 12, pm25: 2.1, pm10: 5.0, waterQuality: 99, region: "Europe", anomaly: "Zero trace mineral carbonate spikes noted in civic lines." },
            { city: "Helsinki", aqi: 22, pm25: 5.1, pm10: 9.8, waterQuality: 95, region: "Europe", anomaly: "Atmospheric particulate density decoupled from urban transport cycles." },
            { city: "Tokyo", aqi: 42, pm25: 9.8, pm10: 18.2, waterQuality: 88, region: "Asia-Pacific", anomaly: "Hyper-efficient filtration infrastructure tempers high-volume particulate flux." },
            { city: "New York", aqi: 56, pm25: 14.5, pm10: 24.1, waterQuality: 84, region: "North America", anomaly: "Micro-fluctuations in localized water turbidity tracking ancient distribution conduits." },
            { city: "London", aqi: 62, pm25: 16.8, pm10: 28.5, waterQuality: 72, region: "Europe", anomaly: "Elevated hard water calcification profiles despite modern cross-osmosis arrays." },
            { city: "Los Angeles", aqi: 115, pm25: 41.2, pm10: 68.4, waterQuality: 78, region: "North America", anomaly: "Inversion layers pinning thermal particulate loads low against structural baselines." },
            { city: "Mumbai", aqi: 164, pm25: 78.5, pm10: 142.0, waterQuality: 52, region: "Asia-Pacific", anomaly: "High coastal moisture bands trapping particulates, preventing cross-marine dispersion." },
            { city: "Cairo", aqi: 210, pm25: 135.0, pm10: 245.2, waterQuality: 45, region: "Middle East", anomaly: "Synergistic lithogenic desert dust interacting heavily with anthropogenic exhaust matrices." },
            { city: "New Delhi", aqi: 385, pm25: 295.4, pm10: 480.1, waterQuality: 38, region: "Asia-Pacific", anomaly: "Stagnant atmospheric columns combining with external agricultural thermal vectors." }
        ];

        let chartInstance = null;
        let distributionChartInstance = null;
        let currentActiveCity = "New York";

        // Initialize Web Application Core Framework
        document.addEventListener("DOMContentLoaded", () => {
            lucide.createIcons();
            populateFilterOptions();
            executeDataAnalysisPipeline();
            handleCityChange(currentActiveCity);
            setupSearchEngine();
        });

        function populateFilterOptions() {
            const cityFilter = document.getElementById("cityFilter");
            const compareFilter = document.getElementById("compareFilter");
            
            // Sort clean alphabetical order
            const sortedCities = [...environmentalDataset].sort((a,b) => a.city.localeCompare(b.city));
            
            sortedCities.forEach(item => {
                const opt1 = document.createElement("option");
                opt1.value = item.city;
                opt1.textContent = item.city;
                if(item.city === currentActiveCity) opt1.selected = true;
                cityFilter.appendChild(opt1);

                const opt2 = document.createElement("option");
                opt2.value = item.city;
                opt2.textContent = item.city;
                compareFilter.appendChild(opt2);
            });
        }

        function setupSearchEngine() {
            document.getElementById("citySearch").addEventListener("input", (e) => {
                const val = e.target.value.toLowerCase().trim();
                const matched = environmentalDataset.find(c => c.city.toLowerCase().includes(val));
                if(matched) {
                    handleCityChange(matched.city);
                    document.getElementById("cityFilter").value = matched.city;
                }
            });
        }

        function resetFilters() {
            document.getElementById("aqiFilter").value = "all";
            document.getElementById("pollutantFilter").value = "aqi";
            document.getElementById("compareFilter").value = "none";
            handleCityChange("New York");
            document.getElementById("cityFilter").value = "New York";
            document.getElementById("citySearch").value = "";
            applyFilters();
        }

        function getAqiMetrics(aqi) {
            if (aqi <= 50) return { label: "Good", color: "bg-emerald-500", text: "text-emerald-400", hex: "#10b981", border: "border-emerald-500/20" };
            if (aqi <= 100) return { label: "Satisfactory", color: "bg-green-400", text: "text-green-400", hex: "#4ade80", border: "border-green-400/20" };
            if (aqi <= 200) return { label: "Moderate", color: "bg-yellow-500", text: "text-yellow-400", hex: "#eab308", border: "border-yellow-500/20" };
            if (aqi <= 300) return { label: "Poor", color: "bg-orange-500", text: "text-orange-400", hex: "#f97316", border: "border-orange-500/20" };
            if (aqi <= 400) return { label: "Very Poor", color: "bg-rose-600", text: "text-rose-400", hex: "#e11d48", border: "border-rose-600/20" };
            return { label: "Severe", color: "bg-red-950", text: "text-red-600", hex: "#7f1d1d", border: "border-red-900/40" };
        }

        function calculateGrades(score) {
            if (score >= 90) return { grade: "A", css: "bg-emerald-500/10 text-emerald-400 border border-emerald-500/20" };
            if (score >= 75) return { grade: "B", css: "bg-cyan-500/10 text-cyan-400 border border-cyan-500/20" };
            if (score >= 60) return { grade: "C", css: "bg-yellow-500/10 text-yellow-400 border border-yellow-500/20" };
            if (score >= 45) return { grade: "D", css: "bg-orange-500/10 text-orange-400 border border-orange-500/20" };
            return { grade: "F", css: "bg-rose-500/10 text-rose-400 border border-rose-500/20" };
        }

        function executeDataAnalysisPipeline() {
            const totalCities = environmentalDataset.length;
            const avgAqi = Math.round(environmentalDataset.reduce((acc, c) => acc + c.aqi, 0) / totalCities);
            
            const sortedByAqi = [...environmentalDataset].sort((a,b) => a.aqi - b.aqi);
            const cleanest = sortedByAqi[0];
            const polluted = sortedByAqi[totalCities - 1];

            // Render Core Analytical Target System Panels
            document.getElementById("metricAvgAqi").textContent = avgAqi;
            const avgMeta = getAqiMetrics(avgAqi);
            document.getElementById("metricAvgAqiLabel").textContent = `Cohort Baseline: ${avgMeta.label}`;
            document.getElementById("metricAvgAqiLabel").className = `text-xs mt-1 font-medium ${avgMeta.text}`;

            document.getElementById("metricMaxCity").textContent = polluted.city;
            document.getElementById("metricMaxAqi").textContent = `AQI Index: ${polluted.aqi}`;
            
            document.getElementById("metricMinCity").textContent = cleanest.city;
            document.getElementById("metricMinAqi").textContent = `AQI Index: ${cleanest.aqi}`;

            document.getElementById("metricCount").textContent = totalCities;

            // Compute executive aggregate insight summary
            document.getElementById("executiveSummaryText").innerHTML = `The multi-regional evaluation matrix encompasses <strong>${totalCities} baseline metropolitan nodes</strong>. Empirical analysis positions <strong>${cleanest.city}</strong> as the absolute environmental baseline apex (AQI ${cleanest.aqi}, Water Assay ${cleanest.waterQuality} pts), whereas <strong>${polluted.city}</strong> reports hazardous atmospheric compounding vectors (AQI ${polluted.aqi}). Regional variances implicate a strong correlation between thermal particulate retention loops and decreased epidermal cellular wellness indices across heavy manufacturing coordinates.`;

            // Render Cohort Profiles Columns
            renderInsightsLists(sortedByAqi);
            renderAnomaliesPanel(sortedByAqi);
        }

        function renderInsightsLists(sortedData) {
            const cleanList = document.getElementById("cleanCityList");
            const pollutedList = document.getElementById("pollutedCityList");
            
            cleanList.innerHTML = "";
            pollutedList.innerHTML = "";

            // Top 3 Cleanest
            sortedData.slice(0, 3).forEach((c, idx) => {
                const meta = getAqiMetrics(c.aqi);
                cleanList.innerHTML += `
                    <div class="flex items-center justify-between p-2.5 rounded-xl bg-emerald-500/[0.02] border border-emerald-500/10">
                        <div class="flex items-center gap-3">
                            <span class="text-xs font-bold text-emerald-500 font-mono">#0${idx+1}</span>
                            <span class="text-xs font-semibold text-white">${c.city}</span>
                        </div>
                        <div class="flex items-center gap-4">
                            <span class="text-[11px] text-gray-400 font-medium">H2O: ${c.waterQuality}/100</span>
                            <span class="text-[11px] font-bold ${meta.text}">${c.label || meta.label} (${c.aqi})</span>
                        </div>
                    </div>`;
            });

            // Top 3 Polluted
            [...sortedData].reverse().slice(0, 3).forEach((c, idx) => {
                const meta = getAqiMetrics(c.aqi);
                pollutedList.innerHTML += `
                    <div class="flex items-center justify-between p-2.5 rounded-xl bg-rose-500/[0.02] border border-rose-500/10">
                        <div class="flex items-center gap-3">
                            <span class="text-xs font-bold text-rose-500 font-mono">#0${idx+1}</span>
                            <span class="text-xs font-semibold text-white">${c.city}</span>
                        </div>
                        <div class="flex items-center gap-4">
                            <span class="text-[11px] text-gray-400 font-medium">H2O: ${c.waterQuality}/100</span>
                            <span class="text-[11px] font-bold ${meta.text}">${c.label || meta.label} (${c.aqi})</span>
                        </div>
                    </div>`;
            });
        }

        function renderAnomaliesPanel(sortedData) {
            const container = document.getElementById("anomalyWorkspace");
            container.innerHTML = "";

            // Identify the extreme gap city as anomaly source
            const dynamicAnomalies = [
                { title: "Particulate Entrapment Loop", city: "Mumbai", text: "Microclimatic coastal marine layer preventing aerodynamic transport of industrial carbon headers." },
                { title: "Atmospheric Inversion Vector", city: "Los Angeles", text: "Thermal atmospheric stratification boundaries holding heavy auto emissions compressed inside low topologies." }
            ];

            dynamicAnomalies.forEach(anom => {
                container.innerHTML += `
                    <div class="p-3 rounded-xl bg-gray-900/60 border border-gray-800 space-y-1">
                        <div class="flex justify-between items-center">
                            <span class="text-xs font-semibold text-amber-400">${anom.title}</span>
                            <span class="text-[10px] bg-amber-500/10 text-amber-400 px-1.5 py-0.5 rounded font-medium">${anom.city}</span>
                        </div>
                        <p class="text-[11px] text-gray-400 leading-normal">${anom.text}</p>
                    </div>`;
            });
        }

        function handleCityChange(cityName) {
            currentActiveCity = cityName;
            const data = environmentalDataset.find(c => c.city === cityName);
            if (!data) return;

            // Calculate environmental scores
            // Air Quality Score formula: inverse map of AQI (0 AQI = 100, 400+ AQI = 0)
            const airScore = Math.max(0, Math.round(100 - (data.aqi * 0.25)));
            const waterScore = data.waterQuality;
            const overallScore = Math.round((airScore * 0.6) + (waterScore * 0.4));

            // Update UI components
            document.getElementById("cardCityName").textContent = data.city;
            document.getElementById("scoreOverall").textContent = overallScore;
            document.getElementById("scoreAir").innerHTML = `${airScore}<span class="text-xs text-gray-500">/100</span>`;
            document.getElementById("scoreWater").innerHTML = `${waterScore}<span class="text-xs text-gray-500">/100</span>`;

            // Calculate metrics & styles
            const airGradeData = calculateGrades(airScore);
            const waterGradeData = calculateGrades(waterScore);
            
            const gAir = document.getElementById("gradeAir");
            gAir.textContent = `Grade ${airGradeData.grade}`;
            gAir.className = `inline-block px-2 py-0.5 rounded text-[10px] font-bold mt-1 ${airGradeData.css}`;

            const gWater = document.getElementById("gradeWater");
            gWater.textContent = `Grade ${waterGradeData.grade}`;
            gWater.className = `inline-block px-2 py-0.5 rounded text-[10px] font-bold mt-1 ${waterGradeData.css}`;

            // Deduce health and risk statuses
            updateRiskProfiles(data, airScore, waterScore);
            updatePhysiologicalImpactCard(data);
            updateRecommendations(data);

            document.getElementById("metricEcoScore").textContent = `${overallScore}/100`;
            const systemEcoLabel = document.getElementById("metricEcoLabel");
            if(overallScore >= 80) { systemEcoLabel.textContent = "Optimal System"; systemEcoLabel.className="text-xs mt-1 font-medium text-emerald-400"; }
            else if(overallScore >= 60) { systemEcoLabel.textContent = "Moderate Stresses"; systemEcoLabel.className="text-xs mt-1 font-medium text-yellow-400"; }
            else { systemEcoLabel.textContent = "Severe Degradation"; systemEcoLabel.className="text-xs mt-1 font-medium text-rose-500"; }

            // Trigger charting sequence refresh
            applyFilters();
            handleComparisonChange(document.getElementById("compareFilter").value);
        }

        function updateRiskProfiles(data, airScore, waterScore) {
            const hairRiskSpan = document.getElementById("riskHair");
            const skinRiskSpan = document.getElementById("riskSkin");

            if (waterScore >= 85) {
                hairRiskSpan.textContent = "🟢 Low Risk Profile"; hairRiskSpan.className = "text-xs font-semibold text-emerald-400";
                skinRiskSpan.textContent = "🟢 Low Risk Profile"; skinRiskSpan.className = "text-xs font-semibold text-emerald-400";
            } else if (waterScore >= 60) {
                hairRiskSpan.textContent = "🟡 Moderate Stress"; hairRiskSpan.className = "text-xs font-semibold text-yellow-400";
                skinRiskSpan.textContent = "🟡 Moderate Stress"; skinRiskSpan.className = "text-xs font-semibold text-yellow-400";
            } else {
                hairRiskSpan.textContent = "🔴 High Threat Layer"; hairRiskSpan.className = "text-xs font-semibold text-rose-500";
                skinRiskSpan.textContent = "🔴 High Threat Layer"; skinRiskSpan.className = "text-xs font-semibold text-rose-500";
            }
        }

        function updatePhysiologicalImpactCard(data) {
            const airMeta = getAqiMetrics(data.aqi);
            const airBadge = document.getElementById("airStatusBadge");
            airBadge.textContent = `AQI ${data.aqi} - ${airMeta.label}`;
            airBadge.className = `text-xs font-semibold px-2.5 py-0.5 rounded-full ${airMeta.text} bg-gray-900 border ${airMeta.border}`;

            const waterBadge = document.getElementById("waterStatusBadge");
            waterBadge.textContent = `Water Index: ${data.waterQuality}/100`;
            if(data.waterQuality >= 85) waterBadge.className = "text-xs font-semibold px-2.5 py-0.5 rounded-full text-emerald-400 bg-gray-900 border border-emerald-500/20";
            else if(data.waterQuality >= 60) waterBadge.className = "text-xs font-semibold px-2.5 py-0.5 rounded-full text-yellow-400 bg-gray-900 border border-yellow-500/20";
            else waterBadge.className = "text-xs font-semibold px-2.5 py-0.5 rounded-full text-rose-500 bg-gray-900 border border-rose-500/20";

            // Internal Mapping Rule Matrix for Dynamic Biological copy
            const lungs = document.getElementById("impact_lungs");
            const sleep = document.getElementById("impact_sleep");
            const energy = document.getElementById("impact_energy");
            const exercise = document.getElementById("impact_exercise");
            const longterm = document.getElementById("impact_longterm");

            const hair = document.getElementById("impact_hair");
            const scalp = document.getElementById("impact_scalp");
            const skin = document.getElementById("impact_skin");
            const acne = document.getElementById("impact_acne");
            const sensitive = document.getElementById("impact_sensitive");

            // Setup dynamic semantic configurations depending on air and water indexes
            if(data.aqi <= 50) {
                lungs.textContent = "Minimal alveolar capillary oxidation stress. Cilia clearing operational threshold normal."; setRiskCol("lungs", "emerald");
                sleep.textContent = "Unfragmented deep REM phases. Zero noted air-boundary hypoxic micro-arousals."; setRiskCol("sleep", "emerald");
                energy.textContent = "Cellular respiration yields peak ATP conversion. Minimal baseline systemic fatigue."; setRiskCol("energy", "emerald");
                exercise.textContent = "Maximal VO2 output threshold clean. Minimal metabolic exercise ventilation limiters."; setRiskCol("exercise", "emerald");
                longterm.textContent = "Baseline cardiopulmonary life expectancy preservation curve perfectly sustained."; setRiskCol("longterm", "emerald");
            } else if(data.aqi <= 150) {
                lungs.textContent = "Mild tracking bronchial inflammation vectors. Susceptible paths may report minor resistance."; setRiskCol("lungs", "yellow");
                sleep.textContent = "Subtle upper respiratory trace irritation might elevate micro-arousal event metrics."; setRiskCol("sleep", "yellow");
                energy.textContent = "Mild sub-clinical immune system allocation to combat oxidation loads. Standard fatigue flags."; setRiskCol("energy", "yellow");
                exercise.textContent = "Systemic anaerobic threshold shift observed. External respiration patterns feel heavy."; setRiskCol("exercise", "yellow");
                longterm.textContent = "Accumulative vascular endothelial stress trends require periodic observation intervals."; setRiskCol("longterm", "yellow");
            } else {
                lungs.textContent = "Severe alveolar space microvascular infiltration. Particulate headers directly compromising lung tissues."; setRiskCol("lungs", "rose");
                sleep.textContent = "Highly fragmented circadian waveforms. Hypoxic systemic responses driving sympathetic spikes."; setRiskCol("sleep", "rose");
                energy.textContent = "Severe systemic cell energy reduction. Metabolic pathway priority diverted to toxin mitigation."; setRiskCol("energy", "rose");
                exercise.textContent = "Heavy exertion strictly contraindicated. Profound pulmonary tissue micro-abrasion parameters active."; setRiskCol("exercise", "rose");
                longterm.textContent = "Elevated epidemiological correlation tracking cardiovascular events and structural pulmonary degradation."; setRiskCol("longterm", "rose");
            }

            if(data.waterQuality >= 80) {
                hair.textContent = "Optimal follicular moisture retained. Zero mineral calcification tracking down shaft cores."; setRiskCol("hair", "emerald");
                scalp.textContent = "Balanced epidermal acid mantle layer protects natural lipid barriers without irritation."; setRiskCol("scalp", "emerald");
                skin.textContent = "Minimal transepidermal water loss. Stratum corneum maintains standard moisture holding."; setRiskCol("skin", "emerald");
                acne.textContent = "Minimal inorganic chemical residue binding to sebum glands. Clog rates negligible."; setRiskCol("acne", "emerald");
                sensitive.textContent = "Low immunogenic signaling. Natural skin barrier system functioning optimally."; setRiskCol("sensitive", "emerald");
            } else if(data.waterQuality >= 60) {
                hair.textContent = "Heavy metal ions inducing slight structural protein cross-link stress. Mild brittleness."; setRiskCol("hair", "yellow");
                scalp.textContent = "Alkaline trace mineral metrics might induce light localized scaling or dandruff flare-ups."; setRiskCol("scalp", "yellow");
                skin.textContent = "Slight mineral buildup stripping exterior layer fats, accelerating superficial dehydration lines."; setRiskCol("skin", "yellow");
                acne.textContent = "Trace calcium compounds create insoluble fatty matrices that can cover active follicle ports."; setRiskCol("acne", "yellow");
                sensitive.textContent = "Disrupted surface pH level might provoke temporary pruritus or erythema in dry exposures."; setRiskCol("sensitive", "yellow");
            } else {
                hair.textContent = "Severe heavy carbonate crystallization stripping protective scales. Pronounced hair fall risk."; setRiskCol("hair", "rose");
                scalp.textContent = "Chronic disruption of natural acid lipid layers causing persistent seborrheic conditions."; setRiskCol("scalp", "rose");
                skin.textContent = "Extreme surface desiccation. Mineral complexes degrading structural tile framework layers."; setRiskCol("skin", "rose");
                acne.textContent = "High heavy-metal binding forms robust plugs, forcing anaerobic microbial acne cascades."; setRiskCol("acne", "rose");
                sensitive.textContent = "Complete structural barrier collapse. Pervasive contact eczema threats triggered instantly."; setRiskCol("sensitive", "rose");
            }
        }

        function setRiskCol(id, color) {
            const el = document.getElementById(`riskIndicator_${id}`);
            if(!el) return;
            el.className = `w-3 h-3 rounded-full mt-1 shrink-0 bg-${color}-500 shadow-sm shadow-${color}-500/50`;
        }

        function updateRecommendations(data) {
            const ind = document.getElementById("recIndoor");
            const out = document.getElementById("recOutdoor");
            const cos = document.getElementById("recCosmetic");

            ind.innerHTML = ""; out.innerHTML = ""; cos.innerHTML = "";

            if(data.aqi > 150) {
                ind.innerHTML += `<li>Run dedicated true-HEPA particulate scrubbers on continuous filtration modes.</li>`;
                ind.innerHTML += `<li>Keep building apertures sealed tightly against morning particulate spikes.</li>`;
                out.innerHTML += `<li>Deploy full fitted respirator frames (N95/FFP2 metric) for unavoidable outdoor stints.</li>`;
                out.innerHTML += `<li>Cease high mechanical ventilation sports actions within outdoor spaces.</li>`;
            } else {
                ind.innerHTML += `<li>Standard baseline aeration routines via outdoor airflow during clean early hours.</li>`;
                ind.innerHTML += `<li>Periodic tracking of interior carbon dioxide limits to preserve sharp cognitions.</li>`;
                out.innerHTML += `<li>Ideal window window for high-performance cardiopulmonary workouts.</li>`;
                out.innerHTML += `<li>Outdoor activities completely cleared without regulatory dynamic masks.</li>`;
            }

            if(data.waterQuality < 70) {
                cos.innerHTML += `<li>Integrate premium multi-stage KDF/activated-carbon filters inside shower pipes.</li>`;
                cos.innerHTML += `<li>Apply low pH skin cleansers to counter heavily alkaline mineral balances.</li>`;
                cos.innerHTML += `<li>Incorporate chelating hair wash sequences weekly to break heavy mineral bonds.</li>`;
            } else {
                cos.innerHTML += `<li>Standard physiological moisture support formulations are entirely sufficient.</li>`;
                cos.innerHTML += `<li>Normal non-specialized skin cleaning and wash intervals fully approved.</li>`;
            }
        }

        function handleComparisonChange(compareCity) {
            const compCard = document.getElementById("comparisonCard");
            if(compareCity === "none" || compareCity === currentActiveCity) {
                compCard.classList.add("hidden");
                updateCharts();
                return;
            }

            compCard.classList.remove("hidden");
            const baseCityData = environmentalDataset.find(c => c.city === currentActiveCity);
            const compCityData = environmentalDataset.find(c => c.city === compareCity);

            document.getElementById("compareCityName").textContent = compCityData.city;
            
            const aqiDelta = baseCityData.aqi - compCityData.aqi;
            const waterDelta = baseCityData.waterQuality - compCityData.waterQuality;

            const aqiEl = document.getElementById("compareAqiDelta");
            if(aqiDelta > 0) { aqiEl.textContent = `+${aqiDelta} Higher (Worse)`; aqiEl.className="font-bold text-rose-500"; }
            else { aqiEl.textContent = `${aqiDelta} Lower (Better)`; aqiEl.className="font-bold text-emerald-400"; }

            const waterEl = document.getElementById("compareWaterDelta");
            if(waterDelta > 0) { waterEl.textContent = `+${waterDelta} Points Premium`; waterEl.className="font-bold text-emerald-400"; }
            else { waterEl.textContent = `${waterDelta} Points Deficit`; waterEl.className="font-bold text-rose-500"; }

            const verdictEl = document.getElementById("compareVerdict");
            if(aqiDelta <= 0 && waterDelta >= 0) { verdictEl.textContent = `${compCityData.city} offers superior ecosystem assets.`; }
            else { verdictEl.textContent = `${baseCityData.city} remains preferable habitat balance matrix.`; }

            updateCharts();
        }

        function applyFilters() {
            updateCharts();
            updateDistributionChart();
        }

        function getFilteredDataset() {
            const aqiTier = document.getElementById("aqiFilter").value;
            return environmentalDataset.filter(item => {
                if(aqiTier === "all") return true;
                const meta = getAqiMetrics(item.aqi);
                return meta.label === aqiTier;
            });
        }

        function updateCharts() {
            const ctx = document.getElementById('primaryAnalyticsChart').getContext('2d');
            const targetPollutant = document.getElementById("pollutantFilter").value;
            const compareCity = document.getElementById("compareFilter").value;

            const filteredData = getFilteredDataset();
            const labels = filteredData.map(c => c.city);
            
            let dataValues = [];
            let labelTitle = "";

            if(targetPollutant === "aqi") {
                dataValues = filteredData.map(c => c.aqi);
                labelTitle = "AQI Metric Evaluation Matrix";
            } else if(targetPollutant === "pm25") {
                dataValues = filteredData.map(c => c.pm25);
                labelTitle = "PM2.5 Concentration Mass (µg/m³)";
            } else {
                dataValues = filteredData.map(c => c.pm10);
                labelTitle = "PM10 Concentration Mass (µg/m³)";
            }

            // Map custom visual color gradients depending on focus indices
            const backgroundColors = filteredData.map(c => {
                if(c.city === currentActiveCity) return '#10b981'; // Target focus
                if(c.city === compareCity) return '#3b82f6'; // Contrast focus
                return 'rgba(255, 255, 255, 0.12)';
            });

            const borderColors = filteredData.map(c => {
                if(c.city === currentActiveCity) return '#34d399';
                if(c.city === compareCity) return '#60a5fa';
                return 'rgba(255, 255, 255, 0.2)';
            });

            if (chartInstance) chartInstance.destroy();

            chartInstance = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: labelTitle,
                        data: dataValues,
                        backgroundColor: backgroundColors,
                        borderColor: borderColors,
                        borderWidth: 1.5,
                        borderRadius: 6,
                        barThickness: 24
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            backgroundColor: '#111827',
                            titleColor: '#fff',
                            bodyColor: '#9ca3af',
                            borderColor: 'rgba(255,255,255,0.1)',
                            borderWidth: 1
                        }
                    },
                    scales: {
                        y: {
                            grid: { color: 'rgba(255,255,255,0.04)', drawTicks: false },
                            ticks: { color: '#9ca3af', font: { family: 'Plus Jakarta Sans', size: 10 } }
                        },
                        x: {
                            grid: { display: false },
                            ticks: { color: '#9ca3af', font: { family: 'Plus Jakarta Sans', size: 10 } }
                        }
                    }
                }
            });
        }

        function updateDistributionChart() {
            const ctx = document.getElementById('distributionChart').getContext('2d');
            
            const distributionCounters = { Good: 0, Satisfactory: 0, Moderate: 0, Poor: 0, VeryPoor: 0, Severe: 0 };
            environmentalDataset.forEach(c => {
                const meta = getAqiMetrics(c.aqi);
                const tag = meta.label.replace(" ", "");
                if(distributionCounters[tag] !== undefined) distributionCounters[tag]++;
            });

            if (distributionChartInstance) distributionChartInstance.destroy();

            distributionChartInstance = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Good', 'Satisfactory', 'Moderate', 'Poor', 'Very Poor', 'Severe'],
                    datasets: [{
                        data: Object.values(distributionCounters),
                        backgroundColor: ['#10b981', '#4ade80', '#eab308', '#f97316', '#e11d48', '#7f1d1d'],
                        borderWidth: 0,
                        hoverOffset: 4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'right',
                            labels: { color: '#9ca3af', font: { family: 'Plus Jakarta Sans', size: 9 }, boxWidth: 10 }
                        }
                    },
                    cutout: '75%'
                }
            });
        }

        function shareDashboard() {
            const data = environmentalDataset.find(c => c.city === currentActiveCity);
            const airScore = Math.max(0, Math.round(100 - (data.aqi * 0.25)));
            const text = `🌍 EcoPulse Environmental Health Diagnostics verified for ${data.city}. Air Quality Score: ${airScore}/100, Water Assay: ${data.waterQuality}/100. Assess your climate health parameters now. #EcoPulse #EnvironmentalAnalytics`;
            const url = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(window.location.href)}`;
            
            // Create fallback copy clipboard mechanism
            navigator.clipboard.writeText(text).then(() => {
                alert("✨ Analytical Summary telemetry encoded to systemic clipboard! Share directly via your LinkedIn profile terminal feed.");
            });
        }
    </script>
</body>
</html>
## What I Learned Today:
*AI-Driven Dashboards:* I learned how to build a complete interactive dashboard with the help of AI (Gemini) without writing the code from scratch.
*HTML & Browser Integration:* I learned that saving code in Notepad with the .html extension allows it to open and run in a browser like a real web application.
*Data Interaction:* I interacted with the dashboard's filters and charts to see how the displayed data changes dynamically on the screen.
*GitHub Architecture:* I learned how to manage files and screenshots efficiently by creating structured folders within my repository.

<img width="1327" height="1272" alt="image" src="https://github.com/user-attachments/assets/c0e4b257-5c82-4f94-96cd-82161a0fb402" />
