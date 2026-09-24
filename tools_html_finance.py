# tools_html_finance.py
# HTML sections for Tools 1-6: Loan Interest, Loan Eligibility, Loan Tenure, Salary, Overtime, Tax

FINANCE_TOOLS_HTML = {}

# 1. LOAN INTEREST CALCULATOR
FINANCE_TOOLS_HTML["loan-interest"] = """
    <!-- ==================== 16. LOAN INTEREST CALCULATOR ==================== -->
    <section id="screen-loan-interest" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Loan Interest Calculator</h1>
        <p class="tool-page-subtitle">Calculate total interest expense, compare reducing balance vs flat interest rates, and evaluate your cost of borrowing.</p>
      </div>

      <div class="card">
        <h2 class="card-title">Loan Interest Parameters</h2>
        <div class="input-group" style="margin-bottom: 14px;">
          <label>Select Currency</label>
          <div class="segmented-control" id="li-currency-control">
            <button type="button" id="li-curr-inr" class="segment-btn active" onclick="setLiCurrency('INR')">Indian Rupee (₹ INR)</button>
            <button type="button" id="li-curr-usd" class="segment-btn" onclick="setLiCurrency('USD')">US Dollar ($ USD)</button>
          </div>
        </div>

        <div class="input-grid-2">
          <div class="input-group">
            <label for="li-principal" id="li-principal-label">Loan Principal (₹)</label>
            <input type="number" id="li-principal" value="500000" min="1000" step="5000" oninput="calculateLoanInterest()">
          </div>
          <div class="input-group">
            <label for="li-rate">Annual Interest Rate (%)</label>
            <input type="number" id="li-rate" value="9.5" min="0.1" max="100" step="0.1" oninput="calculateLoanInterest()">
          </div>
        </div>

        <div class="input-grid-2">
          <div class="input-group">
            <label for="li-tenure">Loan Tenure</label>
            <input type="number" id="li-tenure" value="5" min="1" max="50" oninput="calculateLoanInterest()">
          </div>
          <div class="input-group">
            <label>Tenure Type</label>
            <div class="segmented-control">
              <button type="button" id="li-tenure-yr" class="segment-btn active" onclick="setLiTenureUnit('years')">Years</button>
              <button type="button" id="li-tenure-mo" class="segment-btn" onclick="setLiTenureUnit('months')">Months</button>
            </div>
          </div>
        </div>

        <div class="input-group">
          <label>Interest Computation Method</label>
          <div class="segmented-control">
            <button type="button" id="li-type-reducing" class="segment-btn active" onclick="setLiType('reducing')">Reducing Balance (Standard Bank EMI)</button>
            <button type="button" id="li-type-flat" class="segment-btn" onclick="setLiType('flat')">Flat / Simple Rate</button>
          </div>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="calculateLoanInterest()">Calculate Interest</button>
          <button class="btn btn-outline" onclick="resetLoanInterest()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="li-results">
        <div class="stat-header">TOTAL BORROWING COST</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="li-total-interest-val">₹1,30,050</span>
          <span class="highlight-unit">Total Interest</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Interest to Principal Ratio:</strong> <span id="li-ratio-val">26.01%</span></div>
          <div class="stat-pill"><strong>Monthly Installment:</strong> <span id="li-monthly-val">₹10,501</span></div>
        </div>
        <div class="result-grid-2">
          <div class="metric-box">
            <div class="metric-label">Principal Borrowed</div>
            <div class="metric-value" id="li-res-principal">₹5,00,000</div>
            <div class="metric-sub">Initial sanctioned capital</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Total Amount Paid</div>
            <div class="metric-value" id="li-res-total">₹6,30,050</div>
            <div class="metric-sub">Principal + Total Interest</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Average Annual Interest</div>
            <div class="metric-value" id="li-res-annual-interest">₹26,010/yr</div>
            <div class="metric-sub">Mean cost per elapsed year</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Effective APR Check</div>
            <div class="metric-value" id="li-res-eff-apr">9.50%</div>
            <div class="metric-sub">True annualized financing rate</div>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>Complete Guide to Loan Interest &amp; Borrowing Costs</h2>
        <p>When you borrow money through a home loan, personal loan, vehicle loan, or education finance, your total financial commitment is always higher than the initial principal. The extra charge is the <strong>interest</strong>—the fee paid to the bank or NBFC for the risk and opportunity cost of lending capital. Understanding how loan interest is computed allows you to save substantial sums over your loan tenure.</p>

        <h3>How to Use This Loan Interest Calculator</h3>
        <ol>
          <li><strong>Select your currency:</strong> Toggle between Indian Rupee (₹ INR) and US Dollar ($ USD).</li>
          <li><strong>Enter Loan Principal:</strong> Input the exact sum you plan to borrow from the lender.</li>
          <li><strong>Input Annual Interest Rate:</strong> Type the quoted percentage per annum (p.a.).</li>
          <li><strong>Choose Tenure:</strong> Specify duration in years or months.</li>
          <li><strong>Select Calculation Method:</strong> Choose <em>Reducing Balance</em> for standard retail bank loans or <em>Flat Rate</em> for consumer durables and dealer financing.</li>
          <li>Click <strong>Calculate Interest</strong> to see your total interest, monthly payment, and interest-to-principal ratio.</li>
        </ol>

        <h3>Formulas: Reducing Balance vs Flat Interest</h3>
        <p>In a <strong>Reducing Balance Loan</strong>, monthly interest is calculated only on the remaining unpaid principal at each cycle:</p>
        <p><code>Monthly Interest = Unpaid Principal × (Annual Rate / 12 / 100)</code></p>
        <p>In a <strong>Flat Rate Loan</strong>, interest is calculated on the entire initial principal across the whole tenure, making it far more expensive:</p>
        <p><code>Total Flat Interest = Principal × (Annual Rate / 100) × Tenure in Years</code></p>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: Reducing Balance Auto Loan</strong><br>
          Principal: ₹5,00,000 | Interest Rate: 9.5% p.a. | Tenure: 5 Years (60 Months).<br>
          Monthly EMI = ₹10,501. Total Payment = ₹6,30,050. Total Interest = <strong>₹1,30,050</strong> (26.0% of principal).
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: 12% Flat Rate Trap vs Reducing</strong><br>
          Principal: ₹1,00,000 | Rate: 12% | Tenure: 3 Years.<br>
          Flat Interest = ₹1,00,000 × 12% × 3 = ₹36,000. In reducing balance, total interest is only ₹19,572. A flat 12% rate is equivalent to an effective reducing rate of almost 21.5%!
        </div>

        <h3>Useful Tips to Cut Your Loan Interest</h3>
        <ul>
          <li><strong>Make prepayments early:</strong> In the first third of your loan tenure, 60-70% of each EMI goes toward interest. Early lump-sum prepayments drastically slash total interest.</li>
          <li><strong>Increase your EMI by 5-10% annually:</strong> Aligning repayment hikes with salary increments can cut a 20-year loan tenure down to 12 years.</li>
          <li><strong>Check the APR:</strong> Always compare the Annual Percentage Rate (APR) including processing fees rather than just nominal headline rates.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">What is the difference between an EMI calculator and this Loan Interest calculator?</div>
            <div class="faq-a">An EMI calculator focuses primarily on your required monthly installment, whereas this Loan Interest Calculator breaks down the net cost of borrowing, interest-to-principal ratio, and contrasts reducing versus flat rate schemes.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Why is flat rate interest misleading?</div>
            <div class="faq-a">A flat interest rate charges you interest on the full starting loan amount even after you have paid back 90% of the loan. A flat rate of 10% is approximately equal to an 18% reducing interest rate.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Does shortening loan tenure save interest?</div>
            <div class="faq-a">Yes. Although your monthly installment increases, the total interest paid drops substantially because interest accrues over fewer compounding periods.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Are loan interest payments tax deductible in India?</div>
            <div class="faq-a">Home loan interest qualifies for deduction up to ₹2,00,000 per year under Section 24(b) of the Income Tax Act for self-occupied properties in the Old Tax Regime.</div>
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

# 2. LOAN ELIGIBILITY CALCULATOR
FINANCE_TOOLS_HTML["loan-eligibility"] = """
    <!-- ==================== 17. LOAN ELIGIBILITY CALCULATOR ==================== -->
    <section id="screen-loan-eligibility" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Loan Eligibility Calculator</h1>
        <p class="tool-page-subtitle">Check your maximum home, car, or personal loan eligibility based on net monthly salary and Fixed Obligation to Income Ratio (FOIR).</p>
      </div>

      <div class="card">
        <h2 class="card-title">Income &amp; Obligation Inputs</h2>
        <div class="input-grid-2">
          <div class="input-group">
            <label for="le-income">Net Monthly Income / Salary (₹)</label>
            <input type="number" id="le-income" value="75000" min="5000" step="1000" oninput="calculateLoanEligibility()">
          </div>
          <div class="input-group">
            <label for="le-emis">Existing Monthly EMIs / Debts (₹)</label>
            <input type="number" id="le-emis" value="10000" min="0" step="500" oninput="calculateLoanEligibility()">
          </div>
        </div>

        <div class="input-grid-3">
          <div class="input-group">
            <label for="le-rate">Expected Interest Rate (%)</label>
            <input type="number" id="le-rate" value="8.75" min="1" max="30" step="0.1" oninput="calculateLoanEligibility()">
          </div>
          <div class="input-group">
            <label for="le-tenure">Loan Tenure (Years)</label>
            <input type="number" id="le-tenure" value="20" min="1" max="30" oninput="calculateLoanEligibility()">
          </div>
          <div class="input-group">
            <label for="le-foir">FOIR Limit (%)</label>
            <select id="le-foir" onchange="calculateLoanEligibility()">
              <option value="40">40% (Conservative / Personal Loan)</option>
              <option value="50" selected>50% (Standard Home Loan)</option>
              <option value="60">60% (High Income > ₹1.5L/mo)</option>
              <option value="65">65% (Executive Income)</option>
            </select>
          </div>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="calculateLoanEligibility()">Calculate Eligibility</button>
          <button class="btn btn-outline" onclick="resetLoanEligibility()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="le-results">
        <div class="stat-header">ESTIMATED MAXIMUM LOAN ELIGIBILITY</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="le-max-loan-val">₹31,09,500</span>
          <span class="highlight-unit">Sanction Capacity</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Max Permissible New EMI:</strong> <span id="le-max-emi-val">₹27,500/mo</span></div>
          <div class="stat-pill"><strong>Current FOIR Used:</strong> <span id="le-current-foir-val">13.33%</span></div>
        </div>
        <div class="result-grid-2">
          <div class="metric-box">
            <div class="metric-label">Total Debt Capacity Allowed</div>
            <div class="metric-value" id="le-res-total-cap">₹37,500/mo</div>
            <div class="metric-sub">50% FOIR threshold of net income</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Uncommitted Disposable Income</div>
            <div class="metric-value" id="le-res-disposable">₹37,500/mo</div>
            <div class="metric-sub">Remaining buffer for living expenses</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Conservative Loan (40% FOIR)</div>
            <div class="metric-value" id="le-res-conservative">₹22,61,500</div>
            <div class="metric-sub">Lower risk, highly affordable</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Stretch Loan (60% FOIR)</div>
            <div class="metric-value" id="le-res-stretch">₹39,57,500</div>
            <div class="metric-sub">Maximum capacity with co-applicant</div>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>How Indian Banks Determine Your Loan Eligibility</h2>
        <p>Before sanctioning any retail credit facility—be it a housing loan, car loan, or personal loan—lenders evaluate your debt-servicing capacity using a benchmark known as the <strong>Fixed Obligation to Income Ratio (FOIR)</strong> or Debt-to-Income (DTI) ratio. Banks require that your total monthly loan repayments, including the prospective new loan, do not consume more than 40% to 60% of your net monthly take-home salary.</p>

        <h3>How to Use This Calculator</h3>
        <ol>
          <li>Enter your <strong>Net Monthly Salary</strong> after taxes, PF, and statutory deductions.</li>
          <li>Enter the sum of your <strong>Existing Monthly EMIs</strong> (credit card installments, personal loans, vehicle loans).</li>
          <li>Specify the <strong>Expected Interest Rate</strong> and desired <strong>Tenure</strong> in years.</li>
          <li>Select the lender's <strong>FOIR limit</strong> (typically 50% for standard applicants).</li>
          <li>Click <strong>Calculate Eligibility</strong> to review your maximum borrowing limit and monthly EMI quota.</li>
        </ol>

        <h3>The Present Value Eligibility Formula</h3>
        <p>First, the maximum permissible new monthly EMI is determined:</p>
        <p><code>Max New EMI = (Net Monthly Salary × FOIR%) − Existing EMIs</code></p>
        <p>Next, the maximum principal is calculated using the standard discounted present value formula for an ordinary annuity:</p>
        <p><code>Max Loan Amount = [Max EMI × ((1 + r)^n − 1)] / [r × (1 + r)^n]</code></p>
        <p>Where <em>r</em> is the monthly interest rate (annual rate / 12 / 100) and <em>n</em> is the total tenure in months.</p>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: Single Applicant with Existing Bike Loan</strong><br>
          Salary: ₹75,000/mo | Existing Bike EMI: ₹10,000 | Expected Rate: 8.75% | Tenure: 20 Years | FOIR: 50%.<br>
          Allowed Total EMI = ₹37,500. Permissible New EMI = ₹37,500 − ₹10,000 = ₹27,500.<br>
          Maximum Eligible Loan Amount = <strong>₹31,09,500</strong>.
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: Zero Debt Applicant</strong><br>
          Salary: ₹1,00,000/mo | Existing EMIs: ₹0 | Expected Rate: 8.5% | Tenure: 25 Years | FOIR: 50%.<br>
          Permissible EMI = ₹50,000. Maximum Eligible Loan = <strong>₹62,07,000</strong>.
        </div>

        <h3>Tips to Boost Your Loan Eligibility</h3>
        <ul>
          <li><strong>Close small outstanding loans:</strong> Paying off a ₹6,000/month credit card EMI can boost your home loan eligibility by nearly ₹7,00,000!</li>
          <li><strong>Add a earning co-applicant:</strong> Adding a spouse or working parent pools monthly incomes and significantly enlarges permissible EMI capacity.</li>
          <li><strong>Opt for a longer tenure:</strong> Extending tenure from 15 to 25 years lowers monthly installments per lakh borrowed, increasing your sanction limit.</li>
          <li><strong>Maintain a 750+ CIBIL score:</strong> High credit scores unlock preferential interest rates, directly expanding your loan amount for the same EMI budget.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">What is FOIR and why do banks care about it?</div>
            <div class="faq-a">FOIR stands for Fixed Obligation to Income Ratio. It ensures that a borrower retains at least 40% to 50% of their net salary for household living expenses, food, rent, and unforeseen emergencies without defaulting on loan commitments.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Does annual bonus count toward loan eligibility?</div>
            <div class="faq-a">Most major banks take only the recurring monthly base and fixed allowances into account. Variable incentives and annual bonuses are often discounted by 50% or excluded unless consistently documented across 2-3 years of Form 16.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Will taking a longer tenure increase my overall interest cost?</div>
            <div class="faq-a">Yes. While longer tenure increases eligibility today, it also prolongs the compounding cycle, meaning you pay significantly more total interest over the lifetime of the loan.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can self-employed individuals use this calculator?</div>
            <div class="faq-a">Yes. Self-employed borrowers can input their average monthly net profit after business expenses and taxes as reflected in their latest Income Tax Returns (ITR).</div>
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

# 3. LOAN TENURE CALCULATOR
FINANCE_TOOLS_HTML["loan-tenure"] = """
    <!-- ==================== 18. LOAN TENURE CALCULATOR ==================== -->
    <section id="screen-loan-tenure" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Loan Tenure Calculator</h1>
        <p class="tool-page-subtitle">Calculate the exact number of months and years needed to pay off your loan based on your affordable monthly repayment budget.</p>
      </div>

      <div class="card">
        <h2 class="card-title">Loan &amp; Budget Inputs</h2>
        <div class="input-grid-3">
          <div class="input-group">
            <label for="lt-principal">Loan Amount (Principal ₹)</label>
            <input type="number" id="lt-principal" value="1000000" min="10000" step="10000" oninput="calculateLoanTenure()">
          </div>
          <div class="input-group">
            <label for="lt-rate">Annual Interest Rate (%)</label>
            <input type="number" id="lt-rate" value="9.0" min="0.1" max="40" step="0.1" oninput="calculateLoanTenure()">
          </div>
          <div class="input-group">
            <label for="lt-emi">Target Monthly Payment (₹)</label>
            <input type="number" id="lt-emi" value="15000" min="500" step="500" oninput="calculateLoanTenure()">
          </div>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="calculateLoanTenure()">Calculate Tenure</button>
          <button class="btn btn-outline" onclick="resetLoanTenure()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="lt-results">
        <div class="stat-header">ESTIMATED REPAYMENT DURATION</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="lt-tenure-years-val">8 Years, 6 Months</span>
          <span class="highlight-unit" id="lt-tenure-months-val">102 Total Months</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Total Interest Payable:</strong> <span id="lt-total-interest-val">₹5,20,450</span></div>
          <div class="stat-pill"><strong>Total Payment:</strong> <span id="lt-total-payment-val">₹15,20,450</span></div>
        </div>
        <div class="result-grid-2">
          <div class="metric-box">
            <div class="metric-label">Minimum Mandatory Monthly Payment</div>
            <div class="metric-value" id="lt-res-min-emi">₹7,500</div>
            <div class="metric-sub">Required just to cover monthly interest</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Principal Amortization Speed</div>
            <div class="metric-value" id="lt-res-speed">₹7,500/mo</div>
            <div class="metric-sub">Portion reducing loan balance in Month 1</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Tenure if Payment + ₹2,000/mo</div>
            <div class="metric-value" id="lt-res-extra-tenure">6 Yrs, 10 Mos</div>
            <div class="metric-sub">Saves 20 months of installments</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Interest Saved with + ₹2,000/mo</div>
            <div class="metric-value" id="lt-res-extra-savings">₹1,18,500</div>
            <div class="metric-sub">Net financial savings</div>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>Understanding Loan Payoff Schedules &amp; Tenure Calculation</h2>
        <p>Most borrowers are accustomed to choosing a loan tenure and accepting whatever EMI the bank assigns. However, the reverse approach is often far more financially savvy: determining how much money you can realistically spare each month, and calculating the exact <strong>loan tenure</strong> needed to reach debt freedom. Increasing your monthly payment by even a modest sum can dramatically truncate your loan payoff calendar.</p>

        <h3>How to Use This Loan Tenure Calculator</h3>
        <ol>
          <li>Enter your outstanding or planned <strong>Loan Principal</strong> balance.</li>
          <li>Enter the lender's quoted <strong>Annual Interest Rate</strong>.</li>
          <li>Enter your <strong>Target Monthly Payment (EMI)</strong> that you can comfortably allocate.</li>
          <li>Click <strong>Calculate Tenure</strong>. The solver reveals your exact time to full payoff, along with interest savings if you increase your monthly contribution.</li>
        </ol>

        <h3>Mathematical Formula for Loan Tenure</h3>
        <p>Using the logarithmic amortization formula derived from compound annuity math:</p>
        <p><code>n = − ln(1 − (P × r / EMI)) / ln(1 + r)</code></p>
        <p>Where:</p>
        <ul>
          <li><strong>n</strong> = Total number of monthly installments required.</li>
          <li><strong>P</strong> = Loan principal amount.</li>
          <li><strong>r</strong> = Periodic monthly interest rate = (Annual Rate / 12 / 100).</li>
          <li><strong>EMI</strong> = Chosen monthly payment amount.</li>
          <li><strong>ln</strong> = Natural logarithm function.</li>
        </ul>
        <p><em>Critical Condition:</em> The chosen monthly payment must be strictly greater than <code>P × r</code> (the first month's interest). If it is less, the loan balance will grow indefinitely through negative amortization.</p>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: ₹10,00,000 Personal Loan Payoff</strong><br>
          Loan: ₹10,00,000 | Rate: 9.0% p.a. | Target EMI: ₹15,000/month.<br>
          First month's interest = ₹10,00,000 × (0.09 / 12) = ₹7,500. Remaining ₹7,500 pays down principal.<br>
          Payoff Tenure = <strong>8 Years, 6 Months (102 Months)</strong>. Total Interest = <strong>₹5,20,450</strong>.
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: Accelerating Payoff with ₹20,000/month</strong><br>
          For the exact same ₹10,00,000 loan at 9.0%, increasing EMI to ₹20,000/month drops the payoff tenure to just <strong>5 Years, 5 Months (65 Months)</strong> and reduces total interest to ₹2,88,500—saving over ₹2,31,000 in interest!
        </div>

        <h3>Tips for Accelerated Debt Freedom</h3>
        <ul>
          <li><strong>Bi-weekly or round-up payments:</strong> Paying half your monthly payment every two weeks yields 26 half-payments (13 full payments per year), shaving years off long-term mortgages.</li>
          <li><strong>Apply tax refunds and bonuses:</strong> Directing annual performance bonuses straight to loan principal reduces the base balance on which future interest is compounded.</li>
          <li><strong>Beware the minimum threshold:</strong> Always pay well above the monthly interest cost so that meaningful sums attack the principal balance from day one.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">What happens if my entered monthly payment is too low?</div>
            <div class="faq-a">If your payment is less than or equal to one month's interest charge (Principal × Monthly Rate), the tool will alert you because the loan can never be amortized and debt would grow infinitely.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Are there prepayment penalties for paying off loans faster in India?</div>
            <div class="faq-a">According to Reserve Bank of India (RBI) directives, commercial banks cannot levy foreclosure charges or prepayment penalties on floating-rate individual home loans. Fixed-rate loans and personal loans may have minor prepayment terms.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How does tenure reduction compare to EMI reduction after prepaying?</div>
            <div class="faq-a">When making prepayments, banks offer two choices: keep tenure the same and reduce EMI, or keep EMI the same and reduce tenure. Keeping your EMI the same and reducing tenure saves vastly more interest over the long haul.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Does credit card debt follow this same formula?</div>
            <div class="faq-a">Yes. Credit cards carry much higher interest rates (36% to 42% p.a.). If you only make minimum 5% payments, payoff tenure often exceeds 15-20 years with astronomical interest costs.</div>
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

# 4. SALARY CALCULATOR
FINANCE_TOOLS_HTML["salary"] = """
    <!-- ==================== 19. SALARY CALCULATOR ==================== -->
    <section id="screen-salary" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Salary Calculator</h1>
        <p class="tool-page-subtitle">Calculate in-hand monthly take-home salary from your Annual Cost to Company (CTC) or Monthly Gross Pay with EPF and deductions.</p>
      </div>

      <div class="card">
        <h2 class="card-title">Salary Structure &amp; Deductions</h2>
        <div class="input-grid-2">
          <div class="input-group">
            <label>Salary Input Type</label>
            <div class="segmented-control">
              <button type="button" id="sal-type-ctc" class="segment-btn active" onclick="setSalInputType('ctc')">Annual CTC (₹/Year)</button>
              <button type="button" id="sal-type-monthly" class="segment-btn" onclick="setSalInputType('monthly')">Monthly Gross (₹/Month)</button>
            </div>
          </div>
          <div class="input-group">
            <label for="sal-amount" id="sal-amount-label">Annual CTC (₹)</label>
            <input type="number" id="sal-amount" value="1200000" min="50000" step="25000" oninput="calculateSalary()">
          </div>
        </div>

        <div class="input-grid-3">
          <div class="input-group">
            <label for="sal-basic-pct">Basic Salary (% of CTC/Gross)</label>
            <select id="sal-basic-pct" onchange="calculateSalary()">
              <option value="40">40% of Total Pay</option>
              <option value="50" selected>50% of Total Pay (Standard)</option>
              <option value="60">60% of Total Pay</option>
            </select>
          </div>
          <div class="input-group">
            <label for="sal-pf-type">Employee EPF Deduction</label>
            <select id="sal-pf-type" onchange="calculateSalary()">
              <option value="12" selected>12% of Basic (Standard EPF)</option>
              <option value="cap">Capped at ₹1,800/month</option>
              <option value="0">0% (Opt Out / Below Threshold)</option>
            </select>
          </div>
          <div class="input-group">
            <label for="sal-pt">Professional Tax (₹/Month)</label>
            <input type="number" id="sal-pt" value="200" min="0" max="1000" step="50" oninput="calculateSalary()">
          </div>
        </div>

        <div class="input-grid-2">
          <div class="input-group">
            <label for="sal-other-ded">Other Monthly Deductions (Insurance/NPS ₹)</label>
            <input type="number" id="sal-other-ded" value="1000" min="0" step="250" oninput="calculateSalary()">
          </div>
          <div class="input-group">
            <label for="sal-tax-est">Estimated Monthly TDS / Income Tax (₹)</label>
            <input type="number" id="sal-tax-est" value="5000" min="0" step="500" oninput="calculateSalary()">
          </div>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="calculateSalary()">Calculate In-Hand Salary</button>
          <button class="btn btn-outline" onclick="resetSalary()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="sal-results">
        <div class="stat-header">MONTHLY IN-HAND TAKE-HOME SALARY</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="sal-net-month-val">₹82,800</span>
          <span class="highlight-unit">Per Month In-Hand</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Annual Net Pay:</strong> <span id="sal-net-year-val">₹9,93,600</span></div>
          <div class="stat-pill"><strong>Total Monthly Deductions:</strong> <span id="sal-total-ded-val">₹17,200/mo</span></div>
        </div>
        <div class="result-grid-2">
          <div class="metric-box">
            <div class="metric-label">Monthly Gross Pay</div>
            <div class="metric-value" id="sal-res-gross">₹1,00,000</div>
            <div class="metric-sub">Base before deductions</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Employee EPF (12% Basic)</div>
            <div class="metric-value" id="sal-res-epf">₹6,000/mo</div>
            <div class="metric-sub">Transferred to retirement account</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Employer EPF (in CTC)</div>
            <div class="metric-value" id="sal-res-employer-epf">₹6,000/mo</div>
            <div class="metric-sub">Retirement matching contribution</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Statutory &amp; Tax Deductions</div>
            <div class="metric-value" id="sal-res-statutory">₹6,200/mo</div>
            <div class="metric-sub">PT + Insurance + Estimated TDS</div>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>Understanding CTC vs In-Hand Take-Home Salary in India</h2>
        <p>Receiving a job offer with an impressive <strong>Cost to Company (CTC)</strong> figure often creates excitement, but the actual sum credited to your bank account on payday—your <strong>net in-hand salary</strong>—is invariably smaller. CTC represents the total financial expense your employer incurs to hire and maintain you, which includes compulsory statutory contributions like Employee Provident Fund (EPF), gratuity provisions, group medical insurance, and payroll taxes.</p>

        <h3>How to Use This Salary Calculator</h3>
        <ol>
          <li>Choose whether you are starting with your <strong>Annual CTC</strong> (e.g. ₹12,00,000) or your <strong>Monthly Gross Pay</strong>.</li>
          <li>Select your <strong>Basic Salary proportion</strong> (usually 40% to 50% of CTC).</li>
          <li>Choose your <strong>EPF deduction structure</strong> (standard 12% of basic or the statutory cap of ₹1,800/month).</li>
          <li>Enter your state <strong>Professional Tax</strong> (typically ₹200/month across most Indian states).</li>
          <li>Specify any <strong>medical insurance premiums, voluntary NPS, or monthly TDS tax withholding</strong>.</li>
          <li>Click <strong>Calculate In-Hand Salary</strong> to see your monthly take-home salary and itemized deductions.</li>
        </ol>

        <h3>The Salary Breakdown Formula</h3>
        <p><code>Monthly Gross Pay = (Annual CTC − Employer PF − Annual Gratuity Provision) / 12</code></p>
        <p><code>Basic Salary = Monthly Gross × Basic% (typically 50%)</code></p>
        <p><code>Employee EPF = Basic Salary × 12% (or capped at ₹1,800)</code></p>
        <p><code>Total Deductions = Employee EPF + Professional Tax + Voluntary Deductions + Monthly TDS</code></p>
        <p><code>Net In-Hand Salary = Monthly Gross − Total Deductions</code></p>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: ₹12 Lakhs Annual CTC Offer</strong><br>
          Annual CTC: ₹12,00,000 | Monthly Gross: ₹1,00,000 | Basic: 50% (₹50,000).<br>
          Employee EPF (12% of ₹50k) = ₹6,000 | Professional Tax = ₹200 | Group Health = ₹1,000 | Estimated TDS = ₹10,000.<br>
          Monthly In-Hand = ₹1,00,000 − ₹17,200 = <strong>₹82,800</strong> (Annual Net: ₹9,93,600).
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: ₹6 Lakhs CTC with Capped EPF</strong><br>
          Annual CTC: ₹6,00,000 | Monthly Gross: ₹50,000 | Basic: 50% (₹25,000).<br>
          With capped EPF (₹1,800/mo) and PT (₹200/mo), monthly in-hand is approximately <strong>₹48,000</strong> before income tax.
        </div>

        <h3>Tips for Optimizing Your Salary Structure</h3>
        <ul>
          <li><strong>Maximize tax-exempt allowances:</strong> Take advantage of meal cards, fuel allowances, and gadget reimbursement components where offered by your company.</li>
          <li><strong>Understand employer PF in CTC:</strong> In India, employers generally include their matching 12% PF contribution inside your headline CTC figure.</li>
          <li><strong>Review Form 16 &amp; Tax Regime:</strong> Switching between the New and Old Tax Regimes can alter your monthly TDS withholding by several thousand rupees.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">What is the difference between Gross Salary and Net Salary?</div>
            <div class="faq-a">Gross Salary is the total compensation earned before any deductions. Net Salary (in-hand pay) is the final amount deposited into your bank account after subtracting EPF, Professional Tax, health insurance, and Income Tax (TDS).</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Is EPF mandatory for all employees in India?</div>
            <div class="faq-a">For private sector establishments with 20 or more employees, EPF is mandatory for employees with a basic salary up to ₹15,000/month. For higher basic salaries, employers and employees can agree to cap EPF at ₹1,800/month or contribute 12% on actual basic.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">What is Professional Tax?</div>
            <div class="faq-a">Professional Tax is a state-level levy on salaried individuals. It varies by state (e.g. Maharashtra, Karnataka, Tamil Nadu, West Bengal) with a statutory maximum ceiling of ₹2,500 per year (typically ₹200/month with ₹300 in February).</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Why does my take-home salary fluctuate in February or March?</div>
            <div class="faq-a">Employers reconcile your annual tax investment declarations (80C, 80D, rent receipts) in January-February. Any shortfall or excess tax withholding is adjusted in the final payroll months of the financial year.</div>
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

# 5. OVERTIME PAY CALCULATOR
FINANCE_TOOLS_HTML["overtime"] = """
    <!-- ==================== 20. OVERTIME PAY CALCULATOR ==================== -->
    <section id="screen-overtime" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Overtime Pay Calculator</h1>
        <p class="tool-page-subtitle">Calculate overtime earnings, 1.5x time-and-a-half, 2.0x double-time rates, and total gross paycheck wages.</p>
      </div>

      <div class="card">
        <h2 class="card-title">Wage &amp; Hours Worked</h2>
        <div class="input-grid-2">
          <div class="input-group">
            <label>Select Currency</label>
            <div class="segmented-control">
              <button type="button" id="ot-curr-inr" class="segment-btn active" onclick="setOtCurrency('INR')">Indian Rupee (₹ INR)</button>
              <button type="button" id="ot-curr-usd" class="segment-btn" onclick="setOtCurrency('USD')">US Dollar ($ USD)</button>
            </div>
          </div>
          <div class="input-group">
            <label for="ot-hourly-rate" id="ot-rate-label">Regular Hourly Rate (₹/hour)</label>
            <input type="number" id="ot-hourly-rate" value="250" min="1" step="5" oninput="calculateOvertime()">
          </div>
        </div>

        <div class="input-grid-3">
          <div class="input-group">
            <label for="ot-reg-hours">Regular Hours Worked</label>
            <input type="number" id="ot-reg-hours" value="40" min="0" max="168" step="0.5" oninput="calculateOvertime()">
          </div>
          <div class="input-group">
            <label for="ot-15-hours">1.5x Overtime Hours (Time &amp; Half)</label>
            <input type="number" id="ot-15-hours" value="10" min="0" max="100" step="0.5" oninput="calculateOvertime()">
          </div>
          <div class="input-group">
            <label for="ot-20-hours">2.0x Overtime Hours (Double Time)</label>
            <input type="number" id="ot-20-hours" value="4" min="0" max="100" step="0.5" oninput="calculateOvertime()">
          </div>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="calculateOvertime()">Calculate Overtime</button>
          <button class="btn btn-outline" onclick="resetOvertime()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="ot-results">
        <div class="stat-header">TOTAL GROSS PAYCHECK</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="ot-total-pay-val">₹15,750</span>
          <span class="highlight-unit" id="ot-total-hours-val">54 Total Hours</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Total Overtime Premium:</strong> <span id="ot-total-ot-val">₹5,750</span></div>
          <div class="stat-pill"><strong>Effective Blended Rate:</strong> <span id="ot-blended-rate-val">₹291.67/hr</span></div>
        </div>
        <div class="result-grid-2">
          <div class="metric-box">
            <div class="metric-label">Regular Base Pay</div>
            <div class="metric-value" id="ot-res-reg">₹10,000</div>
            <div class="metric-sub">40 hrs @ ₹250.00/hr</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">1.5x Overtime Pay</div>
            <div class="metric-value" id="ot-res-15">₹3,750</div>
            <div class="metric-sub">10 hrs @ ₹375.00/hr</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">2.0x Double Time Pay</div>
            <div class="metric-value" id="ot-res-20">₹2,000</div>
            <div class="metric-sub">4 hrs @ ₹500.00/hr</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Overtime Share of Paycheck</div>
            <div class="metric-value" id="ot-res-share">36.51%</div>
            <div class="metric-sub">Premium boost to regular wages</div>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>How Overtime Wages and Shift Multipliers Are Calculated</h2>
        <p>Overtime pay compensates employees for working hours beyond their standard weekly or daily threshold. In most labor jurisdictions globally (such as the US FLSA and Indian Factories Act, 1948), non-exempt workers who work beyond standard hours (typically 40 or 48 hours per week) are legally entitled to premium rates. The most prevalent multipliers are <strong>time-and-a-half (1.5x)</strong> for standard overtime and <strong>double-time (2.0x)</strong> for weekend shifts, statutory public holidays, or excessive consecutive work days.</p>

        <h3>How to Use This Overtime Pay Calculator</h3>
        <ol>
          <li>Choose your currency: <strong>₹ INR</strong> or <strong>$ USD</strong>.</li>
          <li>Enter your <strong>Regular Hourly Pay Rate</strong>.</li>
          <li>Enter your <strong>Regular Hours</strong> worked (typically 40 hours per workweek).</li>
          <li>Enter any <strong>1.5x Overtime Hours</strong> worked.</li>
          <li>Enter any <strong>2.0x Double-Time Hours</strong> worked (holidays, Sundays, night shifts).</li>
          <li>Click <strong>Calculate Overtime</strong> to review your total paycheck, overtime premium, and blended hourly rate.</li>
        </ol>

        <h3>The Overtime Formulas</h3>
        <p><code>Regular Pay = Regular Hours × Base Rate</code></p>
        <p><code>Time-and-a-Half Pay (1.5x) = Overtime Hours × (Base Rate × 1.5)</code></p>
        <p><code>Double-Time Pay (2.0x) = Double-Time Hours × (Base Rate × 2.0)</code></p>
        <p><code>Total Gross Pay = Regular Pay + 1.5x Pay + 2.0x Pay</code></p>
        <p><code>Effective Hourly Rate = Total Gross Pay / Total Hours Worked</code></p>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: Warehouse Shift Worker (INR ₹)</strong><br>
          Base Rate: ₹250/hour | Regular: 40 hrs | 1.5x OT: 10 hrs | 2.0x Sunday OT: 4 hrs.<br>
          Regular Pay = 40 × ₹250 = ₹10,000.<br>
          1.5x Pay = 10 × (₹250 × 1.5) = 10 × ₹375 = ₹3,750.<br>
          2.0x Pay = 4 × (₹250 × 2.0) = 4 × ₹500 = ₹2,000.<br>
          Total Gross Pay = <strong>₹15,750</strong> (Total: 54 hours, Blended Rate: ₹291.67/hr).
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: Healthcare Professional (USD $)</strong><br>
          Base Rate: $30.00/hour | Regular: 40 hrs | 1.5x OT: 8 hrs.<br>
          Regular Pay = $1,200.00. Overtime Pay = 8 × $45.00 = $360.00.<br>
          Total Paycheck = <strong>$1,560.00</strong>.
        </div>

        <h3>Important Overtime Tips for Employees &amp; Contractors</h3>
        <ul>
          <li><strong>Track clock-in/out times precisely:</strong> Keep an independent digital log of your shift punches to cross-check with monthly pay stubs.</li>
          <li><strong>Verify your salaried exemption status:</strong> Not all salaried employees are exempt from overtime; check local labor laws regarding duties tests and salary caps.</li>
          <li><strong>Factoring in taxes:</strong> Overtime is taxed at your regular marginal tax bracket—it does not get penalized with a special higher tax rate, although higher gross earnings may push a portion into a higher tier.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">What is the statutory overtime rule in India?</div>
            <div class="faq-a">Under Section 59 of the Factories Act 1948 and state Shops &amp; Commercial Establishments Acts, an employee who works more than 9 hours in any day or more than 48 hours in any week is entitled to wages at twice their ordinary rate of pay (2.0x).</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How do I find my hourly rate if I earn a monthly salary?</div>
            <div class="faq-a">Divide your monthly base salary by the total standard working hours in a month (usually 160 hours for 40 hours/week, or 192 hours for 48 hours/week): Hourly Rate = Monthly Salary / Standard Monthly Hours.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Is working on a public holiday always double time?</div>
            <div class="faq-a">In many contracts and collective bargaining agreements, national holidays are paid at 2.0x (double time) or accompanied by a compensatory off day in lieu. Check your employment handbook.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can overtime be paid as compensatory time off instead of cash?</div>
            <div class="faq-a">Some jurisdictions and public sector organizations allow comp-time in lieu of cash wages, typically at the same 1.5 hours of paid time off per 1 hour of overtime worked.</div>
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

# 6. TAX CALCULATOR
FINANCE_TOOLS_HTML["tax"] = """
    <!-- ==================== 21. TAX CALCULATOR ==================== -->
    <section id="screen-tax" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Tax Calculator</h1>
        <p class="tool-page-subtitle">Compare Indian Income Tax liability under the New Tax Regime vs Old Tax Regime with standard deduction, Section 87A rebate, and 4% cess.</p>
      </div>

      <div class="card">
        <h2 class="card-title">Income &amp; Tax Deductions</h2>
        <div class="input-grid-2">
          <div class="input-group">
            <label for="tax-income">Annual Gross Taxable Income (₹)</label>
            <input type="number" id="tax-income" value="1200000" min="100000" step="25000" oninput="calculateTax()">
          </div>
          <div class="input-group">
            <label for="tax-age">Age Category</label>
            <select id="tax-age" onchange="calculateTax()">
              <option value="general" selected>Individual below 60 Years</option>
              <option value="senior">Senior Citizen (60 - 79 Years)</option>
              <option value="super">Super Senior Citizen (80+ Years)</option>
            </select>
          </div>
        </div>

        <div class="card-title" style="font-size: 0.95rem; margin-top: 10px; margin-bottom: 8px;">Old Tax Regime Deductions (Optional)</div>
        <div class="input-grid-3">
          <div class="input-group">
            <label for="tax-80c">Section 80C Deductions (Max ₹1.5L)</label>
            <input type="number" id="tax-80c" value="150000" min="0" max="150000" step="10000" oninput="calculateTax()">
          </div>
          <div class="input-group">
            <label for="tax-80d">Section 80D Health Insurance (₹)</label>
            <input type="number" id="tax-80d" value="25000" min="0" max="100000" step="5000" oninput="calculateTax()">
          </div>
          <div class="input-group">
            <label for="tax-hra">HRA Exemption / Home Loan (₹)</label>
            <input type="number" id="tax-hra" value="100000" min="0" step="10000" oninput="calculateTax()">
          </div>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="calculateTax()">Calculate Income Tax</button>
          <button class="btn btn-outline" onclick="resetTax()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="tax-results">
        <div class="stat-header">TAX REGIME COMPARISON</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="tax-better-regime-val">New Regime is Better</span>
          <span class="highlight-unit" id="tax-savings-diff-val">Saves ₹14,300</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>New Regime Tax:</strong> <span id="tax-new-total-val">₹85,800</span></div>
          <div class="stat-pill"><strong>Old Regime Tax:</strong> <span id="tax-old-total-val">₹1,00,100</span></div>
        </div>
        <div class="result-grid-2">
          <div class="metric-box">
            <div class="metric-label">New Regime Taxable Income</div>
            <div class="metric-value" id="tax-new-taxable">₹11,25,000</div>
            <div class="metric-sub">After ₹75,000 Standard Deduction</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Old Regime Taxable Income</div>
            <div class="metric-value" id="tax-old-taxable">₹8,75,000</div>
            <div class="metric-sub">After ₹50k Std Ded + 80C + 80D + HRA</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">New Regime Effective Rate</div>
            <div class="metric-value" id="tax-new-eff-rate">7.15%</div>
            <div class="metric-sub">Total Tax ÷ Gross Income</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Old Regime Effective Rate</div>
            <div class="metric-value" id="tax-old-eff-rate">8.34%</div>
            <div class="metric-sub">Total Tax ÷ Gross Income</div>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>Indian Income Tax: New vs Old Tax Regime Slabs &amp; Rules</h2>
        <p>In India, taxpayers can choose each financial year between two distinct income tax frameworks: the <strong>New Tax Regime</strong> (default under Section 115BAC, offering lower slab rates with an enhanced ₹75,000 standard deduction and full Section 87A rebate up to ₹7 Lakhs taxable income) and the <strong>Old Tax Regime</strong> (which maintains traditional deductions such as Section 80C, 80D health insurance, HRA, home loan interest, and NPS contributions).</p>

        <h3>How to Use This Tax Calculator</h3>
        <ol>
          <li>Enter your total <strong>Annual Gross Taxable Income</strong> from salary, freelancing, or business.</li>
          <li>Select your <strong>Age Category</strong> (General, Senior Citizen, or Super Senior).</li>
          <li>Enter any eligible deductions for the Old Regime: <strong>Section 80C</strong> (EPF, PPF, ELSS, life insurance), <strong>Section 80D</strong> (health insurance), and <strong>HRA/Home Loan Interest</strong>.</li>
          <li>Click <strong>Calculate Income Tax</strong> to see an instant side-by-side comparison revealing which regime saves you more money.</li>
        </ol>

        <h3>Current Tax Slabs Overview (FY 2024-25 / FY 2025-26)</h3>
        <p><strong>New Tax Regime Slabs:</strong></p>
        <ul>
          <li>Up to ₹3,00,000: Nil (0%)</li>
          <li>₹3,00,001 to ₹7,00,000: 5% (Eligible for full 87A rebate up to ₹7,00,000 taxable income)</li>
          <li>₹7,00,001 to ₹10,00,000: 10%</li>
          <li>₹10,00,001 to ₹12,00,000: 15%</li>
          <li>₹12,00,001 to ₹15,00,000: 20%</li>
          <li>Above ₹15,00,000: 30%</li>
          <li><em>Standard Deduction:</em> ₹75,000 for salaried employees. 4% Health &amp; Education Cess applies to all tax.</li>
        </ul>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: Salaried Professional at ₹12 Lakhs Income</strong><br>
          Gross: ₹12,00,000. Deductions: 80C (₹1.5L), 80D (₹25k), HRA (₹1.0L).<br>
          <strong>New Regime:</strong> Taxable = ₹12,00,000 − ₹75,000 = ₹11,25,000. Tax + Cess = <strong>₹85,800</strong>.<br>
          <strong>Old Regime:</strong> Taxable = ₹12,00,000 − (₹50k + ₹1.5L + ₹25k + ₹1.0L) = ₹8,75,000. Tax + Cess = <strong>₹1,00,100</strong>.<br>
          <em>Outcome:</em> New Regime saves <strong>₹14,300</strong>!
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: ₹7.5 Lakhs Salary (Zero Tax in New Regime)</strong><br>
          With ₹75,000 standard deduction, taxable income becomes ₹6,75,000. Because it is under ₹7,00,000, Section 87A tax rebate reduces the tax to <strong>₹0 (Zero Tax)</strong>!
        </div>

        <h3>Tips for Indian Tax Planning</h3>
        <ul>
          <li><strong>Calculate the breakeven threshold:</strong> If your total deductions (80C + 80D + HRA + Home Loan) exceed approximately ₹3,75,000, the Old Regime generally yields lower tax. Below that, the New Regime is almost always better.</li>
          <li><strong>Remember the 4% Cess:</strong> All income tax liabilities in India include a mandatory 4% Health and Education Cess added to the computed base tax.</li>
          <li><strong>Select your regime when filing ITR:</strong> Salaried individuals can switch between regimes every year at the time of filing their ITR-1 or ITR-2 before the July 31 deadline.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">What is the Section 87A tax rebate?</div>
            <div class="faq-a">Section 87A provides a tax rebate for lower-to-middle income earners. Under the New Tax Regime, if your taxable income after standard deduction does not exceed ₹7,00,000, your tax liability is reduced to zero.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Is Standard Deduction available to business owners?</div>
            <div class="faq-a">No. The Standard Deduction (₹75,000 in New Regime, ₹50,000 in Old Regime) is exclusively available to salaried employees and pensioners. Business owners deduct actual documented business expenses instead.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can I claim HRA in the New Tax Regime?</div>
            <div class="faq-a">No. House Rent Allowance (HRA), Leave Travel Allowance (LTA), and Section 80C deductions are not permitted under the New Tax Regime. They are available only in the Old Tax Regime.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can I switch regimes if I have business income?</div>
            <div class="faq-a">Individuals with business or professional income (filing ITR-3 or ITR-4) can opt out of the New Regime once, but once they switch back, they cannot change regimes again unless their business income ceases.</div>
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

print("tools_html_finance.py created successfully with Tools 1-6.")
