# tools_html_shopping.py
# HTML sections for Tools 18-20: Tip Calculator, Discount + Final Price Calculator, Sales Tax Calculator

SHOPPING_TOOLS_HTML = {}

# 18. TIP CALCULATOR
SHOPPING_TOOLS_HTML["tip"] = """
    <!-- ==================== 33. TIP CALCULATOR ==================== -->
    <section id="screen-tip" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Tip Calculator</h1>
        <p class="tool-page-subtitle">Calculate restaurant tips, service gratuities, custom percentage additions, and fair bill splits per person in INR (₹) or USD ($).</p>
      </div>

      <div class="card">
        <h2 class="card-title">Bill &amp; Gratuity Details</h2>
        <div class="input-grid-2">
          <div class="input-group">
            <label>Select Currency</label>
            <div class="segmented-control">
              <button type="button" id="tip-curr-inr" class="segment-btn active" onclick="setTipCurrency('INR')">Indian Rupee (₹ INR)</button>
              <button type="button" id="tip-curr-usd" class="segment-btn" onclick="setTipCurrency('USD')">US Dollar ($ USD)</button>
            </div>
          </div>
          <div class="input-group">
            <label for="tip-bill" id="tip-bill-label">Bill Amount (₹)</label>
            <input type="number" id="tip-bill" value="1850" min="1" step="10" oninput="calculateTip()">
          </div>
        </div>

        <div class="input-group">
          <label>Tip Percentage Preset</label>
          <div class="segmented-control" style="flex-wrap: wrap;">
            <button type="button" class="segment-btn" onclick="setTipPreset(5)">5%</button>
            <button type="button" class="segment-btn active" id="tip-pre-10" onclick="setTipPreset(10)">10%</button>
            <button type="button" class="segment-btn" onclick="setTipPreset(15)">15%</button>
            <button type="button" class="segment-btn" onclick="setTipPreset(18)">18%</button>
            <button type="button" class="segment-btn" onclick="setTipPreset(20)">20%</button>
          </div>
        </div>

        <div class="input-grid-2">
          <div class="input-group">
            <label for="tip-custom-pct">Tip Percentage (%)</label>
            <input type="number" id="tip-custom-pct" value="10" min="0" max="100" step="1" oninput="calculateTip()">
          </div>
          <div class="input-group">
            <label for="tip-people">Number of People (Split)</label>
            <input type="number" id="tip-people" value="3" min="1" max="100" step="1" oninput="calculateTip()">
          </div>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="calculateTip()">Calculate Tip</button>
          <button class="btn btn-outline" onclick="resetTip()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="tip-results">
        <div class="stat-header">TOTAL PER PERSON (BILL + TIP)</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="tip-per-person-val">₹678.33</span>
          <span class="highlight-unit">Per Guest</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Total Bill with Tip:</strong> <span id="tip-grand-total-val">₹2,035.00</span></div>
          <div class="stat-pill"><strong>Total Gratuity Added:</strong> <span id="tip-total-amount-val">₹185.00</span></div>
        </div>
        <div class="result-grid-2">
          <div class="metric-box">
            <div class="metric-label">Tip Per Person</div>
            <div class="metric-value" id="tip-res-tip-each">₹61.67</div>
            <div class="metric-sub">Individual tip contribution</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Base Bill Per Person</div>
            <div class="metric-value" id="tip-res-base-each">₹616.67</div>
            <div class="metric-sub">Without tip (Bill ÷ Guests)</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Rounded Total per Person</div>
            <div class="metric-value" id="tip-res-rounded">₹680.00</div>
            <div class="metric-sub">Easy cash settling amount</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Effective Gratuity Rate</div>
            <div class="metric-value" id="tip-res-effective-pct">10.00%</div>
            <div class="metric-sub">On pre-tip subtotal</div>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>Tipping Etiquette and Bill Splitting Guidelines</h2>
        <p>Whether dining out with friends at a restaurant, taking a cab, or getting food delivered, knowing how much to tip and how to divide the bill evenly is an essential social and financial skill. Tipping practices vary around the globe: while North American culture customarily expects 15% to 20% gratuity, dining culture in India and Europe often favors 5% to 10% discretionary tipping, provided service charge has not already been levied on the receipt.</p>

        <h3>How to Use This Tip Calculator</h3>
        <ol>
          <li>Choose your currency: <strong>₹ INR</strong> or <strong>$ USD</strong>.</li>
          <li>Enter the total <strong>Bill Amount</strong> shown on your receipt.</li>
          <li>Tap one of the quick preset percentage chips (5%, 10%, 15%, 18%, 20%) or type a custom percentage.</li>
          <li>Enter the <strong>Number of People</strong> sharing the meal.</li>
          <li>Click <strong>Calculate Tip</strong> to see the grand total, tip amount, and exact split per person.</li>
        </ol>

        <h3>The Gratuity Calculation Formulas</h3>
        <p><code>Total Tip = Bill Amount × (Tip Percentage / 100)</code></p>
        <p><code>Grand Total = Bill Amount + Total Tip</code></p>
        <p><code>Tip Per Person = Total Tip / Number of People</code></p>
        <p><code>Total Per Person = Grand Total / Number of People</code></p>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: Dinner with Friends in India (INR ₹)</strong><br>
          Restaurant Bill: ₹1,850 | Tip: 10% | Diners: 3 people.<br>
          Tip Amount = ₹1,850 × 0.10 = ₹185. Grand Total = ₹2,035.<br>
          Per Person = ₹2,035 / 3 = <strong>₹678.33 per person</strong>.
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: US Business Lunch (USD $)</strong><br>
          Lunch Bill: $84.00 | Tip: 18% | Diners: 2 colleagues.<br>
          Tip = $84.00 × 0.18 = $15.12. Total = $99.12.<br>
          Per Person = <strong>$49.56</strong>.
        </div>

        <h3>Useful Tipping Tips</h3>
        <ul>
          <li><strong>Inspect the bill for "Service Charge":</strong> In India, the Central Consumer Protection Authority (CCPA) issued guidelines stating that service charges are strictly voluntary. If an automatic 10% service charge is already added, you do not need to add an additional tip.</li>
          <li><strong>Tip on the pre-tax amount:</strong> Standard tipping etiquette recommends applying your tip percentage to the food &amp; beverage subtotal before GST or sales tax is applied.</li>
          <li><strong>Round up for cash ease:</strong> When paying cash, rounding each person's share to the nearest ₹10 or $1 eliminates awkward coin exchanges.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">What is the standard tip percentage in India?</div>
            <div class="faq-a">In casual dining and cafes in India, tipping 5% to 10% is customary for attentive service. In fine-dining restaurants where no service charge is billed, 10% is standard.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">What is the difference between Service Tax, Service Charge, and Tip?</div>
            <div class="faq-a">Service Tax was an old government tax (now replaced by GST). Service Charge is an optional restaurant fee retained by the management. A Tip is a voluntary discretionary gift given directly to service staff for pleasant hospitality.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Should you tip for takeout or counter service?</div>
            <div class="faq-a">Tipping on takeout is optional. A small tip (5-10% or loose change) is appreciated for complex packaging or special orders, but not strictly expected.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can this calculator split a bill unevenly?</div>
            <div class="faq-a">This calculator divides the bill equally across all diners. If someone ordered significantly more expensive items, calculate their individual subtotal first with their proportional tip share.</div>
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

# 19. DISCOUNT + FINAL PRICE CALCULATOR
SHOPPING_TOOLS_HTML["discount-final-price"] = """
    <!-- ==================== 34. DISCOUNT + FINAL PRICE CALCULATOR ==================== -->
    <section id="screen-discount-final-price" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Discount + Final Price Calculator</h1>
        <p class="tool-page-subtitle">Calculate stacked / double promotional discounts (e.g., 30% off + extra 15% coupon) with optional sales tax and net savings.</p>
      </div>

      <div class="card">
        <h2 class="card-title">Promotional Sale Details</h2>
        <div class="input-grid-2">
          <div class="input-group">
            <label>Select Currency</label>
            <div class="segmented-control">
              <button type="button" id="dfp-curr-inr" class="segment-btn active" onclick="setDfpCurrency('INR')">Indian Rupee (₹ INR)</button>
              <button type="button" id="dfp-curr-usd" class="segment-btn" onclick="setDfpCurrency('USD')">US Dollar ($ USD)</button>
            </div>
          </div>
          <div class="input-group">
            <label for="dfp-original-price" id="dfp-price-label">Original Tag Price (₹)</label>
            <input type="number" id="dfp-original-price" value="2500" min="1" step="50" oninput="calculateDiscountFinalPrice()">
          </div>
        </div>

        <div class="input-grid-3">
          <div class="input-group">
            <label for="dfp-disc1">Primary Store Discount (%)</label>
            <input type="number" id="dfp-disc1" value="30" min="0" max="100" step="1" oninput="calculateDiscountFinalPrice()">
          </div>
          <div class="input-group">
            <label for="dfp-disc2">Extra / Stacked Discount (%)</label>
            <input type="number" id="dfp-disc2" value="10" min="0" max="100" step="1" oninput="calculateDiscountFinalPrice()">
            <span style="font-size: 0.78rem; color: var(--text-muted);">E.g. Coupon, membership, or credit card cashback</span>
          </div>
          <div class="input-group">
            <label for="dfp-tax-pct">Sales Tax / GST Rate (%)</label>
            <input type="number" id="dfp-tax-pct" value="12" min="0" max="100" step="0.5" oninput="calculateDiscountFinalPrice()">
            <span style="font-size: 0.78rem; color: var(--text-muted);">Set to 0% if price is tax-inclusive</span>
          </div>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="calculateDiscountFinalPrice()">Calculate Final Price</button>
          <button class="btn btn-outline" onclick="resetDiscountFinalPrice()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="dfp-results">
        <div class="stat-header">FINAL CHECKOUT AMOUNT</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="dfp-final-price-val">₹1,764.00</span>
          <span class="highlight-unit">Final Payable</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Total Money Saved:</strong> <span id="dfp-total-saved-val">₹925.00</span></div>
          <div class="stat-pill"><strong>Effective Discount:</strong> <span id="dfp-effective-pct-val">37.00% Off</span></div>
        </div>
        <div class="result-grid-2">
          <div class="metric-box">
            <div class="metric-label">Price After Primary 30% Off</div>
            <div class="metric-value" id="dfp-res-step1">₹1,750.00</div>
            <div class="metric-sub">Saves ₹750.00 in Step 1</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Price After Extra 10% Coupon</div>
            <div class="metric-value" id="dfp-res-step2">₹1,575.00</div>
            <div class="metric-sub">Saves ₹175.00 extra in Step 2</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Sales Tax / GST Added</div>
            <div class="metric-value" id="dfp-res-tax-amount">+₹189.00</div>
            <div class="metric-sub">12% tax on ₹1,575.00</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Total Percentage Paid</div>
            <div class="metric-value" id="dfp-res-paid-pct">70.56%</div>
            <div class="metric-sub">Of original list price</div>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>The Truth About Stacked Discounts: Why 30% + 10% Does NOT Equal 40%</h2>
        <p>Retail stores and e-commerce shopping portals often advertise promotions with compounding promotions: <em>"30% off storewide PLUS take an additional 10% off at checkout with code SAVE10!"</em> Many shoppers mistakenly assume they are getting 40% off the original price. However, successive discounts apply sequentially: the second discount is applied only to the <strong>already reduced price</strong>, resulting in an effective 37% discount rather than 40%.</p>

        <h3>How to Use This Discount + Final Price Calculator</h3>
        <ol>
          <li>Enter the original <strong>Tag Price</strong> of the merchandise.</li>
          <li>Enter the <strong>Primary Discount Percentage</strong> (e.g. 30%).</li>
          <li>Enter any <strong>Additional Stacked Discount</strong> (e.g. 10% coupon code or loyalty rebate).</li>
          <li>Specify the <strong>Sales Tax / GST percentage</strong> to be added at checkout (or leave as 0% if prices are tax-inclusive).</li>
          <li>Click <strong>Calculate Final Price</strong> to see the exact checkout price, total rupee or dollar savings, and the true effective discount rate.</li>
        </ol>

        <h3>Mathematical Formula for Successive Discounts</h3>
        <p><code>Price 1 = Original Price × (1 − (Discount 1 / 100))</code></p>
        <p><code>Price 2 = Price 1 × (1 − (Discount 2 / 100))</code></p>
        <p><code>Effective Combined Discount (%) = 100 − [(100 − D1) × (100 − D2) / 100]</code></p>
        <p><code>Tax Amount = Price 2 × (Tax Rate / 100)</code></p>
        <p><code>Final Price = Price 2 + Tax Amount</code></p>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: Designer Jacket Sale (INR ₹)</strong><br>
          Tag Price: ₹2,500 | Store Sale: 30% off | App Coupon: Extra 10% off | GST: 12%.<br>
          Step 1: ₹2,500 − 30% (₹750) = ₹1,750.<br>
          Step 2: ₹1,750 − 10% (₹175) = ₹1,575.<br>
          Effective Discount = <strong>37% off</strong> (saving ₹925 before tax).<br>
          Step 3: Add 12% GST (+₹189) = <strong>₹1,764.00 Final Checkout Price</strong>.
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: 50% + 50% Trap</strong><br>
          Original: $100. First 50% drops it to $50. Second 50% drops it to $25.<br>
          Final price is <strong>$25 (75% off)</strong>, NOT free ($0)!
        </div>

        <h3>Tips for Smart Shopping</h3>
        <ul>
          <li><strong>Evaluate the true effective discount:</strong> Whenever you see "take an extra X% off already discounted items", calculate the true net percentage before purchasing.</li>
          <li><strong>Watch for tax on discounted vs original price:</strong> By law in most jurisdictions, sales tax / GST is assessed on the final discounted sale price, not the original MSRP.</li>
          <li><strong>Compare minimum threshold coupons:</strong> If a coupon requires a ₹2,000 cart minimum to save ₹200, purchasing ₹400 of unwanted goods just to unlock the coupon actually costs you more.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">Does the order of successive discounts matter?</div>
            <div class="faq-a">No! By the commutative property of multiplication, 30% off followed by 10% off results in the exact same final price as 10% off followed by 30% off: (0.70 × 0.90 = 0.63, or 37% total discount).</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">What is 20% off plus an extra 20% off?</div>
            <div class="faq-a">20% off leaves 80% of the price. Taking 20% off that 80% leaves 64% of the original price, which equals an effective discount of 36% off (not 40%).</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How does GST apply to retail MRP in India?</div>
            <div class="faq-a">In India, the Maximum Retail Price (MRP) printed on packaged consumer goods is legally required to be inclusive of all taxes. However, e-commerce listings sometimes display pre-tax prices with GST calculated at final checkout.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can I use this calculator for single discounts?</div>
            <div class="faq-a">Yes. Simply leave the Extra Discount field at 0% to use it as a standard single-discount calculator with tax.</div>
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

# 20. SALES TAX CALCULATOR
SHOPPING_TOOLS_HTML["sales-tax"] = """
    <!-- ==================== 35. SALES TAX CALCULATOR ==================== -->
    <section id="screen-sales-tax" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Sales Tax Calculator</h1>
        <p class="tool-page-subtitle">Add sales tax to pre-tax amounts or reverse-calculate pre-tax list price and tax amounts from tax-inclusive retail totals.</p>
      </div>

      <div class="card">
        <h2 class="card-title">Sales Tax Computation</h2>
        <div class="input-grid-2">
          <div class="input-group">
            <label>Select Currency</label>
            <div class="segmented-control">
              <button type="button" id="st-curr-inr" class="segment-btn active" onclick="setStCurrency('INR')">Indian Rupee (₹ INR)</button>
              <button type="button" id="st-curr-usd" class="segment-btn" onclick="setStCurrency('USD')">US Dollar ($ USD)</button>
            </div>
          </div>
          <div class="input-group">
            <label>Calculation Direction</label>
            <div class="segmented-control">
              <button type="button" id="st-mode-add" class="segment-btn active" onclick="setStMode('add')">Add Tax (Tax Exclusive)</button>
              <button type="button" id="st-mode-extract" class="segment-btn" onclick="setStMode('extract')">Reverse / Remove Tax (Tax Inclusive)</button>
            </div>
          </div>
        </div>

        <div class="input-grid-2">
          <div class="input-group">
            <label for="st-amount" id="st-amount-label">Net Pre-Tax Amount (₹)</label>
            <input type="number" id="st-amount" value="5000" min="0" step="100" oninput="calculateSalesTax()">
          </div>
          <div class="input-group">
            <label for="st-tax-rate">Sales Tax Rate (%)</label>
            <input type="number" id="st-tax-rate" value="8.25" min="0" max="100" step="0.25" oninput="calculateSalesTax()">
          </div>
        </div>

        <div class="btn-row">
          <button class="btn btn-primary" onclick="calculateSalesTax()">Calculate Sales Tax</button>
          <button class="btn btn-outline" onclick="resetSalesTax()">Reset</button>
        </div>
      </div>

      <!-- Results Card -->
      <div class="card result-card" id="st-results">
        <div class="stat-header">TOTAL GROSS PRICE (WITH TAX)</div>
        <div class="stat-highlight">
          <span class="highlight-number" id="st-gross-val">₹5,412.50</span>
          <span class="highlight-unit">Final Amount</span>
        </div>
        <div class="stats-pills-row">
          <div class="stat-pill"><strong>Sales Tax Amount:</strong> <span id="st-tax-amount-val">₹412.50</span></div>
          <div class="stat-pill"><strong>Pre-Tax Net:</strong> <span id="st-net-val">₹5,000.00</span></div>
        </div>
        <div class="result-grid-2">
          <div class="metric-box">
            <div class="metric-label">Sales Tax Percentage</div>
            <div class="metric-value" id="st-res-tax-pct">8.25%</div>
            <div class="metric-sub">Applied tax levy rate</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Tax Multiplier Factor</div>
            <div class="metric-value" id="st-res-multiplier">1.0825</div>
            <div class="metric-sub">Gross price multiplier</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">Tax Share of Gross Price</div>
            <div class="metric-value" id="st-res-share">7.62%</div>
            <div class="metric-sub">Tax as % of final retail total</div>
          </div>
          <div class="metric-box">
            <div class="metric-label">State / City Surcharge</div>
            <div class="metric-value" id="st-res-state-sub">Included</div>
            <div class="metric-sub">Full statutory levy</div>
          </div>
        </div>
      </div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2>Understanding Sales Tax: Exclusive vs Inclusive Calculations</h2>
        <p>Sales tax is a consumption tax charged on the sale of retail goods and services. Depending on the nation and local jurisdiction, sales tax may be either <strong>exclusive</strong> (added to the price tag at the register, standard across the United States and Canada) or <strong>inclusive</strong> (embedded within the displayed shelf price, standard for Value Added Tax [VAT] and GST in Europe, Australia, and India). Knowing how to calculate both forward and in reverse is indispensable for accounting, invoicing, and auditing.</p>

        <h3>How to Use This Sales Tax Calculator</h3>
        <ol>
          <li>Select your currency (<strong>₹ INR</strong> or <strong>$ USD</strong>).</li>
          <li>Choose your calculation mode: <strong>Add Tax</strong> (if starting with pre-tax price) or <strong>Remove Tax</strong> (if starting with the total checkout price).</li>
          <li>Enter the dollar or rupee amount.</li>
          <li>Enter the local sales tax rate percentage (e.g. 5%, 8.25%, 18%).</li>
          <li>Click <strong>Calculate Sales Tax</strong> to view the pre-tax base, exact tax dollar amount, and total gross cost.</li>
        </ol>

        <h3>The Sales Tax Formulas</h3>
        <p><strong>1. Forward Calculation (Adding Sales Tax):</strong></p>
        <p><code>Tax Amount = Net Pre-Tax Amount × (Tax Rate / 100)</code></p>
        <p><code>Gross Total = Net Pre-Tax Amount + Tax Amount</code></p>
        <p><strong>2. Reverse Calculation (Extracting Embedded Sales Tax):</strong></p>
        <p><code>Net Pre-Tax Amount = Gross Total / (1 + (Tax Rate / 100))</code></p>
        <p><code>Tax Amount = Gross Total − Net Pre-Tax Amount</code></p>

        <h3>Practical Examples</h3>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 1: US Retail Purchase (Adding Tax)</strong><br>
          Shelf Price: $500.00 | Local Sales Tax Rate: 8.25% (e.g. California / Texas).<br>
          Tax Amount = $500.00 × 0.0825 = <strong>$41.25</strong>.<br>
          Final Checkout Total = <strong>$541.25</strong>.
        </div>
        <div class="example-box" style="background: var(--bg-color); border: 1px solid var(--surface-border); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
          <strong>Example 2: Reverse Tax Extraction (Indian Consulting Invoice)</strong><br>
          Total Receipt Amount: ₹11,800 | GST Rate: 18%.<br>
          Pre-Tax Base = ₹11,800 / (1 + 0.18) = ₹11,800 / 1.18 = <strong>₹10,000.00</strong>.<br>
          Embedded Sales Tax = ₹11,800 − ₹10,000 = <strong>₹1,800.00</strong>.
        </div>

        <h3>Tips for Businesses and Consumers</h3>
        <ul>
          <li><strong>Never calculate reverse tax with simple subtraction:</strong> Subtracting 18% from ₹11,800 gives ₹9,676 (wrong!). You must divide by 1.18 to determine the true pre-tax base of ₹10,000.</li>
          <li><strong>Tax exemptions and holidays:</strong> Many US states offer annual sales tax holidays on school supplies, apparel, and energy-efficient appliances where tax rates drop to 0%.</li>
        </ul>

        <h3>Frequently Asked Questions</h3>
        <div class="faq-group">
          <div class="faq-item">
            <div class="faq-q">What is the difference between Sales Tax and VAT / GST?</div>
            <div class="faq-a">Sales tax is a single-stage tax levied only at the final point of sale to the end consumer. Value Added Tax (VAT) and Goods &amp; Services Tax (GST) are multi-stage taxes collected at each step of the supply chain with input tax credits.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Why does sales tax vary so much between cities in the United States?</div>
            <div class="faq-a">In the US, there is no federal sales tax. Instead, individual states, counties, and municipal cities set their own combined local sales taxes, ranging from 0% (Delaware, Oregon, Montana, New Hampshire) to over 10% (parts of California, Louisiana, Tennessee).</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How do I back-calculate the tax rate if I only have pre-tax and post-tax prices?</div>
            <div class="faq-a">Divide the tax amount by the pre-tax amount and multiply by 100: Tax Rate % = (Tax Amount / Pre-Tax Amount) × 100.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Are online e-commerce purchases subject to sales tax?</div>
            <div class="faq-a">Since the US Supreme Court ruling in <em>South Dakota v. Wayfair (2018)</em>, online retailers are required to collect state and local sales tax based on the delivery destination address of the customer.</div>
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

print("tools_html_shopping.py created successfully with Tools 18-20.")
