#  AB Talks 60-Days Challenge - Day 9

##  Project: NutriScope MVP

###  Prompt Used to Build MVP:
Act as an expert frontend web developer. Build a complete single-file HTML application called "NutriScope" (including CSS for professional styling and JavaScript for functionality).

The application must include the following specific features as per these requirements:
1. Profile Inputs (Form Section): Age, Gender, Height, Weight, Activity Level, and Dietary Preference (Vegetarian, Non-Vegetarian, Eggetarian).
2. Food Logging Section: Add Food, specify Quantity, and select Unit with an Editable Table and "Remove Entry" button.
3. Built-in Food Database: 20 common foods only (Rice, Roti, Dal, Paneer, Curd, Chana, Rajma, Banana, Apple, Milk, Oats, Bread, Egg, Chicken, Fish, Potato, Poha, Idli, Dosa, Spinach).
4. Tracking & Calculations Section: Calories, Protein, Carbs, Fat, Fiber, Iron, Calcium, Vitamin C, Vitamin D, Vitamin B12.
<img width="1141" height="634" alt="image" src="https://github.com/user-attachments/assets/01938804-27a7-4452-a186-67ba7ecb4294" />

Now, please enhance this NutriScope application to make it look premium and production-ready. Please update the previous code with the following improvements:

Advanced UI/UX: Use a beautiful, modern color palette (shades of healthy greens, deep neutrals, and crisp white), clean modern typography, smooth transition animations, and a polished dashboard card layout.
Visual Charts: Integrate a simple visual breakdown (using standard CSS progress bars or an easy inline library like Chart.js) to show the macronutrient distribution dynamically.
Enhanced Target Metrics: Improve the dynamic calculation engine so that when profile details change, the daily intake targets adjust gracefully with a visual feedback indicator.
Responsiveness: Ensure the design adapts flawlessly to mobile screens, tablets, and desktops.

Please provide the complete, updated code in a single HTML file inside one code block.
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NutriScope Pro - Precision Nutrition Tracker</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
        body { font-family: 'Plus Jakarta Sans', sans-serif; }
    </style>
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen antialiased">

    <header class="border-b border-slate-800 bg-slate-950/50 backdrop-blur sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
            <div class="flex items-center gap-3">
                <div class="bg-emerald-500 text-slate-950 p-2 rounded-xl font-bold text-xl shadow-lg shadow-emerald-500/20">NS</div>
                <div>
                    <h1 class="text-xl font-bold tracking-tight bg-gradient-to-r from-emerald-400 to-teal-300 bg-clip-text text-transparent">NutriScope Pro</h1>
                    <p class="text-xs text-slate-400">Day 9 Enhanced Production Build</p>
                </div>
            </div>
            <span class="bg-slate-800 text-slate-300 px-3 py-1 rounded-full text-xs font-medium border border-slate-700">AB Talks 60-Days Challenge</span>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 py-8 grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div class="space-y-6">
            <section class="bg-slate-950/60 border border-slate-800 rounded-2xl p-6 shadow-xl backdrop-blur">
                <h2 class="text-lg font-semibold mb-4 text-emerald-400 flex items-center gap-2">
                     User Profile & Targets
                </h2>
                <form id="profileForm" class="space-y-4">
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs text-slate-400 mb-1">Age (Years)</label>
                            <input type="number" id="age" value="25" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-sm focus:border-emerald-500 focus:outline-none transition">
                        </div>
                        <div>
                            <label class="block text-xs text-slate-400 mb-1">Gender</label>
                            <select id="gender" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-sm focus:border-emerald-500 focus:outline-none transition">
                                <option value="male">Male</option>
                                <option value="female">Female</option>
                            </select>
                        </div>
                    </div>
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs text-slate-400 mb-1">Height (cm)</label>
                            <input type="number" id="height" value="175" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-sm focus:border-emerald-500 focus:outline-none transition">
                        </div>
                        <div>
                            <label class="block text-xs text-slate-400 mb-1">Weight (kg)</label>
                            <input type="number" id="weight" value="70" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-sm focus:border-emerald-500 focus:outline-none transition">
                        </div>
                    </div>
                    <div>
                        <label class="block text-xs text-slate-400 mb-1">Activity Level</label>
                        <select id="activity" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-sm focus:border-emerald-500 focus:outline-none transition">
                            <option value="1.2">Sedentary (Little/No Exercise)</option>
                            <option value="1.375" selected>Lightly Active (1-3 days/week)</option>
                            <option value="1.55">Moderately Active (3-5 days/week)</option>
                            <option value="1.725">Very Active (6-7 days/week)</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-xs text-slate-400 mb-1">Dietary Preference</label>
                        <select id="diet" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-sm focus:border-emerald-500 focus:outline-none transition">
                            <option value="Vegetarian">Vegetarian</option>
                            <option value="Non-Vegetarian" selected>Non-Vegetarian</option>
                            <option value="Eggetarian">Eggetarian</option>
                        </select>
                    </div>
                </form>
            </section>

            <section class="bg-slate-950/40 border border-slate-800 rounded-2xl p-5 space-y-3">
                <h3 class="text-xs font-semibold uppercase tracking-wider text-slate-400">Calculated Dynamic Goals</h3>
                <div class="flex justify-between items-center bg-slate-900/50 p-3 rounded-xl border border-slate-800/80">
                    <span class="text-sm">Target Calories:</span>
                    <span id="targetCaloriesDisplay" class="text-base font-bold text-teal-400">-- kcal</span>
                </div>
            </section>
        </div>

        <div class="lg:col-span-2 space-y-6">
            <section class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="bg-slate-950/60 border border-slate-800 p-5 rounded-2xl flex flex-col justify-between">
                    <span class="text-xs text-slate-400 uppercase tracking-wider font-medium">Energy Consumed</span>
                    <div class="mt-2 flex items-baseline gap-2">
                        <span id="totalCalories" class="text-3xl font-bold text-emerald-400">0</span>
                        <span class="text-xs text-slate-500">/ <span id="targetCalText">2000</span> kcal</span>
                    </div>
                    <div class="w-full bg-slate-800 h-1.5 rounded-full mt-3 overflow-hidden">
                        <div id="calorieBar" class="bg-gradient-to-r from-emerald-500 to-teal-400 h-full transition-all duration-500" style="width: 0%"></div>
                    </div>
                </div>
                <div class="bg-slate-950/60 border border-slate-800 p-5 rounded-2xl md:col-span-2">
                    <span class="text-xs text-slate-400 uppercase tracking-wider font-medium">Macro Distribution Analytics</span>
                    <div class="grid grid-cols-2 gap-4 mt-2 items-center">
                        <div class="space-y-2 text-sm">
                            <div class="flex justify-between"><span class="text-rose-400 font-medium">Protein:</span><span id="pLog">0g</span></div>
                            <div class="flex justify-between"><span class="text-amber-400 font-medium">Carbs:</span><span id="cLog">0g</span></div>
                            <div class="flex justify-between"><span class="text-sky-400 font-medium">Fats:</span><span id="fLog">0g</span></div>
                        </div>
                        <div class="h-24 flex justify-center">
                            <canvas id="macroChart"></canvas>
                        </div>
                    </div>
                </div>
            </section>

            <section class="bg-slate-950/60 border border-slate-800 rounded-2xl p-6 shadow-xl">
                <h2 class="text-lg font-semibold mb-4 text-emerald-400 flex items-center gap-2">
                     Interactive Food Logger
                </h2>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-4">
                    <select id="foodSelect" class="bg-slate-900 border border-slate-700 rounded-xl px-3 py-2.5 text-sm focus:border-emerald-500 focus:outline-none transition">
                        </select>
                    <input type="number" id="foodQty" value="100" min="1" class="bg-slate-900 border border-slate-700 rounded-xl px-3 py-2.5 text-sm focus:border-emerald-500 focus:outline-none transition" placeholder="Quantity">
                    <select id="foodUnit" class="bg-slate-900 border border-slate-700 rounded-xl px-3 py-2.5 text-sm focus:border-emerald-500 focus:outline-none transition">
                        <option value="g">Grams (g)</option>
                        <option value="pc">Piece (pc)</option>
                    </select>
                </div>
                <button id="addFoodBtn" class="w-full bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-600 hover:to-teal-600 text-slate-950 font-semibold py-2.5 rounded-xl transition shadow-lg shadow-emerald-500/10 cursor-pointer">
                    + Add Logged Food Entry
                </button>

                <div class="mt-6 overflow-x-auto">
                    <table class="w-full text-left border-collapse text-sm">
                        <thead>
                            <tr class="border-b border-slate-800 text-slate-400">
                                <th class="pb-3 font-medium">Food Item</th>
                                <th class="pb-3 font-medium">Qty/Unit</th>
                                <th class="pb-3 font-medium">Calories</th>
                                <th class="pb-3 font-medium text-right">Actions</th>
                            </tr>
                        </thead>
                        <tbody id="logTableBody" class="divide-y divide-slate-800/50">
                            </tbody>
                    </table>
                </div>
            </section>

            <section class="bg-slate-950/40 border border-slate-800 rounded-2xl p-6">
                <h3 class="text-sm font-semibold uppercase tracking-wider text-slate-400 mb-4">Micronutrient Completion Monitor</h3>
                <div class="grid grid-cols-2 sm:grid-cols-3 gap-4" id="microContainer">
                    </div>
            </section>
        </div>
    </main>

    <script>
        // Exactly 20 Common Foods Database as specified in the rules
        const foodDatabase = {
            "Rice": { cal: 130, p: 2.7, c: 28, f: 0.3, fiber: 0.4, iron: 1.2, calcium: 10, vitC: 0, vitD: 0, vitB12: 0, diet: "Vegetarian" },
            "Roti": { cal: 120, p: 3.5, c: 22, f: 0.5, fiber: 3.2, iron: 1.5, calcium: 20, vitC: 0, vitD: 0, vitB12: 0, diet: "Vegetarian" },
            "Dal": { cal: 150, p: 9.0, c: 24, f: 1.0, fiber: 5.0, iron: 2.7, calcium: 30, vitC: 1.5, vitD: 0, vitB12: 0, diet: "Vegetarian" },
            "Paneer": { cal: 265, p: 18.0, c: 3.5, f: 20.0, fiber: 0, iron: 0.5, calcium: 480, vitC: 0, vitD: 0.2, vitB12: 0.8, diet: "Vegetarian" },
            "Curd": { cal: 98, p: 4.3, c: 4.7, f: 4.3, fiber: 0, iron: 0.1, calcium: 120, vitC: 0, vitD: 0.1, vitB12: 0.4, diet: "Vegetarian" },
            "Chana": { cal: 164, p: 8.9, c: 27, f: 2.6, fiber: 7.6, iron: 2.9, calcium: 49, vitC: 1.0, vitD: 0, vitB12: 0, diet: "Vegetarian" },
            "Rajma": { cal: 140, p: 9.0, c: 23, f: 0.6, fiber: 6.4, iron: 2.9, calcium: 35, vitC: 1.2, vitD: 0, vitB12: 0, diet: "Vegetarian" },
            "Banana": { cal: 89, p: 1.1, c: 23, f: 0.3, fiber: 2.6, iron: 0.3, calcium: 5, vitC: 8.7, vitD: 0, vitB12: 0, diet: "Vegetarian" },
            "Apple": { cal: 52, p: 0.3, c: 14, f: 0.2, fiber: 2.4, iron: 0.1, calcium: 6, vitC: 4.6, vitD: 0, vitB12: 0, diet: "Vegetarian" },
            "Milk": { cal: 61, p: 3.2, c: 4.8, f: 3.3, fiber: 0, iron: 0.05, calcium: 115, vitC: 1.0, vitD: 0.5, vitB12: 0.5, diet: "Vegetarian" },
            "Oats": { cal: 389, p: 16.9, c: 66, f: 6.9, fiber: 10.6, iron: 4.7, calcium: 54, vitC: 0, vitD: 0, vitB12: 0, diet: "Vegetarian" },
            "Bread": { cal: 265, p: 9.0, c: 49, f: 3.2, fiber: 2.7, iron: 3.6, calcium: 260, vitC: 0, vitD: 0, vitB12: 0, diet: "Vegetarian" },
            "Egg": { cal: 155, p: 13.0, c: 1.1, f: 11.0, fiber: 0, iron: 1.2, calcium: 50, vitC: 0, vitD: 2.0, vitB12: 1.1, diet: "Eggetarian" },
            "Chicken": { cal: 239, p: 27.0, c: 0, f: 14.0, fiber: 0, iron: 1.3, calcium: 15, vitC: 0, vitD: 0.1, vitB12: 0.3, diet: "Non-Vegetarian" },
            "Fish": { cal: 206, p: 22.0, c: 0, f: 12.0, fiber: 0, iron: 0.9, calcium: 15, vitC: 0, vitD: 8.0, vitB12: 2.8, diet: "Non-Vegetarian" },
            "Potato": { cal: 77, p: 2.0, c: 17, f: 0.1, fiber: 2.2, iron: 0.8, calcium: 12, vitC: 19.7, vitD: 0, vitB12: 0, diet: "Vegetarian" },
            "Poha": { cal: 130, p: 2.5, c: 29, f: 0.2, fiber: 0.7, iron: 2.0, calcium: 8, vitC: 0, vitD: 0, vitB12: 0, diet: "Vegetarian" },
            "Idli": { cal: 39, p: 1.0, c: 8, f: 0.1, fiber: 0.3, iron: 0.2, calcium: 4, vitC: 0, vitD: 0, vitB12: 0, diet: "Vegetarian" },
            "Dosa": { cal: 133, p: 2.8, c: 26, f: 2.1, fiber: 0.8, iron: 0.5, calcium: 10, vitC: 0, vitD: 0, vitB12: 0, diet: "Vegetarian" },
            "Spinach": { cal: 23, p: 2.9, c: 3.6, f: 0.4, fiber: 2.2, iron: 2.7, calcium: 99, vitC: 28.1, vitD: 0, vitB12: 0, diet: "Vegetarian" }
        };

        let userLogs = [];
        let macroChart;
        let targets = { calories: 2000, protein: 60, carbs: 250, fat: 65, fiber: 30, iron: 17, calcium: 1000, vitC: 90, vitD: 15, vitB12: 2.4 };

        // Initialize UI Elements
        function init() {
            const select = document.getElementById('foodSelect');
            Object.keys(foodDatabase).forEach(food => {
                let opt = document.createElement('option');
                opt.value = food;
                opt.innerText = ${food} (${foodDatabase[food].diet[0]});
                select.appendChild(opt);
            });
            calculateTargets();
            setupChart();
            renderDashboard();
        }

        // Calculate dynamic targets using basic logic mirroring profile criteria
        function calculateTargets() {
            const weight = parseFloat(document.getElementById('weight').value) || 70;
            const height = parseFloat(document.getElementById('height').value) || 175;
            const age = parseFloat(document.getElementById('age').value) || 25;
            const gender = document.getElementById('gender').value;
            const activity = parseFloat(document.getElementById('activity').value) || 1.375;

            // Simple BMR calculation (Mifflin-St Jeor Equation)
            let bmr = (10 * weight) + (6.25 * height) - (5 * age);
            bmr = gender === 'male' ? bmr + 5 : bmr - 161;
            
            targets.calories = Math.round(bmr * activity);
            targets.protein = Math.round(weight * 1.2); // 1.2g per kg
            targets.fat = Math.round((targets.calories * 0.25) / 9);
            targets.carbs = Math.round((targets.calories - (targets.protein * 4) - (targets.fat * 9)) / 4);

            document.getElementById('targetCaloriesDisplay').innerText = ${targets.calories} kcal;
            document.getElementById('targetCalText').innerText = targets.calories;
        }

        function setupChart() {
            const ctx = document.getElementById('macroChart').getContext('2d');
            macroChart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Protein', 'Carbs', 'Fats'],
                    datasets: [{
                        data: [0, 0, 0],
                        backgroundColor: ['#f43f5e', '#fbbf24', '#38bdf8'],
                        borderWidth: 0
                    }]
                },
                options: { plugins: { legend: { display: false } }, cutout: '75%' }
            });
        }

        function renderDashboard() {
            let totals = { cal: 0, p: 0, c: 0, f: 0, fiber: 0, iron: 0, calcium: 0, vitC: 0, vitD: 0, vitB12: 0 };
            const currentDiet = document.getElementById('diet').value;
            const tbody = document.getElementById('logTableBody');
            tbody.innerHTML = '';

            userLogs.forEach((log, index) => {
                const food = foodDatabase[log.name];
                const multiplier = log.qty / 100;

                // Sum items
                totals.cal += food.cal * multiplier;
                totals.p += food.p * multiplier;
                totals.c += food.c * multiplier;
                totals.f += food.f * multiplier;
                totals.fiber += food.fiber * multiplier;
                totals.iron += food.iron * multiplier;
                totals.calcium += food.calcium * multiplier;
                totals.vitC += food.vitC * multiplier;
                totals.vitD += food.vitD * multiplier;
                totals.vitB12 += food.vitB12 * multiplier;

                // Validate dietary preferences & trigger warnings if violated
                let warningClass = "";
                if (currentDiet === "Vegetarian" && food.diet !== "Vegetarian") warningClass = "text-rose-400 bg-rose-500/10 px-1 rounded";
                if (currentDiet === "Eggetarian" && food.diet === "Non-Vegetarian") warningClass = "text-rose-400 bg-rose-500/10 px-1 rounded";

                // Injected log table rows (Editable Logs)
                let row = document.createElement('tr');
                row.className = "border-b border-slate-800/40 hover:bg-slate-800/20 transition";
                row.innerHTML = `
                    <td class="py-3 font-medium ${warningClass}">${log.name}</td>
                    <td class="py-3 text-slate-300">${log.qty}${log.unit}</td>
                    <td class="py-3 font-semibold text-emerald-400">${Math.round(food.cal * multiplier)} kcal</td>
                    <td class="py-3 text-right">
                        <button onclick="removeLog(${index})" class="text-slate-500 hover:text-rose-400 transition cursor-pointer text-xs font-semibold">Remove</button>
                    </td>
                `;
                tbody.appendChild(row);
            });

            // Update Primary Macros Visual Displays
            document.getElementById('totalCalories').innerText = Math.round(totals.cal);
            document.getElementById('pLog').innerText = ${Math.round(totals.p)}g / ${targets.protein}g;
            document.getElementById('cLog').innerText = ${Math.round(totals.c)}g / ${targets.carbs}g;
            document.getElementById('fLog').innerText = ${Math.round(totals.f)}g / ${targets.fat}g;

            // Progress Bar Engine Animation
            const calPercentage = Math.min((totals.cal / targets.calories) * 100, 100);
            document.getElementById('calorieBar').style.width = ${calPercentage}%;

            // Dynamic Chart Refresh Engine
            macroChart.data.datasets[0].data = [totals.p, totals.c, totals.f];
            macroChart.update();

            // Micronutrients Monitor Mapping
            const microContainer = document.getElementById('microContainer');
            microContainer.innerHTML = '';
            const micros = [
                { name: 'Fiber', val: totals.fiber, tgt: targets.fiber, unit: 'g' },
                { name: 'Iron', val: totals.iron, tgt: targets.iron, unit: 'mg' },
                { name: 'Calcium', val: totals.calcium, tgt: targets.calcium, unit: 'mg' },
                { name: 'Vit C', val: totals.vitC, tgt: targets.vitC, unit: 'mg' },
                { name: 'Vit D', val: totals.vitD, tgt: targets.vitD, unit: 'mcg' },
                { name: 'Vit B12', val: totals.vitB12, tgt: targets.vitB12, unit: 'mcg' },
            ];

            micros.forEach(m => {
                let pct = Math.min(Math.round((m.val / m.tgt) * 100), 100);
                let div = document.createElement('div');
                div.className = "bg-slate-900/40 border border-slate-800/80 p-3 rounded-xl";
                div.innerHTML = `
                    <div class="flex justify-between text-xs mb-1">
                        <span class="text-slate-400 font-medium">${m.name}</span>
                        <span class="font-bold text-teal-400">${pct}%</span>
                    </div>
                    <div class="w-full bg-slate-800 h-1 rounded-full overflow-hidden">
                        <div class="bg-teal-400 h-full transition-all duration-300" style="width: ${pct}%"></div>
                    </div>
                `;
                microContainer.appendChild(div);
            });
        }

        // Add Log Engine
        document.getElementById('addFoodBtn').addEventListener('click', () => {
            const name = document.getElementById('foodSelect').value;
            const qty = parseFloat(document.getElementById('foodQty').value) || 0;
            const unit = document.getElementById('foodUnit').value;

            if(qty > 0) {
                userLogs.push({ name, qty, unit });
                renderDashboard();
            }
        });

        // Editable Engine: Remove item row
        window.removeLog = function(index) {
            userLogs.splice(index, 1);
            renderDashboard();
        }

        // Sync Profile state shifts seamlessly
        document.querySelectorAll('#profileForm input, #profileForm select').forEach(element => {
            element.addEventListener('change', () => {
                calculateTargets();
                renderDashboard();
            });
        });

        window.onload = init;
    </script>
</body>
</html>
#  AB Talks 60-Days Challenge - Day 9
##  Project: NutriScope Evolution (MVP vs Enhanced)
<img width="396" height="461" alt="image" src="https://github.com/user-attachments/assets/2bb0b7e5-ee18-4707-9a56-47f7a2e4e4aa" />

---
##  Part 1: NutriScope MVP (Minimum Viable Product)
###  Prompt Used:
"Act as an expert frontend web developer. Build a complete single-file HTML application called "NutriScope" (including CSS for professional styling and JavaScript for functionality). The application must include Profile Inputs (Age, Gender, Height, Weight, Activity Level, Dietary Preference), Food Logging Section with Editable Table, 20 Built-in common foods database, and Tracking calculations for 10 key nutrients."
###  MVP Screenshot:
<img width="396" height="461" alt="image" src="https://github.com/user-attachments/assets/e5a4f5f7-37a5-4f0b-a99d-8200f79f7ba4" />

---
##  Part 2: NutriScope Pro (Enhanced Version)
###  Prompt Used:
"Now, enhance this NutriScope application to make it look premium and production-ready with Advanced UI/UX (healthy greens & deep neutrals), Visual Charts (Chart.js integration for macro distribution), Enhanced Target Metrics, and complete mobile responsiveness."
###  Enhanced Screenshot:
<img width="425" height="483" alt="image" src="https://github.com/user-attachments/assets/d527b57c-faf4-4707-9116-8c76f609282a" />

---
##  Comparison Matrix (MVP vs Enhanced)

| Feature / Metric | MVP Version  | Enhanced Pro Version  |
| :--- | :--- | :--- |
| *UI/UX Design* | Basic layout, functional form fields, and minimal look. | Premium Dark Mode with healthy green highlights, clean typography, and cards layout. |
| *Data Visualization* | Raw text logs and numbers inside an editable table. | Interactive *Doughnut Charts (Chart.js)* and animated CSS progress bars. |
| *Dynamic Calculation* | Static calorie/macro tracking based on manual inputs. | Dynamic *Mifflin-St Jeor Engine* that auto-adjusts daily targets instantly on profile shifts. |
| *Dietary Safeguards* | Basic lists without cross-checks. | Direct warning system if logged food conflicts with user's Dietary Preference. |

##  Comparison Matrix (MVP vs Enhanced) Screenshot:
<img width="425" height="417" alt="image" src="https://github.com/user-attachments/assets/f9c8caac-d2fc-4133-ad38-7142658b5f71" />

---
###  Source Code Files Added:
Day9/nutriscope_mvp.html (The core functional prototype)
Day9/nutriscope_enhanced.html (The advanced visual dashboard)
