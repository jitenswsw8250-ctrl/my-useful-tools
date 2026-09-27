# tools_pdf_image_html.py
# Complete, rich, accessible HTML for the 10 new PDF & Image tools

ADSTERRA_BANNER = """      <!-- Advertisement - Adsterra Banner 320x50 -->
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
      </div>"""

TOOLS_HTML = {}

# 1. PDF MERGE
TOOLS_HTML["pdf-merge"] = f"""    <!-- ==================== 36. PDF MERGE ==================== -->
    <section id="screen-pdf-merge" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">PDF Merge</h1>
        <p class="tool-page-subtitle">Combine multiple PDF documents into a single organized file with drag-and-drop order control. 100% private and browser-based.</p>
        <button type="button" class="header-fav-btn" data-tool-id="pdf-merge" onclick="toggleFavorite('pdf-merge', event)" aria-label="Toggle Favorite" title="Favorite"><span class="header-fav-star">☆</span> <span class="header-fav-text">Favorite</span></button>
      </div>

      <div class="card">
        <div class="privacy-notice-box">
          <span class="privacy-icon">🔒</span>
          <span><strong>Privacy Note:</strong> Your files are processed locally in your browser and are not uploaded to our server.</span>
        </div>

        <div class="file-dropzone" id="pdf-merge-dropzone" onclick="document.getElementById('pdf-merge-input').click()">
          <input type="file" id="pdf-merge-input" accept="application/pdf" multiple style="display:none;" onchange="handlePdfMergeFiles(this.files)">
          <div class="dropzone-icon">📑</div>
          <div class="dropzone-text"><strong>Choose PDF files</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Select 2 or more PDF documents to merge</div>
        </div>

        <div id="pdf-merge-list-container" class="file-list-container" style="display:none;">
          <div class="file-list-header">
            <span class="file-list-title">Selected PDF Files (<span id="pdf-merge-count">0</span>)</span>
            <button type="button" class="btn-text-sm" onclick="document.getElementById('pdf-merge-input').click()">+ Add More PDFs</button>
          </div>
          <div id="pdf-merge-file-list" class="file-item-list"></div>
        </div>

        <div id="pdf-merge-error" class="error-banner" style="display:none;"></div>
        <div id="pdf-merge-progress" class="status-banner" style="display:none;"></div>

        <div class="btn-row">
          <button type="button" class="btn btn-primary" id="pdf-merge-btn" onclick="processPdfMerge()">Merge PDFs</button>
          <button type="button" class="btn btn-outline" onclick="resetPdfMerge()">Reset</button>
        </div>

        <div id="pdf-merge-result" class="result-card" style="display:none;">
          <h3 class="result-header">Merged PDF Ready</h3>
          <div class="stat-highlight">
            <span id="pdf-merge-result-pages" class="highlight-number">0</span>
            <span class="highlight-unit">Pages Combined</span>
          </div>
          <div class="stats-pills-row">
            <div class="stat-pill">Files Merged: <strong id="pdf-merge-result-count">0</strong></div>
            <div class="stat-pill">Total Size: <strong id="pdf-merge-result-size">0 KB</strong></div>
          </div>
          <div style="margin-top: 16px;">
            <a id="pdf-merge-download-btn" class="btn btn-primary btn-block download-btn" download="merged-document.pdf">⬇ Download Merged PDF</a>
          </div>
        </div>
      </div>

      <!-- Copy & Share Result Actions -->
      <div class="result-actions-bar" id="result-actions-pdf-merge">
        <button type="button" class="result-action-btn copy-btn" onclick="copyCurrentResult('pdf-merge')" title="Copy Result"><span class="btn-icon">📋</span> Copy Result</button>
        <button type="button" class="result-action-btn share-btn" onclick="shareCurrentResult('pdf-merge')" title="Share Result"><span class="btn-icon">↗️</span> Share Result</button>
      </div>

      <!-- Related Calculators & Tools Section -->
      <div class="related-tools-section" data-tool="pdf-merge"></div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2 class="prose-title">About PDF Merge - Free Client-Side PDF Combiner</h2>
        <p class="prose-lead">PDF Merge allows you to effortlessly join multiple separate PDF documents into a single, cohesive document. Whether merging invoices, academic assignments, legal contracts, or scanned paper forms, our tool runs entirely inside your web browser. No files are transmitted to any remote servers, providing supreme privacy and instantaneous performance.</p>

        <h3 class="prose-h3">How to Use PDF Merge</h3>
        <ol class="prose-list">
          <li><strong>Select or Drop PDFs:</strong> Click the file upload box or drag your PDF documents directly onto the upload zone.</li>
          <li><strong>Reorder Files:</strong> Use the convenient Up (⬆) and Down (⬇) buttons next to each file to arrange your pages in the exact sequence you want them to appear.</li>
          <li><strong>Remove Unwanted Files:</strong> Click the remove (✕) button on any accidentally added file.</li>
          <li><strong>Click Merge PDFs:</strong> Our client-side PDF engine stitches all documents together in seconds.</li>
          <li><strong>Download:</strong> Click the "Download Merged PDF" button to save your combined PDF immediately to your device.</li>
        </ol>

        <h3 class="prose-h3">Key Features &amp; Benefits</h3>
        <ul class="prose-features">
          <li><strong>Zero Server Upload:</strong> Sensitive financial statements, medical files, and personal IDs never leave your device.</li>
          <li><strong>Unlimited File Combination:</strong> Merge 2, 5, 10, or more documents seamlessly.</li>
          <li><strong>Intuitive Sequence Controls:</strong> Position title pages, body chapters, and appendices in the perfect reading sequence.</li>
          <li><strong>High Fidelity Rendering:</strong> Preserves original document fonts, vector diagrams, hyperlinks, and page orientations.</li>
          <li><strong>Mobile Optimized:</strong> Smoothly reorder and merge documents on Android smartphones, tablets, and desktop workstations.</li>
        </ul>

        <h3 class="prose-h3">Practical Use Case Examples</h3>
        <div class="example-box">
          <div class="example-title">Example 1: Consolidating Tax &amp; Expense Receipts</div>
          <p class="example-desc">A freelancer collects monthly bank statements, freelance invoices, and utility utility receipts as 6 separate PDFs. By dropping them into PDF Merge, arranging them chronologically from January to June, and clicking Merge, they create a single audit-ready annual submission PDF in under five seconds.</p>
        </div>
        <div class="example-box">
          <div class="example-title">Example 2: Academic Thesis Chapters &amp; Cover Sheets</div>
          <p class="example-desc">A graduate student has their thesis cover page, table of contents, bibliography, and 4 experimental chapters saved in distinct PDFs from Word and LaTeX. With PDF Merge, they join all 7 files in the prescribed university order without purchasing costly PDF editor software.</p>
        </div>

        <h3 class="prose-h3">Frequently Asked Questions</h3>
        <div class="faq-list">
          <div class="faq-item">
            <div class="faq-q">Is my sensitive PDF uploaded to any cloud server?</div>
            <div class="faq-a">No. All PDF page parsing, binary assembling, and file generation execute entirely locally within your browser using WebAssembly and Web Standards. Zero bytes of your documents are uploaded to our servers or third parties.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can I merge PDFs that have different page orientations or sizes?</div>
            <div class="faq-a">Yes. Each PDF page maintains its original dimensions (Letter, A4, Legal) and orientation (Portrait or Landscape) throughout the merging process without distorting content.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Is there a limit on the number of PDFs I can combine?</div>
            <div class="faq-a">There is no hardcoded software limit. Because the tool runs directly on your device, it depends only on your device's available memory. Most mobile devices comfortably merge dozens of PDFs at once.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Does merging reduce the text quality or blur scanned images?</div>
            <div class="faq-a">No. PDF Merge preserves the raw vector paths, true-type fonts, embedded raster graphics, and text content verbatim with 100% loss-free reproduction.</div>
          </div>
        </div>
      </div>

{ADSTERRA_BANNER}
    </section>"""

# 2. PDF SPLIT
TOOLS_HTML["pdf-split"] = f"""    <!-- ==================== 37. PDF SPLIT ==================== -->
    <section id="screen-pdf-split" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">PDF Split</h1>
        <p class="tool-page-subtitle">Extract specific page ranges or extract single pages from your PDF document. Secure and processed entirely in your browser.</p>
        <button type="button" class="header-fav-btn" data-tool-id="pdf-split" onclick="toggleFavorite('pdf-split', event)" aria-label="Toggle Favorite" title="Favorite"><span class="header-fav-star">☆</span> <span class="header-fav-text">Favorite</span></button>
      </div>

      <div class="card">
        <div class="privacy-notice-box">
          <span class="privacy-icon">🔒</span>
          <span><strong>Privacy Note:</strong> Your files are processed locally in your browser and are not uploaded to our server.</span>
        </div>

        <div class="file-dropzone" id="pdf-split-dropzone" onclick="document.getElementById('pdf-split-input').click()">
          <input type="file" id="pdf-split-input" accept="application/pdf" style="display:none;" onchange="handlePdfSplitFile(this.files[0])">
          <div class="dropzone-icon">✂️</div>
          <div class="dropzone-text"><strong>Choose a PDF file</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Select a multi-page PDF document to split or extract</div>
        </div>

        <div id="pdf-split-controls" style="display:none; margin-top: 18px;">
          <div class="file-summary-card">
            <div class="file-summary-icon">📄</div>
            <div class="file-summary-info">
              <div class="file-summary-name" id="pdf-split-filename">document.pdf</div>
              <div class="file-summary-meta">Total Pages: <strong id="pdf-split-total-pages" class="text-primary">0</strong> | File Size: <span id="pdf-split-filesize">0 KB</span></div>
            </div>
          </div>

          <div class="input-group" style="margin-top: 16px;">
            <label for="pdf-split-range"><strong>Pages to Extract</strong> (e.g., <code>1-3, 5, 8-10</code>)</label>
            <input type="text" id="pdf-split-range" class="form-input" placeholder="e.g. 1-3, 5" value="1">
            <span class="input-hint">Specify individual pages separated by commas, or page ranges with hyphens.</span>
          </div>

          <div class="quick-preset-chips">
            <span class="preset-label">Quick Presets:</span>
            <button type="button" class="preset-chip" onclick="setPdfSplitPreset('all')">All Pages</button>
            <button type="button" class="preset-chip" onclick="setPdfSplitPreset('first')">First Page (1)</button>
            <button type="button" class="preset-chip" onclick="setPdfSplitPreset('odd')">Odd Pages</button>
            <button type="button" class="preset-chip" onclick="setPdfSplitPreset('even')">Even Pages</button>
          </div>
        </div>

        <div id="pdf-split-error" class="error-banner" style="display:none;"></div>
        <div id="pdf-split-progress" class="status-banner" style="display:none;"></div>

        <div class="btn-row">
          <button type="button" class="btn btn-primary" id="pdf-split-btn" onclick="processPdfSplit()" disabled>Extract Pages</button>
          <button type="button" class="btn btn-outline" onclick="resetPdfSplit()">Reset</button>
        </div>

        <div id="pdf-split-result" class="result-card" style="display:none;">
          <h3 class="result-header">Extracted PDF Created</h3>
          <div class="stat-highlight">
            <span id="pdf-split-result-pages" class="highlight-number">0</span>
            <span class="highlight-unit">Pages Extracted</span>
          </div>
          <div class="stats-pills-row">
            <div class="stat-pill">Extracted Range: <strong id="pdf-split-result-range">-</strong></div>
            <div class="stat-pill">New File Size: <strong id="pdf-split-result-size">0 KB</strong></div>
          </div>
          <div style="margin-top: 16px;">
            <a id="pdf-split-download-btn" class="btn btn-primary btn-block download-btn" download="extracted-pages.pdf">⬇ Download Extracted PDF</a>
          </div>
        </div>
      </div>

      <!-- Copy & Share Result Actions -->
      <div class="result-actions-bar" id="result-actions-pdf-split">
        <button type="button" class="result-action-btn copy-btn" onclick="copyCurrentResult('pdf-split')" title="Copy Result"><span class="btn-icon">📋</span> Copy Result</button>
        <button type="button" class="result-action-btn share-btn" onclick="shareCurrentResult('pdf-split')" title="Share Result"><span class="btn-icon">↗️</span> Share Result</button>
      </div>

      <!-- Related Calculators & Tools Section -->
      <div class="related-tools-section" data-tool="pdf-split"></div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2 class="prose-title">About PDF Split - Extract Pages from PDF Online</h2>
        <p class="prose-lead">PDF Split empowers you to isolate and extract select pages or custom page ranges from any multi-page PDF document. If you only need pages 4 through 7 of a lengthy 100-page manual, or need to separate a signature page from a contract, PDF Split handles it seamlessly right in your browser with zero server uploads.</p>

        <h3 class="prose-h3">How to Split and Extract PDF Pages</h3>
        <ol class="prose-list">
          <li><strong>Upload Your PDF:</strong> Drag and drop your file or tap the upload box to pick your PDF document.</li>
          <li><strong>Review Total Pages:</strong> The tool automatically reads and displays the total page count of your document.</li>
          <li><strong>Specify Pages:</strong> Type the desired pages using numbers, commas, and hyphens (such as <code>1-3, 5, 9-12</code>), or click convenient quick preset buttons like "Odd Pages" or "First Page".</li>
          <li><strong>Click Extract Pages:</strong> The browser builds a lightweight new PDF containing strictly your chosen pages.</li>
          <li><strong>Download:</strong> Click the "Download Extracted PDF" button to immediately obtain your customized PDF.</li>
        </ol>

        <h3 class="prose-h3">Key Features &amp; Benefits</h3>
        <ul class="prose-features">
          <li><strong>Complete Local Confidentiality:</strong> Perfect for confidential legal agreements, payroll sheets, and financial disclosures.</li>
          <li><strong>Flexible Syntax:</strong> Supports discrete page lists (<code>2, 4, 6</code>) as well as continuous intervals (<code>10-25</code>).</li>
          <li><strong>Validation Safeguards:</strong> Automatically prevents typos, out-of-range page numbers, and empty selections.</li>
          <li><strong>Zero Installation:</strong> Runs instantly on Google Chrome, Samsung Internet, Safari, Firefox, and Edge.</li>
        </ul>

        <h3 class="prose-h3">Practical Use Case Examples</h3>
        <div class="example-box">
          <div class="example-title">Example 1: Extracting Certificate from an Annual Report</div>
          <p class="example-desc">An employee receives a 50-page company benefits guide where page 42 is an insurance enrollment certificate. By entering <code>42</code> into PDF Split, they download a standalone 1-page PDF file ready for submission to HR without cumbersome third-party software.</p>
        </div>
        <div class="example-box">
          <div class="example-title">Example 2: Splitting Textbook Chapters for Mobile Reading</div>
          <p class="example-desc">A university student needs to read Chapter 3 (pages 45 to 68) of a heavy 600-page academic textbook. Entering <code>45-68</code> creates an ultra-compact PDF that opens instantly on their mobile phone without battery drain or lag.</p>
        </div>

        <h3 class="prose-h3">Frequently Asked Questions</h3>
        <div class="faq-list">
          <div class="faq-item">
            <div class="faq-q">Can I extract non-consecutive pages in a single split?</div>
            <div class="faq-a">Yes. You can combine ranges and single pages using commas, such as <code>1, 3-5, 9, 12-14</code>. All specified pages will be gathered in order into a single output PDF.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Will splitting remove pages from my original file?</div>
            <div class="faq-a">No. Your original PDF stored on your device remains completely untouched. The browser simply reads the page data and writes a brand new PDF with the selected pages.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">What happens if I type a page number larger than the document's total pages?</div>
            <div class="faq-a">The validator automatically flags out-of-range numbers with a friendly inline message and prevents invalid PDF generation.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Does PDF Split require an active internet connection?</div>
            <div class="faq-a">Once the web app is loaded in your browser, the PDF splitting algorithm runs 100% offline via client-side JavaScript.</div>
          </div>
        </div>
      </div>

{ADSTERRA_BANNER}
    </section>"""

# 3. PDF TO IMAGES
TOOLS_HTML["pdf-to-images"] = f"""    <!-- ==================== 38. PDF TO IMAGES ==================== -->
    <section id="screen-pdf-to-images" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">PDF to Images</h1>
        <p class="tool-page-subtitle">Convert PDF document pages into high-resolution JPG or PNG image files with live browser rendering. 100% client-side privacy.</p>
        <button type="button" class="header-fav-btn" data-tool-id="pdf-to-images" onclick="toggleFavorite('pdf-to-images', event)" aria-label="Toggle Favorite" title="Favorite"><span class="header-fav-star">☆</span> <span class="header-fav-text">Favorite</span></button>
      </div>

      <div class="card">
        <div class="privacy-notice-box">
          <span class="privacy-icon">🔒</span>
          <span><strong>Privacy Note:</strong> Your files are processed locally in your browser and are not uploaded to our server.</span>
        </div>

        <div class="file-dropzone" id="pdf2img-dropzone" onclick="document.getElementById('pdf2img-input').click()">
          <input type="file" id="pdf2img-input" accept="application/pdf" style="display:none;" onchange="handlePdfToImagesFile(this.files[0])">
          <div class="dropzone-icon">🖼️</div>
          <div class="dropzone-text"><strong>Choose a PDF file</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Render each PDF page into clean, high-resolution JPG or PNG images</div>
        </div>

        <div id="pdf2img-controls" style="display:none; margin-top: 18px;">
          <div class="file-summary-card">
            <div class="file-summary-icon">📑</div>
            <div class="file-summary-info">
              <div class="file-summary-name" id="pdf2img-filename">document.pdf</div>
              <div class="file-summary-meta">Detected Pages: <strong id="pdf2img-total-pages" class="text-primary">0</strong></div>
            </div>
          </div>

          <div class="input-grid-2" style="margin-top: 16px;">
            <div class="input-group">
              <label for="pdf2img-format">Output Image Format</label>
              <select id="pdf2img-format" class="form-input">
                <option value="image/jpeg" selected>JPG / JPEG (Compact file size)</option>
                <option value="image/png">PNG (Lossless clarity)</option>
              </select>
            </div>
            <div class="input-group">
              <label for="pdf2img-quality">Rendering DPI / Quality</label>
              <select id="pdf2img-quality" class="form-input">
                <option value="1.5" selected>Standard Web (150 DPI)</option>
                <option value="2.0">High Definition (200 DPI)</option>
                <option value="1.0">Compact / Fast (100 DPI)</option>
              </select>
            </div>
          </div>
        </div>

        <div id="pdf2img-error" class="error-banner" style="display:none;"></div>
        <div id="pdf2img-progress" class="status-banner" style="display:none;"></div>

        <div class="btn-row">
          <button type="button" class="btn btn-primary" id="pdf2img-btn" onclick="processPdfToImages()" disabled>Convert to Images</button>
          <button type="button" class="btn btn-outline" onclick="resetPdfToImages()">Reset</button>
        </div>

        <div id="pdf2img-results" class="result-card" style="display:none;">
          <div class="result-header-row">
            <h3 class="result-header" style="margin:0;">Converted Pages (<span id="pdf2img-rendered-count">0</span>)</h3>
            <button type="button" class="btn btn-outline btn-sm" onclick="downloadAllPdfImages()">⬇ Download All</button>
          </div>
          <div id="pdf2img-gallery" class="image-gallery-grid"></div>
        </div>
      </div>

      <!-- Copy & Share Result Actions -->
      <div class="result-actions-bar" id="result-actions-pdf-to-images">
        <button type="button" class="result-action-btn copy-btn" onclick="copyCurrentResult('pdf-to-images')" title="Copy Result"><span class="btn-icon">📋</span> Copy Result</button>
        <button type="button" class="result-action-btn share-btn" onclick="shareCurrentResult('pdf-to-images')" title="Share Result"><span class="btn-icon">↗️</span> Share Result</button>
      </div>

      <!-- Related Calculators & Tools Section -->
      <div class="related-tools-section" data-tool="pdf-to-images"></div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2 class="prose-title">About PDF to Images - Convert PDF Pages to JPG and PNG</h2>
        <p class="prose-lead">PDF to Images turns every page of your PDF into crisp, standalone graphic images. If you need to embed a PDF chart in a PowerPoint presentation, share an infographic on social media, or upload a scanned letter to a form that only accepts image attachments, this tool renders each page on an HTML5 canvas right inside your browser.</p>

        <h3 class="prose-h3">How to Convert PDF to Images</h3>
        <ol class="prose-list">
          <li><strong>Upload PDF:</strong> Select your file or drop it into the conversion zone.</li>
          <li><strong>Choose Format &amp; Resolution:</strong> Pick JPG for smaller file sizes or PNG for razor-sharp typography and graphics.</li>
          <li><strong>Click Convert:</strong> The client-side rendering pipeline parses vector commands and generates image representations in real time.</li>
          <li><strong>Download:</strong> Tap the download button on any individual page thumbnail, or click "Download All" to grab every rendered page sequentially.</li>
        </ol>

        <h3 class="prose-h3">Key Features &amp; Benefits</h3>
        <ul class="prose-features">
          <li><strong>High-Definition Canvas Rendering:</strong> Utilizes native 150–200 DPI scaling for crystal clear text and graphics.</li>
          <li><strong>No File Size Caps:</strong> Convert slides, brochures, e-books, and receipts on demand.</li>
          <li><strong>Private &amp; Offline-Ready:</strong> Zero data packets leave your device during the conversion.</li>
          <li><strong>JPG &amp; PNG Flexibility:</strong> Tailor your output to photo compression or lossless graphic reproduction.</li>
        </ul>

        <h3 class="prose-h3">Practical Use Case Examples</h3>
        <div class="example-box">
          <div class="example-title">Example 1: Uploading ID Documents to Mobile Portals</div>
          <p class="example-desc">An applicant has their passport scan saved as a PDF, but the mobile job application portal strictly requires a JPG under 2 MB. Using PDF to Images with standard JPG output, page 1 is rendered into a clean 450 KB JPG image ready to upload.</p>
        </div>
        <div class="example-box">
          <div class="example-title">Example 2: Sharing Slide Deck Visuals on Social Media</div>
          <p class="example-desc">A speaker exports their 10-slide keynote talk to PDF and wants to post 3 key infographic slides on LinkedIn. Using PDF to Images with High Quality PNG, they download individual slides as standalone images ready for immediate posting.</p>
        </div>

        <h3 class="prose-h3">Frequently Asked Questions</h3>
        <div class="faq-list">
          <div class="faq-item">
            <div class="faq-q">Should I choose JPG or PNG for my PDF conversion?</div>
            <div class="faq-a">Choose JPG if your PDF contains photographic artwork, scanned paper backgrounds, or if you need smaller download sizes. Choose PNG if your PDF contains fine technical drawings, barcodes, or text that must remain crisp at high zoom.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can I convert multi-page PDF documents?</div>
            <div class="faq-a">Yes. Every single page of your document is rendered into its own numbered image file (e.g., page-1.jpg, page-2.jpg).</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Does this tool support password-protected PDFs?</div>
            <div class="faq-a">For standard unprotected PDFs, rendering is instant. If your PDF is encrypted with a master user password, please unlock it before converting.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Are my files kept secure?</div>
            <div class="faq-a">Yes! The PDF parsing and image rasterization happen inside your device's browser memory. No servers ever see your files.</div>
          </div>
        </div>
      </div>

{ADSTERRA_BANNER}
    </section>"""

# 4. IMAGES TO PDF
TOOLS_HTML["images-to-pdf"] = f"""    <!-- ==================== 39. IMAGES TO PDF ==================== -->
    <section id="screen-images-to-pdf" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Images to PDF</h1>
        <p class="tool-page-subtitle">Turn multiple photos, graphics, and screenshots into a single organized PDF document. Fast, free, and completely local.</p>
        <button type="button" class="header-fav-btn" data-tool-id="images-to-pdf" onclick="toggleFavorite('images-to-pdf', event)" aria-label="Toggle Favorite" title="Favorite"><span class="header-fav-star">☆</span> <span class="header-fav-text">Favorite</span></button>
      </div>

      <div class="card">
        <div class="privacy-notice-box">
          <span class="privacy-icon">🔒</span>
          <span><strong>Privacy Note:</strong> Your files are processed locally in your browser and are not uploaded to our server.</span>
        </div>

        <div class="file-dropzone" id="img2pdf-dropzone" onclick="document.getElementById('img2pdf-input').click()">
          <input type="file" id="img2pdf-input" accept="image/jpeg,image/png,image/webp" multiple style="display:none;" onchange="handleImagesToPdfFiles(this.files)">
          <div class="dropzone-icon">📑</div>
          <div class="dropzone-text"><strong>Choose Images</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Supports JPG, PNG, and WebP photos</div>
        </div>

        <div id="img2pdf-controls" style="display:none; margin-top: 18px;">
          <div class="file-list-header">
            <span class="file-list-title">Selected Images (<span id="img2pdf-count">0</span>)</span>
            <button type="button" class="btn-text-sm" onclick="document.getElementById('img2pdf-input').click()">+ Add More Images</button>
          </div>

          <div id="img2pdf-thumbnails" class="img2pdf-thumb-list"></div>

          <div class="input-grid-2" style="margin-top: 16px;">
            <div class="input-group">
              <label for="img2pdf-page-size">Page Layout / Sizing</label>
              <select id="img2pdf-page-size" class="form-input">
                <option value="fit" selected>Fit to Image (Natural Dimensions)</option>
                <option value="a4-portrait">Standard A4 (Portrait)</option>
                <option value="a4-landscape">Standard A4 (Landscape)</option>
              </select>
            </div>
            <div class="input-group">
              <label for="img2pdf-margins">Page Margins</label>
              <select id="img2pdf-margins" class="form-input">
                <option value="0" selected>None (Full Bleed)</option>
                <option value="20">Small Margin (20 pt)</option>
                <option value="40">Standard Margin (40 pt)</option>
              </select>
            </div>
          </div>
        </div>

        <div id="img2pdf-error" class="error-banner" style="display:none;"></div>
        <div id="img2pdf-progress" class="status-banner" style="display:none;"></div>

        <div class="btn-row">
          <button type="button" class="btn btn-primary" id="img2pdf-btn" onclick="processImagesToPdf()" disabled>Create PDF</button>
          <button type="button" class="btn btn-outline" onclick="resetImagesToPdf()">Reset</button>
        </div>

        <div id="img2pdf-result" class="result-card" style="display:none;">
          <h3 class="result-header">PDF Created Successfully</h3>
          <div class="stat-highlight">
            <span id="img2pdf-result-pages" class="highlight-number">0</span>
            <span class="highlight-unit">Pages Included</span>
          </div>
          <div class="stats-pills-row">
            <div class="stat-pill">Images Compiled: <strong id="img2pdf-result-count">0</strong></div>
            <div class="stat-pill">Estimated PDF Size: <strong id="img2pdf-result-size">0 KB</strong></div>
          </div>
          <div style="margin-top: 16px;">
            <a id="img2pdf-download-btn" class="btn btn-primary btn-block download-btn" download="photos-document.pdf">⬇ Download PDF Document</a>
          </div>
        </div>
      </div>

      <!-- Copy & Share Result Actions -->
      <div class="result-actions-bar" id="result-actions-images-to-pdf">
        <button type="button" class="result-action-btn copy-btn" onclick="copyCurrentResult('images-to-pdf')" title="Copy Result"><span class="btn-icon">📋</span> Copy Result</button>
        <button type="button" class="result-action-btn share-btn" onclick="shareCurrentResult('images-to-pdf')" title="Share Result"><span class="btn-icon">↗️</span> Share Result</button>
      </div>

      <!-- Related Calculators & Tools Section -->
      <div class="related-tools-section" data-tool="images-to-pdf"></div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2 class="prose-title">About Images to PDF - Combine Photos into a Single PDF</h2>
        <p class="prose-lead">Images to PDF transforms your phone photos, camera snapshots, whiteboard diagrams, and graphic files into a clean, presentation-ready PDF file. Perfect for submitting photo assignments, assembling receipt packets, or bundling portfolio work into an easily shareable PDF.</p>

        <h3 class="prose-h3">How to Convert Images to PDF</h3>
        <ol class="prose-list">
          <li><strong>Select Multiple Images:</strong> Tap the upload zone to pick multiple JPG, PNG, or WebP files from your phone gallery or desktop folder.</li>
          <li><strong>Arrange Page Order:</strong> Review image thumbnails and use the ⬆ and ⬇ buttons to sort them into your intended reading sequence.</li>
          <li><strong>Adjust Layout:</strong> Pick between natural image sizing (Fit to Image) or standard A4 formatting with optional margins.</li>
          <li><strong>Create PDF:</strong> Click "Create PDF" to bundle all images into a uniform document.</li>
          <li><strong>Download:</strong> Tap the download button to save your consolidated PDF immediately.</li>
        </ol>

        <h3 class="prose-h3">Key Features &amp; Benefits</h3>
        <ul class="prose-features">
          <li><strong>Multi-Format Support:</strong> Seamlessly mix and match JPG, PNG, and WebP images in the same document.</li>
          <li><strong>Full Client-Side Security:</strong> Images are never sent to external servers or cloud storage.</li>
          <li><strong>Automatic Orientation Handling:</strong> Landscape and portrait photos are laid out with precision.</li>
          <li><strong>Lightweight File Assembly:</strong> Produces compact PDF files ideal for email attachments and portal uploads.</li>
        </ul>

        <h3 class="prose-h3">Practical Use Case Examples</h3>
        <div class="example-box">
          <div class="example-title">Example 1: Homework &amp; Handwritten Exam Submission</div>
          <p class="example-desc">A student takes 4 photos of their handwritten math homework using their smartphone camera. By selecting all 4 JPGs in Images to PDF, arranging them from problem 1 to 4, and clicking Create PDF, they generate a single PDF submission accepted by Google Classroom.</p>
        </div>
        <div class="example-box">
          <div class="example-title">Example 2: Expense Reports with Scanned Paper Receipts</div>
          <p class="example-desc">An executive collects 8 paper taxi and hotel receipt photos during a business trip. Images to PDF combines all 8 photos into a single PDF titled "Travel-Expenses.pdf", making accounting review frictionless.</p>
        </div>

        <h3 class="prose-h3">Frequently Asked Questions</h3>
        <div class="faq-list">
          <div class="faq-item">
            <div class="faq-q">Can I reorder images before generating the PDF?</div>
            <div class="faq-a">Yes! Use the Up and Down arrow buttons on any thumbnail card to change the exact page sequence.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Will my photos be compressed or lose visual clarity?</div>
            <div class="faq-a">Images are embedded into the PDF structure preserving their original pixel resolution so barcodes, signatures, and small text remain razor-sharp.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Is there a limit on how many photos I can add?</div>
            <div class="faq-a">No arbitrary limit is imposed. You can add dozens of photos as needed based on your browser's memory.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can I convert images to PDF without an internet connection?</div>
            <div class="faq-a">Yes. Once loaded, the tool works completely offline on modern Android devices and desktops.</div>
          </div>
        </div>
      </div>

{ADSTERRA_BANNER}
    </section>"""

# 5. IMAGE COMPRESSOR
TOOLS_HTML["image-compressor"] = f"""    <!-- ==================== 40. IMAGE COMPRESSOR ==================== -->
    <section id="screen-image-compressor" class="screen-section">
      <div class="tool-header">
        <button class="back-link" onclick="navigateTo('home')">← Back to All Tools</button>
        <h1 class="tool-page-title">Image Compressor</h1>
        <p class="tool-page-subtitle">Shrink JPG, PNG, and WebP image file sizes by up to 90% without visible quality loss. Instant local processing.</p>
        <button type="button" class="header-fav-btn" data-tool-id="image-compressor" onclick="toggleFavorite('image-compressor', event)" aria-label="Toggle Favorite" title="Favorite"><span class="header-fav-star">☆</span> <span class="header-fav-text">Favorite</span></button>
      </div>

      <div class="card">
        <div class="privacy-notice-box">
          <span class="privacy-icon">🔒</span>
          <span><strong>Privacy Note:</strong> Your files are processed locally in your browser and are not uploaded to our server.</span>
        </div>

        <div class="file-dropzone" id="imgcomp-dropzone" onclick="document.getElementById('imgcomp-input').click()">
          <input type="file" id="imgcomp-input" accept="image/jpeg,image/png,image/webp" style="display:none;" onchange="handleImageCompressorFile(this.files[0])">
          <div class="dropzone-icon">🗜️</div>
          <div class="dropzone-text"><strong>Choose an Image</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Supports JPG, PNG, and WebP files</div>
        </div>

        <div id="imgcomp-controls" style="display:none; margin-top: 18px;">
          <div class="file-summary-card">
            <div class="file-summary-icon">🖼️</div>
            <div class="file-summary-info">
              <div class="file-summary-name" id="imgcomp-filename">image.jpg</div>
              <div class="file-summary-meta">Original Size: <strong id="imgcomp-orig-size" class="text-primary">0 KB</strong> | Dimensions: <span id="imgcomp-orig-dims">0 × 0 px</span></div>
            </div>
          </div>

          <div class="slider-control-group" style="margin-top: 16px;">
            <div class="slider-header">
              <label for="imgcomp-quality"><strong>Compression Quality</strong></label>
              <span id="imgcomp-quality-val" class="slider-badge">75%</span>
            </div>
            <input type="range" id="imgcomp-quality" min="10" max="100" value="75" step="1" oninput="updateCompressorQuality(this.value)">
            <div class="slider-ticks">
              <span>Maximum Savings (10%)</span>
              <span>Balanced (75%)</span>
              <span>Best Quality (100%)</span>
            </div>
          </div>

          <div class="input-grid-2" style="margin-top: 14px;">
            <div class="input-group">
              <label for="imgcomp-max-width">Max Width Scale (Optional)</label>
              <select id="imgcomp-max-width" class="form-input" onchange="runImageCompression()">
                <option value="original" selected>Keep Original Dimensions</option>
                <option value="1920">1920 px (Full HD)</option>
                <option value="1280">1280 px (HD / Web)</option>
                <option value="800">800 px (Email / Chat)</option>
              </select>
            </div>
            <div class="input-group">
              <label for="imgcomp-format">Output Format</label>
              <select id="imgcomp-format" class="form-input" onchange="runImageCompression()">
                <option value="auto" selected>Keep Original Format</option>
                <option value="image/jpeg">Convert to JPG</option>
                <option value="image/webp">Convert to WebP (Smallest)</option>
              </select>
            </div>
          </div>
        </div>

        <div id="imgcomp-error" class="error-banner" style="display:none;"></div>

        <div class="btn-row" id="imgcomp-action-row" style="display:none;">
          <button type="button" class="btn btn-primary" onclick="runImageCompression()">Re-compress</button>
          <button type="button" class="btn btn-outline" onclick="resetImageCompressor()">Reset</button>
        </div>

        <div id="imgcomp-result" class="result-card" style="display:none;">
          <h3 class="result-header">Compression Complete</h3>
          
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
            <a id="imgcomp-download-btn" class="btn btn-primary btn-block download-btn" download="compressed-image.jpg">⬇ Download Compressed Image</a>
          </div>
        </div>
      </div>

      <!-- Copy & Share Result Actions -->
      <div class="result-actions-bar" id="result-actions-image-compressor">
        <button type="button" class="result-action-btn copy-btn" onclick="copyCurrentResult('image-compressor')" title="Copy Result"><span class="btn-icon">📋</span> Copy Result</button>
        <button type="button" class="result-action-btn share-btn" onclick="shareCurrentResult('image-compressor')" title="Share Result"><span class="btn-icon">↗️</span> Share Result</button>
      </div>

      <!-- Related Calculators & Tools Section -->
      <div class="related-tools-section" data-tool="image-compressor"></div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2 class="prose-title">About Image Compressor - Reduce Image Size Online</h2>
        <p class="prose-lead">Image Compressor utilizes the browser's hardware-accelerated Canvas engine to reduce the byte size of JPG, PNG, and WebP graphics by up to 90%. By stripping unnecessary metadata and applying advanced lossy quantizations, your photos load faster, take up minimal disk space, and fit strict email or portal attachment size constraints.</p>

        <h3 class="prose-h3">How to Compress an Image</h3>
        <ol class="prose-list">
          <li><strong>Upload Image:</strong> Select or drag any JPG, PNG, or WebP photo into the upload box.</li>
          <li><strong>Adjust Quality Slider:</strong> Move the quality slider between 10% and 100%. The balanced default (75%) provides remarkable size savings with virtually no visible difference.</li>
          <li><strong>Optional Downscaling:</strong> Choose a maximum width (such as 1920px or 1280px) if you are compressing heavy 12–48 megapixel smartphone camera shots.</li>
          <li><strong>Review Results:</strong> Compare the original and compressed file sizes and check the preview image.</li>
          <li><strong>Download:</strong> Click "Download Compressed Image" to store the optimized image on your device.</li>
        </ol>

        <h3 class="prose-h3">Key Features &amp; Benefits</h3>
        <ul class="prose-features">
          <li><strong>Guaranteed Private:</strong> No pictures are ever sent over the internet or uploaded to remote databases.</li>
          <li><strong>Real-Time Size Feedback:</strong> Immediately see exact byte measurements and percentage reduction statistics.</li>
          <li><strong>Format Flexibility:</strong> Compress native JPGs or convert directly to next-generation WebP for maximum compression efficiency.</li>
          <li><strong>No Watermarks:</strong> Completely clean output without promotional stamps or restrictions.</li>
        </ul>

        <h3 class="prose-h3">Practical Use Case Examples</h3>
        <div class="example-box">
          <div class="example-title">Example 1: Email Attachment Limits</div>
          <p class="example-desc">A user takes a 5.2 MB photo of an apartment lease to email their landlord, but the email server has a 2 MB attachment limit. Setting the slider to 70% compresses the image to 380 KB (-92% smaller) with perfect legibility of every clause.</p>
        </div>
        <div class="example-box">
          <div class="example-title">Example 2: Accelerating Website Page Speeds</div>
          <p class="example-desc">A web blogger has a 3.8 MB hero banner slowing their mobile page load. Using Image Compressor with 75% quality and WebP output drops the file size to 240 KB, improving Google PageSpeed Insights and mobile visitor engagement.</p>
        </div>

        <h3 class="prose-h3">Frequently Asked Questions</h3>
        <div class="faq-list">
          <div class="faq-item">
            <div class="faq-q">Does image compression cause visible blurriness?</div>
            <div class="faq-a">At quality levels between 70% and 85%, human eyes cannot distinguish compression artifacts on normal screens or phone displays. High-frequency noise is eliminated while core contours and colors remain intact.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can I compress PNG images with transparent backgrounds?</div>
            <div class="faq-a">Yes! When compressing PNG with WebP or PNG output, alpha transparency channels are preserved.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Is there any fee or subscription needed?</div>
            <div class="faq-a">No. Image Compressor is 100% free with unlimited conversions and zero account creation.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Does compression remove EXIF camera metadata?</div>
            <div class="faq-a">Yes. Rendering through an HTML5 canvas automatically purges location geotags and camera serial numbers, enhancing your personal privacy.</div>
          </div>
        </div>
      </div>

{ADSTERRA_BANNER}
    </section>"""

print("Generated first 5 HTML sections.")
