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
    description: 'Free, simple, and privacy-friendly online calculators: Age, EMI Loan, Percentage, Discount, and BMI. Fast, lightweight, and 100% browser-based.'
  },
  'all-tools': {
    title: 'All Free Tools & Calculators | MY USEFUL TOOLS',
    description: 'Explore all 5 free, instant browser calculators: Age, EMI, Percentage, Discount, and BMI calculators on MY USEFUL TOOLS.'
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
  const baseUrl = 'https://ais-pre-vatqw65fky76dekso6xcwb-447578213146.asia-southeast1.run.app/';
  const fullTargetUrl = effectiveScreen === 'home' ? baseUrl : `${baseUrl}#${effectiveScreen}`;
  if (canonicalLink) {
    canonicalLink.setAttribute('href', fullTargetUrl);
  }
  if (ogUrl) {
    ogUrl.setAttribute('content', fullTargetUrl);
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
    successBanner.innerHTML = `<strong>Thank you, ${escapeHtml(nameVal)}!</strong> Your message has been verified and validated locally.<br><span style="font-size: 0.82rem; font-weight: normal; margin-top: 4px; display: inline-block;">Note: This browser-based suite currently operates client-side without an external mail server. For direct inquiries, you can reach out via: <a href="mailto:contact@myusefultools.local" style="color: var(--primary); font-weight: 600;">contact@myusefultools.local</a></span>`;
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
