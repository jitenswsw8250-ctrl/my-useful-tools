with open('tools_pdf_image_js.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. In PDF Split, use sourcePdf.getPageIndices().filter(i => targetIndices.includes(i))
old_split = "const copiedPages = await splitPdf.copyPages(sourcePdf, targetIndices);"
new_split = """// Ensure indices are strictly typed and compatible across all environments
    const allIndices = sourcePdf.getPageIndices();
    const safeIndices = allIndices.filter(idx => targetIndices.includes(idx));
    const copiedPages = await splitPdf.copyPages(sourcePdf, safeIndices);"""

if old_split in code:
    code = code.replace(old_split, new_split)
    print("Updated PDF Split copyPages.")
else:
    print("Warning: old_split not found!")

# 2. In Images to PDF, ensure Uint8Array is used for embedPng
old_img2pdf = "const embeddedImg = await pdfDoc.embedPng(pngBytes);"
new_img2pdf = "const embeddedImg = await pdfDoc.embedPng(new Uint8Array(pngBytes));"

if old_img2pdf in code:
    code = code.replace(old_img2pdf, new_img2pdf)
    print("Updated Images to PDF embedPng with new Uint8Array.")
else:
    print("Warning: old_img2pdf not found!")

# 3. In Image Resizer, fallback to natural dimensions if inputs not yet populated
old_resizer = """  const w = parseInt(document.getElementById('imgresize-width').value, 10);
  const h = parseInt(document.getElementById('imgresize-height').value, 10);

  if (!w || !h || w <= 0 || h <= 0) {"""

new_resizer = """  let w = parseInt(document.getElementById('imgresize-width').value, 10);
  let h = parseInt(document.getElementById('imgresize-height').value, 10);

  if ((!w || !h || w <= 0 || h <= 0) && imgResizeLoadedImage) {
    w = imgResizeLoadedImage.naturalWidth;
    h = imgResizeLoadedImage.naturalHeight;
    document.getElementById('imgresize-width').value = w;
    document.getElementById('imgresize-height').value = h;
  }

  if (!w || !h || w <= 0 || h <= 0) {"""

if old_resizer in code:
    code = code.replace(old_resizer, new_resizer)
    print("Updated Image Resizer fallback.")
else:
    print("Warning: old_resizer not found!")

with open('tools_pdf_image_js.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("tools_pdf_image_js.py updated.")
