import re

JS_CODE = r'''// ============================================================================
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

// Helper: Ensure PDFLib is loaded
async function ensurePdfLib() {
  if (typeof PDFLib !== 'undefined') return PDFLib;
  return new Promise((resolve, reject) => {
    const s = document.createElement('script');
    s.src = 'assets/lib/pdf-lib.min.js';
    s.onload = () => resolve(window.PDFLib);
    s.onerror = () => {
      // CDN Fallback
      const s2 = document.createElement('script');
      s2.src = 'https://cdn.jsdelivr.net/npm/pdf-lib@1.17.1/dist/pdf-lib.min.js';
      s2.onload = () => resolve(window.PDFLib);
      s2.onerror = () => reject(new Error('PDF engine failed to load. Please check your network connection.'));
      document.head.appendChild(s2);
    };
    document.head.appendChild(s);
  });
}

// Helper: Ensure pdfjsLib is loaded
async function ensurePdfJsLib() {
  if (typeof pdfjsLib !== 'undefined') {
    if (typeof pdfjsLib.GlobalWorkerOptions !== 'undefined') {
      pdfjsLib.GlobalWorkerOptions.workerSrc = 'assets/lib/pdf.worker.min.js';
    }
    return pdfjsLib;
  }
  return new Promise((resolve, reject) => {
    const s = document.createElement('script');
    s.src = 'assets/lib/pdf.min.js';
    s.onload = () => {
      if (typeof pdfjsLib !== 'undefined' && pdfjsLib.GlobalWorkerOptions) {
        pdfjsLib.GlobalWorkerOptions.workerSrc = 'assets/lib/pdf.worker.min.js';
      }
      resolve(window.pdfjsLib);
    };
    s.onerror = () => {
      const s2 = document.createElement('script');
      s2.src = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js';
      s2.onload = () => {
        if (typeof pdfjsLib !== 'undefined' && pdfjsLib.GlobalWorkerOptions) {
          pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
        }
        resolve(window.pdfjsLib);
      };
      s2.onerror = () => reject(new Error('PDF renderer failed to load. Please check your network connection.'));
      document.head.appendChild(s2);
    };
    document.head.appendChild(s);
  });
}

// Helper: Asynchronously load an image file into an HTMLImageElement
function loadImageFromFile(file) {
  return new Promise((resolve, reject) => {
    const img = new Image();
    const url = URL.createObjectURL(file);
    img.onload = () => {
      resolve({ img, url });
    };
    img.onerror = () => {
      URL.revokeObjectURL(url);
      reject(new Error('Unable to decode image file. File may be corrupted or an unsupported format.'));
    };
    img.src = url;
  });
}

// ==================== 1. PDF MERGE ====================
let pdfMergeFiles = [];
let pdfMergeResultBlob = null;

function handlePdfMergeFiles(files) {
  const errEl = document.getElementById('pdf-merge-error');
  if (errEl) errEl.style.display = 'none';
  if (!files || files.length === 0) return;

  let added = 0;
  for (let i = 0; i < files.length; i++) {
    const f = files[i];
    if (f.type === 'application/pdf' || f.name.toLowerCase().endsWith('.pdf')) {
      pdfMergeFiles.push(f);
      added++;
    }
  }

  if (added === 0 && pdfMergeFiles.length === 0) {
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

  try {
    if (mergeBtn) mergeBtn.disabled = true;
    if (progEl) {
      progEl.textContent = 'Initializing PDF engine...';
      progEl.style.display = 'block';
    }

    const PDFEngine = await ensurePdfLib();
    if (progEl) progEl.textContent = 'Merging PDF documents locally in your browser...';

    const mergedPdf = await PDFEngine.PDFDocument.create();
    let totalPagesMerged = 0;

    for (let i = 0; i < pdfMergeFiles.length; i++) {
      const file = pdfMergeFiles[i];
      if (progEl) progEl.textContent = `Merging file ${i + 1} of ${pdfMergeFiles.length}: ${file.name}...`;
      const arrayBuffer = await file.arrayBuffer();
      const pdf = await PDFEngine.PDFDocument.load(arrayBuffer, { ignoreEncryption: true });
      const copiedPages = await mergedPdf.copyPages(pdf, pdf.getPageIndices());
      copiedPages.forEach(page => mergedPdf.addPage(page));
      totalPagesMerged += copiedPages.length;
    }

    if (progEl) progEl.textContent = 'Finalizing merged PDF...';
    const mergedPdfBytes = await mergedPdf.save();
    pdfMergeResultBlob = new Blob([mergedPdfBytes], { type: 'application/pdf' });

    if (progEl) progEl.style.display = 'none';

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
      errEl.textContent = 'Unable to merge selected PDFs: ' + err.message;
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
  const progEl = document.getElementById('pdf-split-progress');

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

  pdfSplitLoadedFile = file;

  // Immediate UI update
  document.getElementById('pdf-split-filename').textContent = file.name;
  document.getElementById('pdf-split-total-pages').textContent = 'Reading pages...';
  document.getElementById('pdf-split-filesize').textContent = formatBytes(file.size);
  if (summaryEl) summaryEl.style.display = 'flex';
  if (controlsEl) controlsEl.style.display = 'block';
  if (actionRow) actionRow.style.display = 'flex';

  try {
    if (progEl) {
      progEl.textContent = 'Reading PDF structure...';
      progEl.style.display = 'block';
    }
    const PDFEngine = await ensurePdfLib();
    const arrayBuffer = await file.arrayBuffer();
    const pdfDoc = await PDFEngine.PDFDocument.load(arrayBuffer, { ignoreEncryption: true });

    pdfSplitTotalPagesCount = pdfDoc.getPageCount();
    document.getElementById('pdf-split-total-pages').textContent = pdfSplitTotalPagesCount;

    const initialRange = pdfSplitTotalPagesCount > 1 ? `1-${Math.min(3, pdfSplitTotalPagesCount)}` : '1';
    const rangeInput = document.getElementById('pdf-split-range');
    if (rangeInput) rangeInput.value = initialRange;
    onPdfSplitRangeInput();

    if (progEl) progEl.style.display = 'none';
  } catch (err) {
    console.error('PDF Split Load Error:', err);
    if (progEl) progEl.style.display = 'none';
    if (errEl) {
      errEl.textContent = 'Could not read PDF. Document may be password-protected or corrupted.';
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
  const countBadge = document.getElementById('pdf-split-selected-count');
  const errEl = document.getElementById('pdf-split-error');
  if (!input || !countBadge) return;

  try {
    const indices = parsePageRanges(input.value, pdfSplitTotalPagesCount);
    countBadge.textContent = `${indices.length} page(s) selected`;
    if (errEl) errEl.style.display = 'none';
  } catch (e) {
    countBadge.textContent = 'Invalid selection';
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

    const PDFEngine = await ensurePdfLib();
    const arrayBuffer = await pdfSplitLoadedFile.arrayBuffer();
    const sourcePdf = await PDFEngine.PDFDocument.load(arrayBuffer, { ignoreEncryption: true });
    const splitPdf = await PDFEngine.PDFDocument.create();

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
  downloadBlob(pdfSplitResultBlob, `${base}-extracted.pdf`);
}

function resetPdfSplit() {
  pdfSplitLoadedFile = null;
  pdfSplitTotalPagesCount = 0;
  pdfSplitResultBlob = null;
  const input = document.getElementById('pdf-split-input');
  if (input) input.value = '';
  const summaryEl = document.getElementById('pdf-split-summary');
  if (summaryEl) summaryEl.style.display = 'none';
  const controlsEl = document.getElementById('pdf-split-controls');
  if (controlsEl) controlsEl.style.display = 'none';
  const actionRow = document.getElementById('pdf-split-action-row');
  if (actionRow) actionRow.style.display = 'none';
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
  const progEl = document.getElementById('pdf2img-progress');

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

  pdf2ImgFile = file;

  // Immediate UI reveal
  document.getElementById('pdf2img-filename').textContent = file.name;
  document.getElementById('pdf2img-total-pages').textContent = 'Reading pages...';
  document.getElementById('pdf2img-filesize').textContent = formatBytes(file.size);
  if (summaryEl) summaryEl.style.display = 'flex';
  if (controlsEl) controlsEl.style.display = 'block';
  if (actionRow) actionRow.style.display = 'flex';

  try {
    if (progEl) {
      progEl.textContent = 'Initializing PDF renderer...';
      progEl.style.display = 'block';
    }
    const pdfjs = await ensurePdfJsLib();
    const arrayBuffer = await file.arrayBuffer();
    const loadingTask = pdfjs.getDocument({ data: arrayBuffer });
    const pdfDoc = await loadingTask.promise;

    pdf2ImgDoc = pdfDoc;
    document.getElementById('pdf2img-total-pages').textContent = pdfDoc.numPages;
    if (progEl) progEl.style.display = 'none';
  } catch (err) {
    console.error('PDF to Images Read Error:', err);
    if (progEl) progEl.style.display = 'none';
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
      progEl.textContent = 'Rendering PDF pages to images locally...';
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
    if (f.type.startsWith('image/') || f.name.toLowerCase().match(/\.(jpe?g|png|webp|gif|bmp)$/)) {
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

  const layout = document.getElementById('img2pdf-page-size').value;
  const margin = parseFloat(document.getElementById('img2pdf-margins').value) || 0;

  try {
    if (btn) btn.disabled = true;
    if (progEl) {
      progEl.textContent = 'Initializing PDF engine...';
      progEl.style.display = 'block';
    }

    const PDFEngine = await ensurePdfLib();
    const pdfDoc = await PDFEngine.PDFDocument.create();

    for (let i = 0; i < img2PdfItems.length; i++) {
      const item = img2PdfItems[i];
      if (progEl) progEl.textContent = `Processing image ${i + 1} of ${img2PdfItems.length}...`;

      const { img } = await loadImageFromFile(item.file);
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

      const posX = margin + (availW - imgDrawWidth) / 2;
      const posY = margin + (availH - imgDrawHeight) / 2;

      const page = pdfDoc.addPage([pageWidth, pageHeight]);
      page.drawImage(embeddedImg, {
        x: posX,
        y: posY,
        width: imgDrawWidth,
        height: imgDrawHeight
      });
    }

    if (progEl) progEl.textContent = 'Finalizing PDF...';
    const pdfBytes = await pdfDoc.save();
    img2PdfResultBlob = new Blob([pdfBytes], { type: 'application/pdf' });

    if (progEl) progEl.style.display = 'none';

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

  imgCompOriginalFile = file;

  // Immediate UI display
  document.getElementById('imgcomp-filename').textContent = file.name;
  document.getElementById('imgcomp-orig-size').textContent = formatBytes(file.size);
  document.getElementById('imgcomp-orig-dims').textContent = 'Loading dimensions...';
  if (cardEl) cardEl.style.display = 'flex';
  if (controlsEl) controlsEl.style.display = 'block';
  if (actionRow) actionRow.style.display = 'flex';

  const thumb = document.getElementById('imgcomp-selected-thumb');
  const previewUrl = URL.createObjectURL(file);
  if (thumb) thumb.src = previewUrl;

  loadImageFromFile(file).then(({ img }) => {
    imgCompLoadedImage = img;
    document.getElementById('imgcomp-orig-dims').textContent = `${img.naturalWidth} × ${img.naturalHeight} px`;
  }).catch(err => {
    console.warn('Image decode warning:', err);
  });
}

function updateCompressorQuality(val) {
  const badge = document.getElementById('imgcomp-quality-val');
  if (badge) badge.textContent = val + '%';
}

async function runImageCompression() {
  const errEl = document.getElementById('imgcomp-error');
  const progEl = document.getElementById('imgcomp-progress');
  const resultCard = document.getElementById('imgcomp-result');

  if (errEl) errEl.style.display = 'none';
  if (!imgCompOriginalFile) {
    if (errEl) {
      errEl.textContent = 'Please choose an image file first.';
      errEl.style.display = 'block';
    }
    return;
  }

  try {
    let img = imgCompLoadedImage;
    if (!img) {
      const loaded = await loadImageFromFile(imgCompOriginalFile);
      img = loaded.img;
      imgCompLoadedImage = img;
    }

    const quality = parseInt(document.getElementById('imgcomp-quality').value, 10) / 100;
    const maxWOpt = document.getElementById('imgcomp-max-width').value;
    const formatOpt = document.getElementById('imgcomp-format').value;

    let targetFormat = formatOpt === 'auto' ? (imgCompOriginalFile.type || 'image/jpeg') : formatOpt;
    if (targetFormat !== 'image/jpeg' && targetFormat !== 'image/webp') {
      targetFormat = 'image/jpeg';
    }

    let w = img.naturalWidth;
    let h = img.naturalHeight;

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

    ctx.drawImage(img, 0, 0, w, h);

    canvas.toBlob(blob => {
      if (!blob) return;
      imgCompResultBlob = blob;

      const origSize = imgCompOriginalFile.size;
      const newSize = blob.size;
      const reduction = Math.max(0, Math.round(((origSize - newSize) / origSize) * 100));

      document.getElementById('imgcomp-res-orig').textContent = formatBytes(origSize);
      document.getElementById('imgcomp-res-new').textContent = formatBytes(newSize);
      document.getElementById('imgcomp-res-saving').textContent = `-${reduction}%`;

      const preview = document.getElementById('imgcomp-preview');
      if (preview) preview.src = URL.createObjectURL(blob);

      if (resultCard) {
        resultCard.style.display = 'block';
        resultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
      showToast('✓ Image compressed successfully!');
    }, targetFormat, quality);
  } catch (err) {
    console.error('Compression error:', err);
    if (errEl) {
      errEl.textContent = 'Compression failed: ' + err.message;
      errEl.style.display = 'block';
    }
  }
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

  // Immediate UI display
  document.getElementById('imgresize-filename').textContent = file.name;
  document.getElementById('imgresize-orig-size').textContent = formatBytes(file.size);
  document.getElementById('imgresize-orig-dims').textContent = 'Loading dimensions...';
  if (cardEl) cardEl.style.display = 'flex';
  if (controls) controls.style.display = 'block';
  if (actions) actions.style.display = 'flex';

  const thumb = document.getElementById('imgresize-selected-thumb');
  const previewUrl = URL.createObjectURL(file);
  if (thumb) thumb.src = previewUrl;

  loadImageFromFile(file).then(({ img }) => {
    imgResizeLoadedImage = img;
    const w = img.naturalWidth;
    const h = img.naturalHeight;
    imgResizeNaturalRatio = w / h;

    document.getElementById('imgresize-orig-dims').textContent = `${w} × ${h} px`;
    document.getElementById('imgresize-orig-ratio').textContent = `${imgResizeNaturalRatio.toFixed(2)}:1`;
    document.getElementById('imgresize-width').value = w;
    document.getElementById('imgresize-height').value = h;
  }).catch(err => {
    console.warn('Resizer load warning:', err);
  });
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

async function runImageResize() {
  const errEl = document.getElementById('imgresize-error');
  const resultCard = document.getElementById('imgresize-result');

  if (errEl) errEl.style.display = 'none';
  if (!imgResizeOriginalFile) {
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

  try {
    let img = imgResizeLoadedImage;
    if (!img) {
      const loaded = await loadImageFromFile(imgResizeOriginalFile);
      img = loaded.img;
      imgResizeLoadedImage = img;
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
    ctx.drawImage(img, 0, 0, w, h);

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
  } catch (err) {
    console.error('Resize error:', err);
    if (errEl) {
      errEl.textContent = 'Resize failed: ' + err.message;
      errEl.style.display = 'block';
    }
  }
}

function downloadResizedImage() {
  if (!imgResizeResultBlob || !imgResizeOriginalFile) return;
  const isPng = imgResizeOriginalFile.type === 'image/png';
  const ext = isPng ? 'png' : 'jpg';
  const base = imgResizeOriginalFile.name.replace(/\.[^/.]+$/, '');
  const w = document.getElementById('imgresize-width').value;
  const h = document.getElementById('imgresize-height').value;
  downloadBlob(imgResizeResultBlob, `${base}-${w}x${h}.${ext}`);
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

  // Immediate UI display
  document.getElementById('jpg2png-filename').textContent = file.name;
  document.getElementById('jpg2png-orig-size').textContent = formatBytes(file.size);
  document.getElementById('jpg2png-orig-dims').textContent = 'Loading dimensions...';
  if (cardEl) cardEl.style.display = 'flex';
  if (controls) controls.style.display = 'block';
  if (actions) actions.style.display = 'flex';

  const thumb = document.getElementById('jpg2png-selected-thumb');
  const previewUrl = URL.createObjectURL(file);
  if (thumb) thumb.src = previewUrl;

  loadImageFromFile(file).then(({ img }) => {
    jpg2PngLoadedImage = img;
    document.getElementById('jpg2png-orig-dims').textContent = `${img.naturalWidth} × ${img.naturalHeight} px`;
  }).catch(err => {
    console.warn('JPG load warning:', err);
  });
}

async function runJpgToPng() {
  const errEl = document.getElementById('jpg2png-error');
  const resultCard = document.getElementById('jpg2png-result');

  if (errEl) errEl.style.display = 'none';
  if (!jpg2PngOriginalFile) {
    if (errEl) {
      errEl.textContent = 'Please choose a JPG/JPEG image first.';
      errEl.style.display = 'block';
    }
    return;
  }

  try {
    let img = jpg2PngLoadedImage;
    if (!img) {
      const loaded = await loadImageFromFile(jpg2PngOriginalFile);
      img = loaded.img;
      jpg2PngLoadedImage = img;
    }

    const canvas = document.createElement('canvas');
    canvas.width = img.naturalWidth;
    canvas.height = img.naturalHeight;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(img, 0, 0);

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
      showToast('✓ Converted to PNG successfully!');
    }, 'image/png');
  } catch (err) {
    console.error('JPG to PNG error:', err);
    if (errEl) {
      errEl.textContent = 'Conversion failed: ' + err.message;
      errEl.style.display = 'block';
    }
  }
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

  // Immediate UI display
  document.getElementById('png2jpg-filename').textContent = file.name;
  document.getElementById('png2jpg-orig-size').textContent = formatBytes(file.size);
  document.getElementById('png2jpg-orig-dims').textContent = 'Loading dimensions...';
  if (cardEl) cardEl.style.display = 'flex';
  if (controls) controls.style.display = 'block';
  if (actions) actions.style.display = 'flex';

  const thumb = document.getElementById('png2jpg-selected-thumb');
  const previewUrl = URL.createObjectURL(file);
  if (thumb) thumb.src = previewUrl;

  loadImageFromFile(file).then(({ img }) => {
    png2JpgLoadedImage = img;
    document.getElementById('png2jpg-orig-dims').textContent = `${img.naturalWidth} × ${img.naturalHeight} px`;
  }).catch(err => {
    console.warn('PNG load warning:', err);
  });
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

async function runPngToJpg() {
  const errEl = document.getElementById('png2jpg-error');
  const resultCard = document.getElementById('png2jpg-result');

  if (errEl) errEl.style.display = 'none';
  if (!png2JpgOriginalFile) {
    if (errEl) {
      errEl.textContent = 'Please choose a PNG image first.';
      errEl.style.display = 'block';
    }
    return;
  }

  try {
    let img = png2JpgLoadedImage;
    if (!img) {
      const loaded = await loadImageFromFile(png2JpgOriginalFile);
      img = loaded.img;
      png2JpgLoadedImage = img;
    }

    const quality = parseInt(document.getElementById('png2jpg-quality').value, 10) / 100;
    const canvas = document.createElement('canvas');
    canvas.width = img.naturalWidth;
    canvas.height = img.naturalHeight;
    const ctx = canvas.getContext('2d');

    // Fill custom background color for transparency
    ctx.fillStyle = png2JpgBgColor || '#ffffff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(img, 0, 0);

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
      showToast('✓ Converted to JPG successfully!');
    }, 'image/jpeg', quality);
  } catch (err) {
    console.error('PNG to JPG error:', err);
    if (errEl) {
      errEl.textContent = 'Conversion failed: ' + err.message;
      errEl.style.display = 'block';
    }
  }
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

  // Immediate UI display
  document.getElementById('imgcrop-filename').textContent = file.name;
  document.getElementById('imgcrop-orig-size').textContent = formatBytes(file.size);
  document.getElementById('imgcrop-orig-dims').textContent = 'Loading dimensions...';
  if (cardEl) cardEl.style.display = 'flex';
  if (controls) controls.style.display = 'block';
  if (actions) actions.style.display = 'flex';

  const thumb = document.getElementById('imgcrop-selected-thumb');
  const previewUrl = URL.createObjectURL(file);
  if (thumb) thumb.src = previewUrl;

  loadImageFromFile(file).then(({ img }) => {
    imgCropLoadedImage = img;
    document.getElementById('imgcrop-orig-dims').textContent = `${img.naturalWidth} × ${img.naturalHeight} px`;
    setTimeout(drawCropCanvas, 50);
  }).catch(err => {
    console.warn('Crop load warning:', err);
  });
}

function setCropRatio(ratio) {
  imgCropCurrentRatio = ratio;
  const ratioBtnMap = {
    'free': 'crop-ratio-free',
    '1:1': 'crop-ratio-1-1',
    '4:3': 'crop-ratio-4-3',
    '16:9': 'crop-ratio-16-9',
    '1-1': 'crop-ratio-1-1',
    '4-3': 'crop-ratio-4-3',
    '16-9': 'crop-ratio-16-9'
  };
  const activeBtnId = ratioBtnMap[ratio] || 'crop-ratio-free';
  ['crop-ratio-free', 'crop-ratio-1-1', 'crop-ratio-4-3', 'crop-ratio-16-9'].forEach(btnId => {
    const btn = document.getElementById(btnId);
    if (btn) {
      if (btnId === activeBtnId) btn.classList.add('active');
      else btn.classList.remove('active');
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
  if (imgCropCurrentRatio === '1:1' || imgCropCurrentRatio === '1-1') {
    const minDim = Math.min(imgW, imgH) * sizeVal;
    cropW = minDim;
    cropH = minDim;
  } else if (imgCropCurrentRatio === '4:3' || imgCropCurrentRatio === '4-3') {
    const targetW = imgW * sizeVal;
    cropW = targetW;
    cropH = targetW * (3 / 4);
    if (cropH > imgH) {
      cropH = imgH * sizeVal;
      cropW = cropH * (4 / 3);
    }
  } else if (imgCropCurrentRatio === '16:9' || imgCropCurrentRatio === '16-9') {
    const targetW = imgW * sizeVal;
    cropW = targetW;
    cropH = targetW * (9 / 16);
    if (cropH > imgH) {
      cropH = imgH * sizeVal;
      cropW = cropH * (16 / 9);
    }
  } else {
    // Freeform
    cropW = imgW * sizeVal;
    cropH = imgH * sizeVal;
  }

  cropW = Math.max(10, Math.min(cropW, imgW));
  cropH = Math.max(10, Math.min(cropH, imgH));

  const maxLeft = imgW - cropW;
  const maxTop = imgH - cropH;

  const cropX = Math.max(0, Math.min(maxLeft * posXVal, maxLeft));
  const cropY = Math.max(0, Math.min(maxTop * posYVal, maxTop));

  return {
    x: Math.round(cropX),
    y: Math.round(cropY),
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

  // Dark overlay
  ctx.fillStyle = 'rgba(0, 0, 0, 0.6)';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Clear crop box to show bright area
  const box = getCropBox();
  const cX = box.x * displayScale;
  const cY = box.y * displayScale;
  const cW = box.w * displayScale;
  const cH = box.h * displayScale;

  ctx.clearRect(cX, cY, cW, cH);
  ctx.drawImage(imgCropLoadedImage, box.x, box.y, box.w, box.h, cX, cY, cW, cH);

  // Crop border outline
  ctx.strokeStyle = '#2563eb';
  ctx.lineWidth = 2;
  ctx.strokeRect(cX, cY, cW, cH);

  // Grid lines (rule of thirds)
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(cX + cW / 3, cY); ctx.lineTo(cX + cW / 3, cY + cH);
  ctx.moveTo(cX + (2 * cW) / 3, cY); ctx.lineTo(cX + (2 * cW) / 3, cY + cH);
  ctx.moveTo(cX, cY + cH / 3); ctx.lineTo(cX + cW, cY + cH / 3);
  ctx.moveTo(cX, cY + (2 * cH) / 3); ctx.lineTo(cX + cW, cY + (2 * cH) / 3);
  ctx.stroke();
}

async function runImageCrop() {
  const errEl = document.getElementById('imgcrop-error');
  const resultCard = document.getElementById('imgcrop-result');

  if (errEl) errEl.style.display = 'none';
  if (!imgCropOriginalFile) {
    if (errEl) {
      errEl.textContent = 'Please choose an image file first.';
      errEl.style.display = 'block';
    }
    return;
  }

  try {
    let img = imgCropLoadedImage;
    if (!img) {
      const loaded = await loadImageFromFile(imgCropOriginalFile);
      img = loaded.img;
      imgCropLoadedImage = img;
    }

    const box = getCropBox();
    if (!box.w || !box.h) return;

    const canvas = document.createElement('canvas');
    canvas.width = box.w;
    canvas.height = box.h;
    const ctx = canvas.getContext('2d');
    ctx.imageSmoothingEnabled = true;
    ctx.imageSmoothingQuality = 'high';

    ctx.drawImage(img, box.x, box.y, box.w, box.h, 0, 0, box.w, box.h);

    const isPng = imgCropOriginalFile.type === 'image/png';
    const mime = isPng ? 'image/png' : 'image/jpeg';

    canvas.toBlob(blob => {
      if (!blob) return;
      imgCropResultBlob = blob;

      document.getElementById('imgcrop-res-dims').textContent = `${box.w} × ${box.h} px`;
      document.getElementById('imgcrop-res-size').textContent = formatBytes(blob.size);
      document.getElementById('imgcrop-res-ratio').textContent = `${(box.w / box.h).toFixed(2)}:1`;

      const preview = document.getElementById('imgcrop-preview');
      if (preview) preview.src = URL.createObjectURL(blob);

      if (resultCard) {
        resultCard.style.display = 'block';
        resultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
      showToast('✓ Image cropped successfully!');
    }, mime, 0.92);
  } catch (err) {
    console.error('Crop error:', err);
    if (errEl) {
      errEl.textContent = 'Crop failed: ' + err.message;
      errEl.style.display = 'block';
    }
  }
}

function downloadCroppedImage() {
  if (!imgCropResultBlob || !imgCropOriginalFile) return;
  const isPng = imgCropOriginalFile.type === 'image/png';
  const ext = isPng ? 'png' : 'jpg';
  const baseName = imgCropOriginalFile.name.replace(/\.[^/.]+$/, '');
  const box = getCropBox();
  downloadBlob(imgCropResultBlob, `${baseName}-cropped-${box.w}x${box.h}.${ext}`);
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

  // Immediate UI display
  document.getElementById('img2webp-filename').textContent = file.name;
  document.getElementById('img2webp-orig-size').textContent = formatBytes(file.size);
  document.getElementById('img2webp-orig-dims').textContent = 'Loading dimensions...';
  if (cardEl) cardEl.style.display = 'flex';
  if (controls) controls.style.display = 'block';
  if (actions) actions.style.display = 'flex';

  const thumb = document.getElementById('img2webp-selected-thumb');
  const previewUrl = URL.createObjectURL(file);
  if (thumb) thumb.src = previewUrl;

  loadImageFromFile(file).then(({ img }) => {
    img2WebpLoadedImage = img;
    document.getElementById('img2webp-orig-dims').textContent = `${img.naturalWidth} × ${img.naturalHeight} px`;
  }).catch(err => {
    console.warn('WebP load warning:', err);
  });
}

function updateWebpQuality(val) {
  const qVal = document.getElementById('img2webp-quality-val');
  if (qVal) qVal.textContent = val + '%';
}

async function runImageToWebp() {
  const errEl = document.getElementById('img2webp-error');
  const resultCard = document.getElementById('img2webp-result');

  if (errEl) errEl.style.display = 'none';
  if (!img2WebpOriginalFile) {
    if (errEl) {
      errEl.textContent = 'Please choose an image to convert.';
      errEl.style.display = 'block';
    }
    return;
  }

  try {
    let img = img2WebpLoadedImage;
    if (!img) {
      const loaded = await loadImageFromFile(img2WebpOriginalFile);
      img = loaded.img;
      img2WebpLoadedImage = img;
    }

    const quality = parseInt(document.getElementById('img2webp-quality').value, 10) / 100;
    const canvas = document.createElement('canvas');
    canvas.width = img.naturalWidth;
    canvas.height = img.naturalHeight;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(img, 0, 0);

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
      showToast('✓ Converted to WebP successfully!');
    }, 'image/webp', quality);
  } catch (err) {
    console.error('WebP conversion error:', err);
    if (errEl) {
      errEl.textContent = 'Conversion failed: ' + err.message;
      errEl.style.display = 'block';
    }
  }
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

// Drag & Drop Setup and Input Change Listeners for all 10 tools
function initFileDropzones() {
  const toolConfigs = [
    { id: 'pdf-merge-dropzone', inputId: 'pdf-merge-input', handler: files => handlePdfMergeFiles(files) },
    { id: 'pdf-split-dropzone', inputId: 'pdf-split-input', handler: files => files && files[0] && handlePdfSplitFile(files[0]) },
    { id: 'pdf2img-dropzone', inputId: 'pdf2img-input', handler: files => files && files[0] && handlePdfToImagesFile(files[0]) },
    { id: 'img2pdf-dropzone', inputId: 'img2pdf-input', handler: files => handleImagesToPdfFiles(files) },
    { id: 'imgcomp-dropzone', inputId: 'imgcomp-input', handler: files => files && files[0] && handleImageCompressorFile(files[0]) },
    { id: 'imgresize-dropzone', inputId: 'imgresize-input', handler: files => files && files[0] && handleImageResizerFile(files[0]) },
    { id: 'jpg2png-dropzone', inputId: 'jpg2png-input', handler: files => files && files[0] && handleJpgToPngFile(files[0]) },
    { id: 'png2jpg-dropzone', inputId: 'png2jpg-input', handler: files => files && files[0] && handlePngToJpgFile(files[0]) },
    { id: 'imgcrop-dropzone', inputId: 'imgcrop-input', handler: files => files && files[0] && handleImageCropperFile(files[0]) },
    { id: 'img2webp-dropzone', inputId: 'img2webp-input', handler: files => files && files[0] && handleImageToWebpFile(files[0]) }
  ];

  toolConfigs.forEach(cfg => {
    // 1. Listen directly to file input change event
    const inputEl = document.getElementById(cfg.inputId);
    if (inputEl) {
      inputEl.addEventListener('change', function(e) {
        if (this.files && this.files.length > 0) {
          cfg.handler(this.files);
        }
      });
    }

    // 2. Drag & Drop on dropzone
    const dropzoneEl = document.getElementById(cfg.id);
    if (!dropzoneEl) return;

    ['dragenter', 'dragover'].forEach(evt => {
      dropzoneEl.addEventListener(evt, e => {
        e.preventDefault();
        e.stopPropagation();
        dropzoneEl.classList.add('dragover');
      });
    });

    ['dragleave', 'drop'].forEach(evt => {
      dropzoneEl.addEventListener(evt, e => {
        e.preventDefault();
        e.stopPropagation();
        dropzoneEl.classList.remove('dragover');
      });
    });

    dropzoneEl.addEventListener('drop', e => {
      if (e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files.length) {
        cfg.handler(e.dataTransfer.files);
      }
    });
  });
}

// Auto-initialize dropzones when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initFileDropzones);
} else {
  initFileDropzones();
}
'''

with open('tools_pdf_image_js.py', 'w', encoding='utf-8') as f:
    f.write(f'# tools_pdf_image_js.py\nJS_CODE = r\'\'\'{JS_CODE}\'\'\'\n')

print("tools_pdf_image_js.py written successfully.")
