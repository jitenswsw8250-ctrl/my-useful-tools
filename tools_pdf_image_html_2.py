# tools_pdf_image_html_2.py
# HTML sections for Tools 41 to 45: Image Resizer, JPG to PNG, PNG to JPG, Image Cropper, Image to WebP

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

TOOLS_HTML_2 = {}

# 6. IMAGE RESIZER
TOOLS_HTML_2["image-resizer"] = f"""    <!-- ==================== 41. IMAGE RESIZER ==================== -->
    <section id="screen-image-resizer" class="screen-section">
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

        <div class="file-dropzone" id="imgresize-dropzone" onclick="document.getElementById('imgresize-input').click()">
          <input type="file" id="imgresize-input" accept="image/*" style="display:none;" onchange="handleImageResizerFile(this.files[0])">
          <div class="dropzone-icon">📐</div>
          <div class="dropzone-text"><strong>Choose an Image</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Supports JPG, PNG, and WebP graphics</div>
        </div>

        <div id="imgresize-controls" style="display:none; margin-top: 18px;">
          <div class="file-summary-card">
            <div class="file-summary-icon">🖼️</div>
            <div class="file-summary-info">
              <div class="file-summary-name" id="imgresize-filename">photo.jpg</div>
              <div class="file-summary-meta">Original: <strong id="imgresize-orig-dims" class="text-primary">0 × 0 px</strong> (<span id="imgresize-orig-ratio">1:1</span>) | File Size: <span id="imgresize-orig-size">0 KB</span></div>
            </div>
          </div>

          <div class="quick-preset-chips" style="margin-top: 16px;">
            <span class="preset-label">Presets:</span>
            <button type="button" class="preset-chip" onclick="applyResizerPreset(0.5)">50% Scale</button>
            <button type="button" class="preset-chip" onclick="applyResizerPreset(0.75)">75% Scale</button>
            <button type="button" class="preset-chip" onclick="applyResizerExact(1920, 1080)">1920×1080 (FHD)</button>
            <button type="button" class="preset-chip" onclick="applyResizerExact(1280, 720)">1280×720 (HD)</button>
            <button type="button" class="preset-chip" onclick="applyResizerExact(1080, 1080)">1080×1080 (Square)</button>
          </div>

          <div class="input-grid-2" style="margin-top: 14px;">
            <div class="input-group">
              <label for="imgresize-width">Width (pixels)</label>
              <input type="number" id="imgresize-width" class="form-input" min="1" max="10000" oninput="onResizerWidthChange(this.value)">
            </div>
            <div class="input-group">
              <label for="imgresize-height">Height (pixels)</label>
              <input type="number" id="imgresize-height" class="form-input" min="1" max="10000" oninput="onResizerHeightChange(this.value)">
            </div>
          </div>

          <div class="checkbox-row" style="margin-top: 10px;">
            <label class="custom-checkbox">
              <input type="checkbox" id="imgresize-lock-ratio" checked onchange="toggleResizerLock(this.checked)">
              <span>🔒 Lock Aspect Ratio (prevents distortion)</span>
            </label>
          </div>
        </div>

        <div id="imgresize-error" class="error-banner" style="display:none;"></div>

        <div class="btn-row" id="imgresize-action-row" style="display:none;">
          <button type="button" class="btn btn-primary" onclick="runImageResize()">Resize Image</button>
          <button type="button" class="btn btn-outline" onclick="resetImageResizer()">Reset</button>
        </div>

        <div id="imgresize-result" class="result-card" style="display:none;">
          <h3 class="result-header">Resized Image Ready</h3>
          <div class="stat-highlight">
            <span id="imgresize-res-dims" class="highlight-number">0 × 0</span>
            <span class="highlight-unit">Pixels</span>
          </div>
          <div class="stats-pills-row">
            <div class="stat-pill">New File Size: <strong id="imgresize-res-size">0 KB</strong></div>
            <div class="stat-pill">Format: <strong id="imgresize-res-format">JPG</strong></div>
          </div>
          <div class="image-preview-wrapper" style="margin-top: 16px;">
            <img id="imgresize-preview" class="image-preview-box" alt="Resized Preview">
          </div>
          <div style="margin-top: 16px;">
            <a id="imgresize-download-btn" class="btn btn-primary btn-block download-btn" download="resized-image.jpg">⬇ Download Resized Image</a>
          </div>
        </div>
      </div>

      <!-- Copy & Share Result Actions -->
      <div class="result-actions-bar" id="result-actions-image-resizer">
        <button type="button" class="result-action-btn copy-btn" onclick="copyCurrentResult('image-resizer')" title="Copy Result"><span class="btn-icon">📋</span> Copy Result</button>
        <button type="button" class="result-action-btn share-btn" onclick="shareCurrentResult('image-resizer')" title="Share Result"><span class="btn-icon">↗️</span> Share Result</button>
      </div>

      <!-- Related Calculators & Tools Section -->
      <div class="related-tools-section" data-tool="image-resizer"></div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2 class="prose-title">About Image Resizer - Change Image Dimensions Online</h2>
        <p class="prose-lead">Image Resizer lets you change the resolution and dimensions of digital pictures in seconds. Whether adapting a wallpaper for smartphone screens, preparing product photos for an online store, or resizing an avatar to standard dimensions, you have full pixel-level control with smart aspect ratio preservation.</p>

        <h3 class="prose-h3">How to Resize Images</h3>
        <ol class="prose-list">
          <li><strong>Upload Photo:</strong> Pick any image file or drag it directly onto the drop zone.</li>
          <li><strong>Set Target Dimensions:</strong> Enter your desired Width or Height in pixels, or click a popular preset (like 1920×1080 or 50% Scale).</li>
          <li><strong>Lock Aspect Ratio:</strong> Keep "Lock Aspect Ratio" checked to automatically calculate the paired dimension without stretching or squishing.</li>
          <li><strong>Resize &amp; Review:</strong> Click "Resize Image" and check the preview image and updated file size.</li>
          <li><strong>Download:</strong> Tap the download button to save the resized image file.</li>
        </ol>

        <h3 class="prose-h3">Key Features &amp; Benefits</h3>
        <ul class="prose-features">
          <li><strong>Anti-Aliased Resampling:</strong> Canvas bicubic smoothing preserves fine text, textures, and gradient details.</li>
          <li><strong>Distortion Protection:</strong> Smart aspect ratio lock calculates proportional heights or widths in real time.</li>
          <li><strong>One-Click Presets:</strong> Rapidly select Full HD (1080p), HD (720p), Instagram Square (1080×1080), or percentage cuts.</li>
          <li><strong>Confidential &amp; Local:</strong> The entire resizing calculation runs inside your browser sandbox without network uploads.</li>
        </ul>

        <h3 class="prose-h3">Practical Use Case Examples</h3>
        <div class="example-box">
          <div class="example-title">Example 1: Social Media Profile Picture Sizing</div>
          <p class="example-desc">A professional needs a 400×400 pixel headshot for their employee portal, but their photographer gave them a 4000×4000 pixel raw file. Image Resizer downsamples the image to exactly 400×400 px in 0.2 seconds without loss of facial crispness.</p>
        </div>
        <div class="example-box">
          <div class="example-title">Example 2: E-Commerce Store Listing Guidelines</div>
          <p class="example-desc">An online seller has product photos taken in 4032×3024 resolution. The marketplace requires photos no wider than 1200 pixels. With Lock Aspect Ratio active, typing 1200 in the Width automatically computes 900 for Height, ensuring marketplace compliance.</p>
        </div>

        <h3 class="prose-h3">Frequently Asked Questions</h3>
        <div class="faq-list">
          <div class="faq-item">
            <div class="faq-q">What is the difference between image resizing and image compressing?</div>
            <div class="faq-a">Resizing modifies the actual pixel width and height dimensions of an image (e.g. from 3000px to 1500px). Compressing reduces file size in bytes while retaining the original pixel dimensions.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Does resizing stretch or distort my picture?</div>
            <div class="faq-a">No, as long as "Lock Aspect Ratio" remains enabled. Changing the width will proportionally adjust the height to maintain the natural geometry of your subject.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can I enlarge a small photo with this tool?</div>
            <div class="faq-a">Yes. You can upscale smaller images, though upscaling cannot invent missing optical details that were not in the original file.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Which image formats are supported?</div>
            <div class="faq-a">JPG, JPEG, PNG, WebP, GIF, and SVG formats are natively supported for loading and resizing.</div>
          </div>
        </div>
      </div>

{ADSTERRA_BANNER}
    </section>"""

# 7. JPG TO PNG CONVERTER
TOOLS_HTML_2["jpg-to-png"] = f"""    <!-- ==================== 42. JPG TO PNG CONVERTER ==================== -->
    <section id="screen-jpg-to-png" class="screen-section">
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

        <div class="file-dropzone" id="jpg2png-dropzone" onclick="document.getElementById('jpg2png-input').click()">
          <input type="file" id="jpg2png-input" accept=".jpg,.jpeg,image/jpeg" style="display:none;" onchange="handleJpgToPngFile(this.files[0])">
          <div class="dropzone-icon">🔁</div>
          <div class="dropzone-text"><strong>Choose a JPG / JPEG file</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Converts lossy JPEG files into uncompressed PNG graphics</div>
        </div>

        <div id="jpg2png-controls" style="display:none; margin-top: 18px;">
          <div class="file-summary-card">
            <div class="file-summary-icon">🖼️</div>
            <div class="file-summary-info">
              <div class="file-summary-name" id="jpg2png-filename">photo.jpg</div>
              <div class="file-summary-meta">Source: <strong class="text-primary">JPEG</strong> | Size: <span id="jpg2png-orig-size">0 KB</span> | Resolution: <span id="jpg2png-orig-dims">0 × 0 px</span></div>
            </div>
          </div>
        </div>

        <div id="jpg2png-error" class="error-banner" style="display:none;"></div>

        <div class="btn-row" id="jpg2png-action-row" style="display:none;">
          <button type="button" class="btn btn-primary" onclick="runJpgToPng()">Convert to PNG</button>
          <button type="button" class="btn btn-outline" onclick="resetJpgToPng()">Reset</button>
        </div>

        <div id="jpg2png-result" class="result-card" style="display:none;">
          <h3 class="result-header">PNG Conversion Complete</h3>
          <div class="stat-highlight">
            <span class="highlight-number text-emerald">PNG</span>
            <span class="highlight-unit">Format Ready</span>
          </div>
          <div class="stats-pills-row">
            <div class="stat-pill">New File Size: <strong id="jpg2png-res-size">0 KB</strong></div>
            <div class="stat-pill">Quality: <strong>Lossless (Full Bit Depth)</strong></div>
          </div>
          <div class="image-preview-wrapper" style="margin-top: 16px;">
            <img id="jpg2png-preview" class="image-preview-box" alt="PNG Preview">
          </div>
          <div style="margin-top: 16px;">
            <a id="jpg2png-download-btn" class="btn btn-primary btn-block download-btn" download="converted-image.png">⬇ Download PNG Image</a>
          </div>
        </div>
      </div>

      <!-- Copy & Share Result Actions -->
      <div class="result-actions-bar" id="result-actions-jpg-to-png">
        <button type="button" class="result-action-btn copy-btn" onclick="copyCurrentResult('jpg-to-png')" title="Copy Result"><span class="btn-icon">📋</span> Copy Result</button>
        <button type="button" class="result-action-btn share-btn" onclick="shareCurrentResult('jpg-to-png')" title="Share Result"><span class="btn-icon">↗️</span> Share Result</button>
      </div>

      <!-- Related Calculators & Tools Section -->
      <div class="related-tools-section" data-tool="jpg-to-png"></div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2 class="prose-title">About JPG to PNG Converter - Free Online Image Transformation</h2>
        <p class="prose-lead">JPG to PNG Converter transforms standard lossy JPEG photos and illustrations into clean, uncompressed Portable Network Graphics (PNG). PNG is the gold standard format for graphic designers, digital artists, and developers who require lossless editing fidelity without cumulative compression artifacts.</p>

        <h3 class="prose-h3">How to Convert JPG to PNG</h3>
        <ol class="prose-list">
          <li><strong>Upload JPG:</strong> Drag your .jpg or .jpeg file into the converter box or tap to browse your gallery.</li>
          <li><strong>Verify File Details:</strong> The tool verifies image dimensions and file characteristics locally.</li>
          <li><strong>Convert to PNG:</strong> Click "Convert to PNG" to process the bitmap directly inside an HTML5 rendering pipeline.</li>
          <li><strong>Preview &amp; Download:</strong> Inspect the converted PNG and click "Download PNG Image" to save it without any watermarks.</li>
        </ol>

        <h3 class="prose-h3">Key Features &amp; Benefits</h3>
        <ul class="prose-features">
          <li><strong>Zero Generative Loss:</strong> Prevents JPEG re-compression degradation when preparing assets for graphic editing suites.</li>
          <li><strong>Instantaneous:</strong> Operates at native device speed with zero network latency.</li>
          <li><strong>Complete Privacy:</strong> Your photos never touch a cloud server.</li>
          <li><strong>Universal Platform Support:</strong> Compatible with Android smartphones, iPhones, iPad, Chromebooks, and PCs.</li>
        </ul>

        <h3 class="prose-h3">Practical Use Case Examples</h3>
        <div class="example-box">
          <div class="example-title">Example 1: Preparing Images for Alpha Transparency Editing</div>
          <p class="example-desc">A designer has a company logo saved as a JPG with a white background. Converting it to PNG allows them to open it in an image editor and cleanly isolate the transparent background, which the JPG format does not support.</p>
        </div>
        <div class="example-box">
          <div class="example-title">Example 2: Submitting Assets to Print &amp; Publishing Houses</div>
          <p class="example-desc">A commercial printer requires marketing assets in PNG to prevent lossy JPEG blocking artifacts during high-DPI offset printing. JPG to PNG effortlessly provides the required format.</p>
        </div>

        <h3 class="prose-h3">Frequently Asked Questions</h3>
        <div class="faq-list">
          <div class="faq-item">
            <div class="faq-q">Does converting JPG to PNG improve image quality?</div>
            <div class="faq-a">Converting to PNG prevents any further quality loss during subsequent saves and edits. However, it cannot restore optical data that was already discarded when the original JPG was compressed.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Why is the resulting PNG file size sometimes larger than the original JPG?</div>
            <div class="faq-a">PNG uses lossless compression algorithms that store exact color pixel values, whereas JPG uses lossy compression that discards subtle color frequencies to save space.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Will my converted PNG have a transparent background?</div>
            <div class="faq-a">Original JPG files cannot contain transparency. The converted PNG accurately replicates the original image colors and enables you to add transparency in editing software if desired.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Is there any file size limit?</div>
            <div class="faq-a">Because conversion is executed in browser memory, you can convert high-resolution camera photos smoothly without upload limitations.</div>
          </div>
        </div>
      </div>

{ADSTERRA_BANNER}
    </section>"""

# 8. PNG TO JPG CONVERTER
TOOLS_HTML_2["png-to-jpg"] = f"""    <!-- ==================== 43. PNG TO JPG CONVERTER ==================== -->
    <section id="screen-png-to-jpg" class="screen-section">
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

        <div class="file-dropzone" id="png2jpg-dropzone" onclick="document.getElementById('png2jpg-input').click()">
          <input type="file" id="png2jpg-input" accept=".png,image/png" style="display:none;" onchange="handlePngToJpgFile(this.files[0])">
          <div class="dropzone-icon">🔄</div>
          <div class="dropzone-text"><strong>Choose a PNG file</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Converts PNG files into lightweight, universally compatible JPG images</div>
        </div>

        <div id="png2jpg-controls" style="display:none; margin-top: 18px;">
          <div class="file-summary-card">
            <div class="file-summary-icon">🖼️</div>
            <div class="file-summary-info">
              <div class="file-summary-name" id="png2jpg-filename">graphic.png</div>
              <div class="file-summary-meta">Original Size: <span id="png2jpg-orig-size">0 KB</span> | Resolution: <span id="png2jpg-orig-dims">0 × 0 px</span></div>
            </div>
          </div>

          <div class="input-grid-2" style="margin-top: 16px;">
            <div class="input-group">
              <label for="png2jpg-bg-color">Background Color (for transparent pixels)</label>
              <div class="color-picker-row">
                <input type="color" id="png2jpg-bg-color" value="#ffffff" onchange="updatePng2JpgBg(this.value)">
                <span id="png2jpg-bg-hex" class="color-hex-badge">#ffffff (White)</span>
              </div>
            </div>
            <div class="input-group">
              <label for="png2jpg-quality">JPG Quality (<span id="png2jpg-quality-val">85%</span>)</label>
              <input type="range" id="png2jpg-quality" min="10" max="100" value="85" step="1" oninput="updatePng2JpgQuality(this.value)">
            </div>
          </div>
        </div>

        <div id="png2jpg-error" class="error-banner" style="display:none;"></div>

        <div class="btn-row" id="png2jpg-action-row" style="display:none;">
          <button type="button" class="btn btn-primary" onclick="runPngToJpg()">Convert to JPG</button>
          <button type="button" class="btn btn-outline" onclick="resetPngToJpg()">Reset</button>
        </div>

        <div id="png2jpg-result" class="result-card" style="display:none;">
          <h3 class="result-header">JPG Conversion Complete</h3>
          <div class="comparison-stats-grid">
            <div class="comp-stat-col">
              <span class="comp-stat-label">Original PNG</span>
              <span class="comp-stat-val" id="png2jpg-res-orig">0 KB</span>
            </div>
            <div class="comp-stat-arrow">→</div>
            <div class="comp-stat-col">
              <span class="comp-stat-label">New JPG Size</span>
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
            <a id="png2jpg-download-btn" class="btn btn-primary btn-block download-btn" download="converted-image.jpg">⬇ Download JPG Image</a>
          </div>
        </div>
      </div>

      <!-- Copy & Share Result Actions -->
      <div class="result-actions-bar" id="result-actions-png-to-jpg">
        <button type="button" class="result-action-btn copy-btn" onclick="copyCurrentResult('png-to-jpg')" title="Copy Result"><span class="btn-icon">📋</span> Copy Result</button>
        <button type="button" class="result-action-btn share-btn" onclick="shareCurrentResult('png-to-jpg')" title="Share Result"><span class="btn-icon">↗️</span> Share Result</button>
      </div>

      <!-- Related Calculators & Tools Section -->
      <div class="related-tools-section" data-tool="png-to-jpg"></div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2 class="prose-title">About PNG to JPG Converter - Fast Browser-Based Image Conversion</h2>
        <p class="prose-lead">PNG to JPG Converter transforms heavy PNG image files into compact, universally compatible JPG photos. Because PNGs do not have native JPEG compression, screenshots and illustrations can easily balloon to 5–10 megabytes. This tool shrinks file sizes while giving you full control over background color for transparent artwork.</p>

        <h3 class="prose-h3">How to Convert PNG to JPG</h3>
        <ol class="prose-list">
          <li><strong>Upload PNG:</strong> Drag or pick your .png image into the upload card.</li>
          <li><strong>Choose Background Color:</strong> Because JPG does not support transparent alpha pixels, pick a background color (default is pure White #FFFFFF) to fill any transparent regions.</li>
          <li><strong>Adjust Quality:</strong> Set your preferred JPG compression quality level (default 85%).</li>
          <li><strong>Click Convert to JPG:</strong> The canvas renders the background fill and overlays your image instantly.</li>
          <li><strong>Download:</strong> Tap the download button to save your newly optimized JPG file.</li>
        </ol>

        <h3 class="prose-h3">Key Features &amp; Benefits</h3>
        <ul class="prose-features">
          <li><strong>Custom Transparent Pixel Fill:</strong> Avoid ugly black boxes on transparent logos by choosing white, black, or custom brand colors.</li>
          <li><strong>Massive File Savings:</strong> Reduce screenshot and graphic file sizes by up to 70–85%.</li>
          <li><strong>Strict Local Privacy:</strong> Works 100% inside your browser with no network transmission.</li>
          <li><strong>Universal Compatibility:</strong> Output JPGs open flawlessly in all image viewers, legacy web browsers, and mobile devices.</li>
        </ul>

        <h3 class="prose-h3">Practical Use Case Examples</h3>
        <div class="example-box">
          <div class="example-title">Example 1: Compressing Phone Screenshots for Faster Sharing</div>
          <p class="example-desc">Screenshots taken on modern Android phones are saved automatically as 4.5 MB PNGs. Converting them with PNG to JPG produces a crisp 320 KB JPG that shares in half a second over messaging apps.</p>
        </div>
        <div class="example-box">
          <div class="example-title">Example 2: Uploading Transparent Logos to Form Portals</div>
          <p class="example-desc">An applicant needs to upload a company badge to a government certification portal that rejects PNGs. Using PNG to JPG with a white background fill creates an accepted JPG document in seconds.</p>
        </div>

        <h3 class="prose-h3">Frequently Asked Questions</h3>
        <div class="faq-list">
          <div class="faq-item">
            <div class="faq-q">Why do transparent areas turn black in other JPG converters?</div>
            <div class="faq-a">JPG does not support transparency. Standard converters default to black when discarding alpha channels. Our tool lets you choose white or custom colors so your graphics always look intentional and professional.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How much file size reduction can I expect?</div>
            <div class="faq-a">For continuous-tone photos and complex graphics originally saved as PNG, converting to JPG typically slashes file size by 60% to 85%.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Is the converted JPG watermark-free?</div>
            <div class="faq-a">Yes! All converted images are 100% clean and free of watermarks or branding.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Does the converter require an internet connection?</div>
            <div class="faq-a">No. Processing executes entirely via the client-side browser Canvas API.</div>
          </div>
        </div>
      </div>

{ADSTERRA_BANNER}
    </section>"""

# 9. IMAGE CROPPER
TOOLS_HTML_2["image-cropper"] = f"""    <!-- ==================== 44. IMAGE CROPPER ==================== -->
    <section id="screen-image-cropper" class="screen-section">
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

        <div class="file-dropzone" id="imgcrop-dropzone" onclick="document.getElementById('imgcrop-input').click()">
          <input type="file" id="imgcrop-input" accept="image/*" style="display:none;" onchange="handleImageCropperFile(this.files[0])">
          <div class="dropzone-icon">✂️</div>
          <div class="dropzone-text"><strong>Choose an Image</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Crop avatars, banners, and photos to exact shapes</div>
        </div>

        <div id="imgcrop-controls" style="display:none; margin-top: 18px;">
          <div class="aspect-ratio-selector">
            <span class="aspect-label">Aspect Ratio:</span>
            <div class="tab-bar aspect-tabs" style="margin-bottom: 0;">
              <button type="button" class="tab-btn active" id="crop-ratio-free" onclick="setCropRatio('free')">Freeform</button>
              <button type="button" class="tab-btn" id="crop-ratio-1-1" onclick="setCropRatio('1:1')">1:1 Square</button>
              <button type="button" class="tab-btn" id="crop-ratio-4-3" onclick="setCropRatio('4:3')">4:3 Standard</button>
              <button type="button" class="tab-btn" id="crop-ratio-16-9" onclick="setCropRatio('16:9')">16:9 Banner</button>
            </div>
          </div>

          <div class="crop-workspace-container" style="margin-top: 16px;">
            <div class="canvas-crop-wrapper">
              <canvas id="imgcrop-canvas"></canvas>
            </div>
            <div class="crop-slider-controls">
              <div class="crop-slider-row">
                <label>Horizontal Position (X)</label>
                <input type="range" id="crop-pos-x" min="0" max="100" value="50" oninput="onCropParamChange()">
              </div>
              <div class="crop-slider-row">
                <label>Vertical Position (Y)</label>
                <input type="range" id="crop-pos-y" min="0" max="100" value="50" oninput="onCropParamChange()">
              </div>
              <div class="crop-slider-row">
                <label>Crop Size / Zoom</label>
                <input type="range" id="crop-size" min="20" max="100" value="80" oninput="onCropParamChange()">
              </div>
            </div>
          </div>
        </div>

        <div id="imgcrop-error" class="error-banner" style="display:none;"></div>

        <div class="btn-row" id="imgcrop-action-row" style="display:none;">
          <button type="button" class="btn btn-primary" onclick="runImageCrop()">Apply Crop</button>
          <button type="button" class="btn btn-outline" onclick="resetImageCropper()">Reset</button>
        </div>

        <div id="imgcrop-result" class="result-card" style="display:none;">
          <h3 class="result-header">Cropped Image Ready</h3>
          <div class="stat-highlight">
            <span id="imgcrop-res-dims" class="highlight-number">0 × 0</span>
            <span class="highlight-unit">Pixels</span>
          </div>
          <div class="stats-pills-row">
            <div class="stat-pill">Ratio: <strong id="imgcrop-res-ratio">1:1</strong></div>
            <div class="stat-pill">File Size: <strong id="imgcrop-res-size">0 KB</strong></div>
          </div>
          <div class="image-preview-wrapper" style="margin-top: 16px;">
            <img id="imgcrop-preview" class="image-preview-box" alt="Cropped Preview">
          </div>
          <div style="margin-top: 16px;">
            <a id="imgcrop-download-btn" class="btn btn-primary btn-block download-btn" download="cropped-image.png">⬇ Download Cropped Image</a>
          </div>
        </div>
      </div>

      <!-- Copy & Share Result Actions -->
      <div class="result-actions-bar" id="result-actions-image-cropper">
        <button type="button" class="result-action-btn copy-btn" onclick="copyCurrentResult('image-cropper')" title="Copy Result"><span class="btn-icon">📋</span> Copy Result</button>
        <button type="button" class="result-action-btn share-btn" onclick="shareCurrentResult('image-cropper')" title="Share Result"><span class="btn-icon">↗️</span> Share Result</button>
      </div>

      <!-- Related Calculators & Tools Section -->
      <div class="related-tools-section" data-tool="image-cropper"></div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2 class="prose-title">About Image Cropper - Cut Photos to Standard Aspect Ratios</h2>
        <p class="prose-lead">Image Cropper provides precise interactive cropping for digital images, allowing you to isolate the perfect frame from photos. With dedicated aspect ratio presets for 1:1 Square (social media avatars), 4:3 Standard (photography &amp; prints), 16:9 Widescreen (YouTube thumbnails &amp; video banners), or Freeform trimming, you get pixel-accurate results every time.</p>

        <h3 class="prose-h3">How to Crop an Image</h3>
        <ol class="prose-list">
          <li><strong>Upload Photo:</strong> Pick any photo from your phone or drag it into the upload box.</li>
          <li><strong>Select Ratio Preset:</strong> Click 1:1 for square profile avatars, 16:9 for YouTube/website banners, 4:3 for camera prints, or Freeform for arbitrary bounds.</li>
          <li><strong>Adjust Crop Frame:</strong> Use the interactive position and zoom sliders to position the crop box exactly over your focal subject.</li>
          <li><strong>Click Apply Crop:</strong> The canvas renders the high-resolution crop region in real time.</li>
          <li><strong>Download:</strong> Tap the download button to save your cropped image immediately.</li>
        </ol>

        <h3 class="prose-h3">Key Features &amp; Benefits</h3>
        <ul class="prose-features">
          <li><strong>Popular Aspect Ratio Presets:</strong> Quickly match the dimensional specifications of YouTube, Instagram, Twitter/X, and LinkedIn.</li>
          <li><strong>Live Canvas Feedback:</strong> See the exact crop boundaries visually overlaid before exporting.</li>
          <li><strong>Full Resolution Output:</strong> Extracts from the native source resolution without unwanted blur.</li>
          <li><strong>Completely Private:</strong> Processing happens entirely within the security boundary of your device.</li>
        </ul>

        <h3 class="prose-h3">Practical Use Case Examples</h3>
        <div class="example-box">
          <div class="example-title">Example 1: Creating a Perfect 1:1 Profile Avatar</div>
          <p class="example-desc">A user takes a portrait photo with extra background space. Selecting the 1:1 Square preset and adjusting the position slider places their face squarely in the center, producing a tailored avatar for WhatsApp or LinkedIn.</p>
        </div>
        <div class="example-box">
          <div class="example-title">Example 2: Crafting a 16:9 Widescreen Blog Banner</div>
          <p class="example-desc">A content creator captures a vertical camera shot but needs a horizontal 16:9 header image for their blog article. Image Cropper's 16:9 preset extracts the focal horizontal strip at maximum clarity.</p>
        </div>

        <h3 class="prose-h3">Frequently Asked Questions</h3>
        <div class="faq-list">
          <div class="faq-item">
            <div class="faq-q">Does cropping lower the clarity of my photo?</div>
            <div class="faq-a">No! The cropped region is extracted at the native pixel density of the source photo, preserving full resolution.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can I crop transparent PNG images?</div>
            <div class="faq-a">Yes. PNG transparency is preserved intact when downloading the cropped output.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Are there any file upload caps?</div>
            <div class="faq-a">There are no artificial upload limits because your browser processes the image locally.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can I use this on my mobile phone?</div>
            <div class="faq-a">Yes. The touch-friendly controls are designed for smooth single-finger operation on mobile devices.</div>
          </div>
        </div>
      </div>

{ADSTERRA_BANNER}
    </section>"""

# 10. IMAGE TO WEBP CONVERTER
TOOLS_HTML_2["image-to-webp"] = f"""    <!-- ==================== 45. IMAGE TO WEBP CONVERTER ==================== -->
    <section id="screen-image-to-webp" class="screen-section">
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

        <div class="file-dropzone" id="img2webp-dropzone" onclick="document.getElementById('img2webp-input').click()">
          <input type="file" id="img2webp-input" accept="image/jpeg,image/png,image/gif" style="display:none;" onchange="handleImageToWebpFile(this.files[0])">
          <div class="dropzone-icon">⚡</div>
          <div class="dropzone-text"><strong>Choose an Image (JPG or PNG)</strong> or drag &amp; drop here</div>
          <div class="dropzone-sub">Converts standard images to Google's next-gen high-efficiency WebP format</div>
        </div>

        <div id="img2webp-controls" style="display:none; margin-top: 18px;">
          <div class="file-summary-card">
            <div class="file-summary-icon">🖼️</div>
            <div class="file-summary-info">
              <div class="file-summary-name" id="img2webp-filename">photo.jpg</div>
              <div class="file-summary-meta">Original Size: <strong id="img2webp-orig-size" class="text-primary">0 KB</strong> | Resolution: <span id="img2webp-orig-dims">0 × 0 px</span></div>
            </div>
          </div>

          <div class="slider-control-group" style="margin-top: 16px;">
            <div class="slider-header">
              <label for="img2webp-quality"><strong>WebP Compression Quality</strong></label>
              <span id="img2webp-quality-val" class="slider-badge">80%</span>
            </div>
            <input type="range" id="img2webp-quality" min="10" max="100" value="80" step="1" oninput="updateWebpQuality(this.value)">
            <div class="slider-ticks">
              <span>Ultra Compact (10%)</span>
              <span>Recommended (80%)</span>
              <span>Lossless / Near-Lossless (100%)</span>
            </div>
          </div>
        </div>

        <div id="img2webp-error" class="error-banner" style="display:none;"></div>

        <div class="btn-row" id="img2webp-action-row" style="display:none;">
          <button type="button" class="btn btn-primary" onclick="runImageToWebp()">Convert to WebP</button>
          <button type="button" class="btn btn-outline" onclick="resetImageToWebp()">Reset</button>
        </div>

        <div id="img2webp-result" class="result-card" style="display:none;">
          <h3 class="result-header">WebP Conversion Complete</h3>
          <div class="comparison-stats-grid">
            <div class="comp-stat-col">
              <span class="comp-stat-label">Original Image</span>
              <span class="comp-stat-val" id="img2webp-res-orig">0 KB</span>
            </div>
            <div class="comp-stat-arrow">→</div>
            <div class="comp-stat-col">
              <span class="comp-stat-label">WebP File Size</span>
              <span class="comp-stat-val text-emerald" id="img2webp-res-new">0 KB</span>
            </div>
            <div class="comp-stat-col">
              <span class="comp-stat-label">Bandwidth Saved</span>
              <span class="comp-stat-badge" id="img2webp-res-saved">-0%</span>
            </div>
          </div>
          <div class="image-preview-wrapper" style="margin-top: 16px;">
            <img id="img2webp-preview" class="image-preview-box" alt="WebP Preview">
          </div>
          <div style="margin-top: 16px;">
            <a id="img2webp-download-btn" class="btn btn-primary btn-block download-btn" download="converted-image.webp">⬇ Download WebP Image</a>
          </div>
        </div>
      </div>

      <!-- Copy & Share Result Actions -->
      <div class="result-actions-bar" id="result-actions-image-to-webp">
        <button type="button" class="result-action-btn copy-btn" onclick="copyCurrentResult('image-to-webp')" title="Copy Result"><span class="btn-icon">📋</span> Copy Result</button>
        <button type="button" class="result-action-btn share-btn" onclick="shareCurrentResult('image-to-webp')" title="Share Result"><span class="btn-icon">↗️</span> Share Result</button>
      </div>

      <!-- Related Calculators & Tools Section -->
      <div class="related-tools-section" data-tool="image-to-webp"></div>

      <!-- SEO Prose Section -->
      <div class="card prose-card">
        <h2 class="prose-title">About Image to WebP Converter - Next-Gen Web Optimization</h2>
        <p class="prose-lead">Image to WebP Converter transforms traditional JPG, JPEG, and PNG images into Google's modern WebP format. WebP is specifically engineered for the modern internet, delivering 25% to 35% smaller file sizes than comparable JPEGs and up to 80% smaller than PNGs while preserving transparent backgrounds and vivid color gamuts.</p>

        <h3 class="prose-h3">How to Convert Images to WebP</h3>
        <ol class="prose-list">
          <li><strong>Upload Image:</strong> Select or drop your JPG or PNG image into the upload box.</li>
          <li><strong>Set Quality Level:</strong> Choose your quality level using the slider (80% is recommended for the ideal balance between small size and razor-sharp clarity).</li>
          <li><strong>Click Convert to WebP:</strong> The browser's native canvas engine compresses the image into modern WebP binary streams.</li>
          <li><strong>Compare &amp; Download:</strong> Review the bandwidth savings comparison and click "Download WebP Image".</li>
        </ol>

        <h3 class="prose-h3">Key Features &amp; Benefits</h3>
        <ul class="prose-features">
          <li><strong>Next-Gen Compression Efficiency:</strong> Slashing file sizes speeds up website load times and reduces mobile data usage.</li>
          <li><strong>Transparency Support:</strong> Unlike JPG, WebP supports full alpha transparency channels with smaller file sizes than PNG.</li>
          <li><strong>SEO Performance Booster:</strong> Google Search favors fast-loading websites that utilize modern image formats like WebP.</li>
          <li><strong>Zero Cloud Uploads:</strong> Safe for proprietary company graphics and personal family photos.</li>
        </ul>

        <h3 class="prose-h3">Practical Use Case Examples</h3>
        <div class="example-box">
          <div class="example-title">Example 1: Boosting Website Core Web Vitals</div>
          <p class="example-desc">A web developer has 15 PNG product photos on an e-commerce catalog page. Converting them to WebP cuts total page payload from 18 MB down to 2.4 MB, dramatically reducing Largest Contentful Paint (LCP) and bounce rates.</p>
        </div>
        <div class="example-box">
          <div class="example-title">Example 2: Mobile App Asset Size Optimization</div>
          <p class="example-desc">An Android app developer converts UI background illustrations to WebP, trimming 12 MB from the final APK download size on Google Play.</p>
        </div>

        <h3 class="prose-h3">Frequently Asked Questions</h3>
        <div class="faq-list">
          <div class="faq-item">
            <div class="faq-q">Which web browsers support WebP images?</div>
            <div class="faq-a">WebP is natively supported across all modern browsers including Google Chrome, Apple Safari, Mozilla Firefox, Microsoft Edge, and Opera on both desktop and mobile.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Does WebP support transparency?</div>
            <div class="faq-a">Yes! WebP supports both 8-bit alpha transparency and 24-bit RGB color depth, making it a superior, lightweight replacement for PNG.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">How much bandwidth can WebP save?</div>
            <div class="faq-a">According to Google performance studies, WebP images are 26% smaller compared to PNGs and 25-34% smaller than JPEG images at equivalent structural similarity (SSIM) quality.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Is this converter private and secure?</div>
            <div class="faq-a">Yes. All conversion logic runs strictly within your browser. No files are uploaded to our servers.</div>
          </div>
        </div>
      </div>

{ADSTERRA_BANNER}
    </section>"""

print("Generated second 5 HTML sections.")
