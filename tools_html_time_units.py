# tools_html_time_units.py
# HTML sections for Tools 11-17: Hours to Minutes, Minutes to Hours, Length, Weight, Temperature, Area, Volume

TIME_UNITS_TOOLS_HTML = {}

# 11. HOURS TO MINUTES CONVERTER
TIME_UNITS_TOOLS_HTML["hours-to-minutes"] = """
    <!-- ==================== 26. HOURS TO MINUTES CONVERTER ==================== -->
    <section id="screen-hours-to-minutes" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Hours to Minutes Converter</h1>
        <p class="tool-page-subtitle">Convert decimal hours or combined hours and minutes into total minutes, seconds, milliseconds, and decimal workday ratios.</p>
      </div>

      <div class="card">
        <h2 class="card-title">Time Input</h2>
        <div class="input-group" style="margin-bottom: 12px;">
          <label>Input Mode</label>
          <div class="segmented-control">
            <button type="button" id="h2m-mode-dec" class="segment-btn active" onclick="setH2mMode('dec')">Decimal Hours (e.g. 2.75 hrs)</button>
            <button type="button" id="h2m-mode-split" class="segment-btn" onclick="setH2mMode('split')">Hours &amp; Minutes (e.g. 2h 45m)</button>
          </div>
        </div>

        <div id="h2m-dec-container">
          <div class="input-group">
            <label for="h2m-dec-input">Hours (Decimal)</label>
            <input type="number" id="h2m-dec-input" value="2.5" min="0" step="0.25" oninput="convertHoursToMinutes()">
          </div>
        </div>

        <div id="h2m-split-container" style="display: none;">
          <div class="input-grid-2">
            <div class="input-group">
              <label for="h2m-hours-part">Hours</label>
              <input type="number" id="h2m-hours-part" value="2" min="0" step="1" oninput="convertHoursToMinutes()">
            </div>
            <div class="input-group">
              <label for="h2m-mins-part">Minutes</label>
              <input type="number" id="h2m-mins-part" value="30" min="0" max="59" step="1" oninput="convertHoursToMinutes()">
            </div>
          </div>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="convertHoursToMinutes()">Convert to Minutes</button>
          <button class="btn btn-outline" onclick="resetHoursToMinutes()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="h2m-results">
        <div class="stat-header">TOTAL MINUTES CONVERTED</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="h2m-total-mins-val">150</span>
          <span class="highlight-unit">Minutes</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Time Expression:</strong> <span id="h2m-express-val">2 Hours and 30 Minutes</span></div>
          <div class="stat-pill"><strong>Formula:</strong> <span id="h2m-formula-val">2.5 hrs × 60 min/hr</span></div>
        </div>
        <div class="result-grid-2">
          <div class="metric-box">
            <div class="metric-label">Total Seconds</div>
            <div class="metric-value" id="h2m-res-seconds">9,000 sec</div>
            <div class="metric-sub">Minutes × 60</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Total Milliseconds</div>
            <div class="metric-value" id="h2m-res-ms">9,000,000 ms</div>
            <div class="metric-sub">Standard computational time</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Portion of 24-Hour Day</div>
            <div class="metric-value" id="h2m-res-day-pct">10.42%</div>
            <div class="metric-sub">0.1042 calendar days</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Portion of 8-Hour Workday</div>
            <div class="metric-value" id="h2m-res-work-pct">31.25%</div>
            <div class="metric-sub">Standard shift percentage</div>
          </div>
        </div>

        <!-- Quick Reference Table -->
        <div style="margin-top: 16px;">
          <div class="stat-header">COMMON DECIMAL HOURS LOOKUP TABLE</div>
          <div class="data-table-wrapper" style="overflow-x: auto;">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Decimal Hours</th>
                  <th>Hours &amp; Minutes</th>
                  <th>Total Minutes</th>
                  <th>Workday (8h) %</th>
                </tr>
              </thead>
              <tbody>
                <tr><td>0.25 hr (1/4 hr)</td><td>0 hr 15 min</td><td>15 min</td><td>3.13%</td></tr>
                <tr><td>0.50 hr (1/2 hr)</td><td>0 hr 30 min</td><td>30 min</td><td>6.25%</td></tr>
                <tr><td>0.75 hr (3/4 hr)</td><td>0 hr 45 min</td><td>45 min</td><td>9.38%</td></tr>
                <tr><td>1.00 hr</td><td>1 hr 00 min</td><td>60 min</td><td>12.50%</td></tr>
                <tr><td>1.50 hr</td><td>1 hr 30 min</td><td>90 min</td><td>18.75%</td></tr>
                <tr><td>2.50 hr</td><td>2 hr 30 min</td><td>150 min</td><td>31.25%</td></tr>
                <tr><td>7.50 hr</td><td>7 hr 30 min</td><td>450 min</td><td>93.75%</td></tr>
                <tr><td>8.00 hr</td><td>8 hr 00 min</td><td>480 min</td><td>100.00%</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>Converting Decimal Hours to Total Minutes for Payroll and Billing</h2>
        <p>In modern corporate payroll systems, legal timesheets, and contractor billing, time is almost universally logged in <strong>decimal hours</strong> (such as 7.75 hours) rather than standard clock format (7 hours and 45 minutes). Misinterpreting decimal fractions of an hour as clock minutes is one of the most common administrative accounting errors. Multiplying decimal hours by 60 provides the exact number of minutes.</p>

        <h3>How to Use This Hours to Minutes Converter</h3>
        <ol>
          <li>Choose your input format: <strong>Decimal Hours</strong> (e.g. 3.75) or <strong>Hours &amp; Minutes</strong> (e.g. 3h 45m).</li>
          <li>Enter your value into the input field.</li>
          <li>Click <strong>Convert to Minutes</strong> to view total minutes, seconds, milliseconds, and standard workday ratios.</li>
        </ol>

        <h3>The Conversion Formula</h3>
        <p><code>Total Minutes = Decimal Hours × 60</code></p>
        <p>If starting from combined hours and minutes:</p>
        <p><code>Total Minutes = (Hours × 60) + Minutes</code></p>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: Freelance Timesheet Entry</strong><br>
          A contractor logs 6.4 hours on an invoicing portal.<br>
          Calculation: 6.4 × 60 = <strong>384 Total Minutes</strong> (6 Hours and 24 Minutes). Note: 0.4 hours is 24 minutes, NOT 40 minutes!
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: Exam Duration</strong><br>
          A university entrance examination is scheduled for 2.75 hours.<br>
          Calculation: 2.75 × 60 = <strong>165 Minutes</strong> (2 Hours and 45 Minutes).
        </div>

        <h3>Tips for Accurate Time Billing</h3>
        <ul>
          <li><strong>Remember the base 60 rule:</strong> 0.1 hours is 6 minutes, 0.2 is 12 minutes, 0.3 is 18 minutes, and 0.5 is 30 minutes.</li>
          <li><strong>Round to 15-minute increments:</strong> Many payroll and legal invoicing systems round to 0.25 (15 mins) or 0.1 (6 mins) billing blocks.</li>
          <li><strong>Cross-verify elapsed clock times:</strong> Always verify that time intervals between start and end match decimal tallies.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">Why does 0.5 hours equal 30 minutes instead of 50 minutes?</div>
            <div class="faq-a">Time uses the sexagesimal (base-60) system where one full hour contains 60 minutes. Therefore, half of an hour is 0.5 × 60 = 30 minutes.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How do I convert 45 minutes into decimal hours?</div>
            <div class="faq-a">Divide 45 by 60: 45 / 60 = 0.75 hours.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How many minutes are in an 8-hour workday?</div>
            <div class="faq-a">An 8-hour shift contains exactly 8 × 60 = 480 minutes. A 40-hour workweek equals 2,400 minutes.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can this tool handle fractional minutes?</div>
            <div class="faq-a">Yes. If you input decimal hours such as 1.33 hours, it accurately computes 79.8 minutes and shows the breakdown in seconds.</div>
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

# 12. MINUTES TO HOURS CONVERTER
TIME_UNITS_TOOLS_HTML["minutes-to-hours"] = """
    <!-- ==================== 27. MINUTES TO HOURS CONVERTER ==================== -->
    <section id="screen-minutes-to-hours" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Minutes to Hours Converter</h1>
        <p class="tool-page-subtitle">Convert elapsed minutes into decimal hours, clock time (HH:MM:SS), and workday progress percentages.</p>
      </div>

      <div class="card">
        <h2 class="card-title">Minutes Input</h2>
        <div class="input-group">
          <label for="m2h-input">Total Minutes to Convert</label>
          <input type="number" id="m2h-input" value="175" min="0" step="1" oninput="convertMinutesToHours()">
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="convertMinutesToHours()">Convert to Hours</button>
          <button class="btn btn-outline" onclick="resetMinutesToHours()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="m2h-results">
        <div class="stat-header">CONVERTED HOURS (DECIMAL)</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="m2h-dec-val">2.9167</span>
          <span class="highlight-unit">Hours</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Clock Format:</strong> <span id="m2h-clock-val">2 Hours, 55 Minutes</span></div>
          <div class="stat-pill"><strong>Digital Notation:</strong> <span id="m2h-digital-val">02:55:00</span></div>
        </div>
        <div class="result-grid-2">
          <div class="metric-box">
            <div class="metric-label">Whole Hours Component</div>
            <div class="metric-value" id="m2h-res-hours">2 hrs</div>
            <div class="metric-sub">Floor integer division (÷ 60)</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Remainder Minutes</div>
            <div class="metric-value" id="m2h-res-rem-mins">55 mins</div>
            <div class="metric-sub">Modulo remainder (175 mod 60)</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Portion of 8-Hour Work Shift</div>
            <div class="metric-value" id="m2h-res-shift-pct">36.46%</div>
            <div class="metric-sub">Out of 480 standard shift minutes</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Total Seconds Equivalent</div>
            <div class="metric-value" id="m2h-res-secs">10,500 sec</div>
            <div class="metric-sub">Minutes × 60</div>
          </div>
        </div>

        <!-- Lookup Table -->
        <div style="margin-top: 16px;">
          <div class="stat-header">MINUTES TO DECIMAL HOURS CHEAT SHEET</div>
          <div class="data-table-wrapper" style="overflow-x: auto;">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Minutes</th>
                  <th>Clock Time</th>
                  <th>Decimal Hours</th>
                  <th>Shift (8h) %</th>
                </tr>
              </thead>
              <tbody>
                <tr><td>15 min</td><td>0h 15m</td><td>0.250 hr</td><td>3.13%</td></tr>
                <tr><td>30 min</td><td>0h 30m</td><td>0.500 hr</td><td>6.25%</td></tr>
                <tr><td>45 min</td><td>0h 45m</td><td>0.750 hr</td><td>9.38%</td></tr>
                <tr><td>60 min</td><td>1h 00m</td><td>1.000 hr</td><td>12.50%</td></tr>
                <tr><td>90 min</td><td>1h 30m</td><td>1.500 hr</td><td>18.75%</td></tr>
                <tr><td>120 min</td><td>2h 00m</td><td>2.000 hr</td><td>25.00%</td></tr>
                <tr><td>180 min</td><td>3h 00m</td><td>3.000 hr</td><td>37.50%</td></tr>
                <tr><td>240 min</td><td>4h 00m</td><td>4.000 hr</td><td>50.00%</td></tr>
                <tr><td>480 min</td><td>8h 00m</td><td>8.000 hr</td><td>100.00%</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>How to Convert Total Minutes into Decimal and Clock Hours</h2>
        <p>Converting elapsed minutes into decimal hours is a fundamental daily calculation across workforce management, sports performance analytics, aviation flight logs, and equipment rental billing. Because computers and spreadsheets operate in decimal arithmetic (base-10), while clocks operate in minutes and seconds (base-60), having an instant, exact converter eliminates costly rounding errors.</p>

        <h3>How to Use This Minutes to Hours Converter</h3>
        <ol>
          <li>Type the number of <strong>Total Minutes</strong> you wish to convert into the input box.</li>
          <li>Click <strong>Convert to Hours</strong>.</li>
          <li>Review the four-decimal precision hour value, clock time (hours and minutes), and percentage of a standard 8-hour workday.</li>
        </ol>

        <h3>Formulas for Conversion</h3>
        <p><strong>Decimal Hours:</strong></p>
        <p><code>Decimal Hours = Total Minutes / 60</code></p>
        <p><strong>Clock Format (Hours and Minutes):</strong></p>
        <p><code>Hours = Math.floor(Total Minutes / 60)</code></p>
        <p><code>Remaining Minutes = Total Minutes % 60</code></p>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: Audio/Podcast Transcription Time</strong><br>
          An audio file has a duration of 145 minutes.<br>
          Decimal Hours: 145 / 60 = <strong>2.4167 hours</strong>.<br>
          Clock Format: 145 = 2 whole hours (120 mins) + 25 remainder minutes = <strong>2 Hours and 25 Minutes (02:25:00)</strong>.
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: Daily Flight Log</strong><br>
          A pilot logs 330 flight minutes.<br>
          Decimal: 330 / 60 = <strong>5.5000 hours</strong> (5 Hours and 30 Minutes).
        </div>

        <h3>Useful Tips for Payroll Tracking</h3>
        <ul>
          <li><strong>Never write 15 minutes as .15:</strong> 15 minutes is 15/60 = 0.25 hours. Entering .15 shortchanges workers by 6 minutes per entry.</li>
          <li><strong>Common tenth-of-an-hour increments:</strong> 6 mins = 0.1h, 12 mins = 0.2h, 18 mins = 0.3h, 24 mins = 0.4h, 30 mins = 0.5h.</li>
          <li><strong>Use the lookup table for quick audits:</strong> Compare batch employee timesheet totals against our lookup table to verify software payroll exports.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">What is 100 minutes in hours?</div>
            <div class="faq-a">100 minutes divided by 60 equals 1.6667 decimal hours, which translates to 1 hour and 40 minutes (01:40:00).</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How many hours is 1,000 minutes?</div>
            <div class="faq-a">1,000 minutes is 16.6667 hours, or 16 hours and 40 minutes.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How do I enter this into an Excel spreadsheet?</div>
            <div class="faq-a">If cell A1 contains 175 minutes, enter <code>=A1/60</code> to obtain 2.9167 decimal hours, or <code>=TIME(0, A1, 0)</code> formatted as <code>[h]:mm</code> for clock time.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can this calculator process negative minutes?</div>
            <div class="faq-a">Negative values are automatically bounded to 0 because elapsed physical time is non-negative.</div>
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

# 13. LENGTH CONVERTER
TIME_UNITS_TOOLS_HTML["length-converter"] = """
    <!-- ==================== 28. LENGTH CONVERTER ==================== -->
    <section id="screen-length-converter" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Length Converter</h1>
        <p class="tool-page-subtitle">Convert length and distance between millimeters, centimeters, meters, kilometers, inches, feet, yards, miles, and nautical miles.</p>
      </div>

      <div class="card">
        <h2 class="card-title">Length &amp; Distance Conversion</h2>
        <div class="input-grid-3">
          <div class="input-group">
            <label for="len-val">Value to Convert</label>
            <input type="number" id="len-val" value="10" min="0" step="any" oninput="convertLength()">
          </div>
          <div class="input-group">
            <label for="len-from">From Unit</label>
            <select id="len-from" onchange="convertLength()">
              <option value="mm">Millimeters (mm)</option>
              <option value="cm">Centimeters (cm)</option>
              <option value="m" selected>Meters (m)</option>
              <option value="km">Kilometers (km)</option>
              <option value="in">Inches (in)</option>
              <option value="ft">Feet (ft)</option>
              <option value="yd">Yards (yd)</option>
              <option value="mi">Miles (mi)</option>
              <option value="nmi">Nautical Miles (NM)</option>
            </select>
          </div>
          <div class="input-group">
            <label for="len-to">To Unit</label>
            <select id="len-to" onchange="convertLength()">
              <option value="mm">Millimeters (mm)</option>
              <option value="cm">Centimeters (cm)</option>
              <option value="m">Meters (m)</option>
              <option value="km">Kilometers (km)</option>
              <option value="in">Inches (in)</option>
              <option value="ft" selected>Feet (ft)</option>
              <option value="yd">Yards (yd)</option>
              <option value="mi">Miles (mi)</option>
              <option value="nmi">Nautical Miles (NM)</option>
            </select>
          </div>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="convertLength()">Convert Length</button>
          <button class="btn btn-secondary" onclick="swapLengthUnits()">⇄ Swap Units</button>
          <button class="btn btn-outline" onclick="resetLength()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="len-results">
        <div class="stat-header">CONVERTED RESULT</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="len-result-val">32.8084</span>
          <span class="highlight-unit" id="len-result-unit">Feet (ft)</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Conversion Formula:</strong> <span id="len-formula-val">10 m × 3.28084 = 32.8084 ft</span></div>
        </div>

        <!-- All-in-One Comprehensive Table -->
        <div style="margin-top: 14px;">
          <div class="stat-header">SIMULTANEOUS EQUIVALENT MEASUREMENTS</div>
          <div class="data-table-wrapper" style="overflow-x: auto;">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Unit</th>
                  <th>Value</th>
                  <th>Unit Symbol</th>
                  <th>Unit System</th>
                </tr>
              </thead>
              <tbody id="len-table-body">
                <!-- Dynamically generated in JS -->
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>Global Standards for Length and Distance Conversion</h2>
        <p>Length is the fundamental measure of spatial distance between two points. While the International System of Units (SI) designates the <strong>meter (m)</strong> as the global scientific standard, the Imperial and US Customary systems (inches, feet, yards, and miles) remain ubiquitous across architecture, construction, aviation, and everyday commerce in the United States, United Kingdom, and Canada.</p>

        <h3>How to Use This Length Converter</h3>
        <ol>
          <li>Input any positive numerical distance or length value.</li>
          <li>Select the source unit in the <strong>From Unit</strong> dropdown.</li>
          <li>Select the desired target unit in the <strong>To Unit</strong> dropdown.</li>
          <li>Click <strong>Convert Length</strong> to see the exact converted amount, mathematical formula, and a comprehensive table converting your value to all 9 supported metric and imperial units simultaneously.</li>
        </ol>

        <h3>Fundamental Length Conversion Factors</h3>
        <ul>
          <li><strong>1 Inch = 2.54 Centimeters (exact international standard)</strong></li>
          <li><strong>1 Foot = 12 Inches = 0.3048 Meters</strong></li>
          <li><strong>1 Yard = 3 Feet = 0.9144 Meters</strong></li>
          <li><strong>1 Mile = 1,760 Yards = 5,280 Feet = 1.609344 Kilometers</strong></li>
          <li><strong>1 Nautical Mile = 1,852 Meters = 1.15078 Statute Miles</strong></li>
        </ul>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: Architectural Room Dimension</strong><br>
          Converting a 12-foot wall into meters for European tiles:<br>
          12 ft × 0.3048 = <strong>3.6576 Meters</strong> (365.76 cm).
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: Road Trip Distance</strong><br>
          A highway speed sign in the USA displays 65 Miles per hour.<br>
          65 mi × 1.609344 = <strong>104.607 Kilometers</strong>.
        </div>

        <h3>Tips for Precise Length Measurements</h3>
        <ul>
          <li><strong>Aviation vs Ground:</strong> Nautical miles (1,852 m) are defined based on one minute of latitude around the Earth's circumference and are used in maritime and aviation navigation, distinct from statute land miles (1,609.34 m).</li>
          <li><strong>Avoid intermediate rounding:</strong> When chaining measurements, maintain at least 4-5 decimal places until the final step to avoid compounding errors.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">How many centimeters are in an inch?</div>
            <div class="faq-a">By international treaty signed in 1959, 1 inch is defined as exactly 2.54 centimeters.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How many feet are in a meter?</div>
            <div class="faq-a">One meter is equal to approximately 3.28084 feet, or roughly 3 feet 3.37 inches.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">What is the difference between a statute mile and a nautical mile?</div>
            <div class="faq-a">A statute land mile is 5,280 feet (1.609 km), while a nautical mile is 6,076.12 feet (1.852 km). A nautical mile is approximately 15% longer than a standard mile.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How do I convert height in feet and inches (e.g. 5'9") to centimeters?</div>
            <div class="faq-a">Convert to total inches first: (5 × 12) + 9 = 69 inches. Then multiply by 2.54: 69 × 2.54 = 175.26 cm.</div>
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

# 14. WEIGHT CONVERTER
TIME_UNITS_TOOLS_HTML["weight-converter"] = """
    <!-- ==================== 29. WEIGHT CONVERTER ==================== -->
    <section id="screen-weight-converter" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Weight Converter</h1>
        <p class="tool-page-subtitle">Convert weight and mass across milligrams, grams, kilograms, metric tonnes, ounces, pounds, stones, and Indian quintals.</p>
      </div>

      <div class="card">
        <h2 class="card-title">Weight &amp; Mass Conversion</h2>
        <div class="input-grid-3">
          <div class="input-group">
            <label for="wt-val">Value to Convert</label>
            <input type="number" id="wt-val" value="5" min="0" step="any" oninput="convertWeight()">
          </div>
          <div class="input-group">
            <label for="wt-from">From Unit</label>
            <select id="wt-from" onchange="convertWeight()">
              <option value="mg">Milligrams (mg)</option>
              <option value="g">Grams (g)</option>
              <option value="kg" selected>Kilograms (kg)</option>
              <option value="t">Metric Tonnes (t)</option>
              <option value="oz">Ounces (oz)</option>
              <option value="lb">Pounds (lb)</option>
              <option value="st">Stones (st)</option>
              <option value="q">Quintals (q)</option>
            </select>
          </div>
          <div class="input-group">
            <label for="wt-to">To Unit</label>
            <select id="wt-to" onchange="convertWeight()">
              <option value="mg">Milligrams (mg)</option>
              <option value="g">Grams (g)</option>
              <option value="kg">Kilograms (kg)</option>
              <option value="t">Metric Tonnes (t)</option>
              <option value="oz">Ounces (oz)</option>
              <option value="lb" selected>Pounds (lb)</option>
              <option value="st">Stones (st)</option>
              <option value="q">Quintals (q)</option>
            </select>
          </div>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="convertWeight()">Convert Weight</button>
          <button class="btn btn-secondary" onclick="swapWeightUnits()">⇄ Swap Units</button>
          <button class="btn btn-outline" onclick="resetWeight()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="wt-results">
        <div class="stat-header">CONVERTED RESULT</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="wt-result-val">11.0231</span>
          <span class="highlight-unit" id="wt-result-unit">Pounds (lb)</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Conversion Formula:</strong> <span id="wt-formula-val">5 kg × 2.20462 = 11.0231 lb</span></div>
        </div>

        <!-- Equivalent Table -->
        <div style="margin-top: 14px;">
          <div class="stat-header">SIMULTANEOUS MASS EQUIVALENTS</div>
          <div class="data-table-wrapper" style="overflow-x: auto;">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Unit</th>
                  <th>Value</th>
                  <th>Symbol</th>
                  <th>Category</th>
                </tr>
              </thead>
              <tbody id="wt-table-body">
                <!-- Dynamically generated in JS -->
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>Understanding Mass and Weight Units: Metric vs Imperial</h2>
        <p>In physics, mass measures the amount of matter in an object, while weight measures the gravitational force acting upon it. On Earth, the two terms are used interchangeably in commerce, healthcare, and engineering. The SI unit of mass is the <strong>kilogram (kg)</strong>, while Anglo-American markets utilize the <strong>pound (avoirdupois lb)</strong> and <strong>ounce (oz)</strong>, and British healthcare traditions often track body weight in <strong>stones (st)</strong>.</p>

        <h3>How to Use This Weight Converter</h3>
        <ol>
          <li>Enter any numerical mass value into the input field.</li>
          <li>Choose your starting unit from the <strong>From Unit</strong> dropdown.</li>
          <li>Choose your destination unit from the <strong>To Unit</strong> dropdown.</li>
          <li>Click <strong>Convert Weight</strong> to view instant results, calculation formulas, and a full cross-unit table.</li>
        </ol>

        <h3>Key Mass Ratios and Conversion Constants</h3>
        <ul>
          <li><strong>1 Kilogram = 2.20462262 Pounds</strong></li>
          <li><strong>1 Pound = 16 Ounces = 453.59237 Grams (exact)</strong></li>
          <li><strong>1 Stone (UK) = 14 Pounds = 6.35029 Kilograms</strong></li>
          <li><strong>1 Metric Tonne = 1,000 Kilograms = 2,204.62 Pounds</strong></li>
          <li><strong>1 Indian Quintal = 100 Kilograms</strong></li>
        </ul>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: Airline Baggage Allowance</strong><br>
          An international airline permits 50 pounds of checked baggage per passenger.<br>
          50 lb / 2.20462 = <strong>22.68 Kilograms</strong> (typically rounded to 23 kg).
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: Agricultural Harvest</strong><br>
          A farmer harvests 35 Quintals of wheat.<br>
          35 q × 100 = <strong>3,500 Kilograms</strong> (3.5 Metric Tonnes).
        </div>

        <h3>Tips for Accurate Weight Conversions</h3>
        <ul>
          <li><strong>Avoirdupois vs Troy Ounces:</strong> Precious metals (gold, silver) are weighed in Troy ounces (1 troy oz = 31.1035 g), whereas food and postal items use standard Avoirdupois ounces (1 oz = 28.3495 g).</li>
          <li><strong>Commercial Tare Weight:</strong> When shipping freight, remember that gross weight includes packaging, whereas net weight reflects the cargo alone.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">How many grams are in one pound?</div>
            <div class="faq-a">One avoirdupois pound is officially defined as exactly 453.59237 grams.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">What is a stone in UK body weight measurements?</div>
            <div class="faq-a">A stone is an imperial unit of mass equal to exactly 14 pounds (approx. 6.35 kilograms). A person weighing 11 stone 4 lbs weighs 158 lbs or 71.67 kg.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">What is a metric tonne vs a US short ton?</div>
            <div class="faq-a">A metric tonne is 1,000 kg (2,204.6 lbs). A US short ton is 2,000 lbs (907.18 kg). A British long ton is 2,240 lbs (1,016 kg).</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How do I convert body weight from kg to lbs quickly in my head?</div>
            <div class="faq-a">Multiply your weight in kg by 2, then add 10% of that number. For example: 70 kg × 2 = 140; 140 + 14 = 154 lbs (actual is 154.32 lbs).</div>
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

# 15. TEMPERATURE CONVERTER
TIME_UNITS_TOOLS_HTML["temperature-converter"] = """
    <!-- ==================== 30. TEMPERATURE CONVERTER ==================== -->
    <section id="screen-temperature-converter" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Temperature Converter</h1>
        <p class="tool-page-subtitle">Convert temperatures accurately between Celsius (°C), Fahrenheit (°F), and Kelvin (K) with step-by-step mathematical formulas.</p>
      </div>

      <div class="card">
        <h2 class="card-title">Temperature Values</h2>
        <div class="input-grid-3">
          <div class="input-group">
            <label for="temp-val">Temperature Reading</label>
            <input type="number" id="temp-val" value="100" step="any" oninput="convertTemperature()">
          </div>
          <div class="input-group">
            <label for="temp-from">From Scale</label>
            <select id="temp-from" onchange="convertTemperature()">
              <option value="c" selected>Celsius (°C)</option>
              <option value="f">Fahrenheit (°F)</option>
              <option value="k">Kelvin (K)</option>
            </select>
          </div>
          <div class="input-group">
            <label for="temp-to">To Scale</label>
            <select id="temp-to" onchange="convertTemperature()">
              <option value="c">Celsius (°C)</option>
              <option value="f" selected>Fahrenheit (°F)</option>
              <option value="k">Kelvin (K)</option>
            </select>
          </div>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="convertTemperature()">Convert Temperature</button>
          <button class="btn btn-secondary" onclick="swapTemperatureUnits()">⇄ Swap Scales</button>
          <button class="btn btn-outline" onclick="resetTemperature()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="temp-results">
        <div class="stat-header">CONVERTED TEMPERATURE</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="temp-result-val">212.00</span>
          <span class="highlight-unit" id="temp-result-unit">°F</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Formula Applied:</strong> <span id="temp-formula-val">(100 °C × 9/5) + 32 = 212 °F</span></div>
          <div class="stat-pill"><strong>Physical State:</strong> <span id="temp-benchmark-val">Water Boiling Point at Sea Level</span></div>
        </div>
        <div class="result-grid-2">
          <div class="metric-box">
            <div class="metric-label">Celsius Scale (°C)</div>
            <div class="metric-value" id="temp-res-c">100.00 °C</div>
            <div class="metric-sub">Base-100 water phase scale</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Fahrenheit Scale (°F)</div>
            <div class="metric-value" id="temp-res-f">212.00 °F</div>
            <div class="metric-sub">US meteorological standard</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Kelvin Scale (K)</div>
            <div class="metric-value" id="temp-res-k">373.15 K</div>
            <div class="metric-sub">SI absolute thermodynamic scale</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Distance Above Absolute Zero</div>
            <div class="metric-value" id="temp-res-zero">+373.15 K</div>
            <div class="metric-sub">Absolute thermal energy level</div>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>Thermodynamic Scales: Celsius, Fahrenheit, and Kelvin</h2>
        <p>Temperature quantifies the average kinetic energy of vibrating atoms and molecules in a substance. Unlike length or weight where zero signifies nothingness, zero on the <strong>Celsius (°C)</strong> scale represents the freezing point of pure water at one standard atmosphere, while zero on the <strong>Fahrenheit (°F)</strong> scale represents the freezing point of a saltwater brine. Only the <strong>Kelvin (K)</strong> scale is an absolute scale, beginning at <strong>Absolute Zero (0 K or −273.15 °C)</strong>, where all molecular motion ceases.</p>

        <h3>How to Use This Temperature Converter</h3>
        <ol>
          <li>Enter any temperature reading into the input field (supports negative values).</li>
          <li>Choose your starting thermal scale in the <strong>From Scale</strong> selector.</li>
          <li>Choose your target thermal scale in the <strong>To Scale</strong> selector.</li>
          <li>Click <strong>Convert Temperature</strong> to observe the converted value, physical phase benchmark, and simultaneous readings across all three thermodynamic systems.</li>
        </ol>

        <h3>Exact Conversion Equations</h3>
        <ul>
          <li><strong>Celsius to Fahrenheit:</strong> <code>°F = (°C × 9/5) + 32</code> or <code>(°C × 1.8) + 32</code></li>
          <li><strong>Fahrenheit to Celsius:</strong> <code>°C = (°F − 32) × 5/9</code></li>
          <li><strong>Celsius to Kelvin:</strong> <code>K = °C + 273.15</code></li>
          <li><strong>Kelvin to Celsius:</strong> <code>°C = K − 273.15</code></li>
          <li><strong>Fahrenheit to Kelvin:</strong> <code>K = ((°F − 32) × 5/9) + 273.15</code></li>
        </ul>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: Human Body Temperature</strong><br>
          Normal body temperature is approximately 37.0 °C.<br>
          °F = (37.0 × 1.8) + 32 = 66.6 + 32 = <strong>98.6 °F</strong> (310.15 K).
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: Kitchen Baking Oven</strong><br>
          An American baking recipe specifies 350 °F.<br>
          °C = (350 − 32) × 5/9 = 318 × 0.5556 = <strong>176.7 °C</strong> (usually rounded to 180 °C).
        </div>

        <h3>Key Thermal Reference Milestones</h3>
        <ul>
          <li><strong>Absolute Zero:</strong> −273.15 °C = −459.67 °F = 0 K</li>
          <li><strong>Freezing Point of Water:</strong> 0 °C = 32 °F = 273.15 K</li>
          <li><strong>Comfortable Room Temperature:</strong> 20 to 22 °C = 68 to 72 °F</li>
          <li><strong>Boiling Point of Water:</strong> 100 °C = 212 °F = 373.15 K</li>
          <li><strong>The Coincidence Point:</strong> −40 °C is exactly equal to −40 °F!</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">Why does the Kelvin scale not use a degree symbol (°)?</div>
            <div class="faq-a">Kelvin is an absolute thermodynamic unit of measurement rather than an arbitrary scale with an offset zero point. Therefore, standard scientific convention writes 300 K rather than 300 °K.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">At what temperature do Celsius and Fahrenheit read the same number?</div>
            <div class="faq-a">At exactly −40°. When it is −40 °C outside, it is also −40 °F.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can temperature ever drop below 0 Kelvin?</div>
            <div class="faq-a">No. 0 Kelvin is Absolute Zero, the thermodynamic limit where subatomic particles possess minimum quantum zero-point vibrational energy.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How can I quickly convert Fahrenheit to Celsius in my head?</div>
            <div class="faq-a">Subtract 30 and then divide by 2. For example, 70 °F − 30 = 40; 40 / 2 = 20 °C (exact conversion is 21.1 °C).</div>
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

# 16. AREA CONVERTER
TIME_UNITS_TOOLS_HTML["area-converter"] = """
    <!-- ==================== 31. AREA CONVERTER ==================== -->
    <section id="screen-area-converter" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Area Converter</h1>
        <p class="tool-page-subtitle">Convert land, real estate, and construction area across square feet, square meters, acres, hectares, guntha, bigha, and square yards.</p>
      </div>

      <div class="card">
        <h2 class="card-title">Area &amp; Land Measurement</h2>
        <div class="input-grid-3">
          <div class="input-group">
            <label for="area-val">Area Value</label>
            <input type="number" id="area-val" value="1200" min="0" step="any" oninput="convertArea()">
          </div>
          <div class="input-group">
            <label for="area-from">From Unit</label>
            <select id="area-from" onchange="convertArea()">
              <option value="sqft" selected>Square Feet (sq ft)</option>
              <option value="sqm">Square Meters (sq m)</option>
              <option value="sqyd">Square Yards / Gaj (sq yd)</option>
              <option value="acre">Acres (ac)</option>
              <option value="hectare">Hectares (ha)</option>
              <option value="guntha">Guntha (India: 1,089 sq ft)</option>
              <option value="bigha">Bigha (Standard: 27,225 sq ft)</option>
              <option value="sqkm">Square Kilometers (sq km)</option>
            </select>
          </div>
          <div class="input-group">
            <label for="area-to">To Unit</label>
            <select id="area-to" onchange="convertArea()">
              <option value="sqft">Square Feet (sq ft)</option>
              <option value="sqm" selected>Square Meters (sq m)</option>
              <option value="sqyd">Square Yards / Gaj (sq yd)</option>
              <option value="acre">Acres (ac)</option>
              <option value="hectare">Hectares (ha)</option>
              <option value="guntha">Guntha (India: 1,089 sq ft)</option>
              <option value="bigha">Bigha (Standard: 27,225 sq ft)</option>
              <option value="sqkm">Square Kilometers (sq km)</option>
            </select>
          </div>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="convertArea()">Convert Area</button>
          <button class="btn btn-secondary" onclick="swapAreaUnits()">⇄ Swap Units</button>
          <button class="btn btn-outline" onclick="resetArea()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="area-results">
        <div class="stat-header">CONVERTED AREA</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="area-result-val">111.4836</span>
          <span class="highlight-unit" id="area-result-unit">Square Meters (sq m)</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Formula Applied:</strong> <span id="area-formula-val">1,200 sq ft × 0.092903 = 111.48 sq m</span></div>
        </div>

        <!-- Equivalent Table -->
        <div style="margin-top: 14px;">
          <div class="stat-header">SIMULTANEOUS LAND MEASUREMENTS</div>
          <div class="data-table-wrapper" style="overflow-x: auto;">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Unit Name</th>
                  <th>Equivalent Value</th>
                  <th>Symbol</th>
                  <th>Standard Basis</th>
                </tr>
              </thead>
              <tbody id="area-table-body">
                <!-- Dynamically generated in JS -->
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>Land and Real Estate Area Measurements in India and Globally</h2>
        <p>Area measures two-dimensional surface space. In real estate transactions, architectural floor plans, and agricultural property surveys, buyers and sellers encounter a confusing blend of metric units (<strong>square meters, hectares</strong>), imperial units (<strong>square feet, square yards, acres</strong>), and traditional Indian land units (<strong>guntha, bigha, gaj</strong>). Converting accurately prevents severe property miscalculations.</p>

        <h3>How to Use This Area Converter</h3>
        <ol>
          <li>Enter any numerical surface area value into the input box.</li>
          <li>Choose your source unit in the <strong>From Unit</strong> selector.</li>
          <li>Choose your destination unit in the <strong>To Unit</strong> selector.</li>
          <li>Click <strong>Convert Area</strong> to obtain the exact converted result and a complete multi-unit comparative breakdown.</li>
        </ol>

        <h3>Standard Area Conversion Equivalents</h3>
        <ul>
          <li><strong>1 Square Meter = 10.7639 Square Feet</strong></li>
          <li><strong>1 Square Yard (Gaj) = 9 Square Feet = 0.8361 Square Meters</strong></li>
          <li><strong>1 Acre = 43,560 Square Feet = 4,046.86 Square Meters = 40 Gunthas</strong></li>
          <li><strong>1 Hectare = 10,000 Square Meters = 2.47105 Acres = 107,639 Square Feet</strong></li>
          <li><strong>1 Guntha = 1,089 Square Feet = 33 ft × 33 ft</strong></li>
          <li><strong>1 Pucca Bigha (Standard) = 27,225 Square Feet = 165 ft × 165 ft = 25 Gunthas</strong></li>
        </ul>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: Residential Apartment Floor Area</strong><br>
          A builder advertises an apartment with 1,200 sq ft carpet area.<br>
          1,200 sq ft × 0.092903 = <strong>111.48 Square Meters</strong> (133.33 Square Yards / Gaj).
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: Agricultural Farmland</strong><br>
          A farmer owns 5 Acres of land.<br>
          5 Acres = 5 × 40 Gunthas = <strong>200 Gunthas</strong> = <strong>2.0234 Hectares</strong> = <strong>2,17,800 Square Feet</strong>.
        </div>

        <h3>Tips for Real Estate Buyers</h3>
        <ul>
          <li><strong>Carpet Area vs Super Built-up:</strong> RERA in India mandates that property prices be quoted based on usable <em>carpet area</em> (actual net internal floor area), not super built-up area which inflates square footage with common lobbies and elevator shafts.</li>
          <li><strong>Beware regional variations in Bigha:</strong> While a standard Pucca Bigha is 27,225 sq ft, local customary bighas vary widely between Uttar Pradesh, Rajasthan, Bihar, and Assam. Always verify against registered deed documents.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">How many square feet are in one acre?</div>
            <div class="faq-a">One international acre contains exactly 43,560 square feet (approx. 4,046.86 square meters or 4,840 square yards).</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">What is one Guntha equal to in square feet?</div>
            <div class="faq-a">One Guntha is standard in Maharashtra, Karnataka, and Gujarat as exactly 1,089 square feet (or 1/40th of an acre).</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Is a Gaj the same as a Square Yard?</div>
            <div class="faq-a">Yes. In North Indian real estate terminology, "1 Gaj" is synonymous with 1 Square Yard (9 square feet or 0.836 sq m). A 100 Gaj plot equals 900 square feet.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How many acres are in a hectare?</div>
            <div class="faq-a">One hectare is equal to approximately 2.47105 acres (10,000 square meters).</div>
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

# 17. VOLUME CONVERTER
TIME_UNITS_TOOLS_HTML["volume-converter"] = """
    <!-- ==================== 32. VOLUME CONVERTER ==================== -->
    <section id="screen-volume-converter" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Volume Converter</h1>
        <p class="tool-page-subtitle">Convert liquid capacity and cubic volume between milliliters, liters, cubic meters, gallons, cups, fluid ounces, and cubic feet.</p>
      </div>

      <div class="card">
        <h2 class="card-title">Volume &amp; Fluid Capacity</h2>
        <div class="input-grid-3">
          <div class="input-group">
            <label for="vol-val">Volume Value</label>
            <input type="number" id="vol-val" value="5" min="0" step="any" oninput="convertVolume()">
          </div>
          <div class="input-group">
            <label for="vol-from">From Unit</label>
            <select id="vol-from" onchange="convertVolume()">
              <option value="l" selected>Liters (L)</option>
              <option value="ml">Milliliters (ml)</option>
              <option value="m3">Cubic Meters (m³)</option>
              <option value="usgal">US Liquid Gallons (gal)</option>
              <option value="impgal">Imperial Gallons (UK gal)</option>
              <option value="usfloz">US Fluid Ounces (fl oz)</option>
              <option value="uscup">US Cups (cup)</option>
              <option value="cuft">Cubic Feet (ft³)</option>
            </select>
          </div>
          <div class="input-group">
            <label for="vol-to">To Unit</label>
            <select id="vol-to" onchange="convertVolume()">
              <option value="l">Liters (L)</option>
              <option value="ml">Milliliters (ml)</option>
              <option value="m3">Cubic Meters (m³)</option>
              <option value="usgal" selected>US Liquid Gallons (gal)</option>
              <option value="impgal">Imperial Gallons (UK gal)</option>
              <option value="usfloz">US Fluid Ounces (fl oz)</option>
              <option value="uscup">US Cups (cup)</option>
              <option value="cuft">Cubic Feet (ft³)</option>
            </select>
          </div>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="convertVolume()">Convert Volume</button>
          <button class="btn btn-secondary" onclick="swapVolumeUnits()">⇄ Swap Units</button>
          <button class="btn btn-outline" onclick="resetVolume()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="vol-results">
        <div class="stat-header">CONVERTED VOLUME</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="vol-result-val">1.3209</span>
          <span class="highlight-unit" id="vol-result-unit">US Gallons (gal)</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Conversion Formula:</strong> <span id="vol-formula-val">5 L × 0.264172 = 1.3209 US gal</span></div>
        </div>

        <!-- Equivalent Table -->
        <div style="margin-top: 14px;">
          <div class="stat-header">SIMULTANEOUS CAPACITY EQUIVALENTS</div>
          <div class="data-table-wrapper" style="overflow-x: auto;">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Unit</th>
                  <th>Value</th>
                  <th>Symbol</th>
                  <th>Category</th>
                </tr>
              </thead>
              <tbody id="vol-table-body">
                <!-- Dynamically generated in JS -->
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>Liquid Volume &amp; Capacity Conversion: Metric, US, and Imperial</h2>
        <p>Volume measures the three-dimensional space enclosed by a container or occupied by a liquid, gas, or solid substance. In culinary baking, automotive fuel dispensing, civil water tank design, and chemical manufacturing, converting seamlessly between metric units (<strong>liters, milliliters, cubic meters</strong>) and Anglo-American units (<strong>gallons, fluid ounces, pints, cups</strong>) is essential.</p>

        <h3>How to Use This Volume Converter</h3>
        <ol>
          <li>Type the numerical volume value you want to convert.</li>
          <li>Pick your original unit in the <strong>From Unit</strong> selector.</li>
          <li>Pick your target unit in the <strong>To Unit</strong> selector.</li>
          <li>Click <strong>Convert Volume</strong> to see the exact converted amount and a complete table of volume equivalents across all major measurement systems.</li>
        </ol>

        <h3>Key Volume Equivalence Constants</h3>
        <ul>
          <li><strong>1 Liter = 1,000 Milliliters = 1 Cubic Decimeter</strong></li>
          <li><strong>1 US Liquid Gallon = 3.78541 Liters = 128 US Fluid Ounces</strong></li>
          <li><strong>1 Imperial Gallon (UK) = 4.54609 Liters = 160 Imperial Fluid Ounces</strong></li>
          <li><strong>1 US Cup = 236.588 Milliliters = 8 US Fluid Ounces</strong></li>
          <li><strong>1 Cubic Meter = 1,000 Liters = 35.3147 Cubic Feet</strong></li>
        </ul>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: Automotive Fuel Tank Capacity</strong><br>
          A car tank holds 15 US gallons of gasoline.<br>
          15 US gal × 3.78541 = <strong>56.78 Liters</strong>.
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: Culinary Recipe Conversion</strong><br>
          An American culinary recipe calls for 2.5 US cups of milk.<br>
          2.5 cups × 236.588 = <strong>591.47 Milliliters</strong> (approx. 0.59 Liters).
        </div>

        <h3>Tips for Precise Volume Measurements</h3>
        <ul>
          <li><strong>Beware US vs UK Gallons:</strong> An Imperial (UK) gallon (4.546 L) is approximately 20% larger than a US gallon (3.785 L). Never confuse the two in engineering or international shipping.</li>
          <li><strong>Fluid Ounces vs Weight Ounces:</strong> Fluid ounces measure liquid volume; avoirdupois ounces measure mass. Only for pure water at 4°C does 1 fluid ounce weigh approximately 1 ounce.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">How many liters are in one US gallon?</div>
            <div class="faq-a">One US liquid gallon equals exactly 3.785411784 liters.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">What is the difference between a milliliter and a cubic centimeter (cc)?</div>
            <div class="faq-a">They are identical in volume: 1 Milliliter (ml) = 1 Cubic Centimeter (cm³ or cc).</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How many liters fit inside a 1,000-liter rooftop water tank?</div>
            <div class="faq-a">Exactly 1 cubic meter of water (1,000 liters), weighing precisely 1,000 kilograms (1 metric tonne) at standard ambient conditions.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How many cups are in one liter?</div>
            <div class="faq-a">One liter is approximately 4.2268 standard US cups (where 1 US cup is 236.59 ml). In metric culinary countries, a metric cup is defined as exactly 250 ml, yielding exactly 4 metric cups per liter.</div>
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

print("tools_html_time_units.py created successfully with Tools 11-17.")
