# tools_pdf_image_js.py
# Complete, production-grade client-side JavaScript for the 10 new PDF & Image tools

JS_CODE = r'''
// ============================================================================
// PDF & IMAGE TOOLS - 10 NEW BROWSER-BASED UTILITY TOOLS
// 100% Client-Side, Zero Server Uploads, Fully Local and Private
// ============================================================================

// Utility: Format bytes into readable string (e.g. 1.25 MB)
function formatBytes(bytes, decimals = 1) {
  if (!bytes || bytes === 0) return '0 B';
  const k = 1024;
  const dm = decimals < 0 ? 0 : decimals;
  const sizes = ['B', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
}

// Utility: Trigger browser download for a Blob
function downloadBlob(blob, filename) {
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  setTimeout(() => {
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }, 1000);
}

// ==================== 1. PDF MERGE ====================
let pdfMergeFiles = [];

function handlePdfMergeFiles(files) {
  const errEl = document.getElementById('pdf-merge-error');
  if (errEl) errEl.style.display = 'none';

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

  if (!container || !listEl) return;

  if (pdfMergeFiles.length === 0) {
    container.style.display = 'none';
    if (mergeBtn) mergeBtn.disabled = true;
    return;
  }

  container.style.display = 'block';
  if (countEl) countEl.textContent = pdfMergeFiles.length;
  if (mergeBtn) mergeBtn.disabled = pdfMergeFiles.length < 2;

  listEl.innerHTML = pdfMergeFiles.map((file, idx) => `
    <div class="file-item-row" data-index="${idx}">
      <span class="file-item-idx">${idx + 1}</span>
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
      errEl.textContent = 'PDF library is initializing. Please check your internet connection and try again.';
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
    const mergedBlob = new Blob([mergedPdfBytes], { type: 'application/pdf' });

    if (progEl) progEl.style.display = 'none';

    // Populate results
    document.getElementById('pdf-merge-result-pages').textContent = totalPagesMerged;
    document.getElementById('pdf-merge-result-count').textContent = pdfMergeFiles.length;
    document.getElementById('pdf-merge-result-size').textContent = formatBytes(mergedBlob.size);

    const downloadLink = document.getElementById('pdf-merge-download-btn');
    if (downloadLink) {
      downloadLink.href = URL.createObjectURL(mergedBlob);
      downloadLink.download = `merged-document-${Date.now()}.pdf`;
    }

    if (resultCard) resultCard.style.display = 'block';
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

function resetPdfMerge() {
  pdfMergeFiles = [];
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

async function handlePdfSplitFile(file) {
  const errEl = document.getElementById('pdf-split-error');
  const controlsEl = document.getElementById('pdf-split-controls');
  const splitBtn = document.getElementById('pdf-split-btn');

  if (errEl) errEl.style.display = 'none';
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
    document.getElementById('pdf-split-range').value = pdfSplitTotalPagesCount > 1 ? `1-${Math.min(3, pdfSplitTotalPagesCount)}` : '1';

    if (controlsEl) controlsEl.style.display = 'block';
    if (splitBtn) splitBtn.disabled = false;
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
    input.value = evens.length ? evens.join(', ') : '2';
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
  if (!rangeVal) {
    if (errEl) {
      errEl.textContent = 'Please enter pages or a page range to extract.';
      errEl.style.display = 'block';
    }
    return;
  }

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
      progEl.textContent = `Extracting ${targetIndices.length} pages in browser...`;
      progEl.style.display = 'block';
    }

    const arrayBuffer = await pdfSplitLoadedFile.arrayBuffer();
    const sourcePdf = await PDFLib.PDFDocument.load(arrayBuffer, { ignoreEncryption: true });
    const splitPdf = await PDFLib.PDFDocument.create();

    const copiedPages = await splitPdf.copyPages(sourcePdf, targetIndices);
    copiedPages.forEach(p => splitPdf.addPage(p));

    const splitBytes = await splitPdf.save();
    const splitBlob = new Blob([splitBytes], { type: 'application/pdf' });

    if (progEl) progEl.style.display = 'none';

    document.getElementById('pdf-split-result-pages').textContent = targetIndices.length;
    document.getElementById('pdf-split-result-range').textContent = rangeVal;
    document.getElementById('pdf-split-result-size').textContent = formatBytes(splitBlob.size);

    const downloadLink = document.getElementById('pdf-split-download-btn');
    if (downloadLink) {
      downloadLink.href = URL.createObjectURL(splitBlob);
      downloadLink.download = `extracted-pages-${Date.now()}.pdf`;
    }

    if (resultCard) resultCard.style.display = 'block';
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

function resetPdfSplit() {
  pdfSplitLoadedFile = null;
  pdfSplitTotalPagesCount = 0;
  const input = document.getElementById('pdf-split-input');
  if (input) input.value = '';
  const controls = document.getElementById('pdf-split-controls');
  if (controls) controls.style.display = 'none';
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

async function handlePdfToImagesFile(file) {
  const errEl = document.getElementById('pdf2img-error');
  const controlsEl = document.getElementById('pdf2img-controls');
  const convertBtn = document.getElementById('pdf2img-btn');

  if (errEl) errEl.style.display = 'none';
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
    pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
    const arrayBuffer = await file.arrayBuffer();
    const loadingTask = pdfjsLib.getDocument({ data: arrayBuffer });
    const pdfDoc = await loadingTask.promise;

    pdf2ImgFile = file;
    document.getElementById('pdf2img-filename').textContent = file.name;
    document.getElementById('pdf2img-total-pages').textContent = pdfDoc.numPages;

    if (controlsEl) controlsEl.style.display = 'block';
    if (convertBtn) convertBtn.disabled = false;
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

  if (!pdf2ImgFile) {
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

    const arrayBuffer = await pdf2ImgFile.arrayBuffer();
    const pdfDoc = await pdfjsLib.getDocument({ data: arrayBuffer }).promise;
    const numPages = pdfDoc.numPages;

    for (let pageNum = 1; pageNum <= numPages; pageNum++) {
      if (progEl) progEl.textContent = `Rendering page ${pageNum} of ${numPages}...`;
      const page = await pdfDoc.getPage(pageNum);
      const viewport = page.getViewport({ scale });

      const canvas = document.createElement('canvas');
      canvas.width = viewport.width;
      canvas.height = viewport.height;
      const ctx = canvas.getContext('2d');

      // Fill white background for JPEGs
      if (format === 'image/jpeg') {
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
      }

      await page.render({ canvasContext: ctx, viewport }).promise;

      // Convert canvas to blob
      await new Promise(resolve => {
        canvas.toBlob(blob => {
          const blobUrl = URL.createObjectURL(blob);
          const fileName = `page-${pageNum}.${ext}`;
          pdf2ImgRenderedBlobs.push({ blob, url: blobUrl, filename: fileName, pageNum });

          const card = document.createElement('div');
          card.className = 'image-thumb-card';
          card.innerHTML = `
            <div class="thumb-header">Page ${pageNum}</div>
            <div class="thumb-preview-wrap">
              <img src="${blobUrl}" class="thumb-preview" alt="Page ${pageNum}">
            </div>
            <div class="thumb-actions">
              <a href="${blobUrl}" download="${fileName}" class="btn btn-outline btn-sm btn-block">⬇ Page ${pageNum}</a>
            </div>
          `;
          galleryEl.appendChild(card);
          resolve();
        }, format, 0.92);
      });
    }

    if (progEl) progEl.style.display = 'none';
    document.getElementById('pdf2img-rendered-count').textContent = numPages;
    if (resultsCard) resultsCard.style.display = 'block';
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
  pdf2ImgRenderedBlobs = [];
  const input = document.getElementById('pdf2img-input');
  if (input) input.value = '';
  const controls = document.getElementById('pdf2img-controls');
  if (controls) controls.style.display = 'none';
  const results = document.getElementById('pdf2img-results');
  if (results) results.style.display = 'none';
  const errEl = document.getElementById('pdf2img-error');
  if (errEl) errEl.style.display = 'none';
  const progEl = document.getElementById('pdf2img-progress');
  if (progEl) progEl.style.display = 'none';
}


// ==================== 4. IMAGES TO PDF ====================
let img2PdfItems = [];

function handleImagesToPdfFiles(files) {
  const errEl = document.getElementById('img2pdf-error');
  if (errEl) errEl.style.display = 'none';

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
  const btn = document.getElementById('img2pdf-btn');

  if (!controls || !listEl) return;

  if (img2PdfItems.length === 0) {
    controls.style.display = 'none';
    if (btn) btn.disabled = true;
    return;
  }

  controls.style.display = 'block';
  if (countEl) countEl.textContent = img2PdfItems.length;
  if (btn) btn.disabled = false;

  listEl.innerHTML = img2PdfItems.map((item, idx) => `
    <div class="file-item-row" data-index="${idx}">
      <span class="file-item-idx">${idx + 1}</span>
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
      errEl.textContent = 'PDF engine is loading. Please retry.';
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

      // Read image via an Image element to normalize format to PNG canvas
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
      let imgDrawWidth, imgDrawHeight, drawX, drawY;

      if (layout === 'a4-portrait') {
        pageWidth = 595.28;
        pageHeight = 841.89;
      } else if (layout === 'a4-landscape') {
        pageWidth = 841.89;
        pageHeight = 595.28;
      } else {
        // Natural fit
        pageWidth = img.naturalWidth + margin * 2;
        pageHeight = img.naturalHeight + margin * 2;
      }

      const availW = pageWidth - margin * 2;
      const availH = pageHeight - margin * 2;
      const scale = Math.min(availW / img.naturalWidth, availH / img.naturalHeight, 1);

      imgDrawWidth = img.naturalWidth * scale;
      imgDrawHeight = img.naturalHeight * scale;
      drawX = margin + (availW - imgDrawWidth) / 2;
      drawY = margin + (availH - imgDrawHeight) / 2;

      const page = pdfDoc.addPage([pageWidth, pageHeight]);
      page.drawImage(embeddedImg, {
        x: drawX,
        y: drawY,
        width: imgDrawWidth,
        height: imgDrawHeight
      });
    }

    const pdfBytes = await pdfDoc.save();
    const pdfBlob = new Blob([pdfBytes], { type: 'application/pdf' });

    if (progEl) progEl.style.display = 'none';

    document.getElementById('img2pdf-result-pages').textContent = img2PdfItems.length;
    document.getElementById('img2pdf-result-count').textContent = img2PdfItems.length;
    document.getElementById('img2pdf-result-size').textContent = formatBytes(pdfBlob.size);

    const downloadLink = document.getElementById('img2pdf-download-btn');
    if (downloadLink) {
      downloadLink.href = URL.createObjectURL(pdfBlob);
      downloadLink.download = `images-document-${Date.now()}.pdf`;
    }

    if (resultCard) resultCard.style.display = 'block';
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

function resetImagesToPdf() {
  img2PdfItems = [];
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

function handleImageCompressorFile(file) {
  const errEl = document.getElementById('imgcomp-error');
  const controlsEl = document.getElementById('imgcomp-controls');
  const actionRow = document.getElementById('imgcomp-action-row');

  if (errEl) errEl.style.display = 'none';
  if (!file) return;

  if (!file.type.startsWith('image/')) {
    if (errEl) {
      errEl.textContent = 'Please choose a valid image file.';
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
      document.getElementById('imgcomp-filename').textContent = file.name;
      document.getElementById('imgcomp-orig-size').textContent = formatBytes(file.size);
      document.getElementById('imgcomp-orig-dims').textContent = `${img.naturalWidth} × ${img.naturalHeight} px`;

      if (controlsEl) controlsEl.style.display = 'block';
      if (actionRow) actionRow.style.display = 'flex';
      runImageCompression();
    };
    img.src = e.target.result;
  };
  reader.readAsDataURL(file);
}

function updateCompressorQuality(val) {
  document.getElementById('imgcomp-quality-val').textContent = val + '%';
  runImageCompression();
}

function runImageCompression() {
  if (!imgCompLoadedImage || !imgCompOriginalFile) return;

  const quality = parseInt(document.getElementById('imgcomp-quality').value, 10) / 100;
  const maxWOpt = document.getElementById('imgcomp-max-width').value;
  const formatOpt = document.getElementById('imgcomp-format').value;

  let targetFormat = formatOpt === 'auto' ? (imgCompOriginalFile.type || 'image/jpeg') : formatOpt;
  if (targetFormat !== 'image/jpeg' && targetFormat !== 'image/webp') {
    targetFormat = 'image/jpeg'; // fallback
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
    if (!blob) return;

    const originalSize = imgCompOriginalFile.size;
    const newSize = blob.size;
    const savings = Math.max(0, Math.round(((originalSize - newSize) / originalSize) * 100));

    document.getElementById('imgcomp-res-orig').textContent = formatBytes(originalSize);
    document.getElementById('imgcomp-res-new').textContent = formatBytes(newSize);
    document.getElementById('imgcomp-res-saving').textContent = `-${savings}%`;

    const preview = document.getElementById('imgcomp-preview');
    if (preview) preview.src = URL.createObjectURL(blob);

    const ext = targetFormat === 'image/webp' ? 'webp' : 'jpg';
    const baseName = imgCompOriginalFile.name.replace(/\.[^/.]+$/, '');
    const dlBtn = document.getElementById('imgcomp-download-btn');
    if (dlBtn) {
      dlBtn.href = URL.createObjectURL(blob);
      dlBtn.download = `${baseName}-compressed.${ext}`;
    }

    const resultCard = document.getElementById('imgcomp-result');
    if (resultCard) resultCard.style.display = 'block';
  }, targetFormat, quality);
}

function resetImageCompressor() {
  imgCompLoadedImage = null;
  imgCompOriginalFile = null;
  const input = document.getElementById('imgcomp-input');
  if (input) input.value = '';
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
let imgResizeAspectRatioLocked = true;
let imgResizeNaturalRatio = 1;

function handleImageResizerFile(file) {
  const errEl = document.getElementById('imgresize-error');
  const controls = document.getElementById('imgresize-controls');
  const actions = document.getElementById('imgresize-action-row');

  if (errEl) errEl.style.display = 'none';
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

      document.getElementById('imgresize-filename').textContent = file.name;
      document.getElementById('imgresize-orig-dims').textContent = `${w} × ${h} px`;
      document.getElementById('imgresize-orig-ratio').textContent = `${imgResizeNaturalRatio.toFixed(2)}:1`;
      document.getElementById('imgresize-orig-size').textContent = formatBytes(file.size);

      document.getElementById('imgresize-width').value = w;
      document.getElementById('imgresize-height').value = h;

      if (controls) controls.style.display = 'block';
      if (actions) actions.style.display = 'flex';
      runImageResize();
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
  runImageResize();
}

function applyResizerExact(w, h) {
  document.getElementById('imgresize-width').value = w;
  document.getElementById('imgresize-height').value = h;
  runImageResize();
}

function runImageResize() {
  if (!imgResizeLoadedImage) return;

  const w = parseInt(document.getElementById('imgresize-width').value, 10);
  const h = parseInt(document.getElementById('imgresize-height').value, 10);

  if (!w || !h || w <= 0 || h <= 0) {
    const errEl = document.getElementById('imgresize-error');
    if (errEl) {
      errEl.textContent = 'Please enter valid width and height dimensions.';
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

    document.getElementById('imgresize-res-dims').textContent = `${w} × ${h}`;
    document.getElementById('imgresize-res-size').textContent = formatBytes(blob.size);
    document.getElementById('imgresize-res-format').textContent = isPng ? 'PNG' : 'JPG';

    const preview = document.getElementById('imgresize-preview');
    if (preview) preview.src = URL.createObjectURL(blob);

    const ext = isPng ? 'png' : 'jpg';
    const baseName = imgResizeOriginalFile.name.replace(/\.[^/.]+$/, '');
    const dlBtn = document.getElementById('imgresize-download-btn');
    if (dlBtn) {
      dlBtn.href = URL.createObjectURL(blob);
      dlBtn.download = `${baseName}-${w}x${h}.${ext}`;
    }

    const resultCard = document.getElementById('imgresize-result');
    if (resultCard) resultCard.style.display = 'block';
  }, format, 0.9);
}

function resetImageResizer() {
  imgResizeLoadedImage = null;
  imgResizeOriginalFile = null;
  const input = document.getElementById('imgresize-input');
  if (input) input.value = '';
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

function handleJpgToPngFile(file) {
  const errEl = document.getElementById('jpg2png-error');
  const controls = document.getElementById('jpg2png-controls');
  const actions = document.getElementById('jpg2png-action-row');

  if (errEl) errEl.style.display = 'none';
  if (!file) return;

  jpg2PngOriginalFile = file;
  const reader = new FileReader();
  reader.onload = e => {
    const img = new Image();
    img.onload = () => {
      jpg2PngLoadedImage = img;
      document.getElementById('jpg2png-filename').textContent = file.name;
      document.getElementById('jpg2png-orig-size').textContent = formatBytes(file.size);
      document.getElementById('jpg2png-orig-dims').textContent = `${img.naturalWidth} × ${img.naturalHeight} px`;

      if (controls) controls.style.display = 'block';
      if (actions) actions.style.display = 'flex';
      runJpgToPng();
    };
    img.src = e.target.result;
  };
  reader.readAsDataURL(file);
}

function runJpgToPng() {
  if (!jpg2PngLoadedImage || !jpg2PngOriginalFile) return;

  const canvas = document.createElement('canvas');
  canvas.width = jpg2PngLoadedImage.naturalWidth;
  canvas.height = jpg2PngLoadedImage.naturalHeight;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(jpg2PngLoadedImage, 0, 0);

  canvas.toBlob(blob => {
    if (!blob) return;

    document.getElementById('jpg2png-res-size').textContent = formatBytes(blob.size);

    const preview = document.getElementById('jpg2png-preview');
    if (preview) preview.src = URL.createObjectURL(blob);

    const baseName = jpg2PngOriginalFile.name.replace(/\.[^/.]+$/, '');
    const dlBtn = document.getElementById('jpg2png-download-btn');
    if (dlBtn) {
      dlBtn.href = URL.createObjectURL(blob);
      dlBtn.download = `${baseName}.png`;
    }

    const resultCard = document.getElementById('jpg2png-result');
    if (resultCard) resultCard.style.display = 'block';
    showToast('✓ Converted to PNG!');
  }, 'image/png');
}

function resetJpgToPng() {
  jpg2PngLoadedImage = null;
  jpg2PngOriginalFile = null;
  const input = document.getElementById('jpg2png-input');
  if (input) input.value = '';
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

function handlePngToJpgFile(file) {
  const errEl = document.getElementById('png2jpg-error');
  const controls = document.getElementById('png2jpg-controls');
  const actions = document.getElementById('png2jpg-action-row');

  if (errEl) errEl.style.display = 'none';
  if (!file) return;

  png2JpgOriginalFile = file;
  const reader = new FileReader();
  reader.onload = e => {
    const img = new Image();
    img.onload = () => {
      png2JpgLoadedImage = img;
      document.getElementById('png2jpg-filename').textContent = file.name;
      document.getElementById('png2jpg-orig-size').textContent = formatBytes(file.size);
      document.getElementById('png2jpg-orig-dims').textContent = `${img.naturalWidth} × ${img.naturalHeight} px`;

      if (controls) controls.style.display = 'block';
      if (actions) actions.style.display = 'flex';
      runPngToJpg();
    };
    img.src = e.target.result;
  };
  reader.readAsDataURL(file);
}

function updatePng2JpgBg(hex) {
  const badge = document.getElementById('png2jpg-bg-hex');
  if (badge) badge.textContent = hex;
  runPngToJpg();
}

function updatePng2JpgQuality(val) {
  const qVal = document.getElementById('png2jpg-quality-val');
  if (qVal) qVal.textContent = val + '%';
  runPngToJpg();
}

function runPngToJpg() {
  if (!png2JpgLoadedImage || !png2JpgOriginalFile) return;

  const bgColor = document.getElementById('png2jpg-bg-color').value || '#ffffff';
  const quality = parseInt(document.getElementById('png2jpg-quality').value, 10) / 100;

  const canvas = document.createElement('canvas');
  canvas.width = png2JpgLoadedImage.naturalWidth;
  canvas.height = png2JpgLoadedImage.naturalHeight;
  const ctx = canvas.getContext('2d');

  // Fill background for transparency
  ctx.fillStyle = bgColor;
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.drawImage(png2JpgLoadedImage, 0, 0);

  canvas.toBlob(blob => {
    if (!blob) return;

    const originalSize = png2JpgOriginalFile.size;
    const newSize = blob.size;
    const reduction = Math.max(0, Math.round(((originalSize - newSize) / originalSize) * 100));

    document.getElementById('png2jpg-res-orig').textContent = formatBytes(originalSize);
    document.getElementById('png2jpg-res-new').textContent = formatBytes(newSize);
    document.getElementById('png2jpg-res-reduction').textContent = `-${reduction}%`;

    const preview = document.getElementById('png2jpg-preview');
    if (preview) preview.src = URL.createObjectURL(blob);

    const baseName = png2JpgOriginalFile.name.replace(/\.[^/.]+$/, '');
    const dlBtn = document.getElementById('png2jpg-download-btn');
    if (dlBtn) {
      dlBtn.href = URL.createObjectURL(blob);
      dlBtn.download = `${baseName}.jpg`;
    }

    const resultCard = document.getElementById('png2jpg-result');
    if (resultCard) resultCard.style.display = 'block';
    showToast('✓ Converted to JPG!');
  }, 'image/jpeg', quality);
}

function resetPngToJpg() {
  png2JpgLoadedImage = null;
  png2JpgOriginalFile = null;
  const input = document.getElementById('png2jpg-input');
  if (input) input.value = '';
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
let imgCropCurrentRatio = 'free'; // 'free', '1:1', '4:3', '16:9'

function handleImageCropperFile(file) {
  const errEl = document.getElementById('imgcrop-error');
  const controls = document.getElementById('imgcrop-controls');
  const actions = document.getElementById('imgcrop-action-row');

  if (errEl) errEl.style.display = 'none';
  if (!file) return;

  imgCropOriginalFile = file;
  const reader = new FileReader();
  reader.onload = e => {
    const img = new Image();
    img.onload = () => {
      imgCropLoadedImage = img;
      if (controls) controls.style.display = 'block';
      if (actions) actions.style.display = 'flex';
      drawCropCanvas();
    };
    img.src = e.target.result;
  };
  reader.readAsDataURL(file);
}

function setCropRatio(ratio) {
  imgCropCurrentRatio = ratio;
  ['free', '1-1', '4-3', '16-9'].forEach(r => {
    const btn = document.getElementById(`crop-ratio-${r}`);
    if (btn) {
      if (r === ratio.replace(':', '-')) btn.classList.add('active');
      else btn.classList.remove('active');
    }
  });
  drawCropCanvas();
}

function onCropParamChange() {
  drawCropCanvas();
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
    // Freeform
    cropW = imgW * sizeVal;
    cropH = imgH * sizeVal;
  }

  const maxOffsetX = imgW - cropW;
  const maxOffsetY = imgH - cropH;
  const x = Math.max(0, Math.min(maxOffsetX, maxOffsetX * posXVal));
  const y = Math.max(0, Math.min(maxOffsetY, maxOffsetY * posYVal));

  return { x: Math.round(x), y: Math.round(y), w: Math.round(cropW), h: Math.round(cropH) };
}

function drawCropCanvas() {
  if (!imgCropLoadedImage) return;

  const canvas = document.getElementById('imgcrop-canvas');
  if (!canvas) return;

  const wrapWidth = Math.min(canvas.parentElement.clientWidth || 400, 600);
  const displayScale = wrapWidth / imgCropLoadedImage.naturalWidth;
  canvas.width = wrapWidth;
  canvas.height = imgCropLoadedImage.naturalHeight * displayScale;

  const ctx = canvas.getContext('2d');
  // Draw base image
  ctx.drawImage(imgCropLoadedImage, 0, 0, canvas.width, canvas.height);

  // Overlay semi-transparent dark mask
  ctx.fillStyle = 'rgba(0, 0, 0, 0.55)';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Clear crop box hole
  const box = getCropBox();
  const cX = box.x * displayScale;
  const cY = box.y * displayScale;
  const cW = box.w * displayScale;
  const cH = box.h * displayScale;

  ctx.clearRect(cX, cY, cW, cH);
  ctx.drawImage(imgCropLoadedImage, box.x, box.y, box.w, box.h, cX, cY, cW, cH);

  // Draw crop boundary outline
  ctx.strokeStyle = '#2563eb';
  ctx.lineWidth = 2;
  ctx.strokeRect(cX, cY, cW, cH);

  // Draw rule of thirds lines
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
  if (!imgCropLoadedImage || !imgCropOriginalFile) return;

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

    document.getElementById('imgcrop-res-dims').textContent = `${box.w} × ${box.h}`;
    document.getElementById('imgcrop-res-ratio').textContent = imgCropCurrentRatio;
    document.getElementById('imgcrop-res-size').textContent = formatBytes(blob.size);

    const preview = document.getElementById('imgcrop-preview');
    if (preview) preview.src = URL.createObjectURL(blob);

    const ext = format === 'image/png' ? 'png' : 'jpg';
    const baseName = imgCropOriginalFile.name.replace(/\.[^/.]+$/, '');
    const dlBtn = document.getElementById('imgcrop-download-btn');
    if (dlBtn) {
      dlBtn.href = URL.createObjectURL(blob);
      dlBtn.download = `${baseName}-cropped.${ext}`;
    }

    const resultCard = document.getElementById('imgcrop-result');
    if (resultCard) resultCard.style.display = 'block';
    showToast('✓ Image cropped successfully!');
  }, format, 0.92);
}

function resetImageCropper() {
  imgCropLoadedImage = null;
  imgCropOriginalFile = null;
  const input = document.getElementById('imgcrop-input');
  if (input) input.value = '';
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

function handleImageToWebpFile(file) {
  const errEl = document.getElementById('img2webp-error');
  const controls = document.getElementById('img2webp-controls');
  const actions = document.getElementById('img2webp-action-row');

  if (errEl) errEl.style.display = 'none';
  if (!file) return;

  img2WebpOriginalFile = file;
  const reader = new FileReader();
  reader.onload = e => {
    const img = new Image();
    img.onload = () => {
      img2WebpLoadedImage = img;
      document.getElementById('img2webp-filename').textContent = file.name;
      document.getElementById('img2webp-orig-size').textContent = formatBytes(file.size);
      document.getElementById('img2webp-orig-dims').textContent = `${img.naturalWidth} × ${img.naturalHeight} px`;

      if (controls) controls.style.display = 'block';
      if (actions) actions.style.display = 'flex';
      runImageToWebp();
    };
    img.src = e.target.result;
  };
  reader.readAsDataURL(file);
}

function updateWebpQuality(val) {
  const qVal = document.getElementById('img2webp-quality-val');
  if (qVal) qVal.textContent = val + '%';
  runImageToWebp();
}

function runImageToWebp() {
  if (!img2WebpLoadedImage || !img2WebpOriginalFile) return;

  const quality = parseInt(document.getElementById('img2webp-quality').value, 10) / 100;

  const canvas = document.createElement('canvas');
  canvas.width = img2WebpLoadedImage.naturalWidth;
  canvas.height = img2WebpLoadedImage.naturalHeight;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(img2WebpLoadedImage, 0, 0);

  canvas.toBlob(blob => {
    if (!blob) return;

    const originalSize = img2WebpOriginalFile.size;
    const newSize = blob.size;
    const savedPct = Math.max(0, Math.round(((originalSize - newSize) / originalSize) * 100));

    document.getElementById('img2webp-res-orig').textContent = formatBytes(originalSize);
    document.getElementById('img2webp-res-new').textContent = formatBytes(newSize);
    document.getElementById('img2webp-res-saved').textContent = `-${savedPct}%`;

    const preview = document.getElementById('img2webp-preview');
    if (preview) preview.src = URL.createObjectURL(blob);

    const baseName = img2WebpOriginalFile.name.replace(/\.[^/.]+$/, '');
    const dlBtn = document.getElementById('img2webp-download-btn');
    if (dlBtn) {
      dlBtn.href = URL.createObjectURL(blob);
      dlBtn.download = `${baseName}.webp`;
    }

    const resultCard = document.getElementById('img2webp-result');
    if (resultCard) resultCard.style.display = 'block';
    showToast('✓ Converted to WebP!');
  }, 'image/webp', quality);
}

function resetImageToWebp() {
  img2WebpLoadedImage = null;
  img2WebpOriginalFile = null;
  const input = document.getElementById('img2webp-input');
  if (input) input.value = '';
  const controls = document.getElementById('img2webp-controls');
  if (controls) controls.style.display = 'none';
  const actions = document.getElementById('img2webp-action-row');
  if (actions) actions.style.display = 'none';
  const resultCard = document.getElementById('img2webp-result');
  if (resultCard) resultCard.style.display = 'none';
  const errEl = document.getElementById('img2webp-error');
  if (errEl) errEl.style.display = 'none';
}
'''
