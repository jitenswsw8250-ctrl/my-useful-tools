import re
import os
import shutil
import importlib.util

print("1. Loading existing prose & SEO sections...")

spec1 = importlib.util.spec_from_file_location('h1', 'tools_pdf_image_html.py')
m1 = importlib.util.module_from_spec(spec1)
spec1.loader.exec_module(m1)

spec2 = importlib.util.spec_from_file_location('h2', 'tools_pdf_image_html_2.py')
m2 = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(m2)

existing_all = {**m1.TOOLS_HTML, **m2.TOOLS_HTML_2}

def extract_tail(tool_id):
    h = existing_all[tool_id]
    idx = h.find('<!-- Copy & Share Result Actions -->')
    if idx == -1:
        raise ValueError(f"Could not find copy actions marker in {tool_id}")
    return h[idx:]

# Define Interactive Card HTML for each tool
INTERACTIVE_HTML = {
    'pdf-merge': '''    <section id="screen-pdf-merge" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">PDF Merge</h1>
        <p class="tool-page-subtitle">Combine multiple PDF documents into a single organized file with reorder control. 100% private and browser-based.</p>
        <button type="button" class="header-fav-btn" data-tool-id="pdf-merge" onclick="toggleFavorite('pdf-merge', event)" aria-label="Toggle Favorite" title="Favorite"><span class="header-fav-star">☆</span> <span class="header-fav-text">Favorite</span></button>
      </div>

      <div class="card">
        <div class="privacy-notice-box">
          <span class="privacy-icon">🔒</span>
          <span><strong>Privacy Note:</strong> Your files are processed locally in your browser and are not uploaded to our server.</span>
        </div>

        <!-- File Upload / Dropzone -->
        <div class="file-dropzone" id="pdf-merge-dropzone" onclick="document.getElementById('pdf-merge-input').click()">
          <input type="file" id="pdf-merge-input" accept="application/pdf,.pdf" multiple style="display:none;" onclick="event.stopPropagation(); this.value = null;" onchange="handlePdfMergeFiles(this.files)">
          <div class="dropzone-icon">📑</div>
          <div class="dropzone-text"><strong>Choose PDF files</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Select 2 or more PDF documents to merge</div>
        </div>

        <!-- Selected Files List -->
        <div id="pdf-merge-list-container" class="file-list-container" style="display:none;">
          <div class="file-list-header">
            <span class="file-list-title">Selected PDF Files (<span id="pdf-merge-count">0</span>)</span>
            <button type="button" class="btn-text-sm" onclick="document.getElementById('pdf-merge-input').click()">+ Add More PDFs</button>
          </div>
          <div id="pdf-merge-file-list" class="file-item-list"></div>
        </div>

        <!-- Feedback Banners -->
        <div id="pdf-merge-error" class="error-banner" style="display:none; margin-top: 12px;"></div>
        <div id="pdf-merge-progress" class="status-banner" style="display:none; margin-top: 12px;"></div>

        <!-- Actions Row -->
        <div class="btn-row" id="pdf-merge-action-row" style="display:none; margin-top: 16px;">
          <button type="button" class="btn btn-primary" id="pdf-merge-btn" onclick="processPdfMerge()" disabled>Merge PDFs</button>
          <button type="button" class="btn btn-outline" onclick="resetPdfMerge()">Reset</button>
        </div>

        <!-- Result Card -->
        <div id="pdf-merge-result" class="result-card" style="display:none; margin-top: 20px;">
          <h3 class="result-header">✓ Merged PDF Ready</h3>
          <div class="stat-highlight">
            <div class="stat-highlight-val text-primary" id="pdf-merge-result-pages">0</div>
            <div class="stat-highlight-label">Total Pages in Merged Document</div>
          </div>
          <div class="comparison-stats-grid" style="margin-top: 12px;">
            <div class="comp-stat-col">
              <span class="comp-stat-label">Files Merged</span>
              <span class="comp-stat-val" id="pdf-merge-result-count">0</span>
            </div>
            <div class="comp-stat-col">
              <span class="comp-stat-label">Output File Size</span>
              <span class="comp-stat-val text-emerald" id="pdf-merge-result-size">0 KB</span>
            </div>
          </div>
          <div style="margin-top: 16px;">
            <button type="button" id="pdf-merge-download-btn" class="btn btn-primary btn-block download-btn" onclick="downloadMergedPdf()">⬇ Download Merged PDF</button>
            <button type="button" class="btn btn-outline btn-block" style="margin-top: 8px;" onclick="resetPdfMerge()">Merge More PDFs</button>
          </div>
        </div>
      </div>
''',

    'pdf-split': '''    <section id="screen-pdf-split" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">PDF Split</h1>
        <p class="tool-page-subtitle">Extract specific page ranges or split single pages from any PDF document. 100% private in your browser.</p>
        <button type="button" class="header-fav-btn" data-tool-id="pdf-split" onclick="toggleFavorite('pdf-split', event)" aria-label="Toggle Favorite" title="Favorite"><span class="header-fav-star">☆</span> <span class="header-fav-text">Favorite</span></button>
      </div>

      <div class="card">
        <div class="privacy-notice-box">
          <span class="privacy-icon">🔒</span>
          <span><strong>Privacy Note:</strong> Your files are processed locally in your browser and are not uploaded to our server.</span>
        </div>

        <!-- File Upload / Dropzone -->
        <div class="file-dropzone" id="pdf-split-dropzone" onclick="document.getElementById('pdf-split-input').click()">
          <input type="file" id="pdf-split-input" accept="application/pdf,.pdf" style="display:none;" onclick="event.stopPropagation(); this.value = null;" onchange="handlePdfSplitFile(this.files[0])">
          <div class="dropzone-icon">✂️</div>
          <div class="dropzone-text"><strong>Choose a PDF file</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Upload any multi-page PDF document to extract pages</div>
        </div>

        <!-- Selected PDF Summary Card -->
        <div id="pdf-split-summary" class="file-summary-card" style="display:none; margin-top: 16px;">
          <div class="file-summary-icon">📄</div>
          <div class="file-summary-info">
            <div class="file-summary-name" id="pdf-split-filename">document.pdf</div>
            <div class="file-summary-meta">Total Pages: <strong class="text-primary" id="pdf-split-total-pages">0</strong> | Size: <span id="pdf-split-filesize">0 KB</span></div>
          </div>
          <button type="button" class="btn-text-sm" onclick="document.getElementById('pdf-split-input').click()">Change PDF</button>
        </div>

        <!-- Split Controls -->
        <div id="pdf-split-controls" style="display:none; margin-top: 18px;">
          <div class="quick-preset-chips">
            <span class="preset-label">Quick Presets:</span>
            <button type="button" class="preset-chip" onclick="setPdfSplitPreset('all')">All Pages</button>
            <button type="button" class="preset-chip" onclick="setPdfSplitPreset('first')">First Page</button>
            <button type="button" class="preset-chip" onclick="setPdfSplitPreset('odd')">Odd Pages</button>
            <button type="button" class="preset-chip" onclick="setPdfSplitPreset('even')">Even Pages</button>
          </div>

          <div class="input-group" style="margin-top: 14px;">
            <label for="pdf-split-range">Page Range to Extract</label>
            <input type="text" id="pdf-split-range" class="form-input" placeholder="e.g. 1-3, 5, 7" oninput="onPdfSplitRangeInput()">
            <span class="input-hint" id="pdf-split-range-hint">Enter individual page numbers or ranges separated by commas (e.g. 1-3, 5).</span>
          </div>
        </div>

        <!-- Feedback Banners -->
        <div id="pdf-split-error" class="error-banner" style="display:none; margin-top: 12px;"></div>
        <div id="pdf-split-progress" class="status-banner" style="display:none; margin-top: 12px;"></div>

        <!-- Actions Row -->
        <div class="btn-row" id="pdf-split-action-row" style="display:none; margin-top: 16px;">
          <button type="button" class="btn btn-primary" id="pdf-split-btn" onclick="processPdfSplit()">Split &amp; Extract PDF</button>
          <button type="button" class="btn btn-outline" onclick="resetPdfSplit()">Reset</button>
        </div>

        <!-- Result Card -->
        <div id="pdf-split-result" class="result-card" style="display:none; margin-top: 20px;">
          <h3 class="result-header">✓ PDF Split Ready</h3>
          <div class="stat-highlight">
            <div class="stat-highlight-val text-primary" id="pdf-split-result-pages">0</div>
            <div class="stat-highlight-label">Pages Extracted</div>
          </div>
          <div class="comparison-stats-grid" style="margin-top: 12px;">
            <div class="comp-stat-col">
              <span class="comp-stat-label">Page Selection</span>
              <span class="comp-stat-val" id="pdf-split-result-range">-</span>
            </div>
            <div class="comp-stat-col">
              <span class="comp-stat-label">Output File Size</span>
              <span class="comp-stat-val text-emerald" id="pdf-split-result-size">0 KB</span>
            </div>
          </div>
          <div style="margin-top: 16px;">
            <button type="button" id="pdf-split-download-btn" class="btn btn-primary btn-block download-btn" onclick="downloadSplitPdf()">⬇ Download Split PDF</button>
            <button type="button" class="btn btn-outline btn-block" style="margin-top: 8px;" onclick="resetPdfSplit()">Split Another PDF</button>
          </div>
        </div>
      </div>
''',

    'pdf-to-images': '''    <section id="screen-pdf-to-images" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">PDF to Images</h1>
        <p class="tool-page-subtitle">Convert multi-page PDF documents into high-resolution JPG or PNG images. Fast and private in your browser.</p>
        <button type="button" class="header-fav-btn" data-tool-id="pdf-to-images" onclick="toggleFavorite('pdf-to-images', event)" aria-label="Toggle Favorite" title="Favorite"><span class="header-fav-star">☆</span> <span class="header-fav-text">Favorite</span></button>
      </div>

      <div class="card">
        <div class="privacy-notice-box">
          <span class="privacy-icon">🔒</span>
          <span><strong>Privacy Note:</strong> Your files are processed locally in your browser and are not uploaded to our server.</span>
        </div>

        <!-- File Upload / Dropzone -->
        <div class="file-dropzone" id="pdf2img-dropzone" onclick="document.getElementById('pdf2img-input').click()">
          <input type="file" id="pdf2img-input" accept="application/pdf,.pdf" style="display:none;" onclick="event.stopPropagation(); this.value = null;" onchange="handlePdfToImagesFile(this.files[0])">
          <div class="dropzone-icon">🖼️</div>
          <div class="dropzone-text"><strong>Choose a PDF file</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Converts PDF pages into JPG or PNG image files</div>
        </div>

        <!-- Selected PDF Summary Card -->
        <div id="pdf2img-summary" class="file-summary-card" style="display:none; margin-top: 16px;">
          <div class="file-summary-icon">📄</div>
          <div class="file-summary-info">
            <div class="file-summary-name" id="pdf2img-filename">document.pdf</div>
            <div class="file-summary-meta">Document Pages: <strong class="text-primary" id="pdf2img-total-pages">0</strong> | Size: <span id="pdf2img-filesize">0 KB</span></div>
          </div>
          <button type="button" class="btn-text-sm" onclick="document.getElementById('pdf2img-input').click()">Change PDF</button>
        </div>

        <!-- Controls -->
        <div id="pdf2img-controls" style="display:none; margin-top: 18px;">
          <div class="input-grid-2">
            <div class="input-group">
              <label for="pdf2img-format">Image Format</label>
              <select id="pdf2img-format" class="form-input">
                <option value="image/jpeg" selected>JPG (Standard - Smaller size)</option>
                <option value="image/png">PNG (Lossless - Sharpest quality)</option>
              </select>
            </div>
            <div class="input-group">
              <label for="pdf2img-quality">Image Resolution (DPI)</label>
              <select id="pdf2img-quality" class="form-input">
                <option value="1.5" selected>Standard (150 DPI)</option>
                <option value="2.0">High Definition (200 DPI)</option>
                <option value="1.0">Compact / Fast (100 DPI)</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Feedback Banners -->
        <div id="pdf2img-error" class="error-banner" style="display:none; margin-top: 12px;"></div>
        <div id="pdf2img-progress" class="status-banner" style="display:none; margin-top: 12px;"></div>

        <!-- Actions Row -->
        <div class="btn-row" id="pdf2img-action-row" style="display:none; margin-top: 16px;">
          <button type="button" class="btn btn-primary" id="pdf2img-btn" onclick="processPdfToImages()">Convert to Images</button>
          <button type="button" class="btn btn-outline" onclick="resetPdfToImages()">Reset</button>
        </div>

        <!-- Results Card -->
        <div id="pdf2img-results" class="result-card" style="display:none; margin-top: 20px;">
          <div class="file-list-header">
            <h3 class="result-header" style="margin-bottom:0;">✓ Converted Images (<span id="pdf2img-rendered-count">0</span>)</h3>
            <button type="button" class="btn btn-primary btn-sm" onclick="downloadAllPdfImages()">⬇ Download All Images</button>
          </div>
          <div id="pdf2img-gallery" class="image-gallery-grid" style="margin-top: 16px;"></div>
          <div style="margin-top: 16px;">
            <button type="button" class="btn btn-outline btn-block" onclick="resetPdfToImages()">Convert Another PDF</button>
          </div>
        </div>
      </div>
''',

    'images-to-pdf': '''    <section id="screen-images-to-pdf" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Images to PDF</h1>
        <p class="tool-page-subtitle">Convert multiple JPG, PNG, and WebP pictures into a single, clean PDF file. Reorder pages and set page fit.</p>
        <button type="button" class="header-fav-btn" data-tool-id="images-to-pdf" onclick="toggleFavorite('images-to-pdf', event)" aria-label="Toggle Favorite" title="Favorite"><span class="header-fav-star">☆</span> <span class="header-fav-text">Favorite</span></button>
      </div>

      <div class="card">
        <div class="privacy-notice-box">
          <span class="privacy-icon">🔒</span>
          <span><strong>Privacy Note:</strong> Your files are processed locally in your browser and are not uploaded to our server.</span>
        </div>

        <!-- File Upload / Dropzone -->
        <div class="file-dropzone" id="img2pdf-dropzone" onclick="document.getElementById('img2pdf-input').click()">
          <input type="file" id="img2pdf-input" accept="image/jpeg,image/png,image/webp,.jpg,.jpeg,.png,.webp" multiple style="display:none;" onclick="event.stopPropagation(); this.value = null;" onchange="handleImagesToPdfFiles(this.files)">
          <div class="dropzone-icon">📸</div>
          <div class="dropzone-text"><strong>Choose Images</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Supports JPG, PNG, and WebP (select 1 or more images)</div>
        </div>

        <!-- Selected Images Container -->
        <div id="img2pdf-controls" style="display:none; margin-top: 18px;">
          <div class="file-list-header">
            <span class="file-list-title">Selected Images (<span id="img2pdf-count">0</span>)</span>
            <button type="button" class="btn-text-sm" onclick="document.getElementById('img2pdf-input').click()">+ Add More Images</button>
          </div>
          <div id="img2pdf-thumbnails" class="file-item-list"></div>

          <div class="input-grid-2" style="margin-top: 14px;">
            <div class="input-group">
              <label for="img2pdf-page-size">Page Layout</label>
              <select id="img2pdf-page-size" class="form-input">
                <option value="fit" selected>Fit to Image Dimensions (Original)</option>
                <option value="a4-portrait">A4 Paper (Portrait)</option>
                <option value="a4-landscape">A4 Paper (Landscape)</option>
              </select>
            </div>
            <div class="input-group">
              <label for="img2pdf-margins">Page Margins</label>
              <select id="img2pdf-margins" class="form-input">
                <option value="0" selected>No Margins (Full Bleed)</option>
                <option value="20">Standard Margin (20 pt)</option>
                <option value="36">Wide Margin (36 pt)</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Feedback Banners -->
        <div id="img2pdf-error" class="error-banner" style="display:none; margin-top: 12px;"></div>
        <div id="img2pdf-progress" class="status-banner" style="display:none; margin-top: 12px;"></div>

        <!-- Actions Row -->
        <div class="btn-row" id="img2pdf-action-row" style="display:none; margin-top: 16px;">
          <button type="button" class="btn btn-primary" id="img2pdf-btn" onclick="processImagesToPdf()">Create PDF</button>
          <button type="button" class="btn btn-outline" onclick="resetImagesToPdf()">Reset</button>
        </div>

        <!-- Result Card -->
        <div id="img2pdf-result" class="result-card" style="display:none; margin-top: 20px;">
          <h3 class="result-header">✓ PDF Created Successfully</h3>
          <div class="stat-highlight">
            <div class="stat-highlight-val text-primary" id="img2pdf-result-pages">0</div>
            <div class="stat-highlight-label">Pages in Generated PDF</div>
          </div>
          <div class="comparison-stats-grid" style="margin-top: 12px;">
            <div class="comp-stat-col">
              <span class="comp-stat-label">Images Compiled</span>
              <span class="comp-stat-val" id="img2pdf-result-count">0</span>
            </div>
            <div class="comp-stat-col">
              <span class="comp-stat-label">Output PDF Size</span>
              <span class="comp-stat-val text-emerald" id="img2pdf-result-size">0 KB</span>
            </div>
          </div>
          <div style="margin-top: 16px;">
            <button type="button" id="img2pdf-download-btn" class="btn btn-primary btn-block download-btn" onclick="downloadImagesPdf()">⬇ Download PDF</button>
            <button type="button" class="btn btn-outline btn-block" style="margin-top: 8px;" onclick="resetImagesToPdf()">Convert More Images</button>
          </div>
        </div>
      </div>
''',

    'image-compressor': '''    <section id="screen-image-compressor" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Image Compressor</h1>
        <p class="tool-page-subtitle">Compress JPG, PNG, and WebP images by up to 90% without visible quality loss. 100% private in your browser.</p>
        <button type="button" class="header-fav-btn" data-tool-id="image-compressor" onclick="toggleFavorite('image-compressor', event)" aria-label="Toggle Favorite" title="Favorite"><span class="header-fav-star">☆</span> <span class="header-fav-text">Favorite</span></button>
      </div>

      <div class="card">
        <div class="privacy-notice-box">
          <span class="privacy-icon">🔒</span>
          <span><strong>Privacy Note:</strong> Your files are processed locally in your browser and are not uploaded to our server.</span>
        </div>

        <!-- File Upload / Dropzone -->
        <div class="file-dropzone" id="imgcomp-dropzone" onclick="document.getElementById('imgcomp-input').click()">
          <input type="file" id="imgcomp-input" accept="image/jpeg,image/png,image/webp,.jpg,.jpeg,.png,.webp" style="display:none;" onclick="event.stopPropagation(); this.value = null;" onchange="handleImageCompressorFile(this.files[0])">
          <div class="dropzone-icon">🗜️</div>
          <div class="dropzone-text"><strong>Choose an image</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Supports JPG, PNG, and WebP images</div>
        </div>

        <!-- Selected Image Card -->
        <div id="imgcomp-selected-card" class="file-summary-card" style="display:none; margin-top: 16px;">
          <img id="imgcomp-selected-thumb" class="file-summary-thumb" alt="Selected Preview">
          <div class="file-summary-info">
            <div class="file-summary-name" id="imgcomp-filename">photo.jpg</div>
            <div class="file-summary-meta">Original Size: <strong class="text-primary" id="imgcomp-orig-size">0 KB</strong> | Resolution: <span id="imgcomp-orig-dims">0 × 0 px</span></div>
          </div>
          <button type="button" class="btn-text-sm" onclick="document.getElementById('imgcomp-input').click()">Change Image</button>
        </div>

        <!-- Compression Controls -->
        <div id="imgcomp-controls" style="display:none; margin-top: 18px;">
          <div class="slider-control-group">
            <div class="slider-header">
              <label for="imgcomp-quality">Compression Quality</label>
              <span class="slider-badge" id="imgcomp-quality-val">75%</span>
            </div>
            <input type="range" id="imgcomp-quality" min="10" max="100" value="75" step="1" oninput="updateCompressorQuality(this.value)">
            <div class="slider-ticks">
              <span>Maximum Compression (10%)</span>
              <span>Balanced (75%)</span>
              <span>Highest Quality (100%)</span>
            </div>
          </div>

          <div class="input-grid-2" style="margin-top: 14px;">
            <div class="input-group">
              <label for="imgcomp-max-width">Max Width Scale (Optional)</label>
              <select id="imgcomp-max-width" class="form-input">
                <option value="original" selected>Keep Original Dimensions</option>
                <option value="1920">1920 px (Full HD)</option>
                <option value="1280">1280 px (HD / Web)</option>
                <option value="800">800 px (Email / Chat)</option>
              </select>
            </div>
            <div class="input-group">
              <label for="imgcomp-format">Output Format</label>
              <select id="imgcomp-format" class="form-input">
                <option value="auto" selected>Keep Original Format</option>
                <option value="image/jpeg">Convert to JPG</option>
                <option value="image/webp">Convert to WebP (Smallest)</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Feedback Banners -->
        <div id="imgcomp-error" class="error-banner" style="display:none; margin-top: 12px;"></div>
        <div id="imgcomp-progress" class="status-banner" style="display:none; margin-top: 12px;"></div>

        <!-- Actions Row -->
        <div class="btn-row" id="imgcomp-action-row" style="display:none; margin-top: 16px;">
          <button type="button" class="btn btn-primary" id="imgcomp-btn" onclick="runImageCompression()">🗜️ Compress Image</button>
          <button type="button" class="btn btn-outline" onclick="resetImageCompressor()">Reset</button>
        </div>

        <!-- Result Card -->
        <div id="imgcomp-result" class="result-card" style="display:none; margin-top: 20px;">
          <h3 class="result-header">✓ Compression Complete</h3>
          <div class="comparison-stats-grid">
            <div class="comp-stat-col">
              <span class="comp-stat-label">Original Size</span>
              <span class="comp-stat-val" id="imgcomp-res-orig">0 KB</span>
            </div>
            <div class="comp-stat-arrow">→</div>
            <div class="comp-stat-col">
              <span class="comp-stat-label">Compressed Size</span>
              <span class="comp-stat-val text-emerald" id="imgcomp-res-new">0 KB</span>
            </div>
            <div class="comp-stat-col">
              <span class="comp-stat-label">Savings</span>
              <span class="comp-stat-badge" id="imgcomp-res-saving">-0%</span>
            </div>
          </div>
          <div class="image-preview-wrapper" style="margin-top: 16px;">
            <img id="imgcomp-preview" class="image-preview-box" alt="Compressed Preview">
          </div>
          <div style="margin-top: 16px;">
            <button type="button" id="imgcomp-download-btn" class="btn btn-primary btn-block download-btn" onclick="downloadCompressedImage()">⬇ Download Compressed Image</button>
            <button type="button" class="btn btn-outline btn-block" style="margin-top: 8px;" onclick="resetImageCompressor()">Compress Another Image</button>
          </div>
        </div>
      </div>
''',

    'image-resizer': '''    <section id="screen-image-resizer" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Image Resizer</h1>
        <p class="tool-page-subtitle">Resize image dimensions by exact pixels or percentage scale with aspect ratio lock. Fast and 100% private in your browser.</p>
        <button type="button" class="header-fav-btn" data-tool-id="image-resizer" onclick="toggleFavorite('image-resizer', event)" aria-label="Toggle Favorite" title="Favorite"><span class="header-fav-star">☆</span> <span class="header-fav-text">Favorite</span></button>
      </div>

      <div class="card">
        <div class="privacy-notice-box">
          <span class="privacy-icon">🔒</span>
          <span><strong>Privacy Note:</strong> Your files are processed locally in your browser and are not uploaded to our server.</span>
        </div>

        <!-- File Upload / Dropzone -->
        <div class="file-dropzone" id="imgresize-dropzone" onclick="document.getElementById('imgresize-input').click()">
          <input type="file" id="imgresize-input" accept="image/jpeg,image/png,image/webp,.jpg,.jpeg,.png,.webp" style="display:none;" onclick="event.stopPropagation(); this.value = null;" onchange="handleImageResizerFile(this.files[0])">
          <div class="dropzone-icon">📐</div>
          <div class="dropzone-text"><strong>Choose an image</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Resize JPG, PNG, or WebP to custom dimensions</div>
        </div>

        <!-- Selected Image Card -->
        <div id="imgresize-selected-card" class="file-summary-card" style="display:none; margin-top: 16px;">
          <img id="imgresize-selected-thumb" class="file-summary-thumb" alt="Selected Preview">
          <div class="file-summary-info">
            <div class="file-summary-name" id="imgresize-filename">image.jpg</div>
            <div class="file-summary-meta">Original: <strong class="text-primary" id="imgresize-orig-dims">0 × 0 px</strong> (<span id="imgresize-orig-ratio">1:1</span>) | Size: <span id="imgresize-orig-size">0 KB</span></div>
          </div>
          <button type="button" class="btn-text-sm" onclick="document.getElementById('imgresize-input').click()">Change Image</button>
        </div>

        <!-- Resizer Controls -->
        <div id="imgresize-controls" style="display:none; margin-top: 18px;">
          <div class="quick-preset-chips">
            <span class="preset-label">Quick Scales:</span>
            <button type="button" class="preset-chip" onclick="applyResizerPreset(0.5)">50% Scale</button>
            <button type="button" class="preset-chip" onclick="applyResizerPreset(0.75)">75% Scale</button>
            <button type="button" class="preset-chip" onclick="applyResizerExact(1920, 1080)">1920×1080 (FHD)</button>
            <button type="button" class="preset-chip" onclick="applyResizerExact(1280, 720)">1280×720 (HD)</button>
            <button type="button" class="preset-chip" onclick="applyResizerExact(1080, 1080)">1080×1080 (Square)</button>
          </div>

          <div class="input-grid-2" style="margin-top: 14px;">
            <div class="input-group">
              <label for="imgresize-width">Width (Pixels)</label>
              <input type="number" id="imgresize-width" class="form-input" min="1" max="10000" oninput="onResizerWidthChange(this.value)">
            </div>
            <div class="input-group">
              <label for="imgresize-height">Height (Pixels)</label>
              <input type="number" id="imgresize-height" class="form-input" min="1" max="10000" oninput="onResizerHeightChange(this.value)">
            </div>
          </div>

          <div style="margin-top: 12px; display: flex; align-items: center; gap: 8px;">
            <input type="checkbox" id="imgresize-lock-ratio" checked onchange="toggleResizerLock(this.checked)" style="width: 18px; height: 18px; accent-color: var(--primary-color);">
            <label for="imgresize-lock-ratio" style="font-size: 0.9rem; cursor: pointer; user-select: none;"><strong>Lock Aspect Ratio</strong> (Proportional scaling)</label>
          </div>
        </div>

        <!-- Feedback Banners -->
        <div id="imgresize-error" class="error-banner" style="display:none; margin-top: 12px;"></div>
        <div id="imgresize-progress" class="status-banner" style="display:none; margin-top: 12px;"></div>

        <!-- Actions Row -->
        <div class="btn-row" id="imgresize-action-row" style="display:none; margin-top: 16px;">
          <button type="button" class="btn btn-primary" id="imgresize-btn" onclick="runImageResize()">📐 Resize Image</button>
          <button type="button" class="btn btn-outline" onclick="resetImageResizer()">Reset</button>
        </div>

        <!-- Result Card -->
        <div id="imgresize-result" class="result-card" style="display:none; margin-top: 20px;">
          <h3 class="result-header">✓ Image Resized Successfully</h3>
          <div class="comparison-stats-grid">
            <div class="comp-stat-col">
              <span class="comp-stat-label">New Dimensions</span>
              <span class="comp-stat-val text-primary" id="imgresize-res-dims">0 × 0 px</span>
            </div>
            <div class="comp-stat-col">
              <span class="comp-stat-label">New File Size</span>
              <span class="comp-stat-val text-emerald" id="imgresize-res-size">0 KB</span>
            </div>
            <div class="comp-stat-col">
              <span class="comp-stat-label">Format</span>
              <span class="comp-stat-val" id="imgresize-res-format">JPG</span>
            </div>
          </div>
          <div class="image-preview-wrapper" style="margin-top: 16px;">
            <img id="imgresize-preview" class="image-preview-box" alt="Resized Preview">
          </div>
          <div style="margin-top: 16px;">
            <button type="button" id="imgresize-download-btn" class="btn btn-primary btn-block download-btn" onclick="downloadResizedImage()">⬇ Download Resized Image</button>
            <button type="button" class="btn btn-outline btn-block" style="margin-top: 8px;" onclick="resetImageResizer()">Resize Another Image</button>
          </div>
        </div>
      </div>
''',

    'jpg-to-png': '''    <section id="screen-jpg-to-png" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">JPG to PNG Converter</h1>
        <p class="tool-page-subtitle">Convert JPG and JPEG images to lossless high-fidelity PNG format with zero quality degradation. Completely client-side.</p>
        <button type="button" class="header-fav-btn" data-tool-id="jpg-to-png" onclick="toggleFavorite('jpg-to-png', event)" aria-label="Toggle Favorite" title="Favorite"><span class="header-fav-star">☆</span> <span class="header-fav-text">Favorite</span></button>
      </div>

      <div class="card">
        <div class="privacy-notice-box">
          <span class="privacy-icon">🔒</span>
          <span><strong>Privacy Note:</strong> Your files are processed locally in your browser and are not uploaded to our server.</span>
        </div>

        <!-- File Upload / Dropzone -->
        <div class="file-dropzone" id="jpg2png-dropzone" onclick="document.getElementById('jpg2png-input').click()">
          <input type="file" id="jpg2png-input" accept=".jpg,.jpeg,image/jpeg" style="display:none;" onclick="event.stopPropagation(); this.value = null;" onchange="handleJpgToPngFile(this.files[0])">
          <div class="dropzone-icon">🔄</div>
          <div class="dropzone-text"><strong>Choose a JPG/JPEG image</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Converts instantly into crisp, lossless PNG format</div>
        </div>

        <!-- Selected Image Card -->
        <div id="jpg2png-selected-card" class="file-summary-card" style="display:none; margin-top: 16px;">
          <img id="jpg2png-selected-thumb" class="file-summary-thumb" alt="Selected Preview">
          <div class="file-summary-info">
            <div class="file-summary-name" id="jpg2png-filename">photo.jpg</div>
            <div class="file-summary-meta">Source: <strong class="text-primary">JPEG</strong> | Size: <span id="jpg2png-orig-size">0 KB</span> | Resolution: <span id="jpg2png-orig-dims">0 × 0 px</span></div>
          </div>
          <button type="button" class="btn-text-sm" onclick="document.getElementById('jpg2png-input').click()">Change Image</button>
        </div>

        <!-- Controls / Info -->
        <div id="jpg2png-controls" style="display:none; margin-top: 18px;">
          <div class="info-callout" style="padding: 12px 14px; background: rgba(37, 99, 235, 0.05); border: 1px solid rgba(37, 99, 235, 0.2); border-radius: 8px; font-size: 0.88rem; color: var(--text-main);">
            ✨ <strong>Lossless Conversion:</strong> Output PNG preserves 100% of pixel details with uncompressed clarity and zero artifacting.
          </div>
        </div>

        <!-- Feedback Banners -->
        <div id="jpg2png-error" class="error-banner" style="display:none; margin-top: 12px;"></div>
        <div id="jpg2png-progress" class="status-banner" style="display:none; margin-top: 12px;"></div>

        <!-- Actions Row -->
        <div class="btn-row" id="jpg2png-action-row" style="display:none; margin-top: 16px;">
          <button type="button" class="btn btn-primary" id="jpg2png-btn" onclick="runJpgToPng()">🖼️ Convert to PNG</button>
          <button type="button" class="btn btn-outline" onclick="resetJpgToPng()">Reset</button>
        </div>

        <!-- Result Card -->
        <div id="jpg2png-result" class="result-card" style="display:none; margin-top: 20px;">
          <h3 class="result-header">✓ Converted to PNG Successfully</h3>
          <div class="comparison-stats-grid">
            <div class="comp-stat-col">
              <span class="comp-stat-label">Output Format</span>
              <span class="comp-stat-val text-primary">PNG (Lossless)</span>
            </div>
            <div class="comp-stat-col">
              <span class="comp-stat-label">PNG File Size</span>
              <span class="comp-stat-val text-emerald" id="jpg2png-res-size">0 KB</span>
            </div>
          </div>
          <div class="image-preview-wrapper" style="margin-top: 16px;">
            <img id="jpg2png-preview" class="image-preview-box" alt="PNG Preview">
          </div>
          <div style="margin-top: 16px;">
            <button type="button" id="jpg2png-download-btn" class="btn btn-primary btn-block download-btn" onclick="downloadJpgToPng()">⬇ Download PNG Image</button>
            <button type="button" class="btn btn-outline btn-block" style="margin-top: 8px;" onclick="resetJpgToPng()">Convert Another JPG</button>
          </div>
        </div>
      </div>
''',

    'png-to-jpg': '''    <section id="screen-png-to-jpg" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">PNG to JPG Converter</h1>
        <p class="tool-page-subtitle">Transform heavy PNG images into lightweight JPG files. Custom background color selection for transparent areas.</p>
        <button type="button" class="header-fav-btn" data-tool-id="png-to-jpg" onclick="toggleFavorite('png-to-jpg', event)" aria-label="Toggle Favorite" title="Favorite"><span class="header-fav-star">☆</span> <span class="header-fav-text">Favorite</span></button>
      </div>

      <div class="card">
        <div class="privacy-notice-box">
          <span class="privacy-icon">🔒</span>
          <span><strong>Privacy Note:</strong> Your files are processed locally in your browser and are not uploaded to our server.</span>
        </div>

        <!-- File Upload / Dropzone -->
        <div class="file-dropzone" id="png2jpg-dropzone" onclick="document.getElementById('png2jpg-input').click()">
          <input type="file" id="png2jpg-input" accept=".png,image/png" style="display:none;" onclick="event.stopPropagation(); this.value = null;" onchange="handlePngToJpgFile(this.files[0])">
          <div class="dropzone-icon">🎨</div>
          <div class="dropzone-text"><strong>Choose a PNG image</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Converts PNG images to lightweight JPG photos</div>
        </div>

        <!-- Selected Image Card -->
        <div id="png2jpg-selected-card" class="file-summary-card" style="display:none; margin-top: 16px;">
          <img id="png2jpg-selected-thumb" class="file-summary-thumb" alt="Selected Preview">
          <div class="file-summary-info">
            <div class="file-summary-name" id="png2jpg-filename">graphic.png</div>
            <div class="file-summary-meta">Source: <strong class="text-primary">PNG</strong> | Size: <span id="png2jpg-orig-size">0 KB</span> | Resolution: <span id="png2jpg-orig-dims">0 × 0 px</span></div>
          </div>
          <button type="button" class="btn-text-sm" onclick="document.getElementById('png2jpg-input').click()">Change Image</button>
        </div>

        <!-- Controls -->
        <div id="png2jpg-controls" style="display:none; margin-top: 18px;">
          <div class="input-group">
            <label for="png2jpg-bg-color">Background Color (For Transparent Areas)</label>
            <div class="color-picker-row">
              <input type="color" id="png2jpg-bg-color" value="#ffffff" onchange="updatePng2JpgBg(this.value)">
              <span class="color-hex-badge" id="png2jpg-bg-hex">#FFFFFF (White)</span>
            </div>
            <span class="input-hint">Since JPG doesn't support transparency, transparent areas will fill with this color.</span>
          </div>

          <div class="slider-control-group" style="margin-top: 14px;">
            <div class="slider-header">
              <label for="png2jpg-quality">Output JPEG Quality</label>
              <span class="slider-badge" id="png2jpg-quality-val">85%</span>
            </div>
            <input type="range" id="png2jpg-quality" min="10" max="100" value="85" step="1" oninput="updatePng2JpgQuality(this.value)">
            <div class="slider-ticks">
              <span>High Compression (50%)</span>
              <span>Recommended (85%)</span>
              <span>Maximum (100%)</span>
            </div>
          </div>
        </div>

        <!-- Feedback Banners -->
        <div id="png2jpg-error" class="error-banner" style="display:none; margin-top: 12px;"></div>
        <div id="png2jpg-progress" class="status-banner" style="display:none; margin-top: 12px;"></div>

        <!-- Actions Row -->
        <div class="btn-row" id="png2jpg-action-row" style="display:none; margin-top: 16px;">
          <button type="button" class="btn btn-primary" id="png2jpg-btn" onclick="runPngToJpg()">🖼️ Convert to JPG</button>
          <button type="button" class="btn btn-outline" onclick="resetPngToJpg()">Reset</button>
        </div>

        <!-- Result Card -->
        <div id="png2jpg-result" class="result-card" style="display:none; margin-top: 20px;">
          <h3 class="result-header">✓ Converted to JPG Successfully</h3>
          <div class="comparison-stats-grid">
            <div class="comp-stat-col">
              <span class="comp-stat-label">Original PNG</span>
              <span class="comp-stat-val" id="png2jpg-res-orig">0 KB</span>
            </div>
            <div class="comp-stat-arrow">→</div>
            <div class="comp-stat-col">
              <span class="comp-stat-label">Converted JPG</span>
              <span class="comp-stat-val text-emerald" id="png2jpg-res-new">0 KB</span>
            </div>
            <div class="comp-stat-col">
              <span class="comp-stat-label">Reduction</span>
              <span class="comp-stat-badge" id="png2jpg-res-reduction">-0%</span>
            </div>
          </div>
          <div class="image-preview-wrapper" style="margin-top: 16px;">
            <img id="png2jpg-preview" class="image-preview-box" alt="JPG Preview">
          </div>
          <div style="margin-top: 16px;">
            <button type="button" id="png2jpg-download-btn" class="btn btn-primary btn-block download-btn" onclick="downloadPngToJpg()">⬇ Download JPG Image</button>
            <button type="button" class="btn btn-outline btn-block" style="margin-top: 8px;" onclick="resetPngToJpg()">Convert Another PNG</button>
          </div>
        </div>
      </div>
''',

    'image-cropper': '''    <section id="screen-image-cropper" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Image Cropper</h1>
        <p class="tool-page-subtitle">Crop photos with preset aspect ratios (1:1, 4:3, 16:9, Freeform) and live interactive preview. Completely client-side.</p>
        <button type="button" class="header-fav-btn" data-tool-id="image-cropper" onclick="toggleFavorite('image-cropper', event)" aria-label="Toggle Favorite" title="Favorite"><span class="header-fav-star">☆</span> <span class="header-fav-text">Favorite</span></button>
      </div>

      <div class="card">
        <div class="privacy-notice-box">
          <span class="privacy-icon">🔒</span>
          <span><strong>Privacy Note:</strong> Your files are processed locally in your browser and are not uploaded to our server.</span>
        </div>

        <!-- File Upload / Dropzone -->
        <div class="file-dropzone" id="imgcrop-dropzone" onclick="document.getElementById('imgcrop-input').click()">
          <input type="file" id="imgcrop-input" accept="image/jpeg,image/png,image/webp,.jpg,.jpeg,.png,.webp" style="display:none;" onclick="event.stopPropagation(); this.value = null;" onchange="handleImageCropperFile(this.files[0])">
          <div class="dropzone-icon">✂️</div>
          <div class="dropzone-text"><strong>Choose an image</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Crop JPG, PNG, or WebP pictures to custom ratios</div>
        </div>

        <!-- Selected Image Card -->
        <div id="imgcrop-selected-card" class="file-summary-card" style="display:none; margin-top: 16px;">
          <img id="imgcrop-selected-thumb" class="file-summary-thumb" alt="Selected Preview">
          <div class="file-summary-info">
            <div class="file-summary-name" id="imgcrop-filename">photo.jpg</div>
            <div class="file-summary-meta">Dimensions: <strong class="text-primary" id="imgcrop-orig-dims">0 × 0 px</strong> | Size: <span id="imgcrop-orig-size">0 KB</span></div>
          </div>
          <button type="button" class="btn-text-sm" onclick="document.getElementById('imgcrop-input').click()">Change Image</button>
        </div>

        <!-- Crop Controls -->
        <div id="imgcrop-controls" style="display:none; margin-top: 18px;">
          <div class="aspect-ratio-selector">
            <span class="aspect-label">Aspect Ratio:</span>
            <div class="aspect-tabs">
              <button type="button" class="tab-btn active" id="crop-ratio-free" onclick="setCropRatio('free')">Freeform</button>
              <button type="button" class="tab-btn" id="crop-ratio-1-1" onclick="setCropRatio('1:1')">1:1 Square</button>
              <button type="button" class="tab-btn" id="crop-ratio-4-3" onclick="setCropRatio('4:3')">4:3 Standard</button>
              <button type="button" class="tab-btn" id="crop-ratio-16-9" onclick="setCropRatio('16:9')">16:9 Banner</button>
            </div>
          </div>

          <div class="crop-workspace-container" style="margin-top: 14px;">
            <div class="canvas-crop-wrapper">
              <canvas id="imgcrop-canvas"></canvas>
            </div>
          </div>

          <div class="crop-slider-controls" style="margin-top: 14px;">
            <div class="crop-slider-row">
              <label for="crop-size">Crop Size: <span id="crop-size-val">80%</span></label>
              <input type="range" id="crop-size" min="20" max="100" value="80" oninput="onCropParamChange()">
            </div>
            <div class="crop-slider-row">
              <label for="crop-pos-x">Horizontal Position: <span id="crop-pos-x-val">50%</span></label>
              <input type="range" id="crop-pos-x" min="0" max="100" value="50" oninput="onCropParamChange()">
            </div>
            <div class="crop-slider-row">
              <label for="crop-pos-y">Vertical Position: <span id="crop-pos-y-val">50%</span></label>
              <input type="range" id="crop-pos-y" min="0" max="100" value="50" oninput="onCropParamChange()">
            </div>
            <div style="text-align: right; margin-top: 6px;">
              <button type="button" class="btn-text-sm" onclick="resetCropCenter()">🎯 Center Crop Area</button>
            </div>
          </div>
        </div>

        <!-- Feedback Banners -->
        <div id="imgcrop-error" class="error-banner" style="display:none; margin-top: 12px;"></div>
        <div id="imgcrop-progress" class="status-banner" style="display:none; margin-top: 12px;"></div>

        <!-- Actions Row -->
        <div class="btn-row" id="imgcrop-action-row" style="display:none; margin-top: 16px;">
          <button type="button" class="btn btn-primary" id="imgcrop-btn" onclick="runImageCrop()">✂️ Apply Crop</button>
          <button type="button" class="btn btn-outline" onclick="resetImageCropper()">Reset</button>
        </div>

        <!-- Result Card -->
        <div id="imgcrop-result" class="result-card" style="display:none; margin-top: 20px;">
          <h3 class="result-header">✓ Image Cropped Successfully</h3>
          <div class="comparison-stats-grid">
            <div class="comp-stat-col">
              <span class="comp-stat-label">Cropped Dimensions</span>
              <span class="comp-stat-val text-primary" id="imgcrop-res-dims">0 × 0 px</span>
            </div>
            <div class="comp-stat-col">
              <span class="comp-stat-label">Aspect Ratio</span>
              <span class="comp-stat-val" id="imgcrop-res-ratio">1:1</span>
            </div>
            <div class="comp-stat-col">
              <span class="comp-stat-label">Output Size</span>
              <span class="comp-stat-val text-emerald" id="imgcrop-res-size">0 KB</span>
            </div>
          </div>
          <div class="image-preview-wrapper" style="margin-top: 16px;">
            <img id="imgcrop-preview" class="image-preview-box" alt="Cropped Preview">
          </div>
          <div style="margin-top: 16px;">
            <button type="button" id="imgcrop-download-btn" class="btn btn-primary btn-block download-btn" onclick="downloadCroppedImage()">⬇ Download Cropped Image</button>
            <button type="button" class="btn btn-outline btn-block" style="margin-top: 8px;" onclick="resetImageCropper()">Crop Another Image</button>
          </div>
        </div>
      </div>
''',

    'image-to-webp': '''    <section id="screen-image-to-webp" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Image to WebP Converter</h1>
        <p class="tool-page-subtitle">Convert JPG and PNG images into modern, ultra-lightweight WebP format. Reduce image weight by up to 80% locally.</p>
        <button type="button" class="header-fav-btn" data-tool-id="image-to-webp" onclick="toggleFavorite('image-to-webp', event)" aria-label="Toggle Favorite" title="Favorite"><span class="header-fav-star">☆</span> <span class="header-fav-text">Favorite</span></button>
      </div>

      <div class="card">
        <div class="privacy-notice-box">
          <span class="privacy-icon">🔒</span>
          <span><strong>Privacy Note:</strong> Your files are processed locally in your browser and are not uploaded to our server.</span>
        </div>

        <!-- File Upload / Dropzone -->
        <div class="file-dropzone" id="img2webp-dropzone" onclick="document.getElementById('img2webp-input').click()">
          <input type="file" id="img2webp-input" accept="image/jpeg,image/png,image/gif,.jpg,.jpeg,.png,.gif" style="display:none;" onclick="event.stopPropagation(); this.value = null;" onchange="handleImageToWebpFile(this.files[0])">
          <div class="dropzone-icon">🚀</div>
          <div class="dropzone-text"><strong>Choose JPG or PNG image</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Converts images into next-generation WebP format</div>
        </div>

        <!-- Selected Image Card -->
        <div id="img2webp-selected-card" class="file-summary-card" style="display:none; margin-top: 16px;">
          <img id="img2webp-selected-thumb" class="file-summary-thumb" alt="Selected Preview">
          <div class="file-summary-info">
            <div class="file-summary-name" id="img2webp-filename">photo.jpg</div>
            <div class="file-summary-meta">Original: <strong class="text-primary" id="img2webp-orig-size">0 KB</strong> | Resolution: <span id="img2webp-orig-dims">0 × 0 px</span></div>
          </div>
          <button type="button" class="btn-text-sm" onclick="document.getElementById('img2webp-input').click()">Change Image</button>
        </div>

        <!-- Controls -->
        <div id="img2webp-controls" style="display:none; margin-top: 18px;">
          <div class="slider-control-group">
            <div class="slider-header">
              <label for="img2webp-quality">WebP Quality</label>
              <span class="slider-badge" id="img2webp-quality-val">80%</span>
            </div>
            <input type="range" id="img2webp-quality" min="10" max="100" value="80" step="1" oninput="updateWebpQuality(this.value)">
            <div class="slider-ticks">
              <span>Smallest File (50%)</span>
              <span>Optimal Web (80%)</span>
              <span>Max Quality (100%)</span>
            </div>
          </div>
          <div class="info-callout" style="margin-top: 14px; padding: 12px 14px; background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 8px; font-size: 0.88rem; color: var(--text-main);">
            🚀 <strong>Google WebP Advantage:</strong> WebP files are on average 25% to 34% smaller than equivalent JPEGs while retaining identical visual sharpness.
          </div>
        </div>

        <!-- Feedback Banners -->
        <div id="img2webp-error" class="error-banner" style="display:none; margin-top: 12px;"></div>
        <div id="img2webp-progress" class="status-banner" style="display:none; margin-top: 12px;"></div>

        <!-- Actions Row -->
        <div class="btn-row" id="img2webp-action-row" style="display:none; margin-top: 16px;">
          <button type="button" class="btn btn-primary" id="img2webp-btn" onclick="runImageToWebp()">🚀 Convert to WebP</button>
          <button type="button" class="btn btn-outline" onclick="resetImageToWebp()">Reset</button>
        </div>

        <!-- Result Card -->
        <div id="img2webp-result" class="result-card" style="display:none; margin-top: 20px;">
          <h3 class="result-header">✓ Converted to WebP Successfully</h3>
          <div class="comparison-stats-grid">
            <div class="comp-stat-col">
              <span class="comp-stat-label">Original Size</span>
              <span class="comp-stat-val" id="img2webp-res-orig">0 KB</span>
            </div>
            <div class="comp-stat-arrow">→</div>
            <div class="comp-stat-col">
              <span class="comp-stat-label">WebP Size</span>
              <span class="comp-stat-val text-emerald" id="img2webp-res-new">0 KB</span>
            </div>
            <div class="comp-stat-col">
              <span class="comp-stat-label">Space Saved</span>
              <span class="comp-stat-badge" id="img2webp-res-saved">-0%</span>
            </div>
          </div>
          <div class="image-preview-wrapper" style="margin-top: 16px;">
            <img id="img2webp-preview" class="image-preview-box" alt="WebP Preview">
          </div>
          <div style="margin-top: 16px;">
            <button type="button" id="img2webp-download-btn" class="btn btn-primary btn-block download-btn" onclick="downloadWebpImage()">⬇ Download WebP Image</button>
            <button type="button" class="btn btn-outline btn-block" style="margin-top: 8px;" onclick="resetImageToWebp()">Convert Another Image</button>
          </div>
        </div>
      </div>
'''
}

# Construct full HTML for each tool (interactive card + preserved tail)
final_tools_html = {}
for tid in INTERACTIVE_HTML:
    tail = extract_tail(tid)
    final_tools_html[tid] = INTERACTIVE_HTML[tid] + "\n      " + tail

print(f"Generated {len(final_tools_html)} full tool sections.")

# 2. Write tools_pdf_image_html.py (tools 1-5)
with open('tools_pdf_image_html.py', 'w', encoding='utf-8') as f:
    f.write("# tools_pdf_image_html.py\nTOOLS_HTML = {\n")
    for tid in ['pdf-merge', 'pdf-split', 'pdf-to-images', 'images-to-pdf', 'image-compressor']:
        f.write(f"    {repr(tid)}: {repr(final_tools_html[tid])},\n")
    f.write("}\n")
print("tools_pdf_image_html.py written.")

# 3. Write tools_pdf_image_html_2.py (tools 6-10)
with open('tools_pdf_image_html_2.py', 'w', encoding='utf-8') as f:
    f.write("# tools_pdf_image_html_2.py\nTOOLS_HTML_2 = {\n")
    for tid in ['image-resizer', 'jpg-to-png', 'png-to-jpg', 'image-cropper', 'image-to-webp']:
        f.write(f"    {repr(tid)}: {repr(final_tools_html[tid])},\n")
    f.write("}\n")
print("tools_pdf_image_html_2.py written.")

# 4. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix script tags in <head>
old_lib_scripts = re.search(r'<!-- PDF-Lib & PDF\.js[\s\S]*?<script src="script\.js" defer></script>', html)
new_lib_scripts = """  <!-- PDF-Lib & PDF.js for 100% Client-Side PDF Tools (Local with CDN fallback) -->
  <script src="assets/lib/pdf-lib.min.js"></script>
  <script src="assets/lib/pdf.min.js"></script>
  <script>
    if (typeof PDFLib === 'undefined') {
      document.write('<script src="https://cdn.jsdelivr.net/npm/pdf-lib@1.17.1/dist/pdf-lib.min.js"><\\/script>');
    }
    if (typeof pdfjsLib === 'undefined') {
      document.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"><\\/script>');
    }
  </script>
  <script src="script.js" defer></script>"""

if old_lib_scripts:
    html = html.replace(old_lib_scripts.group(0), new_lib_scripts)
    print("Replaced library scripts in <head> with local + CDN fallback tags.")

# Replace each tool section in index.html
for tid, full_sec in final_tools_html.items():
    pattern = re.compile(r'<section id="screen-' + re.escape(tid) + r'"[\s\S]*?</section>', re.MULTILINE)
    if pattern.search(html):
        html = pattern.sub(full_sec.strip(), html)
        print(f"Replaced screen-{tid} in index.html")
    else:
        print(f"WARNING: screen-{tid} NOT found in index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html updated successfully.")

# 5. Update script.js
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add to TOOLS_INFO
tools_info_entry = """  'pdf-merge': { name: 'PDF Merge', icon: '📑', category: 'pdf-images', desc: 'Combine multiple PDF documents into one file in custom page order.' },
  'pdf-split': { name: 'PDF Split', icon: '✂️', category: 'pdf-images', desc: 'Extract custom page ranges or split single pages from any PDF document.' },
  'pdf-to-images': { name: 'PDF to Images', icon: '🖼️', category: 'pdf-images', desc: 'Convert multi-page PDF documents into high-resolution JPG or PNG images.' },
  'images-to-pdf': { name: 'Images to PDF', icon: '📸', category: 'pdf-images', desc: 'Convert JPG, PNG, and WebP images into a single organized PDF document.' },
  'image-compressor': { name: 'Image Compressor', icon: '🗜️', category: 'pdf-images', desc: 'Compress JPG, PNG, and WebP images by up to 90% without visible loss.' },
  'image-resizer': { name: 'Image Resizer', icon: '📐', category: 'pdf-images', desc: 'Resize image dimensions by exact pixels or percentage with aspect ratio lock.' },
  'jpg-to-png': { name: 'JPG to PNG Converter', icon: '🔄', category: 'pdf-images', desc: 'Convert JPG/JPEG images to lossless transparent-ready PNG format.' },
  'png-to-jpg': { name: 'PNG to JPG Converter', icon: '🎨', category: 'pdf-images', desc: 'Convert PNG images to JPG with custom background color for transparency.' },
  'image-cropper': { name: 'Image Cropper', icon: '✂️', category: 'pdf-images', desc: 'Crop images with preset aspect ratios (1:1, 4:3, 16:9, Freeform) and live preview.' },
  'image-to-webp': { name: 'Image to WebP Converter', icon: '🚀', category: 'pdf-images', desc: 'Convert JPG and PNG images into lightweight next-gen WebP format.' },
"""

if "'pdf-merge':" not in js:
    js = js.replace("const TOOLS_INFO = {\n", "const TOOLS_INFO = {\n" + tools_info_entry)
    print("Added 10 tools to TOOLS_INFO in script.js.")

# Add to RELATED_TOOLS_MAP
related_entry = """  'pdf-merge': ['pdf-split', 'pdf-to-images', 'images-to-pdf'],
  'pdf-split': ['pdf-merge', 'pdf-to-images', 'images-to-pdf'],
  'pdf-to-images': ['images-to-pdf', 'pdf-split', 'image-compressor'],
  'images-to-pdf': ['pdf-to-images', 'pdf-merge', 'image-compressor'],
  'image-compressor': ['image-resizer', 'image-to-webp', 'image-cropper'],
  'image-resizer': ['image-compressor', 'image-cropper', 'image-to-webp'],
  'jpg-to-png': ['png-to-jpg', 'image-to-webp', 'image-compressor'],
  'png-to-jpg': ['jpg-to-png', 'image-to-webp', 'image-compressor'],
  'image-cropper': ['image-resizer', 'image-compressor', 'image-to-webp'],
  'image-to-webp': ['image-compressor', 'jpg-to-png', 'png-to-jpg'],
"""

if "'pdf-merge':" not in js[js.find("const RELATED_TOOLS_MAP"):js.find("const RELATED_TOOLS_MAP") + 2500]:
    js = js.replace("const RELATED_TOOLS_MAP = {\n", "const RELATED_TOOLS_MAP = {\n" + related_entry)
    print("Added 10 tools to RELATED_TOOLS_MAP in script.js.")

# Replace PDF & Image Tools JS section
from tools_pdf_image_js import JS_CODE
idx_js = js.find('// PDF & IMAGE TOOLS -')
if idx_js != -1:
    js = js[:idx_js] + JS_CODE
    print("Replaced PDF & Image tools code in script.js.")
else:
    js = js + "\n\n" + JS_CODE
    print("Appended PDF & Image tools code to script.js.")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("script.js updated successfully.")

# 6. Update style.css
from tools_pdf_image_css import CSS_CODE
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx_css = css.find('PDF & IMAGE TOOLS - MODERN, RESPONSIVE STYLES')
if idx_css != -1:
    # find comment start
    comment_start = css.rfind('/*', 0, idx_css)
    css = css[:comment_start] + CSS_CODE
    print("Replaced PDF & Image tools CSS in style.css.")
else:
    css = css + "\n\n" + CSS_CODE
    print("Appended PDF & Image tools CSS to style.css.")

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("style.css updated successfully.")

# 7. Sync to public/ and docs/
for folder in ['public', 'docs']:
    for fname in ['index.html', 'script.js', 'style.css']:
        shutil.copy(fname, os.path.join(folder, fname))
    print(f"Synced files to {folder}/")

print("All files updated and synchronized successfully!")
