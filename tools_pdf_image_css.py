# tools_pdf_image_css.py
# CSS rules for the 10 PDF & Image tools

CSS_CODE = r'''
/* ==========================================================================
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
}
.file-dropzone:hover, .file-dropzone:focus {
  background: rgba(37, 99, 235, 0.08);
  border-color: #1d4ed8;
  transform: translateY(-1px);
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
.file-summary-icon {
  font-size: 1.8rem;
  flex-shrink: 0;
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
  gap: 8px;
}
.preset-label {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--text-muted);
}
.preset-chip {
  background: var(--bg-color);
  border: 1px solid var(--surface-border);
  color: var(--text-main);
  font-size: 0.82rem;
  font-weight: 600;
  padding: 6px 12px;
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.15s ease;
  min-height: 34px;
  display: inline-flex;
  align-items: center;
}
.preset-chip:hover {
  border-color: var(--primary-color, #2563eb);
  background: rgba(37, 99, 235, 0.06);
}

/* Slider Groups */
.slider-control-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.slider-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.92rem;
}
.slider-badge {
  background: var(--primary-color, #2563eb);
  color: #fff;
  font-size: 0.8rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 12px;
}
.slider-ticks {
  display: flex;
  justify-content: space-between;
  font-size: 0.72rem;
  color: var(--text-muted);
}

/* Comparison Stats Grid */
.comparison-stats-grid {
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 14px;
  background: var(--bg-color);
  border: 1px solid var(--surface-border);
  border-radius: 12px;
  text-align: center;
}
.comp-stat-col {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.comp-stat-label {
  font-size: 0.78rem;
  color: var(--text-muted);
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: 0.5px;
}
.comp-stat-val {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--text-main);
}
.comp-stat-arrow {
  font-size: 1.3rem;
  color: var(--text-muted);
}
.comp-stat-badge {
  display: inline-block;
  background: #10b981;
  color: #ffffff;
  padding: 3px 8px;
  border-radius: 12px;
  font-size: 0.88rem;
  font-weight: 800;
}

/* Image Preview */
.image-preview-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 12px;
  background: repeating-conic-gradient(#e2e8f0 0% 25%, #f8fafc 0% 50%) 50% / 16px 16px;
  border: 1px solid var(--surface-border);
  border-radius: 12px;
  overflow: hidden;
  min-height: 120px;
}
[data-theme="dark"] .image-preview-wrapper {
  background: repeating-conic-gradient(#1e293b 0% 25%, #0f172a 0% 50%) 50% / 16px 16px;
}
.image-preview-box {
  max-width: 100%;
  max-height: 320px;
  object-fit: contain;
  border-radius: 6px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
}

/* Image Gallery Grid (PDF to Images) */
.image-gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 14px;
  margin-top: 14px;
}
.image-thumb-card {
  display: flex;
  flex-direction: column;
  background: var(--bg-color);
  border: 1px solid var(--surface-border);
  border-radius: 10px;
  overflow: hidden;
  padding: 8px;
}
.thumb-header {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--text-main);
  margin-bottom: 6px;
  text-align: center;
}
.thumb-preview-wrap {
  display: flex;
  justify-content: center;
  align-items: center;
  background: var(--surface-color);
  border-radius: 6px;
  height: 160px;
  overflow: hidden;
  margin-bottom: 8px;
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
  gap: 10px;
}
.color-picker-row input[type="color"] {
  width: 44px;
  height: 42px;
  padding: 2px;
  border: 1px solid var(--surface-border);
  border-radius: 8px;
  cursor: pointer;
  background: none;
}
.color-hex-badge {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--text-main);
}

/* Aspect Ratio Selector */
.aspect-ratio-selector {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.aspect-label {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--text-main);
}
.aspect-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

/* Crop Workspace */
.crop-workspace-container {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.canvas-crop-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  background: #0f172a;
  border-radius: 12px;
  padding: 8px;
  overflow: hidden;
}
.canvas-crop-wrapper canvas {
  max-width: 100%;
  height: auto;
  border-radius: 6px;
}
.crop-slider-controls {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 12px;
  background: var(--bg-color);
  border: 1px solid var(--surface-border);
  border-radius: 10px;
}
.crop-slider-row {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.crop-slider-row label {
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--text-muted);
}

/* Download Action Button */
.download-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 14px 20px;
  font-size: 1.05rem;
  font-weight: 800;
  text-decoration: none;
  border-radius: 10px;
  text-align: center;
  cursor: pointer;
}
'''
