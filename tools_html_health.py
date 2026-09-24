# tools_html_health.py
# HTML sections for Tools 7-10: Calorie Calculator, BMR Calculator, TDEE Calculator, Pregnancy Due Date Calculator

HEALTH_TOOLS_HTML = {}

MEDICAL_DISCLAIMER_HTML = """
      <!-- Medical & Health Disclaimer -->
      <div class="notice-box" style="margin-bottom: 18px; padding: 14px 16px; background: var(--amber-100, #fef3c7); border-left: 4px solid var(--amber-600, #d97706); font-size: 0.9rem; color: #78350f; border-radius: 8px;">
        <strong>Medical &amp; Health Disclaimer:</strong> Results provided by this calculator are mathematical estimates for general informational and educational purposes only. This tool is not a substitute for professional medical advice, clinical diagnosis, or individualized nutritional treatment. Always consult a qualified physician, obstetrician, or registered dietitian regarding personal health decisions.
      </div>
"""

# 7. CALORIE CALCULATOR
HEALTH_TOOLS_HTML["calorie"] = """
    <!-- ==================== 22. CALORIE CALCULATOR ==================== -->
    <section id="screen-calorie" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Calorie Calculator</h1>
        <p class="tool-page-subtitle">Calculate daily caloric requirements for weight loss, maintenance, or muscle gain with macro breakdowns using the Mifflin-St Jeor formula.</p>
      </div>

      <!-- Medical & Health Disclaimer -->
      <div class="notice-box" style="margin-bottom: 18px; padding: 14px 16px; background: var(--amber-100, #fef3c7); border-left: 4px solid var(--amber-600, #d97706); font-size: 0.9rem; color: #78350f; border-radius: 8px;">
        <strong>Medical &amp; Health Disclaimer:</strong> Results provided by this calculator are mathematical estimates for general informational and educational purposes only. This tool is not a substitute for professional medical advice, clinical diagnosis, or individualized nutritional treatment. Always consult a qualified physician, obstetrician, or registered dietitian regarding personal health decisions.
      </div>

      <div class="card">
        <h2 class="card-title">Physical Profile &amp; Fitness Goal</h2>
        <div class="input-grid-2">
          <div class="input-group">
            <label>Measurement Units</label>
            <div class="segmented-control">
              <button type="button" id="cal-unit-metric" class="segment-btn active" onclick="setCalUnit('metric')">Metric (kg, cm)</button>
              <button type="button" id="cal-unit-imperial" class="segment-btn" onclick="setCalUnit('imperial')">Imperial (lbs, ft/in)</button>
            </div>
          </div>
          <div class="input-group">
            <label>Gender</label>
            <div class="segmented-control">
              <button type="button" id="cal-gender-male" class="segment-btn active" onclick="setCalGender('male')">Male</button>
              <button type="button" id="cal-gender-female" class="segment-btn" onclick="setCalGender('female')">Female</button>
            </div>
          </div>
        </div>

        <div class="input-grid-3">
          <div class="input-group">
            <label for="cal-age">Age (Years)</label>
            <input type="number" id="cal-age" value="28" min="15" max="100" oninput="calculateCalorie()">
          </div>
          <div class="input-group">
            <label for="cal-weight" id="cal-weight-label">Weight (kg)</label>
            <input type="number" id="cal-weight" value="70" min="20" max="300" step="0.5" oninput="calculateCalorie()">
          </div>
          <div class="input-group">
            <label for="cal-height" id="cal-height-label">Height (cm)</label>
            <input type="number" id="cal-height" value="175" min="50" max="250" oninput="calculateCalorie()">
          </div>
        </div>

        <div class="input-grid-2">
          <div class="input-group">
            <label for="cal-activity">Physical Activity Level</label>
            <select id="cal-activity" onchange="calculateCalorie()">
              <option value="1.2">Sedentary (Little or no exercise, desk job)</option>
              <option value="1.375" selected>Lightly Active (Exercise 1-3 days/week)</option>
              <option value="1.55">Moderately Active (Exercise 3-5 days/week)</option>
              <option value="1.725">Very Active (Hard exercise 6-7 days/week)</option>
              <option value="1.9">Extra Active (Intense physical training & job)</option>
            </select>
          </div>
          <div class="input-group">
            <label for="cal-goal">Weight Management Goal</label>
            <select id="cal-goal" onchange="calculateCalorie()">
              <option value="-500">Weight Loss (-0.5 kg / -1 lb per week)</option>
              <option value="-250">Mild Weight Loss (-0.25 kg / -0.5 lb per week)</option>
              <option value="0" selected>Maintain Current Weight</option>
              <option value="250">Mild Weight Gain (+0.25 kg / +0.5 lb per week)</option>
              <option value="500">Muscle Bulking (+0.5 kg / +1 lb per week)</option>
            </select>
          </div>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="calculateCalorie()">Calculate Calories</button>
          <button class="btn btn-outline" onclick="resetCalorie()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="cal-results">
        <div class="stat-header">TARGET DAILY CALORIC INTAKE</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="cal-target-val">2,286</span>
          <span class="highlight-unit">Calories (kcal / day)</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Maintenance (TDEE):</strong> <span id="cal-tdee-val">2,286 kcal</span></div>
          <div class="stat-pill"><strong>Basal Metabolic Rate (BMR):</strong> <span id="cal-bmr-val">1,663 kcal</span></div>
        </div>
        <div class="result-grid-2">
          <div class="metric-box">
            <div class="metric-label">Protein Target (30%)</div>
            <div class="metric-value" id="cal-res-protein">171g / day</div>
            <div class="metric-sub">686 kcal from lean protein sources</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Carbohydrates Target (40%)</div>
            <div class="metric-value" id="cal-res-carbs">229g / day</div>
            <div class="metric-sub">914 kcal from complex carbohydrates</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Healthy Fats Target (30%)</div>
            <div class="metric-value" id="cal-res-fats">76g / day</div>
            <div class="metric-sub">686 kcal from unsaturated fatty acids</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Estimated Weekly Shift</div>
            <div class="metric-value" id="cal-res-weekly-delta">0.0 kg / wk</div>
            <div class="metric-sub">Steady state maintenance</div>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>Complete Guide to Caloric Balance, TDEE, and Macronutrients</h2>
        <p>A calorie is a unit of energy. In human nutrition, energy balance dictates body composition: consuming fewer calories than your body burns creates a negative caloric deficit resulting in weight loss, while consuming more calories creates a surplus resulting in weight gain. Calculating your exact maintenance calories using scientifically validated equations provides a reliable blueprint for achieving your wellness goals sustainably.</p>

        <h3>How to Use This Calorie Calculator</h3>
        <ol>
          <li>Select your preferred units (<strong>Metric: kg/cm</strong> or <strong>Imperial: lbs/inches</strong>).</li>
          <li>Choose your biological sex, age, weight, and height.</li>
          <li>Select your weekly <strong>Physical Activity Level</strong> to account for daily energy expenditure.</li>
          <li>Choose your <strong>Weight Management Goal</strong> (e.g. moderate fat loss of 0.5 kg/week or muscle gain).</li>
          <li>Click <strong>Calculate Calories</strong> to view your daily caloric target along with balanced protein, carbohydrate, and fat macro allocations.</li>
        </ol>

        <h3>The Mifflin-St Jeor Energy Equation</h3>
        <p>Widely regarded by the American Dietetic Association as the most accurate clinical BMR formula:</p>
        <p><code>Men: BMR = (10 × weight in kg) + (6.25 × height in cm) − (5 × age) + 5</code></p>
        <p><code>Women: BMR = (10 × weight in kg) + (6.25 × height in cm) − (5 × age) − 161</code></p>
        <p>Total Daily Energy Expenditure (TDEE) is calculated by multiplying BMR by your physical activity multiplier (1.2 to 1.9). To lose approximately 0.5 kg of body fat per week, a deficit of 500 kcal per day is subtracted from your TDEE (since 1 kg of body fat is roughly 7,700 kcal).</p>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: 28-Year-Old Male Seeking Fat Loss</strong><br>
          Weight: 70 kg | Height: 175 cm | Lightly Active (1.375x).<br>
          BMR = (10×70) + (6.25×175) − (5×28) + 5 = 1,659 kcal.<br>
          TDEE = 1,659 × 1.375 = 2,281 kcal.<br>
          Goal: Weight loss (-500 kcal) → Target = <strong>1,781 kcal/day</strong>.
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: 32-Year-Old Female Seeking Weight Maintenance</strong><br>
          Weight: 58 kg | Height: 162 cm | Moderately Active (1.55x).<br>
          BMR = (10×58) + (6.25×162) − (5×32) − 161 = 1,272 kcal.<br>
          TDEE = 1,272 × 1.55 = <strong>1,972 kcal/day</strong> for steady weight maintenance.
        </div>

        <h3>Tips for Healthy Calorie Management</h3>
        <ul>
          <li><strong>Prioritize lean protein:</strong> Aim for 1.6 to 2.2 grams of protein per kilogram of body weight to preserve lean muscle tissue during a caloric deficit.</li>
          <li><strong>Avoid crash diets:</strong> Restricting intake by more than 750 to 1,000 kcal below maintenance can trigger metabolic slowdown, lethargy, and nutritional deficiencies.</li>
          <li><strong>Track liquid calories:</strong> Sugary soft drinks, fruit juices, and alcohol add substantial calories without promoting satiety.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">What is the safe minimum daily calorie intake?</div>
            <div class="faq-a">Health organizations generally recommend that adult women consume no fewer than 1,200 kcal/day and adult men no fewer than 1,500 kcal/day without direct medical supervision.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Why does weight loss plateau after several weeks?</div>
            <div class="faq-a">As your body weight drops, your BMR and energy cost of movement also decrease. You may need to recalculate your calories every 3-5 kg of lost weight.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Do macronutrient ratios matter if calories are the same?</div>
            <div class="faq-a">While total calories dictate weight change, macronutrients determine body composition (fat vs muscle) and regulate hunger, hormonal health, and athletic performance.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How accurate are activity tracker calorie burns?</div>
            <div class="faq-a">Fitness watches often overestimate exercise calorie burn by 15% to 30%. Using a consistent activity category in this calculator provides a more reliable baseline.</div>
          </div>
        </div>
      </div>

      <!-- Advertisement - Adsterra Banner 320x50 -->
      <div class="ad-banner-wrapper" aria-label="Advertisement">
        <div class="ad-banner-label">Advertisement</div>
        <div class="ad-banner-box">
          <script>
            atOptions = {
              'key' : '19bdb15b0ed7ca7387a9b31c81967da2',
              'format' : 'iframe',
              'height' : 50,
              'width' : 320,
              'params' : {}
            };
          </script>
          <script src="https://www.highrevenueformat.com/19bdb15b0ed7ca7387a9b31c81967da2/invoke.js"></script>
        </div>
      </div>
    </section>
"""

# 8. BMR CALCULATOR
HEALTH_TOOLS_HTML["bmr"] = """
    <!-- ==================== 23. BMR CALCULATOR ==================== -->
    <section id="screen-bmr" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">BMR Calculator</h1>
        <p class="tool-page-subtitle">Calculate your Basal Metabolic Rate—the exact daily calorie expenditure burned by vital organs at complete physical rest.</p>
      </div>

      <!-- Medical & Health Disclaimer -->
      <div class="notice-box" style="margin-bottom: 18px; padding: 14px 16px; background: var(--amber-100, #fef3c7); border-left: 4px solid var(--amber-600, #d97706); font-size: 0.9rem; color: #78350f; border-radius: 8px;">
        <strong>Medical &amp; Health Disclaimer:</strong> Results provided by this calculator are mathematical estimates for general informational and educational purposes only. This tool is not a substitute for professional medical advice, clinical diagnosis, or individualized nutritional treatment. Always consult a qualified physician, obstetrician, or registered dietitian regarding personal health decisions.
      </div>

      <div class="card">
        <h2 class="card-title">Metabolic Parameters</h2>
        <div class="input-grid-2">
          <div class="input-group">
            <label>Measurement System</label>
            <div class="segmented-control">
              <button type="button" id="bmr-unit-metric" class="segment-btn active" onclick="setBmrUnit('metric')">Metric (kg, cm)</button>
              <button type="button" id="bmr-unit-imperial" class="segment-btn" onclick="setBmrUnit('imperial')">Imperial (lbs, ft/in)</button>
            </div>
          </div>
          <div class="input-group">
            <label>Biological Sex</label>
            <div class="segmented-control">
              <button type="button" id="bmr-gender-male" class="segment-btn active" onclick="setBmrGender('male')">Male</button>
              <button type="button" id="bmr-gender-female" class="segment-btn" onclick="setBmrGender('female')">Female</button>
            </div>
          </div>
        </div>

        <div class="input-grid-3">
          <div class="input-group">
            <label for="bmr-age">Age (Years)</label>
            <input type="number" id="bmr-age" value="30" min="15" max="100" oninput="calculateBmr()">
          </div>
          <div class="input-group">
            <label for="bmr-weight" id="bmr-weight-label">Weight (kg)</label>
            <input type="number" id="bmr-weight" value="72" min="20" max="300" step="0.5" oninput="calculateBmr()">
          </div>
          <div class="input-group">
            <label for="bmr-height" id="bmr-height-label">Height (cm)</label>
            <input type="number" id="bmr-height" value="175" min="50" max="250" oninput="calculateBmr()">
          </div>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="calculateBmr()">Calculate BMR</button>
          <button class="btn btn-outline" onclick="resetBmr()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="bmr-results">
        <div class="stat-header">BASAL METABOLIC RATE (RESTING ENERGY)</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="bmr-mifflin-val">1,669</span>
          <span class="highlight-unit">kcal / day</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Hourly Resting Burn:</strong> <span id="bmr-hourly-val">69.5 kcal/hr</span></div>
          <div class="stat-pill"><strong>Harris-Benedict Formula:</strong> <span id="bmr-hb-val">1,701 kcal/day</span></div>
        </div>
        <div class="result-grid-2">
          <div class="metric-box">
            <div class="metric-label">Sedentary (Desk Job, 1.2x)</div>
            <div class="metric-value" id="bmr-res-sed">2,003 kcal</div>
            <div class="metric-sub">BMR × 1.2</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Light Exercise (1-3 days, 1.375x)</div>
            <div class="metric-value" id="bmr-res-light">2,295 kcal</div>
            <div class="metric-sub">BMR × 1.375</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Moderate Exercise (3-5 days, 1.55x)</div>
            <div class="metric-value" id="bmr-res-mod">2,587 kcal</div>
            <div class="metric-sub">BMR × 1.55</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Hard Exercise (6-7 days, 1.725x)</div>
            <div class="metric-value" id="bmr-res-hard">2,879 kcal</div>
            <div class="metric-sub">BMR × 1.725</div>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>What Is Basal Metabolic Rate (BMR) and Why It Matters</h2>
        <p>Your <strong>Basal Metabolic Rate (BMR)</strong> represents the minimum amount of energy (calories) required to maintain vital physiological life functions while your body is at complete physical, digestive, and emotional rest. Even when you are sleeping in a climate-controlled room, your heart beats, lungs respire, brain fires neurons, and cells undergo continuous protein synthesis. BMR typically accounts for <strong>60% to 75%</strong> of your total daily energy expenditure.</p>

        <h3>How to Use This BMR Calculator</h3>
        <ol>
          <li>Select your unit system (<strong>Metric: kg &amp; cm</strong> or <strong>Imperial: lbs &amp; inches</strong>).</li>
          <li>Choose your biological sex, as lean mass differences affect baseline metabolic rates.</li>
          <li>Enter your current age, weight, and standing height.</li>
          <li>Click <strong>Calculate BMR</strong> to obtain both your Mifflin-St Jeor and Revised Harris-Benedict metabolic ratings alongside calorie tiers for various activity levels.</li>
        </ol>

        <h3>The Equations Explained</h3>
        <p><strong>Mifflin-St Jeor Equation (Gold Standard):</strong></p>
        <p><code>BMR (Men) = 10W + 6.25H − 5A + 5</code></p>
        <p><code>BMR (Women) = 10W + 6.25H − 5A − 161</code></p>
        <p><strong>Revised Harris-Benedict Equation:</strong></p>
        <p><code>BMR (Men) = 13.397W + 4.799H − 5.677A + 88.362</code></p>
        <p><code>BMR (Women) = 9.247W + 3.098H − 4.330A + 447.593</code></p>
        <p><em>(W = weight in kg, H = height in cm, A = age in years)</em></p>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: 30-Year-Old Male</strong><br>
          Weight: 72 kg | Height: 175 cm | Age: 30.<br>
          BMR (Mifflin) = (10 × 72) + (6.25 × 175) − (5 × 30) + 5 = 720 + 1,093.75 − 150 + 5 = <strong>1,669 kcal/day</strong>.
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: 25-Year-Old Female</strong><br>
          Weight: 60 kg | Height: 165 cm | Age: 25.<br>
          BMR (Mifflin) = (10 × 60) + (6.25 × 165) − (5 × 25) − 161 = 600 + 1,031.25 − 125 − 161 = <strong>1,345 kcal/day</strong>.
        </div>

        <h3>Factors That Influence Your BMR</h3>
        <ul>
          <li><strong>Lean Muscle Mass:</strong> Muscle tissue burns approximately 3 times more calories at rest per kilogram than adipose fat tissue. Resistance training increases your baseline BMR.</li>
          <li><strong>Age:</strong> Metabolic rate declines by roughly 1-2% per decade after age 30, primarily due to gradual loss of muscle mass (sarcopenia).</li>
          <li><strong>Thyroid Function:</strong> Thyroid hormones (T3 and T4) act as the master thermostat of metabolic rate.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">Should I ever eat fewer calories than my BMR?</div>
            <div class="faq-a">Eating below your BMR is generally not advised unless supervised by a physician. Consuming fewer calories than your resting organs need can prompt metabolic adaptation, muscle wasting, and hormone dysregulation.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How does BMR differ from RMR?</div>
            <div class="faq-a">BMR requires measurement after a strict 12-hour fast in a specialized thermal chamber. Resting Metabolic Rate (RMR) is measured under less restrictive resting conditions and is typically 5-10% higher than BMR.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can drinking cold water boost my BMR?</div>
            <div class="faq-a">Drinking cold water requires your body to expend a negligible number of calories to warm the water to body temperature, but the effect is too small (approx. 8 kcal per glass) to meaningfully alter daily BMR.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Does fasting slow down BMR?</div>
            <div class="faq-a">Short-term intermittent fasting (16-24 hours) does not reduce BMR. Prolonged severe starvation or chronic extreme caloric restriction over multiple weeks, however, triggers adaptive thermogenesis.</div>
          </div>
        </div>
      </div>

      <!-- Advertisement - Adsterra Banner 320x50 -->
      <div class="ad-banner-wrapper" aria-label="Advertisement">
        <div class="ad-banner-label">Advertisement</div>
        <div class="ad-banner-box">
          <script>
            atOptions = {
              'key' : '19bdb15b0ed7ca7387a9b31c81967da2',
              'format' : 'iframe',
              'height' : 50,
              'width' : 320,
              'params' : {}
            };
          </script>
          <script src="https://www.highrevenueformat.com/19bdb15b0ed7ca7387a9b31c81967da2/invoke.js"></script>
        </div>
      </div>
    </section>
"""

# 9. TDEE CALCULATOR
HEALTH_TOOLS_HTML["tdee"] = """
    <!-- ==================== 24. TDEE CALCULATOR ==================== -->
    <section id="screen-tdee" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">TDEE Calculator</h1>
        <p class="tool-page-subtitle">Calculate Total Daily Energy Expenditure factoring in basal metabolism, physical activity levels, and daily exercise energy burn.</p>
      </div>

      <!-- Medical & Health Disclaimer -->
      <div class="notice-box" style="margin-bottom: 18px; padding: 14px 16px; background: var(--amber-100, #fef3c7); border-left: 4px solid var(--amber-600, #d97706); font-size: 0.9rem; color: #78350f; border-radius: 8px;">
        <strong>Medical &amp; Health Disclaimer:</strong> Results provided by this calculator are mathematical estimates for general informational and educational purposes only. This tool is not a substitute for professional medical advice, clinical diagnosis, or individualized nutritional treatment. Always consult a qualified physician, obstetrician, or registered dietitian regarding personal health decisions.
      </div>

      <div class="card">
        <h2 class="card-title">Activity &amp; Metabolic Profile</h2>
        <div class="input-grid-2">
          <div class="input-group">
            <label>Measurement Units</label>
            <div class="segmented-control">
              <button type="button" id="tdee-unit-metric" class="segment-btn active" onclick="setTdeeUnit('metric')">Metric (kg, cm)</button>
              <button type="button" id="tdee-unit-imperial" class="segment-btn" onclick="setTdeeUnit('imperial')">Imperial (lbs, ft/in)</button>
            </div>
          </div>
          <div class="input-group">
            <label>Biological Sex</label>
            <div class="segmented-control">
              <button type="button" id="tdee-gender-male" class="segment-btn active" onclick="setTdeeGender('male')">Male</button>
              <button type="button" id="tdee-gender-female" class="segment-btn" onclick="setTdeeGender('female')">Female</button>
            </div>
          </div>
        </div>

        <div class="input-grid-3">
          <div class="input-group">
            <label for="tdee-age">Age (Years)</label>
            <input type="number" id="tdee-age" value="26" min="15" max="100" oninput="calculateTdee()">
          </div>
          <div class="input-group">
            <label for="tdee-weight" id="tdee-weight-label">Weight (kg)</label>
            <input type="number" id="tdee-weight" value="68" min="20" max="300" step="0.5" oninput="calculateTdee()">
          </div>
          <div class="input-group">
            <label for="tdee-height" id="tdee-height-label">Height (cm)</label>
            <input type="number" id="tdee-height" value="172" min="50" max="250" oninput="calculateTdee()">
          </div>
        </div>

        <div class="input-group">
          <label for="tdee-activity">Physical Activity Profile</label>
          <select id="tdee-activity" onchange="calculateTdee()">
            <option value="1.2">Sedentary: Desk job, little to no deliberate exercise</option>
            <option value="1.375">Light Exercise: Walking, light workouts 1-2 days/week</option>
            <option value="1.55" selected>Moderate Exercise: Gym or cardio 3-5 days/week</option>
            <option value="1.725">Heavy Exercise: Dedicated training 6-7 days/week</option>
            <option value="1.9">Athlete / Manual Labor: Double daily sessions or intense physical work</option>
          </select>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="calculateTdee()">Calculate TDEE</button>
          <button class="btn btn-outline" onclick="resetTdee()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="tdee-results">
        <div class="stat-header">TOTAL DAILY ENERGY EXPENDITURE (MAINTENANCE)</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="tdee-main-val">2,527</span>
          <span class="highlight-unit">kcal / day</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Weekly Energy Burn:</strong> <span id="tdee-weekly-val">17,689 kcal/week</span></div>
          <div class="stat-pill"><strong>Base Metabolic Rate (BMR):</strong> <span id="tdee-bmr-val">1,630 kcal</span></div>
        </div>
        <div class="result-grid-2">
          <div class="metric-box">
            <div class="metric-label">Weight Loss (Cutting: -500 kcal)</div>
            <div class="metric-value" id="tdee-res-cut">2,027 kcal</div>
            <div class="metric-sub">Loses approx 0.45 kg (1 lb) per week</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Moderate Loss (-250 kcal)</div>
            <div class="metric-value" id="tdee-res-mild-cut">2,277 kcal</div>
            <div class="metric-sub">Gentle deficit, easily sustainable</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Lean Muscle Bulk (+300 kcal)</div>
            <div class="metric-value" id="tdee-res-bulk">2,827 kcal</div>
            <div class="metric-sub">Clean hypertrophy with minimal fat gain</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Active Calorie Burn Component</div>
            <div class="metric-value" id="tdee-res-active-burn">897 kcal/day</div>
            <div class="metric-sub">NEAT + Exercise + TEF above BMR</div>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>Mastering Your Total Daily Energy Expenditure (TDEE)</h2>
        <p>While BMR tells you what you burn while resting, <strong>Total Daily Energy Expenditure (TDEE)</strong> tells you the true total number of calories you burn across an entire 24-hour day of living, working, digesting, and exercising. Knowing your exact TDEE removes the guesswork from bodybuilding cutting phases, endurance prep, and sustainable weight management.</p>

        <h3>How to Use This TDEE Calculator</h3>
        <ol>
          <li>Choose your measurement units (<strong>Metric</strong> or <strong>Imperial</strong>).</li>
          <li>Enter your age, sex, weight, and height.</li>
          <li>Select the <strong>Physical Activity Profile</strong> that best matches your typical weekly routine.</li>
          <li>Click <strong>Calculate TDEE</strong> to see your daily maintenance calorie target and tailored thresholds for cutting, maintenance, and lean bulking.</li>
        </ol>

        <h3>The 4 Pillars of Daily Calorie Burn</h3>
        <ul>
          <li><strong>Basal Metabolic Rate (BMR ~60-70%):</strong> Energy burned by internal organs at complete rest.</li>
          <li><strong>Non-Exercise Activity Thermogenesis (NEAT ~15%):</strong> Unplanned movement: walking to work, fidgeting, carrying groceries, climbing stairs.</li>
          <li><strong>Thermic Effect of Food (TEF ~10%):</strong> Energy used to digest and process proteins, carbohydrates, and fats.</li>
          <li><strong>Exercise Activity Thermogenesis (EAT ~5-15%):</strong> Planned physical workouts, sports, weightlifting, and cardio sessions.</li>
        </ul>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: Moderately Active Male</strong><br>
          Age: 26 | Weight: 68 kg | Height: 172 cm | Moderately Active (1.55x).<br>
          BMR = (10×68) + (6.25×172) − (5×26) + 5 = 680 + 1,075 − 130 + 5 = 1,630 kcal.<br>
          TDEE = 1,630 × 1.55 = <strong>2,527 kcal/day</strong>.<br>
          Cutting target = 2,527 − 500 = <strong>2,027 kcal/day</strong>.
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: Sedentary Desk Worker</strong><br>
          Age: 35 | Weight: 85 kg | Height: 180 cm | Sedentary (1.2x).<br>
          BMR = 1,805 kcal. TDEE = 1,805 × 1.2 = <strong>2,166 kcal/day</strong>.
        </div>

        <h3>Tips for Elevating Your TDEE</h3>
        <ul>
          <li><strong>Boost your NEAT:</strong> Take telephone calls while pacing, use a standing desk, or aim for 8,000-10,000 steps daily. NEAT often burns more calories than a 45-minute gym session.</li>
          <li><strong>Increase dietary protein:</strong> Protein has a high thermic effect (20-30% of its calories are burned during digestion, compared to only 5-10% for carbs and 0-3% for fats).</li>
          <li><strong>Build muscle mass:</strong> Increasing functional lean mass permanently raises baseline daily caloric demands.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">How does TDEE differ from BMR?</div>
            <div class="faq-a">BMR is the calories burned doing nothing in bed. TDEE is BMR plus the extra calories burned by eating, standing, walking, working, and working out.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">What should I do if my weight does not change after 2 weeks at target TDEE?</div>
            <div class="faq-a">TDEE formulas provide mathematical estimates. If your weight is stable over 14 days, your actual intake is your true maintenance level. Adjust by 150-200 kcal up or down to continue progress.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Does TDEE fluctuate daily?</div>
            <div class="faq-a">Yes. Days with intense training or long walks burn significantly more calories than rest days spent sitting. Many athletes cycle calories between training days and rest days.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can drinking coffee increase TDEE?</div>
            <div class="faq-a">Caffeine provides a mild temporary thermogenic boost of roughly 3-11% for 1-2 hours, but this does not replace consistent dietary habit adherence.</div>
          </div>
        </div>
      </div>

      <!-- Advertisement - Adsterra Banner 320x50 -->
      <div class="ad-banner-wrapper" aria-label="Advertisement">
        <div class="ad-banner-label">Advertisement</div>
        <div class="ad-banner-box">
          <script>
            atOptions = {
              'key' : '19bdb15b0ed7ca7387a9b31c81967da2',
              'format' : 'iframe',
              'height' : 50,
              'width' : 320,
              'params' : {}
            };
          </script>
          <script src="https://www.highrevenueformat.com/19bdb15b0ed7ca7387a9b31c81967da2/invoke.js"></script>
        </div>
      </div>
    </section>
"""

# 10. PREGNANCY DUE DATE CALCULATOR
HEALTH_TOOLS_HTML["pregnancy-due-date"] = """
    <!-- ==================== 25. PREGNANCY DUE DATE CALCULATOR ==================== -->
    <section id="screen-pregnancy-due-date" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Pregnancy Due Date Calculator</h1>
        <p class="tool-page-subtitle">Estimate your baby's delivery due date (EDD), gestational age in weeks &amp; days, current trimester, and key developmental milestones.</p>
      </div>

      <!-- Medical & Health Disclaimer -->
      <div class="notice-box" style="margin-bottom: 18px; padding: 14px 16px; background: var(--amber-100, #fef3c7); border-left: 4px solid var(--amber-600, #d97706); font-size: 0.9rem; color: #78350f; border-radius: 8px;">
        <strong>Medical &amp; Health Disclaimer:</strong> Results provided by this calculator are mathematical estimates for general informational and educational purposes only. This tool is not a substitute for professional medical advice, clinical diagnosis, or individualized nutritional treatment. Always consult a qualified physician, obstetrician, or registered dietitian regarding personal health decisions.
      </div>

      <div class="card">
        <h2 class="card-title">Pregnancy Timing Method</h2>
        <div class="input-grid-2">
          <div class="input-group">
            <label for="pdd-method">Calculation Method</label>
            <select id="pdd-method" onchange="calculatePregnancyDueDate()">
              <option value="lmp" selected>First Day of Last Menstrual Period (LMP)</option>
              <option value="conception">Exact Conception Date</option>
              <option value="ivf3">IVF 3-Day Embryo Transfer</option>
              <option value="ivf5">IVF 5-Day Blastocyst Transfer</option>
            </select>
          </div>
          <div class="input-group">
            <label for="pdd-date" id="pdd-date-label">First Day of Last Period</label>
            <input type="date" id="pdd-date" onchange="calculatePregnancyDueDate()">
          </div>
        </div>

        <div class="input-group" id="pdd-cycle-group">
          <label for="pdd-cycle">Average Menstrual Cycle Length (Days)</label>
          <input type="number" id="pdd-cycle" value="28" min="20" max="45" oninput="calculatePregnancyDueDate()">
          <span style="font-size: 0.78rem; color: var(--text-muted);">Standard cycle is 28 days. Adjust if your typical cycle is shorter or longer.</span>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="calculatePregnancyDueDate()">Calculate Due Date</button>
          <button class="btn btn-outline" onclick="resetPregnancyDueDate()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="pdd-results">
        <div class="stat-header">ESTIMATED DUE DATE (EDD)</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="pdd-due-date-val">October 28, 2026</span>
          <span class="highlight-unit" id="pdd-countdown-val">180 Days Remaining</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Gestational Age:</strong> <span id="pdd-gest-age-val">14 Weeks, 2 Days</span></div>
          <div class="stat-pill"><strong>Current Stage:</strong> <span id="pdd-trimester-val">Second Trimester (Week 14)</span></div>
        </div>
        <div class="result-grid-2">
          <div class="metric-box">
            <div class="metric-label">Estimated Conception Window</div>
            <div class="metric-value" id="pdd-res-conception">Feb 04, 2026</div>
            <div class="metric-sub">Ovulation &amp; fertilization period</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">End of First Trimester</div>
            <div class="metric-value" id="pdd-res-tri1-end">Apr 22, 2026</div>
            <div class="metric-sub">Completion of Week 13</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Viability Milestone (Week 24)</div>
            <div class="metric-value" id="pdd-res-viability">Jul 08, 2026</div>
            <div class="metric-sub">Critical fetal survival threshold</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Full Term Milestone (Week 37)</div>
            <div class="metric-value" id="pdd-res-fullterm">Oct 07, 2026</div>
            <div class="metric-sub">Fully developed, ready for delivery</div>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>How Pregnancy Due Dates and Gestational Age Are Calculated</h2>
        <p>A full-term human pregnancy lasts an average of <strong>280 days (40 weeks)</strong> counted from the first day of the mother's last menstrual period (LMP). Because the exact moment of fertilization is rarely known with certainty, obstetricians worldwide rely on <strong>Naegele's rule</strong> to establish the initial Estimated Due Date (EDD). Your due date serves as a vital clinical guidepost for scheduling developmental prenatal ultrasounds, maternal blood screenings, and labor preparations.</p>

        <h3>How to Use This Pregnancy Due Date Calculator</h3>
        <ol>
          <li>Select your known pregnancy landmark: <strong>Last Menstrual Period (LMP)</strong>, <strong>Conception Date</strong>, or <strong>IVF Embryo Transfer Date</strong>.</li>
          <li>Pick the relevant date on the calendar.</li>
          <li>If using LMP, enter your typical <strong>menstrual cycle length</strong> (default is 28 days).</li>
          <li>Click <strong>Calculate Due Date</strong> to see your Estimated Delivery Date (EDD), current gestational age in weeks and days, and critical trimester milestones.</li>
        </ol>

        <h3>The Medical Formula: Naegele's Rule</h3>
        <p>For a standard 28-day cycle, Naegele's rule calculates the EDD as:</p>
        <p><code>Due Date = First Day of LMP + 1 Year − 3 Months + 7 Days</code></p>
        <p><em>Cycle Adjustment:</em> If your cycle is <em>C</em> days (where <em>C ≠ 28</em>), add <code>(C − 28)</code> days to the result. For example, in a 32-day cycle, ovulation occurs roughly 4 days later, so 4 days are added to the estimated due date.</p>

        <h3>The Three Pregnancy Trimesters</h3>
        <ul>
          <li><strong>First Trimester (Weeks 1 to 13):</strong> Major organogenesis, heartbeat detection, rapid cellular differentiation, and initial dating scan (nuchal translucency).</li>
          <li><strong>Second Trimester (Weeks 14 to 27):</strong> "The golden trimester": fetal movements ("quickening") begin, anatomy ultrasound (anomaly scan) at weeks 18-20, and viability reached at week 24.</li>
          <li><strong>Third Trimester (Weeks 28 to 40+):</strong> Rapid fetal weight gain, lung maturation, descent into the pelvis, and preparation for labor. Full term is achieved at 37 weeks.</li>
        </ul>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: Standard 28-Day Cycle</strong><br>
          LMP Date: January 15, 2026 | Cycle Length: 28 Days.<br>
          Calculation: Jan 15 + 1 Year = Jan 15, 2027. Subtract 3 months = Oct 15, 2026. Add 7 days = <strong>October 22, 2026</strong>.
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: IVF 5-Day Blastocyst Transfer</strong><br>
          Transfer Date: March 10, 2026.<br>
          Because a 5-day embryo is already at day 19 of a cycle (14 days to ovulation + 5 days), EDD = March 10 + 261 days = <strong>November 26, 2026</strong>.
        </div>

        <h3>Tips for Expecting Parents</h3>
        <ul>
          <li><strong>Only 4% of babies arrive on their exact due date:</strong> Approximately 90% of healthy infants are born within a two-week window either side of their EDD (between 38 and 42 weeks).</li>
          <li><strong>First trimester ultrasound is most accurate:</strong> A crown-rump length (CRL) ultrasound scan performed between weeks 8 and 13 has an error margin of only ±5 days and is considered the clinical gold standard.</li>
          <li><strong>Start folic acid early:</strong> Taking 400 mcg of folic acid daily reduces neural tube defect risks significantly.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">Can my doctor change my due date after an ultrasound?</div>
            <div class="faq-a">Yes. If an early first-trimester dating ultrasound scan differs from your LMP calculation by more than 5 to 7 days, your obstetrician will adjust your official clinical due date to match the ultrasound measurements.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Why am I considered 2 weeks pregnant at conception?</div>
            <div class="faq-a">Gestational age is dated from the first day of your last period, approximately 14 days before ovulation and fertilization actually occur. Therefore, you are already "2 weeks pregnant" on the day conception takes place.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">What constitutes a "full-term" pregnancy?</div>
            <div class="faq-a">According to the American College of Obstetricians and Gynecologists (ACOG), early term is 37 weeks 0 days through 38 weeks 6 days; full term is 39 weeks 0 days through 40 weeks 6 days.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">What if my menstrual cycles are irregular?</div>
            <div class="faq-a">If your cycles are irregular or unpredictable, calculating by LMP can be inaccurate. In such cases, an early dating ultrasound is required to establish gestational age.</div>
          </div>
        </div>
      </div>

      <!-- Advertisement - Adsterra Banner 320x50 -->
      <div class="ad-banner-wrapper" aria-label="Advertisement">
        <div class="ad-banner-label">Advertisement</div>
        <div class="ad-banner-box">
          <script>
            atOptions = {
              'key' : '19bdb15b0ed7ca7387a9b31c81967da2',
              'format' : 'iframe',
              'height' : 50,
              'width' : 320,
              'params' : {}
            };
          </script>
          <script src="https://www.highrevenueformat.com/19bdb15b0ed7ca7387a9b31c81967da2/invoke.js"></script>
        </div>
      </div>
    </section>
"""

print("tools_html_health.py created successfully with Tools 7-10.")
