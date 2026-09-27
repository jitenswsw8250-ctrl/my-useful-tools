# integrate_10_tools.py
# Integrates all 10 PDF & Image tools into index.html, script.js, style.css, and sitemap.xml

import os
import re
from add_10_tools import NEW_TOOLS_DATA
from tools_pdf_image_html import TOOLS_HTML
from tools_pdf_image_html_2 import TOOLS_HTML_2
from tools_pdf_image_js import JS_CODE
from tools_pdf_image_css import CSS_CODE

# Merge HTML dictionaries
ALL_10_TOOLS_HTML = {**TOOLS_HTML, **TOOLS_HTML_2}
print(f"Total HTML tool sections ready: {len(ALL_10_TOOLS_HTML)}")

# 1. UPDATE index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add external libraries to <head> if not present
if 'pdf-lib.min.js' not in html:
    head_marker = '<script src="script.js" defer></script>'
    lib_scripts = """  <!-- PDF-Lib & PDF.js for 100% Client-Side PDF Tools -->
  <script src="https://cdn.jsdelivr.net/npm/pdf-lib@1.17.9/dist/pdf-lib.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
  <script src="script.js" defer></script>"""
    html = html.replace(head_marker, lib_scripts)
    print("Added pdf-lib and pdf.js script tags to <head>")

# Update Category Pills:
# 1. Change "All" badge from 35 to 45
old_all_pill = '<span class="cat-label">All</span> <span class="cat-badge">35</span>'
new_all_pill = '<span class="cat-label">All</span> <span class="cat-badge">45</span>'
if old_all_pill in html:
    html = html.replace(old_all_pill, new_all_pill)
    print("Updated All category badge to 45")

# 2. Add "PDF & Image Tools" category pill right after math or converters
pdf_img_pill = """          <button type="button" class="category-pill" data-category="pdf-images" onclick="filterByCategory('pdf-images')" role="tab" aria-selected="false">
            <span class="cat-icon">📄</span> <span class="cat-label">PDF &amp; Image Tools</span> <span class="cat-badge">10</span>
          </button>"""

if 'data-category="pdf-images"' not in html:
    math_pill_marker = '<button type="button" class="category-pill" data-category="math"'
    html = html.replace(math_pill_marker, pdf_img_pill + "\n" + math_pill_marker)
    print("Added PDF & Image Tools category pill")

# Build Grid Cards for the 10 tools
cards_html = ""
for i, t in enumerate(NEW_TOOLS_DATA, 36):
    tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in t['tags']])
    cards_html += f"""
        <!-- Tool {i}: {t['name']} -->
        <div class="tool-card" onclick="navigateTo('{t['id']}')" data-tool-id="{t['id']}" data-category="pdf-images">
          <button type="button" class="card-fav-btn" data-tool-id="{t['id']}" onclick="event.stopPropagation(); toggleFavorite('{t['id']}', event);" aria-label="Favorite {t['id']}" title="Toggle Favorite"><span class="fav-star">☆</span></button>
          <div class="tool-icon-wrapper">{t['icon']}</div>
          <div class="tool-info">
            <h3 class="tool-title">{t['name']}</h3>
            <p class="tool-desc">{t['desc']}</p>
            <div class="tool-tags">
              {tags_html}
            </div>
          </div>
          <button class="tool-action-btn">Open Tool →</button>
        </div>"""

# Insert cards after Tool 35 card
tool_35_marker = '<!-- Tool 35: Sales Tax Calculator -->'
if tool_35_marker in html and '<!-- Tool 36: PDF Merge -->' not in html:
    # Find end of Tool 35 card
    pos35 = html.find(tool_35_marker)
    open_btn = html.find('<button class="tool-action-btn">Open Tool →</button>\n        </div>', pos35)
    end_of_card = open_btn + len('<button class="tool-action-btn">Open Tool →</button>\n        </div>')
    html = html[:end_of_card] + cards_html + html[end_of_card:]
    print("Added 10 new tool cards to home tools grid")

# Build Drawer Navigation Links
drawer_links = ""
for t in NEW_TOOLS_DATA:
    drawer_links += f"""      <a href="#{t['id']}" onclick="navigateTo('{t['id']}')" class="drawer-item" data-screen="{t['id']}">
        <span class="drawer-icon">{t['icon']}</span>
        <span>{t['name']}</span>
      </a>\n"""

# Update drawer count
html = html.replace('ALL CALCULATORS &amp; UTILITIES (35 TOOLS)', 'ALL TOOLS &amp; UTILITIES (45 TOOLS)')
html = html.replace('ALL CALCULATORS & UTILITIES (35 TOOLS)', 'ALL TOOLS & UTILITIES (45 TOOLS)')

if 'data-screen="pdf-merge"' not in html:
    drawer_sales_tax = '<a href="#sales-tax" onclick="navigateTo(\'sales-tax\')" class="drawer-item" data-screen="sales-tax">\n        <span class="drawer-icon">🏷️</span>\n        <span>Sales Tax Calculator</span>\n      </a>'
    if drawer_sales_tax in html:
        html = html.replace(drawer_sales_tax, drawer_sales_tax + "\n" + drawer_links)
        print("Added 10 new tool links to Drawer navigation")

# Build Footer Links
footer_links = ""
for t in NEW_TOOLS_DATA:
    footer_links += f"""          <a href="#{t['id']}" onclick="navigateTo('{t['id']}')">{t['name']}</a>\n"""

html = html.replace('OUR CALCULATORS (35 TOOLS)', 'ALL UTILITIES &amp; TOOLS (45 TOOLS)')

if 'onclick="navigateTo(\'pdf-merge\')"' not in html:
    footer_sales_tax = '<a href="#sales-tax" onclick="navigateTo(\'sales-tax\')">Sales Tax Calculator</a>'
    if footer_sales_tax in html:
        html = html.replace(footer_sales_tax, footer_sales_tax + "\n" + footer_links)
        print("Added 10 new tool links to Footer navigation")

# Insert 10 tool screens right after sales-tax screen
all_screens_html = "\n\n".join([ALL_10_TOOLS_HTML[t['id']] for t in NEW_TOOLS_DATA])

if 'id="screen-pdf-merge"' not in html:
    sales_tax_screen = '<section id="screen-sales-tax" class="screen-section">'
    pos_st = html.find(sales_tax_screen)
    if pos_st != -1:
        end_st = html.find('</section>', pos_st) + len('</section>')
        html = html[:end_st] + "\n\n" + all_screens_html + html[end_st:]
        print("Added 10 new tool screens to index.html")

# Write updated index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html saved successfully.")


# 2. UPDATE script.js
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add to TOOLS_INFO
tools_info_entries = ""
for t in NEW_TOOLS_DATA:
    tools_info_entries += f"  '{t['id']}': {{ name: '{t['name']}', icon: '{t['icon']}', category: '{t['category']}', desc: '{t['desc']}' }},\n"

if "'pdf-merge'" not in js:
    # insert right after sales-tax entry in TOOLS_INFO
    marker = "'sales-tax': { name: 'Sales Tax Calculator'"
    pos = js.find(marker)
    if pos != -1:
        end_line = js.find('\n', pos) + 1
        js = js[:end_line] + tools_info_entries + js[end_line:]
        print("Added 10 tools to TOOLS_INFO in script.js")

# Add to RELATED_TOOLS_MAP
related_map_entries = """  'pdf-merge': ['pdf-split', 'pdf-to-images', 'images-to-pdf', 'image-compressor'],
  'pdf-split': ['pdf-merge', 'pdf-to-images', 'images-to-pdf', 'image-compressor'],
  'pdf-to-images': ['images-to-pdf', 'pdf-merge', 'jpg-to-png', 'image-compressor'],
  'images-to-pdf': ['pdf-to-images', 'pdf-merge', 'image-compressor', 'image-resizer'],
  'image-compressor': ['image-resizer', 'image-to-webp', 'jpg-to-png', 'png-to-jpg'],
  'image-resizer': ['image-cropper', 'image-compressor', 'image-to-webp', 'jpg-to-png'],
  'jpg-to-png': ['png-to-jpg', 'image-to-webp', 'image-compressor', 'image-resizer'],
  'png-to-jpg': ['jpg-to-png', 'image-to-webp', 'image-compressor', 'image-resizer'],
  'image-cropper': ['image-resizer', 'image-compressor', 'jpg-to-png', 'png-to-jpg'],
  'image-to-webp': ['image-compressor', 'jpg-to-png', 'png-to-jpg', 'image-resizer'],
"""

if "'pdf-merge':" not in js:
    marker = "'sales-tax': ['discount'"
    pos = js.find(marker)
    if pos != -1:
        end_line = js.find('\n', pos) + 1
        js = js[:end_line] + related_map_entries + js[end_line:]
        print("Added 10 tools to RELATED_TOOLS_MAP in script.js")

# Add search aliases
search_aliases_code = """    if (toolId.startsWith('pdf') || toolId === 'images-to-pdf') {
      aliases.push('pdf', 'pdf tool', 'document', 'pdf merge', 'pdf split', 'pdf to images', 'images to pdf');
    }
    if (toolId.startsWith('image') || toolId.includes('jpg') || toolId.includes('png') || toolId.includes('webp')) {
      aliases.push('image', 'photo', 'picture', 'jpg', 'png', 'webp', 'compress', 'resize', 'crop', 'converter');
    }
"""

if "toolId.startsWith('pdf')" not in js:
    marker = "if (toolId === 'emi'"
    pos = js.find(marker)
    if pos != -1:
        js = js[:pos] + search_aliases_code + "    " + js[pos:]
        print("Added search aliases for PDF and Image tools in script.js")

# Add formatters to getResultText(toolId)
result_formatters_code = """  if (toolId === 'pdf-merge') {
    const pages = document.getElementById('pdf-merge-result-pages')?.textContent?.trim() || 'Multiple';
    const size = document.getElementById('pdf-merge-result-size')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - PDF Merge\\nCombined ${pages} Pages into a single PDF (Total: ${size})\\n${url}`;
  }
  if (toolId === 'pdf-split') {
    const pages = document.getElementById('pdf-split-result-pages')?.textContent?.trim() || '1';
    const range = document.getElementById('pdf-split-result-range')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - PDF Split\\nExtracted ${pages} Pages (${range})\\n${url}`;
  }
  if (toolId === 'pdf-to-images') {
    const pages = document.getElementById('pdf2img-rendered-count')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - PDF to Images\\nRendered ${pages} PDF Pages to Images\\n${url}`;
  }
  if (toolId === 'images-to-pdf') {
    const count = document.getElementById('img2pdf-result-count')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - Images to PDF\\nCompiled ${count} Images into PDF\\n${url}`;
  }
  if (toolId === 'image-compressor') {
    const orig = document.getElementById('imgcomp-res-orig')?.textContent?.trim() || '';
    const comp = document.getElementById('imgcomp-res-new')?.textContent?.trim() || '';
    const saving = document.getElementById('imgcomp-res-saving')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - Image Compressor\\nOriginal: ${orig} → Compressed: ${comp} (Saved ${saving})\\n${url}`;
  }
  if (toolId === 'image-resizer') {
    const dims = document.getElementById('imgresize-res-dims')?.textContent?.trim() || '';
    const size = document.getElementById('imgresize-res-size')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - Image Resizer\\nResized Dimensions: ${dims} px (${size})\\n${url}`;
  }
  if (toolId === 'jpg-to-png') {
    const size = document.getElementById('jpg2png-res-size')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - JPG to PNG Converter\\nConverted to Lossless PNG (${size})\\n${url}`;
  }
  if (toolId === 'png-to-jpg') {
    const orig = document.getElementById('png2jpg-res-orig')?.textContent?.trim() || '';
    const nw = document.getElementById('png2jpg-res-new')?.textContent?.trim() || '';
    const red = document.getElementById('png2jpg-res-reduction')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - PNG to JPG Converter\\nOriginal: ${orig} → New JPG: ${nw} (${red})\\n${url}`;
  }
  if (toolId === 'image-cropper') {
    const dims = document.getElementById('imgcrop-res-dims')?.textContent?.trim() || '';
    const ratio = document.getElementById('imgcrop-res-ratio')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - Image Cropper\\nCropped to ${dims} px (${ratio})\\n${url}`;
  }
  if (toolId === 'image-to-webp') {
    const orig = document.getElementById('img2webp-res-orig')?.textContent?.trim() || '';
    const nw = document.getElementById('img2webp-res-new')?.textContent?.trim() || '';
    const saved = document.getElementById('img2webp-res-saved')?.textContent?.trim() || '';
    return `MY USEFUL TOOLS - Image to WebP Converter\\nOriginal: ${orig} → WebP: ${nw} (Saved ${saved})\\n${url}`;
  }
"""

if "toolId === 'pdf-merge'" not in js:
    marker = "if (toolId === 'age')"
    pos = js.find(marker)
    if pos != -1:
        js = js[:pos] + result_formatters_code + "  " + js[pos:]
        print("Added getResultText handlers for 10 tools in script.js")

# Append client-side logic from JS_CODE to script.js
if "handlePdfMergeFiles" not in js:
    js = js + "\n\n" + JS_CODE
    print("Appended client-side JavaScript for all 10 tools to script.js")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("script.js saved successfully.")


# 3. UPDATE style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if ".privacy-notice-box" not in css:
    css = css + "\n\n" + CSS_CODE
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("style.css updated with PDF & Image tool styles.")


# 4. UPDATE sitemap.xml
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

sitemap_entries = ""
base_url = "https://ais-pre-vatqw65fky76dekso6xcwb-447578213146.asia-southeast1.run.app/#"
for t in NEW_TOOLS_DATA:
    if f"#{t['id']}" not in sitemap:
        sitemap_entries += f"""  <url>
    <loc>{base_url}{t['id']}</loc>
    <lastmod>2026-09-27</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>\n"""

if sitemap_entries:
    sitemap = sitemap.replace('</urlset>', sitemap_entries + '</urlset>')
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print("sitemap.xml updated with 10 new URLs.")


# 5. SYNC to public/ and docs/
for folder in ['public', 'docs']:
    for fname in ['index.html', 'script.js', 'style.css', 'sitemap.xml']:
        src = fname
        dst = os.path.join(folder, fname)
        with open(src, 'r', encoding='utf-8') as sf:
            data = sf.read()
        with open(dst, 'w', encoding='utf-8') as df:
            df.write(data)
    print(f"Synchronized files to {folder}/")

print("All 10 tools integrated successfully!")
