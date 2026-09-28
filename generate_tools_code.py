import os
import re

print("Generating clean, robust code for all 10 PDF & Image tools...")

# 1. GENERATE CSS
CSS_CODE = r'''/* ==========================================================================
   PDF & IMAGE TOOLS - MODERN, RESPONSIVE STYLES
   ========================================================================== */

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

/* File Dropzone */
.file-dropzone {
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
}
.file-dropzone:hover, .file-dropzone:focus {
  background: rgba(37, 99, 235, 0.08);
  border-color: #1d4ed8;
  transform: translateY(-1px);
}
.file-dropzone.dragover {
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
  margin-top: 18px;
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
.btn-text-sm {
  background: none;
  border: none;
  color: var(--primary-color, #2563eb);
  font-size: 0.84rem;
  font-weight: 700;
  cursor: pointer;
  padding: 4px 8px;
  border-radius: 6px;
}
.btn-text-sm:hover {
  background: rgba(37, 99, 235, 0.08);
}
.file-item-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
  max-height: 320px;
  overflow-y: auto;
  padding-right: 4px;
}
.file-item-row {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  background: var(--bg-color);
  border: 1px solid var(--surface-border);
  border-radius: 10px;
}
.file-item-idx {
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--text-muted);
  min-width: 18px;
  text-align: center;
}
.file-item-thumb {
  width: 44px;
  height: 44px;
  object-fit: cover;
  border-radius: 6px;
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
  font-size: 0.88rem;
  font-weight: 600;
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
  background: var(--surface-color);
  border: 1px solid var(--surface-border);
  color: var(--text-main);
  border-radius: 6px;
  width: 32px;
  height: 32px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.15s ease;
}
.btn-icon-order:disabled {
  opacity: 0.35;
  cursor: not-allowed;
}
.btn-icon-delete {
  color: #ef4444;
}
.btn-icon-delete:hover {
  background: rgba(239, 68, 68, 0.12);
  border-color: #ef4444;
}

/* Quick Preset Chips */
.quick-preset-chips {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 6px;
  margin-bottom: 12px;
}
.preset-label {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--text-muted);
  margin-right: 4px;
}
.preset-chip {
  background: var(--surface-color);
  border: 1px solid var(--surface-border);
  color: var(--text-main);
  padding: 5px 10px;
  border-radius: 20px;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s ease;
}
.preset-chip:hover {
  border-color: var(--primary-color);
  color: var(--primary-color);
  background: rgba(37, 99, 235, 0.05);
}

/* Slider Controls */
.slider-control-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.slider-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-main);
}
.slider-badge {
  background: rgba(37, 99, 235, 0.1);
  color: var(--primary-color, #2563eb);
  padding: 2px 8px;
  border-radius: 6px;
  font-weight: 700;
  font-size: 0.88rem;
}
.slider-ticks {
  display: flex;
  justify-content: space-between;
  font-size: 0.75rem;
  color: var(--text-muted);
  margin-top: -2px;
}

/* Comparison Stats Grid */
.comparison-stats-grid {
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 14px 10px;
  background: var(--bg-color);
  border: 1px solid var(--surface-border);
  border-radius: 10px;
  gap: 8px;
  text-align: center;
}
.comp-stat-col {
  display: flex;
  flex-direction: column;
  gap: 3px;
  flex: 1;
}
.comp-stat-label {
  font-size: 0.76rem;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.comp-stat-val {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--text-main);
}
.comp-stat-arrow {
  font-size: 1.2rem;
  color: var(--text-muted);
  font-weight: 700;
}
.comp-stat-badge {
  display: inline-block;
  background: rgba(16, 185, 129, 0.12);
  color: #10b981;
  font-size: 1.05rem;
  font-weight: 800;
  padding: 2px 8px;
  border-radius: 6px;
}

/* Image Previews */
.image-preview-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgba(0, 0, 0, 0.03);
  border: 1px solid var(--surface-border);
  border-radius: 10px;
  padding: 12px;
  overflow: hidden;
  max-height: 380px;
}
[data-theme="dark"] .image-preview-wrapper {
  background: rgba(255, 255, 255, 0.02);
}
.image-preview-box {
  max-width: 100%;
  max-height: 340px;
  object-fit: contain;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

/* Image Gallery Grid (PDF to Images) */
.image-gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(170px, 1fr));
  gap: 12px;
  max-height: 480px;
  overflow-y: auto;
  padding-right: 4px;
}
.image-thumb-card {
  background: var(--bg-color);
  border: 1px solid var(--surface-border);
  border-radius: 8px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.thumb-header {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--text-main);
  text-align: center;
}
.thumb-preview-wrap {
  width: 100%;
  height: 140px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0,0,0,0.04);
  border-radius: 6px;
  overflow: hidden;
}
.thumb-preview {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

/* Color Picker Row */
.color-picker-row {
  display: flex;
  align-items: center;
  gap: 12px;
}
.color-picker-row input[type="color"] {
  width: 48px;
  height: 40px;
  padding: 2px;
  border: 1px solid var(--surface-border);
  border-radius: 8px;
  cursor: pointer;
  background: var(--surface-color);
}
.color-hex-badge {
  font-family: monospace;
  font-weight: 700;
  font-size: 0.9rem;
  color: var(--text-main);
}

/* Crop Workspace */
.aspect-ratio-selector {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.aspect-label {
  font-size: 0.84rem;
  font-weight: 700;
  color: var(--text-muted);
}
.aspect-tabs {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}
.aspect-tabs .tab-btn {
  padding: 6px 12px;
  font-size: 0.82rem;
  font-weight: 600;
  border-radius: 8px;
}
.aspect-tabs .tab-btn.active {
  background: var(--primary-color);
  color: #fff;
  border-color: var(--primary-color);
}
.crop-workspace-container {
  display: flex;
  justify-content: center;
  align-items: center;
  background: #111827;
  border-radius: 10px;
  padding: 12px;
  overflow: hidden;
}
.canvas-crop-wrapper {
  max-width: 100%;
  display: flex;
  justify-content: center;
}
#imgcrop-canvas {
  max-width: 100%;
  height: auto;
  border-radius: 6px;
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
.crop-slider-row {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.crop-slider-row label {
  font-size: 0.84rem;
  font-weight: 600;
  color: var(--text-main);
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
