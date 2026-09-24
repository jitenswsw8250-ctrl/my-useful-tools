# integrate_tools.py
# Aggregates and integrates all 20 new tools into index.html, script.js, and sitemap.xml

import json
from generator_data import TOOLS_DATA as NEW_TOOLS
from tools_html_finance import FINANCE_TOOLS_HTML
from tools_html_health import HEALTH_TOOLS_HTML
from tools_html_time_units import TIME_UNITS_TOOLS_HTML
from tools_html_shopping import SHOPPING_TOOLS_HTML
from tools_js import JS_CODE

# All 20 tool HTML sections combined in order
ALL_NEW_SECTIONS = [
    FINANCE_TOOLS_HTML["loan-interest"],
    FINANCE_TOOLS_HTML["loan-eligibility"],
    FINANCE_TOOLS_HTML["loan-tenure"],
    FINANCE_TOOLS_HTML["salary"],
    FINANCE_TOOLS_HTML["overtime"],
    FINANCE_TOOLS_HTML["tax"],
    HEALTH_TOOLS_HTML["calorie"],
    HEALTH_TOOLS_HTML["bmr"],
    HEALTH_TOOLS_HTML["tdee"],
    HEALTH_TOOLS_HTML["pregnancy-due-date"],
    TIME_UNITS_TOOLS_HTML["hours-to-minutes"],
    TIME_UNITS_TOOLS_HTML["minutes-to-hours"],
    TIME_UNITS_TOOLS_HTML["length-converter"],
    TIME_UNITS_TOOLS_HTML["weight-converter"],
    TIME_UNITS_TOOLS_HTML["temperature-converter"],
    TIME_UNITS_TOOLS_HTML["area-converter"],
    TIME_UNITS_TOOLS_HTML["volume-converter"],
    SHOPPING_TOOLS_HTML["tip"],
    SHOPPING_TOOLS_HTML["discount-final-price"],
    SHOPPING_TOOLS_HTML["sales-tax"]
]

print(f"Total new HTML sections assembled: {len(ALL_NEW_SECTIONS)}")

# 1. READ index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Build Drawer Navigation Links for the 20 new tools
drawer_links_html = ""
for t in NEW_TOOLS:
    drawer_links_html += f"""      <a href="#{t['id']}" onclick="navigateTo('{t['id']}')" class="drawer-item" data-screen="{t['id']}">
        <span class="drawer-icon">{t['icon']}</span>
        <span>{t['name']}</span>
      </a>
"""

# Build Homepage Grid Cards for the 20 new tools
cards_html = ""
for i, t in enumerate(NEW_TOOLS, 16):
    tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in t['tags']])
    cards_html += f"""
        <!-- Tool {i}: {t['name']} -->
        <div class="tool-card" onclick="navigateTo('{t['id']}')">
          <div class="tool-icon-wrapper">{t['icon']}</div>
          <div class="tool-info">
            <h3 class="tool-title">{t['name']}</h3>
            <p class="tool-desc">{t['desc']}</p>
            <div class="tool-tags">
              {tags_html}
            </div>
          </div>
          <button class="tool-action-btn">Open Tool →</button>
        </div>
"""

# Build Footer Links for the 20 new tools
footer_links_html = ""
for t in NEW_TOOLS:
    footer_links_html += f"""          <a href="#{t['id']}" onclick="navigateTo('{t['id']}')">{t['name']}</a>\n"""

# Modify Drawer Navigation in index.html
OLD_DRAWER_MARKER = '<div class="drawer-section-label">CALCULATORS (15 TOOLS)</div>'
NEW_DRAWER_MARKER = '<div class="drawer-section-label">ALL CALCULATORS &amp; UTILITIES (35 TOOLS)</div>'
if OLD_DRAWER_MARKER in html_content:
    html_content = html_content.replace(OLD_DRAWER_MARKER, NEW_DRAWER_MARKER)

# Insert new drawer items right before INFORMATION & LEGAL
DRAWER_LEGAL_MARKER = '<div class="drawer-section-label">INFORMATION &amp; LEGAL</div>'
if DRAWER_LEGAL_MARKER in html_content:
    html_content = html_content.replace(
        DRAWER_LEGAL_MARKER,
        drawer_links_html + "\n    " + DRAWER_LEGAL_MARKER
    )

# Insert cards on Home Screen Grid before `</div>\n    </section>\n\n\n    <!-- ==================== 1. AGE CALCULATOR`
GRID_END_MARKER = '<!-- ==================== 1. AGE CALCULATOR ==================== -->'
# We need to find the closing </div> of .tools-grid
old_tool15_marker = '<!-- Tool 15: Average Calculator -->'
# Let's locate the end of Average Calculator tool card in the grid:
# Search for `Mode</span>\n            </div>\n          </div>\n          <button class="tool-action-btn">Open Tool →</button>\n        </div>`
TOOL_15_CARD_END = """              <span class="tag">Mode</span>
            </div>
          </div>
          <button class="tool-action-btn">Open Tool →</button>
        </div>"""

if TOOL_15_CARD_END in html_content:
    html_content = html_content.replace(
        TOOL_15_CARD_END,
        TOOL_15_CARD_END + "\n" + cards_html
    )
    print("Successfully inserted 20 new tool cards into Homepage grid.")
else:
    print("WARNING: Could not find TOOL_15_CARD_END in index.html")

# Insert 20 tool screens before `<!-- 2. ABOUT US -->`
ABOUT_MARKER = '<!-- 2. ABOUT US -->'
if ABOUT_MARKER in html_content:
    all_sections_str = "\n\n".join(ALL_NEW_SECTIONS)
    html_content = html_content.replace(
        ABOUT_MARKER,
        all_sections_str + "\n\n\n    " + ABOUT_MARKER
    )
    print("Successfully inserted 20 new tool screen sections before About Us.")
else:
    print("WARNING: Could not find ABOUT_MARKER in index.html")

# Update Footer Title & links
OLD_FOOTER_TITLE = '<div class="footer-col-title">OUR CALCULATORS (15 TOOLS)</div>'
NEW_FOOTER_TITLE = '<div class="footer-col-title">OUR CALCULATORS (35 TOOLS)</div>'
if OLD_FOOTER_TITLE in html_content:
    html_content = html_content.replace(OLD_FOOTER_TITLE, NEW_FOOTER_TITLE)

FOOTER_AVG_LINK = '<a href="#average" onclick="navigateTo(\'average\')">Average Calculator</a>'
if FOOTER_AVG_LINK in html_content:
    html_content = html_content.replace(
        FOOTER_AVG_LINK,
        FOOTER_AVG_LINK + "\n" + footer_links_html
    )
    print("Successfully inserted 20 new footer links.")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Updated index.html (new size: {len(html_content)} bytes).")

# 2. UPDATE script.js
with open("script.js", "r", encoding="utf-8") as f:
    js_content = f.read()

# Build PAGE_SEO dictionary additions
page_seo_entries = ""
for t in NEW_TOOLS:
    page_seo_entries += f"""  '{t['id']}': {{
    title: {json.dumps(t.get('page_title', t['name']))},
    description: {json.dumps(t['meta_desc'])}
  }},
"""

SEO_END_MARKER = "  disclaimer: {"
if SEO_END_MARKER in js_content:
    js_content = js_content.replace(
        SEO_END_MARKER,
        page_seo_entries + "  disclaimer: {"
    )
    print("Successfully added 20 new tool SEO entries to PAGE_SEO in script.js.")
else:
    print("WARNING: Could not find SEO_END_MARKER in script.js")

# Add initial calculation function calls in DOMContentLoaded
INITIAL_CALLS_MARKER = "  calculateAverage();"
NEW_INITIAL_CALLS = """  calculateAverage();
  calculateLoanInterest();
  calculateLoanEligibility();
  calculateLoanTenure();
  calculateSalary();
  calculateOvertime();
  calculateTax();
  calculateCalorie();
  calculateBmr();
  calculateTdee();
  calculatePregnancyDueDate();
  convertHoursToMinutes();
  convertMinutesToHours();
  convertLength();
  convertWeight();
  convertTemperature();
  convertArea();
  convertVolume();
  calculateTip();
  calculateDiscountFinalPrice();
  calculateSalesTax();"""

if INITIAL_CALLS_MARKER in js_content:
    js_content = js_content.replace(INITIAL_CALLS_MARKER, NEW_INITIAL_CALLS)
    print("Successfully added 20 new initialization calls in DOMContentLoaded.")

# Append the full JS_CODE to script.js
js_content += "\n\n" + JS_CODE

with open("script.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Updated script.js (new size: {len(js_content)} bytes).")

# 3. UPDATE sitemap.xml
with open("sitemap.xml", "r", encoding="utf-8") as f:
    sitemap_content = f.read()

sitemap_entries = ""
for i, t in enumerate(NEW_TOOLS, 16):
    sitemap_entries += f"""  <!-- {i}. {t['name']} -->
  <url>
    <loc>https://ais-pre-vatqw65fky76dekso6xcwb-447578213146.asia-southeast1.run.app/#{t['id']}</loc>
    <lastmod>2026-09-24</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

"""

SITEMAP_END = "</urlset>"
if SITEMAP_END in sitemap_content:
    sitemap_content = sitemap_content.replace(
        SITEMAP_END,
        sitemap_entries + SITEMAP_END
    )
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print(f"Updated sitemap.xml with 20 new tool entries.")

print("All integration tasks complete!")
