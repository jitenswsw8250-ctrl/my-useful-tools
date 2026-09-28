/**
 * MY USEFUL TOOLS - High Performance Client-Side Script
 * Optimized for Mobile Chrome & Android browsers
 * - Zero recalculation loops & instant button responsiveness
 * - Fast DOM caching
 * - Complete implementations of Age, EMI, Percentage, Discount, and BMI calculators
 */

// Global State
let currentScreen = 'home';
let isDarkTheme = false;
let emiCurrency = 'INR';      // 'INR' or 'USD' (default is INR)
let emiTenureUnit = 'years'; // 'years' or 'months' (default is years)
let discCurrency = 'INR';     // 'INR' or 'USD' (default is INR)
let bmiUnit = 'metric';      // 'metric' or 'imperial'

// Cached DOM Elements
let elCache = {};

function initDomCache() {
  elCache = {
    // Theme & Nav
    themeBtn: document.getElementById('theme-toggle-btn'),
    sunIcon: document.querySelector('.sun-icon'),
    moonIcon: document.querySelector('.moon-icon'),
    menuBtn: document.getElementById('menu-btn'),
    shareBtn: document.getElementById('share-btn'),
    drawer: document.getElementById('drawer'),
    overlay: document.getElementById('drawer-overlay'),
    screenSections: document.querySelectorAll('.screen-section'),
    drawerItems: document.querySelectorAll('.drawer-item'),

    // Age Calculator
    ageDay: document.getElementById('age-day'),
    ageMonth: document.getElementById('age-month'),
    ageYear: document.getElementById('age-year'),
    ageDatePicker: document.getElementById('age-date-picker'),
    ageError: document.getElementById('age-error'),
    ageResultCard: document.getElementById('age-result-card'),
    ageYearsNum: document.getElementById('age-years-num'),
    ageBreakdown: document.getElementById('age-breakdown'),
    ageZodiac: document.getElementById('age-zodiac'),
    ageNextBday: document.getElementById('age-next-bday'),
    ageNextDayOfWeek: document.getElementById('age-next-dayofweek'),
    ageTotalDays: document.getElementById('age-total-days'),
    ageTotalHours: document.getElementById('age-total-hours'),

    // EMI Calculator
    emiAmount: document.getElementById('emi-amount'),
    emiAmountLabel: document.getElementById('emi-amount-label'),
    emiCurrInr: document.getElementById('emi-curr-inr'),
    emiCurrUsd: document.getElementById('emi-curr-usd'),
    emiRate: document.getElementById('emi-rate'),
    emiTenure: document.getElementById('emi-tenure'),
    emiTenureYears: document.getElementById('emi-tenure-years'),
    emiTenureMonths: document.getElementById('emi-tenure-months'),
    emiMonthlyVal: document.getElementById('emi-monthly-val'),
    emiTotalInterest: document.getElementById('emi-total-interest'),
    emiTotalPayment: document.getElementById('emi-total-payment'),
    emiInterestPct: document.getElementById('emi-interest-pct'),
    emiPrincipalPct: document.getElementById('emi-principal-pct'),
    barPrincipalPct: document.getElementById('bar-principal-pct'),
    barInterestPct: document.getElementById('bar-interest-pct'),
    splitBarPrincipal: document.getElementById('split-bar-principal'),
    splitBarInterest: document.getElementById('split-bar-interest'),

    // Percentage Calculator
    pctM1X: document.getElementById('pct-m1-x'),
    pctM1Y: document.getElementById('pct-m1-y'),
    pctM1Res: document.getElementById('pct-m1-res'),
    pctM1Expl: document.getElementById('pct-m1-expl'),
    pctM2Initial: document.getElementById('pct-m2-initial'),
    pctM2Final: document.getElementById('pct-m2-final'),
    pctM2Res: document.getElementById('pct-m2-res'),
    pctM2Expl: document.getElementById('pct-m2-expl'),
    pctM3Part: document.getElementById('pct-m3-part'),
    pctM3Whole: document.getElementById('pct-m3-whole'),
    pctM3Res: document.getElementById('pct-m3-res'),
    pctM3Expl: document.getElementById('pct-m3-expl'),
    pctTabBtns: document.querySelectorAll('.tab-btn'),
    pctTabPanes: document.querySelectorAll('.tab-pane'),

    // Discount Calculator
    discCurrencyControl: document.getElementById('disc-currency-control'),
    discCurrInr: document.getElementById('disc-curr-inr'),
    discCurrUsd: document.getElementById('disc-curr-usd'),
    discPriceLabel: document.getElementById('disc-price-label'),
    discPrice: document.getElementById('disc-price'),
    discPercent: document.getElementById('disc-percent'),
    discTaxEnable: document.getElementById('disc-tax-enable'),
    discTaxRate: document.getElementById('disc-tax-rate'),
    discTaxGroup: document.getElementById('disc-tax-group'),
    discFinalLabel: document.getElementById('disc-final-label'),
    discFinalVal: document.getElementById('disc-final-val'),
    discSavingsLabel: document.getElementById('disc-savings-label'),
    discSavingsVal: document.getElementById('disc-savings-val'),
    discSavingsSub: document.getElementById('disc-savings-sub'),
    discOrigLabel: document.getElementById('disc-orig-label'),
    discOrigVal: document.getElementById('disc-orig-val'),
    discTaxVal: document.getElementById('disc-tax-val'),
    discChips: document.querySelectorAll('.chip'),

    // BMI Calculator
    bmiUnitMetric: document.getElementById('bmi-unit-metric'),
    bmiUnitImperial: document.getElementById('bmi-unit-imperial'),
    bmiMetricInputs: document.getElementById('bmi-metric-inputs'),
    bmiImperialInputs: document.getElementById('bmi-imperial-inputs'),
    bmiHeightCm: document.getElementById('bmi-height-cm'),
    bmiWeightKg: document.getElementById('bmi-weight-kg'),
    bmiHeightFt: document.getElementById('bmi-height-ft'),
    bmiHeightIn: document.getElementById('bmi-height-in'),
    bmiWeightLbs: document.getElementById('bmi-weight-lbs'),
    bmiScoreVal: document.getElementById('bmi-score-val'),
    bmiCategoryBadge: document.getElementById('bmi-category-badge'),
    bmiWhoDesc: document.getElementById('bmi-who-desc'),
    bmiHealthyRange: document.getElementById('bmi-healthy-range')
  };
}

// Document Ready
document.addEventListener('DOMContentLoaded', () => {
  initDomCache();

  // Theme initialization
  const savedTheme = localStorage.getItem('mut_theme');
  if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    setTheme(true);
  } else {
    setTheme(false);
  }

  // Theme Toggle Button - Instant touch response
  if (elCache.themeBtn) {
    elCache.themeBtn.addEventListener('click', () => setTheme(!isDarkTheme));
  }

  // Menu Button
  if (elCache.menuBtn) {
    elCache.menuBtn.addEventListener('click', toggleDrawer);
  }

  // Share Button
  if (elCache.shareBtn) {
    elCache.shareBtn.addEventListener('click', handleShare);
  }

  // Date picker sync
  if (elCache.ageDatePicker) {
    elCache.ageDatePicker.addEventListener('change', (e) => {
      if (!e.target.value) return;
      const parts = e.target.value.split('-');
      if (parts.length === 3) {
        if (elCache.ageYear) elCache.ageYear.value = parseInt(parts[0], 10);
        if (elCache.ageMonth) elCache.ageMonth.value = parseInt(parts[1], 10);
        if (elCache.ageDay) elCache.ageDay.value = parseInt(parts[2], 10);
        calculateAge();
      }
    });
  }

  // Currency toggle buttons for Discount Calculator
  if (elCache.discCurrInr) {
    elCache.discCurrInr.addEventListener('click', () => setDiscCurrency('INR'));
  }
  if (elCache.discCurrUsd) {
    elCache.discCurrUsd.addEventListener('click', () => setDiscCurrency('USD'));
  }

  // Initialize initial default state for all calculators
  calculateAge();
  calculateEmi();
  calcPctMode1();
  calcPctMode2();
  calcPctMode3();
  calculateDiscount();
  calculateBmi();
  calculateGst();
  calculateSimpleInterest();
  calculateCompoundInterest();
  calculateProfitLoss();
  calculateSip();
  calculateFd();
  calculateDateDiff();
  calculateTime();
  changeUcCategory();
  calculateAverage();
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
  calculateSalesTax();

  // Hash & Query URL Navigation
  function parseInitialRoute() {
    const params = new URLSearchParams(window.location.search);
    const queryScreen = params.get('tool') || params.get('page') || params.get('screen') || params.get('calc');
    const hash = window.location.hash.replace('#', '');
    const target = queryScreen || hash;
    if (target) {
      navigateTo(target, false);
    }
  }

  window.addEventListener('hashchange', () => {
    const hash = window.location.hash.replace('#', '') || 'home';
    navigateTo(hash, false);
  });

  parseInitialRoute();
  initSearchTools();
  initNewFeatures();
});

// ================= THEME TOGGLE =================
function setTheme(dark) {
  isDarkTheme = dark;
  if (dark) {
    document.body.classList.remove('light-theme');
    document.body.classList.add('dark-theme');
    if (elCache.sunIcon) elCache.sunIcon.style.display = 'none';
    if (elCache.moonIcon) elCache.moonIcon.style.display = 'inline-block';
    localStorage.setItem('mut_theme', 'dark');
  } else {
    document.body.classList.remove('dark-theme');
    document.body.classList.add('light-theme');
    if (elCache.sunIcon) elCache.sunIcon.style.display = 'inline-block';
    if (elCache.moonIcon) elCache.moonIcon.style.display = 'none';
    localStorage.setItem('mut_theme', 'light');
  }
}

// ================= SEO METADATA =================
const PAGE_SEO = {
  home: {
    title: 'MY USEFUL TOOLS - Free Online Calculators & Daily Utilities',
    description: 'Free, simple, and privacy-friendly online calculators: Age, EMI Loan, Percentage, Discount, BMI, GST, Interest, Profit & Loss, SIP, FD, Dates, Time, Units, and Average. Fast, lightweight, and 100% browser-based.'
  },
  'all-tools': {
    title: 'All Free Tools & Calculators | MY USEFUL TOOLS',
    description: 'Explore all 15 free, instant browser calculators: Age, EMI, Percentage, Discount, BMI, GST, Interest, Profit & Loss, SIP, FD, Dates, Time, Units, and Average on MY USEFUL TOOLS.'
  },
  age: {
    title: 'Age Calculator - Exact Years, Months & Days | MY USEFUL TOOLS',
    description: 'Calculate your exact age in years, months, and days with next birthday countdown and zodiac sign. Free, instant, and private.'
  },
  emi: {
    title: 'EMI Loan Calculator - Monthly Installment & Interest | MY USEFUL TOOLS',
    description: 'Calculate loan EMI, total interest payable, and repayment breakdown in INR (₹) or USD ($) for home, car, or personal loans.'
  },
  percentage: {
    title: 'Percentage Calculator - Percent Increase, Decrease & Proportions | MY USEFUL TOOLS',
    description: 'Free online percentage calculator: calculate percentage of a number, percentage change, and proportions instantly.'
  },
  discount: {
    title: 'Discount Calculator - Sale Price, Savings & Tax | MY USEFUL TOOLS',
    description: 'Calculate final sale price after discount with quick percentage presets and optional sales tax in INR (₹) or USD ($).'
  },
  bmi: {
    title: 'BMI Health Calculator - Body Mass Index & Weight Range | MY USEFUL TOOLS',
    description: 'Check your Body Mass Index (BMI) with metric and imperial units. View official WHO categories and healthy weight range.'
  },
  gst: {
    title: 'GST Calculator - Inclusive & Exclusive GST Rates | MY USEFUL TOOLS',
    description: 'Calculate GST inclusive and exclusive prices with CGST, SGST, and IGST breakdowns in INR (₹). Free online Indian Goods & Services Tax calculator.'
  },
  'simple-interest': {
    title: 'Simple Interest Calculator - Interest & Maturity Breakdown | MY USEFUL TOOLS',
    description: 'Compute simple interest and total repayment amounts for loans, savings, and investments with annual or monthly terms.'
  },
  'compound-interest': {
    title: 'Compound Interest Calculator - Compounding Growth & APY | MY USEFUL TOOLS',
    description: 'Calculate compound interest growth with annual, half-yearly, quarterly, or monthly compounding and effective annual rate.'
  },
  'profit-loss': {
    title: 'Profit and Loss Calculator - Margin & Markup Analysis | MY USEFUL TOOLS',
    description: 'Calculate profit, loss, profit percentage, markup, and profit margin on selling price with overhead cost factoring.'
  },
  sip: {
    title: 'SIP Calculator - Mutual Fund Systematic Investment Plan | MY USEFUL TOOLS',
    description: 'Calculate expected future returns and wealth accumulation from monthly mutual fund Systematic Investment Plans (SIP).'
  },
  fd: {
    title: 'FD Calculator - Fixed Deposit Maturity & Interest | MY USEFUL TOOLS',
    description: 'Calculate bank Fixed Deposit (FD) maturity value, total interest earned, and effective yield with quarterly compounding.'
  },
  'date-difference': {
    title: 'Date Difference Calculator - Days, Weeks & Months Between Dates | MY USEFUL TOOLS',
    description: 'Calculate the exact time between two dates in years, months, weeks, days, and working business days.'
  },
  time: {
    title: 'Time Calculator - Clock Duration, Add & Subtract Time | MY USEFUL TOOLS',
    description: 'Calculate duration between two times, add and subtract hours, minutes, and seconds, or convert to decimal hours for payroll.'
  },
  'unit-converter': {
    title: 'Unit Converter - Length, Weight, Temperature, Area & Volume | MY USEFUL TOOLS',
    description: 'Convert between metric and imperial units: meters, feet, kilograms, pounds, Celsius, Fahrenheit, liters, gallons, and more.'
  },
  average: {
    title: 'Average Calculator - Mean, Median, Mode & Standard Deviation | MY USEFUL TOOLS',
    description: 'Calculate arithmetic mean, median, mode, total sum, range, and standard deviation for any list of numbers.'
  },
  about: {
    title: 'About Us - Free Online Utilities | MY USEFUL TOOLS',
    description: 'Learn about MY USEFUL TOOLS, our mission to provide simple, free, privacy-friendly browser-based online calculators and utilities.'
  },
  contact: {
    title: 'Contact Us - Feedback & Inquiries | MY USEFUL TOOLS',
    description: 'Contact the MY USEFUL TOOLS team for feedback, questions, or tool suggestions. Simple and direct communication.'
  },
  privacy: {
    title: 'Privacy Policy | MY USEFUL TOOLS',
    description: 'Read the Privacy Policy for MY USEFUL TOOLS. Learn about local browser-side calculation processing, cookies, and ad settings.'
  },
  terms: {
    title: 'Terms & Conditions | MY USEFUL TOOLS',
    description: 'Terms and conditions of use for MY USEFUL TOOLS free online utility calculators and reference tools.'
  },
  'loan-interest': {
    title: "Loan Interest Calculator - Total Interest & Cost of Borrowing | MY USEFUL TOOLS",
    description: "Calculate the total interest cost, interest vs principal percentage, and loan payoff breakdown in INR (\u20b9) or USD ($). Free and 100% browser-based."
  },
  'loan-eligibility': {
    title: "Loan Eligibility Calculator - Maximum Home & Personal Loan Eligibility | MY USEFUL TOOLS",
    description: "Check your maximum eligible home, car, or personal loan amount based on net monthly income and FOIR debt limits. Fast, free, and client-side."
  },
  'loan-tenure': {
    title: "Loan Tenure Calculator - Loan Payoff Time & Months to Debt Freedom | MY USEFUL TOOLS",
    description: "Calculate how many months or years it will take to pay off a loan based on your affordable monthly payment. Free online payoff calculator."
  },
  'salary': {
    title: "Salary Calculator - In-Hand Take-Home Pay & CTC Breakdown | MY USEFUL TOOLS",
    description: "Calculate take-home in-hand monthly salary from Annual CTC or Gross Salary with PF, Professional Tax, and deductions in INR (\u20b9)."
  },
  'overtime': {
    title: "Overtime Pay Calculator - Time-and-a-Half & Double Time Wages | MY USEFUL TOOLS",
    description: "Calculate overtime earnings, 1.5x time-and-a-half, double time (2.0x), and total gross paycheck. Instant browser calculation."
  },
  'tax': {
    title: "Tax Calculator - Income Tax Liability & New vs Old Regime | MY USEFUL TOOLS",
    description: "Compute Indian Income Tax liability under the New Tax Regime vs Old Tax Regime with standard deduction, Section 87A rebate, and 4% cess."
  },
  'calorie': {
    title: "Calorie Calculator - Daily Caloric Needs for Weight Loss & Gain | MY USEFUL TOOLS",
    description: "Calculate daily caloric intake for weight loss, maintenance, or muscle gain with macro breakdowns using Mifflin-St Jeor formula."
  },
  'bmr': {
    title: "BMR Calculator - Basal Metabolic Rate & Resting Calorie Burn | MY USEFUL TOOLS",
    description: "Calculate Basal Metabolic Rate (BMR)\u2014the exact calories burned at rest by your vital organs with Mifflin-St Jeor and Harris-Benedict formulas."
  },
  'tdee': {
    title: "TDEE Calculator - Total Daily Energy Expenditure & Calorie Burn | MY USEFUL TOOLS",
    description: "Calculate Total Daily Energy Expenditure (TDEE) factoring in metabolic rate and exercise intensity for cutting, maintenance, or bulking."
  },
  'pregnancy-due-date': {
    title: "Pregnancy Due Date Calculator - EDD, Gestational Age & Trimesters | MY USEFUL TOOLS",
    description: "Estimate your baby's due date, gestational age in weeks & days, trimester, and pregnancy milestones using Naegele's rule."
  },
  'hours-to-minutes': {
    title: "Hours to Minutes Converter - Decimal Hours to Total Minutes | MY USEFUL TOOLS",
    description: "Convert decimal hours or hours + minutes into exact total minutes, seconds, and workday proportions with instant lookup tables."
  },
  'minutes-to-hours': {
    title: "Minutes to Hours Converter - Minutes to Decimal Hours & Time | MY USEFUL TOOLS",
    description: "Convert total minutes into decimal hours, hours & minutes, seconds, and work shifts. Ideal for payroll and billing timesheets."
  },
  'length-converter': {
    title: "Length Converter - Convert Meters, Feet, Inches, Miles & KM | MY USEFUL TOOLS",
    description: "Convert length and distance between millimeters, centimeters, meters, kilometers, inches, feet, yards, and miles instantly."
  },
  'weight-converter': {
    title: "Weight Converter - Convert Kilograms, Pounds, Grams & Ounces | MY USEFUL TOOLS",
    description: "Convert weight and mass across milligrams, grams, kilograms, metric tonnes, ounces, pounds, and stones. Free and browser-based."
  },
  'temperature-converter': {
    title: "Temperature Converter - Celsius, Fahrenheit & Kelvin Conversion | MY USEFUL TOOLS",
    description: "Convert temperatures accurately between Celsius (\u00b0C), Fahrenheit (\u00b0F), and Kelvin (K) with step-by-step math and thermal markers."
  },
  'area-converter': {
    title: "Area Converter - Convert Square Feet, Meters, Acres & Hectares | MY USEFUL TOOLS",
    description: "Convert land and geometric area between square meters, square feet, acres, hectares, guntha, bigha, and square yards."
  },
  'volume-converter': {
    title: "Volume Converter - Convert Liters, Gallons, Milliliters & Cups | MY USEFUL TOOLS",
    description: "Convert liquid volume and capacity between milliliters, liters, cubic meters, gallons, cups, fluid ounces, and cubic feet."
  },
  'tip': {
    title: "Tip Calculator - Restaurant Gratuity & Bill Split Per Person | MY USEFUL TOOLS",
    description: "Calculate restaurant tips, service gratuity, bill splitting per person, and custom tip percentages in INR (\u20b9) or USD ($)."
  },
  'discount-final-price': {
    title: "Discount + Final Price Calculator - Stacked Discounts & Sale Price | MY USEFUL TOOLS",
    description: "Compute stacked discounts (double discounts e.g. 40% + extra 15% off) plus optional sales tax / GST and net customer savings."
  },
  'sales-tax': {
    title: "Sales Tax Calculator - Add or Reverse Sales Tax on Any Price | MY USEFUL TOOLS",
    description: "Calculate sales tax addition (exclusive tax) or reverse-calculate pre-tax price from tax-inclusive retail total. Fast and free."
  },
  disclaimer: {
    title: 'Disclaimer | MY USEFUL TOOLS',
    description: 'Read the informational disclaimer for EMI loan estimates, BMI health screening, and utility calculations on MY USEFUL TOOLS.'
  }
};

// ================= NAVIGATION =================
function navigateTo(screenId, updateHash = true) {
  const sections = elCache.screenSections || document.querySelectorAll('.screen-section');
  let effectiveScreen = screenId;
  let scrollToTools = false;

  if (screenId === 'all-tools') {
    effectiveScreen = 'home';
    scrollToTools = true;
  }

  let target = document.getElementById(`screen-${effectiveScreen}`);

  if (!target) {
    effectiveScreen = 'home';
    screenId = 'home';
    target = document.getElementById('screen-home');
  }

  for (let i = 0; i < sections.length; i++) {
    sections[i].classList.remove('active');
  }
  if (target) target.classList.add('active');

  const items = elCache.drawerItems || document.querySelectorAll('.drawer-item');
  for (let i = 0; i < items.length; i++) {
    const item = items[i];
    const itemScreen = item.getAttribute('data-screen');
    if (itemScreen === screenId || (itemScreen === 'home' && effectiveScreen === 'home' && screenId !== 'all-tools')) {
      item.classList.add('active');
    } else {
      item.classList.remove('active');
    }
  }

  currentScreen = effectiveScreen;
  closeDrawer();

  // Record recently used tool
  if (effectiveScreen !== 'home' && effectiveScreen !== 'all-tools' && !['about', 'contact', 'privacy', 'terms', 'disclaimer'].includes(effectiveScreen)) {
    if (typeof recordRecentTool === 'function') {
      recordRecentTool(effectiveScreen);
    }
  } else if (effectiveScreen === 'home') {
    if (typeof renderFavoritesSection === 'function') renderFavoritesSection();
    if (typeof renderRecentToolsSection === 'function') renderRecentToolsSection();
  }

  // Dynamic SEO Title & Meta Description update
  const seo = PAGE_SEO[screenId] || PAGE_SEO[effectiveScreen] || PAGE_SEO.home;
  document.title = seo.title;

  const metaDesc = document.querySelector('meta[name="description"]');
  if (metaDesc) {
    metaDesc.setAttribute('content', seo.description);
  }

  // Update Open Graph and Twitter Card tags
  const ogTitle = document.getElementById('og-title');
  if (ogTitle) ogTitle.setAttribute('content', seo.title);
  const ogDesc = document.getElementById('og-description');
  if (ogDesc) ogDesc.setAttribute('content', seo.description);
  const twTitle = document.getElementById('twitter-title');
  if (twTitle) twTitle.setAttribute('content', seo.title);
  const twDesc = document.getElementById('twitter-description');
  if (twDesc) twDesc.setAttribute('content', seo.description);

  // Update Canonical URL
  const canonicalLink = document.getElementById('canonical-url');
  const ogUrl = document.getElementById('og-url');
  const currentOrigin = (window.location.origin && window.location.origin !== 'null') ? window.location.origin : '';
  const currentPath = window.location.pathname || '/';
  const baseUrl = currentOrigin ? (currentOrigin + currentPath) : 'https://ais-pre-vatqw65fky76dekso6xcwb-447578213146.asia-southeast1.run.app/';
  const fullTargetUrl = effectiveScreen === 'home' ? baseUrl : `${baseUrl}#${effectiveScreen}`;
  if (canonicalLink) {
    canonicalLink.setAttribute('href', fullTargetUrl);
  }
  if (ogUrl) {
    ogUrl.setAttribute('content', fullTargetUrl);
  }

  // Google Analytics 4 page_view tracking for client-side navigation
  if (typeof window.gtag === 'function') {
    window.gtag('event', 'page_view', {
      page_title: seo.title,
      page_location: window.location.href,
      page_path: effectiveScreen === 'home' ? currentPath : `${currentPath}#${effectiveScreen}`
    });
  }

  // Scroll repositioning
  if (scrollToTools) {
    setTimeout(() => {
      const grid = document.getElementById('all-tools-grid') || document.querySelector('.tools-grid');
      if (grid) {
        grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }, 40);
  } else {
    window.scrollTo(0, 0);
  }

  if (updateHash) {
    window.location.hash = screenId === 'home' ? '' : screenId;
  }
}

function toggleDrawer() {
  if (elCache.drawer) elCache.drawer.classList.toggle('open');
  if (elCache.overlay) elCache.overlay.classList.toggle('open');
}

function closeDrawer() {
  if (elCache.drawer) elCache.drawer.classList.remove('open');
  if (elCache.overlay) elCache.overlay.classList.remove('open');
}

function handleShare() {
  shareWebsite();
}

// ================= SEARCH TOOLS =================
function initSearchTools() {
  const searchInput = document.getElementById('tool-search-input');
  const clearBtn = document.getElementById('search-clear-btn');
  const searchBtn = document.getElementById('search-btn');
  const noToolsFound = document.getElementById('no-tools-found');
  const toolsGrid = document.querySelector('.tools-grid') || document.getElementById('tools-grid');

  if (!searchInput || !toolsGrid) return;

  const cards = Array.from(toolsGrid.querySelectorAll('.tool-card'));

  const toolItems = cards.map(card => {
    const titleEl = card.querySelector('.tool-title');
    const descEl = card.querySelector('.tool-desc');
    const tagsEls = card.querySelectorAll('.tool-tags .tag');

    const title = titleEl ? titleEl.textContent.trim() : '';
    const desc = descEl ? descEl.textContent.trim() : '';
    const tags = Array.from(tagsEls).map(t => t.textContent.trim()).join(' ');

    const onclickAttr = card.getAttribute('onclick') || '';
    const match = onclickAttr.match(/navigateTo\('([^']+)'\)/);
    const toolId = match ? match[1] : '';

    const tLower = title.toLowerCase();
    const aliases = [];

    // Specific aliases and synonyms for user test queries
        if (toolId.startsWith('pdf') || toolId === 'images-to-pdf') {
      aliases.push('pdf', 'pdf tool', 'document', 'pdf merge', 'pdf split', 'pdf to images', 'images to pdf');
    }
    if (toolId.startsWith('image') || toolId.includes('jpg') || toolId.includes('png') || toolId.includes('webp')) {
      aliases.push('image', 'photo', 'picture', 'jpg', 'png', 'webp', 'compress', 'resize', 'crop', 'converter');
    }
    if (toolId === 'emi' || tLower.includes('emi')) {
      aliases.push('emi calculator', 'loan emi', 'emi');
    }
    if (toolId === 'bmi' || tLower.includes('bmi')) {
      aliases.push('bmi calculator', 'bmi health', 'body mass index');
    }
    if (tLower.includes('temperature') || toolId.includes('temperature')) {
      aliases.push('temperature converter', 'temperature calculator', 'temp converter');
    }
    if (tLower.includes('discount') || toolId.includes('discount')) {
      aliases.push('discount calculator', 'sale calculator');
    }
    if (tLower.includes('loan') || toolId.startsWith('loan') || toolId === 'emi') {
      aliases.push('loan calculator', 'loans');
    }

    return {
      card,
      title,
      toolId,
      titleLower: tLower,
      aliasesLower: aliases.map(a => a.toLowerCase()),
      searchableText: `${title} ${desc} ${tags} ${toolId} ${aliases.join(' ')}`.toLowerCase()
    };
  });

  let activeCategory = 'all';

  window.filterByCategory = function(category) {
    activeCategory = category;
    const pills = document.querySelectorAll('.category-pill');
    pills.forEach(p => {
      if (p.getAttribute('data-category') === category) {
        p.classList.add('active');
        p.setAttribute('aria-selected', 'true');
      } else {
        p.classList.remove('active');
        p.setAttribute('aria-selected', 'false');
      }
    });
    performSearch();
  };

  function performSearch() {
    const rawVal = searchInput.value;
    const query = rawVal.trim().toLowerCase();

    // Toggle clear button
    if (clearBtn) {
      clearBtn.style.display = rawVal.length > 0 ? 'inline-flex' : 'none';
    }

    let matchCount = 0;
    const queryTokens = query.split(/\s+/).filter(Boolean);

    toolItems.forEach(item => {
      // Category check
      const cardCategory = item.card.getAttribute('data-category') || '';
      const categoryMatch = (activeCategory === 'all' || cardCategory === activeCategory);

      if (!categoryMatch) {
        item.card.style.display = 'none';
        return;
      }

      if (query === '') {
        item.card.style.display = '';
        matchCount++;
        return;
      }

      // 1. Direct title contains search string
      let isMatch = item.titleLower.includes(query);

      // 2. Query matches alias
      if (!isMatch && item.aliasesLower.some(a => a.includes(query) || query.includes(a))) {
        isMatch = true;
      }

      // 3. All tokens in title or aliases
      if (!isMatch && queryTokens.length > 0) {
        const titleAndAliases = item.titleLower + ' ' + item.aliasesLower.join(' ');
        isMatch = queryTokens.every(tok => titleAndAliases.includes(tok));
      }

      if (isMatch) {
        item.card.style.display = '';
        matchCount++;
      } else {
        item.card.style.display = 'none';
      }
    });

    if (noToolsFound) {
      noToolsFound.style.display = matchCount === 0 ? 'block' : 'none';
    }
  }

  // Instant search as the user types
  searchInput.addEventListener('input', performSearch);

  // Clear button click
  if (clearBtn) {
    clearBtn.addEventListener('click', (e) => {
      e.preventDefault();
      searchInput.value = '';
      performSearch();
      searchInput.focus();
    });
  }

  // Search button click
  if (searchBtn) {
    searchBtn.addEventListener('click', (e) => {
      e.preventDefault();
      performSearch();
    });
  }

  // Escape clears search
  searchInput.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      searchInput.value = '';
      performSearch();
    } else if (e.key === 'Enter') {
      e.preventDefault();
      performSearch();
    }
  });
}

// ================= 1. AGE CALCULATOR =================
function calculateAge() {
  const d = parseInt(elCache.ageDay ? elCache.ageDay.value : document.getElementById('age-day').value, 10);
  const m = parseInt(elCache.ageMonth ? elCache.ageMonth.value : document.getElementById('age-month').value, 10);
  const y = parseInt(elCache.ageYear ? elCache.ageYear.value : document.getElementById('age-year').value, 10);
  const errorEl = elCache.ageError || document.getElementById('age-error');
  const resultCard = elCache.ageResultCard || document.getElementById('age-result-card');

  if (isNaN(d) || isNaN(m) || isNaN(y) || d < 1 || d > 31 || m < 1 || m > 12 || y < 1900) {
    if (errorEl) {
      errorEl.textContent = 'Please enter a valid day (1-31), month (1-12), and year.';
      errorEl.style.display = 'block';
    }
    if (resultCard) resultCard.style.opacity = '0.5';
    return;
  }

  const birthDate = new Date(y, m - 1, d);
  const today = new Date();

  // Validate real calendar date
  if (birthDate.getMonth() !== (m - 1) || birthDate.getDate() !== d) {
    if (errorEl) {
      errorEl.textContent = 'Invalid date for the specified month and year.';
      errorEl.style.display = 'block';
    }
    if (resultCard) resultCard.style.opacity = '0.5';
    return;
  }

  if (birthDate > today) {
    if (errorEl) {
      errorEl.textContent = 'Date of birth cannot be in the future.';
      errorEl.style.display = 'block';
    }
    if (resultCard) resultCard.style.opacity = '0.5';
    return;
  }

  if (errorEl) errorEl.style.display = 'none';
  if (resultCard) resultCard.style.opacity = '1';

  // Calculate Years, Months, Days
  let years = today.getFullYear() - birthDate.getFullYear();
  let months = today.getMonth() - birthDate.getMonth();
  let days = today.getDate() - birthDate.getDate();

  if (days < 0) {
    months -= 1;
    const prevMonthDays = new Date(today.getFullYear(), today.getMonth(), 0).getDate();
    days += prevMonthDays;
  }

  if (months < 0) {
    years -= 1;
    months += 12;
  }

  // Next Birthday Calculation
  const nextBday = new Date(today.getFullYear(), m - 1, d);
  if (nextBday < today && (nextBday.toDateString() !== today.toDateString())) {
    nextBday.setFullYear(today.getFullYear() + 1);
  }

  let nextMonths = nextBday.getMonth() - today.getMonth();
  let nextDays = nextBday.getDate() - today.getDate();

  if (nextDays < 0) {
    nextMonths -= 1;
    const prevMonthDays = new Date(nextBday.getFullYear(), nextBday.getMonth(), 0).getDate();
    nextDays += prevMonthDays;
  }
  if (nextMonths < 0) {
    nextMonths += 12;
  }

  const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  const nextDayOfWeek = daysOfWeek[nextBday.getDay()];

  // Total days and hours
  const diffTime = Math.abs(today - birthDate);
  const totalDays = Math.floor(diffTime / 86400000);
  const totalHours = totalDays * 24;

  const zodiac = getZodiac(d, m);

  // Render values
  if (elCache.ageYearsNum) elCache.ageYearsNum.textContent = years;
  if (elCache.ageBreakdown) elCache.ageBreakdown.textContent = `${years} Years, ${months} Months, ${days} Days`;
  if (elCache.ageZodiac) elCache.ageZodiac.textContent = zodiac;

  if (elCache.ageNextBday && elCache.ageNextDayOfWeek) {
    if (nextMonths === 0 && nextDays === 0) {
      elCache.ageNextBday.textContent = '🎉 Happy Birthday Today!';
      elCache.ageNextDayOfWeek.textContent = 'Celebrated today!';
    } else {
      elCache.ageNextBday.textContent = `${nextMonths} Months, ${nextDays} Days`;
      elCache.ageNextDayOfWeek.textContent = `Falling on a ${nextDayOfWeek}`;
    }
  }

  if (elCache.ageTotalDays) elCache.ageTotalDays.textContent = `${totalDays.toLocaleString()} Days`;
  if (elCache.ageTotalHours) elCache.ageTotalHours.textContent = `~${totalHours.toLocaleString()} Total Hours`;
}

function resetAge() {
  if (elCache.ageDay) elCache.ageDay.value = '15';
  if (elCache.ageMonth) elCache.ageMonth.value = '6';
  if (elCache.ageYear) elCache.ageYear.value = '1995';
  if (elCache.ageDatePicker) elCache.ageDatePicker.value = '1995-06-15';
  calculateAge();
}

function getZodiac(day, month) {
  switch (month) {
    case 1: return day < 20 ? 'Capricorn ♑' : 'Aquarius ♒';
    case 2: return day < 19 ? 'Aquarius ♒' : 'Pisces ♓';
    case 3: return day < 21 ? 'Pisces ♓' : 'Aries ♈';
    case 4: return day < 20 ? 'Aries ♈' : 'Taurus ♉';
    case 5: return day < 21 ? 'Taurus ♉' : 'Gemini ♊';
    case 6: return day < 21 ? 'Gemini ♊' : 'Cancer ♋';
    case 7: return day < 23 ? 'Cancer ♋' : 'Leo ♌';
    case 8: return day < 23 ? 'Leo ♌' : 'Virgo ♍';
    case 9: return day < 23 ? 'Virgo ♍' : 'Libra ♎';
    case 10: return day < 23 ? 'Libra ♎' : 'Scorpio ♏';
    case 11: return day < 22 ? 'Scorpio ♏' : 'Sagittarius ♐';
    case 12: return day < 22 ? 'Sagittarius ♐' : 'Capricorn ♑';
    default: return 'Aries ♈';
  }
}

// ================= 2. EMI CALCULATOR =================
function setEmiCurrency(curr) {
  emiCurrency = curr;
  if (elCache.emiCurrInr) elCache.emiCurrInr.classList.toggle('active', curr === 'INR');
  if (elCache.emiCurrUsd) elCache.emiCurrUsd.classList.toggle('active', curr === 'USD');
  if (elCache.emiAmountLabel) {
    elCache.emiAmountLabel.textContent = curr === 'INR' ? 'Loan Amount (₹)' : 'Loan Amount ($)';
  }
  calculateEmi();
}

function setEmiTenureUnit(unit) {
  emiTenureUnit = unit;
  if (elCache.emiTenureYears) elCache.emiTenureYears.classList.toggle('active', unit === 'years');
  if (elCache.emiTenureMonths) elCache.emiTenureMonths.classList.toggle('active', unit === 'months');
  calculateEmi();
}

function calculateEmi() {
  const principal = parseFloat(elCache.emiAmount ? elCache.emiAmount.value : document.getElementById('emi-amount').value) || 0;
  const annualRate = parseFloat(elCache.emiRate ? elCache.emiRate.value : document.getElementById('emi-rate').value) || 0;
  const tenureInput = parseFloat(elCache.emiTenure ? elCache.emiTenure.value : document.getElementById('emi-tenure').value) || 0;

  const months = emiTenureUnit === 'years' ? tenureInput * 12 : tenureInput;

  if (principal <= 0 || annualRate <= 0 || months <= 0) {
    const zeroStr = formatEmiCurrency(0);
    if (elCache.emiMonthlyVal) elCache.emiMonthlyVal.textContent = zeroStr;
    if (elCache.emiTotalInterest) elCache.emiTotalInterest.textContent = zeroStr;
    if (elCache.emiTotalPayment) elCache.emiTotalPayment.textContent = zeroStr;
    return;
  }

  const monthlyRate = annualRate / 1200;
  const factor = Math.pow(1 + monthlyRate, months);
  const emi = (principal * monthlyRate * factor) / (factor - 1);
  const totalPayment = emi * months;
  const totalInterest = totalPayment - principal;

  const principalPct = Math.min(100, Math.max(0, (principal / totalPayment) * 100));
  const interestPct = Math.min(100, Math.max(0, (totalInterest / totalPayment) * 100));

  if (elCache.emiMonthlyVal) elCache.emiMonthlyVal.textContent = formatEmiCurrency(emi);
  if (elCache.emiTotalInterest) elCache.emiTotalInterest.textContent = formatEmiCurrency(totalInterest);
  if (elCache.emiTotalPayment) elCache.emiTotalPayment.textContent = formatEmiCurrency(totalPayment);
  if (elCache.emiInterestPct) elCache.emiInterestPct.textContent = `${interestPct.toFixed(1)}% of repayment`;
  if (elCache.emiPrincipalPct) elCache.emiPrincipalPct.textContent = `${principalPct.toFixed(1)}% Principal (${formatEmiCurrency(principal)})`;

  if (elCache.barPrincipalPct) elCache.barPrincipalPct.textContent = `${principalPct.toFixed(1)}%`;
  if (elCache.barInterestPct) elCache.barInterestPct.textContent = `${interestPct.toFixed(1)}%`;
  if (elCache.splitBarPrincipal) elCache.splitBarPrincipal.style.width = `${principalPct}%`;
  if (elCache.splitBarInterest) elCache.splitBarInterest.style.width = `${interestPct}%`;
}

function resetEmi() {
  setEmiCurrency('INR');
  if (elCache.emiAmount) elCache.emiAmount.value = '50000';
  if (elCache.emiRate) elCache.emiRate.value = '8.5';
  if (elCache.emiTenure) elCache.emiTenure.value = '5';
  setEmiTenureUnit('years');
}

function formatEmiCurrency(val) {
  if (emiCurrency === 'INR') {
    return '₹' + val.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  } else {
    return '$' + val.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }
}

function formatCurrency(val) {
  return val.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

// ================= 3. PERCENTAGE CALCULATOR =================
function switchPctTab(tabIndex) {
  const btns = elCache.pctTabBtns || document.querySelectorAll('.tab-btn');
  const panes = elCache.pctTabPanes || document.querySelectorAll('.tab-pane');

  for (let i = 0; i < btns.length; i++) {
    btns[i].classList.toggle('active', i === tabIndex);
  }
  for (let i = 0; i < panes.length; i++) {
    panes[i].classList.toggle('active', i === tabIndex);
  }
}

function calcPctMode1() {
  const x = parseFloat(elCache.pctM1X ? elCache.pctM1X.value : document.getElementById('pct-m1-x').value) || 0;
  const y = parseFloat(elCache.pctM1Y ? elCache.pctM1Y.value : document.getElementById('pct-m1-y').value) || 0;
  const result = (x / 100) * y;
  if (elCache.pctM1Res) elCache.pctM1Res.textContent = formatDecimal(result);
  if (elCache.pctM1Expl) elCache.pctM1Expl.textContent = `${x}% of ${y} = ${formatDecimal(result)}`;
}

function calcPctMode2() {
  const initial = parseFloat(elCache.pctM2Initial ? elCache.pctM2Initial.value : document.getElementById('pct-m2-initial').value) || 0;
  const finalVal = parseFloat(elCache.pctM2Final ? elCache.pctM2Final.value : document.getElementById('pct-m2-final').value) || 0;
  const resEl = elCache.pctM2Res || document.getElementById('pct-m2-res');
  const explEl = elCache.pctM2Expl || document.getElementById('pct-m2-expl');

  if (initial === 0) {
    if (resEl) {
      resEl.textContent = 'Cannot compute change from zero';
      resEl.className = 'res-bold';
    }
    if (explEl) explEl.textContent = 'Initial value cannot be 0.';
    return;
  }

  const change = ((finalVal - initial) / Math.abs(initial)) * 100;
  const diff = finalVal - initial;

  if (resEl) {
    if (change >= 0) {
      resEl.textContent = `+${change.toFixed(2)}% Increase`;
      resEl.className = 'res-bold text-emerald';
    } else {
      resEl.textContent = `${change.toFixed(2)}% Decrease`;
      resEl.className = 'res-bold text-rose';
    }
  }

  if (explEl) {
    explEl.textContent = `Absolute change of ${diff >= 0 ? '+' : ''}${formatDecimal(diff)} (from ${initial} to ${finalVal})`;
  }
}

function calcPctMode3() {
  const x = parseFloat(elCache.pctM3Part ? elCache.pctM3Part.value : document.getElementById('pct-m3-part').value) || 0;
  const y = parseFloat(elCache.pctM3Whole ? elCache.pctM3Whole.value : document.getElementById('pct-m3-whole').value) || 0;
  const resEl = elCache.pctM3Res || document.getElementById('pct-m3-res');
  const explEl = elCache.pctM3Expl || document.getElementById('pct-m3-expl');

  if (y === 0) {
    if (resEl) resEl.textContent = 'Division by zero';
    if (explEl) explEl.textContent = 'Total (Y) cannot be 0.';
    return;
  }

  const pct = (x / y) * 100;
  if (resEl) resEl.textContent = `${pct.toFixed(2)}%`;
  if (explEl) explEl.textContent = `${x} is ${pct.toFixed(2)}% of ${y}`;
}

function formatDecimal(val) {
  return Number.isInteger(val) ? val.toString() : val.toFixed(2);
}

// ================= 4. DISCOUNT CALCULATOR =================
function setDiscCurrency(curr) {
  discCurrency = curr;
  const inrBtn = elCache.discCurrInr || document.getElementById('disc-curr-inr');
  const usdBtn = elCache.discCurrUsd || document.getElementById('disc-curr-usd');
  if (inrBtn) inrBtn.classList.toggle('active', curr === 'INR');
  if (usdBtn) usdBtn.classList.toggle('active', curr === 'USD');

  const priceLabel = elCache.discPriceLabel || document.getElementById('disc-price-label');
  if (priceLabel) {
    priceLabel.textContent = curr === 'INR' ? 'Original Price (₹)' : 'Original Price ($)';
  }

  const finalLabel = elCache.discFinalLabel || document.getElementById('disc-final-label');
  if (finalLabel) {
    finalLabel.textContent = curr === 'INR' ? 'Final Price (₹)' : 'Final Price ($)';
  }

  const savingsLabel = elCache.discSavingsLabel || document.getElementById('disc-savings-label');
  if (savingsLabel) {
    savingsLabel.textContent = curr === 'INR' ? 'You Save (₹)' : 'You Save ($)';
  }

  const origLabel = elCache.discOrigLabel || document.getElementById('disc-orig-label');
  if (origLabel) {
    origLabel.textContent = curr === 'INR' ? 'Original Price (₹)' : 'Original Price ($)';
  }

  calculateDiscount();
}

function formatDiscCurrency(val) {
  if (discCurrency === 'INR') {
    return '₹' + val.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  } else {
    return '$' + val.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }
}

function setQuickDiscount(pct) {
  if (elCache.discPercent) elCache.discPercent.value = pct;
  const chips = elCache.discChips || document.querySelectorAll('.chip');
  for (let i = 0; i < chips.length; i++) {
    chips[i].classList.remove('active');
  }
  const currentChip = document.getElementById(`chip-${pct}`);
  if (currentChip) currentChip.classList.add('active');
  calculateDiscount();
}

function toggleTaxField() {
  const isTaxEnabled = elCache.discTaxEnable ? elCache.discTaxEnable.checked : false;
  if (elCache.discTaxGroup) {
    elCache.discTaxGroup.style.display = isTaxEnabled ? 'block' : 'none';
  }
  calculateDiscount();
}

function calculateDiscount() {
  const price = parseFloat(elCache.discPrice ? elCache.discPrice.value : document.getElementById('disc-price').value) || 0;
  const discountPct = parseFloat(elCache.discPercent ? elCache.discPercent.value : document.getElementById('disc-percent').value) || 0;
  const isTaxEnabled = elCache.discTaxEnable ? elCache.discTaxEnable.checked : false;
  const taxPct = isTaxEnabled ? (parseFloat(elCache.discTaxRate ? elCache.discTaxRate.value : 0) || 0) : 0;

  // Make sure all labels are in sync with discCurrency
  const priceLabel = elCache.discPriceLabel || document.getElementById('disc-price-label');
  if (priceLabel) {
    priceLabel.textContent = discCurrency === 'INR' ? 'Original Price (₹)' : 'Original Price ($)';
  }
  const finalLabel = elCache.discFinalLabel || document.getElementById('disc-final-label');
  if (finalLabel) {
    finalLabel.textContent = discCurrency === 'INR' ? 'Final Price (₹)' : 'Final Price ($)';
  }
  const savingsLabel = elCache.discSavingsLabel || document.getElementById('disc-savings-label');
  if (savingsLabel) {
    savingsLabel.textContent = discCurrency === 'INR' ? 'You Save (₹)' : 'You Save ($)';
  }
  const origLabel = elCache.discOrigLabel || document.getElementById('disc-orig-label');
  if (origLabel) {
    origLabel.textContent = discCurrency === 'INR' ? 'Original Price (₹)' : 'Original Price ($)';
  }

  if (price <= 0) {
    const zeroStr = formatDiscCurrency(0);
    if (elCache.discFinalVal) elCache.discFinalVal.textContent = zeroStr;
    if (elCache.discSavingsVal) elCache.discSavingsVal.textContent = zeroStr;
    if (elCache.discOrigVal) elCache.discOrigVal.textContent = zeroStr;
    return;
  }

  const savings = price * (discountPct / 100);
  const priceAfterDiscount = Math.max(0, price - savings);
  const taxAmount = priceAfterDiscount * (taxPct / 100);
  const finalPrice = priceAfterDiscount + taxAmount;

  if (elCache.discFinalVal) elCache.discFinalVal.textContent = formatDiscCurrency(finalPrice);
  if (elCache.discSavingsVal) elCache.discSavingsVal.textContent = formatDiscCurrency(savings);
  if (elCache.discSavingsSub) elCache.discSavingsSub.textContent = `${discountPct}% off original price`;
  if (elCache.discOrigVal) elCache.discOrigVal.textContent = formatDiscCurrency(price);

  if (elCache.discTaxVal) {
    elCache.discTaxVal.textContent = isTaxEnabled
      ? `Includes +${formatDiscCurrency(taxAmount)} (${taxPct}% tax)`
      : 'Tax: Not included';
  }
}

function resetDiscount() {
  setDiscCurrency('INR');
  if (elCache.discPrice) elCache.discPrice.value = '120';
  if (elCache.discPercent) elCache.discPercent.value = '25';
  if (elCache.discTaxEnable) elCache.discTaxEnable.checked = false;
  if (elCache.discTaxGroup) elCache.discTaxGroup.style.display = 'none';
  setQuickDiscount(25);
}

// ================= 5. BMI CALCULATOR =================
function setBmiUnit(unit) {
  bmiUnit = unit;
  if (elCache.bmiUnitMetric) elCache.bmiUnitMetric.classList.toggle('active', unit === 'metric');
  if (elCache.bmiUnitImperial) elCache.bmiUnitImperial.classList.toggle('active', unit === 'imperial');

  if (elCache.bmiMetricInputs) elCache.bmiMetricInputs.style.display = unit === 'metric' ? 'grid' : 'none';
  if (elCache.bmiImperialInputs) elCache.bmiImperialInputs.style.display = unit === 'imperial' ? 'block' : 'none';

  calculateBmi();
}

function calculateBmi() {
  let heightMeters = 0;
  let weightKg = 0;

  if (bmiUnit === 'metric') {
    const cm = parseFloat(elCache.bmiHeightCm ? elCache.bmiHeightCm.value : document.getElementById('bmi-height-cm').value) || 0;
    weightKg = parseFloat(elCache.bmiWeightKg ? elCache.bmiWeightKg.value : document.getElementById('bmi-weight-kg').value) || 0;
    heightMeters = cm / 100;
  } else {
    const feet = parseFloat(elCache.bmiHeightFt ? elCache.bmiHeightFt.value : document.getElementById('bmi-height-ft').value) || 0;
    const inches = parseFloat(elCache.bmiHeightIn ? elCache.bmiHeightIn.value : document.getElementById('bmi-height-in').value) || 0;
    const lbs = parseFloat(elCache.bmiWeightLbs ? elCache.bmiWeightLbs.value : document.getElementById('bmi-weight-lbs').value) || 0;

    const totalInches = (feet * 12) + inches;
    heightMeters = totalInches * 0.0254;
    weightKg = lbs * 0.45359237;
  }

  if (heightMeters <= 0 || weightKg <= 0) {
    if (elCache.bmiScoreVal) elCache.bmiScoreVal.textContent = '--';
    return;
  }

  const bmi = weightKg / (heightMeters * heightMeters);
  const badgeEl = elCache.bmiCategoryBadge || document.getElementById('bmi-category-badge');
  const whoDescEl = elCache.bmiWhoDesc || document.getElementById('bmi-who-desc');

  let category = 'Normal Weight';
  let badgeClass = 'badge-normal';
  let desc = '18.5 – 24.9 indicates optimal healthy weight for height.';

  if (bmi < 18.5) {
    category = 'Underweight';
    badgeClass = 'badge-under';
    desc = 'Below 18.5 indicates weight below standard healthy range.';
  } else if (bmi < 25.0) {
    category = 'Normal Weight';
    badgeClass = 'badge-normal';
    desc = '18.5 – 24.9 indicates optimal healthy weight.';
  } else if (bmi < 30.0) {
    category = 'Overweight';
    badgeClass = 'badge-over';
    desc = '25.0 – 29.9 indicates excess body weight.';
  } else {
    category = 'Obese';
    badgeClass = 'badge-obese';
    desc = '30.0 or higher indicates obesity classification.';
  }

  const minHealthyKg = 18.5 * heightMeters * heightMeters;
  const maxHealthyKg = 24.9 * heightMeters * heightMeters;

  let rangeString = '';
  if (bmiUnit === 'metric') {
    rangeString = `${minHealthyKg.toFixed(1)} kg – ${maxHealthyKg.toFixed(1)} kg`;
  } else {
    const minLbs = minHealthyKg * 2.20462;
    const maxLbs = maxHealthyKg * 2.20462;
    rangeString = `${minLbs.toFixed(1)} lbs – ${maxLbs.toFixed(1)} lbs`;
  }

  if (elCache.bmiScoreVal) elCache.bmiScoreVal.textContent = bmi.toFixed(1);
  if (badgeEl) {
    badgeEl.textContent = category;
    badgeEl.className = `category-badge ${badgeClass}`;
  }
  if (whoDescEl) whoDescEl.textContent = desc;
  if (elCache.bmiHealthyRange) elCache.bmiHealthyRange.textContent = rangeString;
}

function resetBmi() {
  if (elCache.bmiHeightCm) elCache.bmiHeightCm.value = '175';
  if (elCache.bmiWeightKg) elCache.bmiWeightKg.value = '70';
  if (elCache.bmiHeightFt) elCache.bmiHeightFt.value = '5';
  if (elCache.bmiHeightIn) elCache.bmiHeightIn.value = '9';
  if (elCache.bmiWeightLbs) elCache.bmiWeightLbs.value = '154';
  calculateBmi();
}

// ================= CONTACT FORM =================
function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

function handleContactSubmit(e) {
  e.preventDefault();
  const nameEl = document.getElementById('contact-name');
  const emailEl = document.getElementById('contact-email');
  const msgEl = document.getElementById('contact-message');
  const nameErr = document.getElementById('contact-name-err');
  const emailErr = document.getElementById('contact-email-err');
  const msgErr = document.getElementById('contact-msg-err');
  const successBanner = document.getElementById('contact-success');

  const nameVal = nameEl ? nameEl.value.trim() : '';
  const emailVal = emailEl ? emailEl.value.trim() : '';
  const msgVal = msgEl ? msgEl.value.trim() : '';

  let isValid = true;

  if (!nameVal) {
    if (nameErr) nameErr.style.display = 'block';
    isValid = false;
  } else if (nameErr) {
    nameErr.style.display = 'none';
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailVal || !emailRegex.test(emailVal)) {
    if (emailErr) emailErr.style.display = 'block';
    isValid = false;
  } else if (emailErr) {
    emailErr.style.display = 'none';
  }

  if (!msgVal || msgVal.length < 5) {
    if (msgErr) msgErr.style.display = 'block';
    isValid = false;
  } else if (msgErr) {
    msgErr.style.display = 'none';
  }

  if (!isValid) return;

  if (successBanner) {
    successBanner.innerHTML = `<strong>Thank you, ${escapeHtml(nameVal)}!</strong> Your message has been verified and validated locally.<br><span style="font-size: 0.82rem; font-weight: normal; margin-top: 4px; display: inline-block;">Note: This browser-based suite currently operates client-side without an external mail server. For direct inquiries, you can reach out via: <a href="mailto:myusefultools2026@gmail.com" style="color: var(--primary); font-weight: 600;">myusefultools2026@gmail.com</a></span>`;
    successBanner.style.display = 'block';
  }

  const form = document.getElementById('contact-form');
  if (form) form.reset();
}

function resetContactForm() {
  const nameErr = document.getElementById('contact-name-err');
  const emailErr = document.getElementById('contact-email-err');
  const msgErr = document.getElementById('contact-msg-err');
  const successBanner = document.getElementById('contact-success');
  if (nameErr) nameErr.style.display = 'none';
  if (emailErr) emailErr.style.display = 'none';
  if (msgErr) msgErr.style.display = 'none';
  if (successBanner) successBanner.style.display = 'none';
}

// ================= UTILITY: INR FORMATTING =================
function formatINR(val) {
  return '₹' + Number(val || 0).toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

// ================= 6. GST CALCULATOR =================
let gstType = 'exclusive'; // 'exclusive' or 'inclusive'

function setGstType(type) {
  gstType = type;
  const excBtn = document.getElementById('gst-type-exclusive');
  const incBtn = document.getElementById('gst-type-inclusive');
  const amountLabel = document.getElementById('gst-amount-label');
  const grossLabel = document.getElementById('gst-gross-label');
  const netLabel = document.getElementById('gst-net-label');
  const typeDesc = document.getElementById('gst-type-desc');

  if (type === 'exclusive') {
    if (excBtn) excBtn.classList.add('active');
    if (incBtn) incBtn.classList.remove('active');
    if (amountLabel) amountLabel.textContent = 'Base Amount (₹)';
    if (grossLabel) grossLabel.textContent = 'Total Gross Amount (₹)';
    if (netLabel) netLabel.textContent = 'Net Amount (Base Price)';
    if (typeDesc) typeDesc.textContent = 'Exclusive mode: GST added to base';
  } else {
    if (incBtn) incBtn.classList.add('active');
    if (excBtn) excBtn.classList.remove('active');
    if (amountLabel) amountLabel.textContent = 'Gross Amount (₹ - includes GST)';
    if (grossLabel) grossLabel.textContent = 'Gross Invoice Amount (₹)';
    if (netLabel) netLabel.textContent = 'Pre-Tax Net Amount (Base Price)';
    if (typeDesc) typeDesc.textContent = 'Inclusive mode: GST removed from total';
  }
  calculateGst();
}

function setQuickGstRate(rate) {
  const rateInput = document.getElementById('gst-rate');
  if (rateInput) rateInput.value = rate;
  document.querySelectorAll('#screen-gst .chip').forEach(c => {
    if (c.textContent.startsWith(rate + '%')) {
      c.classList.add('active');
    } else {
      c.classList.remove('active');
    }
  });
  calculateGst();
}

function calculateGst() {
  const amountEl = document.getElementById('gst-amount');
  const rateEl = document.getElementById('gst-rate');
  if (!amountEl || !rateEl) return;

  const rawAmount = parseFloat(amountEl.value) || 0;
  const rate = Math.max(0, parseFloat(rateEl.value) || 0);

  let net = 0;
  let tax = 0;
  let gross = 0;

  if (gstType === 'exclusive') {
    net = rawAmount;
    tax = net * (rate / 100);
    gross = net + tax;
  } else {
    gross = rawAmount;
    net = gross / (1 + (rate / 100));
    tax = gross - net;
  }

  const cgst = tax / 2;
  const sgst = tax / 2;
  const igst = tax;

  const grossValEl = document.getElementById('gst-gross-val');
  const netValEl = document.getElementById('gst-net-val');
  const taxValEl = document.getElementById('gst-tax-val');
  const rateSubEl = document.getElementById('gst-rate-sub');
  const cgstEl = document.getElementById('gst-cgst-val');
  const sgstEl = document.getElementById('gst-sgst-val');
  const igstEl = document.getElementById('gst-igst-val');

  if (grossValEl) grossValEl.textContent = formatINR(gross);
  if (netValEl) netValEl.textContent = formatINR(net);
  if (taxValEl) taxValEl.textContent = formatINR(tax);
  if (rateSubEl) rateSubEl.textContent = `Calculated at ${rate}% GST`;
  if (cgstEl) cgstEl.textContent = formatINR(cgst);
  if (sgstEl) sgstEl.textContent = formatINR(sgst);
  if (igstEl) igstEl.textContent = formatINR(igst);
}

function resetGst() {
  const amountEl = document.getElementById('gst-amount');
  const rateEl = document.getElementById('gst-rate');
  if (amountEl) amountEl.value = '10000';
  if (rateEl) rateEl.value = '18';
  setGstType('exclusive');
  setQuickGstRate(18);
}

// ================= 7. SIMPLE INTEREST CALCULATOR =================
let siUnit = 'years';

function setSiUnit(unit) {
  siUnit = unit;
  const yBtn = document.getElementById('si-unit-years');
  const mBtn = document.getElementById('si-unit-months');
  if (unit === 'years') {
    if (yBtn) yBtn.classList.add('active');
    if (mBtn) mBtn.classList.remove('active');
  } else {
    if (mBtn) mBtn.classList.add('active');
    if (yBtn) yBtn.classList.remove('active');
  }
  calculateSimpleInterest();
}

function calculateSimpleInterest() {
  const pEl = document.getElementById('si-principal');
  const rEl = document.getElementById('si-rate');
  const tEl = document.getElementById('si-time');
  if (!pEl || !rEl || !tEl) return;

  const P = Math.max(0, parseFloat(pEl.value) || 0);
  const R = Math.max(0, parseFloat(rEl.value) || 0);
  const rawT = Math.max(0, parseFloat(tEl.value) || 0);
  const T = siUnit === 'months' ? (rawT / 12) : rawT;

  const interest = (P * R * T) / 100;
  const total = P + interest;
  const totalMonths = Math.max(1, T * 12);
  const monthlyInterest = interest / totalMonths;
  const dailyInterest = interest / Math.max(1, T * 365);

  const interestValEl = document.getElementById('si-interest-val');
  const totalValEl = document.getElementById('si-total-val');
  const monthlyValEl = document.getElementById('si-monthly-val');
  const dailyValEl = document.getElementById('si-daily-val');

  if (interestValEl) interestValEl.textContent = formatINR(interest);
  if (totalValEl) totalValEl.textContent = formatINR(total);
  if (monthlyValEl) monthlyValEl.textContent = formatINR(monthlyInterest);
  if (dailyValEl) dailyValEl.textContent = `~${formatINR(dailyInterest)} per day`;

  let principalPct = total > 0 ? (P / total) * 100 : 100;
  let interestPct = total > 0 ? (interest / total) * 100 : 0;

  const barPPct = document.getElementById('si-bar-principal-pct');
  const barIPct = document.getElementById('si-bar-interest-pct');
  const barP = document.getElementById('si-bar-principal');
  const barI = document.getElementById('si-bar-interest');

  if (barPPct) barPPct.textContent = principalPct.toFixed(1) + '%';
  if (barIPct) barIPct.textContent = interestPct.toFixed(1) + '%';
  if (barP) barP.style.width = principalPct.toFixed(1) + '%';
  if (barI) barI.style.width = interestPct.toFixed(1) + '%';
}

function resetSimpleInterest() {
  const pEl = document.getElementById('si-principal');
  const rEl = document.getElementById('si-rate');
  const tEl = document.getElementById('si-time');
  if (pEl) pEl.value = '100000';
  if (rEl) rEl.value = '7.5';
  if (tEl) tEl.value = '3';
  setSiUnit('years');
}

// ================= 8. COMPOUND INTEREST CALCULATOR =================
function calculateCompoundInterest() {
  const pEl = document.getElementById('ci-principal');
  const rEl = document.getElementById('ci-rate');
  const tEl = document.getElementById('ci-time');
  const fEl = document.getElementById('ci-freq');
  if (!pEl || !rEl || !tEl || !fEl) return;

  const P = Math.max(0, parseFloat(pEl.value) || 0);
  const r = Math.max(0, parseFloat(rEl.value) || 0) / 100;
  const t = Math.max(0, parseFloat(tEl.value) || 0);
  const n = parseInt(fEl.value, 10) || 4;

  let A = 0;
  if (P > 0 && t > 0) {
    A = P * Math.pow(1 + (r / n), n * t);
  } else {
    A = P;
  }
  const interest = Math.max(0, A - P);
  const simpleInterest = (P * (r * 100) * t) / 100;
  const diff = Math.max(0, interest - simpleInterest);
  const ear = n > 0 ? (Math.pow(1 + (r / n), n) - 1) * 100 : (r * 100);

  const totalValEl = document.getElementById('ci-total-val');
  const interestValEl = document.getElementById('ci-interest-val');
  const earValEl = document.getElementById('ci-ear-val');
  const diffValEl = document.getElementById('ci-diff-val');

  if (totalValEl) totalValEl.textContent = formatINR(A);
  if (interestValEl) interestValEl.textContent = formatINR(interest);
  if (earValEl) earValEl.textContent = ear.toFixed(2) + '%';
  if (diffValEl) diffValEl.textContent = `+${formatINR(diff)} more than Simple Interest`;

  let principalPct = A > 0 ? (P / A) * 100 : 100;
  let interestPct = A > 0 ? (interest / A) * 100 : 0;

  const barPPct = document.getElementById('ci-bar-principal-pct');
  const barIPct = document.getElementById('ci-bar-interest-pct');
  const barP = document.getElementById('ci-bar-principal');
  const barI = document.getElementById('ci-bar-interest');

  if (barPPct) barPPct.textContent = principalPct.toFixed(1) + '%';
  if (barIPct) barIPct.textContent = interestPct.toFixed(1) + '%';
  if (barP) barP.style.width = principalPct.toFixed(1) + '%';
  if (barI) barI.style.width = interestPct.toFixed(1) + '%';
}

function resetCompoundInterest() {
  const pEl = document.getElementById('ci-principal');
  const rEl = document.getElementById('ci-rate');
  const tEl = document.getElementById('ci-time');
  const fEl = document.getElementById('ci-freq');
  if (pEl) pEl.value = '100000';
  if (rEl) rEl.value = '8.0';
  if (tEl) tEl.value = '5';
  if (fEl) fEl.value = '4';
  calculateCompoundInterest();
}

// ================= 9. PROFIT & LOSS CALCULATOR =================
function calculateProfitLoss() {
  const cpEl = document.getElementById('pl-cost-price');
  const spEl = document.getElementById('pl-selling-price');
  const ovEl = document.getElementById('pl-overhead');
  if (!cpEl || !spEl) return;

  const cp = Math.max(0, parseFloat(cpEl.value) || 0);
  const sp = Math.max(0, parseFloat(spEl.value) || 0);
  const ov = Math.max(0, parseFloat(ovEl ? ovEl.value : 0) || 0);
  const totalCost = cp + ov;

  const amountValEl = document.getElementById('pl-amount-val');
  const badgeEl = document.getElementById('pl-badge');
  const pctValEl = document.getElementById('pl-pct-val');
  const marginValEl = document.getElementById('pl-margin-val');
  const totalCostValEl = document.getElementById('pl-total-cost-val');
  const markupValEl = document.getElementById('pl-markup-val');

  if (totalCostValEl) totalCostValEl.textContent = formatINR(totalCost);

  if (totalCost === 0 && sp === 0) {
    if (amountValEl) amountValEl.textContent = '₹0.00';
    if (badgeEl) { badgeEl.textContent = 'BREAK-EVEN'; badgeEl.className = 'category-badge badge-even'; }
    if (pctValEl) pctValEl.textContent = '0.00%';
    if (marginValEl) marginValEl.textContent = '0.00%';
    if (markupValEl) markupValEl.textContent = '0.00%';
    return;
  }

  const diff = sp - totalCost;

  if (diff > 0) {
    const profitPct = totalCost > 0 ? (diff / totalCost) * 100 : 0;
    const marginPct = sp > 0 ? (diff / sp) * 100 : 0;
    const markupPct = totalCost > 0 ? (diff / totalCost) * 100 : 0;

    if (amountValEl) {
      amountValEl.textContent = `+${formatINR(diff)}`;
      amountValEl.className = 'highlight-number text-emerald';
    }
    if (badgeEl) {
      badgeEl.textContent = 'PROFIT';
      badgeEl.className = 'category-badge badge-profit';
    }
    if (pctValEl) {
      pctValEl.textContent = `+${profitPct.toFixed(2)}%`;
      pctValEl.className = 'metric-value text-emerald';
    }
    if (marginValEl) marginValEl.textContent = `${marginPct.toFixed(2)}%`;
    if (markupValEl) markupValEl.textContent = `${markupPct.toFixed(2)}%`;
  } else if (diff < 0) {
    const loss = Math.abs(diff);
    const lossPct = totalCost > 0 ? (loss / totalCost) * 100 : 0;
    const marginPct = sp > 0 ? (diff / sp) * 100 : 0;
    const markupPct = totalCost > 0 ? (diff / totalCost) * 100 : 0;

    if (amountValEl) {
      amountValEl.textContent = `-${formatINR(loss)}`;
      amountValEl.className = 'highlight-number text-rose';
    }
    if (badgeEl) {
      badgeEl.textContent = 'LOSS';
      badgeEl.className = 'category-badge badge-loss';
    }
    if (pctValEl) {
      pctValEl.textContent = `-${lossPct.toFixed(2)}%`;
      pctValEl.className = 'metric-value text-rose';
    }
    if (marginValEl) marginValEl.textContent = `${marginPct.toFixed(2)}%`;
    if (markupValEl) markupValEl.textContent = `${markupPct.toFixed(2)}%`;
  } else {
    if (amountValEl) {
      amountValEl.textContent = '₹0.00';
      amountValEl.className = 'highlight-number text-muted';
    }
    if (badgeEl) {
      badgeEl.textContent = 'BREAK-EVEN';
      badgeEl.className = 'category-badge badge-even';
    }
    if (pctValEl) {
      pctValEl.textContent = '0.00%';
      pctValEl.className = 'metric-value';
    }
    if (marginValEl) marginValEl.textContent = '0.00%';
    if (markupValEl) markupValEl.textContent = '0.00%';
  }
}

function resetProfitLoss() {
  const cpEl = document.getElementById('pl-cost-price');
  const spEl = document.getElementById('pl-selling-price');
  const ovEl = document.getElementById('pl-overhead');
  if (cpEl) cpEl.value = '1200';
  if (spEl) spEl.value = '1500';
  if (ovEl) ovEl.value = '0';
  calculateProfitLoss();
}

// ================= 10. SIP CALCULATOR =================
function calculateSip() {
  const mEl = document.getElementById('sip-monthly');
  const rEl = document.getElementById('sip-rate');
  const yEl = document.getElementById('sip-years');
  if (!mEl || !rEl || !yEl) return;

  const P = Math.max(0, parseFloat(mEl.value) || 0);
  const annualRate = Math.max(0, parseFloat(rEl.value) || 0);
  const years = Math.max(0, parseFloat(yEl.value) || 0);
  const months = Math.round(years * 12);
  const i = (annualRate / 12) / 100;

  const invested = P * months;
  let maturity = 0;
  if (i > 0 && months > 0) {
    maturity = P * ((Math.pow(1 + i, months) - 1) / i) * (1 + i);
  } else {
    maturity = invested;
  }
  const returns = Math.max(0, maturity - invested);
  const multiplier = invested > 0 ? (maturity / invested).toFixed(2) : '1.00';

  const totalValEl = document.getElementById('sip-total-val');
  const investedValEl = document.getElementById('sip-invested-val');
  const returnsValEl = document.getElementById('sip-returns-val');
  const multValEl = document.getElementById('sip-mult-val');
  const monthsSubEl = document.getElementById('sip-months-sub');

  if (totalValEl) totalValEl.textContent = formatINR(maturity);
  if (investedValEl) investedValEl.textContent = formatINR(invested);
  if (returnsValEl) returnsValEl.textContent = formatINR(returns);
  if (multValEl) multValEl.textContent = `${multiplier}x wealth multiplier`;
  if (monthsSubEl) monthsSubEl.textContent = `${months} monthly installments of ${formatINR(P)}`;

  let invPct = maturity > 0 ? (invested / maturity) * 100 : 100;
  let retPct = maturity > 0 ? (returns / maturity) * 100 : 0;

  const barInvPct = document.getElementById('sip-bar-invested-pct');
  const barRetPct = document.getElementById('sip-bar-returns-pct');
  const barInv = document.getElementById('sip-bar-invested');
  const barRet = document.getElementById('sip-bar-returns');

  if (barInvPct) barInvPct.textContent = invPct.toFixed(1) + '%';
  if (barRetPct) barRetPct.textContent = retPct.toFixed(1) + '%';
  if (barInv) barInv.style.width = invPct.toFixed(1) + '%';
  if (barRet) barRet.style.width = retPct.toFixed(1) + '%';
}

function resetSip() {
  const mEl = document.getElementById('sip-monthly');
  const rEl = document.getElementById('sip-rate');
  const yEl = document.getElementById('sip-years');
  if (mEl) mEl.value = '5000';
  if (rEl) rEl.value = '12';
  if (yEl) yEl.value = '10';
  calculateSip();
}

// ================= 11. FD CALCULATOR =================
function calculateFd() {
  const depEl = document.getElementById('fd-deposit');
  const rateEl = document.getElementById('fd-rate');
  const yEl = document.getElementById('fd-years');
  const mEl = document.getElementById('fd-months');
  const fEl = document.getElementById('fd-freq');
  if (!depEl || !rateEl || !yEl || !mEl || !fEl) return;

  const P = Math.max(0, parseFloat(depEl.value) || 0);
  const r = Math.max(0, parseFloat(rateEl.value) || 0) / 100;
  const years = Math.max(0, parseFloat(yEl.value) || 0);
  const months = Math.max(0, parseFloat(mEl.value) || 0);
  const t = years + (months / 12);
  const n = parseInt(fEl.value, 10) || 4;

  let maturity = 0;
  if (P > 0 && t > 0) {
    maturity = P * Math.pow(1 + (r / n), n * t);
  } else {
    maturity = P;
  }
  const interest = Math.max(0, maturity - P);
  const roi = P > 0 ? (interest / P) * 100 : 0;

  const matValEl = document.getElementById('fd-maturity-val');
  const intValEl = document.getElementById('fd-interest-val');
  const roiValEl = document.getElementById('fd-roi-val');
  const princValEl = document.getElementById('fd-principal-val');

  if (matValEl) matValEl.textContent = formatINR(maturity);
  if (intValEl) intValEl.textContent = formatINR(interest);
  if (roiValEl) roiValEl.textContent = `${roi.toFixed(2)}% aggregate growth`;
  if (princValEl) princValEl.textContent = formatINR(P);

  let princPct = maturity > 0 ? (P / maturity) * 100 : 100;
  let intPct = maturity > 0 ? (interest / maturity) * 100 : 0;

  const barPPct = document.getElementById('fd-bar-principal-pct');
  const barIPct = document.getElementById('fd-bar-interest-pct');
  const barP = document.getElementById('fd-bar-principal');
  const barI = document.getElementById('fd-bar-interest');

  if (barPPct) barPPct.textContent = princPct.toFixed(1) + '%';
  if (barIPct) barIPct.textContent = intPct.toFixed(1) + '%';
  if (barP) barP.style.width = princPct.toFixed(1) + '%';
  if (barI) barI.style.width = intPct.toFixed(1) + '%';
}

function resetFd() {
  const depEl = document.getElementById('fd-deposit');
  const rateEl = document.getElementById('fd-rate');
  const yEl = document.getElementById('fd-years');
  const mEl = document.getElementById('fd-months');
  const fEl = document.getElementById('fd-freq');
  if (depEl) depEl.value = '100000';
  if (rateEl) rateEl.value = '7.0';
  if (yEl) yEl.value = '3';
  if (mEl) mEl.value = '0';
  if (fEl) fEl.value = '4';
  calculateFd();
}

// ================= 12. DATE DIFFERENCE CALCULATOR =================
function setDatePreset(days) {
  const startEl = document.getElementById('date-diff-start');
  const endEl = document.getElementById('date-diff-end');
  if (!startEl || !endEl) return;

  const startDate = startEl.value ? new Date(startEl.value) : new Date();
  const endDate = new Date(startDate);
  endDate.setDate(endDate.getDate() + days);

  endEl.value = endDate.toISOString().split('T')[0];
  calculateDateDiff();
}

function calculateDateDiff() {
  const startEl = document.getElementById('date-diff-start');
  const endEl = document.getElementById('date-diff-end');
  const incEndEl = document.getElementById('date-diff-include-end');
  if (!startEl || !endEl) return;

  if (!startEl.value || !endEl.value) return;

  let d1 = new Date(startEl.value + 'T00:00:00');
  let d2 = new Date(endEl.value + 'T00:00:00');

  let isReversed = false;
  if (d1 > d2) {
    const tmp = d1;
    d1 = d2;
    d2 = tmp;
    isReversed = true;
  }

  const includeEnd = incEndEl ? incEndEl.checked : false;

  let y1 = d1.getFullYear(), m1 = d1.getMonth(), day1 = d1.getDate();
  let y2 = d2.getFullYear(), m2 = d2.getMonth(), day2 = d2.getDate();

  let diffYears = y2 - y1;
  let diffMonths = m2 - m1;
  let diffDays = day2 - day1;

  if (diffDays < 0) {
    diffMonths--;
    const prevMonthLastDay = new Date(y2, m2, 0).getDate();
    diffDays += prevMonthLastDay;
  }
  if (diffMonths < 0) {
    diffYears--;
    diffMonths += 12;
  }

  if (includeEnd) {
    diffDays++;
    const currentMonthLastDay = new Date(y2, m2 + 1, 0).getDate();
    if (diffDays >= currentMonthLastDay) {
      diffDays = 0;
      diffMonths++;
      if (diffMonths >= 12) {
        diffMonths = 0;
        diffYears++;
      }
    }
  }

  const oneDayMs = 24 * 60 * 60 * 1000;
  let totalDays = Math.round((d2 - d1) / oneDayMs) + (includeEnd ? 1 : 0);

  let weekdays = 0;
  let weekends = 0;
  let cur = new Date(d1);
  const endCheck = new Date(d2);
  if (!includeEnd) {
    endCheck.setDate(endCheck.getDate() - 1);
  }

  while (cur <= endCheck) {
    const dayOfWeek = cur.getDay();
    if (dayOfWeek === 0 || dayOfWeek === 6) {
      weekends++;
    } else {
      weekdays++;
    }
    cur.setDate(cur.getDate() + 1);
  }

  const totalWeeks = Math.floor(totalDays / 7);
  const remDays = totalDays % 7;
  const totalHours = totalDays * 24;
  const totalMinutes = totalHours * 60;

  const exactEl = document.getElementById('date-diff-exact-val');
  const daysEl = document.getElementById('date-diff-days-val');
  const weeksEl = document.getElementById('date-diff-weeks-val');
  const weekdaysEl = document.getElementById('date-diff-weekdays-val');
  const weekendsEl = document.getElementById('date-diff-weekends-val');
  const hoursEl = document.getElementById('date-diff-hours-val');
  const minsEl = document.getElementById('date-diff-mins-val');
  const leapEl = document.getElementById('date-diff-leap-val');

  const exactStr = `${diffYears} Year${diffYears !== 1 ? 's' : ''}, ${diffMonths} Month${diffMonths !== 1 ? 's' : ''}, ${diffDays} Day${diffDays !== 1 ? 's' : ''}${isReversed ? ' (earlier)' : ''}`;

  if (exactEl) exactEl.textContent = exactStr;
  if (daysEl) daysEl.textContent = `${totalDays.toLocaleString()} Days`;
  if (weeksEl) weeksEl.textContent = `${totalWeeks.toLocaleString()} Weeks and ${remDays} Day${remDays !== 1 ? 's' : ''}`;
  if (weekdaysEl) weekdaysEl.textContent = `${weekdays.toLocaleString()} Weekdays`;
  if (weekendsEl) weekendsEl.textContent = `${weekends.toLocaleString()} Weekend Days`;
  if (hoursEl) hoursEl.textContent = `${totalHours.toLocaleString()} Hours`;
  if (minsEl) minsEl.textContent = `${totalMinutes.toLocaleString()} Minutes`;
  if (leapEl) {
    let hasLeap = false;
    for (let y = y1; y <= y2; y++) {
      if ((y % 4 === 0 && y % 100 !== 0) || (y % 400 === 0)) {
        const leapDay = new Date(y, 1, 29);
        if (leapDay >= d1 && leapDay <= d2) hasLeap = true;
      }
    }
    leapEl.textContent = hasLeap ? 'Includes Leap Year (Feb 29)' : 'Standard calendar interval';
  }
}

function resetDateDiff() {
  const startEl = document.getElementById('date-diff-start');
  const endEl = document.getElementById('date-diff-end');
  const incEndEl = document.getElementById('date-diff-include-end');
  const today = new Date();
  const nextYear = new Date(today);
  nextYear.setFullYear(nextYear.getFullYear() + 1);

  if (startEl) startEl.value = today.toISOString().split('T')[0];
  if (endEl) endEl.value = nextYear.toISOString().split('T')[0];
  if (incEndEl) incEndEl.checked = false;
  calculateDateDiff();
}

// ================= 13. TIME CALCULATOR =================
let currentTimeTab = 0;
let currentTimeOp = 'add';

function switchTimeTab(index) {
  currentTimeTab = index;
  const tabs = [
    document.getElementById('time-tab-0'),
    document.getElementById('time-tab-1'),
    document.getElementById('time-tab-2')
  ];
  const panes = [
    document.getElementById('time-pane-0'),
    document.getElementById('time-pane-1'),
    document.getElementById('time-pane-2')
  ];
  tabs.forEach((t, i) => {
    if (t) {
      if (i === index) t.classList.add('active');
      else t.classList.remove('active');
    }
  });
  panes.forEach((p, i) => {
    if (p) {
      if (i === index) p.classList.add('active');
      else p.classList.remove('active');
    }
  });

  if (index === 0) calculateTime();
  else if (index === 1) calculateTimeAddSub();
  else calculateTimeUnit();
}

function setTimeOp(op) {
  currentTimeOp = op;
  const addBtn = document.getElementById('time-op-add');
  const subBtn = document.getElementById('time-op-sub');
  if (op === 'add') {
    if (addBtn) addBtn.classList.add('active');
    if (subBtn) subBtn.classList.remove('active');
  } else {
    if (subBtn) subBtn.classList.add('active');
    if (addBtn) addBtn.classList.remove('active');
  }
  calculateTimeAddSub();
}

function calculateTime() {
  const startEl = document.getElementById('time-m1-start');
  const endEl = document.getElementById('time-m1-end');
  const nextDayEl = document.getElementById('time-m1-next-day');
  if (!startEl || !endEl) return;

  const sVal = startEl.value;
  const eVal = endEl.value;
  if (!sVal || !eVal) return;

  const [sh, sm] = sVal.split(':').map(Number);
  const [eh, em] = eVal.split(':').map(Number);

  let startSec = (sh * 3600) + (sm * 60);
  let endSec = (eh * 3600) + (em * 60);

  if (nextDayEl && nextDayEl.checked) {
    endSec += 24 * 3600;
  } else if (endSec < startSec) {
    endSec += 24 * 3600;
  }

  const diffSec = endSec - startSec;
  renderTimeResult(diffSec);
}

function calculateTimeAddSub() {
  const h1 = parseInt(document.getElementById('time-m2-h1')?.value || 0, 10);
  const m1 = parseInt(document.getElementById('time-m2-m1')?.value || 0, 10);
  const s1 = parseInt(document.getElementById('time-m2-s1')?.value || 0, 10);

  const h2 = parseInt(document.getElementById('time-m2-h2')?.value || 0, 10);
  const m2 = parseInt(document.getElementById('time-m2-m2')?.value || 0, 10);
  const s2 = parseInt(document.getElementById('time-m2-s2')?.value || 0, 10);

  const sec1 = (h1 * 3600) + (m1 * 60) + s1;
  const sec2 = (h2 * 3600) + (m2 * 60) + s2;

  let totalSec = currentTimeOp === 'add' ? (sec1 + sec2) : (sec1 - sec2);
  renderTimeResult(totalSec);
}

function calculateTimeUnit() {
  const valEl = document.getElementById('time-m3-val');
  const unitEl = document.getElementById('time-m3-unit');
  if (!valEl || !unitEl) return;

  const val = parseFloat(valEl.value) || 0;
  const unit = unitEl.value;
  let sec = 0;
  if (unit === 'hours') sec = val * 3600;
  else if (unit === 'minutes') sec = val * 60;
  else if (unit === 'seconds') sec = val;
  else if (unit === 'days') sec = val * 86400;

  renderTimeResult(Math.round(sec));
}

function renderTimeResult(totalSeconds) {
  const isNegative = totalSeconds < 0;
  const absSec = Math.abs(totalSeconds);

  const h = Math.floor(absSec / 3600);
  const m = Math.floor((absSec % 3600) / 60);
  const s = absSec % 60;

  const decimalHours = (absSec / 3600) * (isNegative ? -1 : 1);
  const totalMins = (absSec / 60) * (isNegative ? -1 : 1);

  const resValEl = document.getElementById('time-res-val');
  const resSubEl = document.getElementById('time-res-sub');
  const resDecEl = document.getElementById('time-res-decimal');
  const resMinsEl = document.getElementById('time-res-mins');
  const resSecsEl = document.getElementById('time-res-secs');

  const prefix = isNegative ? '-' : '';
  if (resValEl) resValEl.textContent = `${prefix}${h}h ${m}m ${s > 0 ? s + 's' : ''}`.trim();
  if (resSubEl) resSubEl.textContent = `${prefix}${h} Hours, ${m} Minutes, ${s} Seconds`;
  if (resDecEl) resDecEl.textContent = `${decimalHours.toFixed(2)} Hours`;
  if (resMinsEl) resMinsEl.textContent = `${Math.round(totalMins).toLocaleString()} Minutes`;
  if (resSecsEl) resSecsEl.textContent = `${(totalSeconds).toLocaleString()} Total Seconds`;
}

function resetTime() {
  const startEl = document.getElementById('time-m1-start');
  const endEl = document.getElementById('time-m1-end');
  const nextDayEl = document.getElementById('time-m1-next-day');
  if (startEl) startEl.value = '09:15';
  if (endEl) endEl.value = '17:45';
  if (nextDayEl) nextDayEl.checked = false;
  calculateTime();
}

function resetTimeAddSub() {
  if (document.getElementById('time-m2-h1')) document.getElementById('time-m2-h1').value = '4';
  if (document.getElementById('time-m2-m1')) document.getElementById('time-m2-m1').value = '45';
  if (document.getElementById('time-m2-s1')) document.getElementById('time-m2-s1').value = '0';
  if (document.getElementById('time-m2-h2')) document.getElementById('time-m2-h2').value = '2';
  if (document.getElementById('time-m2-m2')) document.getElementById('time-m2-m2').value = '30';
  if (document.getElementById('time-m2-s2')) document.getElementById('time-m2-s2').value = '0';
  setTimeOp('add');
}

// ================= 14. UNIT CONVERTER =================
const UC_DEFINITIONS = {
  length: {
    base: 'm',
    units: {
      m: { name: 'Meters (m)', factor: 1 },
      km: { name: 'Kilometers (km)', factor: 1000 },
      cm: { name: 'Centimeters (cm)', factor: 0.01 },
      mm: { name: 'Millimeters (mm)', factor: 0.001 },
      mi: { name: 'Miles (mi)', factor: 1609.344 },
      yd: { name: 'Yards (yd)', factor: 0.9144 },
      ft: { name: 'Feet (ft)', factor: 0.3048 },
      in: { name: 'Inches (in)', factor: 0.0254 }
    },
    defaultFrom: 'm',
    defaultTo: 'ft'
  },
  weight: {
    base: 'kg',
    units: {
      kg: { name: 'Kilograms (kg)', factor: 1 },
      g: { name: 'Grams (g)', factor: 0.001 },
      mg: { name: 'Milligrams (mg)', factor: 0.000001 },
      lb: { name: 'Pounds (lbs)', factor: 0.45359237 },
      oz: { name: 'Ounces (oz)', factor: 0.028349523125 },
      ton: { name: 'Metric Tons (t)', factor: 1000 }
    },
    defaultFrom: 'kg',
    defaultTo: 'lb'
  },
  temperature: {
    isSpecial: true,
    units: {
      c: { name: 'Celsius (°C)' },
      f: { name: 'Fahrenheit (°F)' },
      k: { name: 'Kelvin (K)' }
    },
    defaultFrom: 'c',
    defaultTo: 'f'
  },
  area: {
    base: 'sqm',
    units: {
      sqm: { name: 'Square Meters (m²)', factor: 1 },
      sqkm: { name: 'Square Kilometers (km²)', factor: 1000000 },
      sqft: { name: 'Square Feet (ft²)', factor: 0.09290304 },
      sqyd: { name: 'Square Yards (yd²)', factor: 0.83612736 },
      acre: { name: 'Acres (ac)', factor: 4046.8564224 },
      hectare: { name: 'Hectares (ha)', factor: 10000 }
    },
    defaultFrom: 'sqm',
    defaultTo: 'sqft'
  },
  speed: {
    base: 'kmh',
    units: {
      kmh: { name: 'Kilometers per hour (km/h)', factor: 1 },
      mph: { name: 'Miles per hour (mph)', factor: 1.609344 },
      ms: { name: 'Meters per second (m/s)', factor: 3.6 },
      knot: { name: 'Knots (kn)', factor: 1.852 }
    },
    defaultFrom: 'kmh',
    defaultTo: 'mph'
  },
  volume: {
    base: 'l',
    units: {
      l: { name: 'Liters (L)', factor: 1 },
      ml: { name: 'Milliliters (mL)', factor: 0.001 },
      cum: { name: 'Cubic Meters (m³)', factor: 1000 },
      gal: { name: 'US Gallons (gal)', factor: 3.785411784 },
      floz: { name: 'US Fluid Ounces (fl oz)', factor: 0.0295735295625 }
    },
    defaultFrom: 'l',
    defaultTo: 'gal'
  }
};

function changeUcCategory() {
  const cat = document.getElementById('uc-category')?.value || 'length';
  const def = UC_DEFINITIONS[cat];
  if (!def) return;

  const fromSel = document.getElementById('uc-from');
  const toSel = document.getElementById('uc-to');
  if (!fromSel || !toSel) return;

  fromSel.innerHTML = '';
  toSel.innerHTML = '';

  Object.keys(def.units).forEach(key => {
    const opt1 = document.createElement('option');
    opt1.value = key;
    opt1.textContent = def.units[key].name;
    fromSel.appendChild(opt1);

    const opt2 = document.createElement('option');
    opt2.value = key;
    opt2.textContent = def.units[key].name;
    toSel.appendChild(opt2);
  });

  fromSel.value = def.defaultFrom;
  toSel.value = def.defaultTo;
  convertUnits();
}

function swapUnits() {
  const fromSel = document.getElementById('uc-from');
  const toSel = document.getElementById('uc-to');
  if (!fromSel || !toSel) return;
  const tmp = fromSel.value;
  fromSel.value = toSel.value;
  toSel.value = tmp;
  convertUnits();
}

function convertUnits() {
  const cat = document.getElementById('uc-category')?.value || 'length';
  const valEl = document.getElementById('uc-value');
  const fromSel = document.getElementById('uc-from');
  const toSel = document.getElementById('uc-to');
  if (!valEl || !fromSel || !toSel) return;

  const val = parseFloat(valEl.value) || 0;
  const from = fromSel.value;
  const to = toSel.value;
  const def = UC_DEFINITIONS[cat];
  if (!def) return;

  let result = 0;
  let formulaText = '';

  if (cat === 'temperature') {
    let celsius = 0;
    if (from === 'c') celsius = val;
    else if (from === 'f') celsius = (val - 32) * (5 / 9);
    else if (from === 'k') celsius = val - 273.15;

    if (to === 'c') result = celsius;
    else if (to === 'f') result = (celsius * (9 / 5)) + 32;
    else if (to === 'k') result = celsius + 273.15;

    formulaText = `${val} ${def.units[from].name} = ${result.toFixed(4).replace(/\.?0+$/, '')} ${def.units[to].name}`;
  } else {
    const fromFactor = def.units[from].factor;
    const toFactor = def.units[to].factor;
    const inBase = val * fromFactor;
    result = inBase / toFactor;
    const mult = fromFactor / toFactor;
    formulaText = `${val} ${def.units[from].name.split(' ')[0]} = ${formatUnitNum(result)} ${def.units[to].name.split(' ')[0]} (Factor: ×${formatUnitNum(mult)})`;
  }

  const resValEl = document.getElementById('uc-res-val');
  const resFormEl = document.getElementById('uc-res-formula');
  if (resValEl) {
    const toUnitName = def.units[to].name;
    resValEl.textContent = `${formatUnitNum(result)} ${toUnitName.split(' ')[0]}`;
  }
  if (resFormEl) resFormEl.textContent = formulaText;

  const tableBody = document.getElementById('uc-table-body');
  if (tableBody) {
    let rowsHtml = '';
    Object.keys(def.units).forEach(key => {
      let rowVal = 0;
      if (cat === 'temperature') {
        let c = 0;
        if (from === 'c') c = val;
        else if (from === 'f') c = (val - 32) * (5 / 9);
        else if (from === 'k') c = val - 273.15;

        if (key === 'c') rowVal = c;
        else if (key === 'f') rowVal = (c * (9 / 5)) + 32;
        else if (key === 'k') rowVal = c + 273.15;
      } else {
        const fromFactor = def.units[from].factor;
        const keyFactor = def.units[key].factor;
        rowVal = (val * fromFactor) / keyFactor;
      }
      const isSelected = key === to ? 'style="font-weight:700; color:var(--primary); background:var(--primary-bg);"' : '';
      rowsHtml += `<tr ${isSelected}>
        <td>${def.units[key].name}</td>
        <td>${formatUnitNum(rowVal)}</td>
      </tr>`;
    });
    tableBody.innerHTML = rowsHtml;
  }
}

function formatUnitNum(num) {
  if (Math.abs(num) >= 1e9 || (Math.abs(num) < 1e-4 && num !== 0)) {
    return num.toExponential(4);
  }
  return parseFloat(num.toFixed(6)).toLocaleString('en-US', { maximumFractionDigits: 6 });
}

function resetUnits() {
  const valEl = document.getElementById('uc-value');
  if (valEl) valEl.value = '10';
  changeUcCategory();
}

// ================= 15. AVERAGE CALCULATOR =================
function setAvgSample(type) {
  const inputEl = document.getElementById('avg-input');
  if (!inputEl) return;
  if (type === 'integers') {
    inputEl.value = '1, 2, 3, 4, 5, 6, 7, 8, 9, 10';
  } else if (type === 'scores') {
    inputEl.value = '78, 85, 92, 65, 88, 95, 82, 90, 74, 88';
  } else if (type === 'temps') {
    inputEl.value = '28.5, 30.2, 31.0, 29.4, 27.8, 32.1, 30.5';
  }
  calculateAverage();
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
  calculateSalesTax();
}

function calculateAverage() {
  const inputEl = document.getElementById('avg-input');
  const errEl = document.getElementById('avg-error');
  if (!inputEl) return;

  const raw = inputEl.value;
  const tokens = raw.split(/[\s,;\n\r]+/).map(s => s.trim()).filter(Boolean);
  const nums = [];
  for (let i = 0; i < tokens.length; i++) {
    const n = parseFloat(tokens[i]);
    if (!isNaN(n)) nums.push(n);
  }

  if (nums.length === 0) {
    if (errEl) {
      errEl.textContent = 'Please enter at least one valid number.';
      errEl.style.display = 'block';
    }
    return;
  }
  if (errEl) errEl.style.display = 'none';

  const sorted = [...nums].sort((a, b) => a - b);
  const count = sorted.length;
  const sum = sorted.reduce((acc, curr) => acc + curr, 0);
  const mean = sum / count;

  let median = 0;
  const mid = Math.floor(count / 2);
  if (count % 2 !== 0) {
    median = sorted[mid];
  } else {
    median = (sorted[mid - 1] + sorted[mid]) / 2;
  }

  const freqMap = {};
  let maxFreq = 0;
  sorted.forEach(num => {
    freqMap[num] = (freqMap[num] || 0) + 1;
    if (freqMap[num] > maxFreq) maxFreq = freqMap[num];
  });

  let modeText = 'No Mode (All Unique)';
  if (maxFreq > 1) {
    const modes = Object.keys(freqMap).filter(k => freqMap[k] === maxFreq).map(Number);
    if (modes.length === count) {
      modeText = 'No Mode (All Equal)';
    } else if (modes.length <= 4) {
      modeText = modes.join(', ') + ` (${maxFreq}×)`;
    } else {
      modeText = `Multimodal (${modes.length} modes)`;
    }
  }

  const min = sorted[0];
  const max = sorted[count - 1];
  const range = max - min;

  let sampleStd = 0;
  let popStd = 0;
  if (count > 1) {
    const varianceSum = sorted.reduce((acc, curr) => acc + Math.pow(curr - mean, 2), 0);
    sampleStd = Math.sqrt(varianceSum / (count - 1));
    popStd = Math.sqrt(varianceSum / count);
  }

  let geoMeanText = 'N/A (Requires > 0)';
  const allPositive = sorted.every(n => n > 0);
  if (allPositive) {
    const logSum = sorted.reduce((acc, curr) => acc + Math.log(curr), 0);
    const geoMean = Math.exp(logSum / count);
    geoMeanText = geoMean.toFixed(2);
  }

  const meanEl = document.getElementById('avg-mean-val');
  const medianEl = document.getElementById('avg-median-val');
  const modeEl = document.getElementById('avg-mode-val');
  const sumEl = document.getElementById('avg-sum-val');
  const countEl = document.getElementById('avg-count-val');
  const rangeEl = document.getElementById('avg-range-val');
  const minMaxEl = document.getElementById('avg-minmax-sub');
  const stdEl = document.getElementById('avg-std-val');
  const popStdEl = document.getElementById('avg-popstd-sub');
  const geoMeanEl = document.getElementById('avg-geomean-val');
  const pillsEl = document.getElementById('avg-sorted-pills');

  if (meanEl) meanEl.textContent = mean.toFixed(2);
  if (medianEl) medianEl.textContent = median.toFixed(2);
  if (modeEl) modeEl.textContent = modeText;
  if (sumEl) sumEl.textContent = sum.toLocaleString('en-US', { maximumFractionDigits: 2 });
  if (countEl) countEl.textContent = `Count (n): ${count} number${count !== 1 ? 's' : ''}`;
  if (rangeEl) rangeEl.textContent = `Range: ${range.toFixed(2)}`;
  if (minMaxEl) minMaxEl.textContent = `Min: ${min} | Max: ${max}`;
  if (stdEl) stdEl.textContent = sampleStd.toFixed(2);
  if (popStdEl) popStdEl.textContent = `Population σ: ${popStd.toFixed(2)}`;
  if (geoMeanEl) geoMeanEl.textContent = geoMeanText;

  if (pillsEl) {
    pillsEl.innerHTML = sorted.map(n => `<span class="data-num-pill">${n}</span>`).join('');
  }
}

function resetAverage() {
  const inputEl = document.getElementById('avg-input');
  if (inputEl) inputEl.value = '';
  calculateAverage();
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
  calculateSalesTax();
}



// ============================================================================
// ==================== 20 NEW TOOLS JAVASCRIPT IMPLEMENTATIONS ================
// ============================================================================

// Helper utility functions for new tools
function formatNumberWithCommas(num, dec = 2) {
  if (isNaN(num) || !isFinite(num)) return '0';
  const parts = Number(num).toFixed(dec).split('.');
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  return dec > 0 ? parts.join('.') : parts[0];
}

function formatInrLakhs(num, dec = 0) {
  if (isNaN(num) || !isFinite(num)) return '₹0';
  const n = Math.round(num);
  let str = n.toString();
  let lastThree = str.substring(str.length - 3);
  let otherNumbers = str.substring(0, str.length - 3);
  if (otherNumbers !== '') {
    lastThree = ',' + lastThree;
  }
  return '₹' + otherNumbers.replace(/\B(?=(\d{2})+(?!\d))/g, ',') + lastThree;
}

// ----------------------------------------------------------------------------
// 1. LOAN INTEREST CALCULATOR
// ----------------------------------------------------------------------------
let liCurrency = 'INR';
let liTenureUnit = 'years';
let liType = 'reducing';

function setLiCurrency(curr) {
  liCurrency = curr;
  const inrBtn = document.getElementById('li-curr-inr');
  const usdBtn = document.getElementById('li-curr-usd');
  const label = document.getElementById('li-principal-label');
  if (inrBtn && usdBtn) {
    if (curr === 'INR') {
      inrBtn.classList.add('active');
      usdBtn.classList.remove('active');
      if (label) label.textContent = 'Loan Principal (₹)';
    } else {
      usdBtn.classList.add('active');
      inrBtn.classList.remove('active');
      if (label) label.textContent = 'Loan Principal ($)';
    }
  }
  calculateLoanInterest();
}

function setLiTenureUnit(unit) {
  liTenureUnit = unit;
  const yrBtn = document.getElementById('li-tenure-yr');
  const moBtn = document.getElementById('li-tenure-mo');
  if (yrBtn && moBtn) {
    if (unit === 'years') {
      yrBtn.classList.add('active');
      moBtn.classList.remove('active');
    } else {
      moBtn.classList.add('active');
      yrBtn.classList.remove('active');
    }
  }
  calculateLoanInterest();
}

function setLiType(type) {
  liType = type;
  const redBtn = document.getElementById('li-type-reducing');
  const flatBtn = document.getElementById('li-type-flat');
  if (redBtn && flatBtn) {
    if (type === 'reducing') {
      redBtn.classList.add('active');
      flatBtn.classList.remove('active');
    } else {
      flatBtn.classList.add('active');
      redBtn.classList.remove('active');
    }
  }
  calculateLoanInterest();
}

function calculateLoanInterest() {
  const pInput = document.getElementById('li-principal');
  const rInput = document.getElementById('li-rate');
  const tInput = document.getElementById('li-tenure');
  if (!pInput || !rInput || !tInput) return;

  const P = Math.max(0, parseFloat(pInput.value) || 0);
  const annualRate = Math.max(0, parseFloat(rInput.value) || 0);
  const tenureInput = Math.max(1, parseFloat(tInput.value) || 1);

  const months = liTenureUnit === 'years' ? tenureInput * 12 : tenureInput;
  const years = months / 12;

  let totalInterest = 0;
  let totalAmount = P;
  let monthlyPayment = 0;

  if (P > 0 && annualRate > 0 && months > 0) {
    if (liType === 'reducing') {
      const monthlyRate = annualRate / 12 / 100;
      const emi = (P * monthlyRate * Math.pow(1 + monthlyRate, months)) / (Math.pow(1 + monthlyRate, months) - 1);
      monthlyPayment = emi;
      totalAmount = emi * months;
      totalInterest = totalAmount - P;
    } else {
      // Flat rate
      totalInterest = P * (annualRate / 100) * years;
      totalAmount = P + totalInterest;
      monthlyPayment = totalAmount / months;
    }
  }

  const ratio = P > 0 ? (totalInterest / P) * 100 : 0;
  const avgAnnual = years > 0 ? totalInterest / years : 0;
  const sym = liCurrency === 'INR' ? '₹' : '$';

  const formatMoney = (val) => liCurrency === 'INR' ? formatInrLakhs(val) : '$' + formatNumberWithCommas(val, 0);

  const intEl = document.getElementById('li-total-interest-val');
  if (intEl) intEl.textContent = formatMoney(totalInterest);

  const ratioEl = document.getElementById('li-ratio-val');
  if (ratioEl) ratioEl.textContent = ratio.toFixed(2) + '% of loan';

  const monthlyEl = document.getElementById('li-monthly-val');
  if (monthlyEl) monthlyEl.textContent = formatMoney(monthlyPayment) + '/mo';

  const pEl = document.getElementById('li-res-principal');
  if (pEl) pEl.textContent = formatMoney(P);

  const totEl = document.getElementById('li-res-total');
  if (totEl) totEl.textContent = formatMoney(totalAmount);

  const annEl = document.getElementById('li-res-annual-interest');
  if (annEl) annEl.textContent = formatMoney(avgAnnual) + '/yr';

  const aprEl = document.getElementById('li-res-eff-apr');
  if (aprEl) aprEl.textContent = annualRate.toFixed(2) + '%';
}

function resetLoanInterest() {
  const pInput = document.getElementById('li-principal');
  const rInput = document.getElementById('li-rate');
  const tInput = document.getElementById('li-tenure');
  if (pInput) pInput.value = '500000';
  if (rInput) rInput.value = '9.5';
  if (tInput) tInput.value = '5';
  setLiCurrency('INR');
  setLiTenureUnit('years');
  setLiType('reducing');
  calculateLoanInterest();
}

// ----------------------------------------------------------------------------
// 2. LOAN ELIGIBILITY CALCULATOR
// ----------------------------------------------------------------------------
function calculateLoanEligibility() {
  const incInput = document.getElementById('le-income');
  const emiInput = document.getElementById('le-emis');
  const rInput = document.getElementById('le-rate');
  const tInput = document.getElementById('le-tenure');
  const foirSelect = document.getElementById('le-foir');
  if (!incInput || !emiInput || !rInput || !tInput || !foirSelect) return;

  const income = Math.max(0, parseFloat(incInput.value) || 0);
  const existingEmis = Math.max(0, parseFloat(emiInput.value) || 0);
  const annualRate = Math.max(0.1, parseFloat(rInput.value) || 8.5);
  const years = Math.max(1, parseFloat(tInput.value) || 20);
  const foirPct = parseFloat(foirSelect.value) || 50;

  const maxTotalEmi = income * (foirPct / 100);
  const permissibleNewEmi = Math.max(0, maxTotalEmi - existingEmis);
  const currentFoirUsed = income > 0 ? (existingEmis / income) * 100 : 0;
  const disposable = Math.max(0, income - existingEmis - permissibleNewEmi);

  const n = years * 12;
  const r = annualRate / 12 / 100;

  function pvLoan(emiAmount) {
    if (emiAmount <= 0 || r <= 0) return 0;
    return (emiAmount * (Math.pow(1 + r, n) - 1)) / (r * Math.pow(1 + r, n));
  }

  const maxLoan = pvLoan(permissibleNewEmi);
  const consEmi = Math.max(0, (income * 0.40) - existingEmis);
  const stretchEmi = Math.max(0, (income * 0.60) - existingEmis);

  const consLoan = pvLoan(consEmi);
  const stretchLoan = pvLoan(stretchEmi);

  const maxLoanEl = document.getElementById('le-max-loan-val');
  if (maxLoanEl) maxLoanEl.textContent = formatInrLakhs(maxLoan);

  const maxEmiEl = document.getElementById('le-max-emi-val');
  if (maxEmiEl) maxEmiEl.textContent = formatInrLakhs(permissibleNewEmi) + '/mo';

  const foirEl = document.getElementById('le-current-foir-val');
  if (foirEl) foirEl.textContent = currentFoirUsed.toFixed(1) + '%';

  const totCapEl = document.getElementById('le-res-total-cap');
  if (totCapEl) totCapEl.textContent = formatInrLakhs(maxTotalEmi) + '/mo';

  const dispEl = document.getElementById('le-res-disposable');
  if (dispEl) dispEl.textContent = formatInrLakhs(disposable) + '/mo';

  const consEl = document.getElementById('le-res-conservative');
  if (consEl) consEl.textContent = formatInrLakhs(consLoan);

  const stretchEl = document.getElementById('le-res-stretch');
  if (stretchEl) stretchEl.textContent = formatInrLakhs(stretchLoan);
}

function resetLoanEligibility() {
  const inc = document.getElementById('le-income');
  const emi = document.getElementById('le-emis');
  const r = document.getElementById('le-rate');
  const t = document.getElementById('le-tenure');
  const foir = document.getElementById('le-foir');
  if (inc) inc.value = '75000';
  if (emi) emi.value = '10000';
  if (r) r.value = '8.75';
  if (t) t.value = '20';
  if (foir) foir.value = '50';
  calculateLoanEligibility();
}

// ----------------------------------------------------------------------------
// 3. LOAN TENURE CALCULATOR
// ----------------------------------------------------------------------------
function calculateLoanTenure() {
  const pInput = document.getElementById('lt-principal');
  const rInput = document.getElementById('lt-rate');
  const emiInput = document.getElementById('lt-emi');
  if (!pInput || !rInput || !emiInput) return;

  const P = Math.max(0, parseFloat(pInput.value) || 0);
  const annualRate = Math.max(0.1, parseFloat(rInput.value) || 9.0);
  const EMI = Math.max(1, parseFloat(emiInput.value) || 15000);

  const r = annualRate / 12 / 100;
  const minEmiRequired = P * r;

  function calcMonths(emiVal) {
    if (emiVal <= P * r) return Infinity;
    return -Math.log(1 - (P * r / emiVal)) / Math.log(1 + r);
  }

  const months = calcMonths(EMI);

  const yEl = document.getElementById('lt-tenure-years-val');
  const mEl = document.getElementById('lt-tenure-months-val');
  const intEl = document.getElementById('lt-total-interest-val');
  const totEl = document.getElementById('lt-total-payment-val');
  const minEmiEl = document.getElementById('lt-res-min-emi');
  const speedEl = document.getElementById('lt-res-speed');
  const extraTenureEl = document.getElementById('lt-res-extra-tenure');
  const extraSavEl = document.getElementById('lt-res-extra-savings');

  if (minEmiEl) minEmiEl.textContent = formatInrLakhs(Math.ceil(minEmiRequired) + 1);

  if (!isFinite(months) || months <= 0) {
    if (yEl) yEl.textContent = 'Payment Too Low!';
    if (mEl) mEl.textContent = 'Must exceed interest of ' + formatInrLakhs(minEmiRequired);
    if (intEl) intEl.textContent = 'Infinite';
    if (totEl) totEl.textContent = 'Infinite';
    if (speedEl) speedEl.textContent = '₹0';
    if (extraTenureEl) extraTenureEl.textContent = 'N/A';
    if (extraSavEl) extraSavEl.textContent = 'N/A';
    return;
  }

  const totalMonths = Math.ceil(months);
  const yrs = Math.floor(totalMonths / 12);
  const remMos = totalMonths % 12;

  const totalPayment = EMI * totalMonths;
  const totalInterest = Math.max(0, totalPayment - P);

  if (yEl) yEl.textContent = yrs + ' Years, ' + remMos + ' Months';
  if (mEl) mEl.textContent = totalMonths + ' Total Monthly Payments';
  if (intEl) intEl.textContent = formatInrLakhs(totalInterest);
  if (totEl) totEl.textContent = formatInrLakhs(totalPayment);
  if (speedEl) speedEl.textContent = formatInrLakhs(EMI - minEmiRequired) + '/mo';

  // Extra payment calculation (+ ₹2,000)
  const extraEmi = EMI + 2000;
  const extraMonths = calcMonths(extraEmi);
  if (isFinite(extraMonths)) {
    const eTotalMos = Math.ceil(extraMonths);
    const eYrs = Math.floor(eTotalMos / 12);
    const eRem = eTotalMos % 12;
    const eTotalPay = extraEmi * eTotalMos;
    const eInterest = Math.max(0, eTotalPay - P);
    const savings = Math.max(0, totalInterest - eInterest);
    if (extraTenureEl) extraTenureEl.textContent = eYrs + ' Yrs, ' + eRem + ' Mos';
    if (extraSavEl) extraSavEl.textContent = formatInrLakhs(savings);
  }
}

function resetLoanTenure() {
  const p = document.getElementById('lt-principal');
  const r = document.getElementById('lt-rate');
  const emi = document.getElementById('lt-emi');
  if (p) p.value = '1000000';
  if (r) r.value = '9.0';
  if (emi) emi.value = '15000';
  calculateLoanTenure();
}

// ----------------------------------------------------------------------------
// 4. SALARY CALCULATOR
// ----------------------------------------------------------------------------
let salInputType = 'ctc';

function setSalInputType(type) {
  salInputType = type;
  const ctcBtn = document.getElementById('sal-type-ctc');
  const moBtn = document.getElementById('sal-type-monthly');
  const label = document.getElementById('sal-amount-label');
  const input = document.getElementById('sal-amount');
  if (ctcBtn && moBtn) {
    if (type === 'ctc') {
      ctcBtn.classList.add('active');
      moBtn.classList.remove('active');
      if (label) label.textContent = 'Annual CTC (₹)';
      if (input && input.value === '100000') input.value = '1200000';
    } else {
      moBtn.classList.add('active');
      ctcBtn.classList.remove('active');
      if (label) label.textContent = 'Monthly Gross Salary (₹)';
      if (input && input.value === '1200000') input.value = '100000';
    }
  }
  calculateSalary();
}

function calculateSalary() {
  const amtInput = document.getElementById('sal-amount');
  const basicPctSelect = document.getElementById('sal-basic-pct');
  const pfSelect = document.getElementById('sal-pf-type');
  const ptInput = document.getElementById('sal-pt');
  const otherInput = document.getElementById('sal-other-ded');
  const taxInput = document.getElementById('sal-tax-est');
  if (!amtInput) return;

  const inputAmt = Math.max(0, parseFloat(amtInput.value) || 0);
  const basicPct = parseFloat(basicPctSelect ? basicPctSelect.value : 50) || 50;
  const pfChoice = pfSelect ? pfSelect.value : '12';
  const pt = Math.max(0, parseFloat(ptInput ? ptInput.value : 200) || 0);
  const otherDed = Math.max(0, parseFloat(otherInput ? otherInput.value : 0) || 0);
  const monthlyTds = Math.max(0, parseFloat(taxInput ? taxInput.value : 0) || 0);

  let monthlyGross = 0;
  let employerPf = 0;

  if (salInputType === 'ctc') {
    // Standard Indian structure: CTC = Monthly Gross * 12 + Employer PF * 12
    // If Basic is 50%, Gross = CTC / (1 + 0.50 * 0.12) = CTC / 1.06
    const pfFactor = pfChoice === '12' ? (basicPct / 100) * 0.12 : 0;
    const annualGross = pfChoice === 'cap' ? Math.max(0, inputAmt - (1800 * 12)) : inputAmt / (1 + pfFactor);
    monthlyGross = annualGross / 12;
    employerPf = pfChoice === 'cap' ? 1800 : (monthlyGross * (basicPct / 100)) * (pfChoice === '12' ? 0.12 : 0);
  } else {
    monthlyGross = inputAmt;
    employerPf = (monthlyGross * (basicPct / 100)) * (pfChoice === '12' ? 0.12 : (pfChoice === 'cap' ? 0 : 0));
    if (pfChoice === 'cap') employerPf = 1800;
  }

  const monthlyBasic = monthlyGross * (basicPct / 100);
  let employeePf = 0;
  if (pfChoice === '12') {
    employeePf = monthlyBasic * 0.12;
  } else if (pfChoice === 'cap') {
    employeePf = 1800;
  }

  const totalDeductions = employeePf + pt + otherDed + monthlyTds;
  const netInHand = Math.max(0, monthlyGross - totalDeductions);
  const annualNet = netInHand * 12;

  const netEl = document.getElementById('sal-net-month-val');
  if (netEl) netEl.textContent = formatInrLakhs(netInHand);

  const netYrEl = document.getElementById('sal-net-year-val');
  if (netYrEl) netYrEl.textContent = formatInrLakhs(annualNet);

  const totDedEl = document.getElementById('sal-total-ded-val');
  if (totDedEl) totDedEl.textContent = formatInrLakhs(totalDeductions) + '/mo';

  const grossEl = document.getElementById('sal-res-gross');
  if (grossEl) grossEl.textContent = formatInrLakhs(monthlyGross);

  const epfEl = document.getElementById('sal-res-epf');
  if (epfEl) epfEl.textContent = formatInrLakhs(employeePf) + '/mo';

  const emPfEl = document.getElementById('sal-res-employer-epf');
  if (emPfEl) emPfEl.textContent = formatInrLakhs(employerPf) + '/mo';

  const statEl = document.getElementById('sal-res-statutory');
  if (statEl) statEl.textContent = formatInrLakhs(pt + otherDed + monthlyTds) + '/mo';
}

function resetSalary() {
  const amt = document.getElementById('sal-amount');
  const basic = document.getElementById('sal-basic-pct');
  const pf = document.getElementById('sal-pf-type');
  const pt = document.getElementById('sal-pt');
  const other = document.getElementById('sal-other-ded');
  const tax = document.getElementById('sal-tax-est');
  if (amt) amt.value = '1200000';
  if (basic) basic.value = '50';
  if (pf) pf.value = '12';
  if (pt) pt.value = '200';
  if (other) other.value = '1000';
  if (tax) tax.value = '5000';
  setSalInputType('ctc');
  calculateSalary();
}

// ----------------------------------------------------------------------------
// 5. OVERTIME PAY CALCULATOR
// ----------------------------------------------------------------------------
let otCurrency = 'INR';

function setOtCurrency(curr) {
  otCurrency = curr;
  const inrBtn = document.getElementById('ot-curr-inr');
  const usdBtn = document.getElementById('ot-curr-usd');
  const label = document.getElementById('ot-rate-label');
  if (inrBtn && usdBtn) {
    if (curr === 'INR') {
      inrBtn.classList.add('active');
      usdBtn.classList.remove('active');
      if (label) label.textContent = 'Regular Hourly Rate (₹/hour)';
    } else {
      usdBtn.classList.add('active');
      inrBtn.classList.remove('active');
      if (label) label.textContent = 'Regular Hourly Rate ($/hour)';
    }
  }
  calculateOvertime();
}

function calculateOvertime() {
  const rateInput = document.getElementById('ot-hourly-rate');
  const regInput = document.getElementById('ot-reg-hours');
  const ot15Input = document.getElementById('ot-15-hours');
  const ot20Input = document.getElementById('ot-20-hours');
  if (!rateInput || !regInput || !ot15Input || !ot20Input) return;

  const rate = Math.max(0, parseFloat(rateInput.value) || 0);
  const regHours = Math.max(0, parseFloat(regInput.value) || 0);
  const ot15Hours = Math.max(0, parseFloat(ot15Input.value) || 0);
  const ot20Hours = Math.max(0, parseFloat(ot20Input.value) || 0);

  const regPay = regHours * rate;
  const ot15Pay = ot15Hours * (rate * 1.5);
  const ot20Pay = ot20Hours * (rate * 2.0);

  const totalHours = regHours + ot15Hours + ot20Hours;
  const totalOtPremium = ot15Pay + ot20Pay;
  const totalPay = regPay + totalOtPremium;
  const blendedRate = totalHours > 0 ? totalPay / totalHours : rate;
  const otShare = totalPay > 0 ? (totalOtPremium / totalPay) * 100 : 0;

  const fmt = (val) => otCurrency === 'INR' ? formatInrLakhs(val) : '$' + formatNumberWithCommas(val, 2);

  const totPayEl = document.getElementById('ot-total-pay-val');
  if (totPayEl) totPayEl.textContent = fmt(totalPay);

  const totHrsEl = document.getElementById('ot-total-hours-val');
  if (totHrsEl) totHrsEl.textContent = totalHours.toFixed(1) + ' Total Hours';

  const totOtEl = document.getElementById('ot-total-ot-val');
  if (totOtEl) totOtEl.textContent = fmt(totalOtPremium);

  const blEl = document.getElementById('ot-blended-rate-val');
  if (blEl) blEl.textContent = fmt(blendedRate) + '/hr';

  const regEl = document.getElementById('ot-res-reg');
  if (regEl) regEl.textContent = fmt(regPay);

  const ot15El = document.getElementById('ot-res-15');
  if (ot15El) ot15El.textContent = fmt(ot15Pay);

  const ot20El = document.getElementById('ot-res-20');
  if (ot20El) ot20El.textContent = fmt(ot20Pay);

  const shareEl = document.getElementById('ot-res-share');
  if (shareEl) shareEl.textContent = otShare.toFixed(2) + '%';
}

function resetOvertime() {
  const r = document.getElementById('ot-hourly-rate');
  const reg = document.getElementById('ot-reg-hours');
  const o15 = document.getElementById('ot-15-hours');
  const o20 = document.getElementById('ot-20-hours');
  if (r) r.value = '250';
  if (reg) reg.value = '40';
  if (o15) o15.value = '10';
  if (o20) o20.value = '4';
  setOtCurrency('INR');
  calculateOvertime();
}

// ----------------------------------------------------------------------------
// 6. TAX CALCULATOR
// ----------------------------------------------------------------------------
function calculateTax() {
  const incInput = document.getElementById('tax-income');
  const ageSelect = document.getElementById('tax-age');
  const c80Input = document.getElementById('tax-80c');
  const d80Input = document.getElementById('tax-80d');
  const hraInput = document.getElementById('tax-hra');
  if (!incInput) return;

  const gross = Math.max(0, parseFloat(incInput.value) || 0);
  const age = ageSelect ? ageSelect.value : 'general';
  const ded80c = Math.min(150000, Math.max(0, parseFloat(c80Input ? c80Input.value : 0) || 0));
  const ded80d = Math.max(0, parseFloat(d80Input ? d80Input.value : 0) || 0);
  const hra = Math.max(0, parseFloat(hraInput ? hraInput.value : 0) || 0);

  // New Tax Regime Calculation (FY 2024-25 / 2025-26)
  const newStdDed = 75000;
  const newTaxable = Math.max(0, gross - newStdDed);
  let newBaseTax = 0;

  if (newTaxable <= 300000) {
    newBaseTax = 0;
  } else if (newTaxable <= 700000) {
    newBaseTax = (newTaxable - 300000) * 0.05;
  } else if (newTaxable <= 1000000) {
    newBaseTax = (400000 * 0.05) + ((newTaxable - 700000) * 0.10);
  } else if (newTaxable <= 1200000) {
    newBaseTax = (400000 * 0.05) + (300000 * 0.10) + ((newTaxable - 1000000) * 0.15);
  } else if (newTaxable <= 1500000) {
    newBaseTax = (400000 * 0.05) + (300000 * 0.10) + (200000 * 0.15) + ((newTaxable - 1200000) * 0.20);
  } else {
    newBaseTax = (400000 * 0.05) + (300000 * 0.10) + (200000 * 0.15) + (300000 * 0.20) + ((newTaxable - 1500000) * 0.30);
  }

  // Section 87A rebate in New Regime for taxable income <= 7 Lakhs
  if (newTaxable <= 700000) {
    newBaseTax = 0;
  }

  const newCess = newBaseTax * 0.04;
  const newTotalTax = newBaseTax + newCess;

  // Old Tax Regime Calculation
  const oldStdDed = 50000;
  const oldTaxable = Math.max(0, gross - (oldStdDed + ded80c + ded80d + hra));
  let oldBaseTax = 0;
  const basicExemption = age === 'super' ? 500000 : (age === 'senior' ? 300000 : 250000);

  if (oldTaxable <= basicExemption) {
    oldBaseTax = 0;
  } else if (oldTaxable <= 500000) {
    oldBaseTax = (oldTaxable - basicExemption) * 0.05;
  } else if (oldTaxable <= 1000000) {
    oldBaseTax = ((500000 - basicExemption) * 0.05) + ((oldTaxable - 500000) * 0.20);
  } else {
    oldBaseTax = ((500000 - basicExemption) * 0.05) + (500000 * 0.20) + ((oldTaxable - 1000000) * 0.30);
  }

  // Section 87A rebate in Old Regime for taxable income <= 5 Lakhs
  if (oldTaxable <= 500000) {
    oldBaseTax = 0;
  }

  const oldCess = oldBaseTax * 0.04;
  const oldTotalTax = oldBaseTax + oldCess;

  const diff = Math.abs(newTotalTax - oldTotalTax);
  const betterText = newTotalTax <= oldTotalTax ? 'New Regime is Better' : 'Old Regime is Better';
  const saveText = diff === 0 ? 'Tax is identical' : 'Saves ' + formatInrLakhs(diff);

  const betterEl = document.getElementById('tax-better-regime-val');
  if (betterEl) betterEl.textContent = betterText;

  const saveEl = document.getElementById('tax-savings-diff-val');
  if (saveEl) saveEl.textContent = saveText;

  const newTotEl = document.getElementById('tax-new-total-val');
  if (newTotEl) newTotEl.textContent = formatInrLakhs(newTotalTax);

  const oldTotEl = document.getElementById('tax-old-total-val');
  if (oldTotEl) oldTotEl.textContent = formatInrLakhs(oldTotalTax);

  const newTaxableEl = document.getElementById('tax-new-taxable');
  if (newTaxableEl) newTaxableEl.textContent = formatInrLakhs(newTaxable);

  const oldTaxableEl = document.getElementById('tax-old-taxable');
  if (oldTaxableEl) oldTaxableEl.textContent = formatInrLakhs(oldTaxable);

  const newEffEl = document.getElementById('tax-new-eff-rate');
  if (newEffEl) newEffEl.textContent = gross > 0 ? ((newTotalTax / gross) * 100).toFixed(2) + '%' : '0.00%';

  const oldEffEl = document.getElementById('tax-old-eff-rate');
  if (oldEffEl) oldEffEl.textContent = gross > 0 ? ((oldTotalTax / gross) * 100).toFixed(2) + '%' : '0.00%';
}

function resetTax() {
  const inc = document.getElementById('tax-income');
  const age = document.getElementById('tax-age');
  const c = document.getElementById('tax-80c');
  const d = document.getElementById('tax-80d');
  const hra = document.getElementById('tax-hra');
  if (inc) inc.value = '1200000';
  if (age) age.value = 'general';
  if (c) c.value = '150000';
  if (d) d.value = '25000';
  if (hra) hra.value = '100000';
  calculateTax();
}

// ----------------------------------------------------------------------------
// 7. CALORIE CALCULATOR
// ----------------------------------------------------------------------------
let calUnit = 'metric';
let calGender = 'male';

function setCalUnit(unit) {
  calUnit = unit;
  const mBtn = document.getElementById('cal-unit-metric');
  const iBtn = document.getElementById('cal-unit-imperial');
  const wLabel = document.getElementById('cal-weight-label');
  const hLabel = document.getElementById('cal-height-label');
  const wInput = document.getElementById('cal-weight');
  const hInput = document.getElementById('cal-height');

  if (mBtn && iBtn) {
    if (unit === 'metric') {
      mBtn.classList.add('active');
      iBtn.classList.remove('active');
      if (wLabel) wLabel.textContent = 'Weight (kg)';
      if (hLabel) hLabel.textContent = 'Height (cm)';
      if (wInput) wInput.value = '70';
      if (hInput) hInput.value = '175';
    } else {
      iBtn.classList.add('active');
      mBtn.classList.remove('active');
      if (wLabel) wLabel.textContent = 'Weight (lbs)';
      if (hLabel) hLabel.textContent = 'Height (inches)';
      if (wInput) wInput.value = '154';
      if (hInput) hInput.value = '69';
    }
  }
  calculateCalorie();
}

function setCalGender(g) {
  calGender = g;
  const mBtn = document.getElementById('cal-gender-male');
  const fBtn = document.getElementById('cal-gender-female');
  if (mBtn && fBtn) {
    if (g === 'male') {
      mBtn.classList.add('active');
      fBtn.classList.remove('active');
    } else {
      fBtn.classList.add('active');
      mBtn.classList.remove('active');
    }
  }
  calculateCalorie();
}

function calculateCalorie() {
  const ageInput = document.getElementById('cal-age');
  const wInput = document.getElementById('cal-weight');
  const hInput = document.getElementById('cal-height');
  const actSelect = document.getElementById('cal-activity');
  const goalSelect = document.getElementById('cal-goal');
  if (!ageInput || !wInput || !hInput || !actSelect || !goalSelect) return;

  const age = Math.max(15, parseFloat(ageInput.value) || 28);
  let weightKg = Math.max(20, parseFloat(wInput.value) || 70);
  let heightCm = Math.max(50, parseFloat(hInput.value) || 175);

  if (calUnit === 'imperial') {
    weightKg = weightKg * 0.45359237;
    heightCm = heightCm * 2.54;
  }

  const actMult = parseFloat(actSelect.value) || 1.375;
  const goalDelta = parseFloat(goalSelect.value) || 0;

  // Mifflin-St Jeor Formula
  let bmr = (10 * weightKg) + (6.25 * heightCm) - (5 * age);
  bmr += calGender === 'male' ? 5 : -161;

  const tdee = Math.round(bmr * actMult);
  const targetCalories = Math.max(1200, Math.round(tdee + goalDelta));

  // Macronutrient split: 30% Protein, 40% Carbs, 30% Fat
  const proteinGrams = Math.round((targetCalories * 0.30) / 4);
  const carbsGrams = Math.round((targetCalories * 0.40) / 4);
  const fatGrams = Math.round((targetCalories * 0.30) / 9);

  let shiftText = '0.0 kg / wk';
  if (goalDelta < 0) {
    const kg = Math.abs(goalDelta) / 1000;
    shiftText = '-' + kg.toFixed(2) + ' kg / wk';
  } else if (goalDelta > 0) {
    const kg = goalDelta / 1000;
    shiftText = '+' + kg.toFixed(2) + ' kg / wk';
  }

  const targetEl = document.getElementById('cal-target-val');
  if (targetEl) targetEl.textContent = formatNumberWithCommas(targetCalories, 0);

  const tdeeEl = document.getElementById('cal-tdee-val');
  if (tdeeEl) tdeeEl.textContent = formatNumberWithCommas(tdee, 0) + ' kcal';

  const bmrEl = document.getElementById('cal-bmr-val');
  if (bmrEl) bmrEl.textContent = formatNumberWithCommas(Math.round(bmr), 0) + ' kcal';

  const protEl = document.getElementById('cal-res-protein');
  if (protEl) protEl.textContent = proteinGrams + 'g / day';

  const carbsEl = document.getElementById('cal-res-carbs');
  if (carbsEl) carbsEl.textContent = carbsGrams + 'g / day';

  const fatsEl = document.getElementById('cal-res-fats');
  if (fatsEl) fatsEl.textContent = fatGrams + 'g / day';

  const deltaEl = document.getElementById('cal-res-weekly-delta');
  if (deltaEl) deltaEl.textContent = shiftText;
}

function resetCalorie() {
  const age = document.getElementById('cal-age');
  const w = document.getElementById('cal-weight');
  const h = document.getElementById('cal-height');
  const act = document.getElementById('cal-activity');
  const goal = document.getElementById('cal-goal');
  if (age) age.value = '28';
  if (w) w.value = '70';
  if (h) h.value = '175';
  if (act) act.value = '1.375';
  if (goal) goal.value = '0';
  setCalUnit('metric');
  setCalGender('male');
  calculateCalorie();
}

// ----------------------------------------------------------------------------
// 8. BMR CALCULATOR
// ----------------------------------------------------------------------------
let bmrUnit = 'metric';
let bmrGender = 'male';

function setBmrUnit(unit) {
  bmrUnit = unit;
  const mBtn = document.getElementById('bmr-unit-metric');
  const iBtn = document.getElementById('bmr-unit-imperial');
  const wLabel = document.getElementById('bmr-weight-label');
  const hLabel = document.getElementById('bmr-height-label');
  const wInput = document.getElementById('bmr-weight');
  const hInput = document.getElementById('bmr-height');

  if (mBtn && iBtn) {
    if (unit === 'metric') {
      mBtn.classList.add('active');
      iBtn.classList.remove('active');
      if (wLabel) wLabel.textContent = 'Weight (kg)';
      if (hLabel) hLabel.textContent = 'Height (cm)';
      if (wInput) wInput.value = '72';
      if (hInput) hInput.value = '175';
    } else {
      iBtn.classList.add('active');
      mBtn.classList.remove('active');
      if (wLabel) wLabel.textContent = 'Weight (lbs)';
      if (hLabel) hLabel.textContent = 'Height (inches)';
      if (wInput) wInput.value = '158';
      if (hInput) hInput.value = '69';
    }
  }
  calculateBmr();
}

function setBmrGender(g) {
  bmrGender = g;
  const mBtn = document.getElementById('bmr-gender-male');
  const fBtn = document.getElementById('bmr-gender-female');
  if (mBtn && fBtn) {
    if (g === 'male') {
      mBtn.classList.add('active');
      fBtn.classList.remove('active');
    } else {
      fBtn.classList.add('active');
      mBtn.classList.remove('active');
    }
  }
  calculateBmr();
}

function calculateBmr() {
  const ageInput = document.getElementById('bmr-age');
  const wInput = document.getElementById('bmr-weight');
  const hInput = document.getElementById('bmr-height');
  if (!ageInput || !wInput || !hInput) return;

  const age = Math.max(15, parseFloat(ageInput.value) || 30);
  let weightKg = Math.max(20, parseFloat(wInput.value) || 72);
  let heightCm = Math.max(50, parseFloat(hInput.value) || 175);

  if (bmrUnit === 'imperial') {
    weightKg = weightKg * 0.45359237;
    heightCm = heightCm * 2.54;
  }

  // 1. Mifflin-St Jeor
  let mifflin = (10 * weightKg) + (6.25 * heightCm) - (5 * age);
  mifflin += bmrGender === 'male' ? 5 : -161;

  // 2. Revised Harris-Benedict
  let hb = 0;
  if (bmrGender === 'male') {
    hb = (13.397 * weightKg) + (4.799 * heightCm) - (5.677 * age) + 88.362;
  } else {
    hb = (9.247 * weightKg) + (3.098 * heightCm) - (4.330 * age) + 447.593;
  }

  const hourly = mifflin / 24;

  const mifflinEl = document.getElementById('bmr-mifflin-val');
  if (mifflinEl) mifflinEl.textContent = formatNumberWithCommas(Math.round(mifflin), 0);

  const hrEl = document.getElementById('bmr-hourly-val');
  if (hrEl) hrEl.textContent = hourly.toFixed(1) + ' kcal/hr';

  const hbEl = document.getElementById('bmr-hb-val');
  if (hbEl) hbEl.textContent = formatNumberWithCommas(Math.round(hb), 0) + ' kcal/day';

  const sedEl = document.getElementById('bmr-res-sed');
  if (sedEl) sedEl.textContent = formatNumberWithCommas(Math.round(mifflin * 1.2), 0) + ' kcal';

  const lightEl = document.getElementById('bmr-res-light');
  if (lightEl) lightEl.textContent = formatNumberWithCommas(Math.round(mifflin * 1.375), 0) + ' kcal';

  const modEl = document.getElementById('bmr-res-mod');
  if (modEl) modEl.textContent = formatNumberWithCommas(Math.round(mifflin * 1.55), 0) + ' kcal';

  const hardEl = document.getElementById('bmr-res-hard');
  if (hardEl) hardEl.textContent = formatNumberWithCommas(Math.round(mifflin * 1.725), 0) + ' kcal';
}

function resetBmr() {
  const age = document.getElementById('bmr-age');
  const w = document.getElementById('bmr-weight');
  const h = document.getElementById('bmr-height');
  if (age) age.value = '30';
  if (w) w.value = '72';
  if (h) h.value = '175';
  setBmrUnit('metric');
  setBmrGender('male');
  calculateBmr();
}

// ----------------------------------------------------------------------------
// 9. TDEE CALCULATOR
// ----------------------------------------------------------------------------
let tdeeUnit = 'metric';
let tdeeGender = 'male';

function setTdeeUnit(unit) {
  tdeeUnit = unit;
  const mBtn = document.getElementById('tdee-unit-metric');
  const iBtn = document.getElementById('tdee-unit-imperial');
  const wLabel = document.getElementById('tdee-weight-label');
  const hLabel = document.getElementById('tdee-height-label');
  const wInput = document.getElementById('tdee-weight');
  const hInput = document.getElementById('tdee-height');

  if (mBtn && iBtn) {
    if (unit === 'metric') {
      mBtn.classList.add('active');
      iBtn.classList.remove('active');
      if (wLabel) wLabel.textContent = 'Weight (kg)';
      if (hLabel) hLabel.textContent = 'Height (cm)';
      if (wInput) wInput.value = '68';
      if (hInput) hInput.value = '172';
    } else {
      iBtn.classList.add('active');
      mBtn.classList.remove('active');
      if (wLabel) wLabel.textContent = 'Weight (lbs)';
      if (hLabel) hLabel.textContent = 'Height (inches)';
      if (wInput) wInput.value = '150';
      if (hInput) hInput.value = '68';
    }
  }
  calculateTdee();
}

function setTdeeGender(g) {
  tdeeGender = g;
  const mBtn = document.getElementById('tdee-gender-male');
  const fBtn = document.getElementById('tdee-gender-female');
  if (mBtn && fBtn) {
    if (g === 'male') {
      mBtn.classList.add('active');
      fBtn.classList.remove('active');
    } else {
      fBtn.classList.add('active');
      mBtn.classList.remove('active');
    }
  }
  calculateTdee();
}

function calculateTdee() {
  const ageInput = document.getElementById('tdee-age');
  const wInput = document.getElementById('tdee-weight');
  const hInput = document.getElementById('tdee-height');
  const actSelect = document.getElementById('tdee-activity');
  if (!ageInput || !wInput || !hInput || !actSelect) return;

  const age = Math.max(15, parseFloat(ageInput.value) || 26);
  let weightKg = Math.max(20, parseFloat(wInput.value) || 68);
  let heightCm = Math.max(50, parseFloat(hInput.value) || 172);

  if (tdeeUnit === 'imperial') {
    weightKg = weightKg * 0.45359237;
    heightCm = heightCm * 2.54;
  }

  const actMult = parseFloat(actSelect.value) || 1.55;

  let bmr = (10 * weightKg) + (6.25 * heightCm) - (5 * age);
  bmr += tdeeGender === 'male' ? 5 : -161;

  const tdee = Math.round(bmr * actMult);
  const weekly = tdee * 7;
  const activeBurn = Math.round(tdee - bmr);

  const mainEl = document.getElementById('tdee-main-val');
  if (mainEl) mainEl.textContent = formatNumberWithCommas(tdee, 0);

  const wkEl = document.getElementById('tdee-weekly-val');
  if (wkEl) wkEl.textContent = formatNumberWithCommas(weekly, 0) + ' kcal/week';

  const bmrEl = document.getElementById('tdee-bmr-val');
  if (bmrEl) bmrEl.textContent = formatNumberWithCommas(Math.round(bmr), 0) + ' kcal';

  const cutEl = document.getElementById('tdee-res-cut');
  if (cutEl) cutEl.textContent = formatNumberWithCommas(Math.max(1200, tdee - 500), 0) + ' kcal';

  const mildEl = document.getElementById('tdee-res-mild-cut');
  if (mildEl) mildEl.textContent = formatNumberWithCommas(Math.max(1200, tdee - 250), 0) + ' kcal';

  const bulkEl = document.getElementById('tdee-res-bulk');
  if (bulkEl) bulkEl.textContent = formatNumberWithCommas(tdee + 300, 0) + ' kcal';

  const burnEl = document.getElementById('tdee-res-active-burn');
  if (burnEl) burnEl.textContent = formatNumberWithCommas(activeBurn, 0) + ' kcal/day';
}

function resetTdee() {
  const age = document.getElementById('tdee-age');
  const w = document.getElementById('tdee-weight');
  const h = document.getElementById('tdee-height');
  const act = document.getElementById('tdee-activity');
  if (age) age.value = '26';
  if (w) w.value = '68';
  if (h) h.value = '172';
  if (act) act.value = '1.55';
  setTdeeUnit('metric');
  setTdeeGender('male');
  calculateTdee();
}

// ----------------------------------------------------------------------------
// 10. PREGNANCY DUE DATE CALCULATOR
// ----------------------------------------------------------------------------
function calculatePregnancyDueDate() {
  const methodSelect = document.getElementById('pdd-method');
  const dateInput = document.getElementById('pdd-date');
  const cycleInput = document.getElementById('pdd-cycle');
  const cycleGroup = document.getElementById('pdd-cycle-group');
  if (!methodSelect || !dateInput) return;

  const method = methodSelect.value;
  if (cycleGroup) {
    cycleGroup.style.display = method === 'lmp' ? 'flex' : 'none';
  }

  // Default date if none picked: 100 days ago
  let baseDate = new Date();
  if (dateInput.value) {
    baseDate = new Date(dateInput.value);
  } else {
    baseDate.setDate(baseDate.getDate() - 100);
    dateInput.value = baseDate.toISOString().split('T')[0];
  }

  const cycleDays = parseFloat(cycleInput ? cycleInput.value : 28) || 28;
  const cycleAdj = cycleDays - 28;

  let edd = new Date(baseDate.getTime());
  let lmpEquiv = new Date(baseDate.getTime());

  if (method === 'lmp') {
    // Naegele: LMP + 280 days + cycleAdj
    edd.setDate(edd.getDate() + 280 + cycleAdj);
    lmpEquiv = new Date(baseDate.getTime());
  } else if (method === 'conception') {
    // Conception + 266 days
    edd.setDate(edd.getDate() + 266);
    lmpEquiv.setDate(baseDate.getDate() - 14);
  } else if (method === 'ivf3') {
    // IVF 3-day + 263 days
    edd.setDate(edd.getDate() + 263);
    lmpEquiv.setDate(baseDate.getDate() - 17);
  } else if (method === 'ivf5') {
    // IVF 5-day + 261 days
    edd.setDate(edd.getDate() + 261);
    lmpEquiv.setDate(baseDate.getDate() - 19);
  }

  const today = new Date();
  const diffMs = today - lmpEquiv;
  const totalDays = Math.max(0, Math.floor(diffMs / (1000 * 60 * 60 * 24)));
  const weeks = Math.floor(totalDays / 7);
  const remDays = totalDays % 7;

  const remainingDays = Math.max(0, Math.ceil((edd - today) / (1000 * 60 * 60 * 24)));

  let trimester = 'First Trimester (Week ' + weeks + ')';
  if (weeks >= 28) {
    trimester = 'Third Trimester (Week ' + weeks + ')';
  } else if (weeks >= 14) {
    trimester = 'Second Trimester (Week ' + weeks + ')';
  }

  const options = { year: 'numeric', month: 'short', day: 'numeric' };
  const dueFormatted = edd.toLocaleDateString('en-US', options);

  const conceptionEst = new Date(lmpEquiv.getTime());
  conceptionEst.setDate(conceptionEst.getDate() + 14);

  const tri1End = new Date(lmpEquiv.getTime());
  tri1End.setDate(tri1End.getDate() + (13 * 7));

  const viability = new Date(lmpEquiv.getTime());
  viability.setDate(viability.getDate() + (24 * 7));

  const fullTerm = new Date(lmpEquiv.getTime());
  fullTerm.setDate(fullTerm.getDate() + (37 * 7));

  const dueEl = document.getElementById('pdd-due-date-val');
  if (dueEl) dueEl.textContent = dueFormatted;

  const cdEl = document.getElementById('pdd-countdown-val');
  if (cdEl) cdEl.textContent = remainingDays + ' Days Remaining';

  const gaEl = document.getElementById('pdd-gest-age-val');
  if (gaEl) gaEl.textContent = weeks + ' Weeks, ' + remDays + ' Days';

  const triEl = document.getElementById('pdd-trimester-val');
  if (triEl) triEl.textContent = trimester;

  const concEl = document.getElementById('pdd-res-conception');
  if (concEl) concEl.textContent = conceptionEst.toLocaleDateString('en-US', options);

  const t1El = document.getElementById('pdd-res-tri1-end');
  if (t1El) t1El.textContent = tri1End.toLocaleDateString('en-US', options);

  const viabEl = document.getElementById('pdd-res-viability');
  if (viabEl) viabEl.textContent = viability.toLocaleDateString('en-US', options);

  const ftEl = document.getElementById('pdd-res-fullterm');
  if (ftEl) ftEl.textContent = fullTerm.toLocaleDateString('en-US', options);
}

function resetPregnancyDueDate() {
  const method = document.getElementById('pdd-method');
  const dateInput = document.getElementById('pdd-date');
  const cycle = document.getElementById('pdd-cycle');
  if (method) method.value = 'lmp';
  if (cycle) cycle.value = '28';
  if (dateInput) {
    const d = new Date();
    d.setDate(d.getDate() - 100);
    dateInput.value = d.toISOString().split('T')[0];
  }
  calculatePregnancyDueDate();
}

// ----------------------------------------------------------------------------
// 11. HOURS TO MINUTES CONVERTER
// ----------------------------------------------------------------------------
let h2mMode = 'dec';

function setH2mMode(mode) {
  h2mMode = mode;
  const decBtn = document.getElementById('h2m-mode-dec');
  const splitBtn = document.getElementById('h2m-mode-split');
  const decCont = document.getElementById('h2m-dec-container');
  const splitCont = document.getElementById('h2m-split-container');
  if (decBtn && splitBtn && decCont && splitCont) {
    if (mode === 'dec') {
      decBtn.classList.add('active');
      splitBtn.classList.remove('active');
      decCont.style.display = 'block';
      splitCont.style.display = 'none';
    } else {
      splitBtn.classList.add('active');
      decBtn.classList.remove('active');
      decCont.style.display = 'none';
      splitCont.style.display = 'block';
    }
  }
  convertHoursToMinutes();
}

function convertHoursToMinutes() {
  let decimalHours = 0;
  if (h2mMode === 'dec') {
    const input = document.getElementById('h2m-dec-input');
    decimalHours = Math.max(0, parseFloat(input ? input.value : 0) || 0);
  } else {
    const hInput = document.getElementById('h2m-hours-part');
    const mInput = document.getElementById('h2m-mins-part');
    const h = Math.max(0, parseFloat(hInput ? hInput.value : 0) || 0);
    const m = Math.max(0, parseFloat(mInput ? mInput.value : 0) || 0);
    decimalHours = h + (m / 60);
  }

  const totalMinutes = decimalHours * 60;
  const totalSeconds = totalMinutes * 60;
  const totalMs = totalSeconds * 1000;

  const wholeHours = Math.floor(decimalHours);
  const remMinutes = Math.round((decimalHours - wholeHours) * 60);

  const dayPct = (decimalHours / 24) * 100;
  const workPct = (decimalHours / 8) * 100;

  const minEl = document.getElementById('h2m-total-mins-val');
  if (minEl) minEl.textContent = formatNumberWithCommas(totalMinutes, 1).replace(/\.0$/, '');

  const expEl = document.getElementById('h2m-express-val');
  if (expEl) expEl.textContent = wholeHours + ' Hours and ' + remMinutes + ' Minutes';

  const formEl = document.getElementById('h2m-formula-val');
  if (formEl) formEl.textContent = decimalHours.toFixed(2) + ' hrs × 60 min/hr = ' + totalMinutes.toFixed(1) + ' min';

  const secEl = document.getElementById('h2m-res-seconds');
  if (secEl) secEl.textContent = formatNumberWithCommas(totalSeconds, 0) + ' sec';

  const msEl = document.getElementById('h2m-res-ms');
  if (msEl) msEl.textContent = formatNumberWithCommas(totalMs, 0) + ' ms';

  const dayEl = document.getElementById('h2m-res-day-pct');
  if (dayEl) dayEl.textContent = dayPct.toFixed(2) + '%';

  const workEl = document.getElementById('h2m-res-work-pct');
  if (workEl) workEl.textContent = workPct.toFixed(2) + '%';
}

function resetHoursToMinutes() {
  const dec = document.getElementById('h2m-dec-input');
  const h = document.getElementById('h2m-hours-part');
  const m = document.getElementById('h2m-mins-part');
  if (dec) dec.value = '2.5';
  if (h) h.value = '2';
  if (m) m.value = '30';
  setH2mMode('dec');
  convertHoursToMinutes();
}

// ----------------------------------------------------------------------------
// 12. MINUTES TO HOURS CONVERTER
// ----------------------------------------------------------------------------
function convertMinutesToHours() {
  const input = document.getElementById('m2h-input');
  if (!input) return;

  const totalMinutes = Math.max(0, parseFloat(input.value) || 0);
  const decimalHours = totalMinutes / 60;
  const wholeHours = Math.floor(decimalHours);
  const remMinutes = Math.round(totalMinutes % 60);

  const pad = (n) => String(n).padStart(2, '0');
  const digitalTime = pad(wholeHours) + ':' + pad(remMinutes) + ':00';
  const totalSeconds = totalMinutes * 60;

  const shiftPct = (totalMinutes / 480) * 100;

  const decEl = document.getElementById('m2h-dec-val');
  if (decEl) decEl.textContent = decimalHours.toFixed(4);

  const clockEl = document.getElementById('m2h-clock-val');
  if (clockEl) clockEl.textContent = wholeHours + ' Hours, ' + remMinutes + ' Minutes';

  const digEl = document.getElementById('m2h-digital-val');
  if (digEl) digEl.textContent = digitalTime;

  const hrsEl = document.getElementById('m2h-res-hours');
  if (hrsEl) hrsEl.textContent = wholeHours + ' hrs';

  const remMinsEl = document.getElementById('m2h-res-rem-mins');
  if (remMinsEl) remMinsEl.textContent = remMinutes + ' mins';

  const shiftEl = document.getElementById('m2h-res-shift-pct');
  if (shiftEl) shiftEl.textContent = shiftPct.toFixed(2) + '%';

  const secEl = document.getElementById('m2h-res-secs');
  if (secEl) secEl.textContent = formatNumberWithCommas(totalSeconds, 0) + ' sec';
}

function resetMinutesToHours() {
  const input = document.getElementById('m2h-input');
  if (input) input.value = '175';
  convertMinutesToHours();
}

// ----------------------------------------------------------------------------
// 13. LENGTH CONVERTER
// ----------------------------------------------------------------------------
const LENGTH_FACTORS_TO_METERS = {
  mm: 0.001,
  cm: 0.01,
  m: 1.0,
  km: 1000.0,
  in: 0.0254,
  ft: 0.3048,
  yd: 0.9144,
  mi: 1609.344,
  nmi: 1852.0
};

const LENGTH_LABELS = {
  mm: 'Millimeters',
  cm: 'Centimeters',
  m: 'Meters',
  km: 'Kilometers',
  in: 'Inches',
  ft: 'Feet',
  yd: 'Yards',
  mi: 'Miles',
  nmi: 'Nautical Miles'
};

function convertLength() {
  const valInput = document.getElementById('len-val');
  const fromSelect = document.getElementById('len-from');
  const toSelect = document.getElementById('len-to');
  if (!valInput || !fromSelect || !toSelect) return;

  const val = Math.max(0, parseFloat(valInput.value) || 0);
  const from = fromSelect.value;
  const to = toSelect.value;

  const inMeters = val * (LENGTH_FACTORS_TO_METERS[from] || 1);
  const converted = inMeters / (LENGTH_FACTORS_TO_METERS[to] || 1);

  const resValEl = document.getElementById('len-result-val');
  if (resValEl) resValEl.textContent = formatNumberWithCommas(converted, 4);

  const resUnitEl = document.getElementById('len-result-unit');
  if (resUnitEl) resUnitEl.textContent = (LENGTH_LABELS[to] || to) + ' (' + to + ')';

  const formEl = document.getElementById('len-formula-val');
  if (formEl) formEl.textContent = val + ' ' + from + ' = ' + formatNumberWithCommas(converted, 4) + ' ' + to;

  // Build table
  const tbody = document.getElementById('len-table-body');
  if (tbody) {
    let rows = '';
    const units = ['mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mi', 'nmi'];
    units.forEach(u => {
      const uVal = inMeters / LENGTH_FACTORS_TO_METERS[u];
      const isMetric = ['mm', 'cm', 'm', 'km'].includes(u);
      rows += '<tr>' +
        '<td><strong>' + LENGTH_LABELS[u] + '</strong></td>' +
        '<td>' + formatNumberWithCommas(uVal, 4) + '</td>' +
        '<td>' + u + '</td>' +
        '<td>' + (isMetric ? 'Metric (SI)' : 'Imperial / Nautical') + '</td>' +
        '</tr>';
    });
    tbody.innerHTML = rows;
  }
}

function swapLengthUnits() {
  const fromSelect = document.getElementById('len-from');
  const toSelect = document.getElementById('len-to');
  if (fromSelect && toSelect) {
    const temp = fromSelect.value;
    fromSelect.value = toSelect.value;
    toSelect.value = temp;
    convertLength();
  }
}

function resetLength() {
  const val = document.getElementById('len-val');
  const from = document.getElementById('len-from');
  const to = document.getElementById('len-to');
  if (val) val.value = '10';
  if (from) from.value = 'm';
  if (to) to.value = 'ft';
  convertLength();
}

// ----------------------------------------------------------------------------
// 14. WEIGHT CONVERTER
// ----------------------------------------------------------------------------
const WEIGHT_FACTORS_TO_KG = {
  mg: 0.000001,
  g: 0.001,
  kg: 1.0,
  t: 1000.0,
  oz: 0.028349523125,
  lb: 0.45359237,
  st: 6.35029318,
  q: 100.0
};

const WEIGHT_LABELS = {
  mg: 'Milligrams',
  g: 'Grams',
  kg: 'Kilograms',
  t: 'Metric Tonnes',
  oz: 'Ounces',
  lb: 'Pounds',
  st: 'Stones',
  q: 'Quintals'
};

function convertWeight() {
  const valInput = document.getElementById('wt-val');
  const fromSelect = document.getElementById('wt-from');
  const toSelect = document.getElementById('wt-to');
  if (!valInput || !fromSelect || !toSelect) return;

  const val = Math.max(0, parseFloat(valInput.value) || 0);
  const from = fromSelect.value;
  const to = toSelect.value;

  const inKg = val * (WEIGHT_FACTORS_TO_KG[from] || 1);
  const converted = inKg / (WEIGHT_FACTORS_TO_KG[to] || 1);

  const resValEl = document.getElementById('wt-result-val');
  if (resValEl) resValEl.textContent = formatNumberWithCommas(converted, 4);

  const resUnitEl = document.getElementById('wt-result-unit');
  if (resUnitEl) resUnitEl.textContent = (WEIGHT_LABELS[to] || to) + ' (' + to + ')';

  const formEl = document.getElementById('wt-formula-val');
  if (formEl) formEl.textContent = val + ' ' + from + ' = ' + formatNumberWithCommas(converted, 4) + ' ' + to;

  const tbody = document.getElementById('wt-table-body');
  if (tbody) {
    let rows = '';
    const units = ['mg', 'g', 'kg', 't', 'oz', 'lb', 'st', 'q'];
    units.forEach(u => {
      const uVal = inKg / WEIGHT_FACTORS_TO_KG[u];
      const isMetric = ['mg', 'g', 'kg', 't'].includes(u);
      rows += '<tr>' +
        '<td><strong>' + WEIGHT_LABELS[u] + '</strong></td>' +
        '<td>' + formatNumberWithCommas(uVal, 4) + '</td>' +
        '<td>' + u + '</td>' +
        '<td>' + (isMetric ? 'Metric (SI)' : (u === 'q' ? 'Indian Agricultural' : 'Imperial / US')) + '</td>' +
        '</tr>';
    });
    tbody.innerHTML = rows;
  }
}

function swapWeightUnits() {
  const fromSelect = document.getElementById('wt-from');
  const toSelect = document.getElementById('wt-to');
  if (fromSelect && toSelect) {
    const temp = fromSelect.value;
    fromSelect.value = toSelect.value;
    toSelect.value = temp;
    convertWeight();
  }
}

function resetWeight() {
  const val = document.getElementById('wt-val');
  const from = document.getElementById('wt-from');
  const to = document.getElementById('wt-to');
  if (val) val.value = '5';
  if (from) from.value = 'kg';
  if (to) to.value = 'lb';
  convertWeight();
}

// ----------------------------------------------------------------------------
// 15. TEMPERATURE CONVERTER
// ----------------------------------------------------------------------------
function convertTemperature() {
  const valInput = document.getElementById('temp-val');
  const fromSelect = document.getElementById('temp-from');
  const toSelect = document.getElementById('temp-to');
  if (!valInput || !fromSelect || !toSelect) return;

  const val = parseFloat(valInput.value) || 0;
  const from = fromSelect.value;
  const to = toSelect.value;

  // Convert to Celsius first
  let c = val;
  if (from === 'f') {
    c = (val - 32) * (5 / 9);
  } else if (from === 'k') {
    c = val - 273.15;
  }

  // Convert from Celsius to target
  let converted = c;
  let formula = '';
  if (to === 'f') {
    converted = (c * (9 / 5)) + 32;
    formula = '(' + val + ' °' + from.toUpperCase() + ' → ' + c.toFixed(2) + ' °C) × 9/5 + 32 = ' + converted.toFixed(2) + ' °F';
  } else if (to === 'k') {
    converted = c + 273.15;
    formula = c.toFixed(2) + ' °C + 273.15 = ' + converted.toFixed(2) + ' K';
  } else {
    converted = c;
    formula = val + ' °' + from.toUpperCase() + ' = ' + c.toFixed(2) + ' °C';
  }

  const fVal = (c * (9 / 5)) + 32;
  const kVal = c + 273.15;

  let benchmark = 'Liquid / Ambient Range';
  if (c <= -273.15) benchmark = 'Absolute Zero (0 K)';
  else if (c < 0) benchmark = 'Sub-Freezing (Ice Phase)';
  else if (Math.abs(c) < 0.1) benchmark = 'Water Freezing Point (0 °C)';
  else if (Math.abs(c - 37) <= 0.5) benchmark = 'Normal Human Body Temp (37 °C)';
  else if (Math.abs(c - 100) <= 0.5) benchmark = 'Water Boiling Point at Sea Level (100 °C)';
  else if (c > 100) benchmark = 'Above Boiling Point (Steam Phase)';

  const resValEl = document.getElementById('temp-result-val');
  if (resValEl) resValEl.textContent = converted.toFixed(2);

  const resUnitEl = document.getElementById('temp-result-unit');
  if (resUnitEl) resUnitEl.textContent = to === 'k' ? 'K' : '°' + to.toUpperCase();

  const formEl = document.getElementById('temp-formula-val');
  if (formEl) formEl.textContent = formula;

  const benchEl = document.getElementById('temp-benchmark-val');
  if (benchEl) benchEl.textContent = benchmark;

  const cEl = document.getElementById('temp-res-c');
  if (cEl) cEl.textContent = c.toFixed(2) + ' °C';

  const fEl = document.getElementById('temp-res-f');
  if (fEl) fEl.textContent = fVal.toFixed(2) + ' °F';

  const kEl = document.getElementById('temp-res-k');
  if (kEl) kEl.textContent = kVal.toFixed(2) + ' K';

  const zeroEl = document.getElementById('temp-res-zero');
  if (zeroEl) zeroEl.textContent = (kVal >= 0 ? '+' : '') + kVal.toFixed(2) + ' K';
}

function swapTemperatureUnits() {
  const fromSelect = document.getElementById('temp-from');
  const toSelect = document.getElementById('temp-to');
  if (fromSelect && toSelect) {
    const temp = fromSelect.value;
    fromSelect.value = toSelect.value;
    toSelect.value = temp;
    convertTemperature();
  }
}

function resetTemperature() {
  const val = document.getElementById('temp-val');
  const from = document.getElementById('temp-from');
  const to = document.getElementById('temp-to');
  if (val) val.value = '100';
  if (from) from.value = 'c';
  if (to) to.value = 'f';
  convertTemperature();
}

// ----------------------------------------------------------------------------
// 16. AREA CONVERTER
// ----------------------------------------------------------------------------
const AREA_FACTORS_TO_SQM = {
  sqft: 0.09290304,
  sqm: 1.0,
  sqyd: 0.83612736,
  acre: 4046.8564224,
  hectare: 10000.0,
  guntha: 101.17141056, // 1089 sq ft
  bigha: 2529.285264,  // Standard pucca bigha = 27,225 sq ft
  sqkm: 1000000.0
};

const AREA_LABELS = {
  sqft: 'Square Feet',
  sqm: 'Square Meters',
  sqyd: 'Square Yards (Gaj)',
  acre: 'Acres',
  hectare: 'Hectares',
  guntha: 'Guntha',
  bigha: 'Pucca Bigha',
  sqkm: 'Square Kilometers'
};

function convertArea() {
  const valInput = document.getElementById('area-val');
  const fromSelect = document.getElementById('area-from');
  const toSelect = document.getElementById('area-to');
  if (!valInput || !fromSelect || !toSelect) return;

  const val = Math.max(0, parseFloat(valInput.value) || 0);
  const from = fromSelect.value;
  const to = toSelect.value;

  const inSqm = val * (AREA_FACTORS_TO_SQM[from] || 1);
  const converted = inSqm / (AREA_FACTORS_TO_SQM[to] || 1);

  const resValEl = document.getElementById('area-result-val');
  if (resValEl) resValEl.textContent = formatNumberWithCommas(converted, 4);

  const resUnitEl = document.getElementById('area-result-unit');
  if (resUnitEl) resUnitEl.textContent = (AREA_LABELS[to] || to) + ' (' + to + ')';

  const formEl = document.getElementById('area-formula-val');
  if (formEl) formEl.textContent = val + ' ' + from + ' = ' + formatNumberWithCommas(converted, 4) + ' ' + to;

  const tbody = document.getElementById('area-table-body');
  if (tbody) {
    let rows = '';
    const units = ['sqft', 'sqm', 'sqyd', 'acre', 'hectare', 'guntha', 'bigha', 'sqkm'];
    units.forEach(u => {
      const uVal = inSqm / AREA_FACTORS_TO_SQM[u];
      const isMetric = ['sqm', 'hectare', 'sqkm'].includes(u);
      rows += '<tr>' +
        '<td><strong>' + AREA_LABELS[u] + '</strong></td>' +
        '<td>' + formatNumberWithCommas(uVal, 4) + '</td>' +
        '<td>' + u + '</td>' +
        '<td>' + (isMetric ? 'Metric System' : (['guntha', 'bigha', 'sqyd'].includes(u) ? 'Indian Real Estate' : 'Imperial System')) + '</td>' +
        '</tr>';
    });
    tbody.innerHTML = rows;
  }
}

function swapAreaUnits() {
  const fromSelect = document.getElementById('area-from');
  const toSelect = document.getElementById('area-to');
  if (fromSelect && toSelect) {
    const temp = fromSelect.value;
    fromSelect.value = toSelect.value;
    toSelect.value = temp;
    convertArea();
  }
}

function resetArea() {
  const val = document.getElementById('area-val');
  const from = document.getElementById('area-from');
  const to = document.getElementById('area-to');
  if (val) val.value = '1200';
  if (from) from.value = 'sqft';
  if (to) to.value = 'sqm';
  convertArea();
}

// ----------------------------------------------------------------------------
// 17. VOLUME CONVERTER
// ----------------------------------------------------------------------------
const VOLUME_FACTORS_TO_LITERS = {
  l: 1.0,
  ml: 0.001,
  m3: 1000.0,
  usgal: 3.785411784,
  impgal: 4.54609,
  usfloz: 0.0295735295625,
  uscup: 0.2365882365,
  cuft: 28.316846592
};

const VOLUME_LABELS = {
  l: 'Liters',
  ml: 'Milliliters',
  m3: 'Cubic Meters',
  usgal: 'US Gallons',
  impgal: 'Imperial Gallons (UK)',
  usfloz: 'US Fluid Ounces',
  uscup: 'US Cups',
  cuft: 'Cubic Feet'
};

function convertVolume() {
  const valInput = document.getElementById('vol-val');
  const fromSelect = document.getElementById('vol-from');
  const toSelect = document.getElementById('vol-to');
  if (!valInput || !fromSelect || !toSelect) return;

  const val = Math.max(0, parseFloat(valInput.value) || 0);
  const from = fromSelect.value;
  const to = toSelect.value;

  const inLiters = val * (VOLUME_FACTORS_TO_LITERS[from] || 1);
  const converted = inLiters / (VOLUME_FACTORS_TO_LITERS[to] || 1);

  const resValEl = document.getElementById('vol-result-val');
  if (resValEl) resValEl.textContent = formatNumberWithCommas(converted, 4);

  const resUnitEl = document.getElementById('vol-result-unit');
  if (resUnitEl) resUnitEl.textContent = (VOLUME_LABELS[to] || to) + ' (' + to + ')';

  const formEl = document.getElementById('vol-formula-val');
  if (formEl) formEl.textContent = val + ' ' + from + ' = ' + formatNumberWithCommas(converted, 4) + ' ' + to;

  const tbody = document.getElementById('vol-table-body');
  if (tbody) {
    let rows = '';
    const units = ['ml', 'l', 'm3', 'usgal', 'impgal', 'usfloz', 'uscup', 'cuft'];
    units.forEach(u => {
      const uVal = inLiters / VOLUME_FACTORS_TO_LITERS[u];
      const isMetric = ['ml', 'l', 'm3'].includes(u);
      rows += '<tr>' +
        '<td><strong>' + VOLUME_LABELS[u] + '</strong></td>' +
        '<td>' + formatNumberWithCommas(uVal, 4) + '</td>' +
        '<td>' + u + '</td>' +
        '<td>' + (isMetric ? 'Metric (SI)' : 'US / Imperial') + '</td>' +
        '</tr>';
    });
    tbody.innerHTML = rows;
  }
}

function swapVolumeUnits() {
  const fromSelect = document.getElementById('vol-from');
  const toSelect = document.getElementById('vol-to');
  if (fromSelect && toSelect) {
    const temp = fromSelect.value;
    fromSelect.value = toSelect.value;
    toSelect.value = temp;
    convertVolume();
  }
}

function resetVolume() {
  const val = document.getElementById('vol-val');
  const from = document.getElementById('vol-from');
  const to = document.getElementById('vol-to');
  if (val) val.value = '5';
  if (from) from.value = 'l';
  if (to) to.value = 'usgal';
  convertVolume();
}

// ----------------------------------------------------------------------------
// 18. TIP CALCULATOR
// ----------------------------------------------------------------------------
let tipCurrency = 'INR';

function setTipCurrency(curr) {
  tipCurrency = curr;
  const inrBtn = document.getElementById('tip-curr-inr');
  const usdBtn = document.getElementById('tip-curr-usd');
  const label = document.getElementById('tip-bill-label');
  if (inrBtn && usdBtn) {
    if (curr === 'INR') {
      inrBtn.classList.add('active');
      usdBtn.classList.remove('active');
      if (label) label.textContent = 'Bill Amount (₹)';
    } else {
      usdBtn.classList.add('active');
      inrBtn.classList.remove('active');
      if (label) label.textContent = 'Bill Amount ($)';
    }
  }
  calculateTip();
}

function setTipPreset(pct) {
  const customInput = document.getElementById('tip-custom-pct');
  if (customInput) customInput.value = pct;
  calculateTip();
}

function calculateTip() {
  const billInput = document.getElementById('tip-bill');
  const pctInput = document.getElementById('tip-custom-pct');
  const peopleInput = document.getElementById('tip-people');
  if (!billInput || !pctInput || !peopleInput) return;

  const bill = Math.max(0, parseFloat(billInput.value) || 0);
  const tipPct = Math.max(0, parseFloat(pctInput.value) || 0);
  const people = Math.max(1, parseInt(peopleInput.value, 10) || 1);

  const totalTip = bill * (tipPct / 100);
  const grandTotal = bill + totalTip;

  const tipEach = totalTip / people;
  const baseEach = bill / people;
  const totalEach = grandTotal / people;
  const roundedEach = Math.ceil(totalEach);

  const fmt = (val) => (tipCurrency === 'INR' ? '₹' : '$') + formatNumberWithCommas(val, 2);

  const perPersonEl = document.getElementById('tip-per-person-val');
  if (perPersonEl) perPersonEl.textContent = fmt(totalEach);

  const grandTotEl = document.getElementById('tip-grand-total-val');
  if (grandTotEl) grandTotEl.textContent = fmt(grandTotal);

  const totAmtEl = document.getElementById('tip-total-amount-val');
  if (totAmtEl) totAmtEl.textContent = fmt(totalTip);

  const tipEachEl = document.getElementById('tip-res-tip-each');
  if (tipEachEl) tipEachEl.textContent = fmt(tipEach);

  const baseEachEl = document.getElementById('tip-res-base-each');
  if (baseEachEl) baseEachEl.textContent = fmt(baseEach);

  const roundEl = document.getElementById('tip-res-rounded');
  if (roundEl) roundEl.textContent = (tipCurrency === 'INR' ? '₹' : '$') + formatNumberWithCommas(roundedEach, 2);

  const effEl = document.getElementById('tip-res-effective-pct');
  if (effEl) effEl.textContent = tipPct.toFixed(2) + '%';
}

function resetTip() {
  const bill = document.getElementById('tip-bill');
  const pct = document.getElementById('tip-custom-pct');
  const people = document.getElementById('tip-people');
  if (bill) bill.value = '1850';
  if (pct) pct.value = '10';
  if (people) people.value = '3';
  setTipCurrency('INR');
  calculateTip();
}

// ----------------------------------------------------------------------------
// 19. DISCOUNT + FINAL PRICE CALCULATOR
// ----------------------------------------------------------------------------
let dfpCurrency = 'INR';

function setDfpCurrency(curr) {
  dfpCurrency = curr;
  const inrBtn = document.getElementById('dfp-curr-inr');
  const usdBtn = document.getElementById('dfp-curr-usd');
  const label = document.getElementById('dfp-price-label');
  if (inrBtn && usdBtn) {
    if (curr === 'INR') {
      inrBtn.classList.add('active');
      usdBtn.classList.remove('active');
      if (label) label.textContent = 'Original Tag Price (₹)';
    } else {
      usdBtn.classList.add('active');
      inrBtn.classList.remove('active');
      if (label) label.textContent = 'Original Tag Price ($)';
    }
  }
  calculateDiscountFinalPrice();
}

function calculateDiscountFinalPrice() {
  const pInput = document.getElementById('dfp-original-price');
  const d1Input = document.getElementById('dfp-disc1');
  const d2Input = document.getElementById('dfp-disc2');
  const taxInput = document.getElementById('dfp-tax-pct');
  if (!pInput || !d1Input || !d2Input || !taxInput) return;

  const originalPrice = Math.max(0, parseFloat(pInput.value) || 0);
  const d1 = Math.min(100, Math.max(0, parseFloat(d1Input.value) || 0));
  const d2 = Math.min(100, Math.max(0, parseFloat(d2Input.value) || 0));
  const taxPct = Math.max(0, parseFloat(taxInput.value) || 0);

  const step1Price = originalPrice * (1 - (d1 / 100));
  const step2Price = step1Price * (1 - (d2 / 100));
  const taxAmount = step2Price * (taxPct / 100);
  const finalPrice = step2Price + taxAmount;

  const totalSaved = Math.max(0, originalPrice - step2Price);
  const effectiveDiscPct = originalPrice > 0 ? (totalSaved / originalPrice) * 100 : 0;
  const paidPct = originalPrice > 0 ? (finalPrice / originalPrice) * 100 : 0;

  const fmt = (val) => (dfpCurrency === 'INR' ? '₹' : '$') + formatNumberWithCommas(val, 2);

  const finalEl = document.getElementById('dfp-final-price-val');
  if (finalEl) finalEl.textContent = fmt(finalPrice);

  const saveEl = document.getElementById('dfp-total-saved-val');
  if (saveEl) saveEl.textContent = fmt(totalSaved);

  const effEl = document.getElementById('dfp-effective-pct-val');
  if (effEl) effEl.textContent = effectiveDiscPct.toFixed(2) + '% Off';

  const s1El = document.getElementById('dfp-res-step1');
  if (s1El) s1El.textContent = fmt(step1Price);

  const s2El = document.getElementById('dfp-res-step2');
  if (s2El) s2El.textContent = fmt(step2Price);

  const taxEl = document.getElementById('dfp-res-tax-amount');
  if (taxEl) taxEl.textContent = '+' + fmt(taxAmount);

  const paidEl = document.getElementById('dfp-res-paid-pct');
  if (paidEl) paidEl.textContent = paidPct.toFixed(2) + '%';
}

function resetDiscountFinalPrice() {
  const p = document.getElementById('dfp-original-price');
  const d1 = document.getElementById('dfp-disc1');
  const d2 = document.getElementById('dfp-disc2');
  const tax = document.getElementById('dfp-tax-pct');
  if (p) p.value = '2500';
  if (d1) d1.value = '30';
  if (d2) d2.value = '10';
  if (tax) tax.value = '12';
  setDfpCurrency('INR');
  calculateDiscountFinalPrice();
}

// ----------------------------------------------------------------------------
// 20. SALES TAX CALCULATOR
// ----------------------------------------------------------------------------
let stCurrency = 'INR';
let stMode = 'add'; // 'add' (tax exclusive) or 'extract' (tax inclusive)

function setStCurrency(curr) {
  stCurrency = curr;
  const inrBtn = document.getElementById('st-curr-inr');
  const usdBtn = document.getElementById('st-curr-usd');
  const label = document.getElementById('st-amount-label');
  if (inrBtn && usdBtn) {
    if (curr === 'INR') {
      inrBtn.classList.add('active');
      usdBtn.classList.remove('active');
      if (label) label.textContent = (stMode === 'add' ? 'Net Pre-Tax Amount (₹)' : 'Gross Total (Tax-Inclusive ₹)');
    } else {
      usdBtn.classList.add('active');
      inrBtn.classList.remove('active');
      if (label) label.textContent = (stMode === 'add' ? 'Net Pre-Tax Amount ($)' : 'Gross Total (Tax-Inclusive $)');
    }
  }
  calculateSalesTax();
}

function setStMode(mode) {
  stMode = mode;
  const addBtn = document.getElementById('st-mode-add');
  const extBtn = document.getElementById('st-mode-extract');
  const label = document.getElementById('st-amount-label');
  const sym = stCurrency === 'INR' ? '₹' : '$';

  if (addBtn && extBtn) {
    if (mode === 'add') {
      addBtn.classList.add('active');
      extBtn.classList.remove('active');
      if (label) label.textContent = 'Net Pre-Tax Amount (' + sym + ')';
    } else {
      extBtn.classList.add('active');
      addBtn.classList.remove('active');
      if (label) label.textContent = 'Gross Total (Tax-Inclusive ' + sym + ')';
    }
  }
  calculateSalesTax();
}

function calculateSalesTax() {
  const amtInput = document.getElementById('st-amount');
  const rateInput = document.getElementById('st-tax-rate');
  if (!amtInput || !rateInput) return;

  const inputAmt = Math.max(0, parseFloat(amtInput.value) || 0);
  const taxRate = Math.max(0, parseFloat(rateInput.value) || 0);

  let preTax = 0;
  let taxAmount = 0;
  let grossTotal = 0;

  if (stMode === 'add') {
    preTax = inputAmt;
    taxAmount = preTax * (taxRate / 100);
    grossTotal = preTax + taxAmount;
  } else {
    // Reverse calculation
    grossTotal = inputAmt;
    preTax = grossTotal / (1 + (taxRate / 100));
    taxAmount = grossTotal - preTax;
  }

  const multiplier = 1 + (taxRate / 100);
  const taxShare = grossTotal > 0 ? (taxAmount / grossTotal) * 100 : 0;
  const fmt = (val) => (stCurrency === 'INR' ? '₹' : '$') + formatNumberWithCommas(val, 2);

  const grossEl = document.getElementById('st-gross-val');
  if (grossEl) grossEl.textContent = fmt(grossTotal);

  const taxEl = document.getElementById('st-tax-amount-val');
  if (taxEl) taxEl.textContent = fmt(taxAmount);

  const netEl = document.getElementById('st-net-val');
  if (netEl) netEl.textContent = fmt(preTax);

  const rateEl = document.getElementById('st-res-tax-pct');
  if (rateEl) rateEl.textContent = taxRate.toFixed(2) + '%';

  const multEl = document.getElementById('st-res-multiplier');
  if (multEl) multEl.textContent = multiplier.toFixed(4);

  const shareEl = document.getElementById('st-res-share');
  if (shareEl) shareEl.textContent = taxShare.toFixed(2) + '%';
}

function resetSalesTax() {
  const amt = document.getElementById('st-amount');
  const rate = document.getElementById('st-tax-rate');
  if (amt) amt.value = '5000';
  if (rate) rate.value = '8.25';
  setStCurrency('INR');
  setStMode('add');
  calculateSalesTax();
}


// =========================================================================
// 8 NEW FEATURES IMPLEMENTATION
// 1. Favorite Tools | 2. Recently Used Tools | 3. Copy Result
// 4. Share Result  | 5. Share Website       | 6. Tool Categories
// 7. Related Tools | 8. Add to Home Screen / PWA
// =========================================================================

const TOOLS_INFO = {
  'pdf-merge': { name: 'PDF Merge', icon: '📑', category: 'pdf-images', desc: 'Combine multiple PDF documents into one file in custom page order.' },
  'pdf-split': { name: 'PDF Split', icon: '✂️', category: 'pdf-images', desc: 'Extract custom page ranges or split single pages from any PDF document.' },
  'pdf-to-images': { name: 'PDF to Images', icon: '🖼️', category: 'pdf-images', desc: 'Convert multi-page PDF documents into high-resolution JPG or PNG images.' },
  'images-to-pdf': { name: 'Images to PDF', icon: '📸', category: 'pdf-images', desc: 'Convert JPG, PNG, and WebP images into a single organized PDF document.' },
  'image-compressor': { name: 'Image Compressor', icon: '🗜️', category: 'pdf-images', desc: 'Compress JPG, PNG, and WebP images by up to 90% without visible loss.' },
  'image-resizer': { name: 'Image Resizer', icon: '📐', category: 'pdf-images', desc: 'Resize image dimensions by exact pixels or percentage with aspect ratio lock.' },
  'jpg-to-png': { name: 'JPG to PNG Converter', icon: '🔄', category: 'pdf-images', desc: 'Convert JPG/JPEG images to lossless transparent-ready PNG format.' },
  'png-to-jpg': { name: 'PNG to JPG Converter', icon: '🎨', category: 'pdf-images', desc: 'Convert PNG images to JPG with custom background color for transparency.' },
  'image-cropper': { name: 'Image Cropper', icon: '✂️', category: 'pdf-images', desc: 'Crop images with preset aspect ratios (1:1, 4:3, 16:9, Freeform) and live preview.' },
  'image-to-webp': { name: 'Image to WebP Converter', icon: '🚀', category: 'pdf-images', desc: 'Convert JPG and PNG images into lightweight next-gen WebP format.' },
  'age': { name: 'Age Calculator', icon: '🎂', category: 'datetime', desc: 'Exact age in years, months, days, countdown to next birthday.' },
  'emi': { name: 'EMI Loan Calculator', icon: '🏦', category: 'finance', desc: 'Monthly loan installment, total interest payable, repayment split.' },
  'percentage': { name: 'Percentage Calculator', icon: '📊', category: 'math', desc: 'Solve X% of Y, percent increase/decrease, and proportions.' },
  'discount': { name: 'Discount Calculator', icon: '🏷️', category: 'finance', desc: 'Sale price after discount, savings amount, and optional sales tax.' },
  'bmi': { name: 'BMI Health Calculator', icon: '⚖️', category: 'health', desc: 'Body Mass Index calculator with metric/imperial units and weight ranges.' },
  'gst': { name: 'GST Calculator', icon: '🧾', category: 'finance', desc: 'Calculate GST Exclusive and GST Inclusive prices with CGST/SGST/IGST.' },
  'simple-interest': { name: 'Simple Interest Calculator', icon: '📈', category: 'finance', desc: 'Calculate simple interest, maturity payoff, and monthly breakdown.' },
  'compound-interest': { name: 'Compound Interest Calculator', icon: '💹', category: 'finance', desc: 'Calculate compound interest growth with multiple compounding frequencies.' },
  'profit-loss': { name: 'Profit & Loss Calculator', icon: '💰', category: 'finance', desc: 'Compute profit or loss, profit margin, and percentage markup.' },
  'sip': { name: 'SIP Calculator', icon: '🪙', category: 'finance', desc: 'Estimate mutual fund Systematic Investment Plan future wealth.' },
  'fd': { name: 'FD Calculator', icon: '🏛️', category: 'finance', desc: 'Bank Fixed Deposit maturity amount, interest earned, and quarterly APY.' },
  'date-difference': { name: 'Date Difference Calculator', icon: '📅', category: 'datetime', desc: 'Calculate exact duration between two calendar dates in years, months, and days.' },
  'time': { name: 'Time Calculator', icon: '⏱️', category: 'datetime', desc: 'Add or subtract hours and minutes, or calculate time elapsed.' },
  'unit-converter': { name: 'Unit Converter', icon: '🔄', category: 'converters', desc: 'Multi-category converter for length, weight, temperature, and volume.' },
  'average': { name: 'Average Calculator', icon: '🔢', category: 'math', desc: 'Arithmetic mean, median, mode, sum, range, and standard deviation.' },
  'loan-interest': { name: 'Loan Interest Calculator', icon: '💳', category: 'finance', desc: 'Compute total interest cost and effective interest proportion.' },
  'loan-eligibility': { name: 'Loan Eligibility Calculator', icon: '🎯', category: 'finance', desc: 'Maximum eligible loan amount based on net income and obligations.' },
  'loan-tenure': { name: 'Loan Tenure Calculator', icon: '⏳', category: 'finance', desc: 'Calculate payoff duration and debt-free date based on monthly payment.' },
  'salary': { name: 'Salary Calculator', icon: '💵', category: 'finance', desc: 'Calculate net in-hand take-home pay from annual CTC.' },
  'overtime': { name: 'Overtime Pay Calculator', icon: '⏱️', category: 'finance', desc: 'Calculate overtime wages with standard 1.5x / 2.0x multipliers.' },
  'tax': { name: 'Tax Calculator', icon: '📜', category: 'finance', desc: 'Estimate tax liability and compare Old vs New tax regimes.' },
  'calorie': { name: 'Calorie Calculator', icon: '🥗', category: 'health', desc: 'Daily calories for weight maintenance, healthy loss, or gain.' },
  'bmr': { name: 'BMR Calculator', icon: '🔥', category: 'health', desc: 'Basal Metabolic Rate based on Mifflin-St Jeor formula.' },
  'tdee': { name: 'TDEE Calculator', icon: '⚡', category: 'health', desc: 'Total Daily Energy Expenditure factoring physical activity level.' },
  'pregnancy-due-date': { name: 'Pregnancy Due Date Calculator', icon: '👶', category: 'health', desc: 'Estimate delivery date and current trimester from last menstrual period.' },
  'hours-to-minutes': { name: 'Hours to Minutes Converter', icon: '⏲️', category: 'datetime', desc: 'Convert decimal hours and minutes into total minutes and seconds.' },
  'minutes-to-hours': { name: 'Minutes to Hours Converter', icon: '🕰️', category: 'datetime', desc: 'Convert minutes into decimal hours, hours + minutes, and work shifts.' },
  'length-converter': { name: 'Length Converter', icon: '📏', category: 'converters', desc: 'Convert millimeters, centimeters, meters, kilometers, feet, inches, miles.' },
  'weight-converter': { name: 'Weight Converter', icon: '⚖️', category: 'converters', desc: 'Convert grams, kilograms, tonnes, ounces, pounds, and stones.' },
  'temperature-converter': { name: 'Temperature Converter', icon: '🌡️', category: 'converters', desc: 'Convert Celsius, Fahrenheit, and Kelvin with reference markers.' },
  'area-converter': { name: 'Area Converter', icon: '🗺️', category: 'converters', desc: 'Convert square meters, square feet, acres, and hectares.' },
  'volume-converter': { name: 'Volume Converter', icon: '🧪', category: 'converters', desc: 'Convert liters, milliliters, gallons, cups, and fluid ounces.' },
  'tip': { name: 'Tip Calculator', icon: '🍽️', category: 'finance', desc: 'Calculate dining gratuity, total bill, and split evenly per guest.' },
  'discount-final-price': { name: 'Discount + Final Price Calculator', icon: '🛍️', category: 'finance', desc: 'Calculate stacked double discounts plus optional sales tax.' },
  'sales-tax': { name: 'Sales Tax Calculator', icon: '🏷️', category: 'finance', desc: 'Add sales tax or reverse-calculate pre-tax price from retail total.' },
  'pdf-merge': { name: 'PDF Merge', icon: '📑', category: 'pdf-images', desc: 'Combine multiple PDF documents into one file in custom page order.' },
  'pdf-split': { name: 'PDF Split', icon: '✂️', category: 'pdf-images', desc: 'Extract custom page ranges or split single pages from any PDF document.' },
  'pdf-to-images': { name: 'PDF to Images', icon: '🖼️', category: 'pdf-images', desc: 'Convert multi-page PDF documents into high-resolution JPG or PNG images.' },
  'images-to-pdf': { name: 'Images to PDF', icon: '📑', category: 'pdf-images', desc: 'Combine multiple JPG, PNG, and WebP images into a single clean PDF.' },
  'image-compressor': { name: 'Image Compressor', icon: '🗜️', category: 'pdf-images', desc: 'Reduce image file size while keeping visual clarity 100% locally.' },
  'image-resizer': { name: 'Image Resizer', icon: '📐', category: 'pdf-images', desc: 'Resize images to exact pixel dimensions or percentage scales.' },
  'jpg-to-png': { name: 'JPG to PNG Converter', icon: '🔁', category: 'pdf-images', desc: 'Convert JPG and JPEG images to lossless high-clarity PNG format.' },
  'png-to-jpg': { name: 'PNG to JPG Converter', icon: '🔄', category: 'pdf-images', desc: 'Transform PNG graphics into compressed JPGs with custom background color.' },
  'image-cropper': { name: 'Image Cropper', icon: '✂️', category: 'pdf-images', desc: 'Crop photos and graphics with standard aspect ratio presets or custom box.' },
  'image-to-webp': { name: 'Image to WebP Converter', icon: '⚡', category: 'pdf-images', desc: 'Convert JPG and PNG images to ultra-lightweight next-gen WebP format.' },
};

const RELATED_TOOLS_MAP = {
  'pdf-merge': ['pdf-split', 'pdf-to-images', 'images-to-pdf'],
  'pdf-split': ['pdf-merge', 'pdf-to-images', 'images-to-pdf'],
  'pdf-to-images': ['images-to-pdf', 'pdf-split', 'image-compressor'],
  'images-to-pdf': ['pdf-to-images', 'pdf-merge', 'image-compressor'],
  'image-compressor': ['image-resizer', 'image-to-webp', 'image-cropper'],
  'image-resizer': ['image-compressor', 'image-cropper', 'image-to-webp'],
  'jpg-to-png': ['png-to-jpg', 'image-to-webp', 'image-compressor'],
  'png-to-jpg': ['jpg-to-png', 'image-to-webp', 'image-compressor'],
  'image-cropper': ['image-resizer', 'image-compressor', 'image-to-webp'],
  'image-to-webp': ['image-compressor', 'jpg-to-png', 'png-to-jpg'],
  'age': ['date-difference', 'time', 'hours-to-minutes', 'pregnancy-due-date'],
  'emi': ['loan-interest', 'loan-eligibility', 'loan-tenure', 'fd'],
  'percentage': ['discount', 'profit-loss', 'gst', 'average'],
  'discount': ['discount-final-price', 'sales-tax', 'percentage', 'tip'],
  'bmi': ['calorie', 'bmr', 'tdee', 'pregnancy-due-date'],
  'gst': ['sales-tax', 'tax', 'profit-loss', 'discount'],
  'simple-interest': ['compound-interest', 'loan-interest', 'sip', 'fd'],
  'compound-interest': ['simple-interest', 'sip', 'fd', 'loan-interest'],
  'profit-loss': ['discount', 'percentage', 'gst', 'sales-tax'],
  'sip': ['compound-interest', 'fd', 'simple-interest', 'salary'],
  'fd': ['sip', 'compound-interest', 'simple-interest', 'emi'],
  'date-difference': ['age', 'time', 'hours-to-minutes', 'minutes-to-hours'],
  'time': ['hours-to-minutes', 'minutes-to-hours', 'date-difference', 'overtime'],
  'unit-converter': ['length-converter', 'weight-converter', 'temperature-converter', 'volume-converter'],
  'average': ['percentage', 'profit-loss', 'time', 'salary'],
  'loan-interest': ['emi', 'loan-eligibility', 'loan-tenure', 'simple-interest'],
  'loan-eligibility': ['emi', 'loan-interest', 'loan-tenure', 'salary'],
  'loan-tenure': ['emi', 'loan-interest', 'loan-eligibility', 'simple-interest'],
  'salary': ['overtime', 'tax', 'loan-eligibility', 'sip'],
  'overtime': ['salary', 'time', 'hours-to-minutes', 'tax'],
  'tax': ['salary', 'gst', 'sales-tax', 'overtime'],
  'calorie': ['bmr', 'tdee', 'bmi', 'pregnancy-due-date'],
  'bmr': ['tdee', 'calorie', 'bmi', 'pregnancy-due-date'],
  'tdee': ['bmr', 'calorie', 'bmi', 'pregnancy-due-date'],
  'pregnancy-due-date': ['age', 'date-difference', 'bmi', 'calorie'],
  'hours-to-minutes': ['minutes-to-hours', 'time', 'date-difference', 'overtime'],
  'minutes-to-hours': ['hours-to-minutes', 'time', 'date-difference', 'overtime'],
  'length-converter': ['unit-converter', 'area-converter', 'weight-converter', 'volume-converter'],
  'weight-converter': ['unit-converter', 'volume-converter', 'bmi', 'length-converter'],
  'temperature-converter': ['unit-converter', 'length-converter', 'weight-converter', 'volume-converter'],
  'area-converter': ['length-converter', 'volume-converter', 'unit-converter', 'weight-converter'],
  'volume-converter': ['unit-converter', 'area-converter', 'weight-converter', 'length-converter'],
  'tip': ['discount', 'discount-final-price', 'sales-tax', 'percentage'],
  'discount-final-price': ['discount', 'sales-tax', 'tip', 'percentage'],
  'sales-tax': ['tax', 'gst', 'discount', 'discount-final-price']
};

// ================= TOAST NOTIFICATION SYSTEM =================
let toastTimeout = null;
function showToast(message, duration = 2500) {
  let toast = document.getElementById('toast-notification');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'toast-notification';
    toast.className = 'toast-notification';
    document.body.appendChild(toast);
  }
  toast.textContent = message;
  toast.classList.add('show');
  toast.style.display = 'flex';

  if (toastTimeout) clearTimeout(toastTimeout);
  toastTimeout = setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => {
      if (!toast.classList.contains('show')) {
        toast.style.display = 'none';
      }
    }, 200);
  }, duration);
}

// ================= FEATURE 1: FAVORITE TOOLS =================
function getFavorites() {
  try {
    const raw = localStorage.getItem('mut_favorites');
    return raw ? JSON.parse(raw) : [];
  } catch (e) {
    return [];
  }
}

function saveFavorites(favs) {
  try {
    localStorage.setItem('mut_favorites', JSON.stringify(favs));
  } catch (e) {}
}

function toggleFavorite(toolId, event) {
  if (event) {
    event.stopPropagation();
    event.preventDefault();
  }
  const favs = getFavorites();
  const idx = favs.indexOf(toolId);
  let isFav = false;

  if (idx > -1) {
    favs.splice(idx, 1);
    isFav = false;
  } else {
    favs.push(toolId);
    isFav = true;
  }
  saveFavorites(favs);
  updateFavoriteButtons();
  renderFavoritesSection();

  const toolName = TOOLS_INFO[toolId] ? TOOLS_INFO[toolId].name : 'Tool';
  showToast(isFav ? `⭐ Added "${toolName}" to Favorites` : `Removed "${toolName}" from Favorites`);
}

function updateFavoriteButtons() {
  const favs = getFavorites();

  // Update card buttons
  document.querySelectorAll('.card-fav-btn').forEach(btn => {
    const tid = btn.getAttribute('data-tool-id');
    const isFav = favs.includes(tid);
    if (isFav) {
      btn.classList.add('active');
      btn.setAttribute('title', 'Remove from favorites');
      btn.innerHTML = '<span class="fav-star">★</span>';
    } else {
      btn.classList.remove('active');
      btn.setAttribute('title', 'Add to favorites');
      btn.innerHTML = '<span class="fav-star">☆</span>';
    }
  });

  // Update header buttons on tool screens
  document.querySelectorAll('.header-fav-btn').forEach(btn => {
    const tid = btn.getAttribute('data-tool-id');
    const isFav = favs.includes(tid);
    if (isFav) {
      btn.classList.add('active');
      btn.innerHTML = '<span class="header-fav-star">★</span> <span class="header-fav-text">Favorited</span>';
    } else {
      btn.classList.remove('active');
      btn.innerHTML = '<span class="header-fav-star">☆</span> <span class="header-fav-text">Favorite</span>';
    }
  });
}

function renderFavoritesSection() {
  const sec = document.getElementById('favorite-tools-section');
  const grid = document.getElementById('favorite-tools-grid');
  const countBadge = document.getElementById('fav-count-badge');
  if (!sec || !grid) return;

  const favs = getFavorites().filter(tid => TOOLS_INFO[tid]);

  if (favs.length === 0) {
    sec.style.display = 'none';
    return;
  }

  sec.style.display = 'block';
  if (countBadge) countBadge.textContent = favs.length;

  grid.innerHTML = favs.map(tid => {
    const info = TOOLS_INFO[tid];
    return `
      <div class="compact-tool-item" onclick="navigateTo('${tid}')" role="button" tabindex="0" title="Open ${info.name}">
        <button type="button" class="compact-unfav-btn" onclick="event.stopPropagation(); toggleFavorite('${tid}', event);" title="Remove favorite" aria-label="Remove favorite">★</button>
        <div class="compact-tool-icon">${info.icon}</div>
        <div class="compact-tool-name">${info.name}</div>
        <div class="compact-tool-action">Open Tool →</div>
      </div>
    `;
  }).join('');
}

// ================= FEATURE 2: RECENTLY USED TOOLS =================
function getRecentTools() {
  try {
    const raw = localStorage.getItem('mut_recent_tools');
    return raw ? JSON.parse(raw) : [];
  } catch (e) {
    return [];
  }
}

function recordRecentTool(toolId) {
  if (!TOOLS_INFO[toolId]) return;
  try {
    let recent = getRecentTools().filter(id => id !== toolId && TOOLS_INFO[id]);
    recent.unshift(toolId);
    if (recent.length > 6) recent = recent.slice(0, 6);
    localStorage.setItem('mut_recent_tools', JSON.stringify(recent));
    renderRecentToolsSection();
  } catch (e) {}
}

function clearRecentTools() {
  try {
    localStorage.removeItem('mut_recent_tools');
  } catch (e) {}
  renderRecentToolsSection();
  showToast('✓ Recent tools history cleared');
}

function renderRecentToolsSection() {
  const sec = document.getElementById('recent-tools-section');
  const grid = document.getElementById('recent-tools-grid');
  const countBadge = document.getElementById('recent-count-badge');
  if (!sec || !grid) return;

  const recent = getRecentTools().filter(tid => TOOLS_INFO[tid]);

  if (recent.length === 0) {
    sec.style.display = 'none';
    return;
  }

  sec.style.display = 'block';
  if (countBadge) countBadge.textContent = recent.length;

  grid.innerHTML = recent.map(tid => {
    const info = TOOLS_INFO[tid];
    return `
      <div class="compact-tool-item" onclick="navigateTo('${tid}')" role="button" tabindex="0" title="Open ${info.name}">
        <div class="compact-tool-icon">${info.icon}</div>
        <div class="compact-tool-name">${info.name}</div>
        <div class="compact-tool-action">Open Tool →</div>
      </div>
    `;
  }).join('');
}

// ================= FEATURE 3 & 4: COPY RESULT & SHARE RESULT =================
function getResultText(toolId) {
  const info = TOOLS_INFO[toolId];
  const toolName = info ? info.name : 'Calculator';
  const url = `https://jitenswsw8250-ctrl.github.io/my-useful-tools/#${toolId}`;

  // Dedicated formatters for primary high-detail tools
    if (toolId === 'pdf-merge') {
    const pages = document.getElementById('pdf-merge-result-pages')?.textContent?.trim() || 'Multiple';
    const size = document.getElementById('pdf-merge-result-size')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - PDF Merge\nCombined ${pages} Pages into a single PDF (Total: ${size})\n${url}`;
  }
  if (toolId === 'pdf-split') {
    const pages = document.getElementById('pdf-split-result-pages')?.textContent?.trim() || '1';
    const range = document.getElementById('pdf-split-result-range')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - PDF Split\nExtracted ${pages} Pages (${range})\n${url}`;
  }
  if (toolId === 'pdf-to-images') {
    const pages = document.getElementById('pdf2img-rendered-count')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - PDF to Images\nRendered ${pages} PDF Pages to Images\n${url}`;
  }
  if (toolId === 'images-to-pdf') {
    const count = document.getElementById('img2pdf-result-count')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - Images to PDF\nCompiled ${count} Images into PDF\n${url}`;
  }
  if (toolId === 'image-compressor') {
    const orig = document.getElementById('imgcomp-res-orig')?.textContent?.trim() || '';
    const comp = document.getElementById('imgcomp-res-new')?.textContent?.trim() || '';
    const saving = document.getElementById('imgcomp-res-saving')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - Image Compressor\nOriginal: ${orig} → Compressed: ${comp} (Saved ${saving})\n${url}`;
  }
  if (toolId === 'image-resizer') {
    const dims = document.getElementById('imgresize-res-dims')?.textContent?.trim() || '';
    const size = document.getElementById('imgresize-res-size')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - Image Resizer\nResized Dimensions: ${dims} px (${size})\n${url}`;
  }
  if (toolId === 'jpg-to-png') {
    const size = document.getElementById('jpg2png-res-size')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - JPG to PNG Converter\nConverted to Lossless PNG (${size})\n${url}`;
  }
  if (toolId === 'png-to-jpg') {
    const orig = document.getElementById('png2jpg-res-orig')?.textContent?.trim() || '';
    const nw = document.getElementById('png2jpg-res-new')?.textContent?.trim() || '';
    const red = document.getElementById('png2jpg-res-reduction')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - PNG to JPG Converter\nOriginal: ${orig} → New JPG: ${nw} (${red})\n${url}`;
  }
  if (toolId === 'image-cropper') {
    const dims = document.getElementById('imgcrop-res-dims')?.textContent?.trim() || '';
    const ratio = document.getElementById('imgcrop-res-ratio')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - Image Cropper\nCropped to ${dims} px (${ratio})\n${url}`;
  }
  if (toolId === 'image-to-webp') {
    const orig = document.getElementById('img2webp-res-orig')?.textContent?.trim() || '';
    const nw = document.getElementById('img2webp-res-new')?.textContent?.trim() || '';
    const saved = document.getElementById('img2webp-res-saved')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - Image to WebP Converter\nOriginal: ${orig} → WebP: ${nw} (Saved ${saved})\n${url}`;
  }
  if (toolId === 'age') {
    const years = document.getElementById('age-years-num')?.textContent?.trim() || '';
    const breakdown = document.getElementById('age-breakdown')?.textContent?.trim() || '';
    const nextBday = document.getElementById('age-next-bday')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - ${toolName}\nExact Age: ${years} Years Old (${breakdown})\nNext Birthday: In ${nextBday}\n${url}`;
  }
  if (toolId === 'emi') {
    const emi = document.getElementById('emi-monthly-val')?.textContent?.trim() || '';
    const interest = document.getElementById('emi-total-interest')?.textContent?.trim() || '';
    const payment = document.getElementById('emi-total-payment')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - ${toolName}\nMonthly EMI: ${emi}\nTotal Interest: ${interest}\nTotal Payment: ${payment}\n${url}`;
  }
  if (toolId === 'percentage') {
    let res = '';
    const p1 = document.getElementById('pct-mode-0');
    const p2 = document.getElementById('pct-mode-1');
    const p3 = document.getElementById('pct-mode-2');
    if (p1 && p1.classList.contains('active')) {
      res = document.getElementById('pct-m1-expl')?.textContent?.trim() || document.getElementById('pct-m1-res')?.textContent?.trim();
    } else if (p2 && p2.classList.contains('active')) {
      res = document.getElementById('pct-m2-expl')?.textContent?.trim() || document.getElementById('pct-m2-res')?.textContent?.trim();
    } else if (p3 && p3.classList.contains('active')) {
      res = document.getElementById('pct-m3-expl')?.textContent?.trim() || document.getElementById('pct-m3-res')?.textContent?.trim();
    } else {
      res = document.getElementById('pct-m1-res')?.textContent?.trim() || '';
    }
    return `MY USEFUL TOOLS - ${toolName}\nResult: ${res}\n${url}`;
  }
  if (toolId === 'discount') {
    const finalVal = document.getElementById('disc-final-val')?.textContent?.trim() || '';
    const saveVal = document.getElementById('disc-savings-val')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - ${toolName}\nFinal Sale Price: ${finalVal}\nTotal Savings: ${saveVal}\n${url}`;
  }
  if (toolId === 'bmi') {
    const score = document.getElementById('bmi-score-val')?.textContent?.trim() || '';
    const cat = document.getElementById('bmi-category-badge')?.textContent?.trim() || '';
    const range = document.getElementById('bmi-healthy-range')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - ${toolName}\nBMI Score: ${score} (${cat})\nHealthy Range: ${range}\n${url}`;
  }

  // Generic extractor for all other tools
  const section = document.getElementById(`screen-${toolId}`);
  if (!section) return `MY USEFUL TOOLS - ${toolName}\n${url}`;

  const card = section.querySelector('.result-card');
  if (!card) return `MY USEFUL TOOLS - ${toolName}\n${url}`;

  const header = card.querySelector('.stat-header, .result-header')?.textContent?.trim() || 'Calculated Result';
  const num = card.querySelector('.highlight-number')?.textContent?.trim() || '';
  const unit = card.querySelector('.highlight-unit')?.textContent?.trim() || '';

  const metrics = [];
  card.querySelectorAll('.metric-box').forEach(mb => {
    const lbl = mb.querySelector('.metric-label')?.textContent?.trim();
    const val = mb.querySelector('.metric-val, .metric-number')?.textContent?.trim();
    if (lbl && val) metrics.push(`${lbl}: ${val}`);
  });

  let text = `MY USEFUL TOOLS - ${toolName}\n${header}: ${num} ${unit}`.trim();
  if (metrics.length) {
    text += '\n' + metrics.slice(0, 3).join('\n');
  }
  text += `\n${url}`;
  return text;
}

function copyCurrentResult(toolId) {
  const text = getResultText(toolId);
  const doFeedback = () => {
    showToast('✓ Copied!');
    const btn = document.querySelector(`#result-actions-${toolId} .copy-btn`);
    if (btn) {
      const orig = btn.innerHTML;
      btn.innerHTML = '<span class="btn-icon">✓</span> Copied!';
      setTimeout(() => { btn.innerHTML = orig; }, 2000);
    }
  };

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).then(doFeedback).catch(() => {
      fallbackCopy(text, doFeedback);
    });
  } else {
    fallbackCopy(text, doFeedback);
  }
}

function fallbackCopy(text, callback) {
  const ta = document.createElement('textarea');
  ta.value = text;
  ta.style.position = 'fixed';
  ta.style.left = '-9999px';
  document.body.appendChild(ta);
  ta.focus();
  ta.select();
  try {
    document.execCommand('copy');
    if (callback) callback();
  } catch (err) {
    prompt('Copy result:', text);
  }
  document.body.removeChild(ta);
}

function shareCurrentResult(toolId) {
  const text = getResultText(toolId);
  const info = TOOLS_INFO[toolId];
  const toolName = info ? info.name : 'Calculator';
  const url = `https://jitenswsw8250-ctrl.github.io/my-useful-tools/#${toolId}`;

  if (navigator.share) {
    navigator.share({
      title: `MY USEFUL TOOLS - ${toolName}`,
      text: text,
      url: url
    }).catch(() => {});
  } else {
    copyCurrentResult(toolId);
    showToast('✓ Result copied to clipboard for sharing!');
  }
}

// ================= FEATURE 5: SHARE APP / SHARE WEBSITE =================
function shareWebsite() {
  const shareData = {
    title: 'MY USEFUL TOOLS',
    text: 'Free online calculators and useful tools.',
    url: 'https://jitenswsw8250-ctrl.github.io/my-useful-tools/'
  };

  if (navigator.share) {
    navigator.share(shareData).catch(() => {});
  } else if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(shareData.url).then(() => {
      showToast('✓ Link copied!');
    }).catch(() => {
      prompt('Copy website link:', shareData.url);
    });
  } else {
    prompt('Copy website link:', shareData.url);
  }
}

// ================= FEATURE 7: RELATED TOOLS =================
function initRelatedTools() {
  document.querySelectorAll('.related-tools-section').forEach(container => {
    const tid = container.getAttribute('data-tool');
    const relatedIds = RELATED_TOOLS_MAP[tid] || [];
    if (!relatedIds.length) return;

    const cardsHtml = relatedIds.map(rid => {
      const info = TOOLS_INFO[rid];
      if (!info) return '';
      return `
        <div class="related-tool-card" onclick="navigateTo('${rid}')" role="button" tabindex="0" title="Open ${info.name}">
          <div class="related-tool-icon">${info.icon}</div>
          <div class="related-tool-info">
            <div class="related-tool-name">${info.name}</div>
            <div class="related-tool-sub">${info.desc}</div>
          </div>
        </div>
      `;
    }).join('');

    container.innerHTML = `
      <h3 class="related-tools-title"><span>🔗</span> Related Calculators &amp; Tools</h3>
      <div class="related-tools-grid">
        ${cardsHtml}
      </div>
    `;
  });
}

// ================= FEATURE 8: PWA & SERVICE WORKER =================
let deferredPwaPrompt = null;

function setupPwa() {
  if ('serviceWorker' in navigator && (window.location.protocol === 'https:' || window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1')) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('sw.js').catch(() => {});
    });
  }

  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPwaPrompt = e;
    const heroBtn = document.getElementById('pwa-install-btn');
    if (heroBtn) heroBtn.style.display = 'inline-flex';
    const drawerBtn = document.getElementById('drawer-install-btn');
    if (drawerBtn) drawerBtn.style.display = 'flex';
  });

  window.addEventListener('appinstalled', () => {
    deferredPwaPrompt = null;
    const heroBtn = document.getElementById('pwa-install-btn');
    if (heroBtn) heroBtn.style.display = 'none';
    const drawerBtn = document.getElementById('drawer-install-btn');
    if (drawerBtn) drawerBtn.style.display = 'none';
    showToast('✓ App installed successfully!');
  });
}

function installPwa() {
  if (deferredPwaPrompt) {
    deferredPwaPrompt.prompt();
    deferredPwaPrompt.userChoice.then((choice) => {
      if (choice && choice.outcome === 'accepted') {
        showToast('✓ Adding MY USEFUL TOOLS to Home Screen...');
      }
      deferredPwaPrompt = null;
      const heroBtn = document.getElementById('pwa-install-btn');
      if (heroBtn) heroBtn.style.display = 'none';
    });
  } else {
    showToast('To install: open browser menu (⋮) and tap "Add to Home screen"');
  }
}

// ================= MASTER INITIALIZER FOR NEW FEATURES =================
function initNewFeatures() {
  updateFavoriteButtons();
  renderFavoritesSection();
  renderRecentToolsSection();
  initRelatedTools();
  setupPwa();
}




// ============================================================================
// ============================================================================
// PDF & IMAGE TOOLS - 10 BROWSER-BASED UTILITY TOOLS
// 100% Client-Side, Zero Server Uploads, Fully Local, Fast and Private
// ============================================================================

// Utility: Format bytes into human-readable string (e.g. 1.25 MB)
function formatBytes(bytes, decimals = 1) {
  if (!bytes || bytes === 0) return '0 B';
  const k = 1024;
  const dm = decimals < 0 ? 0 : decimals;
  const sizes = ['B', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
}

// Utility: Trigger reliable browser download for a Blob
function downloadBlob(blob, filename) {
  if (!blob) return;
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  a.style.display = 'none';
  document.body.appendChild(a);
  a.click();
  setTimeout(() => {
    try {
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    } catch (e) {}
  }, 2000);
}

// Drag & Drop Setup for all 10 tools
function initFileDropzones() {
  const dropzoneConfigs = [
    { id: 'pdf-merge-dropzone', inputId: 'pdf-merge-input', handler: files => handlePdfMergeFiles(files) },
    { id: 'pdf-split-dropzone', inputId: 'pdf-split-input', handler: files => files[0] && handlePdfSplitFile(files[0]) },
    { id: 'pdf2img-dropzone', inputId: 'pdf2img-input', handler: files => files[0] && handlePdfToImagesFile(files[0]) },
    { id: 'img2pdf-dropzone', inputId: 'img2pdf-input', handler: files => handleImagesToPdfFiles(files) },
    { id: 'imgcomp-dropzone', inputId: 'imgcomp-input', handler: files => files[0] && handleImageCompressorFile(files[0]) },
    { id: 'imgresize-dropzone', inputId: 'imgresize-input', handler: files => files[0] && handleImageResizerFile(files[0]) },
    { id: 'jpg2png-dropzone', inputId: 'jpg2png-input', handler: files => files[0] && handleJpgToPngFile(files[0]) },
    { id: 'png2jpg-dropzone', inputId: 'png2jpg-input', handler: files => files[0] && handlePngToJpgFile(files[0]) },
    { id: 'imgcrop-dropzone', inputId: 'imgcrop-input', handler: files => files[0] && handleImageCropperFile(files[0]) },
    { id: 'img2webp-dropzone', inputId: 'img2webp-input', handler: files => files[0] && handleImageToWebpFile(files[0]) }
  ];

  dropzoneConfigs.forEach(cfg => {
    const el = document.getElementById(cfg.id);
    if (!el) return;
    ['dragenter', 'dragover'].forEach(evt => {
      el.addEventListener(evt, e => {
        e.preventDefault();
        e.stopPropagation();
        el.classList.add('dragover');
      });
    });
    ['dragleave', 'drop'].forEach(evt => {
      el.addEventListener(evt, e => {
        e.preventDefault();
        e.stopPropagation();
        el.classList.remove('dragover');
      });
    });
    el.addEventListener('drop', e => {
      if (e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files.length) {
        cfg.handler(e.dataTransfer.files);
      }
    });
  });
}

// ==================== 1. PDF MERGE ====================
let pdfMergeFiles = [];
let pdfMergeResultBlob = null;

function handlePdfMergeFiles(files) {
  const errEl = document.getElementById('pdf-merge-error');
  if (errEl) errEl.style.display = 'none';

  if (!files || files.length === 0) return;

  for (let i = 0; i < files.length; i++) {
    const f = files[i];
    if (f.type === 'application/pdf' || f.name.toLowerCase().endsWith('.pdf')) {
      pdfMergeFiles.push(f);
    }
  }

  if (pdfMergeFiles.length === 0) {
    if (errEl) {
      errEl.textContent = 'Please select valid PDF documents (.pdf).';
      errEl.style.display = 'block';
    }
    return;
  }

  renderPdfMergeList();
}

function renderPdfMergeList() {
  const container = document.getElementById('pdf-merge-list-container');
  const listEl = document.getElementById('pdf-merge-file-list');
  const countEl = document.getElementById('pdf-merge-count');
  const mergeBtn = document.getElementById('pdf-merge-btn');
  const actionRow = document.getElementById('pdf-merge-action-row');

  if (!container || !listEl) return;

  if (pdfMergeFiles.length === 0) {
    container.style.display = 'none';
    if (actionRow) actionRow.style.display = 'none';
    if (mergeBtn) mergeBtn.disabled = true;
    return;
  }

  container.style.display = 'block';
  if (actionRow) actionRow.style.display = 'flex';
  if (countEl) countEl.textContent = pdfMergeFiles.length;
  if (mergeBtn) mergeBtn.disabled = pdfMergeFiles.length < 2;

  listEl.innerHTML = pdfMergeFiles.map((file, idx) => `
    <div class="file-item-row" data-index="${idx}">
      <span class="file-item-idx">#${idx + 1}</span>
      <span class="file-item-icon">📄</span>
      <div class="file-item-details">
        <span class="file-item-name" title="${file.name}">${file.name}</span>
        <span class="file-item-size">${formatBytes(file.size)}</span>
      </div>
      <div class="file-item-actions">
        <button type="button" class="btn-icon-order" onclick="movePdfMergeItem(${idx}, -1)" ${idx === 0 ? 'disabled' : ''} title="Move Up">⬆</button>
        <button type="button" class="btn-icon-order" onclick="movePdfMergeItem(${idx}, 1)" ${idx === pdfMergeFiles.length - 1 ? 'disabled' : ''} title="Move Down">⬇</button>
        <button type="button" class="btn-icon-delete" onclick="removePdfMergeItem(${idx})" title="Remove">✕</button>
      </div>
    </div>
  `).join('');
}

function movePdfMergeItem(index, direction) {
  const newIndex = index + direction;
  if (newIndex < 0 || newIndex >= pdfMergeFiles.length) return;
  const temp = pdfMergeFiles[index];
  pdfMergeFiles[index] = pdfMergeFiles[newIndex];
  pdfMergeFiles[newIndex] = temp;
  renderPdfMergeList();
}

function removePdfMergeItem(index) {
  pdfMergeFiles.splice(index, 1);
  renderPdfMergeList();
}

async function processPdfMerge() {
  const errEl = document.getElementById('pdf-merge-error');
  const progEl = document.getElementById('pdf-merge-progress');
  const resultCard = document.getElementById('pdf-merge-result');
  const mergeBtn = document.getElementById('pdf-merge-btn');

  if (errEl) errEl.style.display = 'none';
  if (resultCard) resultCard.style.display = 'none';

  if (pdfMergeFiles.length < 2) {
    if (errEl) {
      errEl.textContent = 'Please select at least 2 PDF files to merge.';
      errEl.style.display = 'block';
    }
    return;
  }

  if (typeof PDFLib === 'undefined') {
    if (errEl) {
      errEl.textContent = 'PDF engine is loading. Please wait a moment and try again.';
      errEl.style.display = 'block';
    }
    return;
  }

  try {
    if (mergeBtn) mergeBtn.disabled = true;
    if (progEl) {
      progEl.textContent = 'Merging PDF documents locally in your browser...';
      progEl.style.display = 'block';
    }

    const mergedPdf = await PDFLib.PDFDocument.create();
    let totalPagesMerged = 0;

    for (let i = 0; i < pdfMergeFiles.length; i++) {
      const file = pdfMergeFiles[i];
      if (progEl) progEl.textContent = `Merging file ${i + 1} of ${pdfMergeFiles.length}: ${file.name}...`;
      const arrayBuffer = await file.arrayBuffer();
      const pdf = await PDFLib.PDFDocument.load(arrayBuffer, { ignoreEncryption: true });
      const copiedPages = await mergedPdf.copyPages(pdf, pdf.getPageIndices());
      copiedPages.forEach(page => mergedPdf.addPage(page));
      totalPagesMerged += copiedPages.length;
    }

    if (progEl) progEl.textContent = 'Finalizing merged PDF...';
    const mergedPdfBytes = await mergedPdf.save();
    pdfMergeResultBlob = new Blob([mergedPdfBytes], { type: 'application/pdf' });

    if (progEl) progEl.style.display = 'none';

    // Populate results
    document.getElementById('pdf-merge-result-pages').textContent = totalPagesMerged;
    document.getElementById('pdf-merge-result-count').textContent = pdfMergeFiles.length;
    document.getElementById('pdf-merge-result-size').textContent = formatBytes(pdfMergeResultBlob.size);

    if (resultCard) {
      resultCard.style.display = 'block';
      resultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
    showToast('✓ PDFs merged successfully!');
  } catch (err) {
    console.error('PDF Merge Error:', err);
    if (progEl) progEl.style.display = 'none';
    if (errEl) {
      errEl.textContent = 'Unable to merge selected PDFs. One of the documents may be password protected or corrupted.';
      errEl.style.display = 'block';
    }
  } finally {
    if (mergeBtn) mergeBtn.disabled = false;
  }
}

function downloadMergedPdf() {
  if (!pdfMergeResultBlob) return;
  downloadBlob(pdfMergeResultBlob, `merged-document-${Date.now()}.pdf`);
}

function resetPdfMerge() {
  pdfMergeFiles = [];
  pdfMergeResultBlob = null;
  renderPdfMergeList();
  const input = document.getElementById('pdf-merge-input');
  if (input) input.value = '';
  const resultCard = document.getElementById('pdf-merge-result');
  if (resultCard) resultCard.style.display = 'none';
  const errEl = document.getElementById('pdf-merge-error');
  if (errEl) errEl.style.display = 'none';
  const progEl = document.getElementById('pdf-merge-progress');
  if (progEl) progEl.style.display = 'none';
}

// ==================== 2. PDF SPLIT ====================
let pdfSplitLoadedFile = null;
let pdfSplitTotalPagesCount = 0;
let pdfSplitResultBlob = null;

async function handlePdfSplitFile(file) {
  const errEl = document.getElementById('pdf-split-error');
  const summaryEl = document.getElementById('pdf-split-summary');
  const controlsEl = document.getElementById('pdf-split-controls');
  const actionRow = document.getElementById('pdf-split-action-row');
  const resultCard = document.getElementById('pdf-split-result');

  if (errEl) errEl.style.display = 'none';
  if (resultCard) resultCard.style.display = 'none';
  if (!file) return;

  if (file.type !== 'application/pdf' && !file.name.toLowerCase().endsWith('.pdf')) {
    if (errEl) {
      errEl.textContent = 'Please choose a valid PDF file (.pdf).';
      errEl.style.display = 'block';
    }
    return;
  }

  if (typeof PDFLib === 'undefined') {
    if (errEl) {
      errEl.textContent = 'PDF engine is loading. Please retry in a moment.';
      errEl.style.display = 'block';
    }
    return;
  }

  try {
    const arrayBuffer = await file.arrayBuffer();
    const pdfDoc = await PDFLib.PDFDocument.load(arrayBuffer, { ignoreEncryption: true });

    pdfSplitLoadedFile = file;
    pdfSplitTotalPagesCount = pdfDoc.getPageCount();

    document.getElementById('pdf-split-filename').textContent = file.name;
    document.getElementById('pdf-split-total-pages').textContent = pdfSplitTotalPagesCount;
    document.getElementById('pdf-split-filesize').textContent = formatBytes(file.size);

    const initialRange = pdfSplitTotalPagesCount > 1 ? `1-${Math.min(3, pdfSplitTotalPagesCount)}` : '1';
    const rangeInput = document.getElementById('pdf-split-range');
    if (rangeInput) rangeInput.value = initialRange;

    onPdfSplitRangeInput();

    if (summaryEl) summaryEl.style.display = 'flex';
    if (controlsEl) controlsEl.style.display = 'block';
    if (actionRow) actionRow.style.display = 'flex';
  } catch (err) {
    console.error('PDF Split Load Error:', err);
    if (errEl) {
      errEl.textContent = 'Could not read PDF. Document may be encrypted or corrupted.';
      errEl.style.display = 'block';
    }
  }
}

function setPdfSplitPreset(preset) {
  if (!pdfSplitTotalPagesCount) return;
  const input = document.getElementById('pdf-split-range');
  if (!input) return;

  if (preset === 'all') {
    input.value = `1-${pdfSplitTotalPagesCount}`;
  } else if (preset === 'first') {
    input.value = '1';
  } else if (preset === 'odd') {
    const odds = [];
    for (let p = 1; p <= pdfSplitTotalPagesCount; p += 2) odds.push(p);
    input.value = odds.join(', ');
  } else if (preset === 'even') {
    const evens = [];
    for (let p = 2; p <= pdfSplitTotalPagesCount; p += 2) evens.push(p);
    input.value = evens.length ? evens.join(', ') : (pdfSplitTotalPagesCount >= 2 ? '2' : '1');
  }
  onPdfSplitRangeInput();
}

function onPdfSplitRangeInput() {
  const input = document.getElementById('pdf-split-range');
  const hint = document.getElementById('pdf-split-range-hint');
  const splitBtn = document.getElementById('pdf-split-btn');
  if (!input || !hint) return;

  const val = input.value.trim();
  if (!val) {
    hint.textContent = 'Please enter pages or ranges (e.g. 1-3, 5).';
    hint.style.color = 'var(--text-muted)';
    if (splitBtn) splitBtn.disabled = true;
    return;
  }

  try {
    const indices = parsePageRanges(val, pdfSplitTotalPagesCount);
    hint.textContent = `✓ Will extract ${indices.length} page(s): ${indices.map(i => i + 1).slice(0, 10).join(', ')}${indices.length > 10 ? '...' : ''}`;
    hint.style.color = '#10b981';
    if (splitBtn) splitBtn.disabled = false;
  } catch (err) {
    hint.textContent = `⚠️ ${err.message}`;
    hint.style.color = '#ef4444';
    if (splitBtn) splitBtn.disabled = true;
  }
}

function parsePageRanges(rangeStr, maxPages) {
  const parts = rangeStr.split(',');
  const pageSet = new Set();

  for (let part of parts) {
    part = part.trim();
    if (!part) continue;

    if (part.includes('-')) {
      const [startStr, endStr] = part.split('-');
      const start = parseInt(startStr, 10);
      const end = parseInt(endStr, 10);

      if (isNaN(start) || isNaN(end) || start < 1 || end < start) {
        throw new Error(`Invalid page range: "${part}"`);
      }
      for (let p = start; p <= Math.min(end, maxPages); p++) {
        pageSet.add(p - 1); // 0-indexed
      }
    } else {
      const pageNum = parseInt(part, 10);
      if (isNaN(pageNum) || pageNum < 1 || pageNum > maxPages) {
        throw new Error(`Page ${pageNum} is out of bounds (document has ${maxPages} pages)`);
      }
      pageSet.add(pageNum - 1);
    }
  }

  const sorted = Array.from(pageSet).sort((a, b) => a - b);
  if (sorted.length === 0) {
    throw new Error('No valid pages selected.');
  }
  return sorted;
}

async function processPdfSplit() {
  const errEl = document.getElementById('pdf-split-error');
  const progEl = document.getElementById('pdf-split-progress');
  const resultCard = document.getElementById('pdf-split-result');
  const splitBtn = document.getElementById('pdf-split-btn');

  if (errEl) errEl.style.display = 'none';
  if (resultCard) resultCard.style.display = 'none';

  if (!pdfSplitLoadedFile) {
    if (errEl) {
      errEl.textContent = 'Please select a PDF file first.';
      errEl.style.display = 'block';
    }
    return;
  }

  const rangeVal = document.getElementById('pdf-split-range').value.trim();
  let targetIndices;
  try {
    targetIndices = parsePageRanges(rangeVal, pdfSplitTotalPagesCount);
  } catch (parseErr) {
    if (errEl) {
      errEl.textContent = parseErr.message;
      errEl.style.display = 'block';
    }
    return;
  }

  try {
    if (splitBtn) splitBtn.disabled = true;
    if (progEl) {
      progEl.textContent = `Extracting ${targetIndices.length} page(s) in browser...`;
      progEl.style.display = 'block';
    }

    const arrayBuffer = await pdfSplitLoadedFile.arrayBuffer();
    const sourcePdf = await PDFLib.PDFDocument.load(arrayBuffer, { ignoreEncryption: true });
    const splitPdf = await PDFLib.PDFDocument.create();

    const copiedPages = await splitPdf.copyPages(sourcePdf, targetIndices);
    copiedPages.forEach(p => splitPdf.addPage(p));

    const splitBytes = await splitPdf.save();
    pdfSplitResultBlob = new Blob([splitBytes], { type: 'application/pdf' });

    if (progEl) progEl.style.display = 'none';

    document.getElementById('pdf-split-result-pages').textContent = targetIndices.length;
    document.getElementById('pdf-split-result-range').textContent = rangeVal;
    document.getElementById('pdf-split-result-size').textContent = formatBytes(pdfSplitResultBlob.size);

    if (resultCard) {
      resultCard.style.display = 'block';
      resultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
    showToast('✓ Pages extracted successfully!');
  } catch (err) {
    console.error('PDF Split Error:', err);
    if (progEl) progEl.style.display = 'none';
    if (errEl) {
      errEl.textContent = 'Failed to extract pages: ' + err.message;
      errEl.style.display = 'block';
    }
  } finally {
    if (splitBtn) splitBtn.disabled = false;
  }
}

function downloadSplitPdf() {
  if (!pdfSplitResultBlob) return;
  const base = pdfSplitLoadedFile ? pdfSplitLoadedFile.name.replace(/\.pdf$/i, '') : 'document';
  downloadBlob(pdfSplitResultBlob, `${base}-extracted-${Date.now()}.pdf`);
}

function resetPdfSplit() {
  pdfSplitLoadedFile = null;
  pdfSplitTotalPagesCount = 0;
  pdfSplitResultBlob = null;

  const input = document.getElementById('pdf-split-input');
  if (input) input.value = '';
  const summaryEl = document.getElementById('pdf-split-summary');
  if (summaryEl) summaryEl.style.display = 'none';
  const controls = document.getElementById('pdf-split-controls');
  if (controls) controls.style.display = 'none';
  const actions = document.getElementById('pdf-split-action-row');
  if (actions) actions.style.display = 'none';
  const resultCard = document.getElementById('pdf-split-result');
  if (resultCard) resultCard.style.display = 'none';
  const errEl = document.getElementById('pdf-split-error');
  if (errEl) errEl.style.display = 'none';
  const progEl = document.getElementById('pdf-split-progress');
  if (progEl) progEl.style.display = 'none';
}

// ==================== 3. PDF TO IMAGES ====================
let pdf2ImgFile = null;
let pdf2ImgRenderedBlobs = [];
let pdf2ImgDoc = null;

async function handlePdfToImagesFile(file) {
  const errEl = document.getElementById('pdf2img-error');
  const summaryEl = document.getElementById('pdf2img-summary');
  const controlsEl = document.getElementById('pdf2img-controls');
  const actionRow = document.getElementById('pdf2img-action-row');
  const resultsCard = document.getElementById('pdf2img-results');

  if (errEl) errEl.style.display = 'none';
  if (resultsCard) resultsCard.style.display = 'none';
  if (!file) return;

  if (file.type !== 'application/pdf' && !file.name.toLowerCase().endsWith('.pdf')) {
    if (errEl) {
      errEl.textContent = 'Please choose a valid PDF file.';
      errEl.style.display = 'block';
    }
    return;
  }

  if (typeof pdfjsLib === 'undefined') {
    if (errEl) {
      errEl.textContent = 'PDF renderer is initializing. Please wait a moment and re-select.';
      errEl.style.display = 'block';
    }
    return;
  }

  try {
    if (typeof pdfjsLib.GlobalWorkerOptions !== 'undefined') {
      pdfjsLib.GlobalWorkerOptions.workerSrc = 'assets/lib/pdf.worker.min.js';
    }

    const arrayBuffer = await file.arrayBuffer();
    const loadingTask = pdfjsLib.getDocument({ data: arrayBuffer });
    const pdfDoc = await loadingTask.promise;

    pdf2ImgFile = file;
    pdf2ImgDoc = pdfDoc;

    document.getElementById('pdf2img-filename').textContent = file.name;
    document.getElementById('pdf2img-total-pages').textContent = pdfDoc.numPages;
    document.getElementById('pdf2img-filesize').textContent = formatBytes(file.size);

    if (summaryEl) summaryEl.style.display = 'flex';
    if (controlsEl) controlsEl.style.display = 'block';
    if (actionRow) actionRow.style.display = 'flex';
  } catch (err) {
    console.error('PDF to Images Read Error:', err);
    if (errEl) {
      errEl.textContent = 'Could not read PDF. File may be encrypted or corrupted.';
      errEl.style.display = 'block';
    }
  }
}

async function processPdfToImages() {
  const errEl = document.getElementById('pdf2img-error');
  const progEl = document.getElementById('pdf2img-progress');
  const resultsCard = document.getElementById('pdf2img-results');
  const galleryEl = document.getElementById('pdf2img-gallery');
  const convertBtn = document.getElementById('pdf2img-btn');

  if (errEl) errEl.style.display = 'none';
  if (resultsCard) resultsCard.style.display = 'none';
  if (galleryEl) galleryEl.innerHTML = '';
  pdf2ImgRenderedBlobs = [];

  if (!pdf2ImgFile || !pdf2ImgDoc) {
    if (errEl) {
      errEl.textContent = 'Please select a PDF file first.';
      errEl.style.display = 'block';
    }
    return;
  }

  const format = document.getElementById('pdf2img-format').value;
  const scale = parseFloat(document.getElementById('pdf2img-quality').value) || 1.5;
  const ext = format === 'image/png' ? 'png' : 'jpg';

  try {
    if (convertBtn) convertBtn.disabled = true;
    if (progEl) {
      progEl.textContent = 'Starting page rendering...';
      progEl.style.display = 'block';
    }

    const numPages = pdf2ImgDoc.numPages;

    for (let pageNum = 1; pageNum <= numPages; pageNum++) {
      if (progEl) progEl.textContent = `Rendering page ${pageNum} of ${numPages}...`;

      const page = await pdf2ImgDoc.getPage(pageNum);
      const viewport = page.getViewport({ scale });
      const canvas = document.createElement('canvas');
      canvas.width = viewport.width;
      canvas.height = viewport.height;
      const ctx = canvas.getContext('2d');

      if (format === 'image/jpeg') {
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
      }

      await page.render({ canvasContext: ctx, viewport }).promise;

      await new Promise(resolve => {
        canvas.toBlob(blob => {
          const blobUrl = URL.createObjectURL(blob);
          const fileName = `page-${pageNum}.${ext}`;
          const itemIdx = pdf2ImgRenderedBlobs.length;
          pdf2ImgRenderedBlobs.push({ blob, url: blobUrl, filename: fileName, pageNum });

          const card = document.createElement('div');
          card.className = 'image-thumb-card';
          card.innerHTML = `
            <div class="thumb-header">Page ${pageNum} (${Math.round(viewport.width)}×${Math.round(viewport.height)} px)</div>
            <div class="thumb-preview-wrap">
              <img src="${blobUrl}" class="thumb-preview" alt="Page ${pageNum}">
            </div>
            <div class="thumb-actions">
              <button type="button" onclick="downloadPdfPageImage(${itemIdx})" class="btn btn-outline btn-sm btn-block">⬇ Download Page ${pageNum}</button>
            </div>
          `;
          galleryEl.appendChild(card);
          resolve();
        }, format, 0.92);
      });
    }

    if (progEl) progEl.style.display = 'none';
    document.getElementById('pdf2img-rendered-count').textContent = numPages;

    if (resultsCard) {
      resultsCard.style.display = 'block';
      resultsCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
    showToast(`✓ Converted ${numPages} pages to images!`);
  } catch (err) {
    console.error('PDF to Images Error:', err);
    if (progEl) progEl.style.display = 'none';
    if (errEl) {
      errEl.textContent = 'Error rendering pages: ' + err.message;
      errEl.style.display = 'block';
    }
  } finally {
    if (convertBtn) convertBtn.disabled = false;
  }
}

function downloadPdfPageImage(index) {
  const item = pdf2ImgRenderedBlobs[index];
  if (!item) return;
  downloadBlob(item.blob, item.filename);
}

function downloadAllPdfImages() {
  if (!pdf2ImgRenderedBlobs.length) return;
  pdf2ImgRenderedBlobs.forEach((item, idx) => {
    setTimeout(() => {
      downloadBlob(item.blob, item.filename);
    }, idx * 250);
  });
  showToast(`Downloading ${pdf2ImgRenderedBlobs.length} images...`);
}

function resetPdfToImages() {
  pdf2ImgFile = null;
  pdf2ImgDoc = null;
  pdf2ImgRenderedBlobs = [];

  const input = document.getElementById('pdf2img-input');
  if (input) input.value = '';
  const summaryEl = document.getElementById('pdf2img-summary');
  if (summaryEl) summaryEl.style.display = 'none';
  const controls = document.getElementById('pdf2img-controls');
  if (controls) controls.style.display = 'none';
  const actions = document.getElementById('pdf2img-action-row');
  if (actions) actions.style.display = 'none';
  const results = document.getElementById('pdf2img-results');
  if (results) results.style.display = 'none';
  const errEl = document.getElementById('pdf2img-error');
  if (errEl) errEl.style.display = 'none';
  const progEl = document.getElementById('pdf2img-progress');
  if (progEl) progEl.style.display = 'none';
}

// ==================== 4. IMAGES TO PDF ====================
let img2PdfItems = [];
let img2PdfResultBlob = null;

function handleImagesToPdfFiles(files) {
  const errEl = document.getElementById('img2pdf-error');
  if (errEl) errEl.style.display = 'none';

  if (!files || files.length === 0) return;

  for (let i = 0; i < files.length; i++) {
    const f = files[i];
    if (f.type.startsWith('image/')) {
      const url = URL.createObjectURL(f);
      img2PdfItems.push({ file: f, url, name: f.name, size: f.size });
    }
  }

  if (img2PdfItems.length === 0) {
    if (errEl) {
      errEl.textContent = 'Please choose valid image files (JPG, PNG, WebP).';
      errEl.style.display = 'block';
    }
    return;
  }

  renderImagesToPdfThumbnails();
}

function renderImagesToPdfThumbnails() {
  const controls = document.getElementById('img2pdf-controls');
  const countEl = document.getElementById('img2pdf-count');
  const listEl = document.getElementById('img2pdf-thumbnails');
  const actionRow = document.getElementById('img2pdf-action-row');
  const btn = document.getElementById('img2pdf-btn');

  if (!controls || !listEl) return;

  if (img2PdfItems.length === 0) {
    controls.style.display = 'none';
    if (actionRow) actionRow.style.display = 'none';
    if (btn) btn.disabled = true;
    return;
  }

  controls.style.display = 'block';
  if (actionRow) actionRow.style.display = 'flex';
  if (countEl) countEl.textContent = img2PdfItems.length;
  if (btn) btn.disabled = false;

  listEl.innerHTML = img2PdfItems.map((item, idx) => `
    <div class="file-item-row" data-index="${idx}">
      <span class="file-item-idx">#${idx + 1}</span>
      <img src="${item.url}" class="file-item-thumb" alt="${item.name}">
      <div class="file-item-details">
        <span class="file-item-name">${item.name}</span>
        <span class="file-item-size">${formatBytes(item.size)}</span>
      </div>
      <div class="file-item-actions">
        <button type="button" class="btn-icon-order" onclick="moveImg2PdfItem(${idx}, -1)" ${idx === 0 ? 'disabled' : ''} title="Move Up">⬆</button>
        <button type="button" class="btn-icon-order" onclick="moveImg2PdfItem(${idx}, 1)" ${idx === img2PdfItems.length - 1 ? 'disabled' : ''} title="Move Down">⬇</button>
        <button type="button" class="btn-icon-delete" onclick="removeImg2PdfItem(${idx})" title="Remove">✕</button>
      </div>
    </div>
  `).join('');
}

function moveImg2PdfItem(idx, dir) {
  const newIdx = idx + dir;
  if (newIdx < 0 || newIdx >= img2PdfItems.length) return;
  const temp = img2PdfItems[idx];
  img2PdfItems[idx] = img2PdfItems[newIdx];
  img2PdfItems[newIdx] = temp;
  renderImagesToPdfThumbnails();
}

function removeImg2PdfItem(idx) {
  img2PdfItems.splice(idx, 1);
  renderImagesToPdfThumbnails();
}

async function processImagesToPdf() {
  const errEl = document.getElementById('img2pdf-error');
  const progEl = document.getElementById('img2pdf-progress');
  const resultCard = document.getElementById('img2pdf-result');
  const btn = document.getElementById('img2pdf-btn');

  if (errEl) errEl.style.display = 'none';
  if (resultCard) resultCard.style.display = 'none';

  if (img2PdfItems.length === 0) {
    if (errEl) {
      errEl.textContent = 'Please add at least one image.';
      errEl.style.display = 'block';
    }
    return;
  }

  if (typeof PDFLib === 'undefined') {
    if (errEl) {
      errEl.textContent = 'PDF engine is loading. Please retry in a moment.';
      errEl.style.display = 'block';
    }
    return;
  }

  const layout = document.getElementById('img2pdf-page-size').value;
  const margin = parseFloat(document.getElementById('img2pdf-margins').value) || 0;

  try {
    if (btn) btn.disabled = true;
    if (progEl) {
      progEl.textContent = 'Generating PDF from images in browser...';
      progEl.style.display = 'block';
    }

    const pdfDoc = await PDFLib.PDFDocument.create();

    for (let i = 0; i < img2PdfItems.length; i++) {
      const item = img2PdfItems[i];
      if (progEl) progEl.textContent = `Processing image ${i + 1} of ${img2PdfItems.length}...`;

      const img = new Image();
      await new Promise((resolve, reject) => {
        img.onload = resolve;
        img.onerror = reject;
        img.src = item.url;
      });

      const canvas = document.createElement('canvas');
      canvas.width = img.naturalWidth;
      canvas.height = img.naturalHeight;
      const ctx = canvas.getContext('2d');
      ctx.drawImage(img, 0, 0);

      const pngBlob = await new Promise(res => canvas.toBlob(res, 'image/png'));
      const pngBytes = await pngBlob.arrayBuffer();
      const embeddedImg = await pdfDoc.embedPng(pngBytes);

      let pageWidth, pageHeight;
      if (layout === 'a4-portrait') {
        pageWidth = 595.28;
        pageHeight = 841.89;
      } else if (layout === 'a4-landscape') {
        pageWidth = 841.89;
        pageHeight = 595.28;
      } else {
        pageWidth = img.naturalWidth + margin * 2;
        pageHeight = img.naturalHeight + margin * 2;
      }

      const availW = Math.max(10, pageWidth - margin * 2);
      const availH = Math.max(10, pageHeight - margin * 2);
      const scale = Math.min(availW / img.naturalWidth, availH / img.naturalHeight, 1);

      const imgDrawWidth = img.naturalWidth * scale;
      const imgDrawHeight = img.naturalHeight * scale;
      const drawX = margin + (availW - imgDrawWidth) / 2;
      const drawY = margin + (availH - imgDrawHeight) / 2;

      const page = pdfDoc.addPage([pageWidth, pageHeight]);
      page.drawImage(embeddedImg, {
        x: drawX,
        y: drawY,
        width: imgDrawWidth,
        height: imgDrawHeight
      });
    }

    const pdfBytes = await pdfDoc.save();
    img2PdfResultBlob = new Blob([pdfBytes], { type: 'application/pdf' });

    if (progEl) progEl.style.display = 'none';

    document.getElementById('img2pdf-result-pages').textContent = img2PdfItems.length;
    document.getElementById('img2pdf-result-count').textContent = img2PdfItems.length;
    document.getElementById('img2pdf-result-size').textContent = formatBytes(img2PdfResultBlob.size);

    if (resultCard) {
      resultCard.style.display = 'block';
      resultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
    showToast('✓ PDF generated successfully!');
  } catch (err) {
    console.error('Images to PDF Error:', err);
    if (progEl) progEl.style.display = 'none';
    if (errEl) {
      errEl.textContent = 'Could not create PDF: ' + err.message;
      errEl.style.display = 'block';
    }
  } finally {
    if (btn) btn.disabled = false;
  }
}

function downloadImagesPdf() {
  if (!img2PdfResultBlob) return;
  downloadBlob(img2PdfResultBlob, `images-document-${Date.now()}.pdf`);
}

function resetImagesToPdf() {
  img2PdfItems = [];
  img2PdfResultBlob = null;
  renderImagesToPdfThumbnails();

  const input = document.getElementById('img2pdf-input');
  if (input) input.value = '';
  const resultCard = document.getElementById('img2pdf-result');
  if (resultCard) resultCard.style.display = 'none';
  const errEl = document.getElementById('img2pdf-error');
  if (errEl) errEl.style.display = 'none';
  const progEl = document.getElementById('img2pdf-progress');
  if (progEl) progEl.style.display = 'none';
}

// ==================== 5. IMAGE COMPRESSOR ====================
let imgCompLoadedImage = null;
let imgCompOriginalFile = null;
let imgCompResultBlob = null;

function handleImageCompressorFile(file) {
  const errEl = document.getElementById('imgcomp-error');
  const cardEl = document.getElementById('imgcomp-selected-card');
  const controlsEl = document.getElementById('imgcomp-controls');
  const actionRow = document.getElementById('imgcomp-action-row');
  const resultCard = document.getElementById('imgcomp-result');

  if (errEl) errEl.style.display = 'none';
  if (resultCard) resultCard.style.display = 'none';
  if (!file) return;

  if (!file.type.startsWith('image/')) {
    if (errEl) {
      errEl.textContent = 'Please choose a valid image file (JPG, PNG, WebP).';
      errEl.style.display = 'block';
    }
    return;
  }

  imgCompOriginalFile = file;

  const reader = new FileReader();
  reader.onload = e => {
    const img = new Image();
    img.onload = () => {
      imgCompLoadedImage = img;

      const thumb = document.getElementById('imgcomp-selected-thumb');
      if (thumb) thumb.src = e.target.result;

      document.getElementById('imgcomp-filename').textContent = file.name;
      document.getElementById('imgcomp-orig-size').textContent = formatBytes(file.size);
      document.getElementById('imgcomp-orig-dims').textContent = `${img.naturalWidth} × ${img.naturalHeight} px`;

      if (cardEl) cardEl.style.display = 'flex';
      if (controlsEl) controlsEl.style.display = 'block';
      if (actionRow) actionRow.style.display = 'flex';
    };
    img.src = e.target.result;
  };
  reader.readAsDataURL(file);
}

function updateCompressorQuality(val) {
  const badge = document.getElementById('imgcomp-quality-val');
  if (badge) badge.textContent = val + '%';
}

function runImageCompression() {
  const errEl = document.getElementById('imgcomp-error');
  const progEl = document.getElementById('imgcomp-progress');
  const resultCard = document.getElementById('imgcomp-result');

  if (errEl) errEl.style.display = 'none';

  if (!imgCompLoadedImage || !imgCompOriginalFile) {
    if (errEl) {
      errEl.textContent = 'Please choose an image file first.';
      errEl.style.display = 'block';
    }
    return;
  }

  const quality = parseInt(document.getElementById('imgcomp-quality').value, 10) / 100;
  const maxWOpt = document.getElementById('imgcomp-max-width').value;
  const formatOpt = document.getElementById('imgcomp-format').value;

  let targetFormat = formatOpt === 'auto' ? (imgCompOriginalFile.type || 'image/jpeg') : formatOpt;
  if (targetFormat !== 'image/jpeg' && targetFormat !== 'image/webp') {
    targetFormat = 'image/jpeg';
  }

  let w = imgCompLoadedImage.naturalWidth;
  let h = imgCompLoadedImage.naturalHeight;

  if (maxWOpt !== 'original') {
    const maxW = parseInt(maxWOpt, 10);
    if (w > maxW) {
      h = Math.round(h * (maxW / w));
      w = maxW;
    }
  }

  const canvas = document.createElement('canvas');
  canvas.width = w;
  canvas.height = h;
  const ctx = canvas.getContext('2d');

  if (targetFormat === 'image/jpeg') {
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, w, h);
  }

  ctx.drawImage(imgCompLoadedImage, 0, 0, w, h);

  canvas.toBlob(blob => {
    if (!blob) {
      if (errEl) {
        errEl.textContent = 'Compression failed. Please try a different quality level.';
        errEl.style.display = 'block';
      }
      return;
    }

    imgCompResultBlob = blob;

    const originalSize = imgCompOriginalFile.size;
    const newSize = blob.size;
    const savings = Math.max(0, Math.round(((originalSize - newSize) / originalSize) * 100));

    document.getElementById('imgcomp-res-orig').textContent = formatBytes(originalSize);
    document.getElementById('imgcomp-res-new').textContent = formatBytes(newSize);
    document.getElementById('imgcomp-res-saving').textContent = `-${savings}%`;

    const preview = document.getElementById('imgcomp-preview');
    if (preview) preview.src = URL.createObjectURL(blob);

    if (resultCard) {
      resultCard.style.display = 'block';
      resultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
    showToast('✓ Image compressed successfully!');
  }, targetFormat, quality);
}

function downloadCompressedImage() {
  if (!imgCompResultBlob || !imgCompOriginalFile) return;
  const formatOpt = document.getElementById('imgcomp-format').value;
  const ext = formatOpt === 'image/webp' ? 'webp' : 'jpg';
  const baseName = imgCompOriginalFile.name.replace(/\.[^/.]+$/, '');
  downloadBlob(imgCompResultBlob, `${baseName}-compressed.${ext}`);
}

function resetImageCompressor() {
  imgCompLoadedImage = null;
  imgCompOriginalFile = null;
  imgCompResultBlob = null;

  const input = document.getElementById('imgcomp-input');
  if (input) input.value = '';
  const card = document.getElementById('imgcomp-selected-card');
  if (card) card.style.display = 'none';
  const controls = document.getElementById('imgcomp-controls');
  if (controls) controls.style.display = 'none';
  const actions = document.getElementById('imgcomp-action-row');
  if (actions) actions.style.display = 'none';
  const resultCard = document.getElementById('imgcomp-result');
  if (resultCard) resultCard.style.display = 'none';
  const errEl = document.getElementById('imgcomp-error');
  if (errEl) errEl.style.display = 'none';
}

// ==================== 6. IMAGE RESIZER ====================
let imgResizeLoadedImage = null;
let imgResizeOriginalFile = null;
let imgResizeResultBlob = null;
let imgResizeAspectRatioLocked = true;
let imgResizeNaturalRatio = 1;

function handleImageResizerFile(file) {
  const errEl = document.getElementById('imgresize-error');
  const cardEl = document.getElementById('imgresize-selected-card');
  const controls = document.getElementById('imgresize-controls');
  const actions = document.getElementById('imgresize-action-row');
  const resultCard = document.getElementById('imgresize-result');

  if (errEl) errEl.style.display = 'none';
  if (resultCard) resultCard.style.display = 'none';
  if (!file) return;

  imgResizeOriginalFile = file;

  const reader = new FileReader();
  reader.onload = e => {
    const img = new Image();
    img.onload = () => {
      imgResizeLoadedImage = img;
      const w = img.naturalWidth;
      const h = img.naturalHeight;
      imgResizeNaturalRatio = w / h;

      const thumb = document.getElementById('imgresize-selected-thumb');
      if (thumb) thumb.src = e.target.result;

      document.getElementById('imgresize-filename').textContent = file.name;
      document.getElementById('imgresize-orig-dims').textContent = `${w} × ${h} px`;
      document.getElementById('imgresize-orig-ratio').textContent = `${imgResizeNaturalRatio.toFixed(2)}:1`;
      document.getElementById('imgresize-orig-size').textContent = formatBytes(file.size);

      document.getElementById('imgresize-width').value = w;
      document.getElementById('imgresize-height').value = h;

      if (cardEl) cardEl.style.display = 'flex';
      if (controls) controls.style.display = 'block';
      if (actions) actions.style.display = 'flex';
    };
    img.src = e.target.result;
  };
  reader.readAsDataURL(file);
}

function toggleResizerLock(locked) {
  imgResizeAspectRatioLocked = locked;
}

function onResizerWidthChange(wVal) {
  const w = parseInt(wVal, 10);
  if (!w || w <= 0) return;
  if (imgResizeAspectRatioLocked && imgResizeNaturalRatio) {
    document.getElementById('imgresize-height').value = Math.round(w / imgResizeNaturalRatio);
  }
}

function onResizerHeightChange(hVal) {
  const h = parseInt(hVal, 10);
  if (!h || h <= 0) return;
  if (imgResizeAspectRatioLocked && imgResizeNaturalRatio) {
    document.getElementById('imgresize-width').value = Math.round(h * imgResizeNaturalRatio);
  }
}

function applyResizerPreset(scale) {
  if (!imgResizeLoadedImage) return;
  const w = Math.round(imgResizeLoadedImage.naturalWidth * scale);
  const h = Math.round(imgResizeLoadedImage.naturalHeight * scale);
  document.getElementById('imgresize-width').value = w;
  document.getElementById('imgresize-height').value = h;
}

function applyResizerExact(w, h) {
  document.getElementById('imgresize-width').value = w;
  document.getElementById('imgresize-height').value = h;
}

function runImageResize() {
  const errEl = document.getElementById('imgresize-error');
  const resultCard = document.getElementById('imgresize-result');
  if (errEl) errEl.style.display = 'none';

  if (!imgResizeLoadedImage || !imgResizeOriginalFile) {
    if (errEl) {
      errEl.textContent = 'Please choose an image file first.';
      errEl.style.display = 'block';
    }
    return;
  }

  const w = parseInt(document.getElementById('imgresize-width').value, 10);
  const h = parseInt(document.getElementById('imgresize-height').value, 10);

  if (!w || !h || w <= 0 || h <= 0) {
    if (errEl) {
      errEl.textContent = 'Please enter valid positive width and height dimensions.';
      errEl.style.display = 'block';
    }
    return;
  }

  const canvas = document.createElement('canvas');
  canvas.width = w;
  canvas.height = h;
  const ctx = canvas.getContext('2d');
  ctx.imageSmoothingEnabled = true;
  ctx.imageSmoothingQuality = 'high';

  const isPng = imgResizeOriginalFile.type === 'image/png';
  if (!isPng) {
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, w, h);
  }

  ctx.drawImage(imgResizeLoadedImage, 0, 0, w, h);
  const format = isPng ? 'image/png' : 'image/jpeg';

  canvas.toBlob(blob => {
    if (!blob) return;
    imgResizeResultBlob = blob;

    document.getElementById('imgresize-res-dims').textContent = `${w} × ${h} px`;
    document.getElementById('imgresize-res-size').textContent = formatBytes(blob.size);
    document.getElementById('imgresize-res-format').textContent = isPng ? 'PNG' : 'JPG';

    const preview = document.getElementById('imgresize-preview');
    if (preview) preview.src = URL.createObjectURL(blob);

    if (resultCard) {
      resultCard.style.display = 'block';
      resultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
    showToast('✓ Image resized successfully!');
  }, format, 0.9);
}

function downloadResizedImage() {
  if (!imgResizeResultBlob || !imgResizeOriginalFile) return;
  const isPng = imgResizeOriginalFile.type === 'image/png';
  const ext = isPng ? 'png' : 'jpg';
  const baseName = imgResizeOriginalFile.name.replace(/\.[^/.]+$/, '');
  const w = document.getElementById('imgresize-width').value;
  const h = document.getElementById('imgresize-height').value;
  downloadBlob(imgResizeResultBlob, `${baseName}-${w}x${h}.${ext}`);
}

function resetImageResizer() {
  imgResizeLoadedImage = null;
  imgResizeOriginalFile = null;
  imgResizeResultBlob = null;

  const input = document.getElementById('imgresize-input');
  if (input) input.value = '';
  const card = document.getElementById('imgresize-selected-card');
  if (card) card.style.display = 'none';
  const controls = document.getElementById('imgresize-controls');
  if (controls) controls.style.display = 'none';
  const actions = document.getElementById('imgresize-action-row');
  if (actions) actions.style.display = 'none';
  const resultCard = document.getElementById('imgresize-result');
  if (resultCard) resultCard.style.display = 'none';
  const errEl = document.getElementById('imgresize-error');
  if (errEl) errEl.style.display = 'none';
}

// ==================== 7. JPG TO PNG CONVERTER ====================
let jpg2PngLoadedImage = null;
let jpg2PngOriginalFile = null;
let jpg2PngResultBlob = null;

function handleJpgToPngFile(file) {
  const errEl = document.getElementById('jpg2png-error');
  const cardEl = document.getElementById('jpg2png-selected-card');
  const controls = document.getElementById('jpg2png-controls');
  const actions = document.getElementById('jpg2png-action-row');
  const resultCard = document.getElementById('jpg2png-result');

  if (errEl) errEl.style.display = 'none';
  if (resultCard) resultCard.style.display = 'none';
  if (!file) return;

  jpg2PngOriginalFile = file;

  const reader = new FileReader();
  reader.onload = e => {
    const img = new Image();
    img.onload = () => {
      jpg2PngLoadedImage = img;

      const thumb = document.getElementById('jpg2png-selected-thumb');
      if (thumb) thumb.src = e.target.result;

      document.getElementById('jpg2png-filename').textContent = file.name;
      document.getElementById('jpg2png-orig-size').textContent = formatBytes(file.size);
      document.getElementById('jpg2png-orig-dims').textContent = `${img.naturalWidth} × ${img.naturalHeight} px`;

      if (cardEl) cardEl.style.display = 'flex';
      if (controls) controls.style.display = 'block';
      if (actions) actions.style.display = 'flex';
    };
    img.src = e.target.result;
  };
  reader.readAsDataURL(file);
}

function runJpgToPng() {
  const errEl = document.getElementById('jpg2png-error');
  const resultCard = document.getElementById('jpg2png-result');
  if (errEl) errEl.style.display = 'none';

  if (!jpg2PngLoadedImage || !jpg2PngOriginalFile) {
    if (errEl) {
      errEl.textContent = 'Please choose a JPG/JPEG image first.';
      errEl.style.display = 'block';
    }
    return;
  }

  const canvas = document.createElement('canvas');
  canvas.width = jpg2PngLoadedImage.naturalWidth;
  canvas.height = jpg2PngLoadedImage.naturalHeight;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(jpg2PngLoadedImage, 0, 0);

  canvas.toBlob(blob => {
    if (!blob) return;
    jpg2PngResultBlob = blob;

    document.getElementById('jpg2png-res-size').textContent = formatBytes(blob.size);

    const preview = document.getElementById('jpg2png-preview');
    if (preview) preview.src = URL.createObjectURL(blob);

    if (resultCard) {
      resultCard.style.display = 'block';
      resultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
    showToast('✓ Converted to PNG!');
  }, 'image/png');
}

function downloadJpgToPng() {
  if (!jpg2PngResultBlob || !jpg2PngOriginalFile) return;
  const baseName = jpg2PngOriginalFile.name.replace(/\.[^/.]+$/, '');
  downloadBlob(jpg2PngResultBlob, `${baseName}.png`);
}

function resetJpgToPng() {
  jpg2PngLoadedImage = null;
  jpg2PngOriginalFile = null;
  jpg2PngResultBlob = null;

  const input = document.getElementById('jpg2png-input');
  if (input) input.value = '';
  const card = document.getElementById('jpg2png-selected-card');
  if (card) card.style.display = 'none';
  const controls = document.getElementById('jpg2png-controls');
  if (controls) controls.style.display = 'none';
  const actions = document.getElementById('jpg2png-action-row');
  if (actions) actions.style.display = 'none';
  const resultCard = document.getElementById('jpg2png-result');
  if (resultCard) resultCard.style.display = 'none';
  const errEl = document.getElementById('jpg2png-error');
  if (errEl) errEl.style.display = 'none';
}

// ==================== 8. PNG TO JPG CONVERTER ====================
let png2JpgLoadedImage = null;
let png2JpgOriginalFile = null;
let png2JpgResultBlob = null;
let png2JpgBgColor = '#ffffff';

function handlePngToJpgFile(file) {
  const errEl = document.getElementById('png2jpg-error');
  const cardEl = document.getElementById('png2jpg-selected-card');
  const controls = document.getElementById('png2jpg-controls');
  const actions = document.getElementById('png2jpg-action-row');
  const resultCard = document.getElementById('png2jpg-result');

  if (errEl) errEl.style.display = 'none';
  if (resultCard) resultCard.style.display = 'none';
  if (!file) return;

  png2JpgOriginalFile = file;

  const reader = new FileReader();
  reader.onload = e => {
    const img = new Image();
    img.onload = () => {
      png2JpgLoadedImage = img;

      const thumb = document.getElementById('png2jpg-selected-thumb');
      if (thumb) thumb.src = e.target.result;

      document.getElementById('png2jpg-filename').textContent = file.name;
      document.getElementById('png2jpg-orig-size').textContent = formatBytes(file.size);
      document.getElementById('png2jpg-orig-dims').textContent = `${img.naturalWidth} × ${img.naturalHeight} px`;

      if (cardEl) cardEl.style.display = 'flex';
      if (controls) controls.style.display = 'block';
      if (actions) actions.style.display = 'flex';
    };
    img.src = e.target.result;
  };
  reader.readAsDataURL(file);
}

function updatePng2JpgBg(hex) {
  png2JpgBgColor = hex;
  const hexBadge = document.getElementById('png2jpg-bg-hex');
  if (hexBadge) hexBadge.textContent = hex.toUpperCase();
}

function updatePng2JpgQuality(val) {
  const qBadge = document.getElementById('png2jpg-quality-val');
  if (qBadge) qBadge.textContent = val + '%';
}

function runPngToJpg() {
  const errEl = document.getElementById('png2jpg-error');
  const resultCard = document.getElementById('png2jpg-result');
  if (errEl) errEl.style.display = 'none';

  if (!png2JpgLoadedImage || !png2JpgOriginalFile) {
    if (errEl) {
      errEl.textContent = 'Please choose a PNG image first.';
      errEl.style.display = 'block';
    }
    return;
  }

  const quality = parseInt(document.getElementById('png2jpg-quality').value, 10) / 100;

  const canvas = document.createElement('canvas');
  canvas.width = png2JpgLoadedImage.naturalWidth;
  canvas.height = png2JpgLoadedImage.naturalHeight;
  const ctx = canvas.getContext('2d');

  // Fill custom background color for transparency
  ctx.fillStyle = png2JpgBgColor || '#ffffff';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.drawImage(png2JpgLoadedImage, 0, 0);

  canvas.toBlob(blob => {
    if (!blob) return;
    png2JpgResultBlob = blob;

    const originalSize = png2JpgOriginalFile.size;
    const newSize = blob.size;
    const reduction = Math.max(0, Math.round(((originalSize - newSize) / originalSize) * 100));

    document.getElementById('png2jpg-res-orig').textContent = formatBytes(originalSize);
    document.getElementById('png2jpg-res-new').textContent = formatBytes(newSize);
    document.getElementById('png2jpg-res-reduction').textContent = `-${reduction}%`;

    const preview = document.getElementById('png2jpg-preview');
    if (preview) preview.src = URL.createObjectURL(blob);

    if (resultCard) {
      resultCard.style.display = 'block';
      resultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
    showToast('✓ Converted to JPG!');
  }, 'image/jpeg', quality);
}

function downloadPngToJpg() {
  if (!png2JpgResultBlob || !png2JpgOriginalFile) return;
  const baseName = png2JpgOriginalFile.name.replace(/\.[^/.]+$/, '');
  downloadBlob(png2JpgResultBlob, `${baseName}.jpg`);
}

function resetPngToJpg() {
  png2JpgLoadedImage = null;
  png2JpgOriginalFile = null;
  png2JpgResultBlob = null;
  png2JpgBgColor = '#ffffff';

  const input = document.getElementById('png2jpg-input');
  if (input) input.value = '';
  const card = document.getElementById('png2jpg-selected-card');
  if (card) card.style.display = 'none';
  const controls = document.getElementById('png2jpg-controls');
  if (controls) controls.style.display = 'none';
  const actions = document.getElementById('png2jpg-action-row');
  if (actions) actions.style.display = 'none';
  const resultCard = document.getElementById('png2jpg-result');
  if (resultCard) resultCard.style.display = 'none';
  const errEl = document.getElementById('png2jpg-error');
  if (errEl) errEl.style.display = 'none';
}

// ==================== 9. IMAGE CROPPER ====================
let imgCropLoadedImage = null;
let imgCropOriginalFile = null;
let imgCropResultBlob = null;
let imgCropCurrentRatio = 'free';

function handleImageCropperFile(file) {
  const errEl = document.getElementById('imgcrop-error');
  const cardEl = document.getElementById('imgcrop-selected-card');
  const controls = document.getElementById('imgcrop-controls');
  const actions = document.getElementById('imgcrop-action-row');
  const resultCard = document.getElementById('imgcrop-result');

  if (errEl) errEl.style.display = 'none';
  if (resultCard) resultCard.style.display = 'none';
  if (!file) return;

  imgCropOriginalFile = file;

  const reader = new FileReader();
  reader.onload = e => {
    const img = new Image();
    img.onload = () => {
      imgCropLoadedImage = img;

      const thumb = document.getElementById('imgcrop-selected-thumb');
      if (thumb) thumb.src = e.target.result;

      document.getElementById('imgcrop-filename').textContent = file.name;
      document.getElementById('imgcrop-orig-dims').textContent = `${img.naturalWidth} × ${img.naturalHeight} px`;
      document.getElementById('imgcrop-orig-size').textContent = formatBytes(file.size);

      if (cardEl) cardEl.style.display = 'flex';
      if (controls) controls.style.display = 'block';
      if (actions) actions.style.display = 'flex';

      setTimeout(drawCropCanvas, 50);
    };
    img.src = e.target.result;
  };
  reader.readAsDataURL(file);
}

function setCropRatio(ratio) {
  imgCropCurrentRatio = ratio;
  const ratioBtnMap = {
    "free": "crop-ratio-free",
    "1:1": "crop-ratio-1-1",
    "4:3": "crop-ratio-4-3",
    "16:9": "crop-ratio-16-9",
    "1-1": "crop-ratio-1-1",
    "4-3": "crop-ratio-4-3",
    "16-9": "crop-ratio-16-9"
  };
  const activeBtnId = ratioBtnMap[ratio] || "crop-ratio-free";
  ["crop-ratio-free", "crop-ratio-1-1", "crop-ratio-4-3", "crop-ratio-16-9"].forEach(btnId => {
    const btn = document.getElementById(btnId);
    if (btn) {
      if (btnId === activeBtnId) btn.classList.add("active");
      else btn.classList.remove("active");
    }
  });
  drawCropCanvas();
}

function onCropParamChange() {
  const sizeVal = document.getElementById('crop-size').value;
  const xVal = document.getElementById('crop-pos-x').value;
  const yVal = document.getElementById('crop-pos-y').value;

  const sizeBadge = document.getElementById('crop-size-val');
  if (sizeBadge) sizeBadge.textContent = sizeVal + '%';

  const xBadge = document.getElementById('crop-pos-x-val');
  if (xBadge) xBadge.textContent = xVal + '%';

  const yBadge = document.getElementById('crop-pos-y-val');
  if (yBadge) yBadge.textContent = yVal + '%';

  drawCropCanvas();
}

function resetCropCenter() {
  document.getElementById('crop-size').value = 80;
  document.getElementById('crop-pos-x').value = 50;
  document.getElementById('crop-pos-y').value = 50;
  onCropParamChange();
}

function getCropBox() {
  if (!imgCropLoadedImage) return { x: 0, y: 0, w: 0, h: 0 };
  const imgW = imgCropLoadedImage.naturalWidth;
  const imgH = imgCropLoadedImage.naturalHeight;

  const posXVal = parseInt(document.getElementById('crop-pos-x').value, 10) / 100;
  const posYVal = parseInt(document.getElementById('crop-pos-y').value, 10) / 100;
  const sizeVal = parseInt(document.getElementById('crop-size').value, 10) / 100;

  let cropW, cropH;

  if (imgCropCurrentRatio === '1:1') {
    const minDim = Math.min(imgW, imgH) * sizeVal;
    cropW = minDim;
    cropH = minDim;
  } else if (imgCropCurrentRatio === '4:3') {
    const targetW = imgW * sizeVal;
    cropW = targetW;
    cropH = targetW * (3 / 4);
    if (cropH > imgH) {
      cropH = imgH * sizeVal;
      cropW = cropH * (4 / 3);
    }
  } else if (imgCropCurrentRatio === '16:9') {
    const targetW = imgW * sizeVal;
    cropW = targetW;
    cropH = targetW * (9 / 16);
    if (cropH > imgH) {
      cropH = imgH * sizeVal;
      cropW = cropH * (16 / 9);
    }
  } else {
    cropW = imgW * sizeVal;
    cropH = imgH * sizeVal;
  }

  const maxOffsetX = Math.max(0, imgW - cropW);
  const maxOffsetY = Math.max(0, imgH - cropH);

  const x = Math.max(0, Math.min(maxOffsetX, maxOffsetX * posXVal));
  const y = Math.max(0, Math.min(maxOffsetY, maxOffsetY * posYVal));

  return {
    x: Math.round(x),
    y: Math.round(y),
    w: Math.round(cropW),
    h: Math.round(cropH)
  };
}

function drawCropCanvas() {
  if (!imgCropLoadedImage) return;
  const canvas = document.getElementById('imgcrop-canvas');
  if (!canvas) return;

  const parentWidth = canvas.parentElement ? canvas.parentElement.clientWidth : 400;
  const wrapWidth = Math.max(280, Math.min(parentWidth || 400, 600));
  const displayScale = wrapWidth / imgCropLoadedImage.naturalWidth;

  canvas.width = wrapWidth;
  canvas.height = imgCropLoadedImage.naturalHeight * displayScale;
  const ctx = canvas.getContext('2d');

  ctx.drawImage(imgCropLoadedImage, 0, 0, canvas.width, canvas.height);

  ctx.fillStyle = 'rgba(0, 0, 0, 0.6)';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  const box = getCropBox();
  const cX = box.x * displayScale;
  const cY = box.y * displayScale;
  const cW = box.w * displayScale;
  const cH = box.h * displayScale;

  ctx.clearRect(cX, cY, cW, cH);
  ctx.drawImage(imgCropLoadedImage, box.x, box.y, box.w, box.h, cX, cY, cW, cH);

  ctx.strokeStyle = '#2563eb';
  ctx.lineWidth = 2;
  ctx.strokeRect(cX, cY, cW, cH);

  ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(cX + cW / 3, cY); ctx.lineTo(cX + cW / 3, cY + cH);
  ctx.moveTo(cX + (2 * cW) / 3, cY); ctx.lineTo(cX + (2 * cW) / 3, cY + cH);
  ctx.moveTo(cX, cY + cH / 3); ctx.lineTo(cX + cW, cY + cH / 3);
  ctx.moveTo(cX, cY + (2 * cH) / 3); ctx.lineTo(cX + cW, cY + (2 * cH) / 3);
  ctx.stroke();
}

function runImageCrop() {
  const errEl = document.getElementById('imgcrop-error');
  const resultCard = document.getElementById('imgcrop-result');
  if (errEl) errEl.style.display = 'none';

  if (!imgCropLoadedImage || !imgCropOriginalFile) {
    if (errEl) {
      errEl.textContent = 'Please choose an image to crop.';
      errEl.style.display = 'block';
    }
    return;
  }

  const box = getCropBox();
  if (box.w <= 0 || box.h <= 0) return;

  const outCanvas = document.createElement('canvas');
  outCanvas.width = box.w;
  outCanvas.height = box.h;
  const outCtx = outCanvas.getContext('2d');
  outCtx.drawImage(imgCropLoadedImage, box.x, box.y, box.w, box.h, 0, 0, box.w, box.h);

  const format = imgCropOriginalFile.type === 'image/png' ? 'image/png' : 'image/jpeg';

  outCanvas.toBlob(blob => {
    if (!blob) return;
    imgCropResultBlob = blob;

    document.getElementById('imgcrop-res-dims').textContent = `${box.w} × ${box.h} px`;
    document.getElementById('imgcrop-res-ratio').textContent = imgCropCurrentRatio.toUpperCase();
    document.getElementById('imgcrop-res-size').textContent = formatBytes(blob.size);

    const preview = document.getElementById('imgcrop-preview');
    if (preview) preview.src = URL.createObjectURL(blob);

    if (resultCard) {
      resultCard.style.display = 'block';
      resultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
    showToast('✓ Image cropped successfully!');
  }, format, 0.92);
}

function downloadCroppedImage() {
  if (!imgCropResultBlob || !imgCropOriginalFile) return;
  const isPng = imgCropOriginalFile.type === 'image/png';
  const ext = isPng ? 'png' : 'jpg';
  const baseName = imgCropOriginalFile.name.replace(/\.[^/.]+$/, '');
  downloadBlob(imgCropResultBlob, `${baseName}-cropped.${ext}`);
}

function resetImageCropper() {
  imgCropLoadedImage = null;
  imgCropOriginalFile = null;
  imgCropResultBlob = null;

  const input = document.getElementById('imgcrop-input');
  if (input) input.value = '';
  const card = document.getElementById('imgcrop-selected-card');
  if (card) card.style.display = 'none';
  const controls = document.getElementById('imgcrop-controls');
  if (controls) controls.style.display = 'none';
  const actions = document.getElementById('imgcrop-action-row');
  if (actions) actions.style.display = 'none';
  const resultCard = document.getElementById('imgcrop-result');
  if (resultCard) resultCard.style.display = 'none';
  const errEl = document.getElementById('imgcrop-error');
  if (errEl) errEl.style.display = 'none';
}

// ==================== 10. IMAGE TO WEBP CONVERTER ====================
let img2WebpLoadedImage = null;
let img2WebpOriginalFile = null;
let img2WebpResultBlob = null;

function handleImageToWebpFile(file) {
  const errEl = document.getElementById('img2webp-error');
  const cardEl = document.getElementById('img2webp-selected-card');
  const controls = document.getElementById('img2webp-controls');
  const actions = document.getElementById('img2webp-action-row');
  const resultCard = document.getElementById('img2webp-result');

  if (errEl) errEl.style.display = 'none';
  if (resultCard) resultCard.style.display = 'none';
  if (!file) return;

  img2WebpOriginalFile = file;

  const reader = new FileReader();
  reader.onload = e => {
    const img = new Image();
    img.onload = () => {
      img2WebpLoadedImage = img;

      const thumb = document.getElementById('img2webp-selected-thumb');
      if (thumb) thumb.src = e.target.result;

      document.getElementById('img2webp-filename').textContent = file.name;
      document.getElementById('img2webp-orig-size').textContent = formatBytes(file.size);
      document.getElementById('img2webp-orig-dims').textContent = `${img.naturalWidth} × ${img.naturalHeight} px`;

      if (cardEl) cardEl.style.display = 'flex';
      if (controls) controls.style.display = 'block';
      if (actions) actions.style.display = 'flex';
    };
    img.src = e.target.result;
  };
  reader.readAsDataURL(file);
}

function updateWebpQuality(val) {
  const qVal = document.getElementById('img2webp-quality-val');
  if (qVal) qVal.textContent = val + '%';
}

function runImageToWebp() {
  const errEl = document.getElementById('img2webp-error');
  const resultCard = document.getElementById('img2webp-result');
  if (errEl) errEl.style.display = 'none';

  if (!img2WebpLoadedImage || !img2WebpOriginalFile) {
    if (errEl) {
      errEl.textContent = 'Please choose an image to convert.';
      errEl.style.display = 'block';
    }
    return;
  }

  const quality = parseInt(document.getElementById('img2webp-quality').value, 10) / 100;

  const canvas = document.createElement('canvas');
  canvas.width = img2WebpLoadedImage.naturalWidth;
  canvas.height = img2WebpLoadedImage.naturalHeight;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(img2WebpLoadedImage, 0, 0);

  canvas.toBlob(blob => {
    if (!blob) return;
    img2WebpResultBlob = blob;

    const originalSize = img2WebpOriginalFile.size;
    const newSize = blob.size;
    const savedPct = Math.max(0, Math.round(((originalSize - newSize) / originalSize) * 100));

    document.getElementById('img2webp-res-orig').textContent = formatBytes(originalSize);
    document.getElementById('img2webp-res-new').textContent = formatBytes(newSize);
    document.getElementById('img2webp-res-saved').textContent = `-${savedPct}%`;

    const preview = document.getElementById('img2webp-preview');
    if (preview) preview.src = URL.createObjectURL(blob);

    if (resultCard) {
      resultCard.style.display = 'block';
      resultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
    showToast('✓ Converted to WebP!');
  }, 'image/webp', quality);
}

function downloadWebpImage() {
  if (!img2WebpResultBlob || !img2WebpOriginalFile) return;
  const baseName = img2WebpOriginalFile.name.replace(/\.[^/.]+$/, '');
  downloadBlob(img2WebpResultBlob, `${baseName}.webp`);
}

function resetImageToWebp() {
  img2WebpLoadedImage = null;
  img2WebpOriginalFile = null;
  img2WebpResultBlob = null;

  const input = document.getElementById('img2webp-input');
  if (input) input.value = '';
  const card = document.getElementById('img2webp-selected-card');
  if (card) card.style.display = 'none';
  const controls = document.getElementById('img2webp-controls');
  if (controls) controls.style.display = 'none';
  const actions = document.getElementById('img2webp-action-row');
  if (actions) actions.style.display = 'none';
  const resultCard = document.getElementById('img2webp-result');
  if (resultCard) resultCard.style.display = 'none';
  const errEl = document.getElementById('img2webp-error');
  if (errEl) errEl.style.display = 'none';
}

// Auto-initialize dropzones when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initFileDropzones);
} else {
  initFileDropzones();
}
