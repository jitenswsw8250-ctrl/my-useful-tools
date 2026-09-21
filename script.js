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
  if (navigator.share) {
    navigator.share({
      title: 'MY USEFUL TOOLS - Free Online Calculators',
      text: 'Check out MY USEFUL TOOLS: 100% free, fast, and privacy-friendly online calculators.',
      url: window.location.href
    }).catch(() => {});
  } else if (navigator.clipboard) {
    navigator.clipboard.writeText(window.location.href).then(() => {
      alert('Website URL copied to clipboard!');
    }).catch(() => {
      prompt('Copy website link:', window.location.href);
    });
  } else {
    prompt('Copy website link:', window.location.href);
  }
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
}
