# tools_js.py
# Complete JavaScript implementations for the 20 new tools of MY USEFUL TOOLS

JS_CODE = """
// ============================================================================
// ==================== 20 NEW TOOLS JAVASCRIPT IMPLEMENTATIONS ================
// ============================================================================

// Helper utility functions for new tools
function formatNumberWithCommas(num, dec = 2) {
  if (isNaN(num) || !isFinite(num)) return '0';
  const parts = Number(num).toFixed(dec).split('.');
  parts[0] = parts[0].replace(/\\B(?=(\\d{3})+(?!\\d))/g, ',');
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
  return '₹' + otherNumbers.replace(/\\B(?=(\\d{2})+(?!\\d))/g, ',') + lastThree;
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
  if (minEl) minEl.textContent = formatNumberWithCommas(totalMinutes, 1).replace(/\\.0$/, '');

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
"""

print("tools_js.py created successfully with all 20 calculator functions.")
