import re
import os
import shutil
import importlib.util

print("1. Preparing CSS for PDF & Image Tools...")

CSS_CODE = r'''/* ==========================================================================
   PDF & IMAGE TOOLS - BULLETPROOF, RESPONSIVE, MODERN STYLES
   ========================================================================== */

/* Visually Hidden File Input - Standard Cross-Browser Accessibility */
.visually-hidden-file-input {
  position: absolute !important;
  width: 1px !important;
  height: 1px !important;
  padding: 0 !important;
  margin: -1px !important;
  overflow: hidden !important;
  clip: rect(0, 0, 0, 0) !important;
  white-space: nowrap !important;
  border: 0 !important;
  opacity: 0 !important;
  pointer-events: none !important;
}

/* Privacy Note Box */
.privacy-notice-box {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 14px;
  background: rgba(16, 185, 129, 0.08);
  border: 1px solid rgba(16, 185, 129, 0.28);
  border-radius: 10px;
  margin-bottom: 18px;
  font-size: 0.88rem;
  color: var(--text-main);
  line-height: 1.45;
}

.privacy-icon {
  font-size: 1.25rem;
  flex-shrink: 0;
}

/* File Dropzone - Clickable Label Element */
label.file-dropzone {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 32px 20px;
  border: 2px dashed var(--primary-color, #2563eb);
  background: rgba(37, 99, 235, 0.03);
  border-radius: 14px;
  cursor: pointer;
  text-align: center;
  transition: all 0.2s ease;
  user-select: none;
  min-height: 140px;
  outline: none;
  margin-bottom: 16px;
  width: 100%;
  box-sizing: border-box;
}

label.file-dropzone:hover, label.file-dropzone:focus-within {
  background: rgba(37, 99, 235, 0.08);
  border-color: #1d4ed8;
  transform: translateY(-1px);
}

label.file-dropzone.dragover {
  background: rgba(16, 185, 129, 0.12) !important;
  border-color: #10b981 !important;
  border-style: solid !important;
}

.dropzone-icon {
  font-size: 2.4rem;
  margin-bottom: 8px;
}

.dropzone-text {
  font-size: 1.02rem;
  color: var(--text-main);
  margin-bottom: 4px;
}

.dropzone-sub {
  font-size: 0.82rem;
  color: var(--text-muted);
}

/* File Summary Card */
.file-summary-card {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 14px;
  background: var(--bg-color);
  border: 1px solid var(--surface-border);
  border-radius: 10px;
  margin-top: 14px;
  box-sizing: border-box;
}

.file-summary-thumb {
  width: 54px;
  height: 54px;
  border-radius: 8px;
  object-fit: cover;
  flex-shrink: 0;
  border: 1px solid var(--surface-border);
  background: var(--surface-color);
}

.file-summary-icon {
  font-size: 1.8rem;
  flex-shrink: 0;
  width: 54px;
  height: 54px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(37, 99, 235, 0.08);
  border-radius: 8px;
}

.file-summary-info {
  flex: 1;
  min-width: 0;
}

.file-summary-name {
  font-weight: 700;
  font-size: 0.95rem;
  color: var(--text-main);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.file-summary-meta {
  font-size: 0.82rem;
  color: var(--text-muted);
  margin-top: 2px;
}

/* File Item Lists (Reorderable) */
.file-list-container {
  margin-top: 16px;
}

.file-list-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.file-list-title {
  font-weight: 700;
  font-size: 0.92rem;
  color: var(--text-main);
}

.file-item-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.file-item-row {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  background: var(--bg-color);
  border: 1px solid var(--surface-border);
  border-radius: 8px;
  transition: all 0.15s ease;
}

.file-item-row:hover {
  border-color: var(--primary-color, #2563eb);
}

.file-item-idx {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--text-muted);
  width: 22px;
  flex-shrink: 0;
}

.file-item-thumb {
  width: 42px;
  height: 42px;
  border-radius: 6px;
  object-fit: cover;
  border: 1px solid var(--surface-border);
  flex-shrink: 0;
}

.file-item-icon {
  font-size: 1.4rem;
  flex-shrink: 0;
}

.file-item-details {
  flex: 1;
  min-width: 0;
}

.file-item-name {
  display: block;
  font-weight: 600;
  font-size: 0.88rem;
  color: var(--text-main);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.file-item-size {
  display: block;
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-top: 2px;
}

.file-item-actions {
  display: flex;
  gap: 4px;
  flex-shrink: 0;
}

.btn-icon-order, .btn-icon-delete {
  padding: 6px 9px;
  font-size: 0.85rem;
  border-radius: 6px;
  border: 1px solid var(--surface-border);
  background: var(--surface-color);
  color: var(--text-main);
  cursor: pointer;
  min-height: 36px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.btn-icon-order:disabled {
  opacity: 0.35;
  cursor: not-allowed;
}

.btn-icon-delete:hover {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  border-color: #ef4444;
}

/* Quick Preset Chips */
.preset-chips-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 8px;
}

.chip-btn {
  padding: 6px 12px;
  border-radius: 20px;
  border: 1px solid var(--surface-border);
  background: var(--bg-color);
  color: var(--text-main);
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s ease;
  min-height: 36px;
  display: inline-flex;
  align-items: center;
}

.chip-btn:hover {
  border-color: var(--primary-color, #2563eb);
  background: rgba(37, 99, 235, 0.05);
}

.chip-btn.active {
  background: var(--primary-color, #2563eb);
  color: #ffffff;
  border-color: var(--primary-color, #2563eb);
}

/* Slider Controls */
.slider-control-group {
  margin-top: 14px;
}

.slider-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
}

.slider-header label {
  font-weight: 600;
  font-size: 0.88rem;
  color: var(--text-main);
}

.slider-badge {
  font-weight: 700;
  font-size: 0.84rem;
  padding: 2px 8px;
  border-radius: 6px;
  background: rgba(37, 99, 235, 0.1);
  color: var(--primary-color, #2563eb);
}

.slider-ticks {
  display: flex;
  justify-content: space-between;
  font-size: 0.74rem;
  color: var(--text-muted);
  margin-top: 4px;
}

/* Comparison Stats Grid */
.comparison-stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
  gap: 10px;
  margin: 14px 0;
}

.comp-stat-col {
  display: flex;
  flex-direction: column;
  padding: 10px 12px;
  background: var(--bg-color);
  border: 1px solid var(--surface-border);
  border-radius: 8px;
  text-align: center;
}

.comp-stat-label {
  font-size: 0.76rem;
  color: var(--text-muted);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.comp-stat-val {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--text-main);
  margin-top: 4px;
}

.comp-stat-badge {
  display: inline-block;
  font-size: 0.82rem;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 4px;
  background: rgba(16, 185, 129, 0.15);
  color: #10b981;
  margin-top: 4px;
}

/* Image Previews */
.image-preview-box {
  width: 100%;
  max-height: 380px;
  object-fit: contain;
  border-radius: 8px;
  border: 1px solid var(--surface-border);
  background: #111827;
  margin: 14px 0;
  display: block;
}

/* Image Gallery Grid (PDF to Images) */
.image-gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 14px;
  margin: 16px 0;
}

.image-thumb-card {
  display: flex;
  flex-direction: column;
  background: var(--bg-color);
  border: 1px solid var(--surface-border);
  border-radius: 10px;
  overflow: hidden;
  padding: 10px;
}

.thumb-header {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--text-main);
  margin-bottom: 8px;
}

.thumb-preview-wrap {
  width: 100%;
  height: 200px;
  background: #f3f4f6;
  border-radius: 6px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.thumb-preview {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.thumb-actions {
  margin-top: 10px;
}

/* Color Picker Row */
.color-picker-row {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 6px;
}

.color-picker-row input[type="color"] {
  width: 44px;
  height: 44px;
  border-radius: 8px;
  border: 1px solid var(--surface-border);
  cursor: pointer;
  padding: 2px;
  background: transparent;
}

.color-hex-badge {
  font-family: monospace;
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--text-main);
}

/* Crop Workspace */
.crop-workspace {
  margin: 14px 0;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.crop-canvas-container {
  display: flex;
  justify-content: center;
  background: #1e293b;
  border-radius: 10px;
  padding: 12px;
  overflow: hidden;
}

#imgcrop-canvas {
  max-width: 100%;
  height: auto;
  border-radius: 6px;
  display: block;
}

.crop-slider-controls {
  display: flex;
  flex-direction: column;
  gap: 10px;
  background: var(--bg-color);
  border: 1px solid var(--surface-border);
  border-radius: 10px;
  padding: 12px 14px;
}

/* Download Button Enhancements */
.download-btn {
  font-size: 1.05rem;
  font-weight: 700;
  padding: 14px 20px;
  text-align: center;
  cursor: pointer;
}
'''

with open('tools_pdf_image_css.py', 'w', encoding='utf-8') as f:
    f.write(f'# tools_pdf_image_css.py\nCSS_CODE = r\'\'\'{CSS_CODE}\'\'\'\n')

print("tools_pdf_image_css.py written.")
