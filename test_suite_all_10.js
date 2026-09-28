const fs = require('fs');
const { JSDOM } = require('jsdom');

console.log('====================================================');
console.log('VERIFYING ACTUAL WORKFLOW FOR ALL 10 TOOLS');
console.log('====================================================');

const html = fs.readFileSync('index.html', 'utf8');
const scriptContent = fs.readFileSync('script.js', 'utf8');

const dom = new JSDOM(html, {
  url: 'https://ais-dev-vatqw65fky76dekso6xcwb-447578213146.asia-southeast1.run.app/',
  runScripts: 'outside-only'
});

const window = dom.window;
window.matchMedia = window.matchMedia || function() {
  return { matches: false, addListener: function() {}, removeListener: function() {} };
};

// Canvas Mocking
window.HTMLCanvasElement.prototype.toBlob = function(callback, type, quality) {
  setTimeout(() => {
    callback(new window.Blob([`fake-${type || 'image/png'}-data`], { type: type || 'image/png' }));
  }, 5);
};
window.HTMLCanvasElement.prototype.getContext = function() {
  return {
    drawImage: () => {},
    fillRect: () => {},
    clearRect: () => {},
    beginPath: () => {},
    moveTo: () => {},
    lineTo: () => {},
    stroke: () => {},
    strokeRect: () => {},
    getImageData: () => ({ data: new Uint8ClampedArray(4) }),
    putImageData: () => {},
    fillStyle: '#fff',
    strokeStyle: '#000',
    lineWidth: 1
  };
};

// Polyfill URL
window.URL.createObjectURL = (blob) => 'blob:https://app/' + Math.random().toString(36).slice(2);
window.URL.revokeObjectURL = () => {};

// Mock Image
window.Image = class {
  constructor() {
    this.naturalWidth = 1200;
    this.naturalHeight = 800;
    this.complete = true;
    setTimeout(() => {
      if (this.onload) this.onload();
    }, 5);
  }
};

// Mock PDFLib in window for PDF tools
const PDFLib = require('./assets/lib/pdf-lib.min.js');
window.PDFLib = PDFLib;

// Mock pdfjsLib for PDF to Images
window.pdfjsLib = {
  GlobalWorkerOptions: {},
  getDocument: () => ({
    promise: Promise.resolve({
      numPages: 2,
      getPage: (num) => Promise.resolve({
        getViewport: () => ({ width: 600, height: 800 }),
        render: () => ({ promise: Promise.resolve() })
      })
    })
  })
};

// Evaluate script.js
window.eval(scriptContent);

const results = [];

async function runTests() {
  // 1. PNG to JPG
  try {
    const file = new window.File(['fake png'], 'my_graphic.png', { type: 'image/png' });
    window.handlePngToJpgFile(file);
    const card = window.document.getElementById('png2jpg-selected-card');
    const controls = window.document.getElementById('png2jpg-controls');
    const actions = window.document.getElementById('png2jpg-action-row');
    const fileDetected = card.style.display === 'flex' && controls.style.display === 'block' && actions.style.display === 'flex';
    
    await window.runPngToJpg();
    await new Promise(r => setTimeout(r, 30));
    const resultCard = window.document.getElementById('png2jpg-result');
    const preview = window.document.getElementById('png2jpg-preview');
    const processed = resultCard.style.display === 'block' && preview.src.startsWith('blob:');
    
    const download = !!window.png2JpgResultBlob;
    window.downloadPngToJpg();

    window.resetPngToJpg();
    const reset = card.style.display === 'none' && resultCard.style.display === 'none';

    results.push({ tool: 'PNG to JPG Converter', select: fileDetected, process: processed, result: processed, download, status: (fileDetected && processed && download && reset) ? 'PASS' : 'FAIL' });
  } catch(e) {
    results.push({ tool: 'PNG to JPG Converter', select: false, process: false, result: false, download: false, status: 'FAIL: ' + e.message });
  }

  // 2. JPG to PNG
  try {
    const file = new window.File(['fake jpg'], 'photo.jpg', { type: 'image/jpeg' });
    window.handleJpgToPngFile(file);
    const card = window.document.getElementById('jpg2png-selected-card');
    const fileDetected = card.style.display === 'flex';

    await window.runJpgToPng();
    await new Promise(r => setTimeout(r, 30));
    const resultCard = window.document.getElementById('jpg2png-result');
    const processed = resultCard.style.display === 'block';

    const download = !!window.jpg2PngResultBlob;
    window.downloadJpgToPng();

    window.resetJpgToPng();
    results.push({ tool: 'JPG to PNG Converter', select: fileDetected, process: processed, result: processed, download, status: (fileDetected && processed && download) ? 'PASS' : 'FAIL' });
  } catch(e) {
    results.push({ tool: 'JPG to PNG Converter', select: false, process: false, result: false, download: false, status: 'FAIL: ' + e.message });
  }

  // 3. Image Compressor
  try {
    const file = new window.File(['fake img'], 'large_photo.jpg', { type: 'image/jpeg' });
    window.handleImageCompressorFile(file);
    const card = window.document.getElementById('imgcomp-selected-card');
    const fileDetected = card.style.display === 'flex';

    await window.runImageCompression();
    await new Promise(r => setTimeout(r, 30));
    const resultCard = window.document.getElementById('imgcomp-result');
    const processed = resultCard.style.display === 'block';

    const download = !!window.imgCompResultBlob;
    window.downloadCompressedImage();

    window.resetImageCompressor();
    results.push({ tool: 'Image Compressor', select: fileDetected, process: processed, result: processed, download, status: (fileDetected && processed && download) ? 'PASS' : 'FAIL' });
  } catch(e) {
    results.push({ tool: 'Image Compressor', select: false, process: false, result: false, download: false, status: 'FAIL: ' + e.message });
  }

  // 4. Image Resizer
  try {
    const file = new window.File(['fake img'], 'photo.png', { type: 'image/png' });
    window.handleImageResizerFile(file);
    const card = window.document.getElementById('imgresize-selected-card');
    const fileDetected = card.style.display === 'flex';

    await new Promise(r => setTimeout(r, 15));
    await window.runImageResize();
    await new Promise(r => setTimeout(r, 30));
    const resultCard = window.document.getElementById('imgresize-result');
    const processed = resultCard.style.display === 'block';

    const download = !!window.imgResizeResultBlob;
    window.downloadResizedImage();

    window.resetImageResizer();
    results.push({ tool: 'Image Resizer', select: fileDetected, process: processed, result: processed, download, status: (fileDetected && processed && download) ? 'PASS' : 'FAIL' });
  } catch(e) {
    results.push({ tool: 'Image Resizer', select: false, process: false, result: false, download: false, status: 'FAIL: ' + e.message });
  }

  // 5. Image Cropper
  try {
    const file = new window.File(['fake img'], 'avatar.jpg', { type: 'image/jpeg' });
    window.handleImageCropperFile(file);
    const card = window.document.getElementById('imgcrop-selected-card');
    const fileDetected = card.style.display === 'flex';

    await new Promise(r => setTimeout(r, 15));
    await window.runImageCrop();
    await new Promise(r => setTimeout(r, 30));
    const resultCard = window.document.getElementById('imgcrop-result');
    const processed = resultCard.style.display === 'block';

    const download = !!window.imgCropResultBlob;
    window.downloadCroppedImage();

    window.resetImageCropper();
    results.push({ tool: 'Image Cropper', select: fileDetected, process: processed, result: processed, download, status: (fileDetected && processed && download) ? 'PASS' : 'FAIL' });
  } catch(e) {
    results.push({ tool: 'Image Cropper', select: false, process: false, result: false, download: false, status: 'FAIL: ' + e.message });
  }

  // 6. Image to WebP
  try {
    const file = new window.File(['fake img'], 'nature.jpg', { type: 'image/jpeg' });
    window.handleImageToWebpFile(file);
    const card = window.document.getElementById('img2webp-selected-card');
    const fileDetected = card.style.display === 'flex';

    await window.runImageToWebp();
    await new Promise(r => setTimeout(r, 30));
    const resultCard = window.document.getElementById('img2webp-result');
    const processed = resultCard.style.display === 'block';

    const download = !!window.img2WebpResultBlob;
    window.downloadWebpImage();

    window.resetImageToWebp();
    results.push({ tool: 'Image to WebP Converter', select: fileDetected, process: processed, result: processed, download, status: (fileDetected && processed && download) ? 'PASS' : 'FAIL' });
  } catch(e) {
    results.push({ tool: 'Image to WebP Converter', select: false, process: false, result: false, download: false, status: 'FAIL: ' + e.message });
  }

  // 7. PDF Merge
  try {
    const doc1 = await PDFLib.PDFDocument.create();
    doc1.addPage();
    const b1 = await doc1.save();
    const f1 = new window.File([b1], 'doc1.pdf', { type: 'application/pdf' });
    f1.arrayBuffer = () => Promise.resolve(b1.buffer);

    const doc2 = await PDFLib.PDFDocument.create();
    doc2.addPage();
    const b2 = await doc2.save();
    const f2 = new window.File([b2], 'doc2.pdf', { type: 'application/pdf' });
    f2.arrayBuffer = () => Promise.resolve(b2.buffer);

    window.handlePdfMergeFiles([f1, f2]);
    const listContainer = window.document.getElementById('pdf-merge-list-container');
    const fileDetected = listContainer.style.display === 'block';

    await window.processPdfMerge();
    const resultCard = window.document.getElementById('pdf-merge-result');
    const processed = resultCard.style.display === 'block';

    const download = !!window.pdfMergeResultBlob;
    window.downloadMergedPdf();

    window.resetPdfMerge();
    results.push({ tool: 'PDF Merge', select: fileDetected, process: processed, result: processed, download, status: (fileDetected && processed && download) ? 'PASS' : 'FAIL' });
  } catch(e) {
    results.push({ tool: 'PDF Merge', select: false, process: false, result: false, download: false, status: 'FAIL: ' + e.message });
  }

  // 8. PDF Split
  try {
    const doc = await PDFLib.PDFDocument.create();
    doc.addPage();
    doc.addPage();
    doc.addPage();
    const bytes = await doc.save();
    const f = new window.File([bytes], 'book.pdf', { type: 'application/pdf' });
    f.arrayBuffer = () => Promise.resolve(bytes.buffer);

    await window.handlePdfSplitFile(f);
    const summary = window.document.getElementById('pdf-split-summary');
    const fileDetected = summary.style.display === 'flex';

    await window.processPdfSplit();
    const resultCard = window.document.getElementById('pdf-split-result');
    const processed = resultCard.style.display === 'block';

    const download = !!window.pdfSplitResultBlob;
    window.downloadSplitPdf();

    window.resetPdfSplit();
    results.push({ tool: 'PDF Split', select: fileDetected, process: processed, result: processed, download, status: (fileDetected && processed && download) ? 'PASS' : 'FAIL' });
  } catch(e) {
    results.push({ tool: 'PDF Split', select: false, process: false, result: false, download: false, status: 'FAIL: ' + e.message });
  }

  // 9. PDF to Images
  try {
    const doc = await PDFLib.PDFDocument.create();
    doc.addPage();
    const bytes = await doc.save();
    const f = new window.File([bytes], 'slides.pdf', { type: 'application/pdf' });
    f.arrayBuffer = () => Promise.resolve(bytes.buffer);

    await window.handlePdfToImagesFile(f);
    const summary = window.document.getElementById('pdf2img-summary');
    const fileDetected = summary.style.display === 'flex';

    await window.processPdfToImages();
    await new Promise(r => setTimeout(r, 40));
    const resultCard = window.document.getElementById('pdf2img-results');
    const gallery = window.document.getElementById('pdf2img-gallery');
    const processed = resultCard.style.display === 'block' && gallery.children.length > 0;

    const download = window.pdf2ImgRenderedBlobs && window.pdf2ImgRenderedBlobs.length > 0;
    window.downloadPdfPageImage(0);

    window.resetPdfToImages();
    results.push({ tool: 'PDF to Images', select: fileDetected, process: processed, result: processed, download, status: (fileDetected && processed && download) ? 'PASS' : 'FAIL' });
  } catch(e) {
    results.push({ tool: 'PDF to Images', select: false, process: false, result: false, download: false, status: 'FAIL: ' + e.message });
  }

  // 10. Images to PDF
  try {
    const f1 = new window.File(['fake img'], 'img1.jpg', { type: 'image/jpeg' });
    const f2 = new window.File(['fake img'], 'img2.png', { type: 'image/png' });

    window.handleImagesToPdfFiles([f1, f2]);
    const controls = window.document.getElementById('img2pdf-controls');
    const fileDetected = controls.style.display === 'block';

    // Mock embedPng for this test
    const origEmbed = window.PDFLib.PDFDocument.prototype.embedPng;
    window.PDFLib.PDFDocument.prototype.embedPng = function() {
      return Promise.resolve({ width: 100, height: 100 });
    };

    await window.processImagesToPdf();
    const resultCard = window.document.getElementById('img2pdf-result');
    const processed = resultCard.style.display === 'block';

    const download = !!window.img2PdfResultBlob;
    window.downloadImagesPdf();

    window.resetImagesToPdf();
    results.push({ tool: 'Images to PDF', select: fileDetected, process: processed, result: processed, download, status: (fileDetected && processed && download) ? 'PASS' : 'FAIL' });
  } catch(e) {
    results.push({ tool: 'Images to PDF', select: false, process: false, result: false, download: false, status: 'FAIL: ' + e.message });
  }

  console.table(results);
}

runTests();
